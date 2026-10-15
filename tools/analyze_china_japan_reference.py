"""Read one actual MD branch; export evidence without changing game/design sources.

Run: python -X utf8 tools/analyze_china_japan_reference.py --md D:/ide/Millennium-Dawn
This is a structural source analysis, not a HOI4 interpreter or balance model.
"""
import argparse
import csv
import hashlib
import itertools
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/china_japan_reference"
TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|#[^\n]*|>=|<=|!=|[{}=<>]|[^\s{}=<>#]+')


def parse(text):
    tokens = [(m.group(), m.start(), m.end()) for m in TOKEN.finditer(text)
              if not m.group().startswith("#")]
    pos = 0

    def block(nested=False):
        nonlocal pos
        result = []
        while pos < len(tokens) and tokens[pos][0] != "}":
            key, start, end = tokens[pos]
            pos += 1
            if pos < len(tokens) and tokens[pos][0] in {"=", ">", "<", ">=", "<=", "!="}:
                op = tokens[pos][0]
                pos += 1
                value, _, end = tokens[pos]
                pos += 1
                if value == "{":
                    value = block(True)
                    end = tokens[pos - 1][2]
                result.append(dict(key=key, op=op, value=value, start=start, end=end))
            else:
                result.append(dict(key=key, op=None, value=None, start=start, end=end))
        if nested:
            if pos >= len(tokens) or tokens[pos][0] != "}":
                raise ValueError("Unclosed block")
            pos += 1
        return result

    result = block()
    if pos != len(tokens):
        raise ValueError("Unmatched closing brace")
    return result


def fields(nodes, key):
    return [n for n in nodes if n["key"] == key]


def one(nodes, key, default=None):
    matches = fields(nodes, key)
    if not matches:
        return default
    if len(matches) != 1:
        raise ValueError(f"Repeated field {key}")
    return matches[0]["value"]


def walk(nodes):
    for node in nodes:
        yield node
        if isinstance(node["value"], list):
            yield from walk(node["value"])


