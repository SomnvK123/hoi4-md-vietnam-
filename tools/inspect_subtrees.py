import re
from pathlib import Path
from collections import defaultdict
import sys

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
    muts = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses.append({
        "id": fid, "x": int(xm.group(1)) if xm else 0, "y": int(ym.group(1)) if ym else 0,
        "rel": rel.group(1) if rel else None, "prereqs": prereqs, "muts": muts,
        "block": block, "start": start, "end": end
    })

fmap = {f["id"]: f for f in focuses}

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = fmap.get(fid)
    if not f or not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], visited)
    return rx + f["x"], ry + f["y"]

for f in focuses:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

rel_children = defaultdict(list)
for f in focuses:
    if f["rel"]:
        rel_children[f["rel"]].append(f["id"])

# Print subtrees anchored to specific roots
for root in ["VIE_enterprise_law", "VIE_state_bank_modernization", "VIE_infrastructure_development",
             "VIE_industrialization_strategy", "VIE_internet_expansion", "VIE_upper_middle_income",
             "VIE_vinacomin_founding"]:
    ch = rel_children[root]
    print(f"\nSubtree of {root} ({len(ch)} direct children):")
    for c in ch:
        cf = fmap[c]
        print(f"  {c:35s} rel=({cf['x']:3d},{cf['y']:2d}) abs=({cf['abs_x']:3d},{cf['abs_y']:2d}) prereqs={cf['prereqs']}")
