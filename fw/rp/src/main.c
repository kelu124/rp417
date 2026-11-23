// rp417 RP2354B supervisor firmware v0.1
//
// USB composite device:
//   CDC0  console (help / status / pwr / si / selftest ...), printf goes here
//   CDC1  transparent bridge to the CH32 USART1 (baud follows the host's line coding)
//   HID   funprog programmer for minichlink (`minichlink -c 0x12090001 -C funprog -w fw.bin flash -b`)
// Boot state = standalone defaults (D15): CH32 domain on, NRST released, USB_SEL = J1, Si5351 off.
#include "board.h"
#include "chlink.h"
#include "console.h"
#include "programmer.h"

#include "pico/stdlib.h"
#include "pico/stdio/driver.h"
#include "pico/bootrom.h"
#include "tusb.h"

// ---- stdio -> CDC0
static void cdc0_out_chars(const char *buf, int len)
{
	if (!tud_cdc_n_connected(0)) return;
	for (int i = 0; i < len; i++) {
		if (buf[i] == '\n') tud_cdc_n_write_char(0, '\r');
		tud_cdc_n_write_char(0, buf[i]);
		if (!tud_cdc_n_write_available(0)) {
			tud_cdc_n_write_flush(0);
			for (int t = 0; t < 1000 && !tud_cdc_n_write_available(0); t++) {
				tud_task();
				sleep_us(10);
			}
		}
	}
	tud_cdc_n_write_flush(0);
}

static stdio_driver_t cdc0_stdio = {
	.out_chars = cdc0_out_chars,
	.crlf_enabled = false,
};

// ---- line coding: 1200 baud on CDC0 = reboot to BOOTSEL (picotool/Arduino convention);
//      CDC1 baud is applied to the CH32 UART (e.g. for the WCH UART ISP fallback).
void tud_cdc_line_coding_cb(uint8_t itf, cdc_line_coding_t const *coding)
{
	if (itf == 0 && coding->bit_rate == 1200) reset_usb_boot(0, 0);
	if (itf == 1) chlink_set_baud(coding->bit_rate);
}

int main(void)
{
	board_init_safe();
	tusb_init();
	stdio_set_driver_enabled(&cdc0_stdio, true);
	board_led(LED_G);

	while (true) {
		tud_task();
		console_task();
		chlink_task();
		prog_task();
	}
}
