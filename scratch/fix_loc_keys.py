import re

loc_file = 'localisation/english/replace/VIE_md_vi_military_l_english.yml'
with open(loc_file, 'r', encoding='utf-8') as f:
    text = f.read()

new_lines = []
for l in text.splitlines():
    m = re.match(r'^\s*([A-Za-z_0-9]+)\s*(?::\d*|:)\s*"(.*)"\s*$', l)
    if m:
        new_lines.append(f'  {m.group(1)}:0 "{m.group(2)}"')
    else:
        new_lines.append(l)

with open(loc_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines) + '\n')

print("Standardized all loc keys to KEY:0 \"...\" successfully.")
