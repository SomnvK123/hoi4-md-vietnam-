import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
FOCUS_FILE = ROOT / 'common/national_focus/VIE_md_focus.txt'
content = FOCUS_FILE.read_text(encoding='utf-8')

def replace_focus_prop(block, prop, new_val):
    pattern = rf'(?m)^(\t+{prop}\s*=\s*).*?$'
    if re.search(pattern, block):
        return re.sub(pattern, rf'\g<1>{new_val}', block)
    else:
        return re.sub(rf'(?m)^(\t+id\s*=\s*\S+\n)', rf'\g<1>\t{prop} = {new_val}\n', block)

def update_focus(text, fid, mutator):
    pattern = rf'(?ms)(^\tfocus\s*=\s*\{{\n\s*id\s*=\s*{fid}\b.*?^\t\}})'
    match = re.search(pattern, text)
    if not match:
        raise ValueError(f"Focus {fid} not found!")
    old_block = match.group(1)
    new_block = mutator(old_block)
    return text[:match.start()] + new_block + text[match.end():]

# ==========================================
# 1. NAVY
# ==========================================
def fix_naval_defence(b):
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_naval_mro\s*\}\n', '', b)
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_small_combatant_construction\s*\}\n', '', b)
    return b
content = update_focus(content, 'VIE_naval_defence_2030', fix_naval_defence)

# ==========================================
# 2. POLITICS
# ==========================================
def fix_party_members(b):
    return replace_focus_prop(b, 'x', '-74')
content = update_focus(content, 'VIE_party_members_private_business', fix_party_members)

def fix_asset_declaration(b):
    return replace_focus_prop(b, 'y', '5')
content = update_focus(content, 'VIE_asset_declaration', fix_asset_declaration)

def fix_party_inspection(b):
    return replace_focus_prop(b, 'y', '6')
content = update_focus(content, 'VIE_party_inspection', fix_party_inspection)

def fix_party_discipline(b):
    b = replace_focus_prop(b, 'y', '7')
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_resolution_congress_12\s*\}\n', '', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_resolution_congress_12' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_resolution_congress_12', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_resolution_congress_12\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_party_discipline', fix_party_discipline)

def fix_cadre_accountability(b):
    return replace_focus_prop(b, 'y', '8')
content = update_focus(content, 'VIE_cadre_accountability', fix_cadre_accountability)

def fix_asset_recovery(b):
    return replace_focus_prop(b, 'y', '8')
content = update_focus(content, 'VIE_asset_recovery', fix_asset_recovery)

def fix_clean_cadres(b):
    return replace_focus_prop(b, 'y', '9')
content = update_focus(content, 'VIE_clean_cadres', fix_clean_cadres)

def fix_concentration_power(b):
    return replace_focus_prop(b, 'y', '10')
content = update_focus(content, 'VIE_concentration_of_power', fix_concentration_power)

def fix_institutional_opening(b):
    return replace_focus_prop(b, 'y', '10')
content = update_focus(content, 'VIE_institutional_opening', fix_institutional_opening)

def fix_era_rising(b):
    return replace_focus_prop(b, 'y', '11')
content = update_focus(content, 'VIE_era_of_rising', fix_era_rising)

def fix_party_centennial(b):
    return replace_focus_prop(b, 'y', '12')
content = update_focus(content, 'VIE_party_centennial_2030', fix_party_centennial)

# ==========================================
# 3. ECONOMY & BANKING
# ==========================================
def fix_enterprise_law(b):
    if 'prerequisite' not in b:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tprerequisite = { focus = VIE_doi_moi_continues }\n\n\g<1>', b)
    b = re.sub(r'(?m)^\t+available\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_doi_moi_continues\s*\}\n+', '', b)
    return b
content = update_focus(content, 'VIE_enterprise_law', fix_enterprise_law)

def fix_state_bank(b):
    if 'prerequisite' not in b:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tprerequisite = { focus = VIE_doi_moi_continues }\n\n\g<1>', b)
    b = re.sub(r'(?m)^\t+available\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_doi_moi_continues\s*\}\n+', '', b)
    return b
content = update_focus(content, 'VIE_state_bank_modernization', fix_state_bank)
def fix_bta_usa(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_enterprise_law')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_doi_moi_continues\s*\}', 'prerequisite = { focus = VIE_enterprise_law }', b)
    return b
