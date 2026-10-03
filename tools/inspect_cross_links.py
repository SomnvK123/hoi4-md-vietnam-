import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from tools.refine_categories import categories, focus_matches, fmap, refine_categorize
from collections import defaultdict

cross_links = []
for f in focus_matches:
    c = refine_categorize(f)
    for p in f["prereqs"]:
        if p in fmap:
            pc = refine_categorize(fmap[p])
            if pc != c:
                cross_links.append((pc, p, c, f["id"]))

print(f"Total cross-branch prerequisite links: {len(cross_links)}")
links_by_pair = defaultdict(list)
for pc, p, c, fid in cross_links:
    links_by_pair[(pc, c)].append((p, fid))

for (pc, c), plist in sorted(links_by_pair.items()):
    print(f"\n{pc} -> {c} ({len(plist)} links):")
    for p, fid in plist:
        print(f"  {p:35s} -> {fid}")
