import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

d = 0
for idx, line in enumerate(lines, 1):
    l = re.sub(r'#[^\n]*', '', line)
    l = re.sub(r'"[^"]*"', '', l)
    open_c = l.count('{')
    close_c = l.count('}')
    d += open_c - close_c
    if idx > 5 and d <= 0:
        print(f"DEPTH DROPPED TO {d} AT LINE {idx}: {line.strip()}")
        break
    if 13035 <= idx <= 13055:
        print(f"{idx:5d} (depth={d}): {line.strip()}")

print(f"Total lines: {len(lines)}, final depth: {d}")
