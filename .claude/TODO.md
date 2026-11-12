# TODO

## Open questions (user)

## Datasheets
- [ ] Get QingKe V5/V3 processor manuals (debug module details for RP-side SDI)
- [ ] Check ADC10065 availability/lifecycle status

## Design
- [ ] Block diagram + full parts list (with JLC availability)
- [ ] Area budget / rough placement to confirm the 63.5 × 88.9 mm outline (D19)
- [ ] RP2350 funprog port (funprog_port.h, bitbang_rvswdio.h — PIO?) + USB HID interface compatible with minichlink pgm-esp32s2-ch32xx
- [ ] (fallback) UART ISP on PB6/PB7 driven by RP2350
- [ ] Power tree incl. standalone power path
- [ ] USB switch part selection for PB8/PB9 (480 Mbps, RP-controlled, default = USB connector)
- [ ] Pin plan: DVP vs UHSIF for ADC10065, ADC/HSADC inputs, SDIO/SDMMC, QSPI, UART, I2C
- [ ] Sample clock source (programmable clock e.g. Si5351?) and ETR wiring
- [ ] Analog front-end: DDS filter, ADC10065 driver, CH32 ADC conditioning
- [ ] Back-feed protection part selection
- [ ] Capture-bus 2:1 switch (ADC10065 ↔ RP2350 counter pattern), ~12 lines, ≥65 MHz, Ioff
- [ ] RP2350 PIO counter-pattern generator: max clock achievable (target ≥65 MHz, ideally up to DVP 150 MHz)
