import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import sys, os
sys.path.insert(0, os.path.abspath("."))
from tools.test_military_layout import military_layout

pattern = re.compile(r'(\tfocus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)\b.*?\n\t\})', re.DOTALL)
foci = {}
for m in pattern.finditer(text):
    fid = m.group(2)
    body = m.group(1)
    all_prs = []
    for pr_blk in re.findall(r'prerequisite\s*=\s*\{([^}]+)\}', body):
        all_prs.extend(re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pr_blk))
    avail_m = re.search(r'available\s*=\s*\{([^}]*)\}', body)
    avail = avail_m.group(1).strip() if avail_m else ""
    foci[fid] = {'prs': all_prs, 'avail': avail}

army_fids = [f for f in military_layout if f.startswith('VIE_lf_') or f.startswith('VIE_military_enterprises_') or f in ['VIE_def_industry_law', 'VIE_path_self_reliant_deterrence']]

print("=== ARMY PREREQUISITES & AVAILABLE ===")
for f in army_fids:
    pr = foci[f]['prs']
    av = foci[f]['avail'].replace('\n', ' ')
    av = re.sub(r'\s+', ' ', av)
    print(f"{f:35} | pr={str(pr):35} | av={av}")
