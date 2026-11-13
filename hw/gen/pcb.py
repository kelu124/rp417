#!/usr/bin/python3
"""rp417 rev A draft board: netlist -> footprints -> placement -> zones -> DSN.

Run from repo root:  /usr/bin/python3 hw/gen/pcb.py
Then route.sh runs freerouting and imports the session.
"""
import os, re, sys, math, subprocess
import pcbnew

HW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(HW, "build")
os.makedirs(BUILD, exist_ok=True)
STOCK = "/usr/share/kicad/footprints"
MM = pcbnew.FromMM
W, H = 63.5, 88.9          # playing card, portrait (D19)
OX, OY = 100.0, 50.0       # board origin on the sheet

# ------------------------------------------------------------------ netlist
net_file = os.path.join(BUILD, "rp417.net")
subprocess.run(["kicad-cli", "sch", "export", "netlist", "--format", "kicadsexpr", "-o", net_file,
                os.path.join(HW, "rp417.kicad_sch")], check=True, capture_output=True)
txt = re.sub(r"\s+", " ", open(net_file).read())


def blocks(s, head):
    out, i = [], 0
    while True:
        i = s.find("(" + head, i)
        if i < 0:
            return out
        d, j = 0, i
        while True:
            if s[j] == "(":
                d += 1
            elif s[j] == ")":
                d -= 1
                if d == 0:
                    break
            j += 1
        out.append(s[i:j + 1])
        i = j + 1


comps = {}
for b in blocks(txt[txt.find("(components"):txt.find("(libparts")], "comp "):
    ref = re.search(r'\(ref "([^"]+)"', b).group(1)
    val = re.search(r'\(value "([^"]*)"', b).group(1)
    fp = re.search(r'\(footprint "([^"]*)"', b)
    sheet = re.search(r'\(sheetpath \(names "([^"]*)"', b)
    comps[ref] = dict(value=val, fp=fp.group(1) if fp else "", sheet=sheet.group(1) if sheet else "",
                      dnp='(property (name "dnp")' in b)
pin_net = {}
nets = {}
for b in blocks(txt[txt.find("(nets"):], "net "):
    name = re.search(r'\(name "([^"]*)"', b).group(1)
    nodes = re.findall(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"', b)
    nets[name] = nodes
    for r, p in nodes:
        pin_net[(r, p)] = name

# ------------------------------------------------------------------ board
board = pcbnew.BOARD()
board.SetCopperLayerCount(6)
ds = board.GetDesignSettings()
ds.SetBoardThickness(MM(1.6))
# JLC 6-layer capability: 0.09/0.09 mm min; we use 0.1 mm tracks/clearance for the draft
nsets = ds.m_NetSettings
dflt = nsets.GetDefaultNetclass()
dflt.SetTrackWidth(MM(0.1)); dflt.SetClearance(MM(0.1))
dflt.SetViaDiameter(MM(0.4)); dflt.SetViaDrill(MM(0.2))
pwr = pcbnew.NETCLASS("Power")
pwr.SetTrackWidth(MM(0.4)); pwr.SetClearance(MM(0.15)); pwr.SetViaDiameter(MM(0.6)); pwr.SetViaDrill(MM(0.3))
nsets.SetNetclass("Power", pwr)
POWER_NETS = ["GND", "+5V_SYS", "+3V3", "+3V3_CH", "+3V3A_CH", "+1V1", "VDDK", "VDD12A", "BUCK_SW",
              "VBUS1", "VBUS2", "VBUS3", "RP_VREG_LX"]
for n in POWER_NETS:
    nsets.SetNetclassPatternAssignment(n, "Power")
ds.m_MinThroughDrill = MM(0.2)
ds.m_TrackMinWidth = MM(0.09)
ds.m_MinClearance = MM(0.09)
ds.m_ViasMinSize = MM(0.35)
ds.m_HoleClearance = MM(0.2)
ds.m_CopperEdgeClearance = MM(0.3)
for lid, nm, typ in [(pcbnew.In1_Cu, "In1.GND", pcbnew.LT_POWER), (pcbnew.In2_Cu, "In2.Sig", pcbnew.LT_SIGNAL),
                     (pcbnew.In3_Cu, "In3.PWR", pcbnew.LT_POWER), (pcbnew.In4_Cu, "In4.GND", pcbnew.LT_POWER)]:
    board.SetLayerName(lid, nm)
    board.SetLayerType(lid, typ)

netinfo = {}
for n in sorted(nets):
    ni = pcbnew.NETINFO_ITEM(board, n)
    board.Add(ni)
    netinfo[n] = ni


def P(x, y):
    return pcbnew.VECTOR2I(MM(OX + x), MM(OY + y))


# outline with 1 mm corner radius
def edge(x0, y0, x1, y1):
    s = pcbnew.PCB_SHAPE(board)
    s.SetShape(pcbnew.SHAPE_T_SEGMENT)
    s.SetStart(P(x0, y0)); s.SetEnd(P(x1, y1))
    s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(MM(0.1))
    board.Add(s)


r = 1.0
edge(r, 0, W - r, 0); edge(W, r, W, H - r); edge(W - r, H, r, H); edge(0, H - r, 0, r)
for cx, cy, a0 in [(r, r, 180), (W - r, r, 270), (W - r, H - r, 0), (r, H - r, 90)]:
    s = pcbnew.PCB_SHAPE(board)
    s.SetShape(pcbnew.SHAPE_T_ARC)
    s.SetCenter(P(cx, cy))
    s.SetStart(P(cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))))
    s.SetArcAngleAndEnd(pcbnew.EDA_ANGLE(90, pcbnew.DEGREES_T), True)
    s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(MM(0.1))
    board.Add(s)

