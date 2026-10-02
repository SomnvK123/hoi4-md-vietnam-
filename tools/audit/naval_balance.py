"""Naval axes balance check (Truc 1 prices, Truc 2 costs and experience thresholds, timeline).

Pure stdlib, portable (no game files needed). Prints tables and PASS/FAIL lines; exit code 1 on any FAIL.
Numbers mirror VIE_naval_truc2_review_and_plan.md and common/scripted_effects/VIE_md_effects_naval_ships.txt.
Update the constants below when the design changes, then rerun.

    python tools/audit/naval_balance.py
"""
from __future__ import annotations

import itertools
import sys
from datetime import date, timedelta

# ---------------------------------------------------------------- experience (report 7.3, Truc 2 plan)
ORIENT = {"shipbuilding": (12, 0), "mro": (0, 12), "balanced": (6, 6)}  # (shipbuilding_exp, mro_exp)
D1_INVEST = {"basic": 5, "extended": 10, "focus": 15}                    # shipbuilding_exp
D2_LEVEL = {"basic": 10, "intensive": 20, "autonomy": 30}                # mro_exp
D3_SPEC = {"patrol": 6, "fast": 8, "multi": 5}                           # shipbuilding_exp
D3_LEVEL = {"pilot": 5, "mass": 10, "transfer": 15}                      # shipbuilding_exp
MOLNIYA_P2_SHIPS = {0: 0, 6: 6, 8: 8, 10: 10}                            # +3 shipbuilding_exp per ship
EXP_PER_SHIP = 3
MRO_CAP_RUSSIA = 50
CAP = 100
THRESH_SHIP, THRESH_MRO = 30, 15      # Decision 5 start (Truc 2 plan, A3 after correction)

# ---------------------------------------------------------------- money, USD bn (modify_treasury_effect)
T1 = {  # unit price, historical quantity
    "kilo": (2.0 / 6 + 0.2, 6),     # 0.333 + 0.2 full training pack = 3.2 for six
    "gepard1": (0.175, 2),
    "gepard2": (0.35, 2),
    "molniya_p1": (0.06, 2),
    "molniya_p2": (0.13, 6),
    "bastion": (0.15, 2),
}
D1_COST = {"basic": 7.5, "extended": 12.0, "focus": 18.0}   # dockyards via MD one_state_dockyard (7.5 each)
D2_BASE, D2_SOURCE, D2_SCOPE = 4.0, {"russia": 0.8, "auto": 1.4}, {"sub": 1.0, "surface": 1.0, "fleet": 1.3}
D2_LEVEL_MULT = {"basic": 1.0, "intensive": 1.6, "autonomy": 2.4}
D3_BASE, D3_LEVEL_MULT = 6.0, {"basic": 1.0, "extended": 1.6, "focus": 2.4}
D4_BASE, D4_FIELD_MULT = 7.0, {"electronics": 1.0, "weapons": 1.0, "full": 1.5}
D4_LEVEL_MULT = {"basic": 1.0, "balanced": 1.6, "autonomy": 2.4}
D5_BASE, D5_MULT = 10.0, {"limited": 1.0, "integrated": 1.5, "high": 2.2}

# MD reference: 1807 literal "treasury_change = -N" values in MD events (all countries), measured 2026-10-02
MD_EVENT_COST_QUANTILES = {10: 0.06, 25: 0.3, 50: 4.0, 75: 10.0, 90: 26.45, 99: 100.0}
VIE_START_TREASURY = 5.0   # history/countries/VIE - Vietnam.txt: treasury 5, debt 77.514

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


def exp_paths():
    """Yield (label, shipbuilding_exp, mro_exp) for every combination of the exp-bearing choices."""
    for (on, (os_, om)), (inv, ie), (ll, le), (sp, se), (sl, sle), (ships, _) in itertools.product(
        ORIENT.items(), D1_INVEST.items(), D2_LEVEL.items(), D3_SPEC.items(), D3_LEVEL.items(), MOLNIYA_P2_SHIPS.items()
    ):
        ship = os_ + ie + se + sle + ships * EXP_PER_SHIP
        mro = om + le
        yield (on, inv, ll, sp, sl, ships), min(ship, CAP), min(mro, CAP)


