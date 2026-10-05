"""Air industry (Truc 2 khong quan) balance check: costs, durations, modifier totals, MIO size, earliest finish.

Pure stdlib, portable. Prints tables and PASS/FAIL lines; exit code 1 on any FAIL.
Numbers mirror VIE_air_force_content_report.md 6.3 and the code in events/VIE_air_ind.txt and
common/scripted_effects/VIE_md_effects_air_ind.txt; section 5 reads the code and compares, so the table cannot drift.

    python tools/audit/air_ind_balance.py
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# event no -> {option: (cost USD bn, months)}; option "a" is the historical one
OPTIONS = {
    11: {"a": (0.15, 12), "b": (0.08, 24)}, 12: {"a": (0.20, 30), "b": (0.15, 24)}, 13: {"a": (0.30, 30), "b": (0.25, 30)},
    21: {"a": (0.10, 18), "b": (0.04, 30)}, 22: {"a": (0.15, 24), "b": (0.20, 30)}, 23: {"a": (0.35, 36), "b": (0.45, 36)},
    31: {"a": (0.10, 18), "b": (0.14, 24)}, 32: {"a": (0.18, 24), "b": (0.22, 18)}, 33: {"a": (0.30, 30), "b": (0.30, 30)},
    41: {"a": (0.12, 18), "b": (0.12, 18)}, 42: {"a": (0.25, 24), "b": (0.32, 24)}, 43: {"a": (0.40, 36), "b": (0.40, 36)},
    51: {"a": (0.05, 12)}, 52: {"a": (0.15, 24), "b": (0.20, 18)}, 53: {"a": (0.30, 36), "b": (0.36, 36)},
}
PILLARS = {"a32": (11, 12, 13), "a31": (21, 22, 23), "radar": (31, 32, 33), "integ": (41, 42, 43), "uav": (51, 52, 53)}
# earliest start (year, month) per tier: focus + date + Truc 1 gate (Pechora contract assumed 2009-03, SPYDER 2015-02)
EARLIEST = {
    "a32": [(2011, 1), (2017, 1), (2024, 1)], "a31": [(2009, 3), (2013, 1), (2021, 1)], "radar": [(2014, 1), (2019, 1), (2024, 1)],
    "integ": [(2015, 2), (2015, 2), (2025, 1)], "uav": [(2018, 1), (2023, 1), (2026, 1)],
}
DEPENDS = {("integ", 1): [("radar", 0)], ("uav", 1): [("radar", 0)]}   # (pillar, tier index) needs (pillar, tier index) finished
# modifier added by Truc 2 (all pillars, full path)
ACCIDENTS = -0.03 - 0.03 - 0.02
DETECTION = 0.02 * 3
AIR_DEF = 0.01 + 0.01 + 0.02
UPKEEP = -0.01
MIO_SIZE = 4
TRUC1_AIR_DEF, TRUC1_DETECTION_MAX = 0.06, 0.05
CAPS = {"accidents": -0.10, "detection": 0.20, "air_def": 0.20, "upkeep": -0.05}
HISTORICAL_TOTAL_RANGE = (2.8, 3.4)     # report 6.3: ~3.1
MATURE_BY = (2032, 12)

fails: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("PASS  " if ok else "FAIL  ") + msg)
    if not ok:
        fails.append(msg)


# ---------------------------------------------------------------- 1. money
print("== 1. Chi (ty USD) ==")
hist = 0.0
for p, evs in PILLARS.items():
    c = sum(OPTIONS[e]["a"][0] for e in evs)
    hist += c
    print(f"  {p:6s} historical {c:.2f}  cheapest {sum(min(v[0] for v in OPTIONS[e].values()) for e in evs):.2f}  dearest {sum(max(v[0] for v in OPTIONS[e].values()) for e in evs):.2f}")
print(f"  total historical {hist:.2f}")
check(HISTORICAL_TOTAL_RANGE[0] <= hist <= HISTORICAL_TOTAL_RANGE[1], f"historical total {hist:.2f} in {HISTORICAL_TOTAL_RANGE}")
check(max(v[0] for o in OPTIONS.values() for v in o.values()) <= 0.5, "no single programme above 0.5 bn")

# ---------------------------------------------------------------- 2. modifiers
print("\n== 2. Modifier (cong don, toan duong) ==")
print(f"  accidents {ACCIDENTS:+.2f}, detection {DETECTION:+.2f}, air_defence {AIR_DEF:+.2f}, upkeep {UPKEEP:+.2f}, MIO size +{MIO_SIZE}")
check(ACCIDENTS >= CAPS["accidents"], f"accidents {ACCIDENTS} >= cap {CAPS['accidents']}")
_f = open(os.path.join(ROOT, "common", "scripted_effects", "VIE_md_effects_air_ind.txt"), encoding="utf-8").read()
_m = re.search(r"VIE_apm_f2_reward = \{(.*?)\n\}", _f, re.S)
_focus_acc = sum(float(v) for v in re.findall(r"VIE_af_air_accidents_factor = ([-\d.]+)", _m.group(1))) if _m else 0
check(ACCIDENTS + _focus_acc >= CAPS["accidents"], f"accidents tiers {ACCIDENTS} + focus F2 {_focus_acc} >= cap {CAPS['accidents']}")
check(DETECTION + TRUC1_DETECTION_MAX <= CAPS["detection"], f"detection Truc 1+2 {DETECTION + TRUC1_DETECTION_MAX:.2f} <= {CAPS['detection']} (con cho Truc 3)")
check(AIR_DEF + TRUC1_AIR_DEF <= CAPS["air_def"], f"air_defence Truc 1+2 {AIR_DEF + TRUC1_AIR_DEF:.2f} <= {CAPS['air_def']}")
check(UPKEEP >= CAPS["upkeep"], f"upkeep {UPKEEP} >= {CAPS['upkeep']}")

# ---------------------------------------------------------------- 3. earliest finish with 2 slots
print("\n== 3. Lich som nhat voi 2 slot (duong lich su, option A) ==")
tasks = {}
for p, evs in PILLARS.items():
    for i, e in enumerate(evs):
        tasks[(p, i)] = OPTIONS[e]["a"][1]
finish: dict = {}
slots = [(0, 0), (0, 0)]  # month index when each slot frees
ym = lambda y, m: y * 12 + (m - 1)
free = [ym(2008, 1), ym(2008, 1)]
pending = sorted(tasks, key=lambda t: (EARLIEST[t[0]][t[1]], t))
while pending:
    ready = []
    for t in pending:
        p, i = t
        prev = finish.get((p, i - 1), ym(2008, 1)) if i else ym(2008, 1)
        dep = max([finish.get(d, 10 ** 9) for d in DEPENDS.get(t, [])] + [0])
        if i and (p, i - 1) not in finish:
            continue
        if dep >= 10 ** 9:
            continue
        start = max(ym(*EARLIEST[p][i]), prev, dep)
        ready.append((start, t))
    start, t = min(ready)
    k = min(range(2), key=lambda s: free[s])
    start = max(start, free[k])
    end = start + tasks[t]
    free[k] = end
    finish[t] = end
    pending.remove(t)
    print(f"  {t[0]:6s} tier {t[1] + 1}: {start // 12}-{start % 12 + 1:02d} -> {end // 12}-{end % 12 + 1:02d}")
last = max(finish.values())
print(f"  all pillars done by {last // 12}-{last % 12 + 1:02d}")
check(last <= ym(*MATURE_BY), f"full path done by {MATURE_BY[0]} (F7 opens 2027-01)")

# ---------------------------------------------------------------- 4. MIO
print("\n== 4. MIO ==")
fx_path = os.path.join(ROOT, "common", "scripted_effects", "VIE_md_effects_air_ind.txt")
ev_path = os.path.join(ROOT, "events", "VIE_air_ind.txt")
try:
    fx = open(fx_path, encoding="utf-8").read()
    ev = open(ev_path, encoding="utf-8").read()
except OSError:
    fx = ev = ""
    check(False, "cannot read code files")
if fx:
    # count MIO calls inside the *_finish effects only (not the helper definition)
    body = fx[fx.index("VIE_apm_a32_finish"):]
    n = len(re.findall(r"VIE_apm_viettel_mio_size = yes", body))
    check(n == MIO_SIZE, f"VIE_apm_viettel_mio_size called {n} times in finish effects (expected {MIO_SIZE})")

# ---------------------------------------------------------------- 5. code cross-check
print("\n== 5. Doi chieu event trong code ==")
if ev:
    blocks = re.split(r"\ncountry_event = \{", ev)[1:]
    code = {}
    for b in blocks:
        m = re.search(r"\n\tid = vie_air_ind\.(\d+)", b)
        if not m:
            continue
        n = int(m.group(1))
        opts = {}
        for ob in re.split(r"\n\toption = \{", b)[1:]:
            nm = re.search(r"name = vie_air_ind\.%d\.(\w)" % n, ob)
            c = re.search(r"set_temp_variable = \{ VIE_apm_cost = ([\d.]+) \}", ob)
            mo = re.search(r"set_temp_variable = \{ VIE_apm_months = (\d+) \}", ob)
            if nm and c and mo:
                opts[nm.group(1)] = (float(c.group(1)), int(mo.group(1)))
        if opts:
            code[n] = opts
    for n, want in OPTIONS.items():
        check(code.get(n) == want, f"event .{n}: code {code.get(n)} vs table {want}")
    check(set(code) == set(OPTIONS), "event set == table")

print()
if fails:
    print(f"{len(fails)} FAIL")
    sys.exit(1)
print("ALL PASS")
