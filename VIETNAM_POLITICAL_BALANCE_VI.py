"""Rebuild the paper model from B1. No HOI4 engine or game files are used."""

import argparse
import csv
import hashlib
import itertools
import json
import math
import re
from datetime import date
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARAMS = ROOT / "VIETNAM_POLITICAL_PARAMETERS_VI.json"
DOC = ROOT / "VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md"
CSV = ROOT / "VIETNAM_POLITICAL_BALANCE_VI.csv"
SEQUENCES = {"cadre": ["training", "training", "succession", "review"],
             "administration": ["administration_project", "administration_project", "review"],
             "inspection": ["audit_standard", "audit", "audit", "review"],
             "social": ["local_project", "local_project", "review"]}


def e104_contract_amendment_gate(contract):
    """One ledger query for XIII12 available and tooltip; no engine trigger is installed."""
    remaining = max(0, contract['support_promised'] - contract['support_received'] - contract['support_forfeited'])
    unused = set(contract['rights_granted']) - set(contract['rights_used']) - set(contract['rights_revoked'])
    return {'unreceived_support': remaining, 'unused_cooperation_rights': len(unused),
            'amend_available': int(remaining > 0 or bool(unused)), 'cancel_available': 1,
            'reason': '' if remaining > 0 or unused else 'hỗ trợ chưa nhận=0; quyền chưa dùng=0; sửa không giữ được lợi ích',
            'cancel_effect': 'đóng nghĩa vụ tương lai; mất hỗ trợ chưa nhận và quyền chưa dùng; không fail mission hoặc thu hồi thưởng'}


def paper_cancel_e104_contract(contract):
    """Paper transition touches only the E104 ledger, preserving all paid/used history."""
    before=e104_contract_amendment_gate(contract)
    after=dict(contract)
    after['support_forfeited']+=before['unreceived_support']
    after['rights_revoked']=sorted(set(contract['rights_revoked']) | (set(contract['rights_granted'])-set(contract['rights_used'])))
    after['contract_state']='terminated'
    return after


