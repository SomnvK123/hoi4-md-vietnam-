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

# Update program_edges to include the straight chains
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

# Update convergences
spec['convergences'] = {
    'VIE_lf_mech_complete': [['VIE_lf_mech_fire_support']],
    'VIE_lf_dev_strategic': [['VIE_lf_mobile_sustainment']],
    'VIE_lf_dev_territorial': [['VIE_lf_territorial_reserve']],
}

SPEC_FILE.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print("Updated structure_v30_2.json successfully!")
