# -*- coding: utf-8 -*-
with open('common/national_focus/VIE_md_focus.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Parser similar to audit.py
def get_focuses():
    # find all focus = { ... }
    blocks = []
    # simple stack
    i = 0
    n = len(text)
    while i < n:
        idx = text.find('focus = {', i)
        if idx == -1: break
        # find matching bracket
        stack = 1
        j = idx + 9
        while j < n and stack > 0:
            if text[j] == '{': stack += 1
            elif text[j] == '}': stack -= 1
            j += 1
        blocks.append(text[idx:j])
        i = j
    return blocks

focuses = {}
order = []
for b in get_focuses():
    fid_m = re.search(r'\bid\s*=\s*(\w+)', b)
    if not fid_m: continue
    fid = fid_m.group(1)
    xm = re.search(r'\bx\s*=\s*(-?\d+)', b)
    ym = re.search(r'\by\s*=\s*(-?\d+)', b)
    relm = re.search(r'\brelative_position_id\s*=\s*(\w+)', b)
    x = int(xm.group(1)) if xm else 0
    y = int(ym.group(1)) if ym else 0
    rel = relm.group(1) if relm else None
    focuses[fid] = {'x': x, 'y': y, 'rel': rel}
    order.append(fid)

abs_coords = {}
for fid in order:
    f = focuses[fid]
    if f['rel'] and f['rel'] in abs_coords:
        px, py = abs_coords[f['rel']]
        abs_coords[fid] = (px + f['x'], py + f['y'])
    else:
        abs_coords[fid] = (f['x'], f['y'])

print('VIE_doi_moi_continues:', abs_coords.get('VIE_doi_moi_continues'))
print('VIE_modernize_vpa:', abs_coords.get('VIE_modernize_vpa'))
print('VIE_force_47:', abs_coords.get('VIE_force_47'))
print('VIE_nav_n00_maritime_strategy_21st:', abs_coords.get('VIE_nav_n00_maritime_strategy_21st'))
