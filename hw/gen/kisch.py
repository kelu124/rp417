"""Minimal KiCad schematic writer for rp417 (label-based, one symbol per part).

Each pin gets a 2.54 mm wire stub ending in a global label with its net name,
or a no-connect flag. Symbols are embedded from .kicad_sym libraries.
"""
import re, uuid, math, os

STOCK_SYM = "/usr/share/kicad/symbols"
HERE = os.path.dirname(os.path.abspath(__file__))
HW = os.path.dirname(HERE)
LIBS = {"lcsc": os.path.join(HW, "lib", "lcsc.kicad_sym"),
        "rp417": os.path.join(HW, "lib", "rp417.kicad_sym")}


def U():
    return str(uuid.uuid4())


def block_at(s, start):
    """Return the balanced (...) block starting at index start."""
    depth = 0
    i = start
    instr = False
    while i < len(s):
        c = s[i]
        if instr:
            if c == '\\':
                i += 2
                continue
            if c == '"':
                instr = False
        else:
            if c == '"':
                instr = True
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return s[start:i + 1]
        i += 1
    raise ValueError("unbalanced")


_libcache = {}


def lib_text(lib):
    if lib not in _libcache:
        path = LIBS.get(lib, os.path.join(STOCK_SYM, lib + ".kicad_sym"))
        _libcache[lib] = open(path).read()
    return _libcache[lib]


class Sym:
    def __init__(self, lib, name, retype=None):
        self.lib, self.name = lib, name
        s = lib_text(lib)
        m = re.search(r'\(symbol "%s"' % re.escape(name), s)
        if not m:
            raise KeyError(f"{lib}:{name}")
        blk = block_at(s, m.start())
        if '(extends ' in blk:
            raise ValueError(f"{lib}:{name} uses extends; use the base symbol")
        for num, t in (retype or {}).items():   # e.g. ORed power outputs -> passive
            blk = re.sub(r'\(pin \w+ (\w+)((?:(?!\(pin ).)*?\(number "%s")' % re.escape(num),
                         lambda m: f'(pin {t} {m.group(1)}{m.group(2)}', blk, count=1, flags=re.S)
        self.raw = blk
        self.pins = []  # (number, name, type, x, y, rot)
        for pm in re.finditer(r'\(pin (\w+) \w+', blk):
            pb = block_at(blk, pm.start())
            at = re.search(r'\(at ([-\d.]+) ([-\d.]+)(?: ([-\d.]+))?\)', pb)
            nm = re.search(r'\(name "([^"]*)"', pb).group(1)
            nu = re.search(r'\(number "([^"]*)"', pb).group(1)
            x, y = float(at.group(1)), float(at.group(2))
            r = float(at.group(3) or 0)
            self.pins.append((nu, nm, pm.group(1), x, y, int(r) % 360))
        xs = [p[3] for p in self.pins] or [0]
        ys = [p[4] for p in self.pins] or [0]
        self.bbox = (min(xs), min(ys), max(xs), max(ys))

    def lib_symbol_text(self):
        # rename top-level symbol to "lib:name"; sub-unit names stay
        t = self.raw.replace(f'(symbol "{self.name}"', f'(symbol "{self.lib}:{self.name}"', 1)
        return t

    def pin_by_name(self, name):
        """Match full name, or the part before '/', or a regex."""
        out = []
        for p in self.pins:
            full = p[1]
            base = full.split('/')[0]
            if full == name or base == name:
                out.append(p)
        return out


