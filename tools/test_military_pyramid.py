import re
from pathlib import Path
from collections import defaultdict
import sys
sys.path.insert(0, ".")

txt = Path("common/national_focus/VIE_md_focus.txt").read_text(encoding="utf-8")
focuses = {}
for m in re.finditer(r"(?m)^\tfocus\s*=\s*\{", txt):
    start = m.start()
    brace = 1
    for i in range(m.end(), len(txt)):
        if txt[i] == '{': brace += 1
        elif txt[i] == '}':
            brace -= 1
            if brace == 0: end = i + 1; break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    prereqs = re.findall(r"\bprerequisite\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    mut = re.findall(r"\bmutually_exclusive\s*=\s*\{[^{}]*focus\s*=\s*(\S+)", block)
    focuses[fid] = {
        'id': fid, 'x': int(xm.group(1)) if xm else 0, 'y': int(ym.group(1)) if ym else 0,
        'rel': rel.group(1) if rel else None, 'prereqs': prereqs, 'mut': mut
    }

from tools.refine_categories import refine_categorize
mil_fids = [fid for fid, f in focuses.items() if refine_categorize(f) == 'QUAN_SU']
print(f"Total Military focuses: {len(mil_fids)}")

# Design Compact Symmetrical Military Pyramid
# Center = 204
# Apex: modernize_vpa at (204, 1)

layout = {
    # Apex
    "VIE_modernize_vpa": (202, 1),

    # ==================== ARMY (LỤC QUÂN) ====================
    # Row 2: Army root
    "VIE_lf_army_reform": (180, 2),

    # Row 3: Logistics & Basic training
    "VIE_lf_logistics_merge": (178, 3),
    "VIE_lf_basic_training": (182, 3),

    # Row 4: Arm Organization
    "VIE_lf_arm_infantry_org": (174, 4),
    "VIE_lf_arm_armor_org": (178, 4),
    "VIE_lf_arm_arty_org": (182, 4),
    "VIE_lf_arm_engineers": (186, 4),

    # Row 5: Arm Training & Combined Arms
    "VIE_lf_arm_infantry_train": (174, 5),
    "VIE_lf_arm_armor_train": (178, 5),
    "VIE_lf_arm_arty_train": (182, 5),
    "VIE_lf_combined_arms": (186, 5),

    # Row 6: Command Reform 1
    "VIE_lf_command_reform_1": (180, 6),

    # Row 7: Force Structure 1
    "VIE_lf_fs_mobile_force": (174, 7),
    "VIE_lf_fs_main_corps": (180, 7),
    "VIE_lf_fs_depth_defence": (186, 7),

    # Row 8: Force Structure 2
    "VIE_lf_fs_mobile_corps": (174, 8),
    "VIE_lf_fs_lean_corps": (180, 8),
    "VIE_lf_fs_militia_units": (186, 8),

    # Row 9: Development
    "VIE_lf_dev_strategic": (176, 9),
    "VIE_lf_dev_territorial": (184, 9),

    # Row 10: Command Reform 2
    "VIE_lf_command_reform_2": (180, 10),

    # Row 11: Capability Phase 1
    "VIE_lf_cap_border_urban": (174, 11),
    "VIE_lf_cap_army_ad": (180, 11),
    "VIE_lf_cap_cyber_ew": (186, 11),

    # Row 12: Capability Phase 2
    "VIE_lf_cap_area_control": (174, 12),
    "VIE_lf_cap_ad_coord": (180, 12),
    "VIE_lf_cap_info_ops": (186, 12),

    # Row 13: Selective Modernization
    "VIE_lf_selective_modernization": (180, 13),

    # Row 14: Command Reform 3
    "VIE_lf_command_reform_3": (180, 14),

    # Row 15: Capstone
    "VIE_lf_force_complete": (180, 15),

    # ==================== DEFENSE INDUSTRY (CNQP) ====================
    # Bridging between Army and Navy (X = 188..192)
    "VIE_def_industry_law": (190, 3),
    "VIE_military_enterprises_core": (188, 4),
    "VIE_military_enterprises_divest": (192, 4),
    "VIE_path_self_reliant_deterrence": (192, 5),

    # ==================== NAVY (HẢI QUÂN) ====================
    # Center spine around X = 202
    # Row 2: Navy root
    "VIE_nf_training_standardization": (202, 2),

    # Row 3: Surface, Submarine, Naval law
    "VIE_nf_surface_force": (198, 3),
    "VIE_nf_submarine_force": (202, 3),
    "VIE_naval_defence_law": (206, 3),

    # Row 4: Command reform 1 & Ba Son
    "VIE_nf_command_reform_1": (200, 4),
    "VIE_ba_son_shipyards": (206, 4),

    # Row 5: Small combatant & MRO
    "VIE_small_combatant_construction": (206, 5),
    "VIE_naval_mro": (204, 5),

    # Row 6: First force & Systems integration
    "VIE_nf_first_force": (200, 6),
    "VIE_naval_systems_integration": (206, 6),

    # Row 7: Command reform 2 & Naval defence 2030
    "VIE_nf_command_reform_2": (200, 7),
    "VIE_naval_defence_2030": (206, 7),

    # Row 8: Medium force
    "VIE_nf_medium_force": (200, 8),

    # Row 9: Operating range
    "VIE_nf_operating_range": (202, 9),

    # Row 10: Denial, Greenwater, Bluewater
    "VIE_nf_denial": (196, 10),
    "VIE_nf_greenwater": (202, 10),
    "VIE_nf_bluewater": (208, 10),

    # Row 11: Specific fleets
    "VIE_nf_denial_defence": (196, 11),
    "VIE_nf_regional_frigates": (200, 11),
    "VIE_nf_amphibious_fleet": (204, 11),
    "VIE_nf_ocean_escort": (206, 11),
    "VIE_nf_replenishment": (208, 11),
    "VIE_nf_naval_aviation": (210, 11),

    # Row 12: Capital ships & Denial subs
    "VIE_nf_denial_subs": (196, 12),
    "VIE_nf_lhd_program": (202, 12),
    "VIE_nf_carrier_group": (208, 12),

    # Row 13: Capstones
    "VIE_nf_denial_command": (196, 13),
    "VIE_nf_regional_command": (202, 13),

    # ==================== AIR FORCE (PK-KQ) ====================
    # Right wing around X = 222 (compacted from width 24 down to 18)
    # Row 2: Air Force root
    "VIE_airf_training_standardization": (222, 2),

    # Row 3: Fighter, SAM, APM law
    "VIE_airf_fighter_force": (216, 3),
    "VIE_airf_sam_force": (222, 3),
    "VIE_apm_law": (228, 3),

    # Row 4: Command reform 1 & APM projects
    "VIE_airf_command_reform_1": (218, 4),
    "VIE_apm_a32": (224, 4),
    "VIE_apm_a31": (228, 4),
    "VIE_apm_radar": (232, 4),

    # Row 5: First force
    "VIE_airf_first_force": (218, 5),

    # Row 6: Command reform 2 & APM integration/uav
    "VIE_airf_command_reform_2": (218, 6),
    "VIE_apm_integration": (226, 6),
    "VIE_apm_uav": (230, 6),

    # Row 7: Medium force
    "VIE_airf_medium_force": (218, 7),

    # Row 8: Operating range & APM mature
    "VIE_airf_operating_range": (218, 8),
    "VIE_apm_mature": (228, 8),

    # Row 9: IADS, Multirole, Unmanned
    "VIE_airf_iads": (214, 9),
    "VIE_airf_multirole": (220, 9),
    "VIE_airf_unmanned": (230, 9),

    # Row 10: 6 pillars of air power
    "VIE_airf_layered_defence": (214, 10),
    "VIE_airf_multirole_fleet": (218, 10),
    "VIE_airf_sustainment": (222, 10),
    "VIE_airf_airlift_tanker": (226, 10),
    "VIE_airf_isr_uav": (230, 10),
    "VIE_airf_datalink": (234, 10),

    # Row 11: EW, Multirole wing, Strike UAV
    "VIE_airf_ew_antistealth": (214, 11),
    "VIE_airf_multirole_wing": (220, 11),
    "VIE_airf_strike_uav": (230, 11),

    # Row 12: IADS Command & Teaming
    "VIE_airf_iads_command": (214, 12),
    "VIE_airf_teaming": (230, 12),
}

print(f"Total mapped: {len(layout)} / {len(mil_fids)}")
missing = set(mil_fids) - set(layout.keys())
print(f"Missing: {missing}")

# Check Duplicates
coords = defaultdict(list)
for fid, (x, y) in layout.items():
    coords[(x, y)].append(fid)

dups = {k: v for k, v in coords.items() if len(v) > 1}
print(f"Duplicates: {len(dups)}")
for k, v in dups.items():
    print(f"  Collision at {k}: {v}")

# Check Gaps < 2
by_y = defaultdict(list)
for fid, (x, y) in layout.items():
    by_y[y].append((x, fid))

bad_gaps = []
for y, items in sorted(by_y.items()):
    items.sort()
    for i in range(len(items) - 1):
        x1, f1 = items[i]
        x2, f2 = items[i+1]
        if x2 - x1 < 2:
            bad_gaps.append((y, f1, x1, f2, x2, x2 - x1))
print(f"Gaps < 2: {len(bad_gaps)}")
for g in bad_gaps:
    print(" ", g)

# Check Upward arrows
upward = []
long_jumps = []
for fid, (cx, cy) in layout.items():
    for p in focuses[fid]["prereqs"]:
        if p in layout:
            px, py = layout[p]
            if cy <= py:
                upward.append((p, fid, py, cy, cy - py))
            dx = abs(cx - px)
            if dx > 8:
                long_jumps.append((p, fid, dx))

print(f"Upward arrows (dy <= 0): {len(upward)}")
for u in upward:
    print(f"  Upward: {u[0]} (y={u[2]}) -> {u[1]} (y={u[3]}), dy={u[4]}")

print(f"Long jumps (dx > 8): {len(long_jumps)}")
for j in long_jumps:
    print(f"  Long jump dx={j[2]}: {j[0]} -> {j[1]}")

xs = [v[0] for v in layout.values()]
ys = [v[1] for v in layout.values()]
print(f"\nNEW MILITARY BOUNDS: X=[{min(xs)}, {max(xs)}] (w={max(xs)-min(xs)}) | Y=[{min(ys)}, {max(ys)}] (h={max(ys)-min(ys)})")
