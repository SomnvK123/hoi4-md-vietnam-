import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))

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

abs_coords = {}
def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f['rel']: return (f['x'], f['y'])
    if f['rel'] not in focuses: return (f['x'], f['y'])
    px, py = get_abs(f['rel'], visited)
    return (px + f['x'], py + f['y'])

for fid in focuses:
    abs_coords[fid] = get_abs(fid)

print("=== ALL FOCUSES WITH |dx| >= 6 OR dy > 1 ===")
jumps = []
for fid, f in focuses.items():
    dx, dy = f['x'], f['y']
    rel = f['rel']
    ax, ay = abs_coords[fid]
    is_root_bridge = (rel == 'VIE_doi_moi_continues')
    if (abs(dx) >= 6 or dy > 1) and not is_root_bridge:
        jumps.append((fid, rel, dx, dy, ax, ay))

print(f"Total non-root jumps (|dx| >= 6 or dy > 1): {len(jumps)}")
for fid, rel, dx, dy, ax, ay in sorted(jumps, key=lambda x: (x[5], x[4])):
    print(f"y={ay:2d}, x={ax:3d} | {fid:38} -> {str(rel):32} | dx={dx:3d}, dy={dy:2d}")
