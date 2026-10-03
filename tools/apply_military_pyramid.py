import re
from pathlib import Path
import sys
sys.path.insert(0, ".")

focus_file = Path("common/national_focus/VIE_md_focus.txt")
txt = focus_file.read_text(encoding="utf-8")

from tools.test_military_pyramid import layout as mil_layout

# Parse focus blocks
pattern = re.compile(r"(?m)^\tfocus\s*=\s*\{")
matches = list(pattern.finditer(txt))

blocks = []
for m in matches:
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

print(f"Total blocks in file: {len(blocks)}")
print(f"Military focuses to update: {len(mil_layout)}")

# Apply updates from bottom to top to preserve character offsets
new_txt = txt
for b in sorted(blocks, key=lambda x: x["start"], reverse=True):
    fid = b["id"]
    if fid in mil_layout:
        ax, ay = mil_layout[fid]
        cur_block = b["block"]
        
        if fid == "VIE_modernize_vpa":
            rel_anchor = "VIE_doi_moi_continues"
            rel_x = ax - 80 # 202 - 80 = 122
            rel_y = ay # 1 - 0 = 1
        else:
            rel_anchor = "VIE_modernize_vpa"
            rel_x = ax - 202
            rel_y = ay - 1
            
        # Update or insert relative_position_id
        if "relative_position_id" in cur_block:
            updated_block = re.sub(
                r"(?m)^\t\trelative_position_id\s*=\s*\S+",
                f"\t\trelative_position_id = {rel_anchor}",
                cur_block
            )
        else:
            updated_block = re.sub(
                r"((?m)^\t\ty\s*=\s*-?\d+)",
                rf"\1\n\t\trelative_position_id = {rel_anchor}",
                cur_block
            )
        
        # Update x = rel_x
        updated_block = re.sub(r"(?m)^\t\tx\s*=\s*-?\d+", f"\t\tx = {rel_x}", updated_block)
        # Update y = rel_y
        updated_block = re.sub(r"(?m)^\t\ty\s*=\s*-?\d+", f"\t\ty = {rel_y}", updated_block)
        
        new_txt = new_txt[:b["start"]] + updated_block + new_txt[b["end"]:]

focus_file.write_text(new_txt, encoding="utf-8")
print("Updated military focuses in VIE_md_focus.txt successfully!")
