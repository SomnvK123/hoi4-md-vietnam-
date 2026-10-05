import re, sys, os
sys.path.insert(0, os.path.abspath("."))

content = open('common/national_focus/VIE_md_focus.txt', encoding='utf-8').read()

focus_matches = []
for m in re.finditer(r'\n\tfocus\s*=\s*\{', content):
    st = m.end()
    d = 1
    i = st
    while d > 0 and i < len(content):
        if content[i] == '{': d += 1
        elif content[i] == '}': d -= 1
        i += 1
    body = content[st:i-1]
    fid_m = re.search(r'\bid\s*=\s*(\w+)', body)
    if fid_m:
        fid = fid_m.group(1)
        line_start = m.start()
        end_pos = i
        while end_pos < len(content) and content[end_pos] in ' \t\r\n':
            end_pos += 1
        focus_matches.append({
            'id': fid,
            'start': line_start,
            'end': end_pos,
            'body': body
        })

print(f"Total focus matches: {len(focus_matches)}")
ids = [f['id'] for f in focus_matches]
from collections import Counter
counts = Counter(ids)
dups = {k: v for k, v in counts.items() if v > 1}
print(f"Duplicates: {dups}")
