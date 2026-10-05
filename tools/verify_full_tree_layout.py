import sys, os
sys.path.insert(0, os.path.abspath("."))
import re

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos = 0
focuses = {}
focus_list = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                block = text[start:i+1]
                id_m = re.search(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                x_m = re.search(r'^\s*x\s*=\s*(-?\d+)', block, re.MULTILINE)
                y_m = re.search(r'^\s*y\s*=\s*(-?\d+)', block, re.MULTILINE)
                rel_m = re.search(r'^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)', block, re.MULTILINE)
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', block)
                if id_m:
                    fid = id_m.group(1)
                    f_data = {
                        'id': fid,
                        'x': int(x_m.group(1)) if x_m else 0,
                        'y': int(y_m.group(1)) if y_m else 0,
                        'rel': rel_m.group(1) if rel_m else None,
                        'prereqs': prereqs,
                        'order': len(focus_list)
                    }
                    focuses[fid] = f_data
                    focus_list.append(f_data)
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"=== FULL TREE VERIFICATION REPORT ===")
print(f"Total focuses parsed in tree: {len(focus_list)} (expected 410)")

# Check forward references
fwd_refs = []
for f in focus_list:
    if f['rel']:
        if f['rel'] not in focuses:
            fwd_refs.append(f"{f['id']} references unknown rel {f['rel']}")
        elif focuses[f['rel']]['order'] >= f['order']:
            fwd_refs.append(f"{f['id']} (order {f['order']}) references future {f['rel']} (order {focuses[f['rel']]['order']})")

print(f"Forward references across entire file: {len(fwd_refs)}")
for fr in fwd_refs:
    print("  ", fr)

# Check collisions
def get_abs(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f['rel']:
        return (f['x'], f['y'])
    px, py = get_abs(f['rel'], visited)
    return (px + f['x'], py + f['y'])

abs_coords = {}
for f in focus_list:
    abs_coords[f['id']] = get_abs(f['id'])

coord_map = {}
collisions = []
for f in focus_list:
    pos_abs = abs_coords[f['id']]
    if pos_abs in coord_map:
        collisions.append((f['id'], coord_map[pos_abs], pos_abs))
    else:
        coord_map[pos_abs] = f['id']

print(f"Total coordinate collisions across entire file: {len(collisions)}")
for c in collisions:
    print("  ", c)

# Check military focuses specifically
import tools.test_military_layout as tml
mil_fids = set(tml.military_layout.keys())
rows = {}
for fid in mil_fids:
    ax, ay = abs_coords[fid]
    rows.setdefault(ay, []).append((ax, fid))

gap_violations = []
for y in sorted(rows.keys()):
    items = sorted(rows[y], key=lambda x: x[0])
    for k in range(len(items) - 1):
        dx = items[k+1][0] - items[k][0]
        if dx < 2:
            gap_violations.append((items[k][1], items[k+1][1], y, dx))

print(f"Military gap violations (dx < 2): {len(gap_violations)}")
for g in gap_violations:
    print("  ", g)
