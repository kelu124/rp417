# RP2350 ↔ CH32 UART protocol (v0.1)

Link: RP GPIO0/GPIO1 (UART0) ↔ 220 Ω ↔ CH32 PA10/PA9 (USART1), **115200 8N1**, ASCII lines.

- Request: `<cmd> [arg]\n` (`\r` ignored), ≤ 63 characters.
- Reply: zero or more data lines, then **`ok`** or **`err <reason>`**. Lines end in `\r\n`.
- Lines starting with `#` are unsolicited events (e.g. `# rp417-ch32 0.1 boot` after reset). The RP ignores them
  while waiting for a reply.
- Normally the RP bridges this UART to its USB CDC1 port, so a host can type the same commands. When the RP itself
  sends a command (console `ch …`, `selftest`), it takes the UART over until `ok`/`err`.

| Command | Reply data | Meaning |
|---|---|---|
| `ping` | `pong` | liveness |
| `ver` | `rp417-ch32 <ver> <date> <time>` | firmware build |
| `clk` | `sysclk <Hz> hse <Hz> cfgr0 <hex>` | configured clocks |
| `led <0-7>` / `led hb` | — | D7 RGB (bit0 R, bit1 G, bit2 B) / back to green heartbeat |
| `mco <off\|sys\|hsi\|hse\|pll2>` | — | MCO source on PB0 (default `hse` = 25 MHz, counted by the RP on GPIO34) |
| `lin` | `logic <hex>` | read LOGIC0..7 (PD12 PD13 PD14 PD15 PD10 PD11 PC6 PC7) |
| `lout <hex>` | — | drive LOGIC0..7 (push-pull) |
| `lz` | — | LOGIC0..7 back to inputs (default after reset) |
| `sync` | `hsync <0\|1> vsync <0\|1>` | read PA4/PA5 (driven by the RP) |
| `mark <0\|1\|z>` | — | drive PB14 low/high or release it |
| `sd` | `sd_cd <0\|1>` | microSD card-detect PD0 (pull-up on) |
| `help` | command list | |

Rule (D29): every CH32 pin facing the RP is an input after reset; the CH32 only drives a shared line
when told to (`lout`, `mark`), and the RP releases its side first.
