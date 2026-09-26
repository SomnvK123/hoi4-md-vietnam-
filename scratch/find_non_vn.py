import re

for f in ['localisation/english/replace/VIE_md_vi_military_l_english.yml', 'localisation/english/replace/VIE_md_vi_mil_DE_l_english.yml']:
    with open(f, 'r', encoding='utf-8-sig') as fp:
        for idx, line in enumerate(fp, 1):
            m = re.match(r'^\s*([A-Za-z0-9_.\-]+):\d*\s*"(.*)"\s*$', line.strip())
            if m:
                val = m.group(2)
                has_vn = any(ord(c) > 127 for c in val)
                if not has_vn:
                    print(f"{f}:{idx} {m.group(1)}: \"{val}\"")
