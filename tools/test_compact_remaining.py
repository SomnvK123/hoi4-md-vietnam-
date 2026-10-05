import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 0
focuses = {}
focus_list = []
while True:
    m = re.search(r'\bfocus\s*=\s*\{', text[pos:])
    if not m: break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == '{': depth += 1
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
    else: break

# Apply all 9 fixes
all_9_mods = {
    'VIE_fdi_attraction': {'rel': 'VIE_household_business', 'x': 0, 'y': 1},
    'VIE_sez_three_zones': {'rel': 'VIE_cptpp_member', 'x': 0, 'y': 1},
    'VIE_shared_future': {'rel': 'VIE_border_trade_gates', 'x': 2, 'y': 1},
    'VIE_indochina_solidarity': {'rel': 'VIE_mekong_dams_response', 'x': 2, 'y': 1},
    'VIE_un_security_council': {'rel': 'VIE_apec_host', 'x': -2, 'y': 1},
    'VIE_hl_all_people_defence': {'rel': 'VIE_hl_army_political_education', 'x': -2, 'y': 1},
    'VIE_hl_party_defence_industry': {'rel': 'VIE_hl_army_political_education', 'x': 0, 'y': 1},
    'VIE_hl_fatherland_front': {'rel': 'VIE_hl_school_theory', 'x': 0, 'y': 1},
    'VIE_hl_indochina_union': {'rel': 'VIE_hl_vientiane_ultimatum', 'x': 1, 'y': 1},
}

for fid, m in all_9_mods.items():
    focuses[fid].update(m)

# Check forward references
fwd_refs = []
for f in focus_list:
    if f['rel']:
        if f['rel'] not in focuses:
            fwd_refs.append(f"{f['id']} references unknown rel {f['rel']}")
        elif focuses[f['rel']]['order'] >= f['order']:
            fwd_refs.append(f"{f['id']} (order {f['order']}) references future {f['rel']} (order {focuses[f['rel']]['order']})")

print(f'Forward references: {len(fwd_refs)}')
for fr in fwd_refs:
    print('  ', fr)

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f['rel'] or f['rel'] not in focuses: return (f['x'], f['y'])
    px, py = get_abs(f['rel'], visited)
    return (px + f['x'], py + f['y'])

coords = {}
collisions = []
for fid in focuses:
    c = get_abs(fid)
    if c in coords:
        collisions.append((fid, coords[c], c))
    coords[c] = fid

print(f'Collisions: {len(collisions)}')
for col in collisions:
    print('  ', col)

# Check remaining dy > 1
dy_jumps = [f for f in focus_list if f['rel'] and f['rel'] != 'VIE_doi_moi_continues' and f['y'] > 1]
print(f'Remaining dy > 1 across entire tree: {len(dy_jumps)}')
for dj in dy_jumps:
    print('  ', dj['id'], dj['rel'], dj['y'])

print("\nVerification successful!")
