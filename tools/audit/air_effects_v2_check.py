"""Scratch check for air effects v2 (will become tools/audit/air_force_balance.py section 1-3)."""
from collections import defaultdict
from itertools import product

CAPS = {"exp": 10, "atk": 10, "sup": 10, "cas": 10, "mis": 16, "rng": 20, "det": 20, "home": 20, "int": 8, "pers": 6,
        "ace": 10, "night": 6, "wx": 6}
OTHER = {"det": 11}
W = {"atk": 1, "sup": 1, "cas": .8, "mis": 1, "int": .8, "home": .8, "det": .8, "rng": .6, "exp": .5, "ace": .8,
     "night": 1, "wx": .8, "pers": -1}

# (kept, new) per node, percent. 'night'/'wx' stored as positive magnitude of improvement.
N = {
 "T1": ({"exp": 4}, {"ace": 3}), "T2": ({"atk": 1}, {"ace": 2}), "T3": ({"home": 2}, {}),
 "T4": ({"mis": 2}, {"night": 1}), "T5": ({}, {}), "T6": ({"mis": 2, "det": 1}, {}),
 "T7": ({"rng": 3}, {"wx": 1}), "T8": ({"rng": 4, "det": 1}, {}),
 "A1": ({"home": 2}, {"int": .5, "rng": -2, "ace": 1.5}), "A2": ({"det": 2, "home": 2}, {"wx": 1, "sup": 1.5}),
 "A3": ({"int": 3, "det": 2}, {"night": 1, "wx": 1, "sup": 1}), "A4": ({"mis": 2, "home": 2}, {"night": 1, "atk": 1}),
 "B1": ({"rng": 4}, {"wx": 1, "pers": 2, "ace": 1}), "B2": ({"atk": 3, "sup": 2, "cas": 2}, {}),
 "B3": ({"mis": 2}, {"wx": 2, "night": 1, "pers": -1}), "B4": ({"rng": 3}, {}),
 "B5": ({"mis": 2, "atk": 2}, {"ace": 2}),
 "C1": ({"det": 1}, {"home": -1, "ace": 1.5, "night": .5}), "C2": ({"det": 3}, {"night": 1.5, "wx": 1}), "C3": ({"mis": 2}, {"wx": 1, "sup": 1}),
 "C4": ({"atk": 3}, {"rng": 1}), "C5": ({"mis": 2, "int": 2}, {"ace": 1, "night": 1}),
}
T6_DIR = {0: {}, 1: {"int": 1}, 2: {"int": .5, "rng": .5, "night": .5}, 3: {"rng": 1}}
B2_SPEC = {"sup": {"sup": 1}, "gnd": {"cas": 1}}
MS1 = {"ace": 1}            # ms1 2011-06 for every player
CHAIN = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
BR = {"A": ["A1", "A2", "A3", "A4"], "B": ["B1", "B2", "B3", "B4", "B5"], "C": ["C1", "C2", "C3", "C4", "C5"]}
CAP = {"A": "A4", "B": "B5", "C": "C5"}
# unchanged decisions (from air_force_balance.py)
D_A = {"sup": {"sup": 3}, "gnd": {"cas": 3, "atk": 1}}
D_B = {"home": 3, "det": 1}; D_B_EARLY = {"home": 1}
D_C = [{"mis": 2}, {"home": 2, "sup": 2}, {"det": 1, "mis": 2}]
D_D = {1: {"int": 3, "home": 2, "rng": -3}, 2: {"atk": 1, "int": 1, "rng": 1}, 3: {"rng": 5, "mis": 2, "pers": 3}}


def add(d, s, m=1.0):
    for k, v in s.items():
        d[k] += v * m


def node(n, which=("k", "n")):
    k, nw = N[n]
    out = defaultdict(float)
    if "k" in which: add(out, k)
    if "n" in which: add(out, nw)
    return out


def total(br, spec, prio, lvl, early, new=True):
    d = defaultdict(float)
    for n in CHAIN + BR[br]:
        add(d, node(n, ("k", "n") if new else ("k",)))
    if new:
        add(d, T6_DIR[prio]); add(d, MS1)
        if br == "B": add(d, B2_SPEC[spec])
    add(d, D_A[spec], 1.5 if lvl == 2 else 1); add(d, D_B, 1.5 if lvl == 2 else 1)
    if early: add(d, D_B_EARLY)
    for s in D_C: add(d, s)
    add(d, D_D[prio])
    add(d, node(CAP[br], ("k",)), .5 if lvl == 2 else .25)
    if (br == "A" and prio == 1) or (br in "BC" and prio == 3): d["mis"] += 1
    return d


def worst(br, new=True):
    mx = defaultdict(float)
    for spec, prio, lvl, early in product(("sup", "gnd"), (1, 2, 3), (1, 2), (False, True)):
        for k, v in total(br, spec, prio, lvl, early, new).items():
            mx[k] = max(mx[k], v)
    return mx


print("== tong lon nhat moi nhanh (Truc 3 + truc khac), tran, %tran ==")
bad = 0
for br in "ABC":
    old, new = worst(br, False), worst(br, True)
    print(f"-- nhanh {br}")
    for k, cap in CAPS.items():
        v = new[k] + OTHER.get(k, 0)
        flag = "PASS" if v <= cap + 1e-9 else "FAIL"
        bad += flag == "FAIL"
        print(f"  {k:5} cu {old[k] + OTHER.get(k, 0):6.2f} -> moi {v:6.2f} / {cap:3}  {v / cap * 100:5.1f}%  {flag}")
print("FAIL" if bad else "ALL PASS", bad)

print("\n== diem rong tung node (chi modifier, trong so W) ==")
tot = defaultdict(float)
for n, (k, nw) in N.items():
    sc = sum(W[t] * v for t, v in {**{}, **{a: k.get(a, 0) + nw.get(a, 0) for a in set(k) | set(nw)}}.items())
    old = sum(W[t] * v for t, v in k.items())
    print(f"  {n}: cu {old:4.1f} -> moi {sc:4.1f}")
    tot[n[0] if n[0] in "ABC" else "T"] += sc
print({k: round(v, 1) for k, v in tot.items()})
# T6 direction extras
for p, s in T6_DIR.items():
    print("  T6 dir", p, round(sum(W[t] * v for t, v in s.items()), 2))
