"""AI check for the three air-force event files: every event with choices keeps at least one option that the AI can pick.

Assumes VIE_ai_historical is always true and the AI is not bankrupt. Options whose only zero-weight modifier has an extra condition
(for example factor = 0 VIE_ai_historical = yes has_country_flag = X, paired with a trigger on the other option) are printed as
"conditional zero" and must be read by hand: the ones in vie_air_ind.13, .21 and vie_air_proc.11 are complementary to a trigger, so safe.

    python tools/audit/air_ai_options.py
"""
import os
import re
import sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
bad = 0
for f in ("events/VIE_air_force.txt", "events/VIE_air_ind.txt", "events/VIE_air_proc.txt"):
    t = open(f, encoding="utf-8").read().replace("\r\n", "\n")
    for blk in re.split(r"\ncountry_event = \{", t)[1:]:
        eid = re.search(r"\n\tid = (\S+)", blk).group(1)
        opts = re.split(r"\n\toption = \{", blk)[1:]
        if len(opts) < 2:
            continue
        alive = 0
        for ob in opts:
            name = re.search(r"name = (\S+)", ob).group(1)
            m = re.search(r"ai_chance = \{(.*?)\n\t\t\}", ob, re.S)
            if not m:
                print("NO ai_chance", eid, name)
                bad += 1
                continue
            ac = m.group(1)
            base = float(re.search(r"base = ([\d.]+)", ac).group(1)) if "base" in ac else 1
            add = sum(float(x) for x in re.findall(r"add = ([\d.]+)", ac))
            # AI: VIE_ai_historical is always true, not bankrupt
            zero = False
            for fm in re.findall(r"modifier = \{([^}]*)\}", ac):
                if "factor = 0" in fm and "has_active_mission" not in fm and "ai_has_high_deficit" not in fm:
                    conds = [c for c in re.findall(r"(\w+) = (?:yes|\w+)", fm.replace("factor = 0", "")) if c != "VIE_ai_historical"]
                    zero = zero or not conds                 # only VIE_ai_historical -> always zero
                    if conds:
                        print("  conditional zero", eid, name, fm.strip())
            gated = "\n\t\ttrigger = {" in ob.split("ai_chance")[0] or "\ttrigger = {" in ob.split("ai_chance")[0]
            ok = (base + add) > 0 and not zero
            print(("ok   " if ok else "ZERO ") + f"{eid:22s} {name:26s} base {base} add {add} zero {zero} trigger {gated}")
            if ok and not gated:
                alive += 1
        if alive == 0:
            print("!! NO ALWAYS-AVAILABLE WEIGHTED OPTION", eid)
            bad += 1
print("problems:", bad)
