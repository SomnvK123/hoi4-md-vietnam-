import json

with open('tools/audit/focus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

attrs = data['attrs']
vpa = attrs.get('VIE_modernize_vpa')
print('VIE_modernize_vpa:', vpa)

# find all military focuses (abs X >= 160)
mil = []
for fid, att in attrs.items():
    abs_pos = att.get('absolute')
    if abs_pos and abs_pos[0] >= 160:
        mil.append((fid, abs_pos, att.get('relative_position_id'), (att.get('x'), att.get('y'))))

mil.sort(key=lambda x: (x[1][1], x[1][0]))
print(f'Total military focuses with X >= 160: {len(mil)}')
for fid, ab, rel, off in mil:
    print(f'{fid:45} abs={ab} rel={rel} off={off}')
