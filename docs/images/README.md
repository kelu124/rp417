# Board images (v1.0)

Renders from `kicad-cli pcb render` of `hw/rp417.kicad_pcb` (commands in `hw/README.md`); layer plots and assembly
views written by `/usr/bin/python3 hw/gen/gen_site.py` (re-run after board changes).

| Top | Bottom |
|---|---|
| ![top](rp417-v1.0-top.png) | ![bottom](rp417-v1.0-bottom.png) |
| ![top angled](rp417-v1.0-top-angled.png) | ![bottom angled](rp417-v1.0-bottom-angled.png) |

Copper layers (board area; B.Cu mirrored as seen from below):

| F.Cu | In1 (GND) | In2 (signal) |
|---|---|---|
| ![F.Cu](rp417-v1.0-F_Cu.png) | ![In1](rp417-v1.0-In1_Cu.png) | ![In2](rp417-v1.0-In2_Cu.png) |

| In3 (+3V3_CH / +3V3) | In4 (GND) | B.Cu |
|---|---|---|
| ![In3](rp417-v1.0-In3_Cu.png) | ![In4](rp417-v1.0-In4_Cu.png) | ![B.Cu](rp417-v1.0-B_Cu.png) |

Assembly views (silkscreen + fab): [top](rp417-v1.0-assembly-top.png), [bottom](rp417-v1.0-assembly-bottom.png).