def main() -> int:
    print("== 1. Experience reachability (Decision 5 start: shipbuilding_exp >= %d, mro_exp >= %d)" % (THRESH_SHIP, THRESH_MRO))
    paths = list(exp_paths())
    ok_paths = [p for p in paths if p[1] >= THRESH_SHIP and p[2] >= THRESH_MRO]
    print("  %d combinations, %d reach the thresholds (%.0f%%)" % (len(paths), len(ok_paths), 100 * len(ok_paths) / len(paths)))
    print("  historical-style paths (all Basic, Russia support, Molniya phase 2 = 6 ships, Basic MRO):")
    for on in ORIENT:
        os_, om = ORIENT[on]
        ship = os_ + D1_INVEST["basic"] + D3_SPEC["patrol"] + D3_LEVEL["pilot"] + 6 * EXP_PER_SHIP
        mro = om + D2_LEVEL["basic"]
        mark = "ok" if ship >= THRESH_SHIP and mro >= THRESH_MRO else "short"
        print("    orientation %-12s ship_exp %2d  mro_exp %2d  -> %s" % (on, ship, mro, mark))
    hist_ship = ORIENT["balanced"][0] + 5 + 6 + 5 + 18
    hist_mro = ORIENT["balanced"][1] + 10
    check(hist_ship >= THRESH_SHIP and hist_mro >= THRESH_MRO,
          "balanced + all-Basic + Molniya phase 2 reaches Decision 5 (%d/%d)" % (hist_ship, hist_mro))
    no_p2 = ORIENT["balanced"][0] + 5 + 6 + 5
    check(no_p2 < THRESH_SHIP, "skipping Molniya phase 2 is NOT enough on all-Basic (%d < %d): domestic building is rewarded" % (no_p2, THRESH_SHIP))
    check(0.15 <= len(ok_paths) / len(paths) <= 0.85, "thresholds are neither trivial nor unreachable (pass rate %.0f%%)" % (100 * len(ok_paths) / len(paths)))
    print("  original report thresholds (50/30) for comparison:")
    orig = [p for p in paths if p[1] >= 50 and p[2] >= 30]
    all_basic = [p for p in paths if p[0][1] == "basic" and p[0][2] == "basic" and p[0][5] == 6]
    check(not any(p[1] >= 50 and p[2] >= 30 for p in all_basic),
          "report thresholds 50/30 are unreachable on every all-Basic path with 6 Molniya ships (%d of %d combos reach it at all)" % (len(orig), len(paths)))
    print("  mro_exp Russia-dependent cap %d: reachable max without cap %d" % (MRO_CAP_RUSSIA, max(p[2] for p in paths)))

    print("\n== 2. Money (USD bn)")
    t1_hist = sum(unit * qty for unit, qty in T1.values())
    for k, (unit, qty) in T1.items():
        print("  Truc 1 %-11s %5.3f x %d = %5.2f" % (k, unit, qty, unit * qty))
    print("  Truc 1 historical total: %.2f" % t1_hist)
    t2_hist = D1_COST["basic"] + D2_BASE * D2_SOURCE["russia"] + D3_BASE * D3_LEVEL_MULT["basic"] + D4_BASE * D4_FIELD_MULT["electronics"] + D5_BASE * D5_MULT["limited"]
    t2_max = D1_COST["focus"] + D2_BASE * D2_LEVEL_MULT["autonomy"] * D2_SOURCE["auto"] * D2_SCOPE["fleet"] + D3_BASE * D3_LEVEL_MULT["focus"] + D4_BASE * D4_LEVEL_MULT["autonomy"] * D4_FIELD_MULT["full"] + D5_BASE * D5_MULT["high"]
    print("  Truc 2 historical (all Basic / Russia / Limited): %.2f   maximum: %.2f" % (t2_hist, t2_max))
    print("  Both axes historical: %.2f   (army Truc 2 total for comparison: 30.25)" % (t1_hist + t2_hist))
    biggest = max(list(D1_COST.values()) + [D5_BASE * D5_MULT["high"], D4_BASE * D4_LEVEL_MULT["autonomy"] * D4_FIELD_MULT["full"], D3_BASE * D3_LEVEL_MULT["focus"], 3.2])
    check(biggest <= MD_EVENT_COST_QUANTILES[90], "largest single item %.1f is below MD event cost p90 (%.2f)" % (biggest, MD_EVENT_COST_QUANTILES[90]))
    check(t1_hist + t2_hist <= 60, "combined historical cost <= 60bn (%.1f)" % (t1_hist + t2_hist))
    check(T1["kilo"][0] * 6 <= 3.3 and T1["kilo"][0] * 6 >= 3.1, "Kilo full pack for six = 3.2bn (source range 1.8-3.2)")
    molniya_total = T1["molniya_p1"][0] * T1["molniya_p1"][1] + T1["molniya_p2"][0] * T1["molniya_p2"][1]
    check(0.8 <= molniya_total <= 1.2, "Molniya phases 1+2 = %.2fbn vs ~1.0bn quoted for the 2 + 6 ships plus licence" % molniya_total)
    check(abs(T1["bastion"][0] * 2 - 0.30) < 1e-9, "Bastion-P two complexes = 0.30bn (Syria 2007: 0.30bn for two complexes)")
    print("  Sigma: 0.33 x qty x config (1.0 / 1.15 / 1.3), x1.25 late; two ships Domestic = %.2f; treasury at start = %.0f" % (0.33 * 2 * 1.3, VIE_START_TREASURY))
    check(0.33 * 2 * 1.3 < VIE_START_TREASURY, "Sigma Funding Gate is reachable at game start treasury (%.2f < %.0f)" % (0.33 * 2 * 1.3, VIE_START_TREASURY))
    print("  Dockyard: MD one_state_dockyard = 7.5 each, two_state_dockyards = 15 (auto-charged; Decision 1 pays only the remainder by hand)")
    check(abs(D1_COST["extended"] - 7.5 - 4.5) < 1e-9 and abs(D1_COST["focus"] - 15 - 3) < 1e-9, "Decision 1 tiers = 7.5 / 7.5+4.5 / 15+3 (ratio 1 : 1.6 : 2.4 of base)")

    print("\n== 3. Timeline for the Ba Son flag before Molniya phase 2 (opens 2009-06-01)")
    f_days = 5 * 7 + 5 * 7                       # Focus 1 and 2, cost 5 each (weeks) with one focus slot
    start = date(2005, 1, 1)
    for lvl, d in (("basic", 146), ("extended", 219), ("focus", 292)):
        ready = start + timedelta(days=f_days + d)
        print("  best case (2005-01-01 start), %-8s milestone at %s" % (lvl, ready))
        check(ready < date(2009, 6, 1), "%s: flag set before 2009-06-01" % lvl)
    latest = date(2009, 6, 1) - timedelta(days=f_days + 292)
    print("  latest start of Focus 1 that still gives tier 3 before 2009-06-01: %s" % latest)

    print("\n== 4. Slot and duration sanity")
    for name, days in (("D1 basic", 365), ("D1 extended", 548), ("D1 focus", 730)):
        print("  %-12s %4d days" % (name, days))
    check(all(d <= 730 * 1.25 for d in (365, 548, 730)), "longest duration with +25%% modifier = %d days (<= 913)" % int(730 * 1.25))
    print("\nRESULT:", "FAIL (%d)" % len(fails) if fails else "PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
