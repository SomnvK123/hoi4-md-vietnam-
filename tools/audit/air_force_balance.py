"""Air force (Truc 3 khong quan) balance check: modifier totals per path, shared caps across Truc 1+2+3, code cross-check.

Pure stdlib, portable. Prints tables and PASS/FAIL lines; exit code 1 on any FAIL.
Numbers mirror VIE_air_truc3_review_and_plan.md 4.2, 4.4, 4.5. The VIE_af_* variables are shared by all axes, so every cap
is checked against the sum of Truc 1 + Truc 2 + Truc 3 (+ land forces for air_defence_factor).
Section 4 reads focus rewards from the code and compares them with the table, so the table cannot drift.

    python tools/audit/air_force_balance.py
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from itertools import product

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# token key -> modifier name (variable VIE_af_<name>)
TOKENS = {
    "exp": "experience_gain_air_factor", "atk": "air_attack_factor", "sup": "air_superiority_efficiency",
    "cas": "air_cas_efficiency", "mis": "air_mission_efficiency", "rng": "air_range_factor", "det": "air_detection",
    "home": "air_home_defence_factor", "int": "air_intercept_efficiency", "pers": "airforce_personnel_cost_multiplier_modifier",
    "ace": "air_ace_generation_chance_factor", "night": "air_night_penalty", "wx": "air_weather_penalty",
}
NAME2KEY = {v: k for k, v in TOKENS.items()}


def reward_pairs(block):
    """(key, percent) for every add_to_variable = { VIE_af_<token> = <number> } in a block; non-numeric values give percent 0."""
    out = []
    for name, val in re.findall(r"add_to_variable = \{ VIE_af_(\w+) = ([-\w.]+)", block):
        if name in NAME2KEY:
            try:
                out.append((NAME2KEY[name], float(val) * 100))
            except ValueError:
                out.append((NAME2KEY[name], 0.0))
    return out


# caps over ALL axes (percent)
CAPS = {"exp": 10, "atk": 10, "sup": 10, "cas": 10, "mis": 16, "rng": 20, "det": 20, "home": 20, "int": 8, "pers": 6, "ace": 10, "night": 6, "wx": 6}
# already used by other axes (percent): Truc 1 radar B +5 and Truc 2 +6 detection; air_defence_factor is not used by Truc 3
OTHER_AXES = {"det": 5 + 6}
AIR_DEF_CAP, AIR_DEF_OTHERS = 20, 6 + 4 + 5 + 3     # Truc 1 air 0.06, Truc 2 0.04, Igla 0.05, TL-01 0.03

# focus id -> {token: percent}; capstone (A4, B5, C5) base is also what D-E multiplies.
# Values = kept + new (VIE_air_effects_content_and_plan.md part 2). Direction-dependent bonuses (T6, B2) live in DIRECTION below.
FOCUS = {
    "VIE_airf_training_standardization": {"exp": 4, "ace": 3}, "VIE_airf_fighter_force": {"atk": 1, "ace": 2},
    "VIE_airf_sam_force": {"home": 2}, "VIE_airf_command_reform_1": {"mis": 2, "night": -1}, "VIE_airf_first_force": {},
    "VIE_airf_command_reform_2": {"mis": 2, "det": 1}, "VIE_airf_medium_force": {"rng": 3, "wx": -1},
    "VIE_airf_operating_range": {"rng": 4, "det": 1},
    "VIE_airf_iads": {"home": 2, "int": 0.5, "rng": -2, "ace": 1.5},
    "VIE_airf_layered_defence": {"det": 2, "home": 2, "wx": -1, "sup": 1.5},
    "VIE_airf_ew_antistealth": {"int": 3, "det": 2, "night": -1, "wx": -1, "sup": 1},
    "VIE_airf_iads_command": {"mis": 2, "home": 2, "night": -1, "atk": 1},
    "VIE_airf_multirole": {"rng": 4, "wx": -1, "pers": 2, "ace": 1},
    "VIE_airf_multirole_fleet": {"atk": 3, "sup": 2, "cas": 2}, "VIE_airf_sustainment": {"mis": 2, "wx": -2, "night": -1, "pers": -1},
    "VIE_airf_airlift_tanker": {"rng": 3}, "VIE_airf_multirole_wing": {"mis": 2, "atk": 2, "ace": 2},
    "VIE_airf_unmanned": {"det": 1, "home": -1, "ace": 1.5, "night": -0.5}, "VIE_airf_isr_uav": {"det": 3, "night": -1.5, "wx": -1},
    "VIE_airf_datalink": {"mis": 2, "wx": -1, "sup": 1}, "VIE_airf_strike_uav": {"atk": 3, "rng": 1},
    "VIE_airf_teaming": {"mis": 2, "int": 2, "ace": 1, "night": -1},
}
# direction-dependent extras (read from VIE_airf_force_priority / VIE_airf_fighter_specialty); worst case taken in section 1
T6_DIR = {0: {}, 1: {"int": 1}, 2: {"int": 0.5, "rng": 0.5, "night": -0.5}, 3: {"rng": 1}}
B2_SPEC = {"sup": {"sup": 1}, "gnd": {"cas": 1}}
MS1 = {"ace": 1}   # milestone vie_air_force.70 (step 6), given to every player
REWARD_CODE = {f: c for f, c in zip(FOCUS, "t1 t2 t3 t4 t5 t6 t7 t8 a1 a2 a3 a4 b1 b2 b3 b4 b5 c1 c2 c3 c4 c5".split())}
CHAIN = [f for f in FOCUS if f.split("_", 2)[2] in (
    "training_standardization", "fighter_force", "sam_force", "command_reform_1", "first_force", "command_reform_2",
    "medium_force", "operating_range")]
BRANCH = {
    "A": ["VIE_airf_iads", "VIE_airf_layered_defence", "VIE_airf_ew_antistealth", "VIE_airf_iads_command"],
    "B": ["VIE_airf_multirole", "VIE_airf_multirole_fleet", "VIE_airf_sustainment", "VIE_airf_airlift_tanker", "VIE_airf_multirole_wing"],
    "C": ["VIE_airf_unmanned", "VIE_airf_isr_uav", "VIE_airf_datalink", "VIE_airf_strike_uav", "VIE_airf_teaming"],
}
CAPSTONE = {"A": "VIE_airf_iads_command", "B": "VIE_airf_multirole_wing", "C": "VIE_airf_teaming"}
D_E_BASE = {"A": {"mis": 2, "home": 2}, "B": {"mis": 2, "atk": 2}, "C": {"mis": 2, "int": 2}}   # what VIE_airf_d5_finish multiplies
DE_BONUS = 0.5      # D-E level 2 adds +50% of the capstone base (level 1: +25%)

# Decisions (level 2 = x1.5). D-A specialty, D-B (early orientation adds HOME +1), D-C stages, D-D force structure
D_A = {"sup": {"sup": 3}, "gnd": {"cas": 3, "atk": 1}}
D_B = {"home": 3, "det": 1}
D_B_EARLY = {"home": 1}
D_C = [{"mis": 2}, {"home": 2, "sup": 2}, {"det": 1, "mis": 2}]
D_D = {1: {"int": 3, "home": 2, "rng": -3}, 2: {"atk": 1, "int": 1, "rng": 1}, 3: {"rng": 5, "mis": 2, "pers": 3}}

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


def add(d, src, mult=1.0):
    for k, v in src.items():
        d[k] += v * mult


def path_total(branch, spec, prio, level, early):
    d = defaultdict(float)
    for f in CHAIN + BRANCH[branch]:
        add(d, FOCUS[f])
    add(d, T6_DIR[prio])
    add(d, MS1)
    if branch == "B":
        add(d, B2_SPEC[spec])
    add(d, D_A[spec], 1.5 if level == 2 else 1.0)
    add(d, D_B, 1.5 if level == 2 else 1.0)
    if early:
        add(d, D_B_EARLY)
    for s in D_C:
        add(d, s)
    add(d, D_D[prio])
    add(d, D_E_BASE[branch], DE_BONUS if level == 2 else 0.25)
    if (branch == "A" and prio == 1) or (branch in "BC" and prio == 3):
        d["mis"] += 1                       # branch fit bonus (VIE_airf_branch_fit_*)
    for k in ("night", "wx"):               # penalties: negative value = improvement, caps are on the magnitude
        d[k] = -d[k]
    return d


# ---------------------------------------------------------------- 1. totals per branch
print("== 1. Tong lon nhat cua Truc 3 (moi to hop chuyen mon x co cau x muc, D-E) ==")
worst = {}
for br in "ABC":
    mx = defaultdict(float)
    for spec, prio, level, early in product(("sup", "gnd"), (1, 2, 3), (1, 2), (False, True)):
        for k, v in path_total(br, spec, prio, level, early).items():
            mx[k] = max(mx[k], v)
    worst[br] = mx
    print(f"  nhanh {br}: " + ", ".join(f"{k} {mx[k]:.2f}" for k in TOKENS if mx[k]))

# ---------------------------------------------------------------- 2. caps across axes
print("\n== 2. Tran cong don Truc 1+2+3 (bien VIE_af_* dung chung) ==")
for br in "ABC":
    for k, cap in CAPS.items():
        total = worst[br][k] + OTHER_AXES.get(k, 0)
        check(total <= cap + 1e-9, f"nhanh {br} {k}: Truc 3 {worst[br][k]:.2f} + truc khac {OTHER_AXES.get(k, 0)} = {total:.2f} <= {cap}")
check(AIR_DEF_OTHERS <= AIR_DEF_CAP, f"air_defence_factor: Truc 1+2+luc quan {AIR_DEF_OTHERS} <= {AIR_DEF_CAP}, Truc 3 khong dung")

# Transient experience: timed ideas also add experience_gain_air_factor. Peak = Truc 3 permanent + Truc 1 pilot-training idea (+5, 3 years)
# + the four Truc 2 / Truc 3 "programme running" indicator ideas (0.25% each, two slots per axis). Truc 1 basic training (+3) never overlaps.
EXP_PEAK = max(worst[b]["exp"] for b in "ABC") + 5 + 4 * 0.25
check(EXP_PEAK <= CAPS["exp"] + 1e-9, f"experience peak with timed ideas {EXP_PEAK:.2f} <= {CAPS['exp']}")

# ---------------------------------------------------------------- 3. tokens exist in dynamic modifier
print("\n== 3. Token trong VIE_armed_forces_modifier ==")
try:
    dm = open(os.path.join(ROOT, "common", "dynamic_modifiers", "VIE_md_dynamic_modifiers.txt"), encoding="utf-8").read()
except OSError:
    dm = ""
    check(False, "cannot read dynamic modifiers")
for k, name in TOKENS.items():
    check(re.search(r"\b%s = VIE_af_%s\b" % (name, name), dm) is not None, f"{name} = VIE_af_{name}")

# ---------------------------------------------------------------- 4. code cross-check (focus rewards)
print("\n== 4. Doi chieu focus trong code ==")
fpath = os.path.join(ROOT, "common", "national_focus", "VIE_md_focus.txt")
try:
    ftxt = open(fpath, encoding="utf-8").read()
except OSError:
    ftxt = ""
    check(False, "cannot read focus file")
present = 0
effects_path = os.path.join(ROOT, "common", "scripted_effects", "VIE_md_effects_air_force.txt")
try:
    etxt0 = open(effects_path, encoding="utf-8").read()
except OSError:
    etxt0 = ""
    check(False, "cannot read effects file")
for fid, want in FOCUS.items():
    name = "VIE_airf_%s_reward" % REWARD_CODE[fid]
    m = re.search(r"\n%s = \{(.*?)\n\}" % name, etxt0, re.S)
    if not m:
        check(False, f"{fid}: effect {name} khong thay")
        continue
    body = re.sub(r"\n\t(?:else_)?if = \{.*?\n\t\}", "", m.group(1), flags=re.S)   # drop direction-dependent branches
    got = {}
    for k, v in reward_pairs(body):
        got[k] = got.get(k, 0) + v
    present += 1
    check({k: round(v, 3) for k, v in got.items()} == {k: float(v) for k, v in want.items()}, f"{fid}: code {got} vs bang {want}")
    block = ftxt[ftxt.find("id = " + fid):]
    block = block[:block.find("\n\t}")]
    check(("VIE_airf_%s_reward = yes" % REWARD_CODE[fid]) in block or "VIE_airf_add_" in block or "add_to_variable" in block,
          f"{fid}: focus goi {name} (hoac con reward cu)")
print(f"  {present}/{len(FOCUS)} focus Truc 3 co effect")

# Decisions: every (token, value) written by a *_finish effect must be the one the table gives (levels x1 / x1.5, early +1, ...)
print("\n== 5. Doi chieu Decision trong code ==")
epath = os.path.join(ROOT, "common", "scripted_effects", "VIE_md_effects_air_force.txt")
try:
    etxt = open(epath, encoding="utf-8").read()
except OSError:
    etxt = ""
    check(False, "cannot read effects file")
EXPECT = {
    "VIE_airf_d1_finish": {("sup", 3), ("sup", 4.5), ("cas", 3), ("cas", 4.5), ("atk", 1), ("atk", 1.5)},
    "VIE_airf_d2_finish": {("home", 3), ("home", 4.5), ("det", 1), ("det", 1.5), ("home", 1)},
    "VIE_airf_d3_stage1": {("mis", 2)}, "VIE_airf_d3_stage2": {("home", 2), ("sup", 2)}, "VIE_airf_d3_finish": {("det", 1), ("mis", 2)},
    "VIE_airf_d4_finish": {("int", 3), ("home", 2), ("rng", -3), ("rng", 5), ("mis", 2), ("pers", 3), ("atk", 1), ("int", 1), ("rng", 1)},
    "VIE_airf_d5_finish": {("mis", 0), ("home", 0), ("atk", 0), ("int", 0)},
}
for name, want in EXPECT.items():
    m = re.search(r"\n%s = \{(.*?)\n\}" % name, etxt, re.S)
    if not m:
        check(False, f"{name}: khong thay trong code")
        continue
    got = {(k, round(v, 3)) for k, v in reward_pairs(m.group(1))}
    if name == "VIE_airf_d5_finish":
        got = {(k, 0) for k, _ in reward_pairs(m.group(1))}
    check(got == {(k, float(v)) for k, v in want}, f"{name}: code {sorted(got)} vs bang {sorted(want)}")
m = re.search(r"VIE_airf_d5_finish = \{(.*?)\n\}", etxt, re.S)
if m:
    vals = [float(v) for v in re.findall(r"VIE_airf_bonus = ([\d.]+) \}", m.group(1))]
    check(sorted(vals) == [0.005, 0.01], f"D-E bonus {vals} = 0.25 / 0.5 x capstone base (MIS 2%)")

# ---------------------------------------------------------------- 6. tech bonus categories exist in MD
print("\n== 6. Category add_tech_bonus (khong quan) co trong file tech cua MD ==")
import glob
ref = ""
for fp in glob.glob(os.path.join(ROOT, "tools", "audit", "md_ref", "tech_*.txt")):
    ref += open(fp, encoding="utf-8", errors="ignore").read()
for fn in ("VIE_md_effects_air_force.txt", "VIE_md_effects_air_ind.txt"):
    txt = open(os.path.join(ROOT, "common", "scripted_effects", fn), encoding="utf-8").read()
    for cat in sorted(set(re.findall(r"category = (CAT_\w+)", txt))):
        check(re.search(r"\b%s\b" % cat, ref) is not None, f"{fn}: {cat}")

print()
if fails:
    print(f"{len(fails)} FAIL")
    sys.exit(1)
print("ALL PASS")
