import re
from pathlib import Path
from collections import defaultdict
import sys

# Load current focus blocks
txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focuses = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == "{": brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses.append({
        "id": fid, "x": int(xm.group(1)) if xm else 0, "y": int(ym.group(1)) if ym else 0,
        "rel": rel.group(1) if rel else None, "prereqs": prereqs,
        "block": block, "start": start, "end": end
    })

fmap = {f["id"]: f for f in focuses}

def get_abs(fid, dmap, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = dmap.get(fid)
    if not f or not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], dmap, visited)
    return rx + f["x"], ry + f["y"]

print(f"Loaded {len(focuses)} focuses.")
