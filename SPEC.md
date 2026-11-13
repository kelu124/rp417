# rp417 — CH32H417 test board supervised by an RP2350

Status: **rev A schematic + draft layout in `hw/`** (last update 2026-11-13)

All decisions are logged in `DECISIONS.md` (Dxx IDs).
Block diagrams (mermaid), pin plans, BOM and area budget: `docs/design/block-diagram.html` (rev A, redrawn 2026-11-13
for D22–D42; open points listed there as P3).

## 0. Guiding constraint (D22)

**As simple as possible, minimal BOM.** Every part must earn its place: prefer firmware, CH32/RP2350
on-chip resources, fewer rails and fewer connectors over extra ICs. Pending proposals are re-evaluated
against this, and earlier decisions may be revisited where they cost many parts.

## 1. Intent

A dev board to push the CH32H417 to its limits (USB3 throughput, parallel capture,
ADC rates, SD/SDIO) with **automated tests**: the RP2350 acts as supervisor/test
fixture, both chips are connected to the host PC over USB, so a PC script can
power, reset, flash, stimulate and measure the CH32 without manual intervention.

The board must also work **without the RP2350** (CH32 standalone).

## 2. Requirements (as stated by the user)

| # | Requirement | Status |
|---|-------------|--------|
| R1 | RP2350 controls CH32 power and reset | agreed |
| R2 | RP2350 programs the CH32 | **decided: minichlink + RP2350 "funprog" programmer** — see §4 |
| R3 | CH32 USB3 (SuperSpeed) connector + a USB2 connection | agreed — see §5 (shared-USB-C idea dropped) |
| R4 | RP2350 ↔ CH32 links: UART, I2C, QSPI, plus GPIO "logic" lines | agreed — QSPI: CH32 is master-only (RM V1.8 ch. 37: flash interface, no slave mode) → RP PIO slave (D38) ✅ |
| R5 | CH32 SD card via SDIO/SDMMC | agreed |
| R6 | ADC10065 (10-bit, 65 MSPS) parallel output into the CH32 | agreed — purpose: **data throughput** tests; CH32-only, jumper-selected input (D30) |
| R7 | Signal generator piloted by the RP2350, feeding the ADC10065 | **changed (D31): AD9851 dropped, Si5351 filtered output** |
| R8 | A stimulus also feeds the CH32's own ADCs: 12-bit ADC (5 MSPS) **and** 10-bit HSADC (20 MSPS) | agreed — fed from the generator / external net (D35) |
| R9 | Back-feeding protection on both chips (power rails and I/O) | agreed — see §6 |
| R10 | Board usable without the RP2350's USB host link (RP2350 is **permanently on board**) | **decided** — see §7 |
| ~~R11~~ | ~~On-board WCH-LinkE~~ | **removed for now** (2026-11-12) |

## 3. Verified CH32H417 facts that drive the design

Source: `datasheets/CH32H417DS0_V1.9_en.md` (V1.9; was checked on V1.4 first), `datasheets/CH32H417RM_V1.8_en.md`, `datasheets/CH32H417_EVB_Reference_EN.md`,
`datasheets/CH32H417_UHSIF_RM_EN.md`.

- **Package: CH32H417MEU6 (QFN88, 10 × 10 mm, 0.4 mm pitch)** (D54, user-supplied; supersedes the QFN128 choice D12).
  BOOT/ISP: QFN128 + QFN88 yes, QFN68 (WEU) **no** (`CH32H417_EVB_Reference_EN.md` §ISP table). QFN88 UART ISP = **PA9/PA10**.
  QFN88 lacks PE2, PE7, PF13, PA6, PA8, PB6, PB7, VREFP, VBAT (DS V1.9 pin table).
- **Lot number:** DS V1.4 said lot-digit-5 = 0 parts lack GPHA/Ethernet/SerDes/CAN; **V1.9 no longer says so**.
  The EVB reference still says WCHISPTool download needs digit 5 ≠ 0 → check on receipt.
