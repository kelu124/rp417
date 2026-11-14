#!/usr/bin/python3
"""Import the freerouting session, fill zones, save hw/rp417.kicad_pcb, run DRC.

Run from repo root after freerouting wrote hw/build/rp417.ses:
    /usr/bin/python3 hw/gen/finish.py
"""
import os, json, subprocess, collections
import pcbnew

HW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(HW, "build")
board = pcbnew.LoadBoard(os.path.join(B, "rp417_placed.kicad_pcb"))
ses = os.path.join(B, "rp417.ses")
if os.path.exists(ses):
    if not pcbnew.ImportSpecctraSES(board, ses):
        raise SystemExit("SES import failed")
filler = pcbnew.ZONE_FILLER(board)
filler.Fill(board.Zones())
out = os.path.join(HW, "rp417.kicad_pcb")
# D61: hw/rp417.kicad_pcb is now hand-routed in KiCad. Never overwrite it unless it is still byte-identical
# to what this script last wrote (hash in build/), or --force is given.
import hashlib, sys
stamp = os.path.join(B, "finish.sha256")
def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
if os.path.exists(out) and "--force" not in sys.argv:
    if not os.path.exists(stamp) or open(stamp).read().strip() != sha(out):
        out = os.path.join(B, "rp417_autorouted.kicad_pcb")
        print(f"hw/rp417.kicad_pcb has manual edits -> writing {out} instead (use --force to overwrite)")
board.Save(out)
if out.endswith(os.path.join("hw", "rp417.kicad_pcb")):
    open(stamp, "w").write(sha(out))

tracks = [t for t in board.GetTracks() if t.GetClass() == "PCB_TRACK"]
vias = [t for t in board.GetTracks() if t.GetClass() == "PCB_VIA"]
print(f"tracks {len(tracks)}  vias {len(vias)}  length {sum(pcbnew.ToMM(t.GetLength()) for t in tracks):.0f} mm")

rep = os.path.join(B, "drc.json")
subprocess.run(["kicad-cli", "pcb", "drc", "--format", "json", "--schematic-parity", "-o", rep, out],
               capture_output=True)
d = json.load(open(rep))

# D59: waived DRC errors that live inside vendor connector footprints (LCSC USB-C / USB-B
# library geometry: GND shell/pin pads too close to the footprint's own NPTH pegs, thin annular
# ring on J1 shell pad 25). Waived only if *every* item of the violation belongs to one of these refs.
WAIVE_TYPES = {"hole_clearance", "annular_width"}
WAIVE_REFS = {"J1", "J2", "J3"}


def waived(v):
    if v["type"] not in WAIVE_TYPES:
        return False
    return all(any(i["description"].endswith(f" of {r}") or f" of {r} " in i["description"]
                   for r in WAIVE_REFS) for i in v["items"])


viol = d.get("violations", [])
w = [v for v in viol if waived(v)]
c = collections.Counter((v["severity"], v["type"]) for v in viol if not waived(v))
for k, n in c.most_common():
    print(n, *k)
print(f"waived (D59, J1-J3 footprint geometry): {len(w)}")
print("unconnected items:", len(d.get("unconnected_items", [])))
print("schematic parity:", len(d.get("schematic_parity", [])))
