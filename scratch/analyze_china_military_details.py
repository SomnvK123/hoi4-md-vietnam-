import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

# Also let's find loc for China focuses
loc_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\localisation\english\MD_China_l_english.yml'
locs = {}
try:
    with open(loc_path, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = re.match(r'^\s*([A-Za-z0-9_]+):\d*\s*\"(.*)\"', line)
            if m:
                locs[m.group(1)] = m.group(2)
except Exception as e:
    print('Loc load error:', e)

lines = text.splitlines()[3154:14496]

def parse_focus_block(raw_lines):
    focuses = []
    cur = None
    for line in raw_lines:
        m = re.match(r'^\tfocus = \{', line)
        if m:
            if cur: focuses.append(cur)
            cur = {'lines': [], 'prereqs': [], 'mutex': []}
        if cur:
            cur['lines'].append(line)
            mid = re.match(r'^\s*id = (\w+)', line)
            if mid: cur['id'] = mid.group(1)
            mx = re.match(r'^\s*x = (-?\d+)', line)
            if mx: cur['x'] = int(mx.group(1))
            my = re.match(r'^\s*y = (-?\d+)', line)
            if my: cur['y'] = int(my.group(1))
            mrel = re.match(r'^\s*relative_position_id = (\w+)', line)
            if mrel: cur['rel'] = mrel.group(1)
            if 'prerequisite = {' in line:
                fids = re.findall(r'focus = (\w+)', line)
                if fids: cur['prereqs'].append(fids)
            if 'mutually_exclusive = {' in line:
                fids = re.findall(r'focus = (\w+)', line)
                if fids: cur['mutex'].extend(fids)
    if cur: focuses.append(cur)
    return focuses

all_military = parse_focus_block(lines)

print(f"Total parsed: {len(all_military)}")

sections = [
    ("1. Core & Military Reform (Eat Imperial Grain)", 3155, 4239),
    ("2. Corruption & Commercial Branch (The Poly Compromise)", 4239, 4744),
    ("3. Army Branch (Streamline the Ranks)", 4744, 6461),
    ("4. Air Branch (Integrated Air and Space)", 6461, 7892),
    ("5. Space Branch (China Manned Space Program)", 7892, 8349),
    ("6. Naval Branch (PLAN)", 8349, 14497),
]

for title, s_start, s_end in sections:
    sub_lines = text.splitlines()[s_start-1:s_end-1]
    f_list = parse_focus_block(sub_lines)
    print(f"\n========================================================")
    print(f"{title}: {len(f_list)} focuses")
    print(f"========================================================")
    for f in f_list[:8]:
        fid = f.get('id', 'unknown')
        name = locs.get(fid, fid)
        rel = f.get('rel', 'ROOT')
        x, y = f.get('x', 0), f.get('y', 0)
        prereqs = f.get('prereqs', [])
        mutex = f.get('mutex', [])
        print(f"  * {name} ({fid}) | pos: ({x}, {y}) rel={rel}")
        if prereqs:
            print(f"      Prereqs: {prereqs}")
        if mutex:
            print(f"      Mutex: {mutex}")
    if len(f_list) > 8:
        print(f"  ... và {len(f_list) - 8} focuses khác ...")