def forecast_programme_completion(p, program, route, mode, cohesion, e102="NA", e103="NA",
                                  rejection_known=False, signed_base_days=None,
                                  elapsed_congress_days=0, recovery_cooldown_remaining=0,
                                  pending_recovery_remaining=None):
    """Single paper counterpart of the design trigger; an uncertain rejection is not a lock."""
    if program is None or mode is None:
        programmes=list(SEQUENCES) if program is None else [program]
        candidates={}
        for candidate_program in programmes:
            paths=[]
            for candidate_mode in p['focus_commitment_gate']['forecast_modes']:
                if candidate_mode!='standard' and p['bop_route_snapshot'][route]<=p['bop_threshold']: continue
                paths.append(forecast_programme_completion(p,candidate_program,route,candidate_mode,cohesion,
                    elapsed_congress_days=elapsed_congress_days,recovery_cooldown_remaining=recovery_cooldown_remaining,
                    pending_recovery_remaining=pending_recovery_remaining))
            candidates[candidate_program]=paths
        available=[path for paths in candidates.values() for path in paths if path['focus_available']]
        planned=[path for paths in candidates.values() for path in paths if path['earliest_feasible_start_day'] is not None]
        best=min(planned,key=lambda path:path['earliest_feasible_start_day']) if planned else None
        return {'focus_available':int(bool(available)), 'programmes':candidates,
                'cohesion_current':cohesion,'latest_start_day':p['program_start_latest'],
                'earliest_feasible_start_day':best['earliest_feasible_start_day'] if best else None,
                'start_days_short':best['start_days_short'] if best else None,
                'available_programmes':[name for name,paths in candidates.items() if any(path['focus_available'] for path in paths)],
                'focus_lock_reason':'' if available else 'không còn đường khởi động hợp lệ trước hạn270; xem cohesion và cooldown',
                'focus_reopen':'Họp xử lý bất đồng/hòa giải vẫn mở; phục hồi nếu còn kịp hoặc chọn chương trình khác đang mở; không gia hạn cửa sổ',
                'recovery_gate_blocked':False,'reconciliation_gate_blocked':False,
                'scope':'cổng chung nếu program=None; cổng lựa chọn nếu program có tên; các gate cũ vẫn áp dụng'}
    def base_at(at_cohesion):
        if signed_base_days is not None: return signed_base_days
        result=p['prepare_days'][route]+sum(p['action_days'][action][int(mode!='standard')] for action in SEQUENCES[program])
        return result+(p['low_cohesion_prepare_extra'] if at_cohesion<p['recovery']['low_below'] else 0)
    base = signed_base_days
    if base is None:
        base = base_at(cohesion)
    evidence = base + (p["e102"][e102][2] if e102 != "NA" else 0)
    risk = program == "inspection" and e103 == "A" and evidence > p["early_days"][program]
    risk_day = max(evidence, p["early_days"][program]) + p["e103"]["reappraisal_days"] if risk else evidence
    deterministic_day = risk_day if rejection_known and risk else evidence
    start_open = base <= p["program_deadline"] - p["reserve_days"]
    choice_open = deterministic_day <= p["program_deadline"] - p["exception_reserve_days"]
    launch_day=elapsed_congress_days if start_open else None
    restored=cohesion;recovery_pp=0;meetings=0;recovery_schedule=[]
    next_meeting=elapsed_congress_days+recovery_cooldown_remaining
    if not start_open and signed_base_days is None:
        if pending_recovery_remaining is not None:
            finish=elapsed_congress_days+pending_recovery_remaining
            restored=min(p['cohesion_limits'][1],restored+p['recovery']['cohesion'])
            next_meeting=max(next_meeting,finish)
            if base_at(restored)<=p['program_deadline']-p['reserve_days']: launch_day=finish
        while launch_day is None and restored<p['recovery']['low_below']:
            fee=p['recovery']['low_pp'] if restored<p['recovery']['low_below'] else p['recovery']['pp']
            recovery_pp+=fee
            finish=next_meeting+p['recovery']['days'];meetings+=1
            restored=min(p['cohesion_limits'][1],restored+p['recovery']['cohesion'])
            recovery_schedule.append([next_meeting,finish,restored,fee,recovery_pp])
            if base_at(restored)<=p['program_deadline']-p['reserve_days']: launch_day=finish
            next_meeting+=p['recovery']['cooldown']
    mode_legal=mode=='standard' or p['bop_route_snapshot'][route]>p['bop_threshold']
    if mode=='fast_override': mode_legal &= restored-p['checkpoint_count']*p['override_cohesion']>=p['override_floor']
    if mode=='combined_fast_paid': mode_legal &= restored>=p['cadre_cohesion_required']
    focus_open=mode_legal and launch_day is not None and launch_day<=p['program_start_latest']
    return {"signed_base_days": base, "forecast_full_day": deterministic_day,
            "forecast_reserve_days": p["program_deadline"] - deterministic_day,
            "risk_full_day": risk_day, "risk_reserve_days": p["program_deadline"] - risk_day,
            "start_available": int(start_open), "choice_available": int(choice_open),
            "reappraisal_risk": int(risk and not rejection_known),
            "lock_reason": "default_reserve" if not start_open else "deterministic_delay" if not choice_open else "",
            "reopen": "Họp xử lý bất đồng trước khởi động; sau ký timer không giảm" if not start_open else
                      "chọn phương án không cộng trễ; không đổi timer đã ký" if not choice_open else "",
            'focus_available':int(focus_open),'cohesion_current':cohesion,'earliest_feasible_start_day':launch_day,
            'latest_start_day':p['program_start_latest'],
            'start_days_short':max(0,launch_day-p['program_start_latest']) if launch_day is not None else None,
            'planned_start_cohesion':restored,'planned_default_full_day':base_at(restored) if launch_day is not None else None,
            'planned_recovery_pp':recovery_pp,'planned_new_meetings':meetings,
            'planned_recovery_schedule':recovery_schedule,
            'focus_lock_reason':'' if focus_open else 'không có đường khởi động hợp lệ trong cửa sổ; kiểm cohesion/cooldown/mode',
            'focus_reopen':'phục hồi cohesion nếu còn kịp; chọn trọng tâm khác đang mở; quá hạn không phục hồi hồi tố cửa sổ',
            'recovery_gate_blocked':False,'reconciliation_gate_blocked':False}


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |",
                       "| " + " | ".join(["---"] * len(headers)) + " |"] +
                      ["| " + " | ".join(map(str, row)) + " |" for row in rows])


