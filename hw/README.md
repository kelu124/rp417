# rp417 hardware — rev A draft

Everything here is **generated**. Edit the generators in `gen/`, not the KiCad files.

| File | What |
|---|---|
| `gen/build.py` | **Netlist source of truth**: every part, value, footprint, LCSC # and net, grouped by sheet. Writes `rp417*.kicad_sch` + `lib/rp417.kicad_sym` + `gen/nets.json`. |
| `gen/kisch.py` | Minimal schematic writer: each pin gets a 2.54 mm stub and a global label (or a no-connect flag). |
| `gen/pcb.py` | Netlist → footprints → placement (fixed anchors in `FIX`; passives anchored to their IC pin, **perpendicular to the IC edge, IC-side pad facing the pin** (D53), decoupling one per power pin on B.Cu) → zones → `build/rp417.dsn`. |
| `gen/finish.py` | Imports the freerouting session, fills zones, writes `rp417.kicad_pcb`, runs DRC. Since D61 the board is hand-routed: if `rp417.kicad_pcb` has edits, it writes `build/rp417_autorouted.kicad_pcb` instead (`--force` to overwrite). |
| `lib/lcsc.*` | Symbols/footprints imported from LCSC with easyeda2kicad (pins re-typed to passive). |
| `lib/lcsc.3dshapes/` | 3D models from LCSC (easyeda2kicad `--3d`). Only the `.wrl` files are committed (5 MB, used by the 3D viewer and renders); the `.step` files (32 MB, needed for STEP export) are gitignored — refetch with `.venv/bin/easyeda2kicad --lcsc_id <C…> --3d --output hw/lib/lcsc`. Models are referenced as `${KIPRJMOD}/lib/lcsc.3dshapes/…`. |
| `renders/` | 3D views (top, bottom, angled) from `kicad-cli pcb render`. |
| `gen/gen_site.py` | GitHub Pages material: copies the renders to `docs/images/`, plots the 6 copper layers + assembly views, writes `docs/pinmap.md` (from the netlist) and `docs/bom.md` (from `production/bom.csv`). Re-run after board/BOM changes. |
| `rp417.kicad_pro` | Design rules + net classes (Default 0.1/0.1 mm, via 0.4/0.2; Power 0.4 mm). |

## Rebuild

```bash
/usr/bin/python3 hw/gen/build.py                      # schematic (KiCad 10 python not needed)
(cd hw && kicad-cli sch erc rp417.kicad_sch)          # expect 0 violations
/usr/bin/python3 hw/gen/pcb.py                        # placement + DSN (needs system python with pcbnew)
cd hw/build && FREEROUTING__USAGE_AND_DIAGNOSTIC_DATA__DISABLE_ANALYTICS=true \
  systemd-run --user --scope -q -p MemoryMax=4G -p MemorySwapMax=0 nice -n 19 \
  java -Xmx3g -Djava.awt.headless=true -jar ~/.local/share/freerouting/freerouting-2.1.0.jar \
  --gui.enabled=false --usage_and_diagnostic_data.disable_analytics=true \
  --router.job_timeout=00:20:00 -de rp417.dsn -do rp417.ses
cd ../.. && /usr/bin/python3 hw/gen/finish.py         # import, fill, DRC
```

Freerouting 2.x ships Segment analytics — keep both "disable analytics" switches above.

**Stopping the router (freerouting 2.1.0):** `-mp` / `--router.max_passes` are *ignored* headless (they set
`maxPasses`, but the batch loop checks `stop_pass_no`, which only the GUI fills in), so the router runs until
its job timeout (default 24 h) and writes the `.ses` only at the end — an external `timeout` kill loses
everything. Use `--router.job_timeout` (it stops cleanly and saves). The D57 board plateaus after ~15–20 min
(2026-11-14: 20 min → 45 passes, 60 unrouted). Keep the memory cap: the box has 31 GB shared with other sessions.

## Stack-up (6 layers, D18)

F.Cu signal · In1 GND · In2 signal · In3 power (+3V3_CH over the top 44 mm, +3V3 below) · In4 GND · B.Cu signal.
F.Cu and B.Cu also carry GND pours.

## Known limits of the draft (to fix by hand in KiCad)

- **Autorouted**: no length matching, no impedance control. USB3 SS pairs (J1 ↔ U1, 90 Ω diff),
  USBHS/USBFS (90 Ω), the DVP primary bus (ADC → PE0–PE6/PF3/PF4/PF14) and the RP counter bus
  (GPIO12–20 → PC6/PC7/PB13/PF5/PD12–15/PA6) must be re-routed as matched groups.
- Power is routed with 0.4 mm traces plus vias to the In3 / In1 / In4 planes; check the buck loop
  (U8, L1, C) and the RP2350 VREG loop (U2 pin 63, L2) by hand — they want short, wide copper.
- LCSC/easyeda footprints: USB-C pegs and the TF-01A holes trip `hole_clearance`/`annular_width`
  rules; compare them with the manufacturer drawings before ordering.
- Schematic is label-based (no drawn wires between symbols): readable as a netlist, not a pretty
  drawing.
