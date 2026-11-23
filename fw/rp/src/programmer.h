// funprog programmer glue: USB HID feature reports <-> funprog core, SWD routing via USB_SEL.
#pragma once
#include <stdbool.h>

void prog_attach(void);          // CH32 powered + PB8/PB9 switched to the RP (USB_SEL = 1)
void prog_activity(bool busy);   // called by the core around each command buffer (LED)
void prog_task(void);            // releases PB8/PB9 back to J1 after PROG_IDLE_MS without commands
bool prog_is_attached(void);
#include <stdint.h>
int  prog_probe(int *opmode, uint32_t *dmstatus);   // 0 = debug module answered; opmode 1 SWIO, 2 RVSWD
