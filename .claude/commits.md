# Commit log

| Date | Hash | Summary |
|------|------|---------|
| — | b7066f5 | Initial commit (README) |
| 2026-11-12 | d91dc6c | Project scaffold: CLAUDE.md, SPEC.md (requirements, verified CH32H417 facts, programming via minichlink/funprog), .claude TODO/DONE/commits, datasheets (PDF + markdown), projects/ survey + clone script (clones gitignored), userinputs notes |
| 2026-11-12 | 9dced23 | SPEC: USB switch on PB8/PB9 and standalone mode marked decided |
| 2026-11-12 | 82bcca4 | SPEC: drop triangle, add RP2350 counter-pattern injection into the capture bus |
| 2026-11-12 | 4d87bc2 | Datasheets: DS V1.9 + RM V1.8 (en/zh) + AD9851 as markdown; DECISIONS.md log (D01–D17); SPEC re-verified on V1.9, DVP RM notes |
| 2026-11-12 | a2de425 | Decisions D18 (KiCad/JLCPCB/6L) and D19 (playing-card outline target) |
| 2026-11-12 | 86f3365 | D20: generator output on 2-pin 2.54 mm header, no SMA |
| 2026-11-12 | 76a563c | docs/design/block-diagram.html: mermaid block/power/capture diagrams, CH32 + RP2354B + interconnect pin plans, proposals P1-1..P1-10 |
| 2026-11-12 | 02e7f84 | D21: DVP-only capture, UHSIF parked |
| 2026-11-12 | f9fafca | SessionStart hook listing unanswered decision points (TODO open questions + untagged P-proposals) |
| 2026-11-13 | cf87f8d | D22: simplicity / minimal-BOM design constraint (SPEC §0) |
| 2026-11-13 | 1d5a528 | D23–D31 (P1 review under D22: simplified power, single-orientation USB3, no INA/bus switches/2:1 switch/AD9851, ADC10065 jumper input); P2-1..P2-9 proposals; hook accepts `tag w` (withdrawn) |
| 2026-11-13 | d27523d | D32–D40: Si5351 plan, LC generator, input-select header, CH32 ADC feed, counter pattern on DVP alternate pins via logic bus, RP sync in JPEG mode, QSPI, AVCC ferrite, keep J2 |
| 2026-11-13 | 1e793a6 | D41: no external 5 V input, 3 × LM66100 |
| 2026-11-13 | 19cdeb6 | Design page rev A redraw, BOM with JLC stock, area budget, RM checks, D42 ADC10065 DNP, P3-1..P3-6 |
| 2026-11-13 | 31868e2 | D43–D47: CH32 user-sourced, IRS jumper 2 Vpp default, USB ESD, genuine Si5351, rev A part selection |
| 2026-11-13 | (see git log) | QFN128 pitch source + corrected fan-out note (WCH EVB footprint: 0.16 mm pads, 0.19 mm gap) |
| 2026-11-13 | (this commit) | D48 parts on both sides; design page status block + side assignment; mermaid diagrams parse-checked |
| 2026-11-13 | (see git log) | hw/: generated KiCad schematic rev A draft (6 sheets, 202 parts, 150 nets, ERC 0), LCSC footprints, generator |
| 2026-11-13 | (see git log) | Board generator (placement with D53 perpendicular-passive rule, zones, DSN), finish/DRC script, project rules, hw/README, D49–D53 |
| 2026-11-13 | (see git log) | D54 CH32H417MEU6 (QFN88), D55 2:1 capture switch back, D56 QFN88 pin moves; schematic + placement regenerated; SPEC/design page updated |
| 2026-11-13 | (see git log) | SN74CBTLV3257 datasheet + 65 MHz check in SPEC; proposal P4-1 (capture series R) |
| 2026-11-13 | 5390dad | D57: capture series R 0/22 Ω, switch channels grouped by CH32 edge, switches moved next to DVP pins |
| 2026-11-13 | 2c127af | D58: U1 consigned to JLC; open question closed |
| 2026-11-13 | 635fcc2 | D59: waive J1–J3 footprint DRC errors in finish.py |
| 2026-11-14 | aadc012 | First routed draft (freerouting 20 min: 2 signal nets + ~58 power-to-plane connections unrouted); README: capped router command, job_timeout instead of ignored -mp |
| 2026-11-14 | d195bd7 | D60: dogbone plane fan-out + EP via grids in pcb.py; reroute: 26 connections open (was 60), 16 of them signals |
| 2026-11-14 | 3303f43 | D60 rev (fewer EP vias, QFN pins via cap) + D61: hand routing from here, finish.py protects the board |
| 2026-11-14 | c730c2c | Hand-routing checkpoint (+3V3 plane restored) + D62 status RGB LEDs D6/D7 (schematic, lib part, datasheet, placed on board); .venv gitignored |
| 2026-11-14 | ea4dd07 | D63: D7 blue on CH32 PF1 via R91 (330 Ω); hand-routing checkpoint |
| 2026-11-14 | 6cba252 | D64: J6 2×2 HSADC test header (PC0, PC3 via R92, GND, GEN_OUT); hand-routing checkpoint |
| 2026-11-14 | bc9c2c3 | D65: J6 pin 1 = PC1 via R93 instead of CH_AIN0 (user's J6.1 branch re-netted); hand-routing checkpoint |
| 2026-11-14 | fee96e6 | D66: SAO header J7 on RP I2C0 (GPIO44/45) + pull-ups; D6 red to GPIO43; hand-routing checkpoint |
| 2026-11-14 | (this commit) | Routing complete (0 unconnected, user hand routing + cleanup, QR codes); D67 3D models (.wrl) + project-relative model paths; 3D renders top/bottom/angled |
