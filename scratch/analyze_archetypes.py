import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

parts = re.split(r'\n\tfocus = \{', text)
print(f"Total focuses in China tree: {len(parts)-1}")

target_focuses = {}
for p in parts[1:]:
    fid = re.search(r'id\s*=\s*(\w+)', p)
    if not fid: continue
    fid = fid.group(1)
    
    frel = re.search(r'relative_position_id\s*=\s*(\w+)', p)
    frel = frel.group(1) if frel else None
    
    fprereqs = re.findall(r'focus\s*=\s*(\w+)', re.search(r'prerequisite\s*=\s*\{([^}]*)\}', p).group(1)) if re.search(r'prerequisite\s*=\s*\{([^}]*)\}', p) else []
    fmutex = re.findall(r'focus\s*=\s*(\w+)', re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', p).group(1)) if re.search(r'mutually_exclusive\s*=\s*\{([^}]*)\}', p) else []
    
    fx = re.search(r'\bx\s*=\s*(-?\d+)', p)
    fy = re.search(r'\by\s*=\s*(-?\d+)', p)
    
    target_focuses[fid] = {
        'id': fid,
        'rel': frel,
        'x': int(fx.group(1)) if fx else 0,
        'y': int(fy.group(1)) if fy else 0,
        'prereqs': fprereqs,
        'mutex': fmutex,
        'text': p[:800]
    }

# Find descendants of CHI_informatized_local_wars
def get_descendants(root_id):
    desc = {root_id}
    changed = True
    while changed:
        changed = False
        for fid, data in target_focuses.items():
            if fid not in desc:
                if any(p in desc for p in data['prereqs']):
                    desc.add(fid)
                    changed = True
    return desc

gw_desc = get_descendants('CHI_the_great_wall')
if_desc = get_descendants('CHI_the_iron_fist')
sb_desc = get_descendants('CHI_the_sharp_blade')

print(f"Great Wall branch focuses: {len(gw_desc)}")
print(f"Iron Fist branch focuses: {len(if_desc)}")
print(f"Sharp Blade branch focuses: {len(sb_desc)}")

print("\n--- GREAT WALL ---")
for fid in gw_desc:
    print(fid, target_focuses[fid]['prereqs'])

print("\n--- IRON FIST ---")
for fid in if_desc:
    print(fid, target_focuses[fid]['prereqs'])

print("\n--- SHARP BLADE ---")
for fid in sb_desc:
    print(fid, target_focuses[fid]['prereqs'])
