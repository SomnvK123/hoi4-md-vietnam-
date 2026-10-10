import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
loc_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\localisation\english\MD_focus_CHI_l_english.yml'

locs = {}
with open(loc_path, encoding='utf-8', errors='replace') as f:
    for line in f:
        m = re.match(r'^\s*([A-Za-z0-9_]+):\d*\s*\"(.*)\"', line)
        if m: locs[m.group(1)] = m.group(2)

with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

army_lines = text.splitlines()[4743:6460]
focuses = []
cur = None

for line in army_lines:
    if line.startswith('\tfocus = {'):
        if cur: focuses.append(cur)
        cur = {'raw': []}
    if cur:
        cur['raw'].append(line)
        m = re.match(r'^\s*id = (\w+)', line)
        if m: cur['id'] = m.group(1)

if cur: focuses.append(cur)

print(f"Total China Army focuses: {len(focuses)}\n")

for f in focuses:
    fid = f['id']
    name = locs.get(fid, fid)
    desc = locs.get(f"{fid}_desc", "")
    full_text = '\n'.join(f['raw'])
    
    ideas = re.findall(r'add_ideas = (\w+)', full_text)
    techs = re.findall(r'category = (\w+)', full_text)
    eq = re.findall(r'type = (\w+)', full_text)
    mutex = re.findall(r'mutually_exclusive = \{ focus = (\w+)(?: focus = (\w+))?', full_text)
    
    effects = []
    if ideas: effects.append(f"Ideas: {ideas}")
    if techs: effects.append(f"Tech: {techs}")
    if eq: effects.append(f"Equipment: {eq}")
    
    print(f"[{fid}] {name}")
    if mutex: print(f"    -> MUTEX: {mutex}")
    if effects: print(f"    -> {' | '.join(effects)}")
