#ifndef _FUNCONFIG_H
#define _FUNCONFIG_H

// rp417 CH32H417MEU6 — ch32fun configuration
//
// 25 MHz crystal Y2 on XI/XO (hw/gen/build.py) -> HSE, PLL x16 -> 400 MHz (ch32fun H41x default).
#define FUNCONF_USE_HSE 1
#define FUNCONF_USE_HSI 0

// NOT ch32fun's UART printf: on H41x it also turns PA12 into a USART6 TX output, and PA12 is
// J2_DP (USBFS / USB ISP). We run our own USART1 driver on PA9/PA10 (uart.c) instead.
#define FUNCONF_USE_UARTPRINTF 0
#define FUNCONF_USE_DEBUGPRINTF 0

// The V5F core is not started in this first firmware (V3F only, no StartV5F call).

#endif
