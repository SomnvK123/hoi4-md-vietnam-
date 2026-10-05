"""Naval Truc 3 (luc luong) + Truc 1B balance check: modifier caps per full path, costs, MD quantiles.

Pure stdlib. Numbers mirror VIE_naval_truc3_review_and_plan.md (5.4 and 5.5). Update the constants
when the design changes, then rerun. Exit code 1 on any FAIL.

    python tools/audit/nf_balance.py
"""
from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------- modifiers (percent points; + = bonus)
# v2 (VIE_naval_effects_content_and_plan.md): new axes hit / speed / capatk / capdef / aa / pers.
SPINE = {  # T1, T3, T4, T5, T7, T8, T9
    "T1": {"exp": 5, "hit": 1},
    "T3": {"org": 2, "hit": 1},
    "T4": {"subatk": 2, "subdef": 1},
    "T5": {"org": 2, "coord": 3},
    "T7": {"org": 2, "coord": 3},
    "T8": {"range": 3, "speed": 1},
    "T9": {"range": 5, "detect": 5},
}
T7_DIR = {"coastal": {"hit": 1.5}, "balanced": {"org": 0.5, "hit": 0.5, "speed": 0.5}, "extended": {"speed": 1.5}}
TRUC2 = {"speed": 2, "hit": 1}  # F4 naval_speed +2, F5 hit +1
MILESTONES = {"org": 1, "hit": 1}  # vie_nav_force.70 / .72 (plan part 5)
D_A = {  # level 2 values (level 1 = 2/3 of them)
    "fire": {"strike": 4.5, "org": 1.5},
    "asw": {"subdef": 4.5, "detect": 3},
}
D_B = {"hist": {"subatk": 4.5, "detect": 1.5}, "early": {"subatk": 4.5, "detect": 2.5}}
D_C = {"coord": 6, "subdef": 2}
D_D = {  # force_priority -> (modifiers, branch it matches)
    "coastal": ({"strike": 2, "range": -3}, "denial"),
    "balanced": ({"org": 1, "strike": 1, "range": 1}, None),
    "extended": ({"range": 4, "org": 2, "pers": 3}, ("green", "blue")),
}
MATCH_BONUS = {"org": 1}
BRANCH = {
    "denial": [{"strike": 3, "hit": 2, "range": -2}, {"mines_plant": 10, "mines_red": 5, "hit": 1},
               {"subatk": 3, "subdef": 2}, {"org": 3, "detect": 4, "hit": 1.5}],
    "green": [{"range": 5, "speed": 2, "pers": 2}, {"range": 3, "org": 2, "aa": 2},
              {"inv_plan": 10, "inv_cap": 1, "speed": 1}, {"inv_cap": 1, "aa": 2},
              {"org": 3, "coord": 3, "hit": 1, "speed": 1}],
    "blue": [{"range": 5, "speed": 2, "capdef": 2, "pers": 3}, {"aa": 5, "subdef": 1},
             {"range": 3, "org": 2, "pers": -1}, {"aa": 3, "detect": 4, "hit": 1},
             {"org": 3, "coord": 5, "capatk": 2, "capdef": 2}],
}
# Bien Dong (Luat Bien) feeds the same VIE_armed_forces_modifier: only spratly_fortification (+range 5).
# Optional, so the worst case always includes it. coord / detect are already at the cap on the Truc 3 worst
# path (19.5 / 14.5), so coast_guard_law and spratly_fortification must not add to them.
SCS = {"range": 5}
CARRIER_MULT = 1.5  # B5 modifiers x1.5 once D-E (carrier group) is done

CAPS = {"org": 18, "coord": 20, "detect": 15, "range": 25, "subatk": 10, "subdef": 10, "strike": 10, "exp": 10,
        "hit": 10, "speed": 10, "capatk": 8, "capdef": 8, "aa": 12, "pers": 6}

# ---------------------------------------------------------------- money, USD bn
FORCE_COST = {  # Decision costs
    "D-A": {1: 0.40, 2: 0.60},
    "D-B": {"hist": {1: 0.30, 2: 0.45}, "early": {1: 0.50, 2: 0.75}},
    "D-C": 0.50,
    "D-D": 0.60,
    "D-E": 1.00,
}
LOC_MULT = {0: 1.0, 1: 1.15, 2: 1.3}
P1B = {  # code: (unit price, min qty, max qty)
    "P1": (0.40, 2, 6),
    "P2": (0.45, 2, 4),
    "P3": (0.50, 2, 4),
    "P4": (0.55, 2, 4),
    "P6": (0.15, 1, 3),
    "P7": (0.60, 1, 2),
    "P8": (0.70, 2, 3),
    "P10": (2.70, 1, 1),
    "P11": (2.00, 1, 2),
}
BRANCH_PROGRAMS = {
    "denial": ["P1", "P2", "P3", "P4", "P6", "P11x"],
    "green": ["P1", "P2", "P3", "P4", "P7"],
    "blue": ["P1", "P2", "P3", "P8", "P10", "P11"],
}
MD_P90 = 26.45
SIZE_NAMES = {"org": "navy_org_factor", "coord": "naval_coordination", "detect": "naval_detection",
              "range": "navy_max_range_factor", "subatk": "navy_submarine_attack_factor",
              "subdef": "navy_submarine_defence_factor", "strike": "naval_strike_attack_factor",
              "exp": "experience_gain_navy_factor", "hit": "naval_hit_chance", "speed": "naval_speed_factor",
              "capatk": "navy_capital_ship_attack_factor", "capdef": "navy_capital_ship_defence_factor",
              "aa": "navy_anti_air_attack_factor", "pers": "navy_personnel_cost (net)"}

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


