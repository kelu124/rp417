# CH32H417 hardware notes

Facts from the WCH documents that shaped the board. Sources (markdown copies in
[`datasheets/`](https://github.com/kelu124/rp417/tree/main/datasheets)): CH32H417 datasheet DS V1.9, reference
manual RM V1.8, EVB reference, UHSIF reference manual.

## Package

- **CH32H417MEU6, QFN88, 10 × 10 mm, 0.4 mm pitch**, 7.7 mm exposed pad (D54). The user supplies the chips.
- QFN88 lacks PE2, PE7, PF13, PA6, PA8, PB6, PB7, VREFP and VBAT (DS V1.9 pin table); it has only HSADC_IN0–3
  (PC0–PC3; IN4–6 are on PF8–PF10, QFN128 only) and one DVP PCLK pin (PB12).
- Pin 7–10 are the internal Ethernet PHY's analog pins (MDIRN/MDIRP/MDITN/MDITP), not GPIOs.
- BOOT/ISP works on QFN128 and QFN88, not on QFN68 (EVB reference, ISP table).
- **Lot number:** DS V1.4 said parts with lot digit 5 = 0 lack some peripherals; V1.9 no longer says so, but the
  EVB reference still says WCHISPTool needs digit 5 ≠ 0. Check on receipt.

## Boot and programming

- **No BOOT0 pin.** The bootloader (56 KB system flash) is entered at power-on:
  - USB ISP on USB FS PA11 (DM) / PA12 (DP): DP high + DM low at power-on; DP must not stay pulled up afterwards.
  - UART ISP, "key-free", on **PA9/PA10 on QFN88** (PB6/PB7 on QFN128): the tool waits, a power cycle enters BOOT.
    Needs an option bit (factory default: enabled).
  - A blank chip enters BOOT automatically.
  - ⇒ controlling the CH32's power is itself a programming mechanism.
- **Debug (SDI):** 1-wire SWIO (default) or 2-wire SWDIO/SWCLK on **PB9/PB8 — the USB HS D−/D+ pins.** WCH's EVB
  wires them to both the USB connector and the debug header; rp417 uses an analog switch instead.
- ch32fun's minichlink knows the chip (model 0x4170, 960 KB flash at 0x08000000); flashing an H41x through
  funprog is still to be confirmed on hardware.

## USB

- **USBSS** 5 Gbps: one TX/RX pair with P/N swap only (RM V1.8 `RB_LINK_SS_PLR`), so J1's SuperSpeed lanes are wired
  for one plug orientation (the other gives USB2 only, D27).
- **USBHS** 480 Mbps on PB8/PB9; **USBFS** 12 Mbps on PA11/PA12 (also OTG).

## Capture and analog

- **DVP:** 8/10/12-bit, PCLK up to 150 MHz, VSYNC/HSYNC. 10/12-bit samples are zero-extended to 16 bit (65 MSPS →
  130 MB/s); lines alternate between two DMA buffers; snapshot or continuous mode (RM V1.8 §29). Gapless capture
  across line and frame boundaries is the open question the counter test answers.
- **UHSIF:** 8–32 bit, ≤ 125 MHz from SYSCLK, 500 MB/s theoretical — parked for rev A (D21).
- **ADC:** 2 × 12-bit, up to 5 MSPS, 16 channels. **HSADC:** 10-bit, 20 MSPS. PC0–PC3 are both ADC_IN10–13 and
  HSADC_IN0–3. VDDA/VREF ≥ 3.0 V recommended when using the HSADC.
- Timers are STM32-style; an external clock on an ETR pin (TIM8_ETR on PF2 here) counts samples.

## Power

- Internal LDO makes the core rails (VDDK, VDD12A) from VDD33; an external supply is optional (DS V1.9 §1.4.3), so
  rp417 has no 1V2 regulator (D25).
- Rail order VDD33 ≥ VDD33A ≥ VDDIO ≥ VIO18 (DS V1.9 Table 3-2) is met by a single 3V3 rail; VIO18 is tied to VDDIO.
- Memory: 896 KB SRAM = 128 KB ITC + 256 KB DTCM (V5 core) + 512 KB shared — the streaming buffer budget.

## Claims checked

| Claim | Verdict |
|---|---|
| UHSIF 32-bit, 125 MHz, 500 MB/s | ✅ datasheet + UHSIF manual |
| DVP up to 12-bit at 150 MHz | ✅ |
| 896 KB SRAM | ✅ (split as above) |
| USB3 measured ≈ 450 MB/s | ⚠️ EVB/marketing figure, not in the datasheet — to measure |
| DVP continuous gapless capture | ⚠️ continuous mode + ping-pong buffers exist; to prove with the counter test |
