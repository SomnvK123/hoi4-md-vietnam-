import sys, os
sys.path.insert(0, os.path.abspath("."))
from tools.test_military_layout import military_layout

print(f"Total military focuses: {len(military_layout)}")

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    d = military_layout[fid]
    if d['rel'] == 'VIE_doi_moi_continues':
        return (80 + d['dx'], 0 + d['dy'])
    px, py = get_abs(d['rel'], visited)
    return (px + d['dx'], py + d['dy'])

abs_coords = {fid: get_abs(fid) for fid in military_layout}

print("\n=== FOCUSES WITH LARGE |dx| >= 6 OR dy > 1 ===")
for fid, cfg in military_layout.items():
    dx = cfg['dx']
    dy = cfg['dy']
    rel = cfg['rel']
    abs_pos = abs_coords[fid]
    if abs(dx) >= 6 or dy > 1:
        print(f"{fid:35} | abs={str(abs_pos):10} | rel={rel:32} | dx={dx:3d}, dy={dy:2d}")

# Spans by row
print("\n=== SUB-BRANCH SPANS BY ROW ===")
rows = {}
for fid, (x, y) in abs_coords.items():
    rows.setdefault(y, []).append((x, fid))

for y in sorted(rows.keys()):
    r = sorted(rows[y])
    xs = [x for x, f in r]
    print(f"y={y:2d} (count={len(r):2d}): x_min={min(xs):3d}, x_max={max(xs):3d}, span={max(xs)-min(xs):2d}")
    print("    " + ", ".join([f"{f}({x})" for x, f in r]))
