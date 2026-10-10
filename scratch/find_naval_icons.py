import re

with open('interface/VIE_md_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

sprites = re.findall(r'name\s*=\s*\"?([^\s\"\n]+)\"?', text)
print(f'Total sprites: {len(sprites)}')
nav = [s for s in sprites if any(k in s.lower() for k in ['nav', 'sea', 'ship', 'kilo', 'gepard', 'boat', 'water', 'sub', 'fleet', 'maritime', 'dock', 'ocean', 'coast', 'ba_son', 'corvette', 'frigate'])]
print(f'Naval related sprites: {len(nav)}')
for s in nav:
    print(s)
