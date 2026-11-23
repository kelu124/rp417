// rp417 supervisor console on USB CDC0. Commands: see cmd_help() / fw/README.md.
#include "console.h"
#include "board.h"
#include "chlink.h"
#include "programmer.h"
#include "si5351.h"

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pico/stdlib.h"
#include "pico/bootrom.h"
#include "hardware/gpio.h"
#include "tusb.h"

#define FW_VERSION "0.1"
#define CDC_CONSOLE 0

static char line[128];
static size_t line_len;

static void cmd_help(void)
{
	printf("rp417 supervisor " FW_VERSION "\n"
	       "  status                      board state\n"
	       "  vmon                        VSYS and +3V3_CH\n"
	       "  pwr on|off|cycle [ms]       CH32 domain (D25/D29 sequence)\n"
	       "  rst [ms] | rst hold|release CH32 NRST\n"
	       "  usbsel usb|swd              PB8/PB9 -> J1 or RP programmer\n"
	       "  capsel adc|rp               DVP bus source\n"
	       "  si <0|1|2> <hz|off>         Si5351 output; si phase <0|1> <n>; si reg <n>\n"
	       "  freq [gpio] [gate_ms]       count edges (default MCO GPIO34, 100 ms)\n"
	       "  ch <line>                   send a command to the CH32 (fw/PROTOCOL.md)\n"
	       "  swd                         probe the CH32 debug module\n"
	       "  selftest                    bring-up tests\n"
	       "  bootsel                     reboot the RP into its USB bootloader\n");
}

static void cmd_status(void)
{
	printf("ch32 power %s  +3V3_CH %.2f V  VSYS %.2f V\n", ch_power_is_on() ? "on" : "off",
	       adc_v3v3ch(), adc_vsys());
	printf("usb_sel %s  cap_sel %s  programmer %s\n", usb_sel_is_swd() ? "swd" : "usb",
	       gpio_get_out_level(PIN_CAP_SEL) ? "rp" : "adc", prog_is_attached() ? "attached" : "idle");
	printf("si5351 reg0 %d  clk0 %lu  clk1 %lu  clk2 %lu  oe %x\n", si5351_read_reg(0),
	       (unsigned long)si5351_get_freq(0), (unsigned long)si5351_get_freq(1),
	       (unsigned long)si5351_get_freq(2), si5351_output_mask());
}

// ---------------------------------------------------------------- selftest
static int fails;

static void check(const char *name, bool ok, const char *fmt, ...)
{
	char detail[96] = "";
	va_list ap;
	va_start(ap, fmt);
	vsnprintf(detail, sizeof detail, fmt, ap);
	va_end(ap);
	printf("%-28s %s  %s\n", name, ok ? "PASS" : "FAIL", detail);
	if (!ok) fails++;
}

static void logic_rp_drive(int v)
{
	for (int i = 0; i < 8; i++) {
		gpio_init(PIN_LOGIC_BASE + i);
		gpio_put(PIN_LOGIC_BASE + i, (v >> i) & 1);
		gpio_set_dir(PIN_LOGIC_BASE + i, GPIO_OUT);
	}
}

static void logic_rp_release(void)
{
	for (int i = 0; i < 8; i++) {
		gpio_init(PIN_LOGIC_BASE + i);
		gpio_set_dir(PIN_LOGIC_BASE + i, GPIO_IN);
		gpio_disable_pulls(PIN_LOGIC_BASE + i);
	}
}

static int logic_rp_read(void)
{
	int v = 0;
	for (int i = 0; i < 8; i++) v |= gpio_get(PIN_LOGIC_BASE + i) << i;
	return v;
}

