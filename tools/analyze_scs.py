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
                avail = re.findall(r'has_completed_focus\s*=\s*([a-zA-Z0-9_]+)', block)
                me = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', block)
                date_m = re.search(r'date\s*([><=]+)\s*([0-9.]+)', block)
                if id_m:
                    fid = id_m.group(1)
                    f_data = {
                        'id': fid,
                        'x': int(x_m.group(1)) if x_m else 0,
                        'y': int(y_m.group(1)) if y_m else 0,
                        'rel': rel_m.group(1) if rel_m else None,
                        'prereqs': prereqs,
                        'avail': avail,
                        'me': me[0].strip() if me else "",
                        'date': date_m.group(0) if date_m else "",
                        'order': len(focus_list),
                        'start_line': text[:start].count('\n') + 1,
                        'block': block
                    }
                    focuses[fid] = f_data
                    focus_list.append(f_data)
                pos = i + 1
                break
        i += 1
    else:
        break

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

for f in focus_list:
    f['abs_x'], f['abs_y'] = get_abs(f['id'])

# Trace subtree from VIE_law_of_the_sea
subtree = []
queue = ["VIE_law_of_the_sea"]
visited = set(["VIE_law_of_the_sea"])
while queue:
    curr = queue.pop(0)
    subtree.append(curr)
    for f in focus_list:
        if f['rel'] == curr or curr in f['prereqs']:
            if f['id'] not in visited:
                visited.add(f['id'])
                queue.append(f['id'])

print(f"Total focuses in VIE_law_of_the_sea subtree: {len(subtree)}")

print("\n=== SOUTH CHINA SEA / LAW OF THE SEA FOCUSES ===")
for fid in subtree:
    f = focuses[fid]
    ax = f['abs_x']
    ay = f['abs_y']
    rel = f['rel']
    pr = f['prereqs']
    av = f['avail']
    me = f['me']
    dt = f['date']
    ln = f['start_line']
    print(f"Line {ln:5} | {fid:32} | abs=({ax:3},{ay:2}) | rel={str(rel):25} | pr={str(pr):30} | {dt}")

# Check external references
ext_refs = []
for fid, f in focuses.items():
    if fid not in visited:
        for p in f['prereqs']:
            if p in visited:
                ext_refs.append((fid, "prereq", p))
        for a in f['avail']:
            if a in visited:
                ext_refs.append((fid, "avail", a))
        if f['rel'] in visited:
            ext_refs.append((fid, "rel", f['rel']))

print(f"\nExternal focuses referencing SCS subtree: {len(ext_refs)}")
for r in ext_refs:
    print("  ", r)