content = update_focus(content, 'VIE_bilateral_trade_agreement_usa', fix_bta_usa)

def fix_rice_export(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_doi_moi_continues')
    b = replace_focus_prop(b, 'x', '-18')
    b = replace_focus_prop(b, 'y', '3')
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_enterprise_law\s*\}\n', '', b)
    return b
content = update_focus(content, 'VIE_rice_export_power', fix_rice_export)

def fix_household(b):
    return replace_focus_prop(b, 'x', '-10')
content = update_focus(content, 'VIE_household_business', fix_household)

def fix_corporate_bond(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_enterprise_law')
    b = replace_focus_prop(b, 'x', '10')
    b = replace_focus_prop(b, 'y', '2')
    return b
content = update_focus(content, 'VIE_corporate_bond_reform', fix_corporate_bond)

def fix_market_upgrade(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_corporate_bond_reform')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_market_upgrade_criteria', fix_market_upgrade)

def fix_intl_financial_centre(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_market_upgrade_criteria')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_cross_ownership_crackdown\s*\}', 'prerequisite = { focus = VIE_market_upgrade_criteria }', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_cross_ownership_crackdown' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_cross_ownership_crackdown', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_cross_ownership_crackdown\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_international_financial_centre', fix_intl_financial_centre)

def fix_investment_grade(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_international_financial_centre')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_investment_grade', fix_investment_grade)

def fix_cashless(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_state_bank_modernization')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_cashless_payments', fix_cashless)

# Gold focuses anchored to deposit insurance
def fix_gold_monopoly_2012(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_state_bank_modernization')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '3')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_state_bank_modernization\s*\}', 'prerequisite = { focus = VIE_deposit_insurance }', b)
    return b
content = update_focus(content, 'VIE_gold_monopoly_2012', fix_gold_monopoly_2012)

def fix_gold_free_market(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_state_bank_modernization')
    b = replace_focus_prop(b, 'x', '4')
    b = replace_focus_prop(b, 'y', '3')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_state_bank_modernization\s*\}', 'prerequisite = { focus = VIE_deposit_insurance }', b)
    return b
content = update_focus(content, 'VIE_gold_free_market', fix_gold_free_market)

def fix_gold_monopoly_lifted(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_gold_monopoly_2012')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_gold_monopoly_lifted', fix_gold_monopoly_lifted)

# VAMC restructuring:
def fix_cross_ownership(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_vamc')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_cross_ownership_crackdown', fix_cross_ownership)

def fix_zero_dong(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_vamc')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_zero_dong_acquisition', fix_zero_dong)

def fix_bank_bankruptcy(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_vamc')
    b = replace_focus_prop(b, 'x', '4')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_bank_bankruptcy', fix_bank_bankruptcy)

def fix_compulsory_transfer(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_zero_dong_acquisition')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_compulsory_transfer_2024', fix_compulsory_transfer)

# Shift Agriculture to X=62, 64 to avoid touching
def fix_new_rural(b):
    b = replace_focus_prop(b, 'x', '28')
    return b
content = update_focus(content, 'VIE_new_rural_development', fix_new_rural)

def fix_high_tech_ag(b):
    b = replace_focus_prop(b, 'x', '28')
    return b
content = update_focus(content, 'VIE_high_tech_agriculture', fix_high_tech_ag)

# ==========================================
# 4. INFRASTRUCTURE & TRANSPORT
# ==========================================
def fix_dual_use(b):
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_airport_master_plan\s*\}', 'prerequisite = { focus = VIE_tan_son_nhat_t3 }', b)
    return b
content = update_focus(content, 'VIE_dual_use_airports', fix_dual_use)

def fix_expressway_3000(b):
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_north_south_expressway_phase2\s+focus\s*=\s*VIE_expressway_regional_links\s*\}', 'prerequisite = { focus = VIE_north_south_expressway_phase2 }', b)
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_expressway_regional_links\s*\}\n', '', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_expressway_regional_links' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_expressway_regional_links', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_expressway_regional_links\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_expressway_3000km', fix_expressway_3000)

def fix_expressway_5000(b):
    b = replace_focus_prop(b, 'y', '8')
    return b
content = update_focus(content, 'VIE_expressway_5000km_2030', fix_expressway_5000)

def fix_sync_infra(b):
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_long_thanh_airport\s*\}', 'prerequisite = { focus = VIE_airport_network_2030 }', b)
    return b
