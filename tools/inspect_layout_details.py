import re
from pathlib import Path
from collections import defaultdict

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
    prereq = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereq": prereq, 
        "start": start, "end": end, "order": len(focus_matches)
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

anchor_roots = [f["id"] for f in focus_matches if f["rel"] is None]
print("Anchor roots (rel is None):", anchor_roots)

direct_to_doi_moi = [f["id"] for f in focus_matches if f["rel"] == "VIE_doi_moi_continues"]
print("\nDirectly anchored to VIE_doi_moi_continues:")
for d in direct_to_doi_moi:
    f = fmap[d]
    print(f"  {d:32s} rel=({f['x']:3d},{f['y']:3d}) abs=({f['abs_x']:3d},{f['abs_y']:3d})")

# Let's see anchor tree children
rel_children = defaultdict(list)
for f in focus_matches:
    if f["rel"]:
        rel_children[f["rel"]].append(f["id"])

print("\nSubtree sizes for each direct child of VIE_doi_moi_continues:")
for d in direct_to_doi_moi:
    # BFS
    q = [d]
    sub = []
    while q:
        curr = q.pop(0)
        sub.append(curr)
        for c in rel_children[curr]:
            q.append(c)
    xs = [fmap[x]["abs_x"] for x in sub]
    ys = [fmap[x]["abs_y"] for x in sub]
    print(f"  {d:32s}: count={len(sub):3d} | x:[{min(xs):3d}, {max(xs):3d}] | y:[{min(ys):3d}, {max(ys):3d}]")

