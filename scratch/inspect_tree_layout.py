import sys
import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse focus blocks
focuses = {}
raw_blocks = text.split('focus = {')[1:]
for block in raw_blocks:
    body = block.split('}\n\tfocus = {')[0]
    id_m = re.search(r'id\s*=\s*(\S+)', body)
    if not id_m: continue
    fid = id_m.group(1)
    x_m = re.search(r'x\s*=\s*(-?\d+)', body)
    y_m = re.search(r'y\s*=\s*(-?\d+)', body)
    rel_m = re.search(r'relative_position_id\s*=\s*(\S+)', body)
    prereqs = re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', body)
    parsed_prereqs = []
    for p in prereqs:
        f_in_p = re.findall(r'focus\s*=\s*(\S+)', p)
        if f_in_p:
            parsed_prereqs.append(f_in_p)
    focuses[fid] = {
        'x': int(x_m.group(1)) if x_m else 0,
        'y': int(y_m.group(1)) if y_m else 0,
        'rel': rel_m.group(1) if rel_m else None,
        'prereqs': parsed_prereqs
    }

# Compute absolute coordinates
abs_pos = {}
for fid, f in focuses.items():
    cur = fid
    abs_x = 0
    abs_y = 0
    visited = set()
    while cur:
        if cur in visited:
            print('Cycle detected at', cur)
            break
        visited.add(cur)
        c_focus = focuses.get(cur)
        if not c_focus:
            break
        abs_x += c_focus['x']
        abs_y += c_focus['y']
        cur = c_focus['rel']
    abs_pos[fid] = (abs_x, abs_y)

# Look at military branch focuses
mil = [(fid, abs_pos[fid], focuses[fid]['rel'], focuses[fid]['x'], focuses[fid]['y']) for fid in focuses if abs_pos[fid][0] >= 160]
mil.sort(key=lambda x: (x[1][1], x[1][0]))

print(f'Military focuses (abs X >= 160): {len(mil)}')
for fid, ab, rel, x, y in mil:
    print(f'{fid:45} abs={ab} rel={rel} off=({x},{y})')
