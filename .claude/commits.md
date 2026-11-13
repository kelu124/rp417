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
| 2026-11-13 | (this commit) | Board generator (placement with D53 perpendicular-passive rule, zones, DSN), finish/DRC script, project rules, hw/README, D49–D53 |
