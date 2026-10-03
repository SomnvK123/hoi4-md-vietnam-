import re
from pathlib import Path
from collections import defaultdict

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")

focus_matches = []
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
    x = int(re.search(r"\bx\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\bx\s*=\s*(-?\d+)", block) else 0
    y = int(re.search(r"\by\s*=\s*(-?\d+)", block).group(1)) if re.search(r"\by\s*=\s*(-?\d+)", block) else 0
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    rel = rel.group(1) if rel else None
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    filters = re.findall(r"\bsearch_filters\s*=\s*\{([^}]+)\}", block)
    filters = filters[0].split() if filters else []
    
    # Check lines right before start for section comment
    pre_txt = txt[max(0, start-500):start]
    comms = [l.strip() for l in pre_txt.splitlines() if l.strip().startswith("#")]
    last_comm = comms[-1] if comms else ""
    
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereqs": prereqs, "filters": filters,
        "last_comm": last_comm, "start": start, "end": end, "block": block
    })

fmap = {f["id"]: f for f in focus_matches}

def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return 0, 0
    visited.add(fid)
    f = fmap.get(fid)
    if not f: return 0, 0
    if not f["rel"]: return f["x"], f["y"]
    rx, ry = get_abs(f["rel"], visited)
    return rx + f["x"], ry + f["y"]

for f in focus_matches:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

print(f"Total focuses: {len(focus_matches)}")

# Let's inspect the exact list of:
# 1. BIEN DONG
# 2. DOI NGOAI
# 3. AN NINH NOI DIA
# 4. CHINH TRI
# 5. QUAN SU
# 6. KINH TE

def categorize(f):
    fid = f["id"]
    if any(k in fid for k in ["_lf_", "_nf_", "_airf_", "_apm_", "modernize_vpa"]):
        return "QUAN_SU"
    if fid.startswith("VIE_sec_"):
        return "AN_NINH"
    if any(k in fid for k in ["law_of_the_sea", "maritime_militia", "fisheries_surveillance", "dk1_platforms", 
                              "legal_warfare", "spratly_fortification", "coast_guard_law", "assert_maritime_rights", 
                              "paracel_ultimatum", "limited_war_doctrine", "peoples_defence", "scs_"]):
        return "BIEN_DONG"
    # Check foreign policy / diplomacy
    if any(k in fid for k in ["asean_", "shared_future", "four_nos", "laos", "cambodia", "us_", "china_plus", 
                              "russia_", "france_", "india_", "japan_", "un_peacekeeping", "multilateral_", "code_of_conduct",
                              "16_words", "border_settlement", "border_trade_gates", "defence_hotline",
                              "gulf_of_tonkin", "apec_host", "un_security_council", "csp_network",
                              "indochina_", "mekong_", "funan_techo", "korea_partnership", "australia_partnership",
                              "global_south_ties"]):
        return "DOI_NGOAI"
    # Check politics
    if any(k in fid for k in ["congress_", "constitution_", "anti_corruption", "asset_", "state_audit", "party_", 
                              "clean_cadres", "public_admin", "decentralization", "institutional_", "peoples_oversight", 
                              "cadre_", "digital_anticorruption", "national_assembly", "ethnic_policy", "concentration_of_power",
                              "cybersecurity_law", "e_government", "resolution_57", "grassroots_democracy",
                              "mass_mobilization", "rule_of_law_state", "streamline_apparatus", "era_of_rising",
                              "platform_2011", "tw4_party_building"]):
        return "CHINH_TRI"
    return "KINH_TE"

categories = defaultdict(list)
for f in focus_matches:
    c = categorize(f)
    categories[c].append(f)

for cat, flist in sorted(categories.items()):
    xs = [f["abs_x"] for f in flist]
    ys = [f["abs_y"] for f in flist]
    print(f"\n=== {cat} ({len(flist)} focuses) ===")
    print(f"  abs_x: [{min(xs)}, {max(xs)}], abs_y: [{min(ys)}, {max(ys)}]")
    print(f"  Sample IDs: {[f['id'] for f in flist[:8]]}")