content = update_focus(content, 'VIE_synchronized_infrastructure_2030', fix_sync_infra)

# ==========================================
# 5. ENERGY & MINING
# ==========================================
def fix_vinacomin(b):
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_doi_moi_continues\s*\}\n', '', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_doi_moi_continues' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_doi_moi_continues', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_doi_moi_continues\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_vinacomin_founding', fix_vinacomin)

def fix_than_quang_ninh(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_vinacomin_founding')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_than_quang_ninh', fix_than_quang_ninh)

def fix_thach_khe(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_than_quang_ninh')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_vinacomin_founding\s*\}', 'prerequisite = { focus = VIE_than_quang_ninh }', b)
    return b
content = update_focus(content, 'VIE_thach_khe_mine_start', fix_thach_khe)

def fix_nui_phao(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_vinacomin_founding')
    b = replace_focus_prop(b, 'x', '4')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_nui_phao_tungsten', fix_nui_phao)

def fix_petrovietnam(b):
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_doi_moi_continues\s*\}\n', '', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_doi_moi_continues' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_doi_moi_continues', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_doi_moi_continues\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_petrovietnam_expansion', fix_petrovietnam)

def fix_petrolimex_downstream(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrovietnam_expansion')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_petrolimex_downstream_network', fix_petrolimex_downstream)

def fix_petrolimex_eneos(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrolimex_downstream_network')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_petrolimex_eneos_partnership', fix_petrolimex_eneos)

def fix_strategic_petroleum(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrolimex_downstream_network')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '2')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_petrolimex_downstream_network\s*\}', 'prerequisite = { focus = VIE_petrolimex_eneos_partnership }', b)
    return b
content = update_focus(content, 'VIE_strategic_petroleum_reserve', fix_strategic_petroleum)

def fix_petrolimex_green(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_strategic_petroleum_reserve')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_petrolimex_green_ev_hubs', fix_petrolimex_green)

def fix_dung_quat(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrovietnam_expansion')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_dung_quat_refinery', fix_dung_quat)

def fix_nghi_son(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_dung_quat_refinery')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_nghi_son_refinery', fix_nghi_son)

