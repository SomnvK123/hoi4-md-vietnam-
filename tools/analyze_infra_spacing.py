import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
import tools.test_infra_layout as til

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
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
    avail = re.sub(r'\s+', ' ', avail)
    foci[fid] = {'prs': all_prs, 'avail': avail}

print("=== INFRASTRUCTURE FOCUSES AND DEPENDENCIES ===")
for fid, d in sorted(til.INFRA_LAYOUT.items(), key=lambda x: (x[1]['abs'][1], x[1]['abs'][0])):
    ax, ay = d['abs']
    pr = foci.get(fid, {}).get('prs', [])
    av = foci.get(fid, {}).get('avail', '')
    print(f"y={ay:2d}, x={ax:3d} | {fid:38} | rel={d['rel']:30} | dx={d['dx']:3d}, dy={d['dy']:2d} | pr={str(pr):35} | av={av[:30]}")
