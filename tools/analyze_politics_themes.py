import re
from pathlib import Path
from collections import defaultdict
import sys
sys.path.insert(0, ".")

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
focuses = {}
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == '{': brace += 1
        elif txt[i] == '}':
            brace -= 1
            if brace == 0: end = i + 1; break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    mut = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses[fid] = {
        'id': fid, 'x': int(xm.group(1)) if xm else 0, 'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None, 'prereqs': prereqs, 'mut': mut
    }

themes = {
    'Congress Spine': ['VIE_prepare_congress_9', 'VIE_resolution_congress_9', 'VIE_resolution_congress_10', 'VIE_resolution_congress_11', 'VIE_resolution_congress_12', 'VIE_resolution_congress_13', 'VIE_resolution_congress_14', 'VIE_concentration_of_power', 'VIE_institutional_opening', 'VIE_era_of_rising', 'VIE_party_centennial_2030'],
    'Party & Anti-Corruption': ['VIE_party_members_private_business', 'VIE_anti_corruption_steering', 'VIE_asset_declaration', 'VIE_tw4_party_building', 'VIE_party_inspection', 'VIE_party_discipline', 'VIE_cadre_accountability', 'VIE_asset_recovery', 'VIE_clean_cadres', 'VIE_peoples_oversight', 'VIE_digital_anticorruption'],
    'Governance & State Reform': ['VIE_grassroots_democracy', 'VIE_mass_mobilization', 'VIE_ethnic_policy', 'VIE_national_assembly_role', 'VIE_state_audit', 'VIE_public_admin_reform', 'VIE_anti_corruption_law', 'VIE_decentralization', 'VIE_platform_2011', 'VIE_streamline_apparatus', 'VIE_e_government', 'VIE_resolution_57_68', 'VIE_institutional_bottlenecks'],
    'Rule of Law & Education/Social': ['VIE_rule_of_law_state', 'VIE_constitution_2013', 'VIE_cybersecurity_law', 'VIE_higher_education_law', 'VIE_education_law_2019', 'VIE_disaster_law_2013', 'VIE_civil_defense_law_2023']
}

for name, fids in themes.items():
    print(f"\n=== {name} ({len(fids)} focuses) ===")
    for fid in fids:
        f = focuses[fid]
        p_list = [p.replace("VIE_", "") for p in f["prereqs"]]
        sid = fid.replace("VIE_", "")
        print(f"  {sid:30s} | prereqs={p_list}")
