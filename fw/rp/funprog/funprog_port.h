#ifndef FUNPROG_PORT_H
#define FUNPROG_PORT_H

// rp417 platform glue for the funprog core.
#include <stdio.h>
#include <string.h>
#include "pico/stdlib.h"
#include "hardware/sync.h"
#include "../src/board.h"
#include "../src/programmer.h"

#if DEBUG_PRINT
#define FUN_PRINTF_DEBUG(format, args...) printf(format, ##args)
#else
#define FUN_PRINTF_DEBUG(format, args...)
#endif

#define STATUS_LED_ON  prog_activity(true)
#define STATUS_LED_OFF prog_activity(false)

// "Target power" = the CH32 domain load switch (D25). POWER_SETUP runs before every attach:
// it routes PB8/PB9 to the RP (USB_SEL = 1), powering the CH32 first if needed.
#define POWER_SETUP prog_attach()
#define POWER_ON    do { ch_power_on(); prog_attach(); } while (0)
#define POWER_OFF   ch_power_off()

#define DELAY_US(n) busy_wait_us_32(n)
#define DELAY_MS(n) sleep_ms(n)

#define SLOW_DOWN_PROTOCOL

// Code runs from flash through XIP cache; the bit loops are short. Put them in RAM to keep timing stable.
#define IRAM __attribute__((section(".time_critical.funprog")))

static void VendorCommand(const char *buffer, unsigned short len)
{
	(void)buffer;
	(void)len;
}

#endif
