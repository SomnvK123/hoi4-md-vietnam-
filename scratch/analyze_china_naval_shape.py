import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

lines = text.splitlines()[8348:14496]
focuses = []
cur = None
for l in lines:
    if l.strip().startswith('focus = {') or l == '\tfocus = {':
        if cur: focuses.append(cur)
        cur = {'raw': []}
    if cur:
        cur['raw'].append(l)
        mid = re.match(r'^\s*id = (\w+)', l)
        if mid: cur['id'] = mid.group(1)
        mx = re.match(r'^\s*x = (-?\d+)', l)
        if mx: cur['x'] = int(mx.group(1))
        my = re.match(r'^\s*y = (-?\d+)', l)
        if my: cur['y'] = int(my.group(1))
        mrel = re.match(r'^\s*relative_position_id = (\w+)', l)
        if mrel: cur['rel'] = mrel.group(1)

if cur: focuses.append(cur)
id_map = {f['id']: f for f in focuses if 'id' in f}

def get_abs(f):
    if 'rel' not in f:
        return f.get('x', 0), f.get('y', 0)
    if f['rel'] not in id_map:
        return f.get('x', 0), f.get('y', 0)
    rx, ry = get_abs(id_map[f['rel']])
    return rx + f.get('x', 0), ry + f.get('y', 0)

plan_cluster = []
for f in focuses:
    fid = f.get('id', '')
    if any(k in fid.lower() for k in [
        'liu_huaqing', 'sovremenny', 'project_998', 'yuan_and_the_shang', 
        'jiangnan', 'flying_leopard', 'yuzhao', '054a', 'lanzhou', 
        'varyag', 'huludao', 'sea_eagles', 'type_901', 'three_distances', 
        'renhai', 'shandong', 'fujian', 'type_075', 'quiet_dragons', 
        'bohai', 'undersea_supremacy', 'surface_capital', 'two_ocean'
    ]):
        f['ax'], f['ay'] = get_abs(f)
        plan_cluster.append(f)

print(f"PLAN focuses count: {len(plan_cluster)}")
by_y = {}
for f in plan_cluster:
    by_y.setdefault(f['ay'], []).append(f)

for y in sorted(by_y.keys()):
    fs = sorted(by_y[y], key=lambda x: x['ax'])
    print(f"\n--- Layer Y={y} ({len(fs)} focuses) ---")
    for f in fs:
        raw_text = "\n".join(f['raw'])
        prereqs = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*(\w+)', raw_text)
        mutex = re.findall(r'mutually_exclusive\s*=\s*\{\s*focus\s*=\s*(\w+)', raw_text)
        cost_m = re.search(r'cost\s*=\s*(\d+)', raw_text)
        cost = cost_m.group(1) if cost_m else '?'
        print(f"  X={f['ax']}: {f['id']} (cost={cost}) | prereqs={prereqs} | mutex={mutex}")
