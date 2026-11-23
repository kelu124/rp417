// Si5351A driver — register map per Skyworks AN619.
//
// Strategy (D32: CLK0 and CLK1 share PLLA so their phase can be tuned):
//  - when the PLL of the requested output is not used by another active output, pick an even integer
//    MultiSynth divider and a fractional PLL (lowest jitter, exact frequency when the fraction fits);
//  - when the PLL is already in use, keep it and use a fractional MultiSynth divider.
// Range: ~8 kHz (R divider up to 128) .. 150 MHz (MS = 6). VCO 600..900 MHz.

#include "si5351.h"
#include "board.h"

#include "pico/stdlib.h"
#include "hardware/i2c.h"

#define SI_ADDR      0x60
#define SI_XTAL_HZ   25000000u
#define VCO_MIN      600000000ull
#define VCO_MAX      900000000ull
#define FRAC_MAX     1048575u

#define REG_OEB          3
#define REG_CLK_CTRL(n)  (16 + (n))
#define REG_PLLA         26
#define REG_PLLB         34
#define REG_MS(n)        (42 + 8 * (n))
#define REG_PHOFF(n)     (165 + (n))
#define REG_PLL_RESET    177
#define REG_XTAL_CL      183

static i2c_inst_t *const bus = i2c0;
static bool present;
static uint8_t oe_mask;                 // bit n = CLKn enabled
static uint32_t clk_hz[3];
static uint64_t vco_hz[2];              // PLLA, PLLB (0 = not programmed)

static int clk_pll(int clk) { return clk == 2 ? 1 : 0; }

static int wr(uint8_t reg, const uint8_t *data, size_t n)
{
	uint8_t buf[1 + 8];
	if (n > 8) return -1;
	buf[0] = reg;
	for (size_t i = 0; i < n; i++) buf[1 + i] = data[i];
	return i2c_write_timeout_us(bus, SI_ADDR, buf, n + 1, false, 2000) == (int)(n + 1) ? 0 : -1;
}

static int wr1(uint8_t reg, uint8_t v) { return wr(reg, &v, 1); }

int si5351_read_reg(uint8_t reg)
{
	uint8_t v;
	if (i2c_write_timeout_us(bus, SI_ADDR, &reg, 1, true, 2000) != 1) return -1;
	if (i2c_read_timeout_us(bus, SI_ADDR, &v, 1, false, 2000) != 1) return -1;
	return v;
}

static uint64_t gcd64(uint64_t a, uint64_t b)
{
	while (b) { uint64_t t = a % b; a = b; b = t; }
	return a;
}

// value = a + b/c, packed into the 8-byte P1/P2/P3 block (AN619 §3.2 / §4.1.2)
static void pack(uint8_t out[8], uint32_t a, uint32_t b, uint32_t c, uint8_t rdiv_log2)
{
	uint32_t f = (uint32_t)((128ull * b) / c);
	uint32_t p1 = 128 * a + f - 512;
	uint32_t p2 = 128 * b - c * f;
	uint32_t p3 = c;
	out[0] = (p3 >> 8) & 0xff;
	out[1] = p3 & 0xff;
	out[2] = (uint8_t)((rdiv_log2 & 7) << 4) | ((p1 >> 16) & 3);
	out[3] = (p1 >> 8) & 0xff;
	out[4] = p1 & 0xff;
	out[5] = (uint8_t)(((p3 >> 16) & 0xf) << 4) | ((p2 >> 16) & 0xf);
	out[6] = (p2 >> 8) & 0xff;
	out[7] = p2 & 0xff;
}

// num/den -> a + b/c with c <= FRAC_MAX (exact when the reduced fraction fits)
static void ratio(uint64_t num, uint64_t den, uint32_t *a, uint32_t *b, uint32_t *c)
{
	*a = (uint32_t)(num / den);
	uint64_t rem = num % den;
	if (!rem) { *b = 0; *c = 1; return; }
	uint64_t g = gcd64(rem, den);
	rem /= g;
	den /= g;
	if (den <= FRAC_MAX) { *b = (uint32_t)rem; *c = (uint32_t)den; return; }
	*c = FRAC_MAX;
	*b = (uint32_t)((rem * FRAC_MAX + den / 2) / den);
	if (*b >= FRAC_MAX) { *b = 0; (*a)++; }
}

