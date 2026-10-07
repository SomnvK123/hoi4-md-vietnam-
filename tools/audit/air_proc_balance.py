"""Air procurement (Truc 1 khong quan) balance check: prices, popups per year, deliveries, modifier caps.

Pure stdlib, portable (no game files needed). Prints tables and PASS/FAIL lines; exit code 1 on any FAIL.
Numbers mirror VIE_air_truc1_review_and_plan.md and common/scripted_effects/VIE_md_effects_air_proc.txt.
It also reads the scheduler in that file and checks that every window below matches it, so the table cannot
drift from the code. Update the constants when the design changes, then rerun.

    python tools/audit/air_proc_balance.py
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
EFFECTS = os.path.join(ROOT, "common", "scripted_effects", "VIE_md_effects_air_proc.txt")

# program: (class, event no or None, window start year-month (first eligible month), window end y, historical cost USD bn, planes delivered to VIE_var_air_delivered)
PROGRAMS = {
    "india_dca":    ("B", 1,    (2000, 3), 2002, 0.05, 0),
    "s300":         ("B", 2,    (2004, 3), 2006, 0.30, 0),
    "su30_1":       ("B", 3,    (2004, 1), 2005, 0.12, 4),
    "yak52":        ("C", None, (2007, 1), 2009, 0.02, 0),
    "su30_2":       ("B", 5,    (2008, 6), 2010, 0.40, 8),
    "su30_3":       ("B", 6,    (2009, 9), 2011, 1.00, 12),
    "pechora":      ("B", 7,    (2009, 1), 2012, 0.15, 0),
    "c295":         ("B", 8,    (2013, 1), 2014, 0.10, 0),
    "su30_4":       ("B", 9,    (2013, 6), 2014, 0.60, 12),
    "spyder":       ("B", 10,   (2015, 1), 2016, 0.25, 0),
    "radar":        ("B", 11,   (2013, 1), 2015, 0.06, 0),
    "mig21_retire": ("C", None, (2016, 1), 2017, -0.03, 0),
    "india_train":  ("B", 13,   (2016, 12), 2018, 0.05, 0),
    "yak130":       ("B", 14,   (2017, 1), 2020, 0.35, 0),
    "t6c":          ("B", 15,   (2022, 1), 2024, 0.15, 0),
    "l39ng":        ("C", None, (2022, 1), 2024, 0.12, 0),
}
# Su-30 deliveries (date, planes): historical path; VIE_var_air_delivered must exceed 11 before 2011-12-31 (Truc 3 T5)
SU30_DELIVERIES = [((2004, 11), 4), ((2010, 12), 4), ((2011, 6), 4), ((2011, 12), 4), ((2012, 6), 4), ((2012, 12), 4),
                   ((2014, 12), 4), ((2015, 8), 4), ((2016, 2), 4)]
# popups already counted per year before air (tools/TESTING.md "Balance sanity", measured 2026-09-30) plus naval additions
BASELINE_POPUPS = {2003: 6 + 1, 2008: 6, 2012: 8, 2014: 8, 2018: 6, 2020: 6, 2021: 12, 2022: 6, 2023: 6, 2024: 7}
POPUP_TARGET = 7
POPUP_KNOWN_EXCEPTIONS = {2012, 2014, 2021}  # already over before air; air must not add to them
# air_defence_factor added by Truc 1 delivery effects: S-300 2 x 0.01, Pechora 0.02, SPYDER 2 x 0.01
AIR_DEF_TRUC1 = 0.02 + 0.02 + 0.02
AIR_DEF_CAP_TRUC1 = 0.06
HISTORICAL_TOTAL_RANGE = (3.6, 4.1)           # report 5.4: ~3.85 bn
SINGLE_EVENT_MAX = 1.1                         # E6 = 1.00; MD event median 4.0 bn, p25 0.3 bn
VIE_START_TREASURY = 5.0

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


# ---------------------------------------------------------------- 1. money
print("== 1. Chi (ty USD, lich su) ==")
total = sum(c for (_, _, _, _, c, _) in PROGRAMS.values())
for name, (cls, ev, start, end, cost, planes) in PROGRAMS.items():
    print(f"  {name:13s} class {cls} event {str(ev or '-'):>4s}  {start[0]}.{start[1]:02d}-{end}  {cost:6.2f}  planes {planes}")
print(f"  total {total:.2f}")
check(HISTORICAL_TOTAL_RANGE[0] <= total <= HISTORICAL_TOTAL_RANGE[1], f"total {total:.2f} in {HISTORICAL_TOTAL_RANGE}")
check(max(c for (_, _, _, _, c, _) in PROGRAMS.values()) <= SINGLE_EVENT_MAX, f"largest single event <= {SINGLE_EVENT_MAX}")
su30 = sum(PROGRAMS[k][4] for k in PROGRAMS if k.startswith("su30"))
check(abs(su30 - 2.12) < 0.01, f"Su-30 total {su30:.2f} (report 2.12)")

# ---------------------------------------------------------------- 2. popups per year (class B only)
print("\n== 2. Pop-up Class B moi nam (uoc tinh theo thang mo cua so dau tien) ==")
air: dict[int, list[str]] = {}
for name, (cls, ev, start, end, cost, planes) in PROGRAMS.items():
    if cls == "B":
        air.setdefault(start[0], []).append(name)
years = sorted(set(air) | set(BASELINE_POPUPS))
for y in years:
    base = BASELINE_POPUPS.get(y, 0)
    add = len(air.get(y, []))
    note = "" if y not in air else "  + " + ", ".join(air[y])
    print(f"  {y}: baseline {base} + air {add} = {base + add}{note}")
    if add and y in POPUP_KNOWN_EXCEPTIONS:
        check(False, f"{y}: air adds popups to a year already over target")
    elif add:
        check(base + add <= POPUP_TARGET or base == 0, f"{y}: {base}+{add} <= {POPUP_TARGET}" if base else f"{y}: baseline unmeasured, run ev.py")

# ---------------------------------------------------------------- 3. deliveries
print("\n== 3. Giao Su-30 (tich luy VIE_var_air_delivered) ==")
cum = 0
by_date = {}
for (y, m), n in SU30_DELIVERIES:
    cum += n
    by_date[(y, m)] = cum
    print(f"  {y}-{m:02d}: +{n} = {cum}")
check(cum == 36, f"historical Su-30 total {cum} == 36")
t5 = max(v for (y, m), v in by_date.items() if (y, m) <= (2011, 6))
check(t5 > 11, f"VIE_var_air_delivered > 11 by 2011-06 (is {t5}) so Truc 3 T5 (date > 2011-12-31) can open")
for name, (cls, ev, start, end, cost, planes) in PROGRAMS.items():
    if name.startswith("su30"):
        first = min(d for d in by_date if d >= start) if any(d >= start for d in by_date) else None
        check(first is not None, f"{name}: has a delivery on/after window start")

# ---------------------------------------------------------------- 4. modifiers
print("\n== 4. Modifier ==")
check(AIR_DEF_TRUC1 <= AIR_DEF_CAP_TRUC1 + 1e-9, f"air_defence_factor from Truc 1 {AIR_DEF_TRUC1:.2f} <= {AIR_DEF_CAP_TRUC1}")

# ---------------------------------------------------------------- 5. code cross-check
print("\n== 5. Doi chieu scheduler trong code ==")
try:
    with open(EFFECTS, encoding="utf-8") as f:
        code = f.read()
except OSError:
    code = ""
    check(False, "cannot read " + EFFECTS)
if code:
    sched = code[code.index("VIE_event_scheduler_air_proc = {"):code.index("# Template Class B")]
    found = {}
    for name, (cls, ev, start, end, cost, planes) in PROGRAMS.items():
        idx = sched.find(f"VIE_ap_{name}_offered")
        if idx == -1:
            check(False, f"{name}: no window call in scheduler")
            continue
        next_idx = len(sched)
        for other in PROGRAMS:
            if other != name:
                oi = sched.find(f"VIE_ap_{other}_offered", idx + 10)
                if oi != -1 and oi < next_idx:
                    next_idx = oi
        prog_block = sched[idx:next_idx]
        m_from = re.search(r"date\s*>\s*(\d+)\.(\d+)\.(\d+)", prog_block)
        m_end = re.search(r"date\s*>\s*(\d+)\.(\d+)\.(\d+)", prog_block[m_from.end():]) if m_from else None
        if not m_from or not m_end:
            check(False, f"{name}: date boundaries missing in scheduler block")
            continue
        fy, fm, fd = int(m_from.group(1)), int(m_from.group(2)), int(m_from.group(3))
        ey, em, ed = int(m_end.group(1)), int(m_end.group(2)), int(m_end.group(3))
        first = (fy, fm + 1) if fm < 12 else (fy + 1, 1)
        ev_m = re.search(r"country_event\s*=\s*\{\s*id\s*=\s*vie_air_proc\.(\d+)", prog_block)
        gcls = "B" if ev_m else "C"
        gev = int(ev_m.group(1)) if ev_m else None
        found[name] = (gcls, gev, fy, fm, ey)
        check(gcls == cls and gev == ev and first == start and ey == end,
              f"{name}: code class {gcls} event {gev} from {first} to {ey}")
    check(set(found) == set(PROGRAMS), "scheduler windows == PROGRAMS keys")

print()
if fails:
    print(f"{len(fails)} FAIL")
    sys.exit(1)
print("ALL PASS")
