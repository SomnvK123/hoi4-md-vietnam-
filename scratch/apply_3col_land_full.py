import json
import re
from pathlib import Path

ROOT = Path('d:/HOI4Mods/md_vietnam')
FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
SPEC_FILE = ROOT / '.claude/docs/land/structure_v30_2.json'

content = FOCUS_FILE.read_text(encoding='utf-8')
spec = json.loads(SPEC_FILE.read_text(encoding='utf-8'))

# 1. Update spec['positions']
new_positions = dict(spec['positions'])
new_positions.update({
    # Strategy M (col 174)
    'VIE_lf_fs_main_corps': [174, 7],
    'VIE_lf_fs_lean_corps': [174, 8],
    'VIE_lf_mech_coordination': [174, 9],
    'VIE_lf_mech_fire_support': [174, 10],
    'VIE_lf_mech_complete': [174, 11],
    # Strategy R (col 180)
    'VIE_lf_fs_mobile_force': [180, 7],
    'VIE_lf_fs_mobile_corps': [180, 8],
    'VIE_lf_mobile_fire_support': [180, 9],
    'VIE_lf_mobile_sustainment': [180, 10],
    'VIE_lf_dev_strategic': [180, 11],
    # Strategy D (col 186)
    'VIE_lf_fs_depth_defence': [186, 7],
    'VIE_lf_fs_militia_units': [186, 8],
    'VIE_lf_territorial_coordination': [186, 9],
    'VIE_lf_territorial_reserve': [186, 10],
    'VIE_lf_dev_territorial': [186, 11],
    # Downstream
    'VIE_lf_command_reform_2': [180, 12],
    'VIE_lf_cap_army_ad': [174, 13],
    'VIE_lf_selective_modernization': [180, 13],
    'VIE_lf_cap_border_urban': [186, 13],
    'VIE_lf_cap_ad_coord': [174, 14],
    'VIE_lf_command_reform_3': [180, 14],
    'VIE_lf_cap_area_control': [186, 14],
    'VIE_lf_cap_info_ops': [174, 15],
    'VIE_lf_force_complete': [180, 15],
    'VIE_lf_cap_cyber_ew': [174, 16],
})
spec['positions'] = new_positions

spec['program_edges'].update({
    'VIE_lf_fs_lean_corps': 'VIE_lf_fs_main_corps',
    'VIE_lf_mech_coordination': 'VIE_lf_fs_lean_corps',
    'VIE_lf_mech_fire_support': 'VIE_lf_mech_coordination',
    'VIE_lf_mech_complete': 'VIE_lf_mech_fire_support',

    'VIE_lf_fs_mobile_corps': 'VIE_lf_fs_mobile_force',
    'VIE_lf_mobile_fire_support': 'VIE_lf_fs_mobile_corps',
    'VIE_lf_mobile_sustainment': 'VIE_lf_mobile_fire_support',
    'VIE_lf_dev_strategic': 'VIE_lf_mobile_sustainment',

    'VIE_lf_fs_militia_units': 'VIE_lf_fs_depth_defence',
    'VIE_lf_territorial_coordination': 'VIE_lf_fs_militia_units',
    'VIE_lf_territorial_reserve': 'VIE_lf_territorial_coordination',
    'VIE_lf_dev_territorial': 'VIE_lf_territorial_reserve',
})

spec['convergences'] = {
    'VIE_lf_mech_complete': [['VIE_lf_mech_fire_support']],
    'VIE_lf_dev_strategic': [['VIE_lf_mobile_sustainment']],
    'VIE_lf_dev_territorial': [['VIE_lf_territorial_reserve']],
}

SPEC_FILE.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print("Updated structure_v30_2.json successfully!")

# 2. Update focus blocks in VIE_md_focus.txt
def replace_focus_prop(block, prop, new_val):
    pattern = rf'(?m)^(\t+{prop}\s*=\s*).*?$'
    if re.search(pattern, block):
        return re.sub(pattern, rf'\g<1>{new_val}', block)
    else:
        return re.sub(rf'(?m)^(\t+id\s*=\s*\S+\n)', rf'\g<1>\t{prop} = {new_val}\n', block)

def set_focus_prereqs(block, prereq_fids):
    # remove existing prerequisites
    block = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{[^\n\}]*\}\n*', '', block)
    # insert new prerequisites before search_filters or cost or available
    prereq_str = ''
    for fid in prereq_fids:
        prereq_str += f'\t\tprerequisite = {{ focus = {fid} }}\n'
    if re.search(r'(?m)^\t+search_filters\s*=\s*\{', block):
        block = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', f'{prereq_str}\n\\g<1>', block)
    elif re.search(r'(?m)^\t+available\s*=\s*\{', block):
        block = re.sub(r'(?m)^(\t+available\s*=\s*\{)', f'{prereq_str}\n\\g<1>', block)
    else:
        block = re.sub(r'(?m)^(\t+completion_reward\s*=\s*\{)', f'{prereq_str}\n\\g<1>', block)
    return block

def get_focus_block(text, fid):
    m = re.search(rf'(?ms)(^\tfocus\s*=\s*\{{\n\s*id\s*=\s*{fid}\b.*?^\t\}})', text)
    assert m, f'Focus {fid} not found'
    return m.group(1), m.start(), m.end()

def update_block(text, fid, mutator):
    block, st, en = get_focus_block(text, fid)
    new_b = mutator(block)
    return text[:st] + new_b + text[en:]