# ------------------------------------------------------------------ footprints
fps = {}
for ref, c in comps.items():
    if ref.startswith("#") or not c["fp"]:
        continue
    lib, name = c["fp"].split(":")
    path = os.path.join(HW, "lib", "lcsc.pretty") if lib == "lcsc" else os.path.join(STOCK, lib + ".pretty")
    fp = pcbnew.FootprintLoad(path, name)
    if fp is None:
        raise SystemExit(f"footprint not found: {c['fp']}")
    fp.SetReference(ref)
    fp.SetValue(c["value"])
    fp.SetFPID(pcbnew.LIB_ID(lib, name))
    if c["dnp"]:
        fp.SetDNP(True)
        fp.SetExcludedFromBOM(False)
        fp.SetExcludedFromPosFiles(True)
    board.Add(fp)
    for pad in fp.Pads():   # easyeda imports: plated holes with no ring
        if pad.GetAttribute() == pcbnew.PAD_ATTRIB_PTH:
            d = pad.GetDrillSize()
            sz = pad.GetSize(pcbnew.F_Cu)
            if sz.x <= d.x + MM(0.05) or sz.y <= d.y + MM(0.05):
                if pad.GetNumber() == "":
                    pad.SetAttribute(pcbnew.PAD_ATTRIB_NPTH)
                    pad.SetLayerSet(pad.UnplatedHoleMask())
                else:
                    pad.SetSize(pcbnew.F_Cu, pcbnew.VECTOR2I(d.x + MM(0.4), d.y + MM(0.4)))
    for pad in fp.Pads():
        n = pin_net.get((ref, pad.GetNumber()))
        if n:
            pad.SetNet(netinfo[n])
    fps[ref] = fp