def fix_son_la(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrovietnam_expansion')
    b = replace_focus_prop(b, 'x', '4')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_son_la_dam', fix_son_la)

def fix_500kv(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_son_la_dam')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_500kv_grid', fix_500kv)

def fix_dppa(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_son_la_dam')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '2')
    return b
content = update_focus(content, 'VIE_dppa_market_reform', fix_dppa)

def fix_coal(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_son_la_dam')
    b = replace_focus_prop(b, 'x', '4')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_coal_power', fix_coal)

def fix_solar_boom(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_coal_power')
    b = replace_focus_prop(b, 'x', '-2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_solar_boom', fix_solar_boom)

def fix_solar_auction(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_coal_power')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_solar_auction', fix_solar_auction)

def fix_power_plan_8(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_solar_auction')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_power_plan_8', fix_power_plan_8)

def fix_jetp(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_power_plan_8')
    b = replace_focus_prop(b, 'x', '-2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_jetp_partnership', fix_jetp)

def fix_net_zero(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrovietnam_expansion')
    b = replace_focus_prop(b, 'x', '6')
    b = replace_focus_prop(b, 'y', '6')
    return b
content = update_focus(content, 'VIE_net_zero_2050', fix_net_zero)

def fix_offshore_wind(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_power_plan_8')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_offshore_wind', fix_offshore_wind)

def fix_energy_security(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_offshore_wind')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_energy_security_2045', fix_energy_security)

def fix_ninh_thuan(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_petrovietnam_expansion')
    b = replace_focus_prop(b, 'x', '12')
    b = replace_focus_prop(b, 'y', '3')
    return b
content = update_focus(content, 'VIE_ninh_thuan_nuclear', fix_ninh_thuan)

def fix_build_nuclear(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_ninh_thuan_nuclear')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_build_nuclear_plant', fix_build_nuclear)

def fix_shelve_nuclear(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_ninh_thuan_nuclear')
    b = replace_focus_prop(b, 'x', '-2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_shelve_nuclear', fix_shelve_nuclear)

def fix_revive_nuclear(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_shelve_nuclear')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_revive_nuclear', fix_revive_nuclear)

# ==========================================
# 6. INDUSTRY & MANUFACTURING
# ==========================================
def fix_auto(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_formosa_steel_complex')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_supporting_industries\s*\}', 'prerequisite = { focus = VIE_formosa_steel_complex }', b)
    return b
content = update_focus(content, 'VIE_domestic_automotive', fix_auto)

def fix_auto_park(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_domestic_automotive')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_integrated_auto_supplier_park', fix_auto_park)

def fix_ev_batteries(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_integrated_auto_supplier_park')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_ev_revolution_batteries', fix_ev_batteries)

def fix_global_auto(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_ev_revolution_batteries')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_global_auto_export', fix_global_auto)

def fix_tier1_vendor(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_hoa_phat_dung_quat_2')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_supporting_industries\s*\}', 'prerequisite = { focus = VIE_hoa_phat_dung_quat_2 }', b)
    return b
content = update_focus(content, 'VIE_tier1_vendor_localization', fix_tier1_vendor)

def fix_fdi_fast_track(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_tier1_vendor_localization')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_china_plus_one\s*\}', 'prerequisite = { focus = VIE_tier1_vendor_localization }', b)
    return b
content = update_focus(content, 'VIE_fdi_fast_track', fix_fdi_fast_track)

def fix_precision_mechanics(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_supporting_industries')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_precision_mechanics_molds', fix_precision_mechanics)

def fix_fdi_screening(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_precision_mechanics_molds')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_china_plus_one\s*\}', 'prerequisite = { focus = VIE_precision_mechanics_molds }', b)
    return b
content = update_focus(content, 'VIE_fdi_technology_screening', fix_fdi_screening)

def fix_apple_supply(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_fdi_technology_screening')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_manufacturing_hub\s*\}', 'prerequisite = { focus = VIE_fdi_technology_screening }', b)
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_fdi_fast_track\s+focus\s*=\s*VIE_fdi_technology_screening\s*\}\n', '', b)
    return b
content = update_focus(content, 'VIE_apple_supply_chain', fix_apple_supply)

def fix_modern_ind_nation(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_apple_supply_chain')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_industrial_productivity_program\s*\}', 'prerequisite = { focus = VIE_apple_supply_chain }', b)
    return b
content = update_focus(content, 'VIE_modern_industrial_nation_2030', fix_modern_ind_nation)

def fix_china_plus(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_samsung_partnership')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_supporting_industries\s*\}', 'prerequisite = { focus = VIE_samsung_partnership }', b)
    return b
content = update_focus(content, 'VIE_china_plus_one', fix_china_plus)

def fix_mfg_hub(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_china_plus_one')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_supporting_industries\s*\}\n', '', b)
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_samsung_partnership\s+focus\s*=\s*VIE_china_plus_one\s*\}', 'prerequisite = { focus = VIE_china_plus_one }', b)
    return b
content = update_focus(content, 'VIE_manufacturing_hub', fix_mfg_hub)

def fix_chip_packaging(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_semiconductor_ambition')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_chip_design_packaging_priority', fix_chip_packaging)

def fix_chip_pilot(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_semiconductor_ambition')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_chip_pilot_fab_priority', fix_chip_pilot)

def fix_chip_design(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_chip_design_packaging_priority')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_chip_design', fix_chip_design)

def fix_osat(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_chip_pilot_fab_priority')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_osat_packaging', fix_osat)

def fix_chip_engineers(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_chip_pilot_fab_priority')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_chip_engineers', fix_chip_engineers)

def fix_semi_fab(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_osat_packaging')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_semiconductor_fab', fix_semi_fab)

def fix_eco_industrial(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_nq23_industrial_policy')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_eco_industrial_parks', fix_eco_industrial)

def fix_ind_productivity(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_nq29_industrialization_2045')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_industrial_productivity_program', fix_ind_productivity)

def fix_inv_support_fund(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_eco_industrial_parks')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    return b
content = update_focus(content, 'VIE_investment_support_fund', fix_inv_support_fund)

# ==========================================
# 7. SCIENCE & DIGITAL
# ==========================================
def fix_nuclear(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_research_universities')
    b = replace_focus_prop(b, 'x', '0')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_nafosted\s*\}', 'prerequisite = { focus = VIE_research_universities }', b)
    return b
content = update_focus(content, 'VIE_nuclear_research', fix_nuclear)

def fix_sci_breakthrough(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_nuclear_research')
    b = replace_focus_prop(b, 'x', '2')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_research_universities\s*\}', 'prerequisite = { focus = VIE_nuclear_research }', b)
    return b
content = update_focus(content, 'VIE_science_breakthrough', fix_sci_breakthrough)

def fix_developed_nation(b):
    b = re.sub(r'(?m)^\t+prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_ageing_society\s*\}\n', '', b)
    avail_pattern = r'(?m)^(\t+available\s*=\s*\{)'
    if re.search(avail_pattern, b):
        if 'VIE_ageing_society' not in b:
            b = re.sub(avail_pattern, r'\g<1>\n\t\t\thas_completed_focus = VIE_ageing_society', b)
    else:
        b = re.sub(r'(?m)^(\t+search_filters\s*=\s*\{)', r'\tavailable = {\n\t\t\thas_completed_focus = VIE_ageing_society\n\t\t}\n\n\g<1>', b)
    return b
content = update_focus(content, 'VIE_developed_nation_2045', fix_developed_nation)

# ==========================================
# 8. LAND FORCES (V30.2 layout alignment)
# ==========================================
spec = json.loads((ROOT / '.claude/docs/land/structure_v30_2.json').read_text(encoding='utf-8'))
land_positions = spec['positions']

def fix_cap_ad(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_lf_command_reform_2')
    b = replace_focus_prop(b, 'x', '-6')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_lf_army_reform\s*\}', 'prerequisite = { focus = VIE_lf_command_reform_2 }', b)
    return b
content = update_focus(content, 'VIE_lf_cap_army_ad', fix_cap_ad)

def fix_cap_border(b):
    b = replace_focus_prop(b, 'relative_position_id', 'VIE_lf_command_reform_2')
    b = replace_focus_prop(b, 'x', '6')
    b = replace_focus_prop(b, 'y', '1')
    b = re.sub(r'prerequisite\s*=\s*\{\s*focus\s*=\s*VIE_lf_army_reform\s*\}', 'prerequisite = { focus = VIE_lf_command_reform_2 }', b)
    return b
content = update_focus(content, 'VIE_lf_cap_border_urban', fix_cap_border)

def parse_focus_spans(text):
    F = {}; order = []; spans = {}
    for m in re.finditer(r'\n\tfocus = \{', text):
        st = m.end(); d = 1; i = st
        while d:
            d += {'{': 1, '}': -1}.get(text[i], 0); i += 1
        b = text[st:i - 1]
        fid = re.search(r'\bid = (\w+)', b).group(1)
        x = int(re.search(r'\n\t\tx = (-?\d+)', b).group(1))
        y = int(re.search(r'\n\t\ty = (-?\d+)', b).group(1))
        r = re.search(r'relative_position_id = (\w+)', b)
        F[fid] = dict(x=x, y=y, rel=r.group(1) if r else None)
        order.append(fid); spans[fid] = (m.start() + 1, i)
    return F, order, spans

F, order, spans = parse_focus_spans(content)

for fid, target_xy in land_positions.items():
    if fid in F:
        d = F[fid]
        anchor = d['rel']
        if anchor:
            anchor_target = land_positions.get(anchor)
            if not anchor_target:
                memo = {}
                def ab(f):
                    if f in memo: return memo[f]
                    df = F[f]; x, y = df['x'], df['y']
                    if df['rel']:
                        px, py = ab(df['rel']); x += px; y += py
                    memo[f] = (x, y); return memo[f]
                anchor_target = ab(anchor)
            dx = target_xy[0] - anchor_target[0]
            dy = target_xy[1] - anchor_target[1]
            def make_mut(dx, dy):
                def mut(b):
                    b = replace_focus_prop(b, 'x', str(dx))
                    b = replace_focus_prop(b, 'y', str(dy))
                    return b
                return mut
            content = update_focus(content, fid, make_mut(dx, dy))
        else:
            def make_mut(tx, ty):
                def mut(b):
                    b = replace_focus_prop(b, 'x', str(tx))
                    b = replace_focus_prop(b, 'y', str(ty))
                    return b
                return mut
            content = update_focus(content, fid, make_mut(target_xy[0], target_xy[1]))

FOCUS_FILE.write_text(content, encoding='utf-8')
print("Successfully applied full layout fixes and land v30.2 to VIE_md_focus.txt!")
