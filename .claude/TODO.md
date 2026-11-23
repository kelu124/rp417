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
- [ ] Hardware: verify the RP2350 funprog port (fw/rp v0.1, D71): SWIO/RVSWD bit timings, minichlink H41x flash path, USB_SEL handover
- [ ] Hardware: run `selftest` on the first board; check CH32 USART1 baud (ch32fun UART_BRR = SYSCLK/baud) and MCO = 25 MHz
- [ ] Firmware: allocate a real USB PID (pid.codes) to replace the 1209:0001 test PID
- [ ] Firmware: SAO header I2C — GPIO44/45 are on I2C0 like the Si5351 bus (GPIO4/5): use PIO I2C or switch pin functions
- [ ] Firmware v0.2: V5F core, USBHS/USB3 throughput, SD, DVP capture + RP PIO counter, HSADC, I2C/QSPI links
- [ ] (fallback) UART ISP on PA9/PA10 (QFN88, D54; PB6/PB7 are QFN128-only) — fw/rp v0.1 bridges it on CDC1 (`pwr cycle` enters BOOT); verify with WCHISPTool
- [ ] Power tree incl. standalone power path
- [ ] Sample clock source (programmable clock e.g. Si5351?) and ETR wiring
- [ ] Analog front-end: Si5351 LC filter, input-select header, CH32 ADC stimulus (P2-2..P2-4)

## Hardware — next iteration (rev B)
- [ ] **USB ISP entry on J2 (PA11/PA12) is unreachable on a programmed chip** (found 2026-11-23): boot needs DP (PA12)
  high + DM low at power-on, DP must not stay pulled up afterwards (`CH32H417_EVB_Reference_EN.md` §5 tips 1),
  but `J2_DP` has no pull-up and no RP GPIO; the host's 15 kΩ pull-down keeps it low. Only a blank chip enters BOOT.
  SDI (PB8/PB9 via U4) and UART ISP (PA9/PA10) still cover programming, so not blocking for rev A.
  Proposals (to become Pn-m / Dxx):
  - **A (recommended): momentary "USB BOOT" push-button J2_DP → 1 kΩ → +3V3_CH**, next to SW2 (RESET). Hold it while
    the CH32 domain is power-cycled (RP load switch or replug). Momentary = DP never stays pulled up; 1 kΩ vs the host's
    15 kΩ gives ≈ 3.1 V (high), and limits current if D+ is driven. Cost: 1 button + 1 resistor, same parts as SW2/D51.
  - B: 2-pad solder jumper (+ 1 kΩ) instead of the button — cheaper, but must be removed after flashing.
  - C: RP-controlled pull-up (GPIO → 1 kΩ → J2_DP) — fully automatic, but no free RP GPIO left (D66), and a powered RP
    must tri-state it while the CH32 is off (D29 back-feed rule).
- [ ] **No pull-up on SWIO_RP** (found 2026-11-23 writing fw/rp): 1-wire SWIO wants ≈ 1 kΩ to 3V3 (pico-rvd README);
  rev A relies on RVSWD fallback / RP pull-up + precharge (SPEC §9a). Proposal: 1 kΩ SWIO_RP → +3V3 on the RP side of U4.
  Safe for D29 as long as USB_SEL = 1 only while the CH32 is powered (firmware already enforces it).

## Parked
- [ ] UHSIF: revisit as a test target (RP2350 PIO master, or FPGA connector) — D21
