# rp417 — CH32H417 test board supervised by an RP2350

Status: **draft / requirements gathering** (last update 2026-11-12)

All decisions are logged in `DECISIONS.md` (Dxx IDs).
Block diagrams (mermaid) and pin plans: `docs/design/block-diagram.html` (proposal P1, pending approval).

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
| R4 | RP2350 ↔ CH32 links: UART, I2C, QSPI, plus GPIO "logic" lines | agreed |
| R5 | CH32 SD card via SDIO/SDMMC | agreed |
| R6 | ADC10065 (10-bit, 65 MSPS) parallel output into the CH32 | agreed — purpose: **data throughput** tests |
| R7 | DDS signal generator (sine/triangle/…) piloted by the RP2350, feeding the ADC10065 | agreed — **AD9851** preferred |
| R8 | DDS also feeds the CH32's own ADCs: 12-bit ADC (5 MSPS) **and** 10-bit HSADC (20 MSPS) | agreed |
| R9 | Back-feeding protection on both chips (power rails and I/O) | agreed — see §6 |
| R10 | Board usable without the RP2350's USB host link (RP2350 is **permanently on board**) | **decided** — see §7 |
| ~~R11~~ | ~~On-board WCH-LinkE~~ | **removed for now** (2026-11-12) |

## 3. Verified CH32H417 facts that drive the design

Source: `datasheets/CH32H417DS0_V1.9_en.md` (V1.9; was checked on V1.4 first), `datasheets/CH32H417RM_V1.8_en.md`, `datasheets/CH32H417_EVB_Reference_EN.md`,
`datasheets/CH32H417_UHSIF_RM_EN.md`.

- **Package: CH32H417QEU (QFN128).** The QFN68 (WEU) has *no* BOOT/ISP function.
- **Lot number:** DS V1.4 said lot-digit-5 = 0 parts lack GPHA/Ethernet/SerDes/CAN; **V1.9 no longer says so**.
  The EVB reference still says WCHISPTool download needs digit 5 ≠ 0 → check on receipt.
- **No BOOT0 pin.** Bootloader entry (56 KB system flash):
  - USB ISP on **USBFS PA11 (DM) / PA12 (DP)**: at power-on, DP high + DM low ⇒ BOOT mode.
    DP must not stay pulled up afterwards.
  - UART ISP on **PB6 (TX) / PB7 (RX)** (QFN128), "key-free": tool waits, power-cycle enters BOOT.
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
UART ISP protocol on PB6/PB7, or forces USBFS DP high at power-on for USB ISP (note: `wchisp` has
no H41x device file yet; WCHISPTool does support it).

## 5. USB

- **J1 – CH32 USB3** USB-C: SS pairs + USBHS D+/D− (PB8/PB9).
- **J2 – CH32 USBFS** USB-C (PA11/PA12): ISP port, second USB2 device.
- **J3 – RP2350** USB-C.
- **Decided 2026-11-12** (SDI programming shares PB8/PB9): a 480 Mbps-capable analog switch on PB8/PB9
  (RP-controlled) to select USB-connector ↔ RP2350 SWD. Default (unpowered/RP absent) = USB. Doubles as a
  software "unplug" for USBHS tests.

## 6. Back-feeding protection (R9)

- Power: every VBUS through ideal-diode / power-mux ORing; nothing back-feeds a port.
  CH32 rail behind an RP-controlled load switch with reverse-current blocking.
- I/O: all RP↔CH32 lines through Ioff (power-off high-Z) buffers / bus switches;
  I2C through a powered-off-high-Z buffer; NRST open-drain; analog feeds with series R + clamp.
- ADC10065 in the CH32 switchable domain.
- RP firmware tri-states before power-off; RP measures the CH32 rail (should be ~0 V when off).

## 7. Standalone mode (R10)

The RP2350 is **permanently on board**; "without the RP2350" means *no host connected to the RP2350's USB*.
Decided 2026-11-12:
- Board power: VBUS of J1 (CH32 USB3), J2 (CH32 USBFS), J3 (RP2350) and an optional external input,
  ORed through ideal diodes → any one cable powers the whole board. RP2350 always powered.
- RP2350 firmware boots into a safe standalone default: CH32 powered, NRST released, USB switch → USB
  connector, DDS off.
- The CH32 can command the RP2350 over UART/I2C (set DDS frequency/waveform, sample clock, power
  measurements), so standalone CH32 tests keep the stimulus side.

## 8. Analog / capture chain (R6–R8)

- AD9851 (180 MHz with 6× REFCLK multiplier, 10-bit DAC, sine + comparator square)
  → reconstruction filter → split:
  - differential driver/balun → ADC10065 (10-bit, 65 MSPS, 3 V, output driver 2.5/3.3 V)
  - offset/gain stage → CH32 ADC + HSADC input(s)
- Waveforms: AD9851 sine (+ comparator square). **No triangle** — decided 2026-11-12: exact throughput
  checking is done digitally instead (below).
- **Counter-pattern injection (decided 2026-11-12):** the ADC10065 has no output-enable (only STBY), so a
  2:1 bus switch (D[9:0] + clock + sync, ~12 lines, RP-controlled) selects ADC10065 ↔ RP2350 onto the CH32
  DVP/UHSIF capture pins. RP2350 PIO drives a known counter sequence at a programmable clock; the host
  checks every sample for loss/duplication/reordering. Bus switch must be Ioff/back-feed safe (§6).
- Generator output exposed on a 2-pin 2.54 mm header, signal + GND (D20); no SMA/U.FL.
- ADC10065 → DVP (D[9:0], PCLK, sync) (D21). **UHSIF parked** — not routed on rev A. Notes for later:
  UHSIF = 8–32 bit, ≤125 MHz from SYSCLK, master/slave handshake bus (CS#/WR#/RD#/OE# + RDNE/WRNF/AF#/AE#
  flags), 4 lines × 8 buffers, fixed default pin maps; suited to FPGA/SoC partners, not a raw ADC.
- Sample clock: proposed programmable clock (e.g. Si5351) so the sample rate can be swept for
  throughput tests; same clock to CH32 timer ETR for sample-accurate markers.

## 9. Board / manufacturing

- KiCad, JLCPCB fab + assembly, 6 layers (D18).
- Outline target 63.5 × 88.9 mm, playing-card size (D19), to be confirmed by an area budget.
  First estimate: 4 × USB-C on the two short edges, microSD at a corner, CH32 QFN128 centred
  next to J1 (short SS pairs), RP2350 + flash on the other half, analog chain (AD9851,
  filter, driver, ADC10065) along one long edge, away from the USB3 lines; small parts on the
  back. Likely feasible only with 0402 passives and QFN/TSSOP logic.

## 10. Open questions

See `.claude/TODO.md`.