- **No BOOT0 pin.** Bootloader entry (56 KB system flash):
  - USB ISP on **USBFS PA11 (DM) / PA12 (DP)**: at power-on, DP high + DM low ⇒ BOOT mode.
    DP must not stay pulled up afterwards.
  - UART ISP on **PB6 (TX) / PB7 (RX)** on QFN128, **PA9 (TX) / PA10 (RX) on QFN88 (our part)**, "key-free": tool waits, power-cycle enters BOOT.
    Needs an option bit enabled (factory default: enabled).
  - Blank chip enters BOOT automatically.
  ⇒ **controlling CH32 power is itself the programming mechanism.**
- **Debug (SDI):** 1-wire SWIO (default) or 2-wire SWDIO/SWCLK.
  **PB9 = SWIO/SWDIO/USBHS_DM and PB8 = SWCLK/USBHS_DP** — the debug pins *are* the USB2
  high-speed pins. The WCH EVB routes them to both the USB connector and the SWD header.
- Three USB controllers: **USBSS** (5 Gbps, SSTX/SSRX A/B, polarity swap supported),
  **USBHS** (480 Mbps, PB8/PB9), **USBFS** (12 Mbps, PA11/PA12, also OTG).
- **DVP:** 8/10/12-bit, PCLK up to 150 MHz, VSYNC/HSYNC sync. ADC10065 at 65 MHz → fits.
  RM §29: 10/12-bit samples are zero-extended to 16 bit (65 MSPS ⇒ 130 MB/s); lines alternate
  between DMA BUF0/BUF1 (COL_NUM samples per line, ROW_NUM lines per frame); snapshot or
  continuous mode (RB_DVP_CM). Gapless line-to-line capture still to be proven (counter test, D16).
- **UHSIF:** 8/16/24/32-bit, clock ≤125 MHz (derived from SYSCLK), 500 MB/s theoretical,
  pins UHSIF_PORT[47:0]. Alternative capture path.
- **ADC:** 2 × 12-bit, up to 5 MSPS, 16 ext channels. **HSADC:** 10-bit, 20 MSPS, 7 channels
  (HSADC_IN0..6). PC0..PC3 are both ADC_IN10..13 *and* HSADC_IN0..3 → one conditioned DDS
  signal can reach both converters (but PC0..PC3 are also UHSIF pins).
- **SRAM 896 KB:** 128 KB ITC + 256 KB DTCM (core V5) + 512 KB shared. Buffer budget for streaming.
- Timers are STM32-style (TIM1 ETR on PE7/PA12) → ADC clock can be counted by a timer.
- VDDA/VREF: ≥3.0 V recommended when using HSADC.

Claims from `userinputs/tocheck.md` — checked:
| Claim | Verdict |
|-------|---------|
| UHSIF 32-bit, 125 MHz, 500 MB/s | ✅ datasheet + UHSIF manual |
| DVP max 12-bit @ 150 MHz | ✅ |
| 896 KB SRAM | ✅ (split, see above) |
| USB3 measured ~450 MB/s | ⚠️ marketing/EVB figure, not in datasheet — to measure ourselves |
| WeAct LA 16 ch @ 200 MHz uses UHSIF | ❓ unverifiable (closed firmware); not needed for us |
| Timer ETR external clock / one-pulse mode | ✅ ETR pins exist; details need the Reference Manual |
| DVP continuous gapless capture | ⚠️ RM: continuous mode + BUF0/BUF1 ping-pong per line exists; gapless across line/frame boundaries to prove with the counter test |

## 4. Programming the CH32 (R2) — decided 2026-11-12

**Primary: minichlink on the host, RP2350 as the programmer.**
- ch32fun's `minichlink` already knows the CH32H417 (`chips.c`: model 0x4170, flash 960 KB @0x08000000,
  bootloader 56 KB @0x1FFF0000, options @0x1FFFF800, RAM 896 KB @0x200A0000).
