# TODO

## Open questions (user)
- [ ] P2-8: drop the external 5 V input (3 × LM66100 instead of 4)?

## Datasheets
- [ ] Get QingKe V5/V3 processor manuals (debug module details for RP-side SDI)
- [ ] Check ADC10065 availability/lifecycle status

## Design
- [ ] RM: confirm DVP takes data only from the AF-selected pin set (D36)
- [ ] RM/hardware: JPEG-mode continuous DVP capture with static HSYNC is gapless (D37)
- [ ] Redraw block diagram / power tree / pin plans in `docs/design/block-diagram.html` for D22–D31 (freed RP GPIO20–32, 44–47)
- [ ] Verify CH32 internal-LDO dissipation at full USB3 load (D25)
- [ ] Bench-check Si5351 → LC filter amplitude into ADC10065 (P2-2)
- [ ] Full parts list with JLC availability (block diagram + pin plan done: P1)
- [ ] Verify in RM: CH32 QSPI master-only? (P1-10)
- [ ] Area budget / rough placement to confirm the 63.5 × 88.9 mm outline (D19)
- [ ] RP2350 funprog port (funprog_port.h, bitbang_rvswdio.h — PIO?) + USB HID interface compatible with minichlink pgm-esp32s2-ch32xx
- [ ] (fallback) UART ISP on PB6/PB7 driven by RP2350
- [ ] Power tree incl. standalone power path
- [ ] Sample clock source (programmable clock e.g. Si5351?) and ETR wiring
- [ ] Analog front-end: Si5351 LC filter, input-select header, CH32 ADC stimulus (P2-2..P2-4)

## Parked
- [ ] UHSIF: revisit as a test target (RP2350 PIO master, or FPGA connector) — D21
