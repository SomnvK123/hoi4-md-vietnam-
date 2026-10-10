import os
import re

icons = [
    'GFX_focus_VIE_naval_defence_law', 'GFX_focus_VIE_ba_son_shipyards', 'GFX_focus_VIE_naval_mro',
    'GFX_focus_VIE_small_combatant_construction', 'GFX_focus_VIE_naval_systems_integration',
    'GFX_focus_VIE_naval_defence_2030', 'GFX_focus_VIE_nf_surface_force', 'GFX_focus_VIE_nf_submarine_force',
    'GFX_focus_VIE_nf_first_force', 'GFX_focus_VIE_nf_medium_force', 'GFX_focus_VIE_nf_operating_range',
    'GFX_focus_VIE_nf_denial', 'GFX_focus_VIE_nf_denial_defence', 'GFX_focus_VIE_nf_denial_subs',
    'GFX_focus_VIE_nf_denial_command', 'GFX_focus_VIE_nf_greenwater', 'GFX_focus_VIE_nf_regional_frigates',
    'GFX_focus_VIE_nf_amphibious_fleet', 'GFX_focus_VIE_nf_lhd_program', 'GFX_focus_VIE_nf_regional_command',
    'GFX_focus_VIE_nf_bluewater', 'GFX_focus_VIE_nf_ocean_escort', 'GFX_focus_VIE_nf_replenishment',
    'GFX_focus_VIE_nf_naval_aviation', 'GFX_focus_VIE_nf_carrier_group', 'GFX_focus_VIE_scs_law_of_the_sea',
    'GFX_focus_VIE_scs_assert_maritime_rights', 'GFX_focus_VIE_scs_maritime_militia',
    'GFX_focus_VIE_scs_coast_guard_law', 'GFX_focus_VIE_scs_maritime_cooperation'
]

with open('interface/VIE_md_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

missing_dds = 0
for ic in icons:
    idx = text.find(ic)
    if idx != -1:
        snippet = text[idx:idx+150]
        tf = re.search(r'texturefile\s*=\s*"([^"]+)"', snippet)
        if tf:
            path = tf.group(1).replace('/', os.sep)
            if not os.path.exists(path):
                print(f'{ic} texture missing: {path}')
                missing_dds += 1
        else:
            print(f'{ic} no texturefile found in gfx block')
    else:
        print(f'{ic} not defined in gfx file')

print(f'Verification complete. Total missing DDS: {missing_dds}')