static void selftest(void)
{
	char d[96];
	fails = 0;
	printf("--- rp417 selftest\n");

	float vs = adc_vsys();
	check("VSYS 4.4..5.5 V", vs > 4.4f && vs < 5.5f, "%.2f V", vs);

	int r = ch_power_off();
	float v = adc_v3v3ch();
	check("CH32 off: rail < 0.3 V", r == 0, "%.2f V", v);
	r = ch_power_on();
	v = adc_v3v3ch();
	check("CH32 on: rail > 3.0 V", r == 0, "%.2f V", v);

	// CH32 boot: retry ping for ~1 s (blank chip or no firmware -> FAIL here)
	int ok = -2;
	for (int i = 0; i < 10 && ok; i++) ok = ch_cmd("ping", d, sizeof d, 100);
	check("CH32 UART ping", ok == 0 && !strcmp(d, "pong"), "%s", ok == 0 ? d : "no answer");
	if (ok) {
		printf("CH32 firmware not answering: skipping CH32-side tests (flash it: minichlink, fw/README.md)\n");
	} else {
		ch_cmd("ver", d, sizeof d, 200);
		printf("    %s\n", d);

		ch_cmd("mco hse", NULL, 0, 200);
		uint32_t f = freq_measure(PIN_MCO, 100);
		check("MCO = HSE 25 MHz +/-0.1%", f > 24975000 && f < 25025000, "%lu Hz", (unsigned long)f);

		// LOGIC0..7, RP -> CH32
		ch_cmd("lz", NULL, 0, 200);
		static const uint8_t pats[] = { 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x55, 0xaa, 0x00, 0xff };
		int bad = 0, got = 0;
		for (unsigned i = 0; i < sizeof pats; i++) {
			logic_rp_drive(pats[i]);
			sleep_us(50);
			if (ch_cmd("lin", d, sizeof d, 200) || sscanf(d, "logic %x", &got) != 1 || got != pats[i]) {
				bad = 1;
				break;
			}
		}
		logic_rp_release();
		check("LOGIC0..7 RP->CH32", !bad, bad ? "pattern mismatch (got %02x)" : "12 patterns", got);

		// LOGIC0..7, CH32 -> RP
		bad = 0;
		for (unsigned i = 0; i < sizeof pats; i++) {
			snprintf(d, sizeof d, "lout %02x", pats[i]);
			ch_cmd(d, NULL, 0, 200);
			sleep_us(50);
			got = logic_rp_read();
			if (got != pats[i]) { bad = 1; break; }
		}
		ch_cmd("lz", NULL, 0, 200);
		check("LOGIC0..7 CH32->RP", !bad, bad ? "pattern mismatch (got %02x)" : "12 patterns", got);

		// HSYNC / VSYNC (RP -> CH32)
		bad = 0;
		for (int s = 0; s < 4; s++) {
			gpio_init(PIN_HSYNC);
			gpio_init(PIN_VSYNC);
			gpio_put(PIN_HSYNC, s & 1);
			gpio_put(PIN_VSYNC, (s >> 1) & 1);
			gpio_set_dir(PIN_HSYNC, GPIO_OUT);
			gpio_set_dir(PIN_VSYNC, GPIO_OUT);
			sleep_us(50);
			int h = -1, vv = -1;
			if (ch_cmd("sync", d, sizeof d, 200) || sscanf(d, "hsync %d vsync %d", &h, &vv) != 2 ||
			    h != (s & 1) || vv != ((s >> 1) & 1))
				bad = 1;
		}
		gpio_set_dir(PIN_HSYNC, GPIO_IN);
		gpio_set_dir(PIN_VSYNC, GPIO_IN);
		check("HSYNC/VSYNC RP->CH32", !bad, "");

		// MARK (CH32 -> RP)
		gpio_init(PIN_MARK);
		ch_cmd("mark 1", NULL, 0, 200);
		sleep_us(50);
		int m1 = gpio_get(PIN_MARK);
		ch_cmd("mark 0", NULL, 0, 200);
		sleep_us(50);
		int m0 = gpio_get(PIN_MARK);
		ch_cmd("mark z", NULL, 0, 200);
		check("MARK CH32->RP", m1 == 1 && m0 == 0, "hi %d lo %d", m1, m0);
	}

	int st = si5351_read_reg(0);
	check("Si5351 on I2C0 (0x60)", st >= 0 && !(st & 0x80), "status %02x", st);

	int opmode;
	uint32_t dm;
	r = prog_probe(&opmode, &dm);
	check("CH32 debug module (SWD)", r == 0, "r %d mode %s dmstatus %08lx", r,
	      opmode == 1 ? "SWIO" : opmode == 2 ? "RVSWD" : "-", (unsigned long)dm);
	usb_sel_swd(false);

	printf("--- %d failure(s)\n", fails);
	board_led(fails ? LED_R : LED_G);
}

