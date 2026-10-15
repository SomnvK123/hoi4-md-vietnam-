"""Export the expanded C proposal from the existing diplomacy registry.

Only document artifacts are written. The legacy plan is read as a baseline for
the other regions; no HOI4 content, historical source or economic value changes.
"""
import csv
import hashlib
import itertools
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from VIE_REGIONAL_DIPLOMACY_REVIEW_VI import rows, section

OUT = ROOT / "artifacts/vie_china_expanded"
REGISTRY = ROOT / "VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json"


def csv_write(name, records):
    with (OUT / name).open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def main():
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    variant = reg["design_variants"]["C_expanded"]
    params = {e["id"]: e for e in reg["parameters"]}
    costs = params[variant["cost_source"]]["value"]
    text = (ROOT / "VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md").read_text(encoding="utf-8")
    protected = [ROOT / p for p in reg["protected_sha256"]]
    protected += [REGISTRY, ROOT / "VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md"]
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    before = {str(p.relative_to(ROOT)): sha(p) for p in protected}
    legacy, old_layout = {}, {}
    for r in rows(section(text, "16")):
        match = re.fullmatch(r"\*\*([RCMABESW]\d+) — (.*?)\*\*", r[0])
        if not match:
            continue
        key, name = match.groups()
        groups = [] if r[3] == "Root" else [re.findall(r"[RCMABESW]\d+", part) for part in r[3].split(" AND ")]
        legacy[key] = dict(key=key, name=name, cost=int(r[2]), pre=groups, mutex=[], slug=r[1].strip("`"))
    for r in rows(section(text, "22.1")):
        if r[0] not in legacy:
            continue
        old_layout[r[0]] = dict(anchor=None if r[1] == "Không" else r[1],
                                xy=list(map(int, re.findall(r"-?\d+", r[2]))))
    old_c = {key for key in legacy if re.fullmatch(r"C\d+", key)}
    nodes = {}
    for key, old in legacy.items():
        if key in old_c:
            continue
        nodes[key] = dict(old, **old_layout[key])
        if key == "R0":
            for new in variant["nodes"]:
                nodes[new["key"]] = dict(new, cost=costs[new["cost_index"]], mutex=new.get("mutex", []))
    r1 = nodes["R1"]
    r1["pre"] = [[variant["r1_replace_old_c_final"] if p == "C6" else p for p in group] for group in r1["pre"]]
    order = list(nodes)
    errors, edges, layout = [], [], []
    row_x = defaultdict(list)
    for key, node in nodes.items():
        parents = [p for g in node["pre"] for p in g]
        anchor = node["anchor"]
        if parents:
            if anchor not in parents or order.index(anchor) >= order.index(key):
                errors.append("anchor invalid/forward: " + key)
            rel = [a - b for a, b in zip(node["xy"], nodes[anchor]["xy"])]
        else:
            rel = node["xy"]
        for group in node["pre"]:
            for parent in group:
                if parent not in nodes:
                    errors.append("missing parent: " + parent)
                    continue
                if nodes[parent]["xy"][1] >= node["xy"][1]:
                    errors.append("child not below parent: " + key)
                edges.append((parent, key, "OR" if len(group) > 1 else "AND"))
        for other in node.get("mutex", []):
            if key not in nodes[other].get("mutex", []):
                errors.append("asymmetric mutex: " + key)
        row_x[node["xy"][1]].append((node["xy"][0], key))
        layout.append(dict(key=key, anchor=anchor or "", absolute_x=node["xy"][0], absolute_y=node["xy"][1], x=rel[0], y=rel[1]))
    gaps = []
    for row in row_x.values():
        row.sort()
        gaps.extend(b[0] - a[0] for a, b in zip(row, row[1:]))
    if min(gaps) < 2:
        errors.append("gap below 2")
    c_nodes = variant["nodes"]
    c_keys = [n["key"] for n in c_nodes]
    reachable, capstone_without_policy, both_policy = 0, 0, 0
    for bits in itertools.product([False, True], repeat=len(c_keys)):
        completed = {k for k, bit in zip(c_keys, bits) if bit} | {"R0"}
        valid = all(
            all(any(p in completed for p in group) for group in n["pre"])
            and not any(m in completed for m in n.get("mutex", []))
            for n in c_nodes if n["key"] in completed
        )
        if not valid:
            continue
        reachable += 1
        capstone_without_policy += "C18" in completed and not ({"C05", "C06"} & completed)
        both_policy += {"C05", "C06"}.issubset(completed)
    if capstone_without_policy or both_policy:
        errors.append("invalid reachable policy route")
    cases = []
    for gate in ["C13", "C15", "C17", "C18"]:
        node = nodes[gate]
        parents = sorted({p for group in node["pre"] for p in group})
        for bits in itertools.product([False, True], repeat=len(parents)):
            done = {p for p, bit in zip(parents, bits) if bit}
            passed = all(any(p in done for p in g) for g in node["pre"])
            cases.append(dict(gate=gate, completed=json.dumps(sorted(done)), prerequisite_pass=int(passed),
                              scope="direct gate only; available/result/finance not simulated"))
    if len({n["slug"] for n in nodes.values()}) != len(nodes):
        errors.append("duplicate slug")
    unchanged_other = all(nodes[k]["xy"] == old_layout[k]["xy"] and nodes[k]["cost"] == legacy[k]["cost"]
                          and nodes[k]["name"] == legacy[k]["name"]
                          and (k == "R1" or nodes[k]["pre"] == legacy[k]["pre"])
                          for k in legacy if k not in old_c)
    if not unchanged_other:
        errors.append("unintended other-region change")
    summary = dict(legacy_total=len(legacy), legacy_c=len(old_c), proposed_c=len(c_nodes),
                   proposed_total=len(nodes), delta=len(c_nodes)-len(old_c), global_edges=len(edges),
                   min_row_gap=min(gaps), checked_completion_subsets=2**len(c_keys),
                   reachable_structural_states=reachable, capstone_without_policy=capstone_without_policy,
                   both_policies_completed=both_policy, economic_parameters_added=0,
                   unpriced_programs=variant["unpriced_programs"], geometry_errors=errors,
                   other_region_layout_cost_names_unchanged=unchanged_other,
                   legacy_svg_is_expanded_diagram=False, engine_tested=False,
                   c_catalog_cost=sum(nodes[k]["cost"] for k in c_keys))
    after = {str(p.relative_to(ROOT)): sha(p) for p in protected}
    summary["protected_files_unchanged_during_run"] = before == after
    assert before == after
    OUT.mkdir(parents=True, exist_ok=True)
    catalog = [dict(key=n["key"], name=n["name"], slug=n["slug"], cost=n["cost"],
                    prerequisites=json.dumps(n["pre"]), mutex=json.dumps(n.get("mutex", [])),
                    role=n.get("role", "legacy baseline"), available=n.get("gate", "legacy baseline")) for n in nodes.values()]
    csv_write("catalog.csv", [r for r in catalog if r["key"] in c_keys])
    csv_write("global_catalog.csv", catalog)
    csv_write("layout.csv", [r for r in layout if r["key"] in c_keys])
    csv_write("global_layout.csv", layout)
    csv_write("gate_cases.csv", cases)
    mermaid = ["flowchart TD", '    R0["R0 · Ngoại giao khu vực"]']
    mermaid += [f'    {n["key"]}["{n["key"]} · {n["name"]}"]' for n in c_nodes]
    mermaid += [f"    {p} -->|{logic}| {c}" for p, c, logic in edges if c in c_keys]
    mermaid += ['    C05 -. "mutex: chỉ chế độ giao thương" .- C06']
    (OUT / "graph.mmd").write_text("\n".join(mermaid) + "\n", encoding="utf-8")
    md = ["# Catalog và layout cụm C mở rộng — bản sinh", "",
          f"Nguồn: registry B1 design_variants.C_expanded. C: {len(old_c)} → {len(c_nodes)}; toàn nhánh: {len(legacy)} − {len(old_c)} + {len(c_nodes)} = {len(nodes)}.", "",
          "ID mới đều là đề xuất, chưa có provider game. AND giữa nhóm prerequisite; OR trong nhóm.", "",
          "| Node | Tên / slug mới dự kiến | Cost | Prerequisite | Mutex | Quyền/kết quả | Available |",
          "|---|---|---:|---|---|---|---|"]
    for n in c_nodes:
        pre = " AND ".join("(" + " OR ".join(g) + ")" for g in n["pre"])
        md.append(f"| {n['key']} | {n['name']} / VIE_rd_{n['slug']} | {nodes[n['key']]['cost']} | {pre} | {','.join(n.get('mutex', [])) or '—'} | {n['role']} | {n['gate']} |")
    md += ["", "```mermaid", *mermaid, "```", "",
           "Mermaid tự bố trí; tọa độ đề xuất thật nằm ở bảng dưới. Chưa kiểm hộp tên/dây/icon trong HOI4.", "",
           "| Node | Anchor | X/Y tuyệt đối | x/y tương đối |", "|---|---|---|---|"]
    for r in layout:
        if r["key"] in c_keys:
            md.append(f"| {r['key']} | {r['anchor']} | ({r['absolute_x']},{r['absolute_y']}) | ({r['x']},{r['y']}) |")
    md += ["", "## Kiểm đã chạy", "", "```json", json.dumps(summary, ensure_ascii=False, indent=2), "```", "",
           "H1 nguyên văn yêu cầu 51 node và SVG khớp: FAIL cho bản mở rộng; người dùng đã bỏ trần C nhưng chưa có SVG tổng mới. Không đổi định nghĩa để PASS.",
           "H2 vẫn FAIL vì bản tổng cũ chưa hợp nhất. H3 PASS nếu geometry_errors rỗng; chỉ hình học node/anchor, chưa kiểm đường dây đi qua hộp.",
           "J2/J5 giữ FAIL theo hồ sơ L1. D2/D3 và cân bằng nội dung mới chưa đủ dữ liệu; hai chương trình mới chưa định giá."]
    (OUT / "catalog_and_layout.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (OUT / "checks.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
