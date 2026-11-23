// RP <-> CH32 USART link (fw/PROTOCOL.md). The UART is normally bridged to USB CDC1; a command
// issued by the RP itself (console 'ch', selftest) takes the UART over until the reply ends.
#pragma once
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

// Send one command line, collect reply lines until "ok"/"err ...".
// Returns 0 on ok, -1 on err, -2 on timeout. 'data' gets the last non-status line (may be NULL).
int ch_cmd(const char *line, char *data, size_t data_len, uint32_t timeout_ms);

void chlink_task(void);           // UART <-> CDC1 bridge pump
bool chlink_busy(void);
void chlink_set_baud(uint32_t baud);