int si5351_init(void)
{
	i2c_init(bus, 400 * 1000);
	gpio_set_function(PIN_MGMT_SDA, GPIO_FUNC_I2C);
	gpio_set_function(PIN_MGMT_SCL, GPIO_FUNC_I2C);   // 4.7k pull-ups R on the board

	present = false;
	oe_mask = 0;
	for (int i = 0; i < 3; i++) clk_hz[i] = 0;
	vco_hz[0] = vco_hz[1] = 0;

	// wait for SYS_INIT to clear (status reg 0 bit 7)
	for (int i = 0; i < 20; i++) {
		int st = si5351_read_reg(0);
		if (st >= 0 && !(st & 0x80)) { present = true; break; }
		sleep_ms(5);
	}
	if (!present) return -1;

	wr1(REG_OEB, 0xff);                                    // all outputs disabled
	for (int n = 0; n < 8; n++) wr1(REG_CLK_CTRL(n), 0x80); // all powered down
	wr1(REG_XTAL_CL, 0xd2);                                // XTAL_CL = 10 pF (bits 7:6 = 11, AN619 reg 183)
	return 0;
}

void si5351_output_enable(uint8_t mask)
{
	oe_mask = mask & 7;
	if (present) wr1(REG_OEB, (uint8_t)~oe_mask);
}

uint8_t si5351_output_mask(void) { return oe_mask; }

uint32_t si5351_get_freq(int clk) { return (clk >= 0 && clk < 3) ? clk_hz[clk] : 0; }

static bool pll_shared(int clk)
{
	for (int o = 0; o < 3; o++)
		if (o != clk && clk_pll(o) == clk_pll(clk) && clk_hz[o]) return true;
	return false;
}

int si5351_set_freq(int clk, uint32_t hz)
{
	if (!present || clk < 0 || clk > 2) return -1;
	if (!hz) {
		wr1(REG_CLK_CTRL(clk), 0x80);
		clk_hz[clk] = 0;
		si5351_output_enable(oe_mask & ~(1u << clk));
		return 0;
	}
	if (hz < 8000 || hz > 150000000) return -2;

	// R divider so that the MultiSynth output is >= 1 MHz
	uint8_t rlog = 0;
	while (((uint64_t)hz << rlog) < 1000000ull && rlog < 7) rlog++;
	uint64_t ms_hz = (uint64_t)hz << rlog;

	int pll = clk_pll(clk);
	uint32_t a, b, c;
	uint8_t regs[8];

	if (!pll_shared(clk) || !vco_hz[pll]) {
		// even integer MultiSynth, fractional PLL
		uint32_t div = (uint32_t)(VCO_MAX / ms_hz);
		if (div & 1) div--;
		if (div < 6) return -2;
		if (div > 1800) div = 1800;
		uint64_t vco = ms_hz * div;
		if (vco < VCO_MIN) return -2;
		ratio(vco, SI_XTAL_HZ, &a, &b, &c);           // PLL multiplier 15..90
		pack(regs, a, b, c, 0);
		wr(pll ? REG_PLLB : REG_PLLA, regs, 8);
		vco_hz[pll] = vco;
		pack(regs, div, 0, 1, rlog);
		wr(REG_MS(clk), regs, 8);
		// PDN=0, MS_INT=1, MS_SRC=pll, CLK_SRC=MS (11), 8 mA
		wr1(REG_CLK_CTRL(clk), 0x40 | (pll ? 0x20 : 0) | 0x0c | 0x03);
		wr1(REG_PLL_RESET, pll ? 0x80 : 0x20);
	} else {
		// PLL in use by the other output: fractional MultiSynth on the existing VCO
		ratio(vco_hz[pll], ms_hz, &a, &b, &c);
		if (a < 8 || a > 2048) return -2;
		pack(regs, a, b, c, rlog);
		wr(REG_MS(clk), regs, 8);
		bool integer = (b == 0) && !(a & 1);
		wr1(REG_CLK_CTRL(clk), (integer ? 0x40 : 0) | (pll ? 0x20 : 0) | 0x0c | 0x03);
	}
	clk_hz[clk] = hz;
	si5351_output_enable(oe_mask | (1u << clk));
	return 0;
}

int si5351_set_phase(int clk, uint8_t steps)
{
	if (!present || clk < 0 || clk > 1) return -1;
	if (wr1(REG_PHOFF(clk), steps & 0x7f)) return -1;
	return wr1(REG_PLL_RESET, 0x20);   // phase offsets apply on PLLA reset
}
