import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
loc_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\localisation\english\MD_focus_CHI_l_english.yml'
out_path = r'd:\HOI4Mods\md_vietnam\scratch\china_military_dump.txt'

locs = {}
with open(loc_path, encoding='utf-8', errors='replace') as f:
    for line in f:
        m = re.match(r'^\s*([A-Za-z0-9_]+):\d*\s*\"(.*)\"', line)
        if m:
            locs[m.group(1)] = m.group(2)

with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

sections = [
    ("1. Cai cach The che & Chong tham nhung (Reform & Anti-Corruption)", 3155, 4744),
    ("2. Luc quan (PLAGF - Streamline the Ranks)", 4744, 6461),
    ("3. Khong quan (PLAAF - Integrated Air and Space)", 6461, 7892),
    ("4. Khong gian & Vu tru (Space - China Manned Space Program)", 7892, 8349),
    ("5. Hai quan (PLAN - Blue Water Navy)", 8349, 14497),
]

with open(out_path, 'w', encoding='utf-8') as out:
    for title, s_start, s_end in sections:
        sub_lines = text.splitlines()[s_start-1:s_end-1]
        f_list = []
        cur = None
        for line in sub_lines:
            m = re.match(r'^\tfocus = \{', line)
            if m:
                if cur: f_list.append(cur)
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
        if cur: f_list.append(cur)

        out.write(f"\n====================================================================\n")
        out.write(f"{title}: {len(f_list)} focuses\n")
        out.write(f"====================================================================\n")
        for f in f_list:
            fid = f.get('id', 'unknown')
            name = locs.get(fid, fid)
            x, y = f.get('x', 0), f.get('y', 0)
            rel = f.get('rel', 'ROOT')
            mutex = f.get('mutex', [])
            prereqs = f.get('prereqs', [])
            extra = ""
            if mutex: extra += f" [MUTEX: {', '.join(mutex)}]"
            if prereqs: extra += f" [PRE: {prereqs}]"
            out.write(f"  [{fid}] {name} (x={x}, y={y}, rel={rel}){extra}\n")

print("Dumped successfully to scratch/china_military_dump.txt")