- minichlink supports "funprog" programmers: a portable core (`minichlink/funprog/`:
  `funprog_rvswdio.h` + `funprog_logic.h`) that bit-bangs **both 1-wire SWIO and 2-wire RVSWD**.
  Existing ports: ESP32-S2, CH32V003, CH570. Host side: `pgm-esp32s2-ch32xx.c` (USB HID).
- RP2350 firmware = a funprog port (`funprog_config.h`, `funprog_port.h`, `bitbang_rvswdio.h`,
  possibly PIO-based) exposed as one interface of the RP2350's composite USB device, next to
  the test-control interface. ch32fun included as a git submodule.
- Wiring: SWIO/SWDIO = PB9, SWCLK = PB8 (shared with USBHS — via the USB switch, §5), plus NRST.
- ⚠️ To verify on hardware: funprog + H41x flash path (minichlink lists the chip, no H417 report seen yet).

**Fallback: bootloader ISP** (no debugger needed) — RP2350 power-cycles the CH32 and talks the WCH
UART ISP protocol on PA9/PA10 (QFN88, D54), or forces USBFS DP high at power-on for USB ISP (note: `wchisp` has
no H41x device file yet; WCHISPTool does support it).

## 5. USB

- **J1 – CH32 USB3** USB-C: SS pairs + USBHS D+/D− (PB8/PB9). **Single-orientation SS** (D27): no orientation mux; one plug
  orientation gives USB3, the flipped one USB2 only. CC1/CC2 = 5.1 kΩ Rd. (CH32 USBSS has one TX/RX pair with P/N swap only,
  RM V1.8 `RB_LINK_SS_PLR`.)
- **J2 – CH32 USBFS** USB-C (PA11/PA12): ISP port, second USB2 device — kept (D40).
- ESD (D45): USBLC6-2SC6 on J1/J2/J3 D±; RClamp0524PATCT (0.3 pF) on the J1 SS pairs.
- **J3 – RP2350** USB-C.
- **Decided 2026-11-12** (SDI programming shares PB8/PB9): a 480 Mbps-capable analog switch on PB8/PB9
  (RP-controlled, TS3USB221A — D26) to select USB-connector ↔ RP2350 SWD. Default (unpowered/RP absent) = USB. Doubles as a
  software "unplug" for USBHS tests.

## 6. Back-feeding protection (R9) — method D29 (supersedes D08 method)

- Power: every VBUS through ideal-diode ORing; nothing back-feeds a port.
  CH32 rail behind an RP-controlled load switch with quick output discharge (D25).
- I/O: **no bus switches / I2C buffer** (D29). The RP2350 is always powered (D13/D15), so the only back-feed direction is
  RP→CH32. RP firmware tri-states every line to the CH32 and disables the Si5351 outputs (ADC clock, PCLK, test signal)
  **before** switching the CH32 domain off. Series resistors on every RP↔CH32 and clock line limit clamp current if
  firmware fails. I2C pull-ups on the CH32 rail. NRST open-drain. PB8/PB9 isolated by the TS3USB221A.
- ADC10065 in the CH32 switched domain, connected only to the CH32 (D30).
- Monitoring: RP2350 ADC on the CH32 3V3 rail and VSYS (D28, no INA3221); the CH32 rail must read ~0 V when off.

## 6a. Power tree (D25)

- VSYS 5 V (ORed VBUS) → **one always-on 3V3 buck** → RP2354B, Si5351A, TS3USB221A.
- 3V3 → **CH32-domain load switch** (RP GPIO EN, default ON for standalone D15, quick output discharge) → CH32 VDD33/VDDIO
  (VIO18 tied to VDDIO, D23), microSD, ADC10065 (VDDA 2.7–3.6 V, `datasheets/ADC10065.md`).
