import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.analyze_military as am

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

def get_focus_body(fid):
    m = re.search(r'focus\s*=\s*\{\s*id\s*=\s*' + fid + r'\b', text)
    if not m:
        return ""
    start = m.start()
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start:i+1]
    return ""

print("=== LUC QUAN FOCUSES DETAILS ===")
for fid in am.categories['Luc quan (VIE_lf_)']:
    body = get_focus_body(fid)
    f = am.focuses[fid]
    date_m = re.search(r'date\s*([><=]+)\s*([0-9.]+)', body)
    date_str = date_m.group(0) if date_m else "no date"
    print(f"{fid:32} x={f['abs_x']:3} y={f['abs_y']:2} {date_str:18} rel={f['rel']} prereqs={f['prereqs']}")

print("\n=== HAI QUAN FOCUSES DETAILS ===")
for fid in am.categories['Hai quan (VIE_nf_)'] + am.categories['Hai quan bo sung / Dong tau']:
    body = get_focus_body(fid)
    f = am.focuses[fid]
    date_m = re.search(r'date\s*([><=]+)\s*([0-9.]+)', body)
    date_str = date_m.group(0) if date_m else "no date"
    print(f"{fid:32} x={f['abs_x']:3} y={f['abs_y']:2} {date_str:18} rel={f['rel']} prereqs={f['prereqs']}")

print("\n=== KHONG QUAN FOCUSES DETAILS ===")
for fid in am.categories['Khong quan (VIE_airf_)'] + am.categories['Phong khong - May bay (APM)']:
    body = get_focus_body(fid)
    f = am.focuses[fid]
    date_m = re.search(r'date\s*([><=]+)\s*([0-9.]+)', body)
    date_str = date_m.group(0) if date_m else "no date"
    print(f"{fid:32} x={f['abs_x']:3} y={f['abs_y']:2} {date_str:18} rel={f['rel']} prereqs={f['prereqs']}")
