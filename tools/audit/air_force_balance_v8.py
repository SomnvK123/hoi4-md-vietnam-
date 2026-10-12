"""Air force V8 balance check: actual modifiers for every mutually exclusive branch,
shared caps across all axes, code cross-check.

Pure stdlib, portable. Prints tables and PASS/FAIL lines; exit code 1 on any FAIL.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# Token mapping
TOKENS = {
    "exp": "experience_gain_air_factor",
    "agility": "air_agility_factor",
    "sup": "air_superiority_efficiency",
    "cas": "air_cas_efficiency",
    "mis": "air_mission_efficiency",
    "rng": "air_range_factor",
    "det": "air_detection",
    "home": "air_home_defence_factor",
    "int": "air_intercept_efficiency",
    "pers": "airforce_personnel_cost_multiplier_modifier",
    "ace": "air_ace_generation_chance_factor",
    "night": "air_night_penalty",
    "acc": "air_accidents_factor",
    "recon": "recon_factor",
    "naval_strike": "naval_strike_targetting_factor",
}
NAME2KEY = {v: k for k, v in TOKENS.items()}

# Caps across ALL axes (percent)
CAPS = {
    "exp": 10.0,
    "agility": 10.0,
    "sup": 10.0,
    "cas": 10.0,
    "mis": 16.0,
    "rng": 20.0,
    "det": 20.0,
    "home": 20.0,
    "int": 8.0,
    "pers": 6.0,
    "ace": 10.0,
    "night": 6.0,
    "recon": 20.0,
    "naval_strike": 15.0,
}

# Already used by other axes (percent): Truc 1 radar B +5% and Truc 2 +6% detection
OTHER_AXES = {
    "det": 5.0 + 6.0,
}

fails: list[str] = []

def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)

def parse_focus_rewards():
    fpath = os.path.join(ROOT, "common", "national_focus", "VIE_md_focus.txt")
    with open(fpath, encoding="utf-8") as f:
        content = f.read()

    focus_dict = {}
    pattern = r"focus\s*=\s*\{\s*id\s*=\s*(VIE_air8_\w+).*?completion_reward\s*=\s*\{(.*?)\n\t\}"
    for m in re.finditer(pattern, content, re.DOTALL):
        fid = m.group(1)
        reward_block = m.group(2)
        rewards = defaultdict(float)
        for var_m in re.finditer(r"add_to_variable\s*=\s*\{\s*VIE_af_(\w+)\s*=\s*([-\d.]+)", reward_block):
            var_name = var_m.group(1)
            val = float(var_m.group(2)) * 100.0
            if var_name in NAME2KEY:
                rewards[NAME2KEY[var_name]] += val
        focus_dict[fid] = dict(rewards)
    return focus_dict

def main():
    print("=" * 60)
    print("PK-KQ V8 BALANCE & CAPS AUDIT")
    print("=" * 60)

    # 1. Check variables in dynamic modifier
    print("\n== 1. Token trong VIE_armed_forces_modifier ==")
    dm_path = os.path.join(ROOT, "common", "dynamic_modifiers", "VIE_md_dynamic_modifiers.txt")
    with open(dm_path, encoding="utf-8") as f:
        dm_text = f.read()

    for k, name in TOKENS.items():
        check(re.search(r"\b%s = VIE_af_%s\b" % (name, name), dm_text) is not None, f"{name} = VIE_af_{name}")

    # 2. Parse Focus Rewards from code
    print("\n== 2. Doc Focus Rewards tu code ==")
    focus_rewards = parse_focus_rewards()
    print(f"Parsed {len(focus_rewards)} V8 Focuses from code.")
    check(len(focus_rewards) == 38, f"Parsed exactly 38 V8 focuses (got {len(focus_rewards)})")

    # Group focuses by branch
    foundation = [
        "VIE_air8_r00_foundation", "VIE_air8_p01_radar_network", "VIE_air8_p02_s300pmu1",
        "VIE_air8_p03_multitier_sam", "VIE_air8_f01_legacy_fleet", "VIE_air8_f02_su30mk2_procurement",
        "VIE_air8_f03_su30mk2_fleet_expansion", "VIE_air8_t01_academy_reform", "VIE_air8_t02_t6c_basic_trainer",
        "VIE_air8_t03_l39ng_jet_trainer", "VIE_air8_t04_yak130_advanced_trainer",
        "VIE_air8_r01_c2_guidance_reform", "VIE_air8_r02_air_orientation",
    ]
    doctrine_a = [
        "VIE_air8_a01_doctrine_defense_in_depth", "VIE_air8_a02_expanded_air_defense_alert",
        "VIE_air8_a03_interceptor_airspace_defense", "VIE_air8_a04_sam_radar_combat_crews",
        "VIE_air8_a05_dispersion_recovery_readiness", "VIE_air8_a06_multilayer_sky_shield",
    ]
    doctrine_b = [
        "VIE_air8_b01_doctrine_mobile_air_defense", "VIE_air8_b02_nextgen_multirole_program",
        "VIE_air8_b03_forward_basing_rapid_reaction", "VIE_air8_b04_maritime_night_strike_training",
        "VIE_air8_b05_mobile_interception_command", "VIE_air8_b06_agile_multirole_air_force",
    ]
    doctrine_c = [
        "VIE_air8_c01_doctrine_integrated_air_warfare", "VIE_air8_c02_unified_radar_data_network",
        "VIE_air8_c03_network_centric_fighters", "VIE_air8_c04_joint_simulated_exercises",
        "VIE_air8_c05_uav_fleet_recon_teaming", "VIE_air8_c06_networked_pkkq_battlespace",
    ]
    industry = [
        "VIE_air8_i00_selective_air_industry", "VIE_air8_i01_a32_su30mk2_overhaul",
        "VIE_air8_i02_domestic_avionics", "VIE_air8_i03_s125vt_upgrade_program",
        "VIE_air8_i04_viettel_vrs_3d_radar", "VIE_air8_i05_vq2_digital_c2",
        "VIE_air8_i06_viettel_tactical_uav",
    ]

    branches = {
        "Hoc thuyet A (Phong khong chieu sau)": foundation + doctrine_a + industry,
        "Hoc thuyet B (Phong thu co dong)": foundation + doctrine_b + industry,
        "Hoc thuyet C (Tac chien tich hop C4ISR)": foundation + doctrine_c + industry,
    }

    print("\n== 3. Kiem tra Tran Can Bang (Caps Audit) theo tung Nhanh ==")
    for bname, fids in branches.items():
        print(f"\n--- {bname} ---")
        totals = defaultdict(float)
        for fid in fids:
            for k, val in focus_rewards.get(fid, {}).items():
                totals[k] += val

        for k, cap in CAPS.items():
            tree_val = totals[k]
            # Convert night penalty to absolute reduction
            if k == "night":
                tree_val = abs(tree_val)
            other_val = OTHER_AXES.get(k, 0.0)
            combined = tree_val + other_val
            check(combined <= cap + 1e-6, f"{k}: Cay V8 {tree_val:.1f}% + Truc ngoai {other_val:.1f}% = {combined:.1f}% <= Cap {cap:.1f}%")

    print()
    if fails:
        print(f"AUDIT FAILED: {len(fails)} errors!")
        sys.exit(1)
    else:
        print("ALL AUDITS PASSED PERFECTLY!")

if __name__ == "__main__":
    main()
