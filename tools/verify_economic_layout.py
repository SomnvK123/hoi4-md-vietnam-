import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse all focuses
focuses = []
pos = 0
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
                focus_body = text[start:i+1]
                id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', focus_body)
                x_m = re.search(r'\bx\s*=\s*(-?\d+)', focus_body)
                y_m = re.search(r'\by\s*=\s*(-?\d+)', focus_body)
                rel_m = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', focus_body)
                prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', focus_body)
                if id_m:
                    focuses.append({
                        'id': id_m.group(1),
                        'x': int(x_m.group(1)) if x_m else 0,
                        'y': int(y_m.group(1)) if y_m else 0,
                        'rel': rel_m.group(1) if rel_m else None,
                        'prereqs': prereqs,
                        'order': len(focuses),
                        'body': focus_body
                    })
                pos = i + 1
                break
        i += 1
    else:
        break

print(f"Total focuses in tree: {len(focuses)}")

focus_dict = {f['id']: f for f in focuses}

# Check forward references
fwd_refs = []
for f in focuses:
    if f['rel']:
        if f['rel'] not in focus_dict:
            fwd_refs.append(f"{f['id']} references unknown rel {f['rel']}")
        elif focus_dict[f['rel']]['order'] > f['order']:
            fwd_refs.append(f"{f['id']} (order {f['order']}) references future rel {f['rel']} (order {focus_dict[f['rel']]['order']})")

print(f"Forward references across ENTIRE file: {len(fwd_refs)}")
for fr in fwd_refs:
    print("  ", fr)

# Absolute coordinates calculation
abs_coords = {}
def get_abs(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    f = focus_dict[fid]
    if not f['rel']:
        return (f['x'], f['y'])
    parent_x, parent_y = get_abs(f['rel'], visited)
    return (parent_x + f['x'], parent_y + f['y'])

for f in focuses:
    abs_coords[f['id']] = get_abs(f['id'])

coord_map = {}
collisions = []
for fid, (ax, ay) in abs_coords.items():
    if (ax, ay) in coord_map:
        collisions.append((fid, coord_map[(ax, ay)], (ax, ay)))
    else:
        coord_map[(ax, ay)] = fid

print(f"Total coordinate collisions across ENTIRE file: {len(collisions)}")
for c in collisions:
    print("  Collision:", c)

# Analyze the 4 Economic Pillars
headers = [
    "## KINH TE - TRUC 1",
    "## KINH TE - TRUC 2",
    "## KINH TE - TRUC 3",
    "## KINH TE - TRUC 4"
]

sections = []
for i in range(len(headers)):
    start_pos = text.find(headers[i])
    if i < len(headers) - 1:
        end_pos = text.find(headers[i+1])
    else:
        # after truc 4
        m_next = re.search(r'###+\s*\n\s*###+.*DIGITAL|SCIENCE|INFRASTRUCTURE|focus\s*=\s*\{\s*id\s*=\s*VIE_(?!high_tech|ai_|robotics|biotech|stem_|global_tech|fourth_ir|automotive|shipbuilding|heavy_machinery|supporting|textile|electronics|chemical|materials|industrial_auto|precision|intel_hcmc|samsung|manufacturing|china_plus|ev_rev|high_tech_fdi|smart_mfg|green_ind|venture_cap|patent|indigenous_tech|defense_dual|semiconductor_fab|national_rnd|innovation_dist|tech_unicorns|hightech_export)', text[start_pos:])
        end_pos = text.find("focus = {", start_pos + 15000)
    sections.append((start_pos, end_pos))

for p_num, (sp, ep) in enumerate(sections, 1):
    sub = text[sp:ep] if ep != -1 else text[sp:]
    fids = re.findall(r'\bid\s*=\s*([a-zA-Z0-9_]+)', sub)
    # filter only focus ids (each has focus = { ... id = ... })
    actual_fids = []
    for f in focuses:
        if f['id'] in fids and text.find(f"id = {f['id']}", sp) < (ep if ep != -1 else len(text)) and text.find(f"id = {f['id']}", sp) >= sp:
            actual_fids.append(f['id'])
    
    print(f"\n--- Pillar {p_num}: {len(actual_fids)} focuses ---")
    rows = {}
    for fid in actual_fids:
        ax, ay = abs_coords[fid]
        rows.setdefault(ay, []).append((ax, fid))
    
    for r_y in sorted(rows.keys()):
        row_items = sorted(rows[r_y], key=lambda x: x[0])
        names = [f"{fid}(x={ax})" for ax, fid in row_items]
        print(f"  y={r_y} ({len(row_items)} focuses): {', '.join(names)}")
        # Check delta x between adjacent items
        for k in range(len(row_items) - 1):
            dx = row_items[k+1][0] - row_items[k][0]
            if dx < 2:
                print(f"    WARNING: dx={dx} < 2 between {row_items[k][1]} and {row_items[k+1][1]} at y={r_y}!")
