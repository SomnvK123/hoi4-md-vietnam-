import re
from pathlib import Path
from collections import defaultdict

txt = Path(r"d:\HOI4Mods\md_vietnam\common\national_focus\VIE_md_focus.txt").read_text(encoding="utf-8")

focus_matches = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    end = m.end()
    for i in range(m.end(), len(txt)):
        if txt[i] == "{":
            brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    id_m = re.search(r"\bid\s*=\s*(\S+)", block)
    if not id_m:
        continue
    fid = id_m.group(1)
    x_m = re.search(r"\bx\s*=\s*(-?\d+)", block)
    y_m = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel_m = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereq_m = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    filters_m = re.findall(r"\bsearch_filters\s*=\s*\{([^}]+)\}", block)
    filters = filters_m[0].split() if filters_m else []

    x = int(x_m.group(1)) if x_m else 0
    y = int(y_m.group(1)) if y_m else 0
    rel = rel_m.group(1) if rel_m else None
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereq": prereq_m, "filters": filters
    })

fmap = {f["id"]: f for f in focus_matches}


def get_abs(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return 0, 0
    visited.add(fid)
    f = fmap.get(fid)
    if not f:
        return 0, 0
    if not f["rel"]:
        return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], visited)
    return rx + f["x"], ry + f["y"]


for f in focus_matches:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

# Print all focuses grouped by their top-level subtrees or sections
# Let's see what roots / sub-roots exist
# In HOI4, root focuses are those with NO prerequisite.
no_prereq = [f for f in focus_matches if not f["prereq"]]
print(f"Focuses with NO prerequisite ({len(no_prereq)}):")
for f in no_prereq:
    print(f"  {f['id']:35s} | abs_x={f['abs_x']:3d}, abs_y={f['abs_y']:3d} | rel={f['rel']}")
