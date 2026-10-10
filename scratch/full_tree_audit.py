import sys
from pathlib import Path
sys.path.insert(0, 'tools/audit')
from industry import ROOT, focus_map, groups, positions, value, values

FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
allf = focus_map(FOCUS_FILE.read_text(encoding='utf-8'))
pos = positions(allf)

# Define branches by X and prefix
def get_branch(fid, x, y):
    if fid.startswith('VIE_lf_'): return 'Land Forces'
    if fid.startswith('VIE_nf_') or fid.startswith('VIE_naval_') or fid in ('VIE_ba_son_shipyards', 'VIE_small_combatant_construction'): return 'Navy'
    if fid.startswith('VIE_airf_'): return 'Air Force'
    if fid.startswith('VIE_apm_'): return 'Air Defense (APM)'
    if fid.startswith('VIE_sf_'): return 'Special Forces'
    if fid.startswith('VIE_def_') or fid.startswith('VIE_military_enterprises_') or fid == 'VIE_path_self_reliant_deterrence': return 'Defense Industry'
    if fid == 'VIE_modernize_vpa': return 'Military Root'
    if x <= 26: return 'Politics & Party'
    if 28 <= x <= 64 and y <= 11: return 'Economy & Banking'
    if 28 <= x <= 64 and y > 11: return 'Foreign Diplomacy'
    if 66 <= x <= 98: return 'Infrastructure & Transport'
    if 100 <= x <= 124: return 'Energy, Mining & Oil'
    if 124 <= x <= 142: return 'Industry & Chips'
    if 144 <= x <= 170: return 'Science & Digital'
    return 'Other'

branch_map = {fid: get_branch(fid, p[0], p[1]) for fid, p in pos.items()}

# 1. Redundant connections across whole tree
def get_ancestors(fid, visited=None):
    if visited is None: visited = set()
    ancestors = set()
    for grp in groups(allf.get(fid, [])):
        for parent in grp:
            if parent in allf and parent not in visited:
                ancestors.add(parent)
                visited.add(parent)
                ancestors.update(get_ancestors(parent, visited))
    return ancestors

print("=== 1. REDUNDANT PREREQUISITES (NỐI THỪA) ===")
for fid, node in allf.items():
    grps = groups(node)
    for i, grp1 in enumerate(grps):
        if len(grp1) == 1:
            p1 = grp1[0]
            for j, grp2 in enumerate(grps):
                if i != j and len(grp2) == 1:
                    p2 = grp2[0]
                    if p1 in get_ancestors(p2):
                        print(f"[{branch_map[fid]}] {fid} (at {pos[fid]}): has redundant prereq {p1} (already ancestor of {p2})")

# 2. Lines that cut horizontally or vertically directly through other cards
print("\n=== 2. SEVERE LINE COLLISIONS (DÂY CẮT QUA CARD KHÁC) ===")
severe_cuts = []
for fid, node in allf.items():
    cx, cy = pos[fid]
    for grp in groups(node):
        for parent in grp:
            if parent in pos:
                px, py = pos[parent]
                # HOI4 path: (px, py) -> (px, mid_y) -> (cx, mid_y) -> (cx, cy)
                # Check 1: Card at same (cx) but py < oy < cy (vertical segment down to child)
                for oid, (ox, oy) in pos.items():
                    if oid not in (fid, parent):
                        # Card directly on child vertical column between py and cy
                        if ox == cx and py < oy < cy:
                            severe_cuts.append((parent, fid, oid, (px, py), (cx, cy), (ox, oy), "Child vertical leg passes through card"))
                        # Card directly on parent vertical column
                        elif ox == px and py < oy < cy:
                            severe_cuts.append((parent, fid, oid, (px, py), (cx, cy), (ox, oy), "Parent vertical leg passes through card"))
                        # Card directly on horizontal segment at mid_y (when oy == mid_y)
                        elif abs(oy - (py + cy) / 2) < 0.1 and min(px, cx) < ox < max(px, cx):
                            severe_cuts.append((parent, fid, oid, (px, py), (cx, cy), (ox, oy), "Horizontal line passes directly through card"))

for p, c, o, p1, p2, op, reason in severe_cuts:
    print(f"[{branch_map[c]}] Line {p} {p1} -> {c} {p2} : {reason} {o} {op}")

# 3. Inter-branch crowding (Bi dinh giua cac nhanh)
print("\n=== 3. BRANCH-BOUNDARY CROWDING (DÍNH GIỮA CÁC NHÁNH KHÁC NHAU) ===")
by_row = {}
for fid, (x, y) in pos.items():
    by_row.setdefault(y, []).append((x, fid))

for y, items in sorted(by_row.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i + 1]
        b1, b2 = branch_map[f1], branch_map[f2]
        if b1 != b2:
            # Different branches!
            diff = x2 - x1
            if diff < 2:
                print(f"CRITICAL COLLISION: Row {y}: {f1} [{b1}] at x={x1} and {f2} [{b2}] at x={x2} diff={diff}")
            elif diff == 2:
                # Adjacent with diff=2 between unrelated branches!
                print(f"Row {y:2}: [{b1}] {f1} (x={x1}) touches [{b2}] {f2} (x={x2}) (diff=2)")
