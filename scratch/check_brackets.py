import re

with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
errors = []

for line_idx, line in enumerate(lines, 1):
    # strip comments
    c_idx = line.find('#')
    code = line[:c_idx] if c_idx != -1 else line
    
    # count braces
    for ch in code:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                errors.append(f'Negative depth at line {line_idx}: {line.strip()}')

print(f'Final depth: {depth}')
if depth != 0:
    print(f'ERROR: Unclosed braces! Final depth = {depth}')
if errors:
    print('Brace underflow errors:')
    for e in errors[:5]:
        print(' ', e)
