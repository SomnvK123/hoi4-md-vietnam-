import re
from pathlib import Path
from collections import defaultdict
import sys

# Load current focuses
txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focus_matches = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    end = m.end()
    for i in range(m.end(), len(txt)):
        if txt[i] == "{": brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    x = int(re.search(r"\bx\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\bx\s*=\s*(-?\d+)", block) else 0
    y = int(re.search(r"\by\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\by\s*=\s*(-?\d+)", block) else 0
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    rel = rel.group(1) if rel else None
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereqs": prereqs,
        "block": block, "order": len(focus_matches)
    })

fmap = {f["id"]: f for f in focus_matches}

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = fmap.get(fid)
    if not f: return 0, 0
    if not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], visited)
    return rx + f["x"], ry + f["y"]

for f in focus_matches:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

print(f"Loaded {len(focus_matches)} focuses.")
