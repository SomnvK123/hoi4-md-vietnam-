import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
cur_focus = None
depth = 0
focuses = {}

for line in lines:
    stripped = line.strip()
    if stripped.startswith('#'): continue
    if 'focus = {' in line:
        cur_focus = {}
        depth = 1
        continue
    if cur_focus is not None:
        depth += line.count('{') - line.count('}')
        for k in ['id', 'relative_position_id', 'x', 'y', 'cost']:
            m = re.search(r'\b' + k + r'\s*=\s*([a-zA-Z0-9_-]+)', line)
            if m and k not in cur_focus: cur_focus[k] = m.group(1)
        if depth <= 0:
            if 'id' in cur_focus: focuses[cur_focus['id']] = cur_focus
            cur_focus = None

def get_abs(fid):
    f = focuses.get(fid)
    if not f: return (0, 0)
    rel = f.get('relative_position_id')
    x = int(f.get('x', 0))
    y = int(f.get('y', 0))
    if rel and rel in focuses:
        rx, ry = get_abs(rel)
        return (rx + x, ry + y)
    return (x, y)

results = []
for fid, f in focuses.items():
    ax, ay = get_abs(fid)
    if 90 <= ax <= 106 and 1 <= ay <= 8:
        results.append((ay, ax, fid, f.get('relative_position_id'), int(f.get('x',0)), int(f.get('y',0))))

results.sort()
print(f"{'ay':2} {'ax':3} | {'id':32} | {'rel':26} | {'x':2} {'y':2}")
print("-" * 80)
for ay, ax, fid, rel, rx, ry in results:
    print(f"{ay:2} {ax:3} | {fid:32} | {str(rel):26} | {rx:2} {ry:2}")
