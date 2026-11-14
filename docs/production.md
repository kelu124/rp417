# Production (JLCPCB)

How to order the v1.0 board, fabricated and assembled by JLCPCB. Background: [bill of materials](bom.md),
[layout and routing](layout.md).

## Files

| File | Where it goes |
|---|---|
| [rp417.zip](https://github.com/kelu124/rp417/raw/main/hw/production/rp417.zip) | PCB order → *Add gerber file* (6 copper layers, mask, paste, silkscreen, edge, PTH + NPTH drill) |
| [bom.csv](https://github.com/kelu124/rp417/blob/main/hw/production/bom.csv) | PCB Assembly → BOM |
| [positions.csv](https://github.com/kelu124/rp417/blob/main/hw/production/positions.csv) | PCB Assembly → CPL (pick and place) |
| [netlist.ipc](https://github.com/kelu124/rp417/blob/main/hw/production/netlist.ipc) | optional IPC-D-356 netlist for electrical test |

All of them come from the routed board `hw/rp417.kicad_pcb` (exported from KiCad). Regenerate them after any board
change, together with the [images](images/) (`hw/gen/gen_site.py`).

## PCB order settings

| Setting | Value |
|---|---|
| Layers | 6 |
| Dimensions | 63.5 × 88.9 mm |
| Min track / clearance used | 0.1 / 0.1 mm |
| Min via | 0.4 mm pad / 0.2 mm drill |
| Assembly | both sides |

Check the 6-layer capabilities (via size, track/space, solder-mask dams between the 0.4 mm-pitch QFN pads) and
choose the stack-up and impedance options on the order page; the USB3 SuperSpeed and USB2 pairs want 90 Ω differential.

## Assembly

- **Both sides** are populated (most decoupling and series resistors are on the bottom).
- **Consigned part:** U1 **CH32H417MEU6** is not stocked by JLCPCB; it is supplied by the user and sent to JLCPCB
  (D43, D58).
- **Not assembled (DNP):** U10 **ADC10065** (hand-soldered by the user, D42) and the 2.54 mm headers **J5, J6, J7**
  (D68). They are absent from the BOM and CPL.
- **Thin stock** at the last check: RP2354B and the RP2350 SMPS inductor (AOTA-B201610S3R3). Reserve them early.
- **Check every part's rotation** in JLCPCB's placement preview: the CPL uses KiCad's rotation convention, which
  differs from JLCPCB's for some packages (QFNs, SOT-23-6, USB-C).

## Before ordering

- Review the 23 starved thermal reliefs (GND pads with fewer than two spokes into the pour).
- Check the QR codes where they cross vias and J3's pads (the fab clips silkscreen over exposed copper).
- Compare the LCSC USB-C and microSD footprints with the manufacturer drawings (D59 waives 21 DRC errors inside them).
- Check JLCPCB's stencil recommendation for the via grids in the U1/U2 exposed pads (open vias can wick solder).
- Check stock and prices of every BOM line on the day of the order.