def q(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def fmt(v):
    return ('%.3f' % v).rstrip('0').rstrip('.')


class Part:
    def __init__(self, ref, sym, value, fp, conns, lcsc="", dnp=False, mpn=""):
        self.ref, self.sym, self.value, self.fp = ref, sym, value, fp
        self.conns = conns  # pin number -> net name, or None for NC
        self.lcsc, self.dnp, self.mpn = lcsc, dnp, mpn
        self.in_bom = True   # D68: False for mounting holes / solder jumpers
        missing = [p[0] for p in sym.pins if p[0] not in conns]
        if missing:
            raise ValueError(f"{ref}: unassigned pins {missing}")
        extra = [k for k in conns if k not in {p[0] for p in sym.pins}]
        if extra:
            raise ValueError(f"{ref}: unknown pins {extra}")


def label_len(net):
    return 1.27 * 0.85 * len(net) + 3.5


class Sheet:
    def __init__(self, name, fname, paper="A2"):
        self.name, self.fname, self.paper = name, fname, paper
        self.parts = []
        self.uuid = U()
        self.sheet_uuid = U()  # uuid of the sheet symbol in root

    def add(self, part):
        self.parts.append(part)
        return part

    def write(self, outdir, root_uuid, project, texts=()):
        W, H = {"A1": (841, 594), "A2": (594, 420), "A3": (420, 297), "A0": (1189, 841)}[self.paper]
        syms = {}
        items = []
        x0, y0 = 20.0, 25.0
        cx, cy, rowh = x0, y0, 0.0
        for p in self.parts:
            s = p.sym
            syms[f"{s.lib}:{s.name}"] = s
            bx0, by0, bx1, by1 = s.bbox
            # extent of labels on left/right
            left = max([label_len(p.conns[n] or '') + 3 for (n, nm, t, x, y, r) in s.pins if r == 0] + [3])
            right = max([label_len(p.conns[n] or '') + 3 for (n, nm, t, x, y, r) in s.pins if r == 180] + [3])
            top = max([label_len(p.conns[n] or '') + 3 for (n, nm, t, x, y, r) in s.pins if r == 270] + [3])
            bot = max([label_len(p.conns[n] or '') + 3 for (n, nm, t, x, y, r) in s.pins if r == 90] + [3])
            w = (bx1 - bx0) + left + right + 6
            h = (by1 - by0) + top + bot + 8
            if cx + w > W - 15 and cx > x0:
                cx = x0
                cy += rowh
                rowh = 0
            # symbol origin so that bbox fits: sch y = Y - y
            X = cx + left - bx0
            Y = cy + top + by1 + 4
            X = round(X / 1.27) * 1.27
            Y = round(Y / 1.27) * 1.27
            cx += w
            rowh = max(rowh, h)
            items.append(self._symbol(p, X, Y, root_uuid, project))
            for (n, nm, t, px, py, r) in s.pins:
                ax, ay = X + px, Y - py
                net = p.conns[n]
                if net is None:
                    items.append(f'(no_connect (at {fmt(ax)} {fmt(ay)}) (uuid {q(U())}))')
                    continue
                ox, oy, ang = {0: (-1, 0, 180), 180: (1, 0, 0), 90: (0, 1, 270), 270: (0, -1, 90)}[r]
                ex, ey = ax + ox * 2.54, ay + oy * 2.54
                items.append(f'(wire (pts (xy {fmt(ax)} {fmt(ay)}) (xy {fmt(ex)} {fmt(ey)})) '
                             f'(stroke (width 0) (type default)) (uuid {q(U())}))')
                just = {0: "left", 180: "right", 90: "left", 270: "right"}[ang]
                items.append(f'(global_label {q(net)} (shape passive) (at {fmt(ex)} {fmt(ey)} {ang}) '
                             f'(fields_autoplaced yes) (effects (font (size 1.27 1.27)) (justify {just})) '
                             f'(uuid {q(U())}) (property "Intersheetrefs" "${{INTERSHEET_REFS}}" '
                             f'(at {fmt(ex)} {fmt(ey)} 0) (effects (font (size 1.27 1.27)) (hide yes))))')
        tx = ''.join(f'(text {q(t)} (exclude_from_sim no) (at 20 {12 + 6 * i} 0) '
                     f'(effects (font (size 2 2)) (justify left)) (uuid {q(U())}))\n'
                     for i, t in enumerate(texts))
        libs = '\n'.join(s.lib_symbol_text() for s in syms.values())
        out = (f'(kicad_sch (version 20250114) (generator "eeschema") (generator_version "9.0")\n'
               f'(uuid {q(self.uuid)})\n(paper {q(self.paper)})\n'
               f'(title_block (title {q("rp417 - " + self.name)}) (date "2026-11-13") (rev "A-draft") '
               f'(comment 1 "Generated by hw/gen/build.py - edit the generator, not this file"))\n'
               f'(lib_symbols\n{libs}\n)\n' + tx + '\n'.join(items) + '\n(embedded_fonts no)\n)\n')
        open(os.path.join(outdir, self.fname), 'w').write(out)

    def _symbol(self, p, X, Y, root_uuid, project):
        s = p.sym
        bx0, by0, bx1, by1 = s.bbox
        ry = Y - by1 - 3
        props = [("Reference", p.ref, X + bx0, ry, False),
                 ("Value", p.value, X + bx0, ry - 2.5 if False else Y - by0 + 3, False),
                 ("Footprint", p.fp, X, Y, True),
                 ("Datasheet", "", X, Y, True),
                 ("Description", "", X, Y, True),
                 ("LCSC", p.lcsc, X, Y, True),
                 ("MPN", p.mpn or p.value, X, Y, True)]
        pr = ''.join(f'(property {q(k)} {q(v)} (at {fmt(px)} {fmt(py)} 0) '
                     f'(effects (font (size 1.27 1.27)) (justify left){" (hide yes)" if hid else ""}))'
                     for k, v, px, py, hid in props)
        pins = ''.join(f'(pin {q(n)} (uuid {q(U())}))' for (n, *_r) in s.pins)
        return (f'(symbol (lib_id {q(s.lib + ":" + s.name)}) (at {fmt(X)} {fmt(Y)} 0) (unit 1) '
                f'(exclude_from_sim no) (in_bom {"yes" if p.in_bom else "no"}) (on_board yes) (dnp {"yes" if p.dnp else "no"}) '
                f'(fields_autoplaced yes) (uuid {q(U())}) {pr} {pins} '
                f'(instances (project {q(project)} (path {q("/" + root_uuid + "/" + self.sheet_uuid)} '
                f'(reference {q(p.ref)}) (unit 1)))))')


def write_root(outdir, project, sheets, root_uuid, notes=()):
    items = []
    x, y = 25.0, 40.0
    for i, sh in enumerate(sheets):
        items.append(
            f'(sheet (at {fmt(x)} {fmt(y)}) (size 60 20) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) '
            f'(fields_autoplaced yes) (stroke (width 0.1524) (type solid)) (fill (color 0 0 0 0.0000)) '
            f'(uuid {q(sh.sheet_uuid)}) '
            f'(property "Sheetname" {q(sh.name)} (at {fmt(x)} {fmt(y - 0.7)} 0) (effects (font (size 1.6 1.6)) (justify left bottom))) '
            f'(property "Sheetfile" {q(sh.fname)} (at {fmt(x)} {fmt(y + 20.6)} 0) (effects (font (size 1.27 1.27)) (justify left top))) '
            f'(instances (project {q(project)} (path {q("/" + root_uuid)} (page {q(str(i + 2))})))))')
        x += 75
        if x > 330:
            x = 25.0
            y += 40
    tx = ''.join(f'(text {q(t)} (exclude_from_sim no) (at 25 {150 + 6 * i} 0) (effects (font (size 2 2)) (justify left)) (uuid {q(U())}))\n'
                 for i, t in enumerate(notes))
    out = (f'(kicad_sch (version 20250114) (generator "eeschema") (generator_version "9.0")\n'
           f'(uuid {q(root_uuid)})\n(paper "A3")\n'
           f'(title_block (title "rp417 - CH32H417 test board supervised by an RP2350") (date "2026-11-13") (rev "A-draft"))\n'
           f'(lib_symbols)\n' + tx + '\n'.join(items) +
           '\n(sheet_instances (path "/" (page "1")))\n(embedded_fonts no)\n)\n')
    open(os.path.join(outdir, project + ".kicad_sch"), 'w').write(out)


def make_ic_symbol(name, pins, ref="U", body_w=20.32):
    """pins: list of (number, name, type, side) side in L/R/T/B. Returns kicad_sym symbol text."""
    L = [p for p in pins if p[3] == 'L']
    R = [p for p in pins if p[3] == 'R']
    n = max(len(L), len(R))
    h = (n + 1) * 2.54
    top = h / 2
    top = math.ceil(top / 2.54) * 2.54
    out = []
    for side, lst in (('L', L), ('R', R)):
        for i, (num, nm, t, _s) in enumerate(lst):
            y = top - 2.54 * (i + 1)
            if side == 'L':
                x, r = -body_w / 2 - 5.08, 0
            else:
                x, r = body_w / 2 + 5.08, 180
            out.append(f'(pin {t} line (at {fmt(x)} {fmt(y)} {r}) (length 5.08) '
                       f'(name {q(nm)} (effects (font (size 1.27 1.27)))) '
                       f'(number {q(num)} (effects (font (size 1.27 1.27)))))')
    bot = top - 2.54 * (n + 1)
    return (f'(symbol {q(name)} (exclude_from_sim no) (in_bom yes) (on_board yes)\n'
            f' (property "Reference" {q(ref)} (at 0 {fmt(top + 2)} 0) (effects (font (size 1.27 1.27))))\n'
            f' (property "Value" {q(name)} (at 0 {fmt(bot - 2)} 0) (effects (font (size 1.27 1.27))))\n'
            f' (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f' (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f' (property "Description" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
            f' (symbol {q(name + "_0_1")} (rectangle (start {fmt(-body_w / 2)} {fmt(top)}) (end {fmt(body_w / 2)} {fmt(bot)}) '
            f'(stroke (width 0.254) (type default)) (fill (type background))))\n'
            f' (symbol {q(name + "_1_1")} ' + ' '.join(out) + '))')
