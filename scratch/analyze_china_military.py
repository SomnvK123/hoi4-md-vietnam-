import re

file_path = r'd:\SteamLibrary\steamapps\workshop\content\394360\2777392649\common\national_focus\05_china.txt'
with open(file_path, encoding='utf-8', errors='replace') as f:
    text = f.read()

lines = text.splitlines()[3154:14496]

focuses = []
cur = None

for line in lines:
    m = re.match(r'^\tfocus = \{', line)
    if m:
        if cur: focuses.append(cur)
        cur = {'raw': []}
    if cur:
        cur['raw'].append(line)
        mid = re.match(r'^\s*id = (\w+)', line)
        if mid: cur['id'] = mid.group(1)
        mx = re.match(r'^\s*x = (-?\d+)', line)
        if mx: cur['x'] = int(mx.group(1))
        my = re.match(r'^\s*y = (-?\d+)', line)
        if my: cur['y'] = int(my.group(1))
        mrel = re.match(r'^\s*relative_position_id = (\w+)', line)
        if mrel: cur['rel'] = mrel.group(1)

if cur: focuses.append(cur)

print(f"Total military focuses: {len(focuses)}")

# Group by sub-sections
sections = [
    ("Reform branch (Eat Imperial Grain)", 3183, 4239),
    ("Corruption branch (Poly Compromise)", 4239, 4744),
    ("Army branch (Streamline the Ranks)", 4744, 6461),
    ("Air branch (Integrated Air and Space)", 6461, 7892),
    ("Space branch (Manned Space Program)", 7892, 8349),
    ("Naval branch (PLAN)", 8349, 14497),
]

for name, start, end in sections:
    sub_lines = text.splitlines()[start-1:end-1]
    count = sum(1 for l in sub_lines if l.strip().startswith('focus = {') or l == '\tfocus = {')
    print(f"  - {name}: ~{count} focuses (lines {start}-{end})")

# Check root focuses
print("\nRoot focuses:")
for f in focuses:
    if 'rel' not in f:
        print(f"  - {f.get('id')}: abs (x={f.get('x')}, y={f.get('y')})")
