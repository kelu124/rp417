// rp417 RP2354B supervisor — pin map and board-level control.
// Source of truth for the nets: hw/gen/build.py (docs/pinmap.md).
#pragma once
#include <stdbool.h>
#include <stdint.h>
#include "pico/types.h"

// ---- RP <-> CH32 (all through series R, D29)
#define PIN_UART_TX      0   // RP_UART_TX -> R50 220R -> CH32 PA10 (USART1 RX)
#define PIN_UART_RX      1   // RP_UART_RX <- R51 220R <- CH32 PA9  (USART1 TX)
#define PIN_CH_SDA       2   // I2C1 -> R52 100R -> CH32 PB11 (not used in v0.1)
#define PIN_CH_SCL       3   // I2C1 -> R53 100R -> CH32 PB10 (not used in v0.1)
#define PIN_QSPI_BASE    6   // GPIO6..11 -> CH32 QSPI2 (PE10..PE15), not used in v0.1
#define PIN_LOGIC_BASE  12   // GPIO12..19 = LOGIC0..7 (CH32 PD12 PD13 PD14 PD15 PD10 PD11 PC6 PC7)
#define PIN_CNT_BASE    20   // GPIO20..29 = counter D0..D9 (to capture switch B, D55)
#define PIN_CNT_PCLK    30   // counter PCLK (side-set)
#define PIN_HSYNC       31   // -> CH32 PA4 (DVP HSYNC, D37)
#define PIN_VSYNC       32   // -> CH32 PA5 (DVP VSYNC, D37)
#define PIN_MARK        33   // <- CH32 PB14 (shot marker)
#define PIN_MCO         34   // <- CH32 PB0 (MCO)
#define PIN_SWIO        35   // -> U4 2D- -> CH32 PB9 (SWIO/SWDIO) when USB_SEL = 1
#define PIN_SWCLK       36   // -> U4 2D+ -> CH32 PB8 (SWCLK)      when USB_SEL = 1
#define PIN_CH_NRST     37   // -> R83 1k -> CH32 NRST (open-drain emulation: drive low or float)

// ---- board control
#define PIN_MGMT_SDA     4   // I2C0: Si5351A (0x60)
#define PIN_MGMT_SCL     5
#define PIN_CH_PWR_EN   38   // TPS22918 ON, 100k pull-up (CH32 domain ON by default, D15/D25)
#define PIN_USB_SEL     39   // TS3USB221A S: 0 = CH32 PB8/PB9 on J1 (100k pull-down), 1 = RP SWD
#define PIN_ADC_V3V3CH  40   // ADC0: +3V3_CH / 2   (100k/100k)
#define PIN_ADC_VSYS    41   // ADC1: VSYS * 56/156 (100k/56k)
#define PIN_CAP_SEL     42   // 2:1 capture switches: 0 = ADC10065 (pull-down), 1 = RP counter
#define PIN_LED_R       43   // D6, common anode on +3V3 -> active LOW
#define PIN_SAO_SDA     44   // I2C0 alt pins (SAO header J7) — clashes with MGMT on I2C0, unused in v0.1
#define PIN_SAO_SCL     45
#define PIN_LED_G       46
#define PIN_LED_B       47

#define LED_R 1
#define LED_G 2
#define LED_B 4

void board_init_safe(void);          // standalone defaults (D15): CH32 on, NRST released, USB_SEL=USB
void board_led(uint8_t rgb);

// CH32 power domain (D25/D29). Off: tri-state every RP->CH32 line and stop the Si5351 outputs first.
bool ch_power_is_on(void);
int  ch_power_on(void);              // 0 ok, <0 rail did not come up
int  ch_power_off(void);             // 0 ok, <0 rail did not discharge
void ch_lines_release(void);         // every RP->CH32 output to input (high-Z)
void ch_lines_enable(void);          // UART TX back on (others stay inputs until a test drives them)

void ch_reset_pulse(uint32_t ms);
void ch_reset_hold(bool assert);

void usb_sel_swd(bool swd);          // true = PB8/PB9 to the RP programmer
bool usb_sel_is_swd(void);
void cap_sel_rp(bool rp);            // true = RP counter drives the DVP bus

float adc_v3v3ch(void);
float adc_vsys(void);

uint32_t freq_measure(uint pin, uint32_t gate_ms);   // edges per second on a GPIO in 16..47
