import os
import re

with open('interface/VIE_md_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

sprites = re.findall(r'name\s*=\s*"([^"]+)"', text)
keywords = ['nav', 'sub', 'ship', 'sea', 'water', 'fleet', 'maritime', 'dock', 'port', 'island', 'ocean', 'coast', 'kilo', 'gepard', 'cam_ranh', 'truong_sa', 'bastion', 'radar', 'missile', 'aviation']
matched = [s for s in sorted(sprites) if any(k in s.lower() for k in keywords)]
print(f"Total matched sprites: {len(matched)}")
for s in matched:
    print(s)
