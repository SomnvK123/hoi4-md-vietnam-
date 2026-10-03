import re
from pathlib import Path

focus_file = Path("common/national_focus/VIE_md_focus.txt")
txt = focus_file.read_text(encoding="utf-8")

# Parse all focus blocks
pattern = re.compile(r"(?m)^\tfocus\s*=\s*\{")
matches = list(pattern.finditer(txt))

blocks = []
for i, m in enumerate(matches):
    start = m.start()
    brace = 1
    for j in range(m.end(), len(txt)):
        if txt[j] == '{': brace += 1
        elif txt[j] == '}':
            brace -= 1
            if brace == 0:
                end = j + 1
                break
    block = txt[start:end]
    fid = re.search(r"\bid\s*=\s*(\S+)", block).group(1)
    xm = re.search(r"\bx\s*=\s*(-?\d+)", block)
    ym = re.search(r"\by\s*=\s*(-?\d+)", block)
    rel = re.search(r"\brelative_position_id\s*=\s*(\S+)", block)
    blocks.append({
        "id": fid,
        "x": int(xm.group(1)) if xm else 0,
        "y": int(ym.group(1)) if ym else 0,
        "rel": rel.group(1) if rel else None,
        "block": block,
        "start": start,
        "end": end
    })

bmap = {b["id"]: b for b in blocks}

# Define new (x, y) coordinates for target focuses
new_coords = {}

# 1. ĐỐI NGOẠI:
# Root: VIE_asean_integration -> x = -34, y = 12
new_coords["VIE_asean_integration"] = (-34, 12)
# All children of VIE_asean_integration: shift x by -14
for b in blocks:
    if b["rel"] == "VIE_asean_integration":
        new_coords[b["id"]] = (b["x"] - 14, b["y"])

# 2. BIỂN ĐÔNG:
# Root: VIE_law_of_the_sea -> x = -4, y = 13
new_coords["VIE_law_of_the_sea"] = (-4, 13)
# All children of VIE_law_of_the_sea except peacekeeping and four nos: shift x by +3
for b in blocks:
    if b["rel"] == "VIE_law_of_the_sea" and b["id"] not in ["VIE_un_peacekeeping", "VIE_four_nos_doctrine"]:
        new_coords[b["id"]] = (b["x"] + 3, b["y"])

# Bridge peacekeeping & four nos inside Biển Đông (under peoples_defence at 77):
new_coords["VIE_un_peacekeeping"] = (5, 5)
new_coords["VIE_four_nos_doctrine"] = (5, 6)

# 3. AN NINH NỘI ĐỊA:
sec_shifts = {
    "VIE_sec_cyber_control": (13, 13),
    "VIE_sec_surveillance_network": (11, 14),
    "VIE_sec_public_order": (13, 14),
    "VIE_sec_security_economy": (15, 14),
    "VIE_sec_cyber_sovereignty": (11, 15),
    "VIE_sec_loyalty_vetting": (13, 15),
    "VIE_sec_border_control": (15, 15),
    "VIE_sec_managed_opening": (13, 16)
}
new_coords.update(sec_shifts)

# 4. QUÂN SỰ:
# modernize_vpa at apex abs 206 (rel 126 from doi_moi)
new_coords["VIE_modernize_vpa"] = (126, 1)
# Army: abs 180 -> rel_x = -26, y = 2
new_coords["VIE_lf_army_reform"] = (-26, 2)
# Navy: abs 198 -> rel_x = -8, y = 2
new_coords["VIE_nf_training_standardization"] = (-8, 2)
# Air Force: abs 218 -> rel_x = 12, y = 1
new_coords["VIE_airf_training_standardization"] = (12, 1)

print(f"Total focuses to update: {len(new_coords)}")

# Reconstruct file with updated coordinates
new_txt = txt
# Replace from bottom to top to preserve character offsets
for b in sorted(blocks, key=lambda x: x["start"], reverse=True):
    fid = b["id"]
    if fid in new_coords:
        nx, ny = new_coords[fid]
        cur_block = b["block"]
        
        # Replace x = ...
        updated_block = re.sub(r"(?m)^\t\tx\s*=\s*-?\d+", f"\t\tx = {nx}", cur_block)
        # Replace y = ...
        updated_block = re.sub(r"(?m)^\t\ty\s*=\s*-?\d+", f"\t\ty = {ny}", updated_block)
        
        new_txt = new_txt[:b["start"]] + updated_block + new_txt[b["end"]:]

focus_file.write_text(new_txt, encoding="utf-8")
print("Updated VIE_md_focus.txt successfully!")
