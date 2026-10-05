import sys, os
sys.path.insert(0, os.path.abspath("."))
import re
import tools.analyze_diplomacy as ad

# Proposed layout mapping: fid -> { 'rel': parent_fid, 'dx': int, 'dy': int, 'prereqs': [...], 'avail': [...] }
# Note: dx, dy are relative to parent_fid
# VIE_asean_integration is at (48, 11), neo VIE_doi_moi_continues (80, 0): dx = -32, dy = 11

diplomacy_layout = {
    # ROOT (y = 11)
    "VIE_asean_integration": {
        "rel": "VIE_doi_moi_continues", "dx": -32, "dy": 11, # abs (48, 11)
        "prereqs": [], "avail": []
    },

    # =========================================================
    # TRUC 1: QUAN HE VIET - TRUNG & BIEN GIOI TREN BO (6 focus)
    # Zone: x = 34 .. 38
    # =========================================================
    # y = 12
    "VIE_gulf_of_tonkin": {
        "rel": "VIE_asean_integration", "dx": -12, "dy": 1, # abs (36, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    # y = 13
    "VIE_border_settlement": {
        "rel": "VIE_gulf_of_tonkin", "dx": 0, "dy": 1, # abs (36, 13)
        "prereqs": ["VIE_gulf_of_tonkin"], "avail": []
    },
    # y = 14
    "VIE_16_words": {
        "rel": "VIE_border_settlement", "dx": 0, "dy": 1, # abs (36, 14)
        "prereqs": ["VIE_border_settlement"], "avail": []
    },
    # y = 15
    "VIE_border_trade_gates": {
        "rel": "VIE_16_words", "dx": -2, "dy": 1, # abs (34, 15)
        "prereqs": ["VIE_16_words"], "avail": []
    },
    "VIE_defence_hotline": {
        "rel": "VIE_16_words", "dx": 2, "dy": 1, # abs (38, 15)
        "prereqs": ["VIE_16_words"], "avail": []
    },
    # y = 16
    "VIE_shared_future": {
        "rel": "VIE_16_words", "dx": 0, "dy": 2, # abs (36, 16)
        "prereqs": ["VIE_16_words"], "avail": ["VIE_border_trade_gates", "VIE_defence_hotline"]
    },

    # =========================================================
    # TRUC 2: LAO, CAMPUCHIA & AN NINH NGUON NUOC ME KONG (7 focus)
    # Zone: x = 40 .. 44
    # =========================================================
    # y = 12
    "VIE_special_relations_laos": {
        "rel": "VIE_asean_integration", "dx": -8, "dy": 1, # abs (40, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    "VIE_cambodia_relations": {
        "rel": "VIE_asean_integration", "dx": -4, "dy": 1, # abs (44, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    # y = 13
    "VIE_mekong_commission": {
        "rel": "VIE_special_relations_laos", "dx": 0, "dy": 1, # abs (40, 13)
        "prereqs": ["VIE_special_relations_laos"], "avail": []
    },
    "VIE_cambodia_border": {
        "rel": "VIE_cambodia_relations", "dx": 0, "dy": 1, # abs (44, 13)
        "prereqs": ["VIE_cambodia_relations"], "avail": []
    },
    # y = 14
    "VIE_mekong_dams_response": {
        "rel": "VIE_mekong_commission", "dx": 0, "dy": 1, # abs (40, 14)
        "prereqs": ["VIE_mekong_commission"], "avail": []
    },
    "VIE_funan_techo_response": {
        "rel": "VIE_cambodia_border", "dx": 0, "dy": 1, # abs (44, 14)
        "prereqs": ["VIE_cambodia_border"], "avail": []
    },
    # y = 15
    "VIE_indochina_solidarity": {
        "rel": "VIE_special_relations_laos", "dx": 2, "dy": 3, # abs (42, 15)
        "prereqs": ["VIE_special_relations_laos"], "avail": ["VIE_cambodia_relations"]
    },

    # =========================================================
    # TRUC 3: TRONG TAM ASEAN & DA PHUONG HOA (APEC, LHQ) (5 focus)
    # Zone: x = 46 .. 50
    # =========================================================
    # y = 12
    "VIE_asean_chair": {
        "rel": "VIE_asean_integration", "dx": 0, "dy": 1, # abs (48, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    # y = 13
    "VIE_code_of_conduct": {
        "rel": "VIE_asean_chair", "dx": -2, "dy": 1, # abs (46, 13)
        "prereqs": ["VIE_asean_chair"], "avail": []
    },
    "VIE_apec_host": {
        "rel": "VIE_asean_chair", "dx": 2, "dy": 1, # abs (50, 13)
        "prereqs": ["VIE_asean_chair"], "avail": []
    },
    # y = 14
    "VIE_un_security_council": {
        "rel": "VIE_asean_chair", "dx": 0, "dy": 2, # abs (48, 14)
        "prereqs": ["VIE_asean_chair"], "avail": ["VIE_apec_host"]
    },
    # y = 15
    "VIE_multilateral_champion": {
        "rel": "VIE_un_security_council", "dx": 0, "dy": 1, # abs (48, 15)
        "prereqs": ["VIE_un_security_council"], "avail": []
    },

    # =========================================================
    # TRUC 4: QUAN HE VIET - MY (5 focus)
    # Zone: x = 52 .. 54
    # =========================================================
    # y = 12
    "VIE_us_engagement": {
        "rel": "VIE_asean_integration", "dx": 4, "dy": 1, # abs (52, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    # y = 13
    "VIE_us_comprehensive_partnership": {
        "rel": "VIE_us_engagement", "dx": 0, "dy": 1, # abs (52, 13)
        "prereqs": ["VIE_us_engagement"], "avail": []
    },
    # y = 14
    "VIE_us_embargo_lifted": {
        "rel": "VIE_us_comprehensive_partnership", "dx": 0, "dy": 1, # abs (52, 14)
        "prereqs": ["VIE_us_comprehensive_partnership"], "avail": []
    },
    # y = 15
    "VIE_us_carrier_visit": {
        "rel": "VIE_us_embargo_lifted", "dx": 0, "dy": 1, # abs (52, 15)
        "prereqs": ["VIE_us_embargo_lifted"], "avail": []
    },
    "VIE_us_tariff_deal": {
        "rel": "VIE_us_embargo_lifted", "dx": 2, "dy": 1, # abs (54, 15)
        "prereqs": ["VIE_us_embargo_lifted"], "avail": []
    },

    # =========================================================
    # TRUC 5: DOI TAC CHIEN LUOC & NGOAI GIAO CAY TRE (9 focus)
    # Zone: x = 56 .. 62
    # =========================================================
    # y = 12
    "VIE_japan_partnership": {
        "rel": "VIE_asean_integration", "dx": 10, "dy": 1, # abs (58, 12)
        "prereqs": ["VIE_asean_integration"], "avail": []
    },
    # y = 13
    "VIE_korea_partnership": {
        "rel": "VIE_japan_partnership", "dx": -2, "dy": 1, # abs (56, 13)
        "prereqs": ["VIE_japan_partnership"], "avail": []
    },
    "VIE_india_partnership": {
        "rel": "VIE_japan_partnership", "dx": 0, "dy": 1, # abs (58, 13)
        "prereqs": ["VIE_japan_partnership"], "avail": []
    },
    "VIE_australia_partnership": {
        "rel": "VIE_japan_partnership", "dx": 2, "dy": 1, # abs (60, 13)
        "prereqs": ["VIE_japan_partnership"], "avail": []
    },
    "VIE_france_eu": {
        "rel": "VIE_japan_partnership", "dx": 4, "dy": 1, # abs (62, 13)
        "prereqs": ["VIE_japan_partnership"], "avail": []
    },
    # y = 14
    "VIE_gulf_investment": {
        "rel": "VIE_korea_partnership", "dx": 0, "dy": 1, # abs (56, 14)
        "prereqs": ["VIE_korea_partnership"], "avail": []
    },
    "VIE_csp_network": {
        "rel": "VIE_india_partnership", "dx": 0, "dy": 1, # abs (58, 14)
        "prereqs": ["VIE_india_partnership"], "avail": ["VIE_korea_partnership"]
    },
    "VIE_global_south_ties": {
        "rel": "VIE_australia_partnership", "dx": 0, "dy": 1, # abs (60, 14)
        "prereqs": ["VIE_australia_partnership"], "avail": []
    },
    # y = 15
    "VIE_bamboo_diplomacy": {
        "rel": "VIE_csp_network", "dx": 0, "dy": 1, # abs (58, 15)
        "prereqs": ["VIE_csp_network"], "avail": []
    }
}

print(f"Total mapped diplomacy focuses: {len(diplomacy_layout)} (expected 33)")
missing = [fid for fid in ad.subtree if fid not in diplomacy_layout]
print(f"Missing from layout: {missing}")

# Calculate absolute coordinates
abs_coords = {}
def get_abs_pos(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    entry = diplomacy_layout[fid]
    parent = entry["rel"]
    if parent == "VIE_doi_moi_continues":
        return (80 + entry["dx"], 0 + entry["dy"])
    px, py = get_abs_pos(parent, visited)
    return (px + entry["dx"], py + entry["dy"])

for fid in diplomacy_layout:
    abs_coords[fid] = get_abs_pos(fid)

# Check collisions within diplomacy
coord_map = {}
collisions = []
for fid, (ax, ay) in abs_coords.items():
    if (ax, ay) in coord_map:
        collisions.append((fid, coord_map[(ax, ay)], (ax, ay)))
    else:
        coord_map[(ax, ay)] = fid

print(f"Collisions within diplomacy: {len(collisions)}")
for c in collisions:
    print("  Collision:", c)

# Check collisions with external focuses in the mod
ext_collisions = []
for fid, (ax, ay) in abs_coords.items():
    for ext_fid, ext_f in ad.focuses.items():
        if ext_fid not in diplomacy_layout:
            if (ext_f['abs_x'], ext_f['abs_y']) == (ax, ay):
                ext_collisions.append((fid, ext_fid, (ax, ay)))

print(f"Collisions with external focuses: {len(ext_collisions)}")
for c in ext_collisions:
    print("  Collision:", c)

# Check gap violations
rows = {}
for fid, (ax, ay) in abs_coords.items():
    rows.setdefault(ay, []).append((ax, fid))

gap_violations = []
for y in sorted(rows.keys()):
    items = sorted(rows[y], key=lambda x: x[0])
    row_str = ", ".join([f"{fid}(x={ax})" for ax, fid in items])
    print(f"Row y={y:2} ({len(items):2} focuses): {row_str}")
    for k in range(len(items) - 1):
        dx = items[k+1][0] - items[k][0]
        if dx < 2:
            gap_violations.append((items[k][1], items[k+1][1], y, dx))

print(f"Gap violations (dx < 2): {len(gap_violations)}")
for g in gap_violations:
    print("  Gap violation:", g)

# Check prerequisite y_child > y_parent
prereq_violations = []
for fid, entry in diplomacy_layout.items():
    ax, ay = abs_coords[fid]
    for p in entry["prereqs"]:
        if p in abs_coords:
            p_ax, p_ay = abs_coords[p]
            if ay <= p_ay:
                prereq_violations.append((fid, p, ay, p_ay))

print(f"Prerequisite y_child <= y_parent violations: {len(prereq_violations)}")
for pv in prereq_violations:
    print("  Prereq violation:", pv)
