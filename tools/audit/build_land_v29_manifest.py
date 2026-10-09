"""Rebuild the reviewed v29 land layout manifest from live focus definitions."""
import json
from pathlib import Path

from industry import ROOT, focus_map, groups, positions, value, values


SOURCE = ROOT / '.claude/docs/land/structure_v28.json'
DEST = ROOT / '.claude/docs/land/structure_v29.json'


def main():
    spec = json.loads(SOURCE.read_text(encoding='utf-8'))
    focuses = focus_map((ROOT / 'common/national_focus/VIE_md_focus.txt').read_text(encoding='utf-8'))
    pos = positions(focuses)
    purposes = {
        2: 'foundation', 3: 'foundation support', 4: 'branch training',
        5: 'branch proficiency gate', 6: 'combined-arms gate',
        7: 'command reform I', 8: 'mutually exclusive force priority',
        9: 'parallel route projects', 10: 'route completion AND gate',
        11: 'shared command reform II', 12: 'capability specialization',
        13: 'capability specialization branch', 14: 'two-of-three capability gate',
        15: 'command reform III', 16: 'land-force capstone',
    }
    coordinates = {}
    by_id = {node[0]: node for path in spec['paths'] for node in path['nodes']}
    definitions = [
        ('regular', 'fs_main_corps', ['fs_lean_corps', 'mech_equipment', 'mech_sustainment'], 'mech_complete'),
        ('mobile', 'fs_mobile_force', ['fs_mobile_corps', 'mobile_fire_support', 'mobile_sustainment'], 'dev_strategic'),
        ('depth', 'fs_depth_defence', ['fs_militia_units', 'territorial_reserve', 'territorial_coordination'], 'dev_territorial'),
    ]
    for flag, root, components, terminal in definitions:
        path = next(p for p in spec['paths'] if p['flag'] == flag)
        ids = [root, *components, terminal]
        path['root'] = root
        path['components'] = components
        path['terminal'] = terminal
        path['column'] = pos['VIE_lf_' + root][0]
        path['nodes'] = [by_id[node_id] for node_id in ids]
        path['positions'] = [list(pos['VIE_lf_' + node_id]) for node_id in ids]
        for node_id in ids:
            coordinates['VIE_lf_' + node_id] = flag

    layout = {}
    for fid in sorted((fid for fid in focuses if fid.startswith('VIE_lf_')), key=lambda f: (pos[f][1], pos[f][0])):
        node = focuses[fid]
        x, y = pos[fid]
        anchor = value(node, 'relative_position_id')
        pre = groups(node)
        ex = values(value(node, 'mutually_exclusive', []), 'focus')
        layout[fid] = {
            'position': [x, y], 'display_row': y,
            'purpose': purposes[y], 'anchor': anchor, 'pre': pre,
            'ex': ex, 'available': value(node, 'available', []) or [],
        }
    spec['layout'] = layout
    DEST.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {DEST.name}: {len(layout)} focus records; 3 routes with 3 sibling projects and one AND terminal each.')


if __name__ == '__main__':
    main()
