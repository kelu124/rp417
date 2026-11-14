# TODO

## Open questions (user)

## Datasheets
- [ ] Add RP2350 datasheet (verify I2C GPIO mapping used in D66)
- [ ] Get QingKe V5/V3 processor manuals (debug module details for RP-side SDI)

## Design
- [ ] Verify pinouts taken from datasheets/LCSC: TPS22918, ADC10065 D0–D9 order, TF-01A CD pin 9, SN74CBTLV3257
- [ ] KiCad schematic rev A (from design page §1–§8), then placement + routing
- [ ] Hardware: JPEG-mode continuous DVP capture with static HSYNC is gapless (D37; RM supports it)
- [ ] Hardware: measure CH32 temperature at full USB3 load (D25; estimate +20–25 °C)
- [ ] Order/reserve early: RP2354B, AOTA-B201610S3R3 inductor (thin JLC stock)
- [ ] LC filter values (5th order, fc ≈ 30 MHz, 50 Ω) — L now 470 nH (D68): re-check C values / corner on the bench
- [ ] Compare LCSC QFN88 footprint with WCH drawing
- [ ] Bench-check Si5351 → LC filter amplitude into ADC10065 (P2-2)
- [ ] RP2350 funprog port (funprog_port.h, bitbang_rvswdio.h — PIO?) + USB HID interface compatible with minichlink pgm-esp32s2-ch32xx
- [ ] (fallback) UART ISP on PB6/PB7 driven by RP2350
- [ ] Power tree incl. standalone power path
- [ ] Sample clock source (programmable clock e.g. Si5351?) and ETR wiring
- [ ] Analog front-end: Si5351 LC filter, input-select header, CH32 ADC stimulus (P2-2..P2-4)

## Parked
- [ ] UHSIF: revisit as a test target (RP2350 PIO master, or FPGA connector) — D21
