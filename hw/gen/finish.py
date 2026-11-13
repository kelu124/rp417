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
board.Save(out)

tracks = [t for t in board.GetTracks() if t.GetClass() == "PCB_TRACK"]
vias = [t for t in board.GetTracks() if t.GetClass() == "PCB_VIA"]
print(f"tracks {len(tracks)}  vias {len(vias)}  length {sum(pcbnew.ToMM(t.GetLength()) for t in tracks):.0f} mm")

rep = os.path.join(B, "drc.json")
subprocess.run(["kicad-cli", "pcb", "drc", "--format", "json", "--schematic-parity", "-o", rep, out],
               capture_output=True)
d = json.load(open(rep))
c = collections.Counter((v["severity"], v["type"]) for v in d.get("violations", []))
for k, n in c.most_common():
    print(n, *k)
print("unconnected items:", len(d.get("unconnected_items", [])))
print("schematic parity:", len(d.get("schematic_parity", [])))
