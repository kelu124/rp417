// rp417 board: RP2354B (RP2350B die + 2 MB in-package flash), 12 MHz crystal (D47).
// Pin assignment: docs/pinmap.md / hw/gen/build.py. Only SDK-level defaults here; the firmware's own
// pin map is fw/rp/src/board.h.

#ifndef _BOARDS_RP417_H
#define _BOARDS_RP417_H


#define RP417

// QFN80 package: 48 GPIO
#define PICO_RP2350A 0

// No default UART/LED/I2C/SPI: every pin is spoken for (board.h). stdio goes to USB CDC 0.

#define PICO_BOOT_STAGE2_CHOOSE_W25Q080 1
#ifndef PICO_FLASH_SPI_CLKDIV
#define PICO_FLASH_SPI_CLKDIV 2
#endif
#ifndef PICO_FLASH_SIZE_BYTES
#define PICO_FLASH_SIZE_BYTES (2 * 1024 * 1024)
#endif

#ifndef PICO_RP2350_A2_SUPPORTED
#define PICO_RP2350_A2_SUPPORTED 1
#endif

#endif