def check_l2_node_choices():
    data = json.loads(PARAMS.read_text(encoding="utf-8"))
    p = {key: row["value"] for key, row in data["parameters"].items()}
    prices = p["node_choice_prices"]
    expected_ids = [f"{term}{i:02}" for term in ("X", "XI", "XII", "XIII", "XIV") for i in range(1, 9)]
    all_focus_costs = {node: int(cost) for node, cost in re.findall(
        r"^\| ((?:F|IX|X|XI|XII|XIII|XIV)\d\d)(?: `[^`]+`)? \| [^|]+ \| (\d+) \|",
        DOC.read_text(encoding="utf-8").split('### 7.4a.')[0], re.M)}
    assert set(all_focus_costs) == set(p["focus_nodes"]), f"Tổng focus/cost không khớp B1: {len(all_focus_costs)}"
    assert all(all_focus_costs[node] == row["cost"] for node, row in p["focus_nodes"].items()), "Có cost focus lệch B1"
    nodes = {}
    pattern = re.compile(r"^\| ((?:X|XI|XII|XIII|XIV)\d\d) \| ([^|]+) \| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$")
    choice_pattern = re.compile(r"([AB]): (\d+(?:[.,]\d+)?) (PP|ngân khố)")
    for line in DOC.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        node, name, cost, gate, choices, next_term = match.groups()
        term = re.match(r"(?:XIV|XIII|XII|XI|X)", node).group(0)
        anchor = date.fromisoformat(p["congress_dates"][term]).strftime("%d/%m/%Y")
        options = {label: (float(amount.replace(",", ".")), kind) for label, amount, kind in choice_pattern.findall(choices)}
        assert set(options) == {"A", "B"}, f"{node}: cần đúng hai giá lựa chọn A/B"
        assert len(gate.split(";")) >= 4 and "chế độ" in gate, f"{node}: gate thiếu kỳ/ngày/prerequisite/chế độ"
        assert term in gate and anchor in gate, f"{node}: sai kỳ hoặc ngày neo B1"
        assert any(kind in choices for kind in ("Event", "Decision", "Milestone", "Resolver")), f"{node}: thiếu caller"
        assert len(next_term.strip()) > 20, f"{node}: thiếu hậu quả liên nhiệm kỳ"
        pair = []
        for label in ("A", "B"):
            amount, kind = options[label]
            expected_pair = prices[node][0 if label == "A" else 1]
            actual_pair = [amount, 0] if kind == "PP" else [0, amount]
            assert actual_pair == expected_pair, f"{node} {label}: giá tài liệu lệch B1"
            pair.append(actual_pair)
        assert int(cost) == p["focus_nodes"][node]["cost"], f"{node}: cost lệch danh mục B1"
        nodes[node] = pair
    assert set(nodes) == set(expected_ids), f"40 node đặc tả: {len(nodes)}; thiếu/thừa ID"
    scenarios = []
    for node, pair in nodes.items():
        winners = set()
        values = {}
        for route in p["prepare_days"]:
            for r in p["r_values"]:
                for k in p["k_values"]:
                    costs = [round(pp + treasury * k, 6) for pp, treasury in pair]
                    values.setdefault(k, costs)
                    if costs[0] < costs[1]:
                        winners.add("A")
                    elif costs[1] < costs[0]:
                        winners.add("B")
        assert winners == {"A", "B"}, f"{node}: có lựa chọn luôn rẻ nhất tại k={values}"
        scenarios.append({"node": node, "costs_k20_k40_k60": [values[k] for k in p["k_values"]]})
    return {"focus_nodes": len(all_focus_costs), "l2_nodes": len(nodes), "routes_checked": len(p["prepare_days"]),
            "r_values_checked": len(p["r_values"]), "k_values": p["k_values"],
            "all_events_have_cost_crossover": True, "examples": scenarios[:3]}