- **No external 1V2**: CH32 internal LDO supplies VDDK/VDD12A from VDD33 (`CH32H417DS0_V1.9_en.md` §1.4.3; external
  supply optional, only to reduce heat). Estimate (DS V1.9 Tables 3-6-4/3-6-5): I<sub>DDK</sub> ≈ 112 mA (400/100 MHz, all
  peripherals) + I<sub>DD12A</sub> ≈ 85 mA (USB3) → ≈ 0.4 W in the LDO, ≈ 0.75 W for the chip. No θ<sub>JA</sub> given; at a typical
  25–35 °C/W for QFN128 + stitched pad → +20–25 °C, inside T<sub>J</sub> ≤ 105 °C. ⚠️ Estimate — measure on hardware.
- VDD33A/VREFP: CH32 3V3 via ferrite + caps, no LDO (D39).
- Rail order to respect: VDD33 ≥ VDD33A ≥ VDDIO ≥ VIO18 (DS V1.9 Table 3-2) — satisfied by a single 3V3 rail.

## 7. Standalone mode (R10)

The RP2350 is **permanently on board**; "without the RP2350" means *no host connected to the RP2350's USB*.
Decided 2026-11-12:
- Board power: VBUS of J1 (CH32 USB3), J2 (CH32 USBFS) and J3 (RP2350) only (no external input, D41),
  ORed through ideal diodes → any one cable powers the whole board. RP2350 always powered.
- RP2350 firmware boots into a safe standalone default: CH32 powered, NRST released, USB switch → USB
  connector, DDS off.
- The CH32 can command the RP2350 over UART/I2C (set DDS frequency/waveform, sample clock, power
  measurements), so standalone CH32 tests keep the stimulus side.

## 8. Analog / capture chain (R6–R8)

- **Clocks (D32):** Si5351A CLK0 → ADC10065 CLK; CLK1 (same PLL A, phase-tunable) → capture switch B1 → CH32 PCLK (PB12) + TIM8_ETR (PF2)
  for sample counting; CLK2 (PLL B) → generator. Outputs disabled by the RP before CH32 power-off (D29).
- **Generator (D31, D33):** Si5351 CLK2 → 50 Ω → 5th-order LC low-pass, f<sub>c</sub> ≈ 30 MHz, doubly terminated → ≈ 2 Vpp sine
  (ideal ≈ (4/π)·(3.3/2)·½ ≈ 2 Vpp; Si5351 driver impedance lowers it — estimate 1.5–2 Vpp, ⚠️ bench-verify). Clean sine ≈ 10–30 MHz; below f<sub>c</sub>/3 a shaped square (fine for throughput, D05).
- **Input select (D34):** 1×4 2.54 mm header `GEN | ADC_IN | EXT | GND`; jumper 1–2 = generator, 2–3 = external.
  EXT: 49.9 Ω termination, series R + clamp diodes. GEN + GND = scope probe point (replaces D20).
- **ADC10065 (D30, D42):** **DNP** — user hand-solders their own part. CH32-only, on the CH32 domain. ADC_IN → AC coupling + VCOM bias → VIN+, VIN− tied to VCOM,
  IRS on a 3-way solder jumper, default VDDA = 2.0 Vpp full scale (GND 1.5 / open 1.0 Vpp) (D44, `datasheets/ADC10065.md`). D0–D9 → 33 Ω → capture switch B1 → DVP (D55).
- **CH32 ADC + HSADC (D35):** ADC_IN → series R + AC cap + VDD33A/2 bias → PC0 (ADC_IN10 + HSADC_IN0). No anti-alias
  filter: 10–30 MHz sines alias at 5/20 MSPS (deterministic, fine for throughput).
- **Counter pattern (D55, supersedes D36):** 2:1 capture switch, 3 × SN74CBTLV3257PWR on D0–D9 + PCLK, powered from
  the CH32 domain (Ioff isolation), S = RP GPIO42 `CAP_SEL`, pull-down → ADC10065 by default. One DVP pin set on QFN88:
  D0 PE0, D1 PE1, D2 PB13, D3 PE3, D4 PE4, D5 PF14, D6 PE5, D7 PE6, D8 PF4, D9 PF3, PCLK **PB12** (the only PCLK pin on
  QFN88), HSYNC PA4, VSYNC PA5 (DS V1.9 Table 2-2-23). RP PIO counter = GPIO20–29 (D0–D9) + side-set PCLK GPIO30 → full
  10-bit counter. Sample counter: TIM8_ETR on PF2 (D56).
