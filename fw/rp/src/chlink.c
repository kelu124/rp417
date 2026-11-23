#include "chlink.h"
#include "board.h"

#include <string.h>
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/uart.h"
#include "tusb.h"

#define CDC_BRIDGE 1

static bool busy;

bool chlink_busy(void) { return busy; }

void chlink_set_baud(uint32_t baud)
{
	if (baud >= 1200 && baud <= 3000000) uart_set_baudrate(uart0, baud);
}

void chlink_task(void)
{
	if (busy || !ch_power_is_on()) return;
	// CH32 -> host
	uint8_t buf[64];
	size_t n = 0;
	while (n < sizeof buf && uart_is_readable(uart0)) buf[n++] = uart_getc(uart0);
	if (n && tud_cdc_n_connected(CDC_BRIDGE)) {
		tud_cdc_n_write(CDC_BRIDGE, buf, n);
		tud_cdc_n_write_flush(CDC_BRIDGE);
	}
	// host -> CH32
	while (tud_cdc_n_available(CDC_BRIDGE) && uart_is_writable(uart0)) {
		int c = tud_cdc_n_read_char(CDC_BRIDGE);
		if (c < 0) break;
		uart_putc_raw(uart0, (char)c);
	}
}

int ch_cmd(const char *line, char *data, size_t data_len, uint32_t timeout_ms)
{
	if (!ch_power_is_on()) return -2;
	busy = true;
	while (uart_is_readable(uart0)) (void)uart_getc(uart0);   // drop stale bytes
	uart_puts(uart0, line);
	uart_putc_raw(uart0, '\n');

	char rx[96];
	size_t len = 0;
	int ret = -2;
	if (data && data_len) data[0] = 0;
	absolute_time_t end = make_timeout_time_ms(timeout_ms);

	while (absolute_time_diff_us(get_absolute_time(), end) > 0) {
		tud_task();
		if (!uart_is_readable(uart0)) continue;
		char c = uart_getc(uart0);
		if (c == '\r') continue;
		if (c != '\n') {
			if (len < sizeof rx - 1) rx[len++] = c;
			continue;
		}
		rx[len] = 0;
		len = 0;
		if (!rx[0] || rx[0] == '#') continue;              // blank / event lines
		if (!strcmp(rx, "ok")) { ret = 0; break; }
		if (!strncmp(rx, "err", 3)) {
			if (data && data_len) snprintf(data, data_len, "%s", rx);
			ret = -1;
			break;
		}
		if (data && data_len) snprintf(data, data_len, "%s", rx);
	}
	busy = false;
	return ret;
}
