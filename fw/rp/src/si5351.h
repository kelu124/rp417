// Si5351A-B-GT driver (I2C0 MGMT bus, address 0x60, 25 MHz crystal Y1 with 10 pF load).
// CLK0 -> ADC10065 CLK, CLK1 -> DVP PCLK path (both PLLA, D32), CLK2 -> generator LC filter (PLLB, D31/D33).
#pragma once
#include <stdbool.h>
#include <stdint.h>

int  si5351_init(void);                        // 0 ok, <0 no ACK (outputs left disabled)
int  si5351_set_freq(int clk, uint32_t hz);    // 0 ok; 0 Hz = power the output down
uint32_t si5351_get_freq(int clk);             // last programmed value (0 = off)
void si5351_output_enable(uint8_t mask);       // bit n = CLKn enabled
uint8_t si5351_output_mask(void);
int  si5351_set_phase(int clk, uint8_t steps); // CLK0/CLK1 phase offset, in units of 1/(4*f_vco)
int  si5351_read_reg(uint8_t reg);