- **Switch check at 65 MHz** (`datasheets/SN74CBTLV3257.md`, TI SCDS040N, V<sub>CC</sub> 3.3 V, PW package): r<sub>on</sub> 5 Ω typ /
  7 Ω max at V<sub>I</sub> = 0, 10 / 15 Ω at V<sub>I</sub> = 2.4 V; C<sub>io(off)</sub> A ≈ 10.5 pF, B 5.5 pF; t<sub>pd</sub> ≤ 0.25 ns (RC); tested to
  200 MHz; I<sub>off</sub> ≤ 15 µA (partial power-down ✅ for D29). ✅ OK for 65 MHz, but the switch adds ≈ 20 pF to each line:
  with 33 Ω series R the edges slow to ≈ 5–6 ns (10–90 %) → **D57: PCLK 0 Ω, data 22 Ω, switches next to their DVP pins** (≈ 3.5–4.5 ns).
- **Logic bus (D03, D56):** 8 general GPIO, RP GPIO12–19 ↔ CH32 PD12–PD15, PD10, PD11, PC6, PC7 (33 Ω series).
- **Sync (D37):** RP2350 drives HSYNC (PA4) and VSYNC (PA5) in both modes. DVP in JPEG mode: HSYNC may be static,
  buffer switching by DMA length = COL_NUM (RM V1.8 §29.2.2, §29.3.1) → no PCLK alignment needed.
  ⚠️ To verify on hardware: gapless continuous streaming.
- **UHSIF parked** (D21) — not routed on rev A. Notes for later: 8–32 bit, ≤125 MHz from SYSCLK, master/slave handshake
  bus, fixed default pin maps; suited to FPGA/SoC partners, not a raw ADC.

## 9. Board / manufacturing

- KiCad, JLCPCB fab + assembly, 6 layers (D18).
- Outline 63.5 × 88.9 mm (D19). **Area budget (2026-11-13): ≈ 1900 mm² of parts+keep-outs ≈ 34 % of one side** → fits;
  **parts on both sides where it helps** (D48): decoupling, series-R arrays, bias networks, ORing and load switch on the
  bottom; connectors, ICs, crystals, analog and ESD on top. Details + placement sketch: `docs/design/block-diagram.html` §9.
- (Superseded by D54: now QFN88 10 × 10 mm, 0.4 mm pitch, LCSC footprint `QFN-88_L10.0-W10.0-P0.40-BL-EP7.7`.) The QFN128 is 12.3 × 12.3 mm, **0.35 mm pitch** (DS V1.9 ch. 4 package table; confirmed by WCH's own EVB footprint
  `projects/sdk/ch32h417/EVT/PUB/SCHPCB/CH32H417QEU6-R0` "QFN128_12.3X12.3": single row of 32 pads per side, 0.16 × 0.8 mm,
  0.19 mm gap, + exposed pad). Fan-out leaves each pad outward, so ~0.1–0.127 mm traces suffice (no routing between pads);
  check JLC 6-layer pad/solder-mask-dam rules and the stencil for 0.19 mm gaps. Reuse WCH's footprint.
- **Sourcing snapshot 2026-11-13** (JLC parts API, §8 of the design page): **CH32H417QEU6 = 0 stock at JLC** (C49363240) →
  **user-sourced** (D43; consign vs hand-solder to confirm). Thin stock: RP2354B (524), RP2350 SMPS inductor AOTA-B201610S3R3 (143). ADC10065 is DNP (D42; LCSC has 4 + 30).
  Almost every IC/connector is an Extended part. Part selection = design page §8 (D47); genuine Si5351A-B-GTR (D46).

## 10. Open questions

See `.claude/TODO.md`.
