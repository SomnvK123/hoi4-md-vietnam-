import re

def main():
    with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the naval tree block
    # Start: # --- NAVAL TREE: V34 ORGANIC DIAMOND / SAIL BLUEPRINT ---
    # End: # ==========================================
    #      # AIR FORCE TREE: 2000-2020 Revamp
    match = re.search(r'(# --- NAVAL TREE: V34 ORGANIC DIAMOND / SAIL BLUEPRINT ---.*?)(# ==========================================\s+# AIR FORCE TREE)', content, re.DOTALL)
    if not match:
        print("Could not find naval section!")
        return

    naval_block = match.group(1)

    # Dictionary of exact clean prerequisites and relative anchors
    # (id: (rel_id, x, y, list_of_prereqs))
    clean_meta = {
        "VIE_nav_n00_maritime_strategy_21st": ("VIE_modernize_vpa", 10, 1, [["VIE_modernize_vpa"]]),
        "VIE_nav_t01_organization_reform": ("VIE_nav_n00_maritime_strategy_21st", -5, 1, [["VIE_nav_n00_maritime_strategy_21st"]]),
        "VIE_nav_i01_shipbuilding_industry": ("VIE_nav_n00_maritime_strategy_21st", 7, 1, [["VIE_nav_n00_maritime_strategy_21st"]]),
        
        "VIE_nav_s01_maritime_surveillance": ("VIE_nav_t01_organization_reform", -4, 1, [["VIE_nav_t01_organization_reform"]]),
        "VIE_nav_t02_officer_sailor_quality": ("VIE_nav_t01_organization_reform", 0, 1, [["VIE_nav_t01_organization_reform"]]),
        "VIE_nav_t03_regional_commands": ("VIE_nav_t01_organization_reform", 3, 1, [["VIE_nav_t01_organization_reform"]]),
        "VIE_nav_l01_naval_bases": ("VIE_nav_t01_organization_reform", 7, 1, [["VIE_nav_t01_organization_reform"]]),
        "VIE_nav_i02_technology_transfer_molniya": ("VIE_nav_i01_shipbuilding_industry", -2, 1, [["VIE_nav_i01_shipbuilding_industry"]]),
        "VIE_nav_i03_ship_systems_integration": ("VIE_nav_i01_shipbuilding_industry", 2, 1, [["VIE_nav_i01_shipbuilding_industry"]]),
        
        "VIE_nav_s02_island_defense_forces": ("VIE_nav_s01_maritime_surveillance", -1, 1, [["VIE_nav_s01_maritime_surveillance"]]),
        "VIE_nav_s03_subsurface_recon": ("VIE_nav_s01_maritime_surveillance", 1, 1, [["VIE_nav_s01_maritime_surveillance"]]),
        "VIE_nav_w01_surface_combatants": ("VIE_nav_t02_officer_sailor_quality", -1, 1, [["VIE_nav_t02_officer_sailor_quality"]]),
        "VIE_nav_w04_kilo_submarine_force": ("VIE_nav_t02_officer_sailor_quality", 1, 1, [["VIE_nav_t02_officer_sailor_quality"]]),
        "VIE_nav_t04_joint_command_system": ("VIE_nav_t03_regional_commands", 0, 1, [["VIE_nav_t02_officer_sailor_quality"], ["VIE_nav_t03_regional_commands"]]),
        "VIE_nav_l02_overhaul_maintenance": ("VIE_nav_l01_naval_bases", -1, 1, [["VIE_nav_l01_naval_bases"]]),
        "VIE_nav_l03_island_logistics": ("VIE_nav_l01_naval_bases", 1, 1, [["VIE_nav_l01_naval_bases"]]),
        "VIE_nav_i04_domestic_corvette_class": ("VIE_nav_i02_technology_transfer_molniya", 2, 1, [["VIE_nav_i02_technology_transfer_molniya"], ["VIE_nav_i03_ship_systems_integration"]]),
        
        "VIE_nav_s04_joint_island_defense": ("VIE_nav_s02_island_defense_forces", 1, 1, [["VIE_nav_s02_island_defense_forces"], ["VIE_nav_s03_subsurface_recon"]]),
        "VIE_nav_w02_missile_boats": ("VIE_nav_w01_surface_combatants", 0, 1, [["VIE_nav_w01_surface_combatants"]]),
        "VIE_nav_w03_multirole_frigates": ("VIE_nav_w04_kilo_submarine_force", 0, 1, [["VIE_nav_w01_surface_combatants"]]),
        "VIE_nav_l04_support_rescue_vessels": ("VIE_nav_l02_overhaul_maintenance", 1, 1, [["VIE_nav_l02_overhaul_maintenance"], ["VIE_nav_l03_island_logistics"]]),
        
        "VIE_nav_s05_unified_maritime_picture": ("VIE_nav_s04_joint_island_defense", 0, 1, [["VIE_nav_s04_joint_island_defense"]]),
        "VIE_nav_w05_asw_fleet_defense": ("VIE_nav_w03_multirole_frigates", 0, 1, [["VIE_nav_w03_multirole_frigates"]]),
        "VIE_nav_l05_sustained_operations": ("VIE_nav_l04_support_rescue_vessels", 0, 1, [["VIE_nav_l04_support_rescue_vessels"]]),
        
        "VIE_nav_p01_integrated_defense_choice": ("VIE_nav_t04_joint_command_system", -5, 3, [["VIE_nav_t04_joint_command_system"]]),
        "VIE_nav_h01_fleet_development_priority": ("VIE_nav_t04_joint_command_system", 2, 3, [["VIE_nav_t04_joint_command_system"]]),
        
        "VIE_nav_p02_coastal_island_network": ("VIE_nav_p01_integrated_defense_choice", -2, 1, [["VIE_nav_p01_integrated_defense_choice"]]),
        "VIE_nav_p03_island_territory_defense": ("VIE_nav_p01_integrated_defense_choice", 2, 1, [["VIE_nav_p01_integrated_defense_choice"]]),
        "VIE_nav_h02_multirole_task_groups": ("VIE_nav_h01_fleet_development_priority", 0, 1, [["VIE_nav_h01_fleet_development_priority"]]),
        
        "VIE_nav_p04_layered_defense": ("VIE_nav_p02_coastal_island_network", 0, 1, [["VIE_nav_p02_coastal_island_network"]]),
        "VIE_nav_g01_greenwater_navy": ("VIE_nav_h02_multirole_task_groups", -2, 1, [["VIE_nav_h02_multirole_task_groups"]]),
        "VIE_nav_b01_bluewater_navy": ("VIE_nav_h02_multirole_task_groups", 3, 1, [["VIE_nav_h02_multirole_task_groups"]]),
        
        "VIE_nav_p05_joint_coastal_defense": ("VIE_nav_p04_layered_defense", 2, 1, [["VIE_nav_p04_layered_defense"]]),
        "VIE_nav_g02_advanced_frigates_asw": ("VIE_nav_g01_greenwater_navy", 0, 1, [["VIE_nav_g01_greenwater_navy"]]),
        "VIE_nav_b02_extended_deployment_fleet": ("VIE_nav_b01_bluewater_navy", 0, 1, [["VIE_nav_b01_bluewater_navy"]]),
        
        "VIE_nav_p06_active_coastal_defense_capstone": ("VIE_nav_p05_joint_coastal_defense", 0, 1, [["VIE_nav_p05_joint_coastal_defense"]]),
        "VIE_nav_g03_self_reliant_greenwater_capstone": ("VIE_nav_g02_advanced_frigates_asw", 0, 1, [["VIE_nav_g02_advanced_frigates_asw"]]),
        "VIE_nav_b03_sustained_bluewater_capstone": ("VIE_nav_b02_extended_deployment_fleet", 0, 1, [["VIE_nav_b02_extended_deployment_fleet"]]),
        
        "VIE_nav_f01_tactical_doctrine_alignment": (
            "VIE_nav_g03_self_reliant_greenwater_capstone", 0, 1,
            [[
                "VIE_nav_p06_active_coastal_defense_capstone",
                "VIE_nav_g03_self_reliant_greenwater_capstone",
                "VIE_nav_b03_sustained_bluewater_capstone"
            ]]
        ),
        "VIE_nav_f02_regular_modern_navy": ("VIE_nav_f01_tactical_doctrine_alignment", 0, 1, [["VIE_nav_f01_tactical_doctrine_alignment"]]),
    }

    # Process each focus in the naval_block
    # Extract each focus block
    focus_pattern = re.compile(r'(\tfocus\s*=\s*\{\s*id\s*=\s*(VIE_nav_[a-z0-9_]+)\s*\n)(.*?)(\n\t\})', re.DOTALL)

    def replace_focus(m):
        header = m.group(1)
        fid = m.group(2)
        body = m.group(3)
        footer = m.group(4)

        if fid not in clean_meta:
            return m.group(0)

        rel_id, dx, dy, prereqs_list = clean_meta[fid]

        # Remove existing relative_position_id, x, y
        body = re.sub(r'\t+x\s*=\s*[-0-9]+\n', '', body)
        body = re.sub(r'\t+y\s*=\s*[-0-9]+\n', '', body)
        body = re.sub(r'\t+relative_position_id\s*=\s*[a-zA-Z0-9_]+\n', '', body)

        # Remove existing prerequisite blocks
        body = re.sub(r'\t+prerequisite\s*=\s*\{[^\}]*\}\n*', '', body)

        # Build position block
        pos_block = f"\t\tx = {dx}\n\t\ty = {dy}\n"
        if rel_id:
            pos_block += f"\t\trelative_position_id = {rel_id}\n\n"

        # Build prereqs block
        prereq_blocks = ""
        for pgroup in prereqs_list:
            if len(pgroup) == 1:
                prereq_blocks += f"\t\tprerequisite = {{ focus = {pgroup[0]} }}\n"
            else:
                # OR condition
                joined = " ".join(f"focus = {p}" for p in pgroup)
                prereq_blocks += f"\t\tprerequisite = {{ {joined} }}\n"

        if prereq_blocks:
            prereq_blocks += "\n"

        # Re-insert position right after icon
        icon_match = re.search(r'(\t+icon\s*=\s*[a-zA-Z0-9_]+\n)', body)
        if icon_match:
            idx = icon_match.end()
            body_before = body[:idx]
            body_after = body[idx:].lstrip()
            new_body = body_before + "\n" + pos_block + prereq_blocks + body_after
        else:
            new_body = pos_block + prereq_blocks + body

        return header + new_body + footer

    new_naval_block = focus_pattern.sub(replace_focus, naval_block)

    new_content = content[:match.start(1)] + new_naval_block + content[match.end(1):]

    with open("common/national_focus/VIE_md_focus.txt", "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Naval focus prerequisites cleaned up according to Image 2 blueprint!")

if __name__ == "__main__":
    main()
