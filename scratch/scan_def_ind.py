import os, re
from pathlib import Path

targets = [
    'VIE_def_industry_law',
    'VIE_military_enterprises_core',
    'VIE_military_enterprises_divest',
    'VIE_path_self_reliant_deterrence',
    'VIE_def_ind_',
    'VIE_def_industry_',
    'VIE_self_reliant_deterrence'
]

root = Path('.')
matches = {}

for p in root.rglob('*'):
    if p.is_file() and not any(part.startswith('.') for part in p.parts) and 'scratch' not in p.parts:
        try:
            content = p.read_text(encoding='utf-8', errors='replace')
            for t in targets:
                found = re.findall(rf'\b{t}\w*', content)
                if found:
                    matches.setdefault(str(p), set()).update(found)
        except Exception:
            pass

with open('scratch/defense_industry_refs.txt', 'w', encoding='utf-8') as out:
    for f, items in sorted(matches.items()):
        out.write(f"{f}: {sorted(list(items))}\n")

print("Done scanning defense industry references.")