def raw(text, node):
    return text[node["start"]:node["end"]]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def csv_write(name, records):
    with (OUT / name).open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--md", type=Path, required=True)
    args = ap.parse_args()
    probe = parse('log = "keep # and { braces }" # ignore }\n prerequisite = { focus = A focus = B }')
    assert one(probe, "log") == '"keep # and { braces }"'
    assert [n["value"] for n in one(probe, "prerequisite")] == ["A", "B"]
    paths = {
        "focus": "common/national_focus/05_china.txt",
        "events": "events/05_china.txt",
        "decisions": "common/decisions/05_CHI_decisions.txt",
        "categories": "common/decisions/categories/99_CHI_decision_categories.txt",
        "ideas": "common/ideas/05_china.txt",
        "modifiers": "common/dynamic_modifiers/99_CHI_dynamic_modifiers.txt",
        "influence": "common/scripted_triggers/00_influence_scripted_triggers.txt",
    }
    missing = [str(args.md / p) for p in paths.values() if not (args.md / p).is_file()]
    if missing:
        raise SystemExit("Missing required sources: " + "; ".join(missing))
    protected = list(args.md / p for p in paths.values()) + [
        ROOT / "VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md",
        ROOT / "VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json",
        ROOT / "VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md",
        ROOT / "VIETNAM_POLITICAL_PARAMETERS_VI.json",
        ROOT / "CHINA_POLITICS_DIPLOMACY_ARCHITECTURE_REPORT_VI.md",
    ]
    before = {str(p): sha(p) for p in protected}
    texts = {key: (args.md / p).read_text(encoding="utf-8-sig") for key, p in paths.items()}
    trees = {key: parse(text) for key, text in texts.items()}
    all_focus = [n for n in walk(trees["focus"]) if n["key"] == "focus" and isinstance(n["value"], list) and one(n["value"], "id")]
    by_id = {one(n["value"], "id"): n for n in all_focus}
    ids = list(by_id)
    start = ids.index("CHI_the_japan_question")
    end = ids.index("CHI_Form_the_SCO", start)
    selected = ids[start:end]
    assert len(selected) == 18, selected
    memo = {}

    def position(fid, chain=()):
        if fid in chain:
            raise ValueError("Anchor cycle: " + str(chain))
        if fid not in memo:
            body = by_id[fid]["value"]
            x, y = int(one(body, "x")), int(one(body, "y"))
            anchor = one(body, "relative_position_id")
            if anchor:
                ax, ay = position(anchor, chain + (fid,))
                x, y = x + ax, y + ay
            memo[fid] = x, y
        return memo[fid]

    labels = {fid: f"J{i:02}" for i, fid in enumerate(selected, 1)}
    records, edges, issues = [], [], []
    row_x = defaultdict(list)
    for fid in selected:
        node = by_id[fid]
        b = node["value"]
        groups = [[n["value"] for n in fields(p["value"], "focus")] for p in fields(b, "prerequisite")]
        mutex = [n["value"] for p in fields(b, "mutually_exclusive") for n in fields(p["value"], "focus")]
        anchor = one(b, "relative_position_id")
        xy = position(fid)
        parents = [p for g in groups for p in g]
        row_x[xy[1]].append((xy[0], fid))
        if anchor not in parents:
            issues.append(dict(type="anchor_not_direct_parent", focus=fid, anchor=anchor))
        for parent in parents:
            if position(parent)[1] >= xy[1]:
                issues.append(dict(type="child_not_below_parent", focus=fid, parent=parent))
            edges.append(dict(parent=parent, child=fid, logic="OR" if any(parent in g and len(g) > 1 for g in groups) else "AND"))
        records.append(dict(label=labels[fid], id=fid, line=texts["focus"].count("\n", 0, node["start"]) + 1,
                            cost=int(one(b, "cost", 10)), anchor=anchor, x=int(one(b, "x")), y=int(one(b, "y")),
                            absolute_x=xy[0], absolute_y=xy[1],
                            prerequisites=json.dumps(groups), mutex=json.dumps(mutex),
                            available="\n".join(raw(texts["focus"], n) for n in fields(b, "available"))))
    gaps = []
    for y, pairs in row_x.items():
        pairs.sort()
        for a, b in zip(pairs, pairs[1:]):
            gaps.append(b[0] - a[0])
            if b[0] - a[0] < 2:
                issues.append(dict(type="gap_below_2", row=y, left=a[1], right=b[1], gap=b[0] - a[0]))
    decisions_node = next(n for n in trees["decisions"] if n["key"] == "CHI_japan_strategy")
    decisions = []
    for n in decisions_node["value"]:
        if not isinstance(n["value"], list):
            continue
        b = n["value"]
        decisions.append(dict(id=n["key"], line=texts["decisions"].count("\n", 0, n["start"]) + 1,
                              allowed=raw(texts["decisions"], fields(b, "allowed")[0]) if fields(b, "allowed") else "",
                              pp=one(b, "cost", "engine_default"), days_remove=one(b, "days_remove", ""),
                              cooldown=one(b, "days_re_enable", ""), source=raw(texts["decisions"], n)))
    tables = []
    for fid in ["CHI_the_senkaku_crisis", "CHI_the_tokyo_communique"]:
        body = by_id[fid]["value"]
        groups = [[n["value"] for n in fields(p["value"], "focus")] for p in fields(body, "prerequisite")]
        count = next(n for n in walk(one(body, "available")) if n["key"] == "count_triggers")
        count_ids = [n["value"] for n in fields(count["value"], "has_completed_focus")]
        amount = int(one(count["value"], "amount"))
        for bits in itertools.product([False, True], repeat=len(count_ids)):
            completed = {i for i, bit in zip(count_ids, bits) if bit}
            pre_ok = all(any(p in completed for p in g) for g in groups)
            count_ok = sum(bits) >= amount
            pressure_values = [False, True] if fid.endswith("senkaku_crisis") else [False]
            for pressure in pressure_values:
                tables.append(dict(focus=fid, axes="".join(str(int(bit)) for bit in bits),
                                   prerequisites_pass=int(pre_ok), count_pass=int(count_ok),
                                   pressure_alternative=int(pressure),
                                   structural_gate_pass=int(pre_ok and (count_ok or pressure)),
                                   assumption="all other external gates satisfied; no bypass; not engine"))
    evidence = {}
    event_ids = {"CHI_foreign." + str(i) for i in [200,201,202,204,211,213,215,217,220,221,222,223,224,226,227,231,244,250]}
    for key, tree in trees.items():
        if key == "focus":
            nodes = [by_id[fid] for fid in selected]
        elif key == "decisions":
            nodes = decisions_node["value"]
        elif key == "events":
            nodes = [n for n in tree if isinstance(n["value"], list) and one(n["value"], "id") in event_ids]
        else:
            nodes = [n for n in walk(tree) if isinstance(n["value"], list) and
                     (n["key"].startswith(("CHI_jap", "CHI_sez_japanese", "CHI_sino_japanese", "CHI_rare_earth", "JAP_china", "JAP_sino", "CHI_coast_guard")) or
                      n["key"] in {"CHI_japan_strategy", "influence_higher_70", "sender_influence_higher_70"})]
        evidence[key] = [dict(key=n["key"], line=texts[key].count("\n", 0, n["start"]) + 1,
                              source=raw(texts[key], n)) for n in nodes]
    assert all(sha(p) == before[str(p)] for p in protected)
    OUT.mkdir(parents=True, exist_ok=True)
    csv_write("focus.csv", records)
    csv_write("decisions.csv", decisions)
    csv_write("gate_truth_table.csv", tables)
    def required_path(fid):
        result = {fid}
        b = by_id[fid]["value"]
        for group in fields(b, "prerequisite"):
            parents = [n["value"] for n in fields(group["value"], "focus")]
            if len(parents) != 1:
                raise ValueError("Route cost requires a chosen OR path")
            parent = parents[0]
            if parent in selected:
                result.update(required_path(parent))
        return result
    route_costs = []
    for endpoint in ["CHI_the_senkaku_crisis", "CHI_the_tokyo_communique"]:
        route = required_path(endpoint) | {"CHI_break_the_first_island_chain"}
        route_costs.append(dict(endpoint=endpoint, nodes=len(route),
                                cost=sum(int(one(by_id[f]["value"], "cost", 10)) for f in route),
                                assumption="from Japan root through capstone; focus cost only; excludes external root/decisions/wait/availability"))
    csv_write("route_costs.csv", route_costs)
    result = dict(md_root=str(args.md.resolve()), source_sha256={paths[k]: before[str(args.md / paths[k])] for k in paths},
                  total_focus_in_source=len(all_focus), selected_focus=len(selected),
                  mutex_pairs=sorted({tuple(sorted((fid, other))) for fid in selected for other in json.loads(next(r["mutex"] for r in records if r["id"] == fid))}),
                  prerequisite_edges=len(edges), focus_cost_sum=sum(r["cost"] for r in records),
                  decision_count=len(decisions), min_row_gap=min(gaps), geometry_findings=issues,
                  route_costs=route_costs, parser_string_comment_probe="PASS",
                  readonly_sources_unchanged=True, evidence=evidence)
    (OUT / "evidence.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Trung–Nhật — dữ liệu trích từ code", "", "Chỉ kiểm cấu trúc; không mô phỏng HOI4.", "",
             "| Mã | ID thật | Cost | Anchor | x/y tương đối | X/Y tuyệt đối | Prerequisite (AND giữa nhóm, OR trong nhóm) |",
             "|---|---|---:|---|---|---|---|"]
    for r in records:
        groups = json.loads(r["prerequisites"])
        pre = " AND ".join("(" + " OR ".join(labels.get(i, i) for i in g) + ")" for g in groups)
        lines.append(f"| {r['label']} | {r['id']} | {r['cost']} | {labels.get(r['anchor'], r['anchor'])} | ({r['x']},{r['y']}) | ({r['absolute_x']},{r['absolute_y']}) | {pre} |")
    lines += ["", "```mermaid", "flowchart TD", '    ROOT["Ngoại giao khu vực CHI"]']
    for fid in selected:
        lines.append(f'    {labels[fid]}["{labels[fid]}: {fid.removeprefix("CHI_")}"]')
    for edge in edges:
        lines.append(f"    {labels.get(edge['parent'], 'ROOT')} -->|{edge['logic']}| {labels[edge['child']]}")
    for a, b in result["mutex_pairs"]:
        lines.append(f"    {labels[a]} -. mutex .- {labels[b]}")
    lines += ["```", "", "Mermaid thể hiện quan hệ; vị trí vẽ tự động không là tọa độ engine. Tọa độ thật ở bảng/CSV.", "",
              "## Kiểm hình học nguồn", "", "Không áp tiêu chuẩn VIE ngược thành khẳng định nguồn MD đã đạt chuẩn.", ""]
    for finding in issues:
        lines.append("- " + json.dumps(finding, ensure_ascii=False))
    (OUT / "extracted_layout.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "evidence"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