# ------------------------------------------------------------------ placement
# fixed parts: (x, y, rotation_deg, side)  side: 'F' or 'B'
FIX = {
    "J1": (20.0, 4.6, 180, "F"), "J2": (48.0, 4.4, 180, "F"), "J3": (31.75, 84.5, 0, "F"),
    "U1": (28.0, 26.0, 270, "F"),        # CH32 MEU6 QFN88 rot 270: USB3 (84-88) top-left -> J1, QSPI bottom, SDMMC right
    "J4": (54.0, 30.0, 90, "F"),         # microSD on the right edge, near SDMMC pins (85-101)
    "U10": (5.6, 27.0, 0, "F"),          # ADC10065 far left
    "U11": (34.5, 14.5, 90, "F"), "U12": (16.8, 22.5, 0, "F"), "U13": (35.0, 37.0, 90, "F"),   # 2:1 switch within ~10 mm of its DVP pins (D57)
    "U3": (12.0, 49.0, 0, "F"), "Y1": (12.0, 43.2, 0, "F"),
    "J5": (2.6, 52.0, 0, "F"),           # 1x4 header on the left edge
    "U2": (31.0, 62.0, 0, "F"), "Y3": (20.5, 62.0, 0, "F"),
    "Y2": (19.8, 31.0, 90, "F"),
    "U4": (13.0, 12.0, 0, "F"), "D1": (27.5, 10.5, 0, "F"), "D4": (17.0, 9.4, 0, "F"),
    "D2": (48.0, 11.0, 0, "F"), "D3": (31.75, 78.0, 0, "F"),
    "U5": (8.0, 9.0, 0, "F"), "U6": (57.0, 11.0, 0, "F"), "U7": (41.0, 80.0, 0, "F"),
    "U8": (54.0, 66.0, 0, "F"), "L1": (54.0, 71.5, 0, "F"), "U9": (52.0, 50.0, 0, "F"),
    "SW1": (10.0, 79.0, 0, "F"), "SW2": (54.0, 79.0, 0, "F"),
    "JP1": (3.5, 38.0, 90, "F"), "D5": (6.5, 58.0, 0, "F"),
    "H1": (3.5, 3.5, 0, "F"), "H2": (W - 3.5, 3.5, 0, "F"), "H3": (3.5, H - 3.5, 0, "F"),
    "H4": (W - 3.5, H - 3.5, 0, "F"),
}
ANCHOR_BY_SHEET = {"/CH32H417/": "U1", "/RP2354B supervisor/": "U2", "/Clocks + analog/": "U3",
                   "/microSD + RP-CH32 links/": "U1", "/USB + ESD/": "J1", "/Power/": "U8"}
RAILS = {"GND", "+3V3", "+3V3_CH", "+3V3A_CH", "+5V_SYS", "+1V1", "VDDK", "VDD12A"}


def place(fp, x, y, rot, side):
    fp.SetPosition(P(x, y))
    fp.SetOrientationDegrees(rot)
    if side == "B" and not fp.IsFlipped():
        fp.Flip(fp.GetPosition(), pcbnew.FLIP_DIRECTION_LEFT_RIGHT)


occupied = {"F": [], "B": []}


def rect_of(fp, margin=0.25):
    """union of courtyard and pad extents (easyeda courtyards can be smaller than the pads)."""
    to = lambda v: pcbnew.ToMM(v)
    boxes = []
    cy = fp.GetCourtyard(pcbnew.B_CrtYd if fp.IsFlipped() else pcbnew.F_CrtYd)
    if cy.OutlineCount():
        boxes.append(cy.BBox())
    for pad in fp.Pads():
        boxes.append(pad.GetBoundingBox())
    if not boxes:
        boxes.append(fp.GetBoundingBox(False))
    l = min(to(b.GetLeft()) for b in boxes); t = min(to(b.GetTop()) for b in boxes)
    r = max(to(b.GetRight()) for b in boxes); bt = max(to(b.GetBottom()) for b in boxes)
    return (l - OX - margin, t - OY - margin, r - OX + margin, bt - OY + margin)