def add(total: Counter, mods: dict, mult: float = 1.0) -> None:
    for k, v in mods.items():
        total[k] += v * mult


def path_totals(branch: str, da: str, db: str, dd: str, carriers: bool):
    t: Counter = Counter()
    for m in SPINE.values():
        add(t, m)
    add(t, D_A[da])
    add(t, D_B[db])
    add(t, {"coord": D_C["coord"], "subdef": D_C["subdef"]})
    add(t, SCS)
    add(t, T7_DIR[dd])
    add(t, TRUC2)
    add(t, MILESTONES)
    mods, match = D_D[dd]
    add(t, mods)
    ok_match = (match == branch) if isinstance(match, str) else (branch in match if match else True)
    if ok_match and match is not None:
        add(t, MATCH_BONUS)
    for i, m in enumerate(BRANCH[branch]):
        mult = CARRIER_MULT if (branch == "blue" and i == 4 and carriers) else 1.0
        add(t, m, mult)
    return t


def main() -> int:
    print("== 1. Modifier totals per full path (percent points), caps from plan 5.4")
    worst: Counter = Counter()
    worst_label: dict = {}
    n = 0
    for branch, da, db, dd, car in itertools.product(BRANCH, D_A, D_B, D_D, (False, True)):
        n += 1
        t = path_totals(branch, da, db, dd, car)
        for k, v in t.items():
            if v > worst[k]:
                worst[k] = v
                worst_label[k] = (branch, da, db, dd, car)
    print("  %d path combinations" % n)
    for k in sorted(CAPS):
        print("  %-30s worst %5.1f  cap %2d  at %s" % (SIZE_NAMES[k], worst[k], CAPS[k], worst_label.get(k)))
        check(worst[k] <= CAPS[k], "%s worst case %.1f <= cap %d" % (SIZE_NAMES[k], worst[k], CAPS[k]))

    # experience_gain_navy_factor also comes from static ideas (read from the idea file so it cannot drift)
    ideas = Path(__file__).resolve().parents[2].joinpath("common/ideas/VIE_md_ideas_p2.txt").read_text(encoding="utf-8")
    idea_exp = 0.0
    for name in ("VIE_coast_guard_idea", "VIE_cam_ranh_idea"):
        m = re.search(r"\t\t%s = \{.*?experience_gain_navy_factor = ([\d.]+)" % name, ideas, re.S)
        v = float(m.group(1)) * 100 if m else 0.0
        idea_exp += v
        print("  %-28s experience_gain_navy_factor +%.1f" % (name, v))
    check(worst["exp"] + idea_exp <= CAPS["exp"],
          "experience_gain_navy_factor force axis %.1f + ideas %.1f <= cap %d" % (worst["exp"], idea_exp, CAPS["exp"]))

    print("\n== 2. Force Decisions (USD bn)")
    low = FORCE_COST["D-A"][1] + FORCE_COST["D-B"]["hist"][1] + FORCE_COST["D-C"] + FORCE_COST["D-D"]
    high = FORCE_COST["D-A"][2] + FORCE_COST["D-B"]["early"][2] + FORCE_COST["D-C"] + FORCE_COST["D-D"]
    print("  D-A..D-D all Basic / Historical: %.2f   all Intensive / Early: %.2f   plus D-E %.2f" % (low, high, FORCE_COST["D-E"]))
    check(abs(low - 1.8) < 1e-9 and abs(high - 2.45) < 1e-9, "force decision totals 1.8 .. 2.45 (plan 5.5)")

    print("\n== 3. Truc 1B programs (USD bn, max quantity, domestic x%.1f)" % LOC_MULT[2])
    total_max = 0.0
    biggest = 0.0
    for code, (unit, lo, hi) in P1B.items():
        c = unit * hi * LOC_MULT[2]
        total_max += c
        biggest = max(biggest, c)
        print("  %-4s %5.2f x %d x 1.3 = %6.2f   (min qty import %5.2f)" % (code, unit, hi, c, unit * lo))
    print("  all programs at max quantity, domestic: %.2f" % total_max)
    check(biggest <= MD_P90, "largest single program %.2f below MD event cost p90 %.2f" % (biggest, MD_P90))
    check(total_max <= 25, "sum of all 1B programs <= 25bn (%.1f)" % total_max)
    check(P1B["P11"][0] * 2 * LOC_MULT[2] == 5.2, "P11 x2 domestic = 5.2bn (plan 5.5 text)")

    print("\n== 4. Per-branch purchase totals (import path, typical quantity = max)")
    for br, progs in {"denial": ["P1", "P2", "P3", "P4", "P6"], "green": ["P1", "P2", "P3", "P4", "P7"], "blue": ["P1", "P2", "P3", "P8", "P10", "P11"]}.items():
        s = sum(P1B[p][0] * P1B[p][2] for p in progs)
        print("  %-7s %.2f" % (br, s))
        check(s <= 25, "%s branch purchases <= 25bn" % br)
    print("\nRESULT:", "FAIL (%d)" % len(fails) if fails else "PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
