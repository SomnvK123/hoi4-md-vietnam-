import os, glob, re

ROOT = r'd:/HOI4Mods/md_vietnam'
os.chdir(ROOT)

files = glob.glob('localisation/english/**/*.yml', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8-sig', errors='ignore') as fp:
        lines = [line.strip() for line in fp if line.strip() and not line.strip().startswith('#') and line.strip() != 'l_english:']
    # Check sample lines
    vn_count = 0
    en_count = 0
    for line in lines:
        m = re.match(r'^[A-Za-z0-9_.\-]+:\d*\s*\"(.*)\"$', line)
        if m:
            val = m.group(1)
            has_vn = any(ord(c) > 127 for c in val)
            if has_vn: vn_count += 1
            else: en_count += 1
    print(f"{f:55s}: {len(lines):4d} keys | VN: {vn_count:4d} | Non-VN: {en_count:4d}")
