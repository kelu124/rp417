# rp417 firmware v0.1 (bring-up)

Two programs, **not tested on hardware yet** (the board has not arrived). Both build cleanly.

| Dir | Target | Base | Output |
|---|---|---|---|
| `rp/` | RP2354B supervisor | pico-sdk 2.1 + TinyUSB | `rp/build/rp417_rp.uf2` |
| `ch32/` | CH32H417MEU6 (V3F core only) | [ch32fun](https://github.com/cnlohr/ch32fun) | `ch32/rp417_ch32.bin` |

Both reuse the reference clone of ch32fun in `projects/tools/ch32fun` (run `projects/clone.sh` first):
the CH32 firmware builds on it, the RP firmware compiles its `minichlink/funprog` programmer core.

## Build

```sh
# RP2354B
cd fw/rp && mkdir -p build && cd build
cmake .. -DPICO_SDK_PATH=$HOME/projets/pico-sdk && make          # -> rp417_rp.uf2

# CH32H417 (riscv64-unknown-elf-gcc or the xPack riscv-none-elf-gcc)
cd fw/ch32 && make build                                         # -> rp417_ch32.bin
```

## First power-up

1. Hold **BOOTSEL** (SW1), plug J3, copy `rp417_rp.uf2` to the RP2350 drive. Later updates: console
   `bootsel`, or open the console port at 1200 baud.
2. The RP enumerates as **1209:0001 "rp417 supervisor"** (pid.codes *test* PID, to replace before sharing) with:
   - **CDC0 console**: `help`, `status`, `vmon`, `pwr on|off|cycle`, `rst`, `usbsel`, `capsel`, `si`, `freq`, `ch`, `swd`, `selftest`, `bootsel`
   - **CDC1**: transparent bridge to the CH32 USART1 (baud = host's line coding)
   - **HID**: funprog programmer for minichlink
3. RP boot state = standalone defaults (D15): CH32 domain on, NRST released, PB8/PB9 on J1, CAP_SEL = ADC10065,
   Si5351 outputs off. LED D6 green = idle, blue = programming, red at the end of a failed `selftest`.
4. Flash the CH32:
   ```sh
   minichlink -c 0x12090001 -C funprog -w fw/ch32/rp417_ch32.bin flash -b
   ```
   The programmer powers the CH32 domain if needed, switches PB8/PB9 to the RP (USB_SEL = 1) and gives them back to
   J1 after 3 s without programmer traffic. Fallbacks if SWD does not work (SPEC §4): a blank chip enters
   BOOT on power-up → WCHISPTool over USB on J2, or UART ISP through CDC1 (`pwr cycle` on the console to enter BOOT).
5. Run `selftest` on the console:

   | Check | How |
   |---|---|
   | VSYS 4.4–5.5 V | RP ADC1 (100k/56k) |
   | CH32 off → rail < 0.3 V, on → > 3.0 V | D29 off-sequence, TPS22918 quick discharge, ADC0 |
   | CH32 UART `ping` | needs the CH32 firmware |
   | MCO = HSE 25 MHz ± 0.1 % | PIO edge counter on GPIO34, 100 ms gate |
   | LOGIC0..7 both directions | 12 patterns each way |
   | HSYNC/VSYNC RP→CH32, MARK CH32→RP | |
   | Si5351 answers on I2C0 | status register |
   | CH32 debug module (SWD) | funprog init, DMSTATUS read |

## Known limits / to verify on the board

- **SWIO has no pull-up on rev A** (net `SWIO_RP` = RP GPIO35 + U4 only). funprog tries 1-wire SWIO first, then
  2-wire RVSWD. 1-wire reads use the RP pull-up plus a 15 ns active precharge; RVSWD should not need it. Rev B: add
  a pull-up (TODO).
- SWIO/RVSWD bit timings are taken from cnlohr's ch570funprog and converted to ns at 150 MHz. They are untested
  against the H417, and minichlink's H41x flash path through a funprog programmer is unproven (SPEC §4 ⚠️).
- CH32 USART1 baud uses ch32fun's `UART_BRR` (SYSCLK/baud, as in its H41x uartdemo); check the actual bit time
  with a scope or `ch ping` on the first board.
- ch32fun's own UART printf is **off**: on H41x it also drives PA12 (= J2_DP) as USART6 TX.
- The Si5351 driver: CLK0/CLK1 on PLLA (phase-coherent when they share it), CLK2 on PLLB, 8 kHz–150 MHz.
  Phase offsets (`si phase`) untested.
- Not in v0.1: V5F core, USB3/USBHS/SD/DVP/HSADC tests, the RP PIO counter, I2C link to the CH32, QSPI link, SAO.
