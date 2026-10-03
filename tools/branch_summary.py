import re
from pathlib import Path
from collections import defaultdict

txt = Path(r"d:\HOI4Mods\md_vietnam\common\national_focus\VIE_md_focus.txt").read_text(encoding="utf-8")

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
    prereq = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    filters = re.findall(r"\bsearch_filters\s*=\s*\{([^}]+)\}", block)
    filters = filters[0].split() if filters else []
    
    focus_matches.append({
        "id": fid, "x": x, "y": y, "rel": rel, "prereq": prereq, "filters": filters,
        "block": block
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

def classify(f):
    fid = f["id"]
    if any(k in fid for k in ["_lf_", "_nf_", "_airf_", "_apm_", "modernize_vpa"]):
        return "QUAN_SU"
    if fid.startswith("VIE_sec_"):
        return "AN_NINH"
    if any(k in fid for k in ["law_of_the_sea", "maritime_militia", "fisheries_surveillance", "dk1_platforms", 
                              "legal_warfare", "spratly_fortification", "coast_guard_law", "assert_maritime_rights", 
                              "paracel_ultimatum", "limited_war_doctrine", "peoples_defence", "scs_"]):
        return "BIEN_DONG"
    if any(k in fid for k in ["asean_", "shared_future", "four_nos", "laos", "cambodia", "us_", "china_plus", 
                              "russia_", "france_", "india_", "japan_", "un_peacekeeping", "multilateral_", "code_of_conduct"]):
        return "DOI_NGOAI"
    if any(k in fid for k in ["congress_", "constitution_", "anti_corruption", "asset_", "state_audit", "party_", 
                              "clean_cadres", "public_admin", "decentralization", "institutional_", "peoples_oversight", 
                              "cadre_", "digital_anticorruption", "national_assembly", "ethnic_policy", "concentration_of_power",
                              "cybersecurity_law", "e_government", "resolution_57"]):
        return "CHINH_TRI"
    return "KINH_TE"

branches = defaultdict(list)
for f in focus_matches:
    b = classify(f)
    branches[b].append(f)

print("=== CROSS-BRANCH PREREQUISITES ===")
for bname, flist in sorted(branches.items()):
    for f in flist:
        for p in f["prereq"]:
            if p in fmap:
                pb = classify(fmap[p])
                if pb != bname:
                    print(f"  {bname:10s} {f['id']:35s} -> {pb:10s} {p}")
