import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
from tools.test_military_layout import military_layout

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

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

navy_fids = [f for f in military_layout if f.startswith('VIE_nf_') or f.startswith('VIE_naval_') or f == 'VIE_ba_son_shipyards']

print("=== NAVY PREREQUISITES & POSITIONS ===")
for f in navy_fids:
    cfg = military_layout[f]
    pr = foci[f]['prs']
    print(f"{f:35} | abs={cfg['abs']} | rel={cfg['rel']:30} | dx={cfg['dx']:2d}, dy={cfg['dy']:2d} | pr={pr}")
