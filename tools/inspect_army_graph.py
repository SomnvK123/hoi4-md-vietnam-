import re
from pathlib import Path
from collections import defaultdict
import sys
sys.path.insert(0, ".")

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
focuses = {}
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == '{': brace += 1
        elif txt[i] == '}':
            brace -= 1
            if brace == 0: end = i + 1; break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    mut = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    avail = re.search(r"\bavailable\s*=\s*\{([^}]*)\}", block)
    focuses[fid] = {
        'id': fid, 'x': int(xm.group(1)) if xm else 0, 'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None, 'prereqs': prereqs, 'mut': mut,
        'avail': avail.group(1).strip() if avail else ''
    }

army = [f for f in focuses if 'lf_' in f or f == 'VIE_lf_army_reform']
print(f"Total Army focuses: {len(army)}")

for f in sorted(army, key=lambda x: focuses[x]['y']):
    sid = f.replace("VIE_", "")
    p_str = ", ".join([p.replace("VIE_", "") for p in focuses[f]['prereqs']])
    print(f"{sid:30s} | y={focuses[f]['y']:2d} | prereqs=[{p_str}] | avail={focuses[f]['avail']}")
