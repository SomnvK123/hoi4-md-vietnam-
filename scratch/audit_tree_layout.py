import sys
from pathlib import Path
sys.path.insert(0, 'tools/audit')
from industry import ROOT, focus_map, groups, positions, value, values

FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
allf = focus_map(FOCUS_FILE.read_text(encoding='utf-8'))
pos = positions(allf)

print(f"Total focuses: {len(allf)}")

# 1. Check transitive redundant prerequisites (noi thua)
def get_ancestors(fid, visited=None):
    if visited is None:
        visited = set()
    ancestors = set()
    for grp in groups(allf.get(fid, [])):
        for parent in grp:
            if parent in allf and parent not in visited:
                ancestors.add(parent)
                visited.add(parent)
                ancestors.update(get_ancestors(parent, visited))
    return ancestors

redundant_prereqs = []
for fid, node in allf.items():
    grps = groups(node)
    for i, grp1 in enumerate(grps):
        if len(grp1) == 1:
            p1 = grp1[0]
            for j, grp2 in enumerate(grps):
                if i != j and len(grp2) == 1:
                    p2 = grp2[0]
                    if p1 in get_ancestors(p2):
                        redundant_prereqs.append((fid, p1, p2))

print(f"\n=== 1. Transitive Redundant Prerequisites: {len(redundant_prereqs)} ===")
for fid, ancestor, intermediate in redundant_prereqs:
    print(f"  {fid:35} -> redundant {ancestor:30} (inherited via {intermediate})")

# 2. Check line crossing through other nodes (day cat ngang de len card khac)
# In HOI4: line from (x1, y1) to (x2, y2):
# Mid Y = (y1 + y2) / 2.
# Path is: (x1, y1) -> (x1, mid_y) -> (x2, mid_y) -> (x2, y2).
# If another focus sits at (x_other, y_other):
# Does (x_other, y_other) intersect or sit right on the line?
# Especially: if y_other is between y1 and y2, or if mid_y == y_other, or x1 <= x_other <= x2 at y_other.
line_intersections = []
for fid, node in allf.items():
    x2, y2 = pos[fid]
    for grp in groups(node):
        for parent in grp:
            if parent in pos:
                x1, y1 = pos[parent]
                if y2 > y1 and abs(x2 - x1) > 2:
                    # Horizontal segment is between min(x1,x2) and max(x1,x2)
                    min_x, max_x = min(x1, x2), max(x1, x2)
                    # Check any node that sits in between
                    for other_id, (ox, oy) in pos.items():
                        if other_id not in (fid, parent):
                            # If other is strictly between x1 and x2
                            if min_x < ox < max_x:
                                # If other is at y1 or y2 or in between
                                if y1 <= oy <= y2:
                                    line_intersections.append((parent, fid, other_id, (x1, y1), (x2, y2), (ox, oy)))

print(f"\n=== 2. Lines Cutting Through or Over Intermediate Nodes: {len(line_intersections)} ===")
for p, c, o, p1, p2, op in line_intersections[:50]:
    print(f"  Line {p} {p1} -> {c} {p2} cuts across {o} {op}")
if len(line_intersections) > 50:
    print(f"  ... and {len(line_intersections) - 50} more")

# 3. Check for multi-branch column collisions / proximity (bi dinh)
# Group focuses into branches by prefix or functional clusters
by_row = {}
for fid, (x, y) in pos.items():
    by_row.setdefault(y, []).append((x, fid))

crowded = []
for y, items in sorted(by_row.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i + 1]
        diff = x2 - x1
        if diff < 2:
            crowded.append((y, f1, f2, diff, "DIFF < 2 (COLLISION)"))
        elif diff == 2:
            # Check if they belong to different branches
            b1 = f1.split('_')[1] if len(f1.split('_')) > 1 else f1
            b2 = f2.split('_')[1] if len(f2.split('_')) > 1 else f2
            if b1 != b2:
                # check if there's parent/child relationship between them
                p1 = [p for g in groups(allf[f1]) for p in g]
                p2 = [p for g in groups(allf[f2]) for p in g]
                if f1 not in p2 and f2 not in p1:
                    crowded.append((y, f1, f2, diff, f"DIFF 2 between {b1} and {b2}"))

print(f"\n=== 3. Crowded / Inter-branch adjacent focuses on same row: {len(crowded)} ===")
for y, f1, f2, diff, note in crowded[:40]:
    print(f"  Row {y:2}: {f1} (x={pos[f1][0]}) and {f2} (x={pos[f2][0]}) -> {note}")