def run():
    args = argparse.ArgumentParser()
    args.add_argument("--capture-b1", action="store_true")
    args.add_argument("--apply-l1", action="store_true")
    args.add_argument("--sync-confirmed", action="store_true")
    args.add_argument("--check-l2", action="store_true")
    args.add_argument("--csv-only", action="store_true")
    args.add_argument("--audit-l3", action="store_true")
    args.add_argument("--audit-json", action="store_true")
    args.add_argument("--sync-approved", action="store_true")
    parsed = args.parse_args()
    if not any((parsed.check_l2, parsed.csv_only)):
        parsed.audit_l3 = True
    if parsed.audit_json:
        parsed.audit_l3 = True
    if parsed.check_l2:
        print(json.dumps(check_l2_node_choices(), ensure_ascii=False, indent=2))
        return
    data = json.loads(PARAMS.read_text(encoding="utf-8"))
    p = {key: row["value"] for key, row in data["parameters"].items()}
    sequences = SEQUENCES
    names = {"cadre": "Cán bộ", "administration": "Công vụ", "inspection": "Kiểm tra", "social": "Dân vận"}
    routes = list(p["prepare_days"])
    modes = ["standard", "fast_paid", "fast_override", "combined_fast_paid"]

    def timeline(program, route, fast):
        return p["prepare_days"][route] + sum(p["action_days"][action][int(fast)] for action in sequences[program])

    def audit_outcome(base, e102, e103):
        evidence = base + p["e102"][e102][2]
        cutoff = p["early_days"]["inspection"]
        rejected = e103 == "A" and evidence > cutoff
        potential = max(evidence, cutoff) + p["e103"]["reappraisal_days"] if rejected else evidence
        # B buys a contract extension; C closes only the contract as partial.
        # Neither operation substitutes for program evidence.
        contract = "accepted" if e103 == "A" and not rejected else "rejected" if rejected else "extended" if e103 == "B" else "partial"
        if e103 == "B" and evidence > p["e103"]["B_deadline"]:
            contract = "extension_missed"
        return potential, rejected, contract

    rows = []
    for program, route, mode in itertools.product(sequences, routes, modes):
        fast = mode != "standard"
        combined = mode == "combined_fast_paid"
        legal = not fast or p["bop_route_snapshot"][route] > p["bop_threshold"]
        event_pairs = itertools.product("ABC", "ABC") if program == "inspection" else [("NA", "NA")]
        for e102, e103 in event_pairs:
            for k, r in itertools.product(p["k_values"], p["r_values"]):
                record = {"program": program, "route": route, "mode": mode, "e102": e102, "e103": e103,
                          "k": k, "r": r, "eligible": int(legal), "status": "script_calculation_not_engine" if legal else "locked_by_bop"}
                if not legal:
                    rows.append(record)
                    continue
                cohesion = p["cohesion_initial"]
                bop = p["bop_route_snapshot"][route]
                factor = next(band[2] for band in p["cohesion_price_bands"] if band[0] <= cohesion <= band[1])
                start = int((Decimal(str(p["tools"]["start"][0])) * Decimal(str(factor))).to_integral_value(rounding=ROUND_CEILING))
                tools = sum(p["tools"][action][0] for action in sequences[program])
                treasury = sum(p["tools"][action][1] for action in sequences[program])
                upfront = p["fast_upfront_pp"] if fast else 0
                checkpoints = p["checkpoint_count"] * p["checkpoint_pp"] if fast and mode != "fast_override" else 0
                checkpoint_treasury = p["checkpoint_count"] * p["checkpoint_treasury"] if fast and mode != "fast_override" else 0
                treasury += checkpoint_treasury
                recovery = 0
                office = p["combined"]["pp"] if combined else 0
                if combined:
                    assert bop > p["bop_threshold"] and cohesion >= p["cadre_cohesion_required"]
                    # Program price/mode was signed first; offices merge before checkpoint drift.
                    cohesion += p["combined"]["cohesion"]
                    bop += p["combined"]["bop"]
                if mode == "fast_override":
                    for _ in range(p["checkpoint_count"]):
                        assert cohesion - p["override_cohesion"] >= p["override_floor"]
                        cohesion -= p["override_cohesion"]
                        bop += p["override_bop"]
                    if program == "cadre":
                        # Recover between checkpoints and before succession review.
                        recovery = math.ceil((p["cadre_cohesion_required"] - cohesion) / p["recovery"]["cohesion"])
                        cohesion += recovery * p["recovery"]["cohesion"]
                elif fast:
                    bop += p["checkpoint_count"] * p["consult_bop"]
                if program == "cadre" and combined:
                    recovery = max(0, math.ceil((p["cadre_cohesion_required"] - cohesion) / p["recovery"]["cohesion"]))
                    cohesion += recovery * p["recovery"]["cohesion"]
                day = timeline(program, route, fast)
                event_pp, signature, grant = 0, 0, 0
                contract = "NA"
                rejected = False
                if program == "inspection":
                    event_pp += p["e102"][e102][0] + p["e103"][e103 + "_pp"]
                    treasury += p["e102"][e102][1] + p["e103"].get(e103 + "_treasury", 0)
                    day, rejected, contract = audit_outcome(day, e102, e103)
                    if rejected:
                        cohesion += p["e103"]["rejection_cohesion"]
                    if e102 == "A":
                        # Identical partner acceptance scenario on all routes.
                        option = "A" if combined else "B"
                        signature = p["e104"][option + "_pp"]
                        grant = p["e104"][option + "_grant"]
                        treasury -= grant
                full = day <= p["program_deadline"]
                early_full = full and day <= p["early_days"][program]
                early = early_full and (program != "inspection" or contract == "accepted")
                bonus = p["early_pp"] if early else 0
                if full and route == "collective":
                    cohesion += min(p["collective_full_extra"], max(0, p["collective_extra_cap"] - cohesion))
                cohesion += p["outcome_cohesion"]["full" if full else "partial"]
                cohesion = min(p["cohesion_limits"][1], max(p["cohesion_limits"][0], cohesion))
                gross = start + tools + event_pp + upfront + checkpoints + office + signature + recovery * p["recovery"]["pp"]
                net = gross - bonus
                daily = (r + p["branch_pp_daily"]) * p["accounting_days"]
                loss = p["cohesion_initial"] - cohesion
                record.update(pp_start=start, pp_actions=tools, pp_e102=0 if e102 == "NA" else p["e102"][e102][0],
                              pp_e103=0 if e103 == "NA" else p["e103"][e103 + "_pp"], pp_fast_upfront=upfront,
                              pp_checkpoints=checkpoints, pp_combined=office, pp_signature=signature,
                              pp_recovery=recovery * p["recovery"]["pp"], pp_early_reward=bonus,
                              treasury_checkpoints=checkpoint_treasury,
                              event_cost_pp=event_pp + signature, treasury_e103=0 if e103 == "NA" else p["e103"].get(e103 + "_treasury", 0),
                              net_treasury_cost=round(treasury, 6),
                              e103_contract_deadline=p["e103"]["B_deadline"] if e103 == "B" else p["early_days"]["inspection"] if e103 == "A" else "",
                              pp_gross_cost=gross, pp_net_cost=net, treasury_net_cost=round(treasury, 6),
                              treasury_pp_equivalent=round(treasury*k, 6), potential_full_day=day,
                              full_day=day if full else "", result="full" if full else "partial_at_deadline",
                              remaining_reserve_days=p["program_deadline"]-day if full else "",
                              full_after_early_cutoff=int(full and day>p["early_days"][program]),
                              declared_choice_exception=int(program==p["choice_full_exception"]["program"] and (e102 in p["choice_full_exception"]["e102"] or e103 in p["choice_full_exception"]["e103"] or rejected)),
                              early_cutoff=p["early_days"][program], early_reward_earned=int(early),
                              cohesion_final=cohesion, cohesion_net_spent=loss, bop_final=round(bop, 6),
                              modeled_pp_income=round(daily, 6), modeled_pp_remaining=round(daily-net, 6),
                              gross_cost_income_ratio=round(gross/daily, 6), net_cost_income_ratio=round(net/daily, 6),
                              converted_cost=round(net+treasury*k+loss*p["cohesion_pp_rate"], 6),
                              converted_cost_income_ratio=round((net+treasury*k+loss*p["cohesion_pp_rate"])/daily,6),
                              e103_contract=contract, e104_grant=grant, side_project_available=int(early_full),
                              side_project_if_taken_pp=p["side_project"]["pp"] if early_full else 0,
                              side_project_if_taken_finish=day+p["side_project"]["days"] if early_full else "",
                              technical_training_opportunity=int(grant > 0),
                              deep_data_cooperation_opportunity=int(grant == p["e104"]["A_grant"]),
                              opportunity_count=int(early_full)+int(grant > 0))
                forecast = forecast_programme_completion(p, program, route, mode, p["cohesion_initial"], e102, e103)
                record.update({"forecast_" + key if not key.startswith("forecast_") else key: value
                               for key, value in forecast.items() if not isinstance(value,(dict,list))})
                rows.append(record)
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with CSV.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    if parsed.audit_l3:
        from VIETNAM_POLITICAL_CROSSCHECK_VI import audit_l3, sync_approved_document
        if parsed.sync_approved:
            sync_approved_document()
        raise SystemExit(audit_l3(write_json=parsed.audit_json))
    if parsed.csv_only:
        print(json.dumps({"rows": len(rows), "eligible_rows": sum(row["eligible"] for row in rows),
                          "nodes": len(p["focus_nodes"]), "csv": str(CSV)}, ensure_ascii=False, indent=2))
        return


if __name__ == "__main__":
    run()
