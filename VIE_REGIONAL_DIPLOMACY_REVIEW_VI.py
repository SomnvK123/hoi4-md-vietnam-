"""B1 source extraction and baseline audit. Never writes political/game sources.

Run --init once before edits, then run without arguments to regenerate exports.
Exit 1 reports unfulfilled design invariants; it does not imply a Python error.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PLAN = "VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md"
POL = "VIETNAM_POLITICAL_PARAMETERS_VI.json"
REGISTRY = ROOT / "VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json"
REQUIRED = [
    PLAN, "VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.svg",
    "VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md", POL,
    "VIETNAM_POLITICAL_BALANCE_VI.py", "VIETNAM_POLITICAL_BALANCE_VI.csv",
    "VIETNAM_POLITICAL_NODE_CHOICES_VI.csv", "VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv",
    "VIETNAM_POLITICAL_CONSUMERS_VI.py", "VIETNAM_POLITICAL_CROSSCHECK_VI.py",
    "CHINA_POLITICS_DIPLOMACY_ARCHITECTURE_REPORT_VI.md",
]
PROTECTED = [p for p in REQUIRED if p != PLAN] + [
    "VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.png",
    "common/scripted_effects/VIE_md_effects_politics.txt",
    "common/scripted_effects/VIE_md_effects_politics_runtime.txt",
    "common/scripted_triggers/VIE_md_triggers_politics.txt",
    "common/scripted_triggers/VIE_md_triggers_politics_runtime.txt",
    "common/national_focus/VIE_md_focus.txt",
]


def read(name):
    return (ROOT / name).read_text(encoding="utf-8-sig")


def digest(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()


def section(text, number):
    match = re.search(rf"^(#{{2,4}}) {re.escape(number)}[. ]", text, re.M)
    if not match:
        raise ValueError(f"Missing section {number}")
    rest = text[match.end():]
    end = re.search(rf"^#{{2,{len(match[1])}}} ", rest, re.M)
    return text[match.start():match.end() + (end.start() if end else len(rest))]


def rows(text):
    return [[c.strip() for c in line.strip().strip("|").split("|")]
            for line in text.splitlines() if line.startswith("|")]


def row(text, number, prefix):
    hits = [r for r in rows(section(text, number)) if r[0].startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"Expected unique row {number}/{prefix}: {len(hits)}")
    return hits[0]


def nums(text):
    return [float(x.replace(",", ".")) for x in re.findall(r"[-+]?\d+(?:[,.]\d+)?", text)]


def initialize(text):
    entries = []

    def add(key, value, unit, source, refs, terms):
        entries.append(dict(id=key, value=value, unit=unit, source=source,
                            diplomacy_refs=refs.split(";"), search_terms=terms.split(";"),
                            status="proposal_from_existing_plan"))

    actions = [
        ("send", "Gửi đề nghị", "14.3;14.5;14.8;19.2;21.1", "gửi;đề nghị;phí gửi"),
        ("resend", "Sửa và gửi lại", "13.5;13.8;14.3;14.4;14.8;19.2;21.1", "gửi lại;sửa;phiên mới"),
        ("accept_partial", "Nhận phạm vi thu hẹp", "13.5;13.6;14.3;14.4;17.1;19.2;21.1", "thu hẹp;phạm vi"),
        ("start", "Bắt đầu sau đồng ý", "14.3;14.5;14.8;18.4;19.2;21.1", "bắt đầu;triển khai;hạn bắt đầu"),
        ("contingency_prepare", "Chuẩn bị dự phòng C", "14.3;14.7;14.8;17.1;19.2;21.1", "dự phòng;chuẩn bị"),
        ("contingency_use", "Kích hoạt dự phòng C", "14.7;14.8;20.2;21.1", "dự phòng;kích hoạt;ứng phó"),
        ("issue_dialogue", "Đối thoại xử lý", "14.6;14.8;19.2;21.1", "vướng mắc;đối thoại;phản hồi"),
        ("w_repair", "Sửa thực hiện W", "17.7;19.2;21.1;24.2", "sửa;yêu cầu bổ sung;gia hạn"),
        ("resume", "Nối lại chương trình", "14.6;19.2;20.3;21.1;24.2", "nối lại;tạm dừng;tháng"),
        ("cancel", "Rút/hủy", "5.2;14.5;18.4;19.2;21.1;24.2", "hủy;rút;hoàn"),
    ]
    for key, prefix, refs, terms in actions:
        r = row(text, "21.1", prefix)
        for col, field, unit in [(1, "pp", "PP"), (2, "treasury", "treasury_script_unit")]:
            v = nums(r[col])
            add(f"action.{key}.{field}", v[0] if v else None, unit, f"21.1/{prefix}/{field}", refs, terms)
        v = nums(r[3])
        if v:
            add(f"action.{key}.timer_days", v[0], "day", f"21.1/{prefix}/timer", refs, terms)
        if key == "w_repair":
            add("action.w_repair.max_per_run", 1 if "một lần" in r[3] else None, "count",
                "21.1/Sửa thực hiện W/một lần", refs, terms)
    for key, prefix, sub in [
        ("C", "C thương mại", "1"), ("M", "M dữ liệu", "2"), ("A", "A sáng kiến", "3"),
        ("B", "B cứu nạn", "4"), ("E", "E công nghệ", "5"), ("S", "S kỹ thuật", "6"), ("W", "W tiêu chuẩn", "7")
    ]:
        r = row(text, "21.2", prefix)
        for col, package in [(1, "small"), (2, "deep")]:
            v = nums(r[col])
            if len(v) != 3:
                raise ValueError(r)
            for value, field, unit in zip(v, ["treasury", "days", "monthly"],
                                          ["treasury_script_unit", "day", "treasury_script_unit/month"]):
                add(f"package.{key}.{package}.{field}", value, unit, f"21.2/{prefix}/{package}",
                    f"14.8;17.{sub};18.4;20.3;21.1;21.2;24.2", "gói;ngân khố;duy trì;triển khai")
    for key, prefix, unit, refs in [
        ("C.trade_targeted", "C thương mại", "targeted_trade_opinion", "14.2;17.1;20.1;20.2"),
        ("M.trade_targeted", "M kết nối", "targeted_trade_opinion", "17.2;20.1;20.2"),
        ("A.trade_national", "A sáng kiến", "national_trade_opinion", "17.3;20.1;20.2"),
        ("E.research_bonus_percent", "E công nghệ", "percent", "17.5;20.2;22.3"),
        ("EW.research_speed", "E/W đào tạo", "research_speed_factor", "17.5;17.7;20.1;20.2"),
        ("S.research_bonus_percent", "S hỗ trợ", "percent", "17.6;20.2;22.3"),
        ("W.trade_targeted", "W thị trường", "targeted_trade_opinion", "17.7;20.1;20.2"),
        ("C.issue_pp_factor", "Vướng mắc C", "political_power_factor", "14.6;14.7;17.1;20.2"),
        ("C.contingency_pp_factor", "Dự phòng C", "political_power_factor", "14.7;17.1;20.2"),
    ]:
        r = row(text, "20.2", prefix)
        for col, package in [(1, "small"), (2, "deep")]:
            add(f"reward.{key}.{package}", nums(r[col])[0], unit, f"20.2/{prefix}/{package}",
                refs, prefix + ";lợi ích;bonus;phạt")
        if "research_bonus" in key:
            add(f"reward.{key}.uses", nums(r[1])[1], "count", f"20.2/{prefix}/uses", refs, "lần dùng;nghiên cứu;bonus")
    add("reward.R1.maintain_cost_factor", nums(row(text, "20.2", "R1 mạng lưới")[1])[0],
        "improve_relations_maintain_cost_factor", "20.2/R1", "16;20.2;22.3", "R1;mạng lưới;duy trì quan hệ")
    add("reward.EW.duration", nums(row(text, "20.2", "E/W đào tạo")[3])[0], "day",
        "20.2/EW/lifetime", "20.2;22.3", "730;trao đổi;đào tạo")
    add("reward.C.issue_max_days", nums(row(text, "20.2", "Vướng mắc C")[3])[0], "day",
        "20.2/Vướng mắc C/lifetime", "14.6;14.7;20.2;21.1;24.2", "90;vướng mắc;thời hạn")
    focus_costs = sorted({int(r[2]) for r in rows(section(text, "16"))
                         if re.match(r"\*\*[RCMABESW]\d+ —", r[0])})
    add("focus.cost_values", focus_costs, "focus_cost", "16/catalog costs",
        "16;22.1;24.1", "Cost;cost;focus")
    for key, pattern, unit in [
        ("research", r"research speed tối đa \*\*\+([\d,]+)", "research_speed_factor"),
        ("trade_national", r"trade opinion quốc gia tối đa \*\*\+([\d,]+)", "trade_opinion_factor"),
        ("maintain_reduction", r"giảm duy trì quan hệ tối đa \*\*([\d,]+)", "reduction_magnitude"),
        ("trade_targeted", r"cùng một nước tối đa \*\*\+([\d,]+)", "targeted_trade_opinion"),
    ]:
        add("cap."+key, float(re.search(pattern, section(text, "20.2"))[1].replace(",", ".")), unit,
            "20.2/caps", "20.1;20.2;24.2", "trần;clamp;tối đa;cap")
    for key, pattern in [
        ("wide_quorum", r"(\d+) bên đồng ý cho khung rộng"),
        ("deep_quorum", r"(\d+) bên cho nhóm nhỏ"),
        ("invited", r"gồm \*\*(\d+) bên ngoài VIE"),
    ]:
        add("roster.A."+key, int(re.search(pattern, section(text, "17.3"))[1]), "country",
            "17.3/quorum", "17.3;21.2;22.3;24.2", "roster;ngưỡng;khung rộng;nhóm")
    add("roster.M.quorum", int(re.search(r"Ít nhất (\d+) nước", section(text, "17.2"))[1]), "country",
        "17.2/quorum", "17.2;21.2;22.3;24.2", "roster;hai bên;nước nhận")
    add("roster.M.bilateral_quorum", 1 if "hợp tác song phương dữ liệu" in section(text, "17.2") else None,
        "country", "17.2/bilateral fallback", "17.2;22.3", "song phương dữ liệu")
    add("implementation_slots", 2 if "**hai chương trình" in section(text, "18.2") else None, "program",
        "18.2/slots", "18.2;18.4;19.2;21.2;21.3;24.2", "slot;hai chương trình")
    add("network.min_regions", int(re.search(r"ít nhất (\d+) cụm", section(text, "22.3"))[1]), "region",
        "22.3/R1", "16;22.3;24.2", "ba cụm;3 cụm;R1")
    add("network.recognition_days", int(re.search(r"thử (\d+) ngày", section(text, "22.3"))[1]), "day",
        "22.3/recognition", "20.2;22.3;24.2", "730;ghi nhận;hết hạn")
    weights = re.search(r"base weight.*?\*\*([\d/]+)\*\*", section(text, "21.3"))[1]
    for key, value in zip(["accept", "amend", "refuse"], nums(weights)):
        add("ai.base_weight."+key, value, "relative_weight", "21.3/weights", "13.6;14.4;21.3;24.2",
            "weight;trọng số;phản hồi")
    political_keys = [
        "cohesion_price_bands", "sign_days", "prepare_days", "combined", "split", "override_cohesion",
        "bop_threshold", "bop_limits", "cohesion_initial", "cohesion_limits",
        "collective_full_extra", "collective_extra_cap", "outcome_cohesion",
        "cadre_cohesion_required", "tier_cap", "cadre_discount_pp",
        "low_cohesion_prepare_extra", "recovery", "congress_dates",
        "e104", "late_signature_windows", "contract_obligations", "e104_training",
        "k_values", "r_values", "cohesion_pp_rate", "accounting_days", "branch_pp_daily",
        "focus_days_per_cost", "tools", "action_days", "program_start_latest",
    ]
    units = {
        "cohesion_price_bands": "[cohesion lower, cohesion upper, PP multiplier]",
        "sign_days": "day, indexed by cadre tier",
        "prepare_days": "day, indexed by BoP zone",
        "k_values": "PP/treasury script unit, sensitivity only",
        "r_values": "PP/day", "cohesion_pp_rate": "PP/cohesion, accounting only",
        "bop_threshold": "BoP", "bop_limits": "BoP",
        "cohesion_initial": "cohesion", "cohesion_limits": "cohesion",
        "collective_full_extra": "cohesion", "collective_extra_cap": "cohesion",
        "outcome_cohesion": "cohesion", "cadre_cohesion_required": "cohesion",
        "tier_cap": "tier", "cadre_discount_pp": "PP, indexed by tier",
        "low_cohesion_prepare_extra": "day", "accounting_days": "day",
        "branch_pp_daily": "PP/day", "focus_days_per_cost": "day/focus_cost, paper assumption",
        "congress_dates": "date from source; no new historical claim",
        "action_days": "[standard days, fast days]",
        "tools": "[PP, treasury script unit]", "late_signature_windows": "day",
        "override_cohesion": "cohesion lost per override", "program_start_latest": "day",
    }
    for key in political_keys:
        entries.append(dict(id="politics."+key, source_file=POL, source_key=key,
                            unit=units.get(key,"mixed fields; keys name units, see political source"),
                            source=f"{POL}:parameters.{key}.value",
                            diplomacy_refs=["B1", "L1 (pending)", "L2 (not started)"],
                            search_terms=[key], status="read_only_reference"))
    return dict(schema="Diplomacy B1 baseline; L1 decisions pending",
                policy="Registry owns diplomacy proposals; political entries are live references. CSV/MD are generated views.",
                treasury_unit="chưa xác định trong JSON/tài liệu chính trị; k không phải tỷ giá engine",
                parameters=entries, protected_sha256={p: digest(p) for p in PROTECTED},
                original_plan_sha256=digest(PLAN))


def resolve(entry, politics):
    return politics["parameters"][entry["source_key"]]["value"] if "source_key" in entry else entry["value"]


def csv_out(name, records):
    with (ROOT/name).open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)


def l1_cohesion_analysis(values, p):
    """All discrete cohesion states; selected gate is a design, not game code."""
    def price(action, cohesion):
        factor = next(f for lo,hi,f in p["cohesion_price_bands"] if lo <= cohesion <= hi)
        return int((Decimal(str(values[f"action.{action}.pp"]))*Decimal(str(factor))).to_integral_value(rounding=ROUND_CEILING))
    records=[]
    threshold=p["cadre_cohesion_required"]
    recovery=p["recovery"]
    for cohesion in range(p["cohesion_limits"][0],p["cohesion_limits"][1]+1):
        current=cohesion
        pp=meetings=0
        while current<threshold:
            pp+=recovery["low_pp"] if current<recovery["low_below"] else recovery["pp"]
            meetings+=1
            current=min(p["cohesion_limits"][1],current+recovery["cohesion"])
        first_fee=recovery["low_pp"] if cohesion<recovery["low_below"] else recovery["pp"]
        restored=min(p["cohesion_limits"][1],cohesion+recovery["cohesion"])
        saved=price("send",cohesion)-price("send",restored)
        records.append(dict(cohesion=cohesion,send_pp=price("send",cohesion),resend_pp=price("resend",cohesion),
                            one_recovery_pp=first_fee,one_recovery_send_saved_pp=saved,
                            one_recovery_resend_saved_pp=price("resend",cohesion)-price("resend",restored),
                            one_send_net_after_recovery_pp=saved-first_fee,
                            sends_to_recoup_recovery=(first_fee+saved-1)//saved if saved else "",
                            deep_gate_available=int(cohesion>=threshold),target_cohesion=threshold,
                            recovery_count_to_gate=meetings,recovery_pp_to_gate=pp,
                            recovery_days_to_gate=(recovery["days"]+(meetings-1)*recovery["cooldown"]) if meetings else 0,
                            recovered_cohesion=current,status="approved_design_not_engine"))
    csv_out("VIE_REGIONAL_DIPLOMACY_L1_COHESION_STATES_VI.csv",records)
    bands=[]
    for lo,hi,factor in p["cohesion_price_bands"]:
        subset=[r for r in records if lo<=r["cohesion"]<=hi]
        span=lambda key: f"{min(r[key] for r in subset)}–{max(r[key] for r in subset)}"
        bands.append(dict(band=f"{lo}–{hi}",price_factor=factor,send_pp=subset[0]["send_pp"],
                          resend_pp=subset[0]["resend_pp"],
                          one_recovery_send_max_saved=max(r["one_recovery_send_saved_pp"] for r in subset),
                          one_recovery_resend_max_saved=max(r["one_recovery_resend_saved_pp"] for r in subset),
                          gate_eligible=sum(r["deep_gate_available"] for r in subset),
                          band_states=len(subset),recovery_count_range=span("recovery_count_to_gate"),
                          recovery_pp_range=span("recovery_pp_to_gate"),recovery_days_range=span("recovery_days_to_gate")))
    csv_out("VIE_REGIONAL_DIPLOMACY_L1_COHESION_BANDS_VI.csv",bands)
    spread=max(r["send_pp"] for r in records)-min(r["send_pp"] for r in records)
    initial=p["cohesion_initial"]
    after_override=initial-p["override_cohesion"]
    override=next(r for r in records if r["cohesion"]==after_override)
    csv_out("VIE_REGIONAL_DIPLOMACY_L1_OVERRIDE_VI.csv",[
        dict(initial=initial,override_cohesion_loss=p["override_cohesion"],after_override=after_override,
             threshold=threshold,deep_before=int(initial>=threshold),deep_after=int(after_override>=threshold),
             recovery_count=override["recovery_count_to_gate"],recovery_pp=override["recovery_pp_to_gate"],
             recovery_days=override["recovery_days_to_gate"],after_recovery=override["recovered_cohesion"],
             status="approved_design_not_engine")])
    output=["# L1 — Gate cohesion gói sâu C/E đã chọn","",
            "Nguồn: registry B1 và các khóa cohesion_price_bands, cadre_cohesion_required, recovery, cohesion_limits, cohesion_initial, override_cohesion trong JSON chính trị.",
            "Giá phí reader cũ chỉ là ứng viên đã bị rút khỏi kế hoạch áp dụng; bảng này giữ để kiểm lại kết luận.",
            f"Chênh toàn dải phí gửi: {max(r['send_pp'] for r in records)} − {min(r['send_pp'] for r in records)} = {spread} PP.",
            f"Một lượt phục hồi: tiết kiệm tối đa {max(r['one_recovery_send_saved_pp'] for r in records)} PP gửi hoặc {max(r['one_recovery_resend_saved_pp'] for r in records)} PP gửi lại; phí phục hồi lấy đúng JSON.",
            "Không suy từ chênh toàn dải sang lợi ích của một lần phục hồi. Nếu gom nhiều lần gửi có thể thu hồi phí phục hồi; chưa có batch/caller/lịch để chứng minh hành vi đó.",
            "Đã chọn (b): rút reader phí, giữ phí cơ sở B1 và thay bằng gate sâu C/E. Không áp gate này lên các cụm khác.",
            f"Gate thiết kế: cohesion hiện tại ≥ {threshold}; đọc trực tiếp cadre_cohesion_required, không thêm tham số.",
            "Kiểm ở soạn/gửi/gửi lại/bắt đầu và nâng gói; phản hồi chấp thuận vẫn được ghi, chờ phục hồi vẫn chịu hạn bắt đầu, sau start không hủy hay viết lại timer vì cohesion giảm.",
            "Tooltip trước: cohesion hiện tại/ngưỡng, gói nhỏ còn mở, phí/lịch phục hồi. Sau: gói đã chốt và chi phí đã trả.",
            "Phép thử bỏ gate: với cùng điều kiện khác, các trạng thái dưới ngưỡng chỉ chọn gói nhỏ/đợi phục hồi khi có gate, có thể gửi sâu ngay khi bỏ gate. Chưa chứng minh cân bằng hoặc đường hồi phục luôn kịp hạn.",
            "",
            "| Band | Hệ số | Phí gửi/gửi lại cũ | Tiết kiệm tối đa sau một phục hồi gửi/gửi lại | Trạng thái đạt gate/tổng | Số lượt để đạt | PP phục hồi | Ngày phục hồi |",
            "|---|---|---|---|---|---|---|---|"]
    for b in bands:
        output.append(f"| {b['band']} | {b['price_factor']} | {b['send_pp']}/{b['resend_pp']} | {b['one_recovery_send_max_saved']}/{b['one_recovery_resend_max_saved']} | {b['gate_eligible']}/{b['band_states']} | {b['recovery_count_range']} | {b['recovery_pp_range']} | {b['recovery_days_range']} |")
    output+=["","Giả định riêng của phép đạt gate: chọn phục hồi đầu tiên ngay, không có cooldown còn lại, không có thay đổi cohesion khác, đủ PP, chỉ dùng recovery purpose=cohesion.",
             "Ngày đạt với n lượt = recovery.days + (n−1)×recovery.cooldown; n=0 thì không đợi. Không tính số PP quy đổi là thu PP thật.",
             "Tất cả trạng thái nguyên trong cohesion_limits được xuất CSV; band chứa ngưỡng được tách theo giá trị thật, không giả tất cả cùng đạt.",
             "", "## Sau một lần vượt phản đối", "",
             f"Đọc nguồn: {initial} − {p['override_cohesion']} = {after_override}; {after_override} < {threshold} nên gói sâu bị khóa trước start.",
             f"Phục hồi tối thiểu: {override['recovery_count_to_gate']} lượt, {override['recovery_pp_to_gate']} PP, {override['recovery_days_to_gate']} ngày, cohesion lên {override['recovered_cohesion']} ≥ {threshold}.",
             "Không tính cohesion phục hồi thành PP thật; không đưa thêm phí ký/gửi vào khoản phục hồi. Cooldown còn lại hoặc biến động khác sẽ làm khác ngày đạt.",
             "Phép thử bỏ gate đổi tập lựa chọn gói sâu tại trạng thái sau vượt; gate giữ nguyên thì phải phục hồi/chọn gói nhỏ/chờ, không có gate thì không bị chặn vì cohesion.",
             "Đây là chứng cứ cho reader cohesion, không dùng để cho reader BoP hoặc tier hoãn PASS. Chưa chạy engine, chưa kiểm cân bằng."]
    (ROOT/"VIE_REGIONAL_DIPLOMACY_L1_CALCULATIONS_VI.md").write_text("\n".join(output)+"\n",encoding="utf-8")
    return dict(states=len(records),bands=len(bands),full_spread=spread,
                one_send_saved=max(r["one_recovery_send_saved_pp"] for r in records),
                gate_eligible=sum(r["deep_gate_available"] for r in records),override=override)


def graph_checks(text):
    catalog, layout, visual = {}, {}, {}
    for r in rows(section(text, "16")):
        m = re.match(r"\*\*([RCMABESW]\d+) — (.*?)\*\*", r[0])
        if m:
            catalog[m[1]] = dict(name=m[2], slug=r[1], cost=int(r[2]), prereq=r[3], available=r[4])
    for r in rows(section(text, "22.1")):
        if r[0] in catalog:
            # A comma separates coordinates; it is not a decimal separator here.
            point = lambda cell: tuple(map(int, re.findall(r"-?\d+", cell)))
            layout[r[0]] = dict(anchor=r[1], xy=point(r[2]), relative=point(r[3]))
    ns = {"s": "http://www.w3.org/2000/svg"}
    svg = ET.parse(ROOT/"VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.svg").getroot()
    errors = []
    for group in svg.findall("s:g", ns):
        title, rect = group.find("s:title", ns), group.find("s:rect", ns)
        if title is None or rect is None:
            continue
        m = re.fullmatch(r"([RCMABESW]\d+): (.*?) \| prerequisite: (.*?) \| (.*)", title.text)
        if not m:
            errors.append("unrecognized SVG title")
            continue
        n, name, prereq, available = m.groups()
        if n in visual:
            errors.append("duplicate SVG node "+n)
        visual[n] = dict(name=name, prereq=prereq, available=available,
                         label=" ".join(t.text or "" for t in group.findall("s:text",ns)[1:]),
                         center=(float(rect.get("x"))+float(rect.get("width"))/2,
                                 float(rect.get("y"))+float(rect.get("height"))/2))
    tokens = lambda s: set(re.findall(r"\b[RCMABESW]\d+\b", s))
    expected, actual = Counter(), Counter()
    for n, data in catalog.items():
        for parent in tokens(data["prereq"]):
            expected[(parent,n," OR " in data["prereq"])] += 1
    centers = {k:v["center"] for k,v in visual.items()}
    for path in svg.findall("s:path", ns):
        coords = nums(path.get("d"))
        if len(coords) != 4:
            errors.append("unsupported SVG path")
            continue
        a = [n for n,(x,y) in centers.items() if abs(x-coords[0])<.01 and abs(y+38-coords[1])<.01]
        b = [n for n,(x,y) in centers.items() if abs(x-coords[2])<.01 and abs(y-38-coords[3])<.01]
        if len(a)!=1 or len(b)!=1:
            errors.append("unresolved SVG edge")
        else:
            actual[(a[0],b[0],"or" in path.get("class","").split())] += 1
    if actual != expected:
        errors.append("SVG edges differ: "+str(actual-expected)+"/"+str(expected-actual))
    if len(catalog)!=51 or set(catalog)!=set(layout) or set(catalog)!=set(visual):
        errors.append("node counts/IDs differ")
    if len(set(c["slug"] for c in catalog.values()))!=len(catalog):
        errors.append("duplicate slug")
    for axis in (0,1):
        first = next(iter(layout))
        other = next(n for n in layout if layout[n]["xy"][axis]!=layout[first]["xy"][axis])
        scale = (centers[other][axis]-centers[first][axis])/(layout[other]["xy"][axis]-layout[first]["xy"][axis])
        offset = centers[first][axis]-scale*layout[first]["xy"][axis]
        for n in layout:
            if abs(centers[n][axis]-(layout[n]["xy"][axis]*scale+offset))>.01:
                errors.append("SVG position mismatch "+n)
    for n in set(catalog)&set(visual):
        if any(catalog[n][key]!=visual[n][key] for key in ("name","available")) or tokens(catalog[n]["prereq"])!=tokens(visual[n]["prereq"]):
            errors.append("SVG title mismatch "+n)
        if catalog[n]["name"] != visual[n]["label"]:
            errors.append("SVG visible label mismatch "+n)
    geometry, gaps, order = [], [], list(layout)
    for n,data in layout.items():
        parents = tokens(catalog[n]["prereq"])
        anchor = data["anchor"]
        if parents:
            if anchor not in parents or order.index(anchor)>=order.index(n):
                geometry.append("invalid/forward anchor "+n)
            if tuple(a-b for a,b in zip(data["xy"],layout[anchor]["xy"]))!=data["relative"]:
                geometry.append("relative mismatch "+n)
            if any(data["xy"][1]<=layout[p]["xy"][1] for p in parents):
                geometry.append("not below all parents "+n)
        elif data["relative"]!=data["xy"]:
            geometry.append("root mismatch "+n)
    for y in sorted({d["xy"][1] for d in layout.values()}):
        xs = sorted(d["xy"][0] for d in layout.values() if d["xy"][1]==y)
        gaps.extend(b-a for a,b in zip(xs,xs[1:]))
    if min(gaps)<2:
        geometry.append("horizontal gap below 2")
    return dict(counts=[len(catalog),len(layout),len(visual)],errors=errors,geometry=geometry,
                min_gap=min(gaps),anchors=len(layout)-1,edges=sum(expected.values()))


def l1_interface_checks(text,reg,p):
    source=read("common/scripted_effects/VIE_md_effects_politics.txt")
    min_term=min(map(int,re.findall(r"VIE_resolve_congress_(\d+)\s*=",source)))
    has_provider=all(s in source for s in ("set_country_flag = VIE_congress_resolved",
                                           "set_variable = { VIE_last_congress = "+str(min_term)+" }"))
    body=section(text,"19.4")
    root_expression=bool(re.search(
        r"OR\s*=\s*\{\s*has_completed_focus\s*=\s*VIE_publish_responsibility_rules\s*"
        r"has_country_flag\s*=\s*VIE_congress_resolved\s*\}",body))
    root_cases=[]
    for term in (min_term-1,min_term):
        for f02 in (False,True):
            for default in (False,True):
                for elapsed in (0,p["program_start_latest"]+1):
                    root_cases.append(dict(congress=term,f02=f02,default_congress=default,
                                           elapsed=elapsed,old_f02_lock=term>=min_term and f02,
                                           selected_root=term>=min_term and (f02 or default),
                                           scope="paper_root_contract_not_engine"))
    csv_out("VIE_REGIONAL_DIPLOMACY_L1_ROOT_CASES_VI.csv",root_cases)
    default_route=all(r["selected_root"] for r in root_cases if
                      r["congress"]==min_term and not r["f02"] and r["default_congress"])
    gate_sections=["14.2","14.3","14.8","17.5","19.2","19.4","21.2","21.3","24.2"]
    c_consumers=[s for s in gate_sections if
                 ("cadre_cohesion_required" in section(text,s) or "cohesion" in section(text,s))]
    ai=read("common/ai_strategy_plans/VIE_strategy_plans.txt")
    focus=read("common/national_focus/VIE_md_focus.txt")
    f02_part=re.search(r"id\s*=\s*VIE_publish_responsibility_rules(.*?)\n\s*focus\s*=",focus,re.S)[1]
    ai_weight=int(re.search(r"ai_will_do\s*=\s*\{\s*base\s*=\s*(\d+)",f02_part)[1])
    return dict(root_provider=has_provider,root_expression=root_expression,root_cases=len(root_cases),
                root_default_without_f02=default_route,cohesion_consumers=c_consumers,
                cohesion_consumers_expected=gate_sections,active_readers=reg["l1_review"]["active_readers"],
                deferred_readers=reg["l1_review"]["deferred_readers"],
                prepare_delta=p["prepare_days"]["balanced"]-p["prepare_days"]["central"],
                ai_f02_mentions=ai.count("VIE_publish_responsibility_rules"),ai_f02_base=ai_weight)


def run(reg, politics, text):
    if len({e["id"] for e in reg["parameters"]}) != len(reg["parameters"]):
        raise ValueError("Duplicate parameter ID; refusing a silent overwrite")
    values = {e["id"]:resolve(e,politics) for e in reg["parameters"]}
    csv_out("VIE_REGIONAL_DIPLOMACY_L1_B_RENAMES_VI.csv",reg["l1_review"]["b_rename_mapping"])
    exported, mentions = [], []
    for e in reg["parameters"]:
        exported.append(dict(parameter=e["id"],value=json.dumps(values[e["id"]],ensure_ascii=False),
                             unit=e["unit"],source=e["source"],diplomacy_refs=";".join(e["diplomacy_refs"]),
                             political_refs=politics["parameters"][e["source_key"]]["refs"] if "source_key" in e else "",status=e["status"]))
        current_section = ""
        if "source_key" in e:
            continue
        for lineno,line in enumerate(text.splitlines(),1):
            h = re.match(r"^#{2,4} (\d+(?:\.\d+)*)[. ]",line)
            if h:
                current_section=h[1]
            if any(current_section==ref or current_section.startswith(ref+".") for ref in e["diplomacy_refs"]):
                if any(term.casefold() in line.casefold() for term in e["search_terms"]):
                    mentions.append(dict(parameter=e["id"],section=current_section,line=lineno,
                                         match_kind="lexical_candidate_not_exhaustive_proof",text=line))
    csv_out("VIE_REGIONAL_DIPLOMACY_B1_PARAMETERS_VI.csv",exported)
    csv_out("VIE_REGIONAL_DIPLOMACY_B1_MENTIONS_VI.csv",mentions)
    g=graph_checks(text)
    changed=[p for p,h in reg["protected_sha256"].items() if digest(p)!=h]
    layout_metadata_changes=[]
    svg_name="VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.svg"
    import VIE_REGIONAL_DIPLOMACY_EXPORT_LAYOUT_VI as diagram
    svg=ET.fromstring(read(svg_name))
    geometry_unchanged=diagram.geometry_hash(svg)==reg["l1_review"]["svg_geometry_sha256"]
    png_matches=digest(diagram.PNG)==hashlib.sha256(diagram.render_png(svg)).hexdigest()
    if svg_name in changed and geometry_unchanged and not g["errors"]:
            layout_metadata_changes.append(svg_name)
            changed.remove(svg_name)
    if diagram.PNG in changed and geometry_unchanged and png_matches:
        layout_metadata_changes.append(diagram.PNG)
        changed.remove(diagram.PNG)
    current={e["id"]:resolve(e,politics) for e in initialize(text)["parameters"]}
    drift=[key for key in values if values[key]!=current[key]]
    p={k:e["value"] for k,e in politics["parameters"].items()}
    l1_results=l1_cohesion_analysis(values,p)
    interfaces=l1_interface_checks(text,reg,p)
    doc=read("VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md")
    sign_ok="/".join(map(str,p["sign_days"])) in section(doc,"5.2")
    bands_ok=all(f"| {lo}–{hi} | {factor:.2f} |" in section(doc,"3.3") for lo,hi,factor in p["cohesion_price_bands"])
    derived=[]
    for region in ("C","E"):
        for package in ("small","deep"):
            for k in p["k_values"]:
                for r in p["r_values"]:
                    treasury=values[f"package.{region}.{package}.treasury"]
                    monthly=values[f"package.{region}.{package}.monthly"]
                    pp=values["action.send.pp"]
                    equivalent=pp+treasury*k
                    derived.append(dict(region=region,package=package,k=k,r=r,pp=pp,treasury=treasury,monthly=monthly,
                                        converted_pp=equivalent,days=values[f"package.{region}.{package}.days"],
                                        monthly_converted_pp=monthly*k,pp_days_to_fund=equivalent/r,
                                        benefit_valuation="chưa định giá; không tính hoàn vốn",status="B1 current prices; not L2 model"))
    csv_out("VIE_REGIONAL_DIPLOMACY_B1_COSTS_VI.csv",derived)
    probes=[]
    for lo,hi,factor in p["cohesion_price_bands"]:
        for action in ("send","resend"):
            base=Decimal(str(values[f"action.{action}.pp"]))
            price=int((base*Decimal(str(factor))).to_integral_value(rounding=ROUND_CEILING))
            probes.append(dict(link="candidate_cohesion_price",action=action,source_band=f"{lo}..{hi}",
                               base_pp=str(base),factor=factor,derived_pp=price,status="retired_price_reader_not_applied"))
    csv_out("VIE_REGIONAL_DIPLOMACY_B1_READER_PROBES_VI.csv",probes)
    invariants=[]
    def inv(key,ok,evidence):
        invariants.append(dict(id=key,result="PASS" if ok else "FAIL",evidence=evidence,
                               scope=f"legacy_{g['counts'][0]}_node_baseline"))
    j1=(interfaces["root_provider"] and interfaces["root_expression"]
        and interfaces["root_default_without_f02"]
        and interfaces["cohesion_consumers"]==interfaces["cohesion_consumers_expected"])
    inv("J1",j1,f"Ba giao diện thiết kế G/P/C có writer, consumer, hiệu ứng và tooltip; root OR nguồn thật={interfaces['root_expression']}/{interfaces['root_provider']}; {len(interfaces['cohesion_consumers'])} mục C/E đọc gate. Không có script game ngoại giao mới; T tier/kiêm nhiệm hoãn, không tính active.")
    inv("J2",False,f"G có {interfaces['root_cases']} ca đối chứng đường mặc định/bỏ F02; C: {p['cohesion_initial']}−{p['override_cohesion']}={l1_results['override']['cohesion']}<{p['cadre_cohesion_required']}, phục hồi {l1_results['override']['recovery_pp_to_gate']}PP mở lại. P chỉ đổi chuẩn bị {interfaces['prepare_delta']} ngày, chưa chứng minh đổi lựa chọn. Người dùng chọn giữ lịch, J2 FAIL và L1 mở; không đổi định nghĩa.")
    inv("J3",not changed and not drift and sign_ok and bands_ok,
        f"Đọc JSON trực tiếp; bảng ký/bands khớp tài liệu={sign_ok}/{bands_ok}; drift={drift}; nguồn đổi={changed}.")
    gate_nodes=["C1","M1","A1","B1","E1","S1","W1"]
    catalog_rows={re.search(r"\*\*([RCMABESW]\d+)",r[0])[1]:r for r in rows(section(text,"16")) if re.match(r"\*\*[RCMABESW]\d+",r[0])}
    expected_gates=reg["l1_review"]["gate_review"]
    gated=[n for n in gate_nodes if
           re.search("≥"+re.escape(expected_gates[n].split(";")[0])+r"(?![IVX])",catalog_rows[n][4])
           and "giả định gameplay" in catalog_rows[n][4]]
    root_gate_ok=all(term in catalog_rows["R0"][4] for term in ("≥IX","F02 OR VIE_congress_resolved","giả định gameplay")) and interfaces["root_default_without_f02"]
    inv("J4",len(gated)==len(gate_nodes) and root_gate_ok,f"{len(gated)}/{len(gate_nodes)} cụm có đúng kỳ và nhãn giả định gameplay; R0 IX+(F02 OR mặc định)={root_gate_ok}. B1=X, S1=XIII với phạm vi tách XIII05–08; không coi là năm hình thành quan hệ.")
    inv("J5",False,"NỢ ĐÃ BIẾT: ownership biển/S-vs-XIII05–08/W-vs-X05–X08/hợp đồng ghi ngay trong plan 19.5. E104 chỉ có kế hoạch chuyển riêng19.6, sau C qua kiểm; chưa chuyển/kiểm thật nên J5 giữ FAIL.")
    inv("D1",False,"Chưa chứng minh mọi chương trình: C sâu có trade opinion cao hơn; quyền sâu E/S chưa có consumer đo được.")
    inv("D2",False,"Chưa có ngưỡng hoàn vốn người dùng chọn; trade opinion/research chưa định giá; gom PP không là hoàn vốn.")
    small=sum(values[f"package.{key}.small.monthly"] for key in "CMABESW")
    deep=sum(values[f"package.{key}.deep.monthly"] for key in "CMABESW")
    inv("D3",False,f"Đúng một chương trình/cụm: phí tháng nhỏ={small:.2f}, sâu={deep:.2f}; không có thu treasury. r là PP/ngày; M/E/W có thể nhiều chương trình.")
    inv("D4",False,f"Research: 3×{values['reward.EW.research_speed.deep']}={3*values['reward.EW.research_speed.deep']} chạm trần nếu đủ 3 nguồn. R1 duy nhất {abs(values['reward.R1.maintain_cost_factor'])} < trần {values['cap.maintain_reduction']}; chưa có nguồn thứ hai.")
    inv("D5",False,"Category/điều kiện/consumer riêng JAP/KOR và USA/SOV/RAJ chưa đủ; không so bằng tên lĩnh vực.")
    inv("D6",False,"Đã nhập k và công cụ chính trị; chưa có mô hình đủ phản hồi/hủy/vướng mắc hoặc lợi ích định giá.")
    inv("D7",True,"Đơn vị treasury trong tài liệu/JSON chính trị: chưa xác định; k chỉ là sensitivity, không là tỷ giá engine.")
    inv("D8",False,"Chưa định nghĩa đủ chiều có tác dụng; không dùng tên cờ cơ hội để tạo PASS.")
    inv("N1",False,"M/A/B/E/S/W chưa đủ bảy thành phần; dành L3, chưa viết lại.")
    inv("N2",False,"Chưa có event mới để thử lựa chọn rẻ nhất.")
    inv("N3",False,"Quyền hợp tác sâu E/S chưa có consumer chốt; không tính vào so thống trị.")
    inv("N4",False,"Chưa rà nguồn toàn tài liệu; không thêm mốc/nhân vật; các gate ứng viên ghi giả định gameplay.")
    inv("H1",not g["errors"],f"catalog/layout/SVG={g['counts']}; 49+2=51; edges={g['edges']}; errors={g['errors']}")
    inv("H2",False,"Mâu thuẫn cũ:14.3 A04 sau A02+A03,17.1 từ C4;14.6 chưa chọn duy trì,20.3 có phí tháng;11/14 còn nói chưa có số trong khi21 có bộ thử. Chờ L4.")
    inv("H3",not g["geometry"],f"{g['anchors']} anchor trước node/cha trực tiếp; relative=node-anchor; {g['edges']} cạnh con thấp hơn cha; min gap={g['min_gap']}>=2; errors={g['geometry']}.")
    inv("H4",True,"Chỉ Python/XML/CSV; chưa chạy HOI4, chưa playtest hay xác nhận cân bằng.")
    csv_out("VIE_REGIONAL_DIPLOMACY_INVARIANTS_VI.csv",invariants)
    expanded=reg.get("design_variants",{}).get("C_expanded",{}).get("nodes",[])
    if expanded:
        old_c=sum(bool(re.fullmatch(r"C\d+",key)) for key in catalog_rows)
        proposed=g["counts"][0]-old_c+len(expanded)
        scope_note=(f"**Phạm vi các kiểm dưới đây: baseline {g['counts'][0]} node trước mở rộng C.** "
                    f"Ứng viên C mới có {len(expanded)} node, toàn nhánh {proposed}; "
                    "[đặc tả và kiểm riêng](VIE_CHINA_EXPANDED_BRANCH_DESIGN_VI.md). "
                    "H1 PASS baseline không chứng nhận ứng viên mới hoặc SVG tổng mới; J2/J5 vẫn FAIL.")
    else:
        scope_note="Phạm vi: catalog baseline trong plan tổng."
    out=["# B1 — Bảng tham số duy nhất và kiểm baseline","",
         scope_note,"",
         "**L1 đã áp các lựa chọn vào thiết kế: gate sâu C/E, B1=X, S1=XIII, R0 dùng F02 hoặc mặc định đại hội. J2/J5 vẫn FAIL, chưa đóng L1 hoặc sang L2.** Không sửa gameplay/chính trị.","",
         "Nguồn chuẩn: [registry](VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json). Dòng politics.* tham chiếu JSON chính trị trực tiếp; không lưu bản số thứ hai.",
         "CSV/Markdown là bản sinh; sửa nguồn chuẩn rồi chạy lại script, không sửa tay bản xuất.",
         f"Đủ {len(REQUIRED)}/{len(REQUIRED)} file bắt buộc; chính trị có {len(p['focus_nodes'])} node. Bảo vệ {len(reg['protected_sha256'])} nguồn: thay đổi ngoài phạm vi={changed}.",
         f"Đối chiếu giá với bảng nguồn: drift={drift}; bảng ký/bands khớp tài liệu={sign_ok}/{bands_ok}.","",
         f"Đổi nhãn/export sơ đồ được yêu cầu: {layout_metadata_changes}; hình học giữ nguyên={geometry_unchanged}, PNG khớp render SVG={png_matches}.",
         "[Tính lại gate cohesion đã chọn](VIE_REGIONAL_DIPLOMACY_L1_CALCULATIONS_VI.md); [hồ sơ L1](VIE_REGIONAL_DIPLOMACY_L1_REVIEW_VI.md); [bảng bất biến Markdown](VIE_REGIONAL_DIPLOMACY_L1_INVARIANTS_VI.md).","",
         "Đơn vị treasury: **chưa xác định trong tài liệu/JSON chính trị**; k không phải tỷ giá engine.",
         "Ô treasury=null ở start/resume là tham chiếu giá gói/phí tháng, không phải 0.",
         "CSV mentions là các ứng viên tìm theo từ khóa ở mục sử dụng, chưa chứng minh mọi cách diễn đạt đã được tìm.","",
         "| Tham số | Giá trị | Đơn vị | Nguồn | Các mục sử dụng |","|---|---|---|---|---|"]
    for e in reg["parameters"]:
        out.append(f"| {e['id']} | {json.dumps(values[e['id']],ensure_ascii=False)} | {e['unit']} | {e['source']} | {'; '.join(e['diplomacy_refs'])} |")
    out += ["","## Số dẫn xuất","",
            f"- Đúng một chương trình/cụm: phí tháng nhỏ={small:.2f}; sâu={deep:.2f}. Đây không là tổng tối đa của hệ thống.",
            "- CSV costs: PP gửi + treasury triển khai × k; phí tháng riêng, chưa chọn horizon duy trì.",
            "- pp_days_to_fund = chi quy đổi / r là thời gian gom nguồn lực giả định, không phải hoàn vốn.",
            "- Không cộng branch_pp_daily chính trị vào r lần nữa khi chưa chốt baseline thu PP ngoại giao.",
            "- CSV reader_probes lưu phép tính reader phí đã bị rút, không áp theo cohesion. Gate sâu C/E đã chọn; các bảng band/override được sinh riêng.","",
            "| Bất biến | PASS/FAIL | Bằng chứng / giới hạn |","|---|---|---|"]
    out += [f"| {r['id']} | {r['result']} | {r['evidence']} |" for r in invariants]
    out += ["","FAIL bao gồm yêu cầu chưa hoàn thành/chưa đủ bằng chứng; không đồng nghĩa vừa sinh lỗi gameplay.",
            "Các mục D/N thuộc L2/L3 giữ FAIL, không đổi định nghĩa để PASS.","","## Tái tạo","",
            "Chạy: python -X utf8 VIE_REGIONAL_DIPLOMACY_REVIEW_VI.py",
            "Exit 1 khi còn bất biến FAIL; đọc diagnostics. Không chạy balance chính trị để ghi lại CSV.",
            "B1 chưa thay mô hình đủ kịch bản L2; trade opinion/research/cơ hội chưa được quy tùy ý ra PP."]
    (ROOT/"VIE_REGIONAL_DIPLOMACY_B1_VI.md").write_text("\n".join(out)+"\n",encoding="utf-8")
    checks=["# L1 — Bảng bất biến và kiểm bàn giao","",
            scope_note,"",
            "J1/J4 PASS ở mức hợp đồng thiết kế và phép tính, không chứng minh engine. J2 và J5 giữ FAIL; chưa đóng L1, chưa sang L2.",
            "", "| Bất biến | PASS/FAIL | Phép tính / bằng chứng |","|---|---|---|"]
    checks += [f"| {r['id']} | {r['result']} | {r['evidence']} |" for r in invariants]
    checks += ["",f"Catalog/layout/SVG={g['counts']}; {g['anchors']} anchor; {g['edges']} cạnh; gap nhỏ nhất={g['min_gap']}.",
               f"Hình học SVG so baseline không đổi={geometry_unchanged}; PNG xuất từ SVG khớp={png_matches}.",
               f"AI: focus F02 có base={interfaces['ai_f02_base']}; số tham chiếu F02 trong hai plan={interfaces['ai_f02_mentions']}. Trọng số không chứng minh AI luôn chọn.",
               f"Đường R0 bỏ F02 vẫn mở sau đại hội={interfaces['root_default_without_f02']}; chỉ đọc điều kiện nền, không kéo hạn programme sang ngoại giao.",
               "", "## Liên kết local hiện tại", ""]
    for name in [PLAN,"VIE_REGIONAL_DIPLOMACY_L1_REVIEW_VI.md"]:
        links=[t for t in re.findall(r"\]\(([^)]+)\)",read(name)) if not t.startswith(("http:","https:","#"))]
        targets={t.split("#")[0] for t in links}
        missing=[t for t in sorted(targets) if not (ROOT/t).is_file()]
        checks.append(f"- {name}: {len(links)} lần xuất hiện, {len(targets)} đích duy nhất; thiếu={missing}.")
    (ROOT/"VIE_REGIONAL_DIPLOMACY_L1_INVARIANTS_VI.md").write_text("\n".join(checks)+"\n",encoding="utf-8")
    print(json.dumps(dict(parameters=len(values),mentions=len(mentions),cost_rows=len(derived),reader_probes=len(probes),
                          graph=g,source_changed_outside_scope=changed,authorized_diagram_exports=layout_metadata_changes,
                          cohesion_analysis=l1_results,interfaces=interfaces,
                          invariants=dict(Counter(r["result"] for r in invariants))),ensure_ascii=False,indent=2))
    return all(r["result"]=="PASS" for r in invariants)


def self_test(text):
    """Falsify the graph checks in memory; no source or SVG is rewritten."""
    baseline=graph_checks(text)
    if baseline["errors"] or baseline["geometry"]:
        raise AssertionError("Cannot test rejection against a failing graph baseline")
    cases = [
        ("AND changed to OR", text.replace("C2 AND C3", "C2 OR C3", 1), "errors"),
        ("relative offset changed", text.replace("| C2 | C1 | (322,4) | (-4,2) |",
                                                "| C2 | C1 | (322,4) | (-3,2) |", 1), "geometry"),
        ("anchor not direct parent", text.replace("| C2 | C1 | (322,4)",
                                                 "| C2 | R0 | (322,4)", 1), "geometry"),
        ("horizontal gap below two", text.replace("| C2 | C1 | (322,4)",
                                                 "| C2 | C1 | (329,4)", 1), "geometry"),
        ("available differs from SVG", text.replace("| CHI hợp lệ; kỳ", "| CHI khác; kỳ", 1), "errors"),
    ]
    for name, mutated, field in cases:
        if mutated == text or not graph_checks(mutated)[field]:
            raise AssertionError("Audit failed to reject: " + name)
    print(f"Self-test: {len(cases)} deliberate graph faults rejected; no source writes")


def main():
    if hasattr(sys.stdout,"reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser()
    parser.add_argument("--init",action="store_true")
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--export-layout",action="store_true",help="Update document SVG labels and regenerate PNG")
    args=parser.parse_args()
    missing=sorted({p for p in REQUIRED+PROTECTED if not (ROOT/p).is_file()})
    if missing:
        raise SystemExit("STOP missing inputs: "+", ".join(missing))
    text=read(PLAN)
    if args.init:
        if REGISTRY.exists():
            raise SystemExit("STOP registry exists; refusing baseline reset")
        REGISTRY.write_text(json.dumps(initialize(text),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    reg=json.loads(REGISTRY.read_text(encoding="utf-8"))
    if args.export_layout:
        import VIE_REGIONAL_DIPLOMACY_EXPORT_LAYOUT_VI as diagram
        catalog={}
        for r in rows(section(text,"16")):
            m=re.match(r"\*\*([RCMABESW]\d+) — (.*?)\*\*",r[0])
            if m:
                catalog[m[1]]=dict(name=m[2],prereq=r[3],available=r[4])
        print(diagram.export_layout(ROOT,catalog,reg["l1_review"]["b_names"]))
    if args.self_test:
        self_test(text)
    return 0 if run(reg,json.loads(read(POL)),text) else 1


if __name__=="__main__":
    raise SystemExit(main())
