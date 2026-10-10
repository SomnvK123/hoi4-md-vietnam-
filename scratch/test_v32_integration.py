import re

# Read current focus tree
with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    orig_tree = f.read()

# Read new focuses
with open('scratch/v32_focuses.txt', 'r', encoding='utf-8') as f:
    new_focuses = f.read()

test_tree = orig_tree + "\n\n" + new_focuses

# Parse test tree
focuses = {}
raw_blocks = test_tree.split('focus = {')[1:]
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

print(f'Total test focuses: {len(focuses)}')

# Calculate absolute positions
abs_pos = {}
for fid, f in focuses.items():
    cur = fid
    abs_x, abs_y = 0, 0
    visited = set()
    while cur:
        if cur in visited:
            print(f'Cycle detected at {cur}!')
            break
        visited.add(cur)
        cf = focuses.get(cur)
        if not cf:
            break
        abs_x += cf['x']
        abs_y += cf['y']
        cur = cf['rel']
    abs_pos[fid] = (abs_x, abs_y)

# Check duplicate absolute (x, y)
pos_map = {}
duplicates = 0
for fid, pos in abs_pos.items():
    if pos in pos_map:
        print(f'DUPLICATE POSITION {pos}: {fid} and {pos_map[pos]}')
        duplicates += 1
    else:
        pos_map[pos] = fid

if duplicates == 0:
    print('ALL POSITIONS UNIQUE (0 duplicates)!')

# Check dangling prerequisites
dangling = 0
for fid, f in focuses.items():
    for p_group in f['prereqs']:
        for p in p_group:
            if p not in focuses:
                print(f'DANGLING PREREQ in {fid}: {p} not found!')
                dangling += 1
    if f['rel'] and f['rel'] not in focuses:
        print(f'DANGLING ANCHOR in {fid}: {f["rel"]} not found!')
        dangling += 1

if dangling == 0:
    print('ALL PREREQUISITES AND ANCHORS VALID (0 dangling)!')
