"""Draw a keyboard picture (SVG) from a Microsoft Keyboard Layout Creator .klc file.

Usage: python scripts/klc_to_svg.py src/current/EnDe2611.klc docs/img/EnDe2611.svg
Each key shows: base (bottom left), Shift (top left), AltGr (bottom right),
Shift+AltGr (top right). Dead keys are drawn in orange.
"""
import sys
from html import escape

COLS = ["0", "1", "2", "6", "7"]  # base, shift, ctrl, altgr, shift+altgr


def parse(path):
    text = open(path, encoding="utf-16").read()
    lines = text.splitlines()
    shift_states, keys, dead = [], {}, set()
    section = None
    for raw in lines:
        line = raw.split("//")[0].strip()
        if not line:
            continue
        word = line.split()[0]
        if word in ("SHIFTSTATE", "LAYOUT", "DEADKEY", "KEYNAME", "KEYNAME_EXT",
                    "KEYNAME_DEAD", "DESCRIPTIONS", "LANGUAGENAMES", "ENDKBD"):
            section = word
            continue
        if section == "SHIFTSTATE":
            shift_states.append(word)
        elif section == "LAYOUT":
            parts = line.split()
            sc, vals = parts[0].lower(), parts[3:3 + len(shift_states)]
            cell = {}
            for st, v in zip(shift_states, vals):
                is_dead = v.endswith("@")
                v = v.rstrip("@")
                if v == "-1":
                    continue
                ch = v if len(v) == 1 else chr(int(v, 16))
                if ord(ch) < 0x20:
                    continue
                cell[st] = (ch, is_dead)
            keys[sc] = cell
    return keys


ROWS = [
    [("29", 1), ("02", 1), ("03", 1), ("04", 1), ("05", 1), ("06", 1), ("07", 1), ("08", 1),
     ("09", 1), ("0a", 1), ("0b", 1), ("0c", 1), ("0d", 1), ("Backspace", 2)],
    [("Tab", 1.5), ("10", 1), ("11", 1), ("12", 1), ("13", 1), ("14", 1), ("15", 1), ("16", 1),
     ("17", 1), ("18", 1), ("19", 1), ("1a", 1), ("1b", 1), ("Enter", 1.5)],
    [("Caps", 1.75), ("1e", 1), ("1f", 1), ("20", 1), ("21", 1), ("22", 1), ("23", 1), ("24", 1),
     ("25", 1), ("26", 1), ("27", 1), ("28", 1), ("2b", 1), ("", 1.25)],
    [("Shift", 1.25), ("56", 1), ("2c", 1), ("2d", 1), ("2e", 1), ("2f", 1), ("30", 1), ("31", 1),
     ("32", 1), ("33", 1), ("34", 1), ("35", 1), ("Shift ", 2.75)],
    [("Ctrl", 1.5), ("Win", 1.25), ("Alt", 1.25), ("39", 6.25), ("AltGr", 1.25), ("Win ", 1.25),
     ("Ctrl ", 1.5)],
]

U = 64  # key unit in px
GAP = 6
INK, ALT, DEAD, MUTED = "#1F1F1F", "#0B57D0", "#B45309", "#5F6368"
SPACE_NAMES = {" ": "нп", " ": "узк. нп", " ": ""}


def label(ch):
    return SPACE_NAMES.get(ch, ch)


def draw(keys, title):
    width = 15 * U
    out = []
    y = 0
    for row in ROWS:
        x = 0
        for name, w in row:
            kw, kh = w * U - GAP, U - GAP
            cell = keys.get(name)
            is_mod = cell is None
            fill = "#E8EEF7" if is_mod else "#FFFFFF"
            if name == "AltGr":
                fill = "#D3E3FD"
            out.append(f'<rect x="{x}" y="{y}" width="{kw}" height="{kh}" rx="10" '
                       f'fill="{fill}" stroke="#C4CBD6"/>')
            if is_mod:
                if name.strip():
                    color = ALT if name == "AltGr" else MUTED
                    out.append(f'<text x="{x + 8}" y="{y + kh - 10}" font-size="12" '
                               f'fill="{color}">{escape(name.strip())}</text>')
            else:
                base, shift = cell.get("0"), cell.get("1")
                alt, salt = cell.get("6"), cell.get("7")
                if name == "39":
                    parts = []
                    if alt:
                        parts.append(f"правый Alt: {label(alt[0])}")
                    if salt:
                        parts.append(f"Shift + правый Alt: {label(salt[0])}")
                    out.append(f'<text x="{x + kw / 2}" y="{y + kh / 2 + 5}" font-size="13" '
                               f'text-anchor="middle" fill="{ALT}">{escape("   ·   ".join(parts))}</text>')
                else:
                    letter_pair = (base and shift and base[0].isalpha()
                                   and shift[0] == base[0].upper() and base[0] != shift[0])
                    if letter_pair:
                        out.append(f'<text x="{x + 9}" y="{y + 26}" font-size="22" font-weight="500" '
                                   f'fill="{INK}">{escape(shift[0])}</text>')
                    else:
                        if shift:
                            out.append(f'<text x="{x + 9}" y="{y + 22}" font-size="17" '
                                       f'fill="{INK}">{escape(label(shift[0]))}</text>')
                        if base:
                            out.append(f'<text x="{x + 9}" y="{y + kh - 9}" font-size="19" font-weight="500" '
                                       f'fill="{INK}">{escape(label(base[0]))}</text>')
                    for val, ty in ((salt, y + 22), (alt, y + kh - 9)):
                        if val:
                            color = DEAD if val[1] else ALT
                            out.append(f'<text x="{x + kw - 8}" y="{ty}" font-size="16" '
                                       f'text-anchor="end" fill="{color}">{escape(label(val[0]))}</text>')
            x += w * U
        y += U
    height = 5 * U
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 {width + 2} {height + 2}" '
            f'role="img" aria-label="{escape(title)}" '
            f'font-family="Roboto, \'Segoe UI\', \'Segoe UI Symbol\', \'Noto Sans\', \'Noto Sans Symbols 2\', sans-serif">'
            f'<title>{escape(title)}</title>' + "".join(out) + "</svg>\n")


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else src
    open(dst, "w", encoding="utf-8").write(draw(parse(src), title))
