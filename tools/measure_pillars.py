import re
from pathlib import Path
from collections import defaultdict

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focuses = []
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
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
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    focuses.append({
        "id": fid, "x": int(xm.group(1)) if xm else 0, "y": int(ym.group(1)) if ym else 0,
        "rel": rel.group(1) if rel else None
    })

fmap = {f["id"]: f for f in focuses}

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = fmap.get(fid)
    if not f or not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], visited)
    return rx + f["x"], ry + f["y"]

for f in focuses:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

rel_children = defaultdict(list)
for f in focuses:
    if f["rel"]:
        rel_children[f["rel"]].append(f["id"])

# Let's inspect subtrees:
subtrees = {
    "Pillar 1: Trade & Enterprise (enterprise_law)": ["VIE_enterprise_law", "VIE_sez_three_zones", "VIE_sez_postpone", "VIE_sez_pass_99", "VIE_island_special_zones", "VIE_sez_strategic_investors", "VIE_bilateral_trade_agreement_usa", "VIE_fdi_attraction", "VIE_wto_negotiations", "VIE_wto_reforms", "VIE_export_powerhouse", "VIE_cptpp_member", "VIE_evfta", "VIE_equitization_soes", "VIE_investment_law_2005"],
    "Pillar 2: Agriculture (anchored to enterprise_law)": ["VIE_rice_export_power", "VIE_new_rural_development", "VIE_high_tech_agriculture", "VIE_land_law_reform", "VIE_mekong_climate_adaptation"],
    "Pillar 3: Banking & SOEs (state_bank_modernization)": ["VIE_state_bank_modernization", "VIE_fight_inflation", "VIE_restructure_banking", "VIE_state_conglomerates", "VIE_deposit_insurance", "VIE_vamc", "VIE_scic", "VIE_cross_ownership_crackdown", "VIE_corporate_bond_reform", "VIE_market_upgrade_criteria", "VIE_international_financial_centre", "VIE_investment_grade", "VIE_zero_dong_acquisition", "VIE_bank_bankruptcy", "VIE_compulsory_transfer_2024", "VIE_soe_gradual_restructuring", "VIE_soe_rapid_divestment", "VIE_soe_governance", "VIE_hose_exchange", "VIE_cashless_payments", "VIE_household_business", "VIE_private_champions", "VIE_private_sector_engine", "VIE_gold_monopoly_2012", "VIE_gold_free_market", "VIE_gold_monopoly_lifted"],
    "Pillar 4: Infrastructure (infrastructure_development)": [f["id"] for f in focuses if f["rel"] == "VIE_infrastructure_development" or f["id"] == "VIE_infrastructure_development"],
    "Pillar 5: Mining (vinacomin_founding)": ["VIE_vinacomin_founding", "VIE_bauxite_tay_nguyen", "VIE_bauxite_suspend", "VIE_rare_earths", "VIE_than_quang_ninh", "VIE_nui_phao_tungsten", "VIE_thach_khe_mine_start"],
    "Pillar 6: Energy Sector": ["VIE_strategic_petroleum_reserve", "VIE_son_la_dam", "VIE_petrolimex_green_ev_hubs", "VIE_petrolimex_eneos_partnership", "VIE_petrovietnam_expansion", "VIE_shelve_nuclear", "VIE_revive_nuclear", "VIE_petrolimex_downstream_network", "VIE_500kv_grid", "VIE_dppa_market_reform", "VIE_dung_quat_refinery", "VIE_build_nuclear_plant", "VIE_net_zero_2050", "VIE_coal_power", "VIE_jetp_partnership", "VIE_solar_boom", "VIE_nghi_son_refinery", "VIE_solar_auction", "VIE_power_plan_8", "VIE_ninh_thuan_nuclear", "VIE_offshore_wind", "VIE_energy_security_2045"],
    "Pillar 7: Industrialization & Automotive": [f["id"] for f in focuses if f["rel"] == "VIE_industrialization_strategy" or f["id"] == "VIE_industrialization_strategy" or f["id"] in ["VIE_supporting_industries", "VIE_china_plus_one", "VIE_domestic_automotive", "VIE_integrated_auto_supplier_park", "VIE_ev_revolution_batteries", "VIE_global_auto_export", "VIE_hoa_phat_hrc_steel", "VIE_precision_mechanics_molds", "VIE_tier1_vendor_localization", "VIE_manufacturing_hub"]],
    "Pillar 8: Internet, Tech & Science": [f["id"] for f in focuses if f["rel"] == "VIE_internet_expansion" or f["id"] == "VIE_internet_expansion" or f["id"] in ["VIE_research_universities", "VIE_nuclear_research", "VIE_nafosted", "VIE_science_breakthrough", "VIE_vinasat", "VIE_earth_observation"]],
    "Pillar 9: Upper Middle Income 2045": [f["id"] for f in focuses if f["rel"] == "VIE_upper_middle_income" or f["id"] == "VIE_upper_middle_income"]
}

for name, fids in subtrees.items():
    xs = [fmap[f]["abs_x"] for f in fids if f in fmap]
    ys = [fmap[f]["abs_y"] for f in fids if f in fmap]
    if xs:
        print(f"{name:50s} : {len(fids):2d} focuses | abs_x: [{min(xs):3d}, {max(xs):3d}] (w={max(xs)-min(xs):2d}) | abs_y: [{min(ys):2d}, {max(ys):2d}]")
