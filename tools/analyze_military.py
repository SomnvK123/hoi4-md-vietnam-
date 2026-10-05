import re

with open("common/national_focus/VIE_md_focus.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos = 0
focuses = {}
focus_list = []
while True:
    m = re.search(r"\bfocus\s*=\s*\{", text[pos:])
    if not m:
        break
    start = pos + m.start()
    depth = 0
    i = pos + m.end() - 1
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                block = text[start:i+1]
                id_m = re.search(r"^\s*id\s*=\s*([a-zA-Z0-9_]+)", block, re.MULTILINE)
                x_m = re.search(r"^\s*x\s*=\s*(-?\d+)", block, re.MULTILINE)
                y_m = re.search(r"^\s*y\s*=\s*(-?\d+)", block, re.MULTILINE)
                rel_m = re.search(r"^\s*relative_position_id\s*=\s*([a-zA-Z0-9_]+)", block, re.MULTILINE)
                prereqs = re.findall(r"prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}", block)
                avail = re.findall(r"has_completed_focus\s*=\s*([a-zA-Z0-9_]+)", block)
                if id_m:
                    fid = id_m.group(1)
                    f_data = {
                        "id": fid,
                        "x": int(x_m.group(1)) if x_m else 0,
                        "y": int(y_m.group(1)) if y_m else 0,
                        "rel": rel_m.group(1) if rel_m else None,
                        "prereqs": prereqs,
                        "avail": avail,
                        "order": len(focus_list)
                    }
                    focuses[fid] = f_data
                    focus_list.append(f_data)
                pos = i + 1
                break
        i += 1
    else:
        break

def get_abs(fid, visited=None):
    if visited is None:
        visited = set()
    if fid in visited:
        return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f["rel"]:
        return (f["x"], f["y"])
    px, py = get_abs(f["rel"], visited)
    return (px + f["x"], py + f["y"])

for f in focus_list:
    f["abs_x"], f["abs_y"] = get_abs(f["id"])

vpa_subtree = []
queue = ["VIE_modernize_vpa"]
visited_vpa = set(["VIE_modernize_vpa"])
while queue:
    curr = queue.pop(0)
    vpa_subtree.append(curr)
    for f in focus_list:
        if f["rel"] == curr or curr in f["prereqs"]:
            if f["id"] not in visited_vpa:
                visited_vpa.add(f["id"])
                queue.append(f["id"])

categories = {}
for fid in vpa_subtree:
    if fid.startswith("VIE_lf_"):
        cat = "Luc quan (VIE_lf_)"
    elif fid.startswith("VIE_nf_"):
        cat = "Hai quan (VIE_nf_)"
    elif fid.startswith("VIE_airf_"):
        cat = "Khong quan (VIE_airf_)"
    elif fid.startswith("VIE_msl_"):
        cat = "Ten lua & Ran de (VIE_msl_)"
    elif fid.startswith("VIE_def_"):
        cat = "Cong nghiep quoc phong (VIE_def_)"
    elif "apm" in fid:
        cat = "Phong khong - May bay (APM)"
    elif "naval" in fid or "ba_son" in fid or "shipyards" in fid:
        cat = "Hai quan bo sung / Dong tau"
    else:
        cat = "Goc & Chien luoc tong the"
    categories.setdefault(cat, []).append(fid)

md_out = ["# Phân tích Hiện trạng Nhánh Quân sự (VIE_modernize_vpa - 92 Focus)\n\n"]
md_out.append(f"Tổng số focus: **{len(vpa_subtree)}**\n")
md_out.append(f"Tọa độ bao quát: x = {min(focuses[f]['abs_x'] for f in vpa_subtree)} .. {max(focuses[f]['abs_x'] for f in vpa_subtree)}, y = {min(focuses[f]['abs_y'] for f in vpa_subtree)} .. {max(focuses[f]['abs_y'] for f in vpa_subtree)}\n\n")

for cat in sorted(categories.keys()):
    fids = categories[cat]
    md_out.append(f"## {cat} ({len(fids)} focuses)\n\n")
    md_out.append("| Focus ID | x (abs) | y (abs) | relative_position_id | prerequisite | available |\n")
    md_out.append("|---|:---:|:---:|---|---|---|\n")
    for fid in fids:
        f = focuses[fid]
        rel = f['rel'] or '-'
        pr = ", ".join(f['prereqs']) or '-'
        av = ", ".join(f['avail']) or '-'
        md_out.append(f"| `{fid}` | {f['abs_x']} | {f['abs_y']} | `{rel}` | {pr} | {av} |\n")
    md_out.append("\n")

with open("VIE_military_current_tree_analysis.md", "w", encoding="utf-8") as f:
    f.writelines(md_out)

print("Wrote analysis to VIE_military_current_tree_analysis.md")
