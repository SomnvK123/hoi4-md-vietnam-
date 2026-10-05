import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import sys, os
sys.path.append(os.path.dirname(__file__))
from analyze_infra import foci, get_abs, infra_visited

print(f"Total infra focuses: {len(infra_visited)}")

# Let's inspect each focus's current definition
rows = {}
for fid in infra_visited:
    ax, ay = get_abs(fid)
    rows.setdefault(ay, []).append((ax, fid))

for y in sorted(rows.keys()):
    print(f"\n--- ROW y = {y} ({len(rows[y])} focuses) ---")
    for x, fid in sorted(rows[y]):
        d = foci[fid]
        print(f"  fid={fid:38} | abs=({x:2d},{y:2d}) | rel={str(d['rel']):32} (dx={d['dx']:3d}, dy={d['dy']:2d}) | prs={d['prs']}")