// ---------------------------------------------------------------- dispatcher
static void run(char *s)
{
	char raw[sizeof line];
	snprintf(raw, sizeof raw, "%s", s);
	char *cmd = strtok(s, " \t");
	if (!cmd) return;
	char *a1 = strtok(NULL, " \t");
	char *a2 = strtok(NULL, " \t");

	if (!strcmp(cmd, "help") || !strcmp(cmd, "?")) cmd_help();
	else if (!strcmp(cmd, "status")) cmd_status();
	else if (!strcmp(cmd, "vmon")) printf("VSYS %.3f V  +3V3_CH %.3f V\n", adc_vsys(), adc_v3v3ch());
	else if (!strcmp(cmd, "pwr") && a1) {
		int r = 0;
		if (!strcmp(a1, "on")) r = ch_power_on();
		else if (!strcmp(a1, "off")) r = ch_power_off();
		else if (!strcmp(a1, "cycle")) {
			r = ch_power_off();
			sleep_ms(a2 ? atoi(a2) : 100);
			r |= ch_power_on();
		} else { printf("?\n"); return; }
		printf("%s  +3V3_CH %.2f V\n", r ? "rail check FAILED" : "ok", adc_v3v3ch());
	} else if (!strcmp(cmd, "rst")) {
		if (a1 && !strcmp(a1, "hold")) ch_reset_hold(true);
		else if (a1 && !strcmp(a1, "release")) ch_reset_hold(false);
		else ch_reset_pulse(a1 ? atoi(a1) : 10);
		printf("ok\n");
	} else if (!strcmp(cmd, "usbsel") && a1) {
		usb_sel_swd(!strcmp(a1, "swd"));
		printf("usb_sel %s\n", usb_sel_is_swd() ? "swd" : "usb");
	} else if (!strcmp(cmd, "capsel") && a1) {
		cap_sel_rp(!strcmp(a1, "rp"));
		printf("ok\n");
	} else if (!strcmp(cmd, "si") && a1) {
		if (!strcmp(a1, "phase") && a2) {
			char *a3 = strtok(NULL, " \t");
			printf("%s\n", si5351_set_phase(atoi(a2), a3 ? atoi(a3) : 0) ? "err" : "ok");
		} else if (!strcmp(a1, "reg") && a2) {
			printf("reg %d = %d\n", atoi(a2), si5351_read_reg(atoi(a2)));
		} else if (a2) {
			uint32_t hz = strcmp(a2, "off") ? strtoul(a2, NULL, 0) : 0;
			int r = si5351_set_freq(atoi(a1), hz);
			printf(r ? "err %d\n" : "ok\n", r);
		} else printf("?\n");
	} else if (!strcmp(cmd, "freq")) {
		uint pin = a1 ? atoi(a1) : PIN_MCO;
		uint32_t gate = a2 ? atoi(a2) : 100;
		printf("GPIO%u: %lu Hz\n", pin, (unsigned long)freq_measure(pin, gate));
	} else if (!strcmp(cmd, "ch")) {
		// forward everything after "ch " verbatim
		char *buf = strstr(raw, "ch") + 2;
		while (*buf == ' ' || *buf == '\t') buf++;
		char d[96];
		int r = ch_cmd(buf, d, sizeof d, 500);
		if (d[0]) printf("%s\n", d);
		printf("%s\n", r == 0 ? "ok" : r == -1 ? "err" : "timeout");
	} else if (!strcmp(cmd, "swd")) {
		int opmode;
		uint32_t dm;
		int r = prog_probe(&opmode, &dm);
		printf("probe %d  mode %d  dmstatus %08lx\n", r, opmode, (unsigned long)dm);
	} else if (!strcmp(cmd, "selftest")) selftest();
	else if (!strcmp(cmd, "bootsel")) {
		printf("rebooting to BOOTSEL\n");
		sleep_ms(100);
		reset_usb_boot(0, 0);
	} else printf("unknown '%s' (help)\n", cmd);
}

void console_task(void)
{
	while (tud_cdc_n_available(CDC_CONSOLE)) {
		int c = tud_cdc_n_read_char(CDC_CONSOLE);
		if (c < 0) break;
		if (c == '\r' || c == '\n') {
			tud_cdc_n_write_str(CDC_CONSOLE, "\r\n");
			line[line_len] = 0;
			line_len = 0;
			run(line);
			printf("> ");
		} else if ((c == 8 || c == 127) && line_len) {
			line_len--;
			tud_cdc_n_write_str(CDC_CONSOLE, "\b \b");
		} else if (c >= ' ' && line_len < sizeof line - 1) {
			line[line_len++] = (char)c;
			tud_cdc_n_write_char(CDC_CONSOLE, (char)c);
		}
		tud_cdc_n_write_flush(CDC_CONSOLE);
	}
}
