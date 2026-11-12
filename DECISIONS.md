# Design decision log

Every design decision, in order. Never edit a past entry's decision: if it changes, add a new
entry that **supersedes** it and mark the old one `Superseded by Dxx`.
Format: ID · date · decision · why · alternatives considered · decided by · SPEC section.

| ID | Date | Decision | Why | Alternatives considered | By | SPEC |
|----|------|----------|-----|-------------------------|----|------|
| D01 | 2026-11-12 | RP2350 supervises the CH32H417: it controls power and reset | Automated, hands-off limit testing | — | user | §1, R1 |
| D02 | 2026-11-12 | Separate USB-C connectors: J1 CH32 USB3 (SS + USBHS D+/D−), J2 CH32 USBFS, J3 RP2350 | A cable carries only one D+/D− pair, so a USB3-on-one-side/USB2-on-the-other connector would pick the controller by plug orientation | Single shared USB-C (rejected) | user approved proposal | §5, R3 |
| D03 | 2026-11-12 | RP2350 ↔ CH32 links: UART, I2C, QSPI + GPIO | Test control and data paths between supervisor and target | — | user | R4 |
| D04 | 2026-11-12 | CH32 SD card on SDIO/SDMMC | Storage throughput testing | — | user | R5 |
| D05 | 2026-11-12 | ADC10065 (10-bit, 65 MSPS) feeds the CH32 parallel capture; its purpose is **data throughput**, not signal quality | Defines the analog spec: no high-end generator chain needed for fidelity | Signal-quality target (rejected) | user | §8, R6 |
| D06 | 2026-11-12 | Signal generator: AD9851 DDS, controlled by the RP2350 | User preference; 180 MHz clock covers the 32.5 MHz Nyquist of 65 MSPS | AD9833 (too slow), AD9910 (overkill) | user | §8, R7 |
| D07 | 2026-11-12 | The generator also feeds the CH32's 12-bit ADC (5 MSPS) and 10-bit HSADC (20 MSPS) | Test both internal converters | — | user | §8, R8 |
| D08 | 2026-11-12 | Back-feed protection on both chips: power-rail ORing with reverse blocking, Ioff buffers/bus switches on every RP↔CH32 line, I2C power-off-high-Z buffer, open-drain NRST, series R + clamp on analog feeds, ADC10065 in the CH32 switched domain | The RP2350 deliberately powers the CH32 off while its own lines may be live | — | user (requirement), Claude (method) | §6, R9 |
| D09 | 2026-11-12 | ~~On-board WCH-LinkE~~ | — | — | user | R11 · **Superseded by D10** |
| D10 | 2026-11-12 | WCH-LinkE removed from the design | User decision | Keep WCH-LinkE | user | R11 |
| D11 | 2026-11-12 | Programming: **minichlink on the host + RP2350 running a ch32fun "funprog" port** (1-wire SWIO and 2-wire RVSWD); bootloader UART ISP on PB6/PB7 as fallback | minichlink already lists the CH32H417; funprog is a portable programmer core; no extra programmer hardware | wchisp USB ISP (no H41x support yet), WCH-LinkE (removed, D10), custom SDI code from scratch | user | §4, R2 |
| D12 | 2026-11-12 | MCU package: **CH32H417QEU (QFN128)** | The QFN68 (WEU) has no BOOT/ISP; QFN128 exposes DVP + UHSIF + SDIO + the rest | QFN68, QFN88 | Claude (from datasheet) | §3 |
| D13 | 2026-11-12 | RP2350 is **permanently on board** | User decision | Removable or socketed module | user | §7, R10 |
| D14 | 2026-11-12 | **USB switch on PB8/PB9** (480 Mbps analog, RP-controlled, default = USB connector) | PB8/PB9 are both USBHS D+/D− and the SDI debug pins; also allows a software "unplug" of USBHS | Debug-only header, no switch | user | §5 |
| D15 | 2026-11-12 | **Standalone mode**: any VBUS (J1/J2/J3/external) ORed through ideal diodes powers the whole board; RP2350 always powered and boots into safe defaults (CH32 on, NRST released, switch → USB, DDS off); the CH32 can command the RP2350 over UART/I2C | The board must work with no host on the RP2350's USB | CH32-only power path with RP held in reset | user approved proposal | §7 |
| D16 | 2026-11-12 | **No triangle waveform.** Exact throughput checking via **RP2350 counter-pattern injection**: a 2:1 bus switch (D[9:0] + clock + sync) selects ADC10065 or RP2350 PIO onto the CH32 capture pins | The ADC10065 has no output enable; a digital counter detects every lost, duplicated or reordered sample exactly | A: RP-driven parallel DAC for arbitrary waveforms; C: both | user (option B) | §8 |
| D17 | 2026-11-12 | Reference documents: CH32H417 datasheet **V1.9** and Reference Manual **V1.8** (EN primary, ZH kept); V1.4 mirror copy dropped | Latest official versions supplied by the user | — | Claude | §3 |
