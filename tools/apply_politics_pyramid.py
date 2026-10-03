import re
from pathlib import Path
import sys
sys.path.insert(0, ".")

focus_file = Path("common/national_focus/VIE_md_focus.txt")
txt = focus_file.read_text(encoding="utf-8")

from tools.optimize_politics_pyramid import layout
politics_abs = {k: (v[0] + 2, v[1]) for k, v in layout.items()}

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
print(f"Politics focuses to update: {len(politics_abs)}")

# Apply updates from bottom to top
new_txt = txt
for b in sorted(blocks, key=lambda x: x["start"], reverse=True):
    fid = b["id"]
    if fid in politics_abs:
        ax, ay = politics_abs[fid]
        rel_x = ax - 80
        rel_y = ay
        cur_block = b["block"]
        
        # Update relative_position_id = VIE_doi_moi_continues
        if "relative_position_id" in cur_block:
            updated_block = re.sub(r"(?m)^\t\trelative_position_id\s*=\s*\S+", "\t\trelative_position_id = VIE_doi_moi_continues", cur_block)
        else:
            # Insert relative_position_id after y = ...
            updated_block = re.sub(r"((?m)^\t\ty\s*=\s*-?\d+)", r"\1\n\t\trelative_position_id = VIE_doi_moi_continues", cur_block)
        
        # Update x = rel_x
        updated_block = re.sub(r"(?m)^\t\tx\s*=\s*-?\d+", f"\t\tx = {rel_x}", updated_block)
        # Update y = rel_y
        updated_block = re.sub(r"(?m)^\t\ty\s*=\s*-?\d+", f"\t\ty = {rel_y}", updated_block)
        
        new_txt = new_txt[:b["start"]] + updated_block + new_txt[b["end"]:]

focus_file.write_text(new_txt, encoding="utf-8")
print("Updated politics focuses in VIE_md_focus.txt successfully!")