def overlaps(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def mark(fp, sides):
    rc = rect_of(fp)
    for s in sides:
        occupied[s].append(rc)


for ref, (x, y, rot, side) in FIX.items():
    place(fps[ref], x, y, rot, side)
    th = any(p.GetAttribute() == pcbnew.PAD_ATTRIB_PTH for p in fps[ref].Pads()) or ref.startswith("H")
    mark(fps[ref], ["F", "B"] if th else [side])


IC_LIKE = [r for r in FIX if not r.startswith("H")]
served = {}
mm = lambda v: pcbnew.ToMM(v)


def nets_of(ref):
    return {pin_net[k] for k in pin_net if k[0] == ref}


def pad_xy(pad):
    p = pad.GetPosition()
    return mm(p.x) - OX, mm(p.y) - OY


def edge_of(icref, pad):
    """Which IC edge the pad sits on -> (outward unit vector, axis 'h' or 'v')."""
    l, t, r, b = rect_of(fps[icref], 0)
    cx, cy = (l + r) / 2, (t + b) / 2
    px, py = pad_xy(pad)
    ex, ey = (px - cx) / max(0.5, (r - l) / 2), (py - cy) / max(0.5, (b - t) / 2)
    if abs(ex) >= abs(ey):
        return ((1 if ex > 0 else -1), 0), "h"
    return (0, (1 if ey > 0 else -1)), "v"


def target_for(ref):
    """(ic ref, ic pad, net) the passive belongs to.  Signal nets first, then decoupling round-robin."""
    ns = nets_of(ref)
    cand = []
    for n in sorted(ns - RAILS):
        for r2, pn in nets[n]:
            if r2 in IC_LIKE:
                for pad in fps[r2].Pads():
                    if pad.GetNumber() == pn:
                        cand.append((0 if r2.startswith("U") else 1, r2, pad, n))
    if cand:
        cand.sort(key=lambda c: c[0])
        return cand[0][1:], False
    sheet = comps[ref]["sheet"]
    for n in sorted(ns - {"GND"}):
        opts = []
        for r2 in IC_LIKE:
            same = comps.get(r2, {}).get("sheet") == sheet
            for pad in fps[r2].Pads():
                if pad.GetNetname() == n:
                    opts.append((served.get((r2, pad.GetNumber()), 0), 0 if same else 1,
                                 0 if r2.startswith("U") else 1, r2, pad))
        if opts:
            opts.sort(key=lambda o: o[:3])
            _, _, _, r2, pad = opts[0]
            served[(r2, pad.GetNumber())] = served.get((r2, pad.GetNumber()), 0) + 1
            return (r2, pad, n), True
    return (ANCHOR_BY_SHEET.get(sheet, "U1"), None, None), True


def axis_rots(fp, x, y, side, axis):
    """rotations that give the 2-pad part the wanted axis ('h' horizontal / 'v' vertical)."""
    out = []
    for rot in (0, 90, 180, 270):
        place(fp, x, y, rot, side)
        pads = list(fp.Pads())
        (x1, y1), (x2, y2) = pad_xy(pads[0]), pad_xy(pads[-1])
        if (abs(x2 - x1) > abs(y2 - y1)) == (axis == "h"):
            out.append(rot)
    return out


def facing_rot(fp, x, y, side, rots, net, tgt):
    """among rots, the one whose pad on `net` is closest to the IC pin."""
    best = None
    for rot in rots:
        place(fp, x, y, rot, side)
        d = min((math.dist(pad_xy(p), tgt) for p in fp.Pads() if p.GetNetname() == net), default=0)
        if best is None or d < best[0]:
            best = (d, rot)
    return best[1]


def try_place(fp, tx, ty, side, rots, maxr=40):
    for rad in [i * 0.25 for i in range(0, int(maxr / 0.25))]:
        steps = max(1, int(2 * math.pi * rad / 0.35))
        for k in range(steps):
            a = 2 * math.pi * k / steps
            x, y = tx + rad * math.cos(a), ty + rad * math.sin(a)
            for rot in rots:
                place(fp, x, y, rot, side)
                rc = rect_of(fp)
                if rc[0] < 0.4 or rc[1] < 0.4 or rc[2] > W - 0.4 or rc[3] > H - 0.4:
                    continue
                if any(overlaps(rc, o) for o in occupied[side]):
                    continue
                occupied[side].append(rc)
                return True
    return False


free = [r for r in fps if r not in FIX]
info = {r: target_for(r) for r in free}
# decoupling first (bottom, under its own pin), then signal passives nearest their IC pin
free.sort(key=lambda r: (0 if info[r][1] else 1, comps[r]["sheet"], r))
unplaced, not_perp = [], []
for ref in free:
    fp = fps[ref]
    (icref, icpad, net), decoup = info[ref]
    ns = nets_of(ref)
    # D48: decoupling, series-R arrays, bias networks on the bottom
    side = "B" if (ref.startswith("C") and "GND" in ns) or (comps[ref]["sheet"] == "/microSD + RP-CH32 links/"
                                                           and ref.startswith("R")) else "F"
    if ref.startswith("R") and ns <= RAILS | {"ADC_V3V3CH", "ADC_VSYS", "BUCK_FB", "CH_PWR_EN", "USB_SEL"}:
        side = "B"
    if icpad is None:
        c = fps[icref].GetPosition()
        ok = try_place(fp, mm(c.x) - OX, mm(c.y) - OY, side, [0, 90])
        not_perp.append(ref)
    else:
        (ox, oy), edge_axis = edge_of(icref, icpad)
        px, py = pad_xy(icpad)
        # user rule: long axis perpendicular to the IC edge, IC-side pad facing the pin
        want = edge_axis
        off = 0.0 if side == "B" and decoup else 1.4
        tx, ty = px + ox * off, py + oy * off
        rots = axis_rots(fp, tx, ty, side, want)
        rot = facing_rot(fp, tx, ty, side, rots, net, (px, py))
        ok = try_place(fp, tx, ty, side, [rot], maxr=25)
        if not ok:
            ok = try_place(fp, tx, ty, side, rots + [r for r in (0, 90, 180, 270) if r not in rots])
            not_perp.append(ref)
    if not ok:
        unplaced.append(ref)
print("UNPLACED:", unplaced)
print("not perpendicular / no IC pin:", not_perp)

# ------------------------------------------------------------------ zones
def zone(layer, net, pts, prio=0):
    z = pcbnew.ZONE(board)
    z.SetLayer(layer)
    z.SetNet(netinfo[net])
    z.SetAssignedPriority(prio)
    z.SetLocalClearance(MM(0.2))
    z.SetMinThickness(MM(0.15))
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL if layer in (pcbnew.F_Cu, pcbnew.B_Cu)
                       else pcbnew.ZONE_CONNECTION_FULL)
    ol = z.Outline()
    ol.NewOutline()
    for x, y in pts:
        ol.Append(MM(OX + x), MM(OY + y))
    board.Add(z)


full = [(0.3, 0.3), (W - 0.3, 0.3), (W - 0.3, H - 0.3), (0.3, H - 0.3)]
zone(pcbnew.In1_Cu, "GND", full)
zone(pcbnew.In4_Cu, "GND", full)
# In3: +3V3_CH under the CH32 domain (top 46 mm), +3V3 below it
zone(pcbnew.In3_Cu, "+3V3_CH", [(0.3, 0.3), (W - 0.3, 0.3), (W - 0.3, 44), (0.3, 44)], 1)
zone(pcbnew.In3_Cu, "+3V3", [(0.3, 45), (W - 0.3, 45), (W - 0.3, H - 0.3), (0.3, H - 0.3)], 1)
zone(pcbnew.F_Cu, "GND", full)
zone(pcbnew.B_Cu, "GND", full)

out = os.path.join(BUILD, "rp417_placed.kicad_pcb")
import shutil; shutil.copy(os.path.join(HW, "rp417.kicad_pro"), os.path.join(BUILD, "rp417_placed.kicad_pro"))
board.Save(out)
pcbnew.ExportSpecctraDSN(board, os.path.join(BUILD, "rp417.dsn"))
print("saved", out, "footprints", len(fps), "unplaced", len(unplaced))