# Update definitions: (fid, anchor, dx, dy, prereqs)
updates = [
    # Strategy M
    ('VIE_lf_fs_main_corps', 'VIE_lf_command_reform_1', -6, 1, ['VIE_lf_command_reform_1']),
    ('VIE_lf_fs_lean_corps', 'VIE_lf_fs_main_corps', 0, 1, ['VIE_lf_fs_main_corps']),
    ('VIE_lf_mech_coordination', 'VIE_lf_fs_lean_corps', 0, 1, ['VIE_lf_fs_lean_corps']),
    ('VIE_lf_mech_fire_support', 'VIE_lf_mech_coordination', 0, 1, ['VIE_lf_mech_coordination']),
    ('VIE_lf_mech_complete', 'VIE_lf_mech_fire_support', 0, 1, ['VIE_lf_mech_fire_support']),

    # Strategy R
    ('VIE_lf_fs_mobile_force', 'VIE_lf_command_reform_1', 0, 1, ['VIE_lf_command_reform_1']),
    ('VIE_lf_fs_mobile_corps', 'VIE_lf_fs_mobile_force', 0, 1, ['VIE_lf_fs_mobile_force']),
    ('VIE_lf_mobile_fire_support', 'VIE_lf_fs_mobile_corps', 0, 1, ['VIE_lf_fs_mobile_corps']),
    ('VIE_lf_mobile_sustainment', 'VIE_lf_mobile_fire_support', 0, 1, ['VIE_lf_mobile_fire_support']),
    ('VIE_lf_dev_strategic', 'VIE_lf_mobile_sustainment', 0, 1, ['VIE_lf_mobile_sustainment']),

    # Strategy D
    ('VIE_lf_fs_depth_defence', 'VIE_lf_command_reform_1', 6, 1, ['VIE_lf_command_reform_1']),
    ('VIE_lf_fs_militia_units', 'VIE_lf_fs_depth_defence', 0, 1, ['VIE_lf_fs_depth_defence']),
    ('VIE_lf_territorial_coordination', 'VIE_lf_fs_militia_units', 0, 1, ['VIE_lf_fs_militia_units']),
    ('VIE_lf_territorial_reserve', 'VIE_lf_territorial_coordination', 0, 1, ['VIE_lf_territorial_coordination']),
    ('VIE_lf_dev_territorial', 'VIE_lf_territorial_reserve', 0, 1, ['VIE_lf_territorial_reserve']),

    # Downstream
    ('VIE_lf_command_reform_2', 'VIE_lf_dev_strategic', 0, 1, ['VIE_lf_mech_complete focus = VIE_lf_dev_strategic focus = VIE_lf_dev_territorial']),
    ('VIE_lf_cap_army_ad', 'VIE_lf_command_reform_2', -6, 1, ['VIE_lf_command_reform_2']),
    ('VIE_lf_selective_modernization', 'VIE_lf_command_reform_2', 0, 1, ['VIE_lf_command_reform_2']),
    ('VIE_lf_cap_border_urban', 'VIE_lf_command_reform_2', 6, 1, ['VIE_lf_command_reform_2']),
    ('VIE_lf_cap_ad_coord', 'VIE_lf_cap_army_ad', 0, 1, ['VIE_lf_cap_army_ad']),
    ('VIE_lf_command_reform_3', 'VIE_lf_selective_modernization', 0, 1, ['VIE_lf_selective_modernization']),
    ('VIE_lf_cap_area_control', 'VIE_lf_cap_border_urban', 0, 1, ['VIE_lf_cap_border_urban']),
    ('VIE_lf_cap_info_ops', 'VIE_lf_cap_ad_coord', 0, 1, ['VIE_lf_cap_ad_coord']),
    ('VIE_lf_force_complete', 'VIE_lf_command_reform_3', 0, 1, ['VIE_lf_command_reform_3']),
    ('VIE_lf_cap_cyber_ew', 'VIE_lf_cap_info_ops', 0, 1, ['VIE_lf_cap_info_ops']),
]

for fid, anchor, dx, dy, prereqs in updates:
    def make_mut(a, x, y, pr):
        def mut(b):
            b = replace_focus_prop(b, 'relative_position_id', a)
            b = replace_focus_prop(b, 'x', str(x))
            b = replace_focus_prop(b, 'y', str(y))
            b = set_focus_prereqs(b, pr)
            return b
        return mut
    content = update_block(content, fid, make_mut(anchor, dx, dy, prereqs))

# 3. Fix file declaration order to ensure top-down anchors:
# In Strategy M: VIE_lf_fs_lean_corps must be before VIE_lf_mech_coordination
b_coordination, st_c, en_c = get_focus_block(content, 'VIE_lf_mech_coordination')
b_lean, st_l, en_l = get_focus_block(content, 'VIE_lf_fs_lean_corps')
if st_c < st_l:
    # swap them
    print("Reordering Strategy M blocks (lean_corps before mech_coordination)...")
    content = update_block(content, 'VIE_lf_fs_lean_corps', lambda _: b_coordination)
    content = update_block(content, 'VIE_lf_mech_coordination', lambda _: b_lean)

# In Strategy D: VIE_lf_territorial_coordination must be before VIE_lf_territorial_reserve
b_reserve, st_r, en_r = get_focus_block(content, 'VIE_lf_territorial_reserve')
b_coord_d, st_cd, en_cd = get_focus_block(content, 'VIE_lf_territorial_coordination')
if st_r < st_cd:
    print("Reordering Strategy D blocks (territorial_coordination before territorial_reserve)...")
    content = update_block(content, 'VIE_lf_territorial_coordination', lambda _: b_reserve)
    content = update_block(content, 'VIE_lf_territorial_reserve', lambda _: b_coord_d)

FOCUS_FILE.write_text(content, encoding='utf-8')
print("Successfully updated VIE_md_focus.txt!")
