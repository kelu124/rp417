// rp417 RP2354B supervisor — board-level control (power, reset, switches, monitors).
#include "board.h"
#include "si5351.h"

#include "pico/stdlib.h"
#include "hardware/adc.h"
#include "hardware/gpio.h"
#include "hardware/pio.h"
#include "hardware/uart.h"
#include "edgecount.pio.h"

// Every RP GPIO that reaches the CH32 domain (D29): must be high-Z while the CH32 is off.
static const uint8_t ch_pins[] = {
	PIN_UART_TX, PIN_UART_RX, PIN_CH_SDA, PIN_CH_SCL,
	6, 7, 8, 9, 10, 11,                       // QSPI
	12, 13, 14, 15, 16, 17, 18, 19,           // LOGIC0..7
	20, 21, 22, 23, 24, 25, 26, 27, 28, 29,   // counter D0..D9 (through the capture switch)
	PIN_CNT_PCLK, PIN_HSYNC, PIN_VSYNC, PIN_MARK, PIN_MCO,
	PIN_SWIO, PIN_SWCLK,
};

static bool ch_on;

static void pin_input(uint pin)
{
	gpio_init(pin);              // SIO, input, output latch 0
	gpio_set_dir(pin, GPIO_IN);
	gpio_disable_pulls(pin);
}

static void pin_output(uint pin, bool value)
{
	gpio_init(pin);
	gpio_put(pin, value);
	gpio_set_dir(pin, GPIO_OUT);
}

void board_led(uint8_t rgb)
{
	gpio_put(PIN_LED_R, !(rgb & LED_R));
	gpio_put(PIN_LED_G, !(rgb & LED_G));
	gpio_put(PIN_LED_B, !(rgb & LED_B));
}

void ch_lines_release(void)
{
	uart_deinit(uart0);
	for (unsigned i = 0; i < sizeof ch_pins; i++) pin_input(ch_pins[i]);
	// NRST: open-drain emulation, released = input (CH32 has its own pull-up + C36 100 nF)
	pin_input(PIN_CH_NRST);
}

void ch_lines_enable(void)
{
	uart_init(uart0, 115200);
	gpio_set_function(PIN_UART_TX, GPIO_FUNC_UART);
	gpio_set_function(PIN_UART_RX, GPIO_FUNC_UART);
	gpio_pull_up(PIN_UART_RX);   // idle high if the CH32 has PA9 floating (e.g. in reset)
}

void board_init_safe(void)
{
	// LEDs first (active low): red while initialising
	pin_output(PIN_LED_R, 0);
	pin_output(PIN_LED_G, 1);
	pin_output(PIN_LED_B, 1);

	// Switches to their hardware defaults: USB connector, ADC10065 on the DVP bus
	pin_output(PIN_USB_SEL, 0);
	pin_output(PIN_CAP_SEL, 0);
	gpio_disable_pulls(PIN_SAO_SDA);
	gpio_disable_pulls(PIN_SAO_SCL);

	adc_init();
	adc_gpio_init(PIN_ADC_V3V3CH);
	adc_gpio_init(PIN_ADC_VSYS);

	// Si5351: all outputs off (D15 "DDS off"); harmless if the chip does not answer.
	si5351_init();

	// CH32 domain on (D15 standalone default), NRST released
	ch_lines_release();
	pin_output(PIN_CH_PWR_EN, 1);
	ch_on = true;
	sleep_ms(5);
	ch_lines_enable();
}

bool ch_power_is_on(void) { return ch_on; }

int ch_power_off(void)
{
	// D29 order: stop everything that could back-feed, then switch off.
	si5351_output_enable(0x00);
	usb_sel_swd(false);
	cap_sel_rp(false);
	ch_lines_release();
	gpio_put(PIN_CH_PWR_EN, 0);
	ch_on = false;
	// TPS22918 quick output discharge (QOD tied to VOUT): wait for the rail to fall
	for (int i = 0; i < 100; i++) {
		sleep_ms(2);
		if (adc_v3v3ch() < 0.3f) return 0;
	}
	return -1;
}

int ch_power_on(void)
{
	ch_lines_release();
	gpio_put(PIN_CH_PWR_EN, 1);
	ch_on = true;
	for (int i = 0; i < 50; i++) {
		sleep_ms(1);
		if (adc_v3v3ch() > 3.0f) {
			sleep_ms(2);
			ch_lines_enable();
			return 0;
		}
	}
	ch_lines_enable();
	return -1;
}

void ch_reset_hold(bool assert)
{
	if (assert) pin_output(PIN_CH_NRST, 0);
	else pin_input(PIN_CH_NRST);
}

void ch_reset_pulse(uint32_t ms)
{
	ch_reset_hold(true);
	sleep_ms(ms ? ms : 10);
	ch_reset_hold(false);
}

void usb_sel_swd(bool swd)
{
	if (swd && !ch_on) return;          // never connect the RP SWD pins to an unpowered CH32 (D29)
	if (!swd) {
		pin_input(PIN_SWIO);
		pin_input(PIN_SWCLK);
	}
	gpio_put(PIN_USB_SEL, swd);
}

bool usb_sel_is_swd(void) { return gpio_get_out_level(PIN_USB_SEL); }

void cap_sel_rp(bool rp) { gpio_put(PIN_CAP_SEL, rp); }

static float adc_read_v(uint ch)
{
	adc_select_input(ch);
	uint32_t acc = 0;
	for (int i = 0; i < 16; i++) acc += adc_read();
	return (acc / 16.0f) * 3.3f / 4096.0f;   // ADC_AVDD = +3V3 (no external reference)
}

float adc_v3v3ch(void) { return adc_read_v(PIN_ADC_V3V3CH - 40) * 2.0f; }
float adc_vsys(void)   { return adc_read_v(PIN_ADC_VSYS - 40) * (156.0f / 56.0f); }

// ---- frequency counter (PIO1, GPIO base 16 so it can reach GPIO16..47)
uint32_t freq_measure(uint pin, uint32_t gate_ms)
{
	if (pin < 16 || pin > 47 || !gate_ms) return 0;
	PIO pio = pio1;
	static int offset = -1;
	static int sm = -1;
	if (offset < 0) {
		pio_set_gpio_base(pio, 16);
		offset = pio_add_program(pio, &edgecount_program);
		sm = pio_claim_unused_sm(pio, true);
	}
	pio_sm_config c = edgecount_program_get_default_config(offset);
	sm_config_set_in_pins(&c, pin);
	pio_sm_init(pio, sm, offset, &c);
	pio_sm_exec(pio, sm, pio_encode_mov_not(pio_x, pio_null));   // X = 0xffffffff
	pio_sm_set_enabled(pio, sm, true);
	sleep_ms(gate_ms);
	pio_sm_set_enabled(pio, sm, false);
	pio_sm_exec(pio, sm, pio_encode_mov(pio_isr, pio_x));
	pio_sm_exec(pio, sm, pio_encode_push(false, false));
	uint32_t x = pio_sm_get(pio, sm);
	uint32_t edges = 0xffffffffu - x;
	return (uint32_t)((uint64_t)edges * 1000u / gate_ms);
}
