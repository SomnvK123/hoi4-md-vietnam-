import re
from pathlib import Path
import sys

target_path = Path(r"d:\HOI4Mods\md_vietnam\common\national_focus\VIE_md_focus.txt")
# Restore from bak first to be completely clean
bak_path = Path(r"d:\HOI4Mods\md_vietnam\common\national_focus\VIE_md_focus.txt.bak")
txt = bak_path.read_text(encoding="utf-8")

# Parse all focus blocks with exact char offsets
focus_blocks = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    end = m.end()
    for i in range(m.end(), len(txt)):
        if txt[i] == "{": brace += 1
        elif txt[i] == "}":
            brace -= 1
            if brace == 0:
                end = i + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    x = int(xm.group(1)) if xm else 0
    y = int(ym.group(1)) if ym else 0
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    rel = rel.group(1) if rel else None
    
    focus_blocks.append({
        "id": fid, "start": start, "end": end, "block": block,
        "x": x, "y": y, "rel": rel
    })

fmap = {f["id"]: f for f in focus_blocks}
print(f"Parsed {len(focus_blocks)} focus blocks from backup.")

# Planned modifications: fid -> (new_x, new_y)
modifications = {}

# 1. Root of Doi Moi
modifications["VIE_doi_moi_continues"] = (80, 0)

# 2. CHINH TRI (42 focuses)
chinh_tri_fids = [
    "VIE_prepare_congress_9", "VIE_grassroots_democracy", "VIE_mass_mobilization",
    "VIE_resolution_congress_9", "VIE_ethnic_policy", "VIE_national_assembly_role",
    "VIE_state_audit", "VIE_public_admin_reform", "VIE_anti_corruption_law",
    "VIE_decentralization", "VIE_resolution_congress_10", "VIE_party_members_private_business",
    "VIE_anti_corruption_steering", "VIE_asset_declaration", "VIE_resolution_congress_11",
    "VIE_tw4_party_building", "VIE_platform_2011", "VIE_rule_of_law_state",
    "VIE_party_inspection", "VIE_constitution_2013", "VIE_resolution_congress_12",
    "VIE_party_discipline", "VIE_streamline_apparatus", "VIE_cybersecurity_law",
    "VIE_cadre_accountability", "VIE_asset_recovery", "VIE_clean_cadres",
    "VIE_resolution_congress_13", "VIE_peoples_oversight", "VIE_digital_anticorruption",
    "VIE_e_government", "VIE_resolution_57_68", "VIE_institutional_bottlenecks",
    "VIE_resolution_congress_14", "VIE_concentration_of_power", "VIE_institutional_opening",
    "VIE_era_of_rising", "VIE_party_centennial_2030"
]

for fid in chinh_tri_fids:
    old_x = fmap[fid]["x"]
    old_y = fmap[fid]["y"]
    modifications[fid] = (old_x + 32, old_y)

# 4 constitutional sub-laws
modifications["VIE_higher_education_law"] = (4, 1)
modifications["VIE_education_law_2019"] = (4, 2)
modifications["VIE_disaster_law_2013"] = (8, 1)
modifications["VIE_civil_defense_law_2023"] = (8, 2)

# 3. QUAN SU root
modifications["VIE_modernize_vpa"] = (114, 1)

# 4. DOI NGOAI root
modifications["VIE_asean_integration"] = (-48, 12)

# 5. BIEN DONG root & bridge
modifications["VIE_law_of_the_sea"] = (2, 13)
modifications["VIE_un_peacekeeping"] = (-18, 5)
modifications["VIE_four_nos_doctrine"] = (-18, 6)

# 6. AN NINH NOI DIA (8 focuses)
modifications["VIE_sec_cyber_control"] = (20, 13)
modifications["VIE_sec_surveillance_network"] = (18, 14)
modifications["VIE_sec_public_order"] = (20, 14)
modifications["VIE_sec_security_economy"] = (22, 14)
modifications["VIE_sec_cyber_sovereignty"] = (18, 15)
modifications["VIE_sec_loyalty_vetting"] = (20, 15)
modifications["VIE_sec_border_control"] = (22, 15)
modifications["VIE_sec_managed_opening"] = (20, 16)

print(f"Total focus modifications planned: {len(modifications)}")
assert len(modifications) == 56, f"Expected 56 modifications, got {len(modifications)}"

# Reconstruct text by replacing in reverse order of start offset
new_txt = txt
for f in sorted(focus_blocks, key=lambda x: x["start"], reverse=True):
    fid = f["id"]
    if fid in modifications:
        nx, ny = modifications[fid]
        block = f["block"]
        # Replace x = ... and y = ... inside block
        # Only replace the top-level x = and y = within the first 300 chars of block
        header_end = min(300, len(block))
        header = block[:header_end]
        rest = block[header_end:]
        
        # Replace x
        header = re.sub(r"(\bx\s*=\s*)-?\d+", r"\g<1>" + str(nx), header, count=1)
        # Replace y
        header = re.sub(r"(\by\s*=\s*)-?\d+", r"\g<1>" + str(ny), header, count=1)
        
        new_block = header + rest
        new_txt = new_txt[:f["start"]] + new_block + new_txt[f["end"]:]

target_path.write_text(new_txt, encoding="utf-8")
print("Successfully written updated VIE_md_focus.txt!")
