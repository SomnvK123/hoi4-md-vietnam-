import glob
import re
import sys
import os

if sys.stdout:
    sys.stdout.reconfigure(encoding="utf-8")

os.makedirs("scratch", exist_ok=True)
txt = open("common/national_focus/VIE_md_focus.txt", encoding="utf-8").read()

fids = [
    "VIE_asean_integration", "VIE_border_settlement", "VIE_asean_chair",
    "VIE_un_security_council", "VIE_us_comprehensive_partnership",
    "VIE_us_embargo_lifted", "VIE_csp_network", "VIE_bamboo_diplomacy",
    "VIE_special_relations_laos", "VIE_cambodia_relations", "VIE_indochina_solidarity",
    "VIE_indochina_federation", "VIE_16_words", "VIE_border_trade_gates",
    "VIE_defence_hotline", "VIE_code_of_conduct", "VIE_shared_future",
    "VIE_gulf_of_tonkin", "VIE_apec_host", "VIE_us_carrier_visit",
    "VIE_us_tariff_deal", "VIE_cambodia_border", "VIE_mekong_commission",
    "VIE_mekong_dams_response", "VIE_funan_techo_response", "VIE_india_partnership",
    "VIE_japan_partnership", "VIE_korea_partnership", "VIE_australia_partnership",
    "VIE_france_eu", "VIE_gulf_investment", "VIE_global_south_ties",
    "VIE_us_engagement", "VIE_multilateral_champion"
]

loc = {}
for yml in glob.glob("localisation/**/*.yml", recursive=True):
    try:
        content = open(yml, encoding="utf-8").read()
    except Exception:
        continue
    for m in re.finditer(r'^\s*([A-Za-z0-9_]+):\d*\s*"([^"\n]*)"', content, re.MULTILINE):
        loc[m.group(1)] = m.group(2)

with open("scratch/dip_details.txt", "w", encoding="utf-8") as out:
    for fid in fids:
        title = loc.get(fid, "???")
        desc = loc.get(fid + "_desc", "")
        m = re.search(rf'id\s*=\s*{fid}\b.*?(?=\n\tfocus\s*=\s*|\Z)', txt, re.DOTALL)
        icon = "NOT FOUND"
        prereqs = []
        if m:
            ic_m = re.search(r'icon\s*=\s*(\S+)', m.group(0))
            if ic_m:
                icon = ic_m.group(1)
            prereqs = re.findall(r'focus\s*=\s*(\w+)', m.group(0))
        out.write(f"ID: {fid}\nTitle: {title}\nIcon: {icon}\nPrereqs: {prereqs}\nDesc: {desc}\n\n")

print(f"Exported {len(fids)} focuses to scratch/dip_details.txt")
