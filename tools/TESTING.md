# md_vietnam: how to test (the game loads the mod with a clean error.log since 2026-09-19; content not yet playtested)

> This file grew into a build log as well as a test script. The top section (through "Balance sanity" below) is
> the live "how to test today" guide and is kept accurate. Everything from "Batch 1 additions" onward is a dated
> changelog of what was added or fixed at the time — a later dated entry can delete content an earlier one
> describes, and that deletion is not always logged as its own entry (see the note added to "Batch 4"/"Batch 5").
> The "## Removed: ..." headings are the authoritative record of what is gone. Grep an id in `common/` or
> `events/` before typing it into the console; if it is not there, the entry you read is history, not a live test.

0. Launcher: add "Millennium Dawn - Vietnam" to the playset **after** Millennium Dawn. Start the game once,
   then open `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log` and search for `VIE`, `vie_`,
   `power_balance`, `on_action`, `game_rule`, `md_vietnam`. Fix these before playing.
1. Before each session: `python3 tools/verify_all_loc.py` (portable, no local paths to edit; checks loc keys/BOM
   and prints the current focus count). `tools/check_static.py` and `tools/audit_mod.py` do deeper checks (focus
   grid, dangling effect/trigger calls, GFX refs) but hardcode a Windows path to a local Millennium Dawn workshop
   install and a local HOI4 install (`check_static.py` lines 7, 69, 145, 224), or to the checkout itself
   (`audit_mod.py` line 12, `unify.py` line 5); edit those constants for your machine first, or they raise
   `FileNotFoundError` before running any check. There is no `check_vie.ps1` in this repo.

## Smoke test (10 minutes)
| Step | Expected |
|---|---|
| Start 2000, play as VIE, unpause one month | leader changes to Le Kha Phieu, a balance-of-power widget "Direction of the Party" appears, idea "Independence and Self-Reliance" |
| Open the focus tree | 381 focuses, all visible; the one remaining alternative-regime root, `VIE_sec_cyber_control` (the security-state door), is greyed out until `ruling_party = 7`, or both `VIE_ax_civil_norm < -7` and `VIE_ax_checks_norm < -1` plus `VIE_security_unlocked` |
| Do the first focuses (`focus.autocomplete` for speed) | no errors; `VIE_doi_moi_continues` first |
| Mid-April 2001 | event "The Ninth Party Congress" |
| 2014 May | HD-981 chain (3 events); afterwards the door event `vie_alt.1` (20-40 days after the rig leaves) |
| Game rules screen | "Vietnam: Alternative History" (Plausible / Historical / Free) |

## Land force building (Truc 3, 30 focuses VIE_lf_*), not yet run in game
Design, deviations from the report and the 9 build steps: `VIE_truc3_review_and_plan.md`. Balance numbers: `python tools/audit/lf_balance.py` (must print PASS).
On a save copy with `debug` on:
- [ ] `error.log`: grep `VIE_lf_`, `vie_lf`, `VIE_dec_lf_`, `reduce_focus_completion_cost`, `force_update_dynamic_modifier`, `urban_attack_factor`, `army_personnel_cost`, `Cum Co dong`, `Dan quan Khu vuc`.
- [ ] **Reload bug (Truc 2, fixed in step 0):** play to 2015, finish a Truc 2 decision, save, reload: `VIE_def_industry_level` and `VIE_lf_arm_count` are NOT reset to 0.
- [ ] Number of focus slots in MD is 1 (the plan assumes it). If 2 or more, rerun the simulation of report section 8.12.
- [ ] Gate: `VIE_lf_army_reform` is greyed before 11/2/2019 on `plausible`/`historical`; on `free` it opens after 2012 once `VIE_def_industry_level >= 2`.
- [ ] Arms limit: after BB1, TG1, PB1 the Engineers node is greyed; BB2/TG2/PB2 still clickable; `VIE_lf_combined_arms` greyed until `arm_done >= 3`; every 3-of-4 combination reaches it (especially BB + TG + Engineers).
- [ ] First Force Structure: picking `VIE_lf_fs_main_corps` greys the mobile and depth roots; `VIE_lf_dev_strategic` and `VIE_lf_dev_territorial` exclude each other and both open from any of the three second nodes.
- [ ] Capability limit: after two roots the third is greyed; `VIE_lf_selective_modernization` greyed until `cap_done >= 2`; any two areas open it.
- [ ] Favoured area: after FR1 the Army-AD root is 14 days cheaper than the other two roots (checks the unit of `reduce_focus_completion_cost`).
- [ ] Tooltips of `VIE_armed_forces_modifier` change right after each node (if not, `force_update_dynamic_modifier` is needed). The two MD cost modifiers: is +2% really +2%?
- [ ] Division templates "Cum Co dong" (FM2) and "Dan quan Khu vuc" (FD2) appear, no regiment errors.
- [ ] Six decisions appear in `VIE_military_readiness_category` next to the four old ones (same category block in two files merges?). Cooldown starts when? Timed ideas expire after 180/90 days.
- [ ] Events: `event vie_lf.1` ... `.5`; 2022-01-17, 2022-12-20 (hidden), 2023-12-02, 2024-12-15 (hidden), 2025-02-05; never two pop-ups within 45 days; the milestone halves the cost of the matching focus if it is not done yet.
- [ ] Re-count pop-ups per year for 2022-2025 (rule: at most 7; 2024 may already be over because of Truc 2).
- [ ] AI observe run: after 2019 the AI takes Truc 3, direction follows the AI path, nothing gets stuck on `bankruptcy_incoming_collapse`.
- [ ] Step 8 (AI soft-links): with `VIE_lf_regular` the AI buys K9/BMP-3/TOS-1A/CAESAR options more often; with `VIE_lf_depth` Igla option A. Nothing opens or closes differently.
- [ ] Focus icons: the 35 army-branch focuses (30 `VIE_lf_*`, `VIE_modernize_vpa`, 4 Truc 2) show their own `GFX_focus_VIE_*` icon (93x91, `gfx/interface/goals/`); no `texture` / `GFX_focus_VIE_` errors in `error.log`; icons stay readable at game size.

## Army commander roster (2000-2014 / 2015-now / 2026), not yet run in game
Design and the 4 experiments (E1-E4) behind it: `VIE_land_forces_implementation_plan_v2.md`. On a save copy with `debug` on:
- [ ] `error.log` after loading: no `VIE_army_`, `portrait` or `trait` errors. Placeholder portraits are flat silhouettes
      generated by `python tools/build_vie_placeholder_portraits.py`; replace them with real photos later.
- [ ] Start 2000, VIE recruit panel: field marshals Nguyen Chi Vinh + Le Van Dung; corps commanders Phung Quang Thanh,
      Huynh Tien Phong, Phi Quoc Tuan, Ngo Xuan Lich (6 with Vinh/Dung); army_chief advisors Le Van Dung, Phung Quang Thanh,
      Nguyen Khac Nghien, Do Ba Ty; high_command advisors Pham Van Tra, Nguyen Van Duoc, Hoang Ky, Pham Xuan Hung.
      `VIE_army_le_manh` no longer exists (character removed 2026-10-02).
- [ ] `effect set_country_flag = VIE_army_phase1_recruited` already set after the first load; reload a 2007 save: nobody is recruited twice.
- [ ] `event vie_army_commanders.2`: the 2000-2014 group disappears, Phung Si Tan / Nguyen Doan Anh / Nguyen Hong Thai
      (corps) and Nguyen Phuong Nam / Vu Hai San (high_command) appear. Phi Quoc Tuan is retired too.
- [ ] `event vie_army_commanders.1`: 8 Corps 12/34 / Military Region 7 commanders appear (incl. Truong Manh Dung).
- [ ] Open question to settle once: `effect retire_character = VIE_Phan_Van_Giang` then `effect recruit_character = VIE_Phan_Van_Giang`.
      The current code does not depend on it (Branch N), but moving upstream 2015+ generals back to 2015 would.

## Air force roster (8-step air_chief chain + 12 high_command), not yet run in game
Design and the three experiments (E5-E7) behind it: `VIE_air_force_implementation_plan.md`. Placeholder portraits come from
`tools/build_vie_placeholder_portraits.py`. On a save copy with `debug` on:
- [ ] `error.log`: no `VIE_air_`, `trait`, `portrait` or `idea_token` errors.
- [ ] E5, start 2000: the air panel has no Tran Quang Phuong and no Tran Viet Khoa (retired in on_startup by `VIE_air_phase0_done`).
      If they are still there, retire-at-startup does not work and the plan's step 0 needs another approach.
- [ ] Start 2000: `air_chief` offers only Nguyen Duc Soat; `high_command` (ledger air) offers Pham Thanh Ngan, Han Vinh Tuong,
      Pham Tuan, Nguyen Van Phiet plus upstream Vo Minh Luong and Vo Trong Viet.
- [ ] E6: hire Soat as air chief, then `effect retire_character = VIE_air_nguyen_duc_soat`: does the slot empty?
- [ ] E7, `effect VIE_event_scheduler_air = yes` after setting the date to each step (2002-02-07, 2007-02, 2010-07, 2015-05-21,
      2019-12-31, 2023-05-19, 2025-06-28): air_chief changes to Than, Duc, Hoa, Vinh, Kha, Hien, Son in that order and
      `VIE_air_step_N` flags appear. If direct recruit/retire inside the scheduler fails, switch to hidden events (plan, step 4).
- [ ] Reload a 2012 save: nobody is recruited twice and the roster still matches the 2010-07 to 2015-05 row of the plan.

## Naval procurement (Truc 1 hai quan, namespace vie_naval), not yet run in game
Design, deviations from the report and the 7 build steps: `VIE_naval_truc1_review_and_plan.md`. Flags: `VIE_v9_flag_mapping.md` (section "Truc 1 hai quan").
Files: `VIE_md_effects_naval*.txt` (scheduler, ships, sigma, late), `VIE_md_triggers_naval.txt`, `events/VIE_naval.txt` (21 events), `VIE_md_naval_decisions.txt`.
Console: `effect VIE_event_scheduler_naval = yes` runs one tick; set the date first. On a save copy with `debug` on:
- [ ] `error.log`: grep `vie_naval`, `VIE_naval`, `equipment_variant`, `create_ship`, `module`, `slot`, `frigate_hull_3`, `attack_submarine_hull_2`, `corvette_hull_2`, `multiply_temp_variable`.
- [ ] **Highest risk, check first:** does `create_ship` with `creator = SOV` deliver when VIE has not researched the hull (VIE starts with `corvette_hull_1` only)? The old p12 scheduler that used the same pattern was never run in game. If ships do not arrive, the money was still charged: note the log line.
- [ ] Own variants (`"Molniya Class"`, `"Gepard Class"`, `"Gepard 3.9 Class"`, `"Improved Kilo Class"`, `"Sigma Class"`) appear in the ship designer; modules are not silently dropped for missing tech. `effect VIE_naval_ensure_variants = yes` twice must not create version 2.
- [ ] Obsolete SOV variants (`"Molniya Class"`, `"Gepard 3.9 Class"`) are accepted by `create_ship`.
- [ ] Start 2000, wait to 2003-06: exactly ONE popup `vie_naval.1` (A 2 ships / C skip; B hidden). Pick A: treasury -0.12bn, flag `VIE_molniya_contracted`. 2007-02 and 2008-02 one corvette each, no popup. Pick C: no ships.
- [ ] Set `VIE_popup_cd` by hand (`effect set_country_flag = { flag = VIE_popup_cd days = 45 }`) in 2003-06 and wait: the offer slips to the next month, nothing is lost. Keep it set to 2006-01: `VIE_molniya_p1_gate_seen` then silent fallback gives the 2 ships (flag `VIE_molniya_p1_offered`, no `_missed`).
- [ ] War with SOV through the whole 2003-06..2005-12 window: `VIE_molniya_p1_missed` after 2005-12; Decision `VIE_naval_late_molniya` appears (category "Mua sam Hai quan (muon)").
- [ ] Gepard I 2006-01 (`.10` then `.11` in the same sitting, `.11` ignores popup cooldown): A = Gepard 3.9, B = ASW. Ships 2011-03 / 2011-08. Treasury -0.35bn for 2.
- [ ] Bastion-P 2006-07 (`.30` then `.31`): bunkers appear in provinces 4119 / 10309 / 10162 per choice; after the first delivery `effect has_country_flag = VIE_ev_bastion_p_coastal_defence`; after all delivered `VIE_ext_naval_missile`.
- [ ] Kilo 2009-12 (`.20` then `.21`): full pack -3.2bn for 6, +20 navy XP; cut pack -2.0bn and every boat 6 months later. First boat 2014-01-15; `VIE_ev_kilo_submarines` set -> `VIE_paracel_ultimatum` becomes selectable (other gates permitting). After the sixth: `VIE_opp_sub_mro`, and `VIE_kilo_flotilla_idea` only with the full pack.
- [ ] Gepard II only after Gepard I is delivered: window 2011-12; with Gepard I skipped the offer never appears and `VIE_gepard2_missed` is set after 2014-12.
- [ ] Molniya phase 2 needs `VIE_cap_ba_son_yard` (nothing sets it yet, Truc 2 Focus 1-2 and Decision 1 are not built): `effect set_country_flag = VIE_cap_ba_son_yard` in 2009-06 to test `.3`. Options B/C appear only with `effect set_variable = { VIE_var_ba_son_tier = 2 }`. Ships 2014-07, 2015-06, 2017-10.
- [ ] Sigma 2011-10 (`.40`): A "continue talks" then in 2013-08 `.44` and `VIE_sigma_suspended`, NO ship ever. B -> `.41` -> `.42` -> Funding Gate: log the real `treasury` at 2011-10. If it is below 0.66bn the gate always fails (check the pop-up `.43`). `.43` A (halve) must not loop forever; B borrows (debt +10%).
- [ ] Sigma delivered by hidden event `.45` every 182 days after 900 / 1080 / 1260 days; `VIE_var_integration_exp` +8 (Domestic) / +4 (Hybrid) on the last ship.
- [ ] Late path: with `_missed` set (`effect set_country_flag = VIE_kilo_missed`, date after 2011-12) Decision `VIE_naval_late_kilo` appears, 50 PP, 180 day cooldown; sign it: +25% cost, first boat after 1840 days, then every 210 days (`vie_naval.53`); the dated delivery flags (`VIE_kilo_s1..s8`) are all pre-set so no double delivery.
- [ ] Remove SOV from the map before 2009-12 (annex by console): Kilo is `_missed`, late Decision unavailable until it exists; phase 2 Molniya still delivers using the own variant.
- [ ] No `VIE_gepard_contract` / `VIE_kilo_contract` left anywhere live: `grep -rn` in `common/` and `events/` (only `.bak` and `v1*_removed_*.txt` may match).
- [ ] Pop-ups per year 2003-2019 (`python tools/audit/ev.py`, then play observe mode): naval adds `.1` (2003), `.10` `.30` (2006), `.3` (2009), `.20` (2009-12), `.40` `.12` (2011); chained `.11/.21/.31/.41/.42/.43` are exempt. Target <= 7 per year, record the years over.
- [ ] Civil war: `effect set_variable = { VIE_catch_up = 1 }` then `effect VIE_event_scheduler_naval = yes`: no popup, no ship, offered flags set, `VIE_sigma_suspended` set.
- [ ] AI-only run to 2020: AI VIE has Molniya phase 1, Gepard I, Bastion-P and Kilo (`VIE_ai_historical`); no Sigma. Gepard II and Molniya phase 2 depend on Truc 2 for the Ba Son flag.
- [ ] Prices (USD bn, see top of `VIE_md_effects_naval_ships.txt`): Kilo 0.333/boat (+0.2 full pack), Gepard I 0.175, Gepard II 0.35, Molniya p1 0.06, Molniya p2 0.13, Bastion-P 0.15, Sigma 0.33. Lowest confidence: Molniya p1. Run `python tools/audit/naval_balance.py` after changing any price.

## Naval industry (Truc 2 hai quan, namespace vie_nav_ind), not yet run in game
Design, deviations and the 9 steps: `VIE_naval_truc2_review_and_plan.md`. Flags: `VIE_v9_flag_mapping.md` (section "Truc 2 hai quan"). Balance numbers: `python tools/audit/naval_balance.py` (must print PASS).
Files: `VIE_md_effects_nav_ind.txt` (helpers, D1-D5 start/finish), `events/VIE_nav_ind.txt` (17 events), `VIE_md_nav_ind_decisions.txt` (category `VIE_naval_industry_category`), `VIE_md_ideas_nav_ind.txt`, six focuses `VIE_naval_defence_law` ... `VIE_naval_defence_2030` right of `VIE_modernize_vpa` (x 256-260). On a save copy with `debug` on:
- [ ] `error.log`: grep `vie_nav_ind`, `VIE_nav_`, `VIE_naval_has_`, `two_state_dockyards`, `one_state_dockyard`, `add_tech_bonus`, `add_mio_size`, `add_timed_idea`, `CAT_`, `minor_flavor`.
- [ ] **First check:** `days = <temp variable>` works for `country_event` and `add_timed_idea` (MD does it, see plan part 10, but this mod never has): finish D1 Basic, the timed idea `VIE_nav_prog_ba_son` shows a countdown of about 365 days and `vie_nav_ind.60` fires after 146.
- [ ] Focus tree: the six focuses sit in a clean column left of the army block, none overlapping `VIE_def_industry_law` at (266, 2). Focus 1 opens from 2005-01, Focus 3 needs `VIE_var_hulls_delivered >= 4` (ships only; Bastion-P does not count) (tooltip shows) and 2012, Focus 4 needs 2010, Focus 5 needs Focus 3 AND 4 and 2018 and one source, Focus 6 needs 2028. `effect set_variable = { VIE_var_hulls_delivered = 4 }` and the date console to test.
- [ ] Focus 2 completion fires `vie_nav_ind.1` (orientation A/B/C); A and C add `VIE_var_shipbuilding_exp`, B and C add `VIE_var_mro_exp`. Decision `VIE_nav_d1_ba_son` is greyed until an orientation is chosen and fewer than 2 programs run (both tooltips).
- [ ] D1: Basic -> `.60` after 146 days sets `VIE_cap_ba_son_yard` and `VIE_var_ba_son_tier = 1`; Expanded 219 days and tier 2; Focus 292 days and tier 3. At the end one dockyard appears in state 519 (two for Focus), MIO Ba Son +1/+2/+3, shipbuilding_exp +5/+10/+15, `VIE_nav_d1_done`. **Treasury:** MD charges 7.5 per dockyard itself; the extra hand charge is only 4.5 / 3.0 and Balanced orientation adds 15% of the tier total. Compare treasury before and after: a total of 15+ for Basic means a double charge.
- [ ] Truc 1 link: after `.60` with tier 2+, `vie_naval.3` (Molniya phase 2, 2009-06 window) shows options B and C (8 and 10 ships). With tier 1 only A and E show.
- [ ] D3: needs `VIE_cap_ba_son_yard`; `.20` spec adds exp at once; level 3 hides without `VIE_molniya_domestic_started`. After completion `VIE_small_combatant_cost_mult` is 0.80/0.85/0.90; a late Molniya phase 2 contract (Decision `VIE_naval_late_molniya`) is cheaper by that factor.
- [ ] D2: needs a delivered Kilo or Gepard/Molniya; scope sub/surface/fleet follow the Truc 1 deliveries; Russia support sets `VIE_mro_russia_dependent` and clamps `VIE_var_mro_exp` at 50; level 2 needs D1 done, level 3 needs D1 done plus D1 Expanded+ or D3 done. Duration: orientation MRO-first 0.75x, shipbuilding-first 1.25x, Russia 0.75x, autonomous 1.25x, 0.85x with `VIE_opp_sub_mro`.
- [ ] D4: Electronics needs one of `VIE_semiconductor_fab`, `VIE_chip_design`, `VIE_earth_observation`, `VIE_vinasat` (completed focus); Weapons needs `VIE_ext_naval_missile` (Truc 1: all Bastion-P delivered). Full needs both, 1.5x price. Balanced level adds +5 exp when a Sigma has been delivered.
- [ ] D5: needs shipbuilding_exp 30 and mro_exp 15 (tooltips show the current values); balanced orientation + all-Basic + Molniya phase 2 (6 ships) reaches 40/16. The four priorities need D1, D2, D4 done as written; autonomy Integrated needs `VIE_var_ba_son_tier >= 2`, High needs tier 3 and `VIE_var_integration_tier >= 2`. End sets `VIE_cap_mature_naval_industry` and idea `VIE_nav_mature_industry_idea`.
- [ ] Slot: start D2 and D3 together; D4 or D5 shows the slot tooltip greyed; finishing one frees it. Console `effect VIE_nav_program_recount = yes` with no timed ideas gives 0.
- [ ] Civil war: after `VIE_collapse_aftermath` the slot counter equals the number of `VIE_nav_prog_*` ideas held; a rebel-tag winner starts at 0. Pending completion events of the old country are lost with the tag (known limit).
- [ ] AI-only run to 2020: AI VIE completes Focus 1, 2, Decision 1 before 2009-06 (else Molniya phase 2 is missed) and later D3 and D2; no D4/D5 before their dates. Watch `ai_will_do` of the six focuses (90 / 90 / 70 / 70 / 60 / 60).
- [ ] Notifications `.60 .61 .62 .63 .64 .65` use `minor_flavor = yes`: check they appear as the small flavor notices and not as full pop-ups; if the attribute is rejected, remove it.
- [ ] Prices (USD bn): D1 7.5 / 12 / 18; D2 4.0 x 1 / 1.6 / 2.4 x 0.8 or 1.4 x 1.3 (fleet); D3 6.0 / 9.6 / 14.4; D4 7.0 / 11.2 / 16.8 x 1.5 (Full); D5 10 / 15 / 22. Totals: historical 33.7, all-max 97.1. Change a price: rerun `python tools/audit/naval_balance.py`.

## Console shortcuts (use a save copy, enable `debug` first)
* `tag VIE`, then `event vie_alt.14` (first free election: options a/b/c switch the ruling party to 2/liberalism,
  1/conservatism or 3/socialism), `event vie_col.2` (collapse and civil war; the rebel party is picked by
  `VIE_col_pick_rebel` — 13 with `VIE_reform_mandate`/`VIE_press_relaxed`, 5 with `VIE_wk_grievance`/
  `VIE_wa_labor_repressed`, else 22).
* `effect set_country_flag = VIE_security_unlocked` opens the one alternative-regime root left in the tree
  (`VIE_sec_cyber_control`). `VIE_tc_unlocked`, `VIE_np_unlocked`, `VIE_junta_unlocked`, `VIE_sez_unlocked`,
  `VIE_oligarch_unlocked` and `VIE_monarchy_unlocked` no longer gate anything — those bands were deleted (see the
  "Removed:" entries near the end of this file). `VIE_democracy_path_open` and `VIE_developmental_unlocked` still
  exist but only swap an idea or an internal-faction reward, not a focus band any more.
* There is no `VIE_enter_regime` effect — that name is dead, left over in a comment at
  `common/scripted_effects/VIE_md_effects_p3.txt:6`. To force a regime change from the console, call the real
  gateway directly: `effect { set_temp_variable = { rul_party_temp = 22 } VIE_transition_regime = yes }`. Party
  indices this mod actually drives: 1 conservatism, 2 liberalism, 3 socialism, 7 autocracy/security state, 13
  reformist, 19 the Party (default). Slots 20/21/22 (nationalist populist/fascist/military-junta, MD-defined) have
  no focus content beyond the civil-war rebel outcome, but `VIE_transition_regime` still switches to them cleanly.
  After the call, check: ruling party, leader (must be fictional for any slot other than 19), balance-of-power
  widget, Four Nos idea state.
* `effect add_stability = -0.9`, then wait a month, to test the collapse check (needs two crisis ideas, e.g.
  `effect add_ideas = VIE_state_debt_overhang`, `effect add_ideas = VIE_bond_overhang`, and a pole such as an
  extreme `VIE_party_balance` value or `effect set_country_flag = VIE_wa_suppressed`; `VIE_lac_hong_active` no
  longer exists — see `VIE_collapse_pole` in `common/scripted_triggers/VIE_md_triggers_p3.txt`).

## Civil-war checklist (run once, on a copy of a save)
- [ ] Units: totals before/after; no units stuck in provinces of the other side (search error.log for `Could not find province` or `unit`).
- [ ] Fleets and aircraft in split states.
- [ ] Both countries: treasury, taxes and debt display normal numbers (no NaN, no negative infinity).
- [ ] Save, then load in the middle of the war.
- [ ] War ends: winner absorbs the loser, flags `VIE_collapse_done` and `VIE_post_collapse` present, event `vie_col.6` fires.
- [ ] If the **rebels** win: the new tag still receives monthly events (`VIE_event_scheduler_*` in the log) and has the right balance of power.

## Balance sanity (observe mode, 2000-2026)
* Stability stays between 40% and 90% on the historical trunk; treasury never far below zero for more than a year.
* No collapse and no alternative regime appears under the "Historical" game rule.
* Pop-ups: never two within **45** days (except chained events) — this is the real,
  code-enforced rule, via the `VIE_popup_cd` country flag (set in 102 places across
  10 scheduler files; every scheduler reads it before firing).
* Pop-ups per calendar year: the old target here was "at most 5". **That target was
  never enforced by any code and is already exceeded by the mod as it stands** —
  measured on 2026-09-30 across `VIE_event_scheduler` … `_p14`, counting only events
  with a `title` (hidden class-C events excluded), 11 of 29 years are over 5:
  `2003=6 · 2008=6 · 2012=8 · 2014=8 · 2018=6 · 2020=6 · 2021=12 · 2022=6 ·
  2023=6 · 2024=7`, and Trục 1 adds `.14`/`.15`/`.16` (2016→6, 2018→7, 2019→6).
  **Revised target: ≤ 7 per year.** 2021 (=12) is a known pre-existing exception and
  is not Trục 1's doing; reducing it means re-dating existing p2/p10 events, which is
  out of scope for Trục 1. If you want 2021 fixed, that is its own task.

## Batch 1 additions (plan v6 step 2): what to look at
| Item | Expected |
|---|---|
| Political column x -12..-3 | new anti-corruption ladder (`VIE_anti_corruption_law` -> capstone `VIE_clean_cadres`), administration reform, assembly/ethnic/cyber focuses |
| Finance chain at x 8..10, rows 1..5 | `VIE_state_bank_modernization` root; `VIE_market_upgrade_criteria` (after 2023) fires `vie_eco.13` about 30 days later |
| Events | 2004 `vie_pol.18` (option B needs `VIE_ethnic_policy`), mid-2018 `vie_pol.10`, 2023-24 `vie_cor.6` and `vie_pol.21` (only after `VIE_party_discipline`) |
| Far right of the tree (x 25..30 from root) | G4 tourism/culture and G5 population/labour roots; G9 vision chain at x 22..24, rows 5..8 unlocks 2030 onwards |

## Batch 2 additions
| Item | Expected |
|---|---|
| Near the WTO chain, x 0..1 rows 3..5 | `VIE_hose_exchange`, `VIE_investment_law_2005`, `VIE_wto_reforms`, `VIE_export_powerhouse` (needs CPTPP done) |
| Diplomacy block x 6..10 rows 6..8 | partner network under `VIE_csp_network`; capstone `VIE_global_south_ties` needs India and Gulf |
| East block x 32..36 / 39..41 / 44..53 / 56..62 / 64..68 / 72..74 (row 1 down) | industry, state groups, energy, infrastructure, East Sea, national defence; roots have no prerequisite and are gated by date or by a completed focus |
| Events | 2006 `vie_dip.5` (sets `VIE_apec_year`, opens `VIE_apec_host`), 2018-19 `vie_eco.19`, 2020 `vie_eco.21` (only after `VIE_solar_boom`), 2021 `vie_scs.13` (option B needs `VIE_coast_guard_law`), 2023 `vie_eco.25` (skipped after `VIE_500kv_grid`), `vie_dip.17` opens 10 days after `VIE_rare_earths` |
| Mutually exclusive | `VIE_legal_warfare` <-> `VIE_assert_maritime_rights` (both sides declared) |

## Batch 3 additions
| Item | Expected |
|---|---|
| East block rows 5..8, x 32..70 | E1 army (32..36), E2 navy (40..48), E3 air (52..60), E4 defence industry (64..70); roots need `VIE_modernize_vpa` (E4 needs `VIE_viettel_military_tech`) |
| `VIE_fighter_replacement` | fires `vie_dip.16` 10 days later; option B needs `VIE_us_arms_open` (set by the 2016 embargo event) |
| Under the education root (x 21..22, rows 3..4) | G1: university autonomy, vocational training, free schooling (2025), English |
| East of the batch-2 groups (x 76..110, rows 1..4) | G2 health, G3 environment, G6 digital, G7 science, G8 chips |
| Regime bands | C5 rest at x -12..-10 rows 13..15, C7 rest at x -5..-3 rows 14..15 (after `VIE_press_relaxation`), C6 rest at x -31 / -27 rows 13..14 |
| Events | `vie_soc.14` random Hanoi smog (silenced by `VIE_hanoi_air_quality`), `vie_soc.18` 2024-25, `vie_eco.29` 2021-23 (needs `VIE_domestic_automotive`) |

## Batch 4 additions (Tier A bands finished)
**Superseded, kept for history only:** every band this table describes (Autonomy/`tc_*`, Populist/`np_*`,
Free zones/`lb_*`, Oligarchs/`ol_*`, Development council/`wa_*`) has since been deleted from the tree; none of
the focus ids below exist any more and this deletion was never logged as its own dated entry in this file
(`grep -c "id = VIE_tc_asean_bloc" common/national_focus/VIE_md_focus.txt` is 0, same for the others named here).
| Band (x from root, rows 13..17) | New focuses | Check |
|---|---|---|
| Autonomy x -2..4 | import substitution, non-aligned summit, workers' councils, arms diversification, ASEAN bloc, market socialism, rare-earth leverage, Mekong leadership, capstone | `VIE_tc_asean_bloc` creates a non-aligned faction (`create_faction_from_template`), check the log for faction errors; `VIE_tc_arms_diversification` opens `vie_int.10` |
| Populist x 6..12 | national goods, youth brigades, fishermen, veterans, media, nationalist economy, referendum, capstone | `VIE_np_nationalist_economy` opens `vie_int.11`; BoP widget moves with `VIE_pop_*` |
| Free zones x 28..34 | Van Don, Bac Van Phong, Phu Quoc, free port, casinos, digital assets, safeguards | Phu Quoc opens `vie_alt.26`, casinos `vie_alt.25` |
| Oligarchs x 36..42 | bank capture, land bank, donations, private security, offshore wealth, golden visa, tycoon diplomacy | donations open `vie_alt.27` |
| Development council x -23..-13 | five-year plans, Japanese capital, Cam Ranh access, technical education, Korea, new countryside, purge, transition, capstone | `VIE_wa_korea_partnership` opens `vie_alt.29` |
None of these flags open anything today; see the superseded note above instead of running `effect set_country_flag = VIE_tc_unlocked` etc.

## Batch 5 additions (Tier B/C, democracy packages, party names)
**Partly superseded:** the Junta/unity/monarchy row, the Green band row and the Democracy row describe the
round-table branch and the Junta/Caretaker/Monarchy/Green bands, all removed later (see "Removed: nationalist /
street hypothetical branches", "Removed: Junta, Caretaker government, Monarchy, Green coalition", and the
`round_table_talks` removal under "Trunk redesign", further down this file) — none of their ids exist today.
The Lac Hong/workers row is also dead (slot 21 has no focus content, and `VIE_wk_unlocked` never gated anything
after the workers band was cut). In the party-slots row, slot 17's leader branch was removed with the Green band;
only 5, 14 and 18 still have a fictional leader in `VIE_political_leaders.txt`. Only these two rows are still
testable:
| Item | Expected |
|---|---|
| Security x 22..26 | `VIE_sec_managed_opening` still exists and still sets `VIE_wa_unlocked`, but nothing reads that flag any more (the development council band it used to open is gone); `VIE_sec_cyber_sovereignty` still opens `vie_alt.31` |
| Party slots 5, 14, 18 | fictional leaders in `VIE_political_leaders.txt`; regime change to 14 or 18 enables elections; check `change_ruling_party_effect` works for these slots |

## Branch restructure (v6.1)
Layout changed: East block rows 1..6 now hold D3 (x 33..39), D4 (x 40..44), D5 (x 46..53), D6 (x 59..66), E6 (x 69..73); E1..E4 sit in rows 8..11 (x 32..71) and E5 in rows 5..8 (x 73..77). New focuses: `VIE_new_rural_development`, `VIE_energy_security_2045`, `VIE_us_engagement`. Check in game: no prerequisite line longer than about 16 cells; `VIE_assert_maritime_rights` hangs from `VIE_law_of_the_sea` next to `VIE_legal_warfare`; `VIE_era_of_rising` has two alternative parents; `VIE_managed_pluralism` needs the three C7 focuses.

## Batch 6 (events)
| Item | Expected |
|---|---|
| `VIE_md_p10.txt` | 71 events load (`setup.log`: `Events loaded events/VIE_md_p10.txt' #71`); no `Unknown effect` in error.log |
| News | `vie_news.1` (WTO) on 11 Jan 2007, `vie_news.3` on 10 May 2014; other news fire once when the regime flag / focus / war condition is true (`effect set_country_flag = VIE_tc_active` to test `vie_news.4`) |
| Focus-linked | `VIE_asset_recovery` -> `vie_cor.8`, `VIE_spratly_fortification` -> `vie_scs.14`, `VIE_code_of_conduct` -> `vie_scs.18`, `VIE_us_carrier_visit` -> `vie_dip.10`, `VIE_overseas_vietnamese` -> `vie_dip.19`, `VIE_sea_games_bid` -> `vie_soc.8` (the `VIE_tc_nonaligned_summit` -> `vie_dip.18` link this row used to have no longer applies: that focus was part of the deleted Autonomy/`tc_*` band) |
| Pop-up budget | run 2000-2026 in observe mode: never two pop-ups within 45 days except chained events |

## Batch 7
* `vie_alt.23` needs a party-ruled VIE with stability under 35% after Sept 2021 (`effect add_stability = -0.5`).
* `vie_scs.16`: `effect set_variable = { VIE_scs_tension = 3 }`; option B needs CHI to exist and no war. `vie_scs.17` follows 120 days after option B while at war with CHI.
* Workers as civil-war rebel: `effect set_country_flag = VIE_wk_grievance`, then `event vie_col.2`; rebel takes states 519 and 524; if the rebel wins, ruling party 5 and flag `VIE_wk_unlocked` are still set, but `VIE_wk_unlocked` no longer opens anything — the workers band (`wk_*`) was removed (see "Removed: nationalist / street hypothetical branches" below).
* `vie_col.8`: appears once during the civil war (20% per month).

## Shortcut menu
The left-hand buttons are 17, not 11: Doi Moi root, anti-corruption, WTO, banks, state groups, roads, army,
East Sea, ASEAN, digital, alternative paths, and one per military column (army/navy/air/defence-industry) plus
rule-of-law and bilateral-diplomacy (`common/national_focus/VIE_md_focus.txt`, the `shortcut = { ... }` blocks
right after `focus_tree = {`). Click each and check the view lands on the right focus. The "alternative paths"
button (`VIE_alt_paths_shortcut`) is currently broken: its target, `VIE_developmental_state`, does not exist in
the tree any more (a leftover from one of the deleted alt-regime bands) — clicking it should either do nothing or
log an error; either way this is a known game-file bug, not a TESTING.md error, and is not fixed here.

## Leader lifecycle (2026-09-20)
Code: `VIE_create_leader_*`, `VIE_new_leader_*`, `VIE_recreate_general_secretary`, `VIE_create_leader_restored_party`
(common/scripted_effects/VIE_md_effects.txt), `set_leader_VIE` (VIE_political_leaders.txt), `VIE_transition_regime`.
Variable `VIE_gs` = current General Secretary (1 Phieu, 2 Manh, 3 Trong, 4 Dung, 5 To Lam, 0 none).
1. New game, check the leader on 1/2000 is Le Kha Phieu, and after the Ninth Congress (4/2001) Nong Duc Manh.
   Names come from loc keys `VIE_leader_*`; if the leader panel shows the raw key, `create_country_leader` does
   not localise `name` in this build: replace the keys with plain strings.
2. During Party rule run an MD effect that calls `set_leader` (e.g. `event` any MD election/reshuffle, or console
   `effect set_leader = yes` if available): the General Secretary must come back, not a random generated leader.
3. Edge Junta -> Party: take `VIE_national_salvation_council`, then `VIE_restore_civilian_rule` option back to the Party.
   Expect: leader "Hoang Van Tuan" (fictional), `VIE_congress_controls_leader` cleared on leaving and not set,
   `VIE_gs = 0`, Congress chain running again (VIE_party_rule_active).
4. Democracy, second election: win with party 2, lose to 1, win again with 2: each change must give that
   party's fictional leader (counters are reset at the top of set_leader_VIE), never a random one.
5. Enter any regime twice (e.g. populist 20 -> junta 22 -> back to 20): leader of 20 is recreated.
6. `vie_col.6` option D text is now key `vie_col.6.e` (the old key collided with the event description).

## Four Nos doctrine / state fixes (2026-09-20)
1. Take `VIE_four_nos_doctrine` (needs VIE_four_nos, i.e. after 11/2019), then `VIE_pivot_to_the_west` (or console
   `event vie_int.10` option B): both `VIE_four_nos` and `VIE_four_nos_doctrine_idea` must disappear.
   The removal comes from `cancel = { NOT = { has_idea = VIE_four_nos } }` on the doctrine idea.
2. `VIE_lb_bac_van_phong` now builds in state 519 (Khanh Hoa), not 521.

## E-branch fixes (2026-09-20)
1. `VIE_shipyards`: dockyard now in state 522 (Hai Phong). State 524 has no coastal province, so the old dockyard could never build.
   Check: take the focus, 522 gains a dockyard (state view).
2. `VIE_provincial_defence_zones`: now builds level-1 bunkers on the border provinces of 523, 524 and 520
   (`province = { all_provinces = yes limit_to_border = yes }`). Check in the map view that bunkers appear on the
   China/Laos/Cambodia border provinces. If a state gets none (no province flagged as border by the engine) nothing is built and no error appears.

## Military branch E1-E6 + doctrine paths (2026-09-20)
Static check first: `python3 tools/check_static.py` (must print 0 errors).
Files: focus (VIE_md_focus.txt: E1-E6 rewards, +4 focuses), ideas p2 (rewritten + 10 new), scripted_effects/VIE_md_effects_p12.txt
(deliveries), events vie_dip.16 (p7), vie_scs.16/19 (p11), decisions (VIE_military_category, 3 switch decisions),
localisation/english/replace/VIE_md_vi_military_l_english.yml. The alternative-regime band of the tree moved down 3 rows to make room.
1. Tanks/planes: with NSB `medium_tank_chassis_2` (T-90 focus), without `MBT_4`; Su-30/Yak-130 use the By Blood Alone branch, otherwise
   `AS_Fighter2` / `L_Strike_fighter2`. Open the equipment stockpile screen after each focus. If the amount is 0 the producer/variant
   combination did not match (SOV variant "T-90"/"Su-30"/"Yak-130"): change `producer` or drop it.
2. **[Superseded 2026-10-02: p12 was removed, ships now come from the naval procurement axis, see "Naval procurement" above.]** Ships (VIE_event_scheduler_p12): sign `VIE_gepard_frigates` and `VIE_kilo_submarines` and jump the date (console `date 2011.6.1`,
   then 2014.8, 2015.1 ... 2017.2, one month at a time): 2+2 Gepard, six Kilo one by one. After the sixth boat idea
   `VIE_kilo_flotilla_idea` appears. Names "Dinh Tien Hoang", "Ha Noi" ... show in the navy screen.
3. Buildings: Cam Ranh naval base +2 (province 10162, state 519), coastal bunkers 10162 and 10309 (Bastion), 522 radar/AA/dockyard,
   518 naval base (province 1423, coast guard law), 801 radar (DK1) and bunkers/air base/AA (Spratly fortification, needs date > 2020.12.31).
4. Arms export: `VIE_arms_export` sets `VIE_arms_export_active`; one treasury payment per year for five years.
5. vie_dip.16 (after `VIE_fighter_replacement`): option A Su-30 stock, B Gripen (needs VIE_us_arms_open), C home fighter tech if `VIE_dual_use_industry`.
6. vie_scs.19 fires 90 days after `VIE_legal_warfare`; `VIE_limited_war_doctrine` cuts the war clock of vie_scs.16 to 60 days.
7. Armed forces development (design v2, replaces the old three exclusive doctrine paths). Root `VIE_defence_strategy_review`
   (after 2009) opens three branches: army (`VIE_army_development`, needs `VIE_modernize_vpa`), navy (`VIE_navy_development`,
   needs `VIE_navy_modernization`), air (`VIE_air_development`, needs `VIE_air_force_modernization`). Each branch has one fork:
   army `VIE_path_peoples_war` vs `VIE_army_expeditionary`; navy `VIE_path_maritime_denial` vs `VIE_navy_blue_water`;
   air `VIE_air_superiority_ops` vs `VIE_air_deep_strike`. `VIE_path_self_reliant_deterrence` now sits under `VIE_dual_use_industry` (E4).
   Small bonuses are added to the dynamic modifier `VIE_armed_forces_modifier` (variables `VIE_af_*`): after the first focus the national
   modifier list must show ONE "Quan doi Nhan dan Viet Nam" entry and grow as focuses are taken (not one entry per branch).
   Check: the fork partner turns grey after one is taken; `VIE_army_logistics_reform` opens after either army fork;
   `VIE_army_iron_triangle` needs jungle warfare AND logistics AND `VIE_reserve_mobilization`; `VIE_air_full_spectrum` needs the three
   air focuses AND `VIE_air_dominance_coast`. Buildings: 521/523 anti-air (layered SAM), 519 radar (early warning),
   naval bases at province 11134 (state 801) and 4223 (state 518). The three `VIE_switch_doctrine_*` decisions are gone.
   `reduce_focus_completion_cost` (cost = 14) makes the listed follow-up focuses cheaper: verify the direction in the focus screen.
   Old saves that already took one of the previous `VIE_path_*` focuses may show a strange tree: start a new game.
8. Four Nos: after taking Cam Ranh (capstone) or the Four Nos doctrine, `VIE_pivot_to_the_west` must remove those ideas as well.

## Path C tension dial (2026-09-20)
1. `VIE_assert_maritime_rights` now opens at tension >= 2 OR (idea `VIE_maritime_denial_idea` and tension >= 1).
   Take `VIE_path_maritime_denial` (adds +1 tension): the assert focus must become available at once (legal_warfare not taken).
2. Decisions (category "Chien luoc quan su", visible only with the maritime-denial idea): `VIE_scs_patrol_disputed_waters`
   (50 PP, every 180 days, tension +1, naval XP, CHI opinion down; hidden while the populist balance is active, unavailable at tension 3 or at war with CHI)
   and `VIE_scs_deescalate` (25 PP, tension -1). Console `set_variable VIE_scs_tension = 2` style checks: at 3 the clash event vie_scs.16 fires once.
3. Known gap: tension never decays by itself (plan v6 promised a slow decay that was not coded). Not added on purpose; decide after playtesting.

## Deep military expansion (2026-09-20, +72 focus -> 485 total)
Generator lives OUTSIDE the mod: `D:\HOI4Mods\_gen` (lib.py, blockA/B/C/DE.py, variants.py, variant_map.py, infra.py, overview.py).
Re-running `python3 blockX.py` rewrites the block between `# ==== GEN:X begin/end ====` markers in the focus file and its loc/idea files.
1. Load: error.log must have no `VIE`/`vie_` lines; setup.log lists `VIE_md_ideas_p3A/B/C/DE` and the MIO file.
2. Army block (18): `VIE_army_nco_corps` .. `VIE_army_vpa_2030`. Templates "Su doan bo binh co gioi", "Lu doan dac cong", "Lu doan vien chinh"
   are created by `VIE_army_mech_corps`, `VIE_army_combat_engineers`, `VIE_army_exp_brigades` (units spawn in the capital). Peoples-war side:
   dan_quan_modern -> underground_bases -> border_guard_corps; expeditionary side: exp_brigades -> exp_hubs -> intervention_force. Capstone needs one of the two ends.
3. Navy block (18): `VIE_navy_naval_regions` .. `VIE_navy_vn_navy_2030`. Blue-water only (needs `VIE_navy_blue_water`): blue_destroyers, replenishment,
   light_carrier, spratly_fleet. Denial only: usv_uuv. Marines create the "Lu doan hai quan danh bo" template + unit 147.
4. Air block (18): `VIE_air_divisions` .. `VIE_air_air_2030`. Strategic-strike chain (sead -> alcm/long_strike -> strat_reach) needs `VIE_air_deep_strike` (excludes superiority_ops);
   `VIE_air_superiority_wing` needs `VIE_air_superiority_ops`. Check that the fork partner really blocks these via the `available` text.
5. Defence industry (10, `VIE_def_*`) + missiles (8, `VIE_msl_*`). MIO (Arms Against Tyranny only): 4 companies in the Defense Companies window
   (Viettel, GDT/Z factories, Ba Son, VAECO); each `VIE_def_*` company focus adds size/funds/free trait picks. Nuclear chain (`VIE_msl_nuclear_power` ..
   `VIE_msl_deterrent_doctrine`) needs Gotterdammerung, threat > 0.25 for the threshold, rule VIE_alt_history != historical, and the MD special project
   `sp_nuclear_warhead_program` for the last two. Both are hypothetical and gated behind NOT Four Nos.
6. Equipment variants (needs the DLC the MD source used + Arms Against Tyranny, otherwise a stockpile fallback or nothing): sp_artillery, armor_modernization,
   missile_boats, blue_destroyers, submarine_expansion, uav_armed. Watch error.log for "module"/"slot" errors: variants were copied 1:1 from CHI/DEN/GRE/NED focuses.
7. Decisions (category "San sang chien dau"): 6 repeatable decisions with cooldowns (365/365/365/730/540/1095 days).
8. Unverified in game: `add_mio_size`/`free_trait_picks` semantics, `start_equipment_factor` in create_unit, `reduce_focus_completion_cost`, connector look of the long edges.

## Unified military layout (2026-09-20)
`D:\HOI4Mods\_gen\unify.py 4 --write` re-laid ALL military focuses as one super-branch: root `VIE_modernize_vpa` (row 10) -> 4 column heads
(`VIE_tank_modernization` army, `VIE_navy_modernization`, `VIE_air_force_modernization`, `VIE_viettel_military_tech` defence industry) -> feeder tier ->
join node `VIE_defence_strategy_review` (free-floating, gates the 3 development heads) -> doctrine forks -> capstones. Only x/y changed, plus an added
prerequisite `VIE_modernize_vpa` on the 4 heads (already required through `available`, so no gameplay change). Backup: `_backup_v3/VIE_md_focus.pre_unify.txt`.
Check in game: the four heads hang from the root; the tree has ~17 harmless connector-behind-node spots (mostly the old fork cross links).

## Hand-tidied columns (2026-09-20)
Layout now comes from `D:\HOI4Mods\_gen\manual_layout.py` (`python3 unify.py 4 --manual --write`, after regenerating blockA/B/C/DE). Each column is a tidy trunk
(feeders in one row, join node, fork left/right, capstone at the bottom). Connector-behind-node spots: 17 -> 7 (only two-parent fork bars).
Two prerequisites changed for tidiness: `VIE_navy_submarine_expansion` now needs ba_son + coastal_sensors (was ba_son + sub_base; coastal_sensors already needs sub_base or missile_boats);
`VIE_air_air_2030` needs `VIE_air_domestic_radar` and lists maintenance/academy/ew/long_range_sam in `available`. 4 column shortcuts added at the top of the tree.

## Political axis regroup (2026-09-20, focus 485 -> 487)
`D:\HOI4Mods\_gen\political_layout.py` (ORD=01423 python3 political_layout.py 3 --write) moved 86 political focuses to five columns LEFT of the economy block
(x -74..10, rows unchanged): C1 Noi tri & Dang (21), C2 Phap che (4 + new constitution_2013), C5 Chu quyen bien dao & QP toan dan (18), C3 Ngoai giao song phuong (26), C4 Da phuong & thuong mai (17 + new multilateral_champion).
Economy block (x 16..139) and military block untouched; 5 economy-law focuses stay next to their parents (land_law_reform, labor_code_2019, soe_governance, national_digital_transformation, social_insurance_reform),
plus digital_id, population_policy, universal_health_insurance. Focuses with a non-root `relative_position_id` (wto_negotiations, bilateral_trade_agreement_usa, paracel_ultimatum, samsung_partnership) get their x recomputed against their real base.
`_gen/politics_patch.py` (idempotent): 34 BoP effects added, `decrease_corruption` on party_inspection/asset_recovery/state_audit, `VIE_cybersecurity_law` now needs `VIE_constitution_2013` (row 5),
8 display renames (loc only), 2 shortcuts (Phap quyen, Ngoai giao song phuong). `check_static.py` warns when a political-axis focus has no BoP move and is not in BOP_EXEMPT.
In game check: root doi_moi_continues sits at the right end of the political block; C1 first-tier focuses hang from a long bar on row 0; the BoP bar moves after completing e.g. VIE_public_admin_reform;
constitution_2013 opens after rule_of_law_state (date > 2013.10.31); multilateral_champion needs un_security_council + asean_chair + (cptpp_member OR evfta), date > 2021. About 42 connector-behind-node spots (mostly long root bars and cross-column links).

## Review of the state-building batches (2026-09-20)
Bugs found and fixed (script `D:\HOI4Mods\_gen\review_fix1.py`, `review_fix2.py`; backups `_backup_v5\*pre_review*`):
1. `events/VIE_md_axis.txt` called `VIE_enter_regime = { ... }`, a macro that no longer exists (the generator that expanded it was lost): vie_axis.1.a and vie_axis.2.a would have logged "unknown effect". Expanded to the explicit `VIE_transition_regime` sequence. `check_static.py` now flags any undefined `VIE_*` effect/trigger call.
2. Failure edge 1 (Kien tao -> Tai phiet) tested `VIE_developmental_active`, a flag nothing ever sets -> the event could never fire. Now `has_completed_focus = VIE_developmental_state` and not already in slot 15.
3. Regime-root gates required the axis thresholds even when the regime was ALREADY entered (defend_the_foundation, np, junta, sec, sez, oligarch, wa, lac hong, round_table). After an event switched the party slot the root focus could be locked -> dead branch. Now `OR = { ruling_party = X  AND = { axis gate + unlock flag } }`; the Lac Hong gate moved to its door (`vie_alt.15.b` trigger: mob>=9, checks<=-5); round_table_talks needs the axes only on the "from strength" route (ruling_party 19), not after Collapse/junta/1987.
4. Entropy event vie_axis.2 could fire one month after entering Lac Hong (mob<7). `vie_alt.15.b` now sets `VIE_lh_young` for 600 days and the entropy edge waits for it.
5. `corruption_level_07` was tested as an exact level; now 07..10.
6. Faction check gave `intelligence_community` (evicting `farmers`) on the PLAIN historical run (civil -10). Now needs civil<=-8 AND checks<=-2 (same as the An ninh gate) or the security flag.
7. Geddes cost hit 68 focuses (-155 opinion); the plain historical run drove `communist_cadres` to ~0 (-16% army org regain, +12% bureaucracy cost). Now only merit>=2 focuses, at -1 (40 removed, 22 softened).
8. vie_axis.3 (stall) no longer fires after a real election; line endings of the focus file normalised (CRLF); junk moved out of the mod folder (`.bak`, 9 design `.md` -> `D:\HOI4Mods\_docs`).
Verified: the 360 axis effects in the focus file match `axis_map*.py` exactly (0 missing, 0 extra, 0 wrong values); all 11 gates are reachable (random search over the trunk+military focuses).
Known/open: event options that lead to a gated branch (D4, D5, D6...) do not warn that the axis gate may still lock the root; the "replacement route is punished" rule for Collapse -> democracy is not coded; nothing here has been run in game yet (last error.log is from 12:42).

### Review follow-up (2026-09-20, `_gen/review_fix3.py`; backups `_backup_v5\*pre_fix3*`)
1. Gate tooltips: the 20 axis checks on the 10 gated regime roots are wrapped in `custom_trigger_tooltip` (keys `VIE_gate_<axis>_<ge|le>_<n>`, ASCII `>=`/`<=`), showing the current value with `[?VIE_ax_<axis>_norm|0]`.
2. Nine event options that only set an unlock flag (vie_alt.3.b/3.c/6.b/7.b/31.b, the D4 tc/np options, D1 conservative, D5 developmental) now show a note `VIE_gate_note_<branch>` with the thresholds and the current values. Options that already switch the party slot need no note.
3. Democratic transition by route: `VIE_round_table_talks` gives `VIE_negotiated_transition_idea` (5 years, +5% stability, +5% PP gain) when it comes from strength (slot 19 or 0, no collapse), and `VIE_fragile_transition_idea` (-5% stability, -10% PP gain, -5% war support, merit -2) after Collapse/junta/caretaker; `VIE_consolidate_democracy` removes the fragile idea. Route test: `VIE_collapse_done` or a party slot other than 19/0.
4. Geddes cost kept at the softened level (merit>=2 focuses, -1); restoring -2 on all 68 focuses drives communist_cadres to ~0 on the plain historical run.
Check in game: open a gated root (grey) and read the tooltip; pick vie_alt.3.b and read the note; finish round_table_talks after a Collapse and after managed pluralism and compare the idea received.

## State-Building Batches 5-7 Verification (2026-09-21)
Static check: `python3 tools/check_static.py` (0 errors, 128 warnings).

### Batch 5 (Regime Gates & Structural Crisis Events)
- All 11 regime roots are gated by axis conditions + flags / party slots:
  - `VIE_defend_the_foundation` (market_norm < -1, integ_norm < 4)
  - `VIE_developmental_state` (merit_norm > 3)
  - `VIE_tc_strategic_autonomy` (integ_norm < 5, west_norm < 5)
  - `VIE_np_street_mandate` (mob_norm > 6, checks_norm < 1)
  - `VIE_sec_cyber_control` (civil_norm < -7, checks_norm < -1)
  - `VIE_lb_sez_law` (market_norm > 4, decent_norm > 2)
  - `VIE_ol_bailout` (merit_norm < 3, market_norm > 2)
  - `VIE_wa_development_council` (west_norm > 5, merit_norm > 4, checks_norm < -3)
  - `VIE_managed_pluralism` (merit_norm > 6, civil_norm > -7, checks_norm > 4)
  - `VIE_national_salvation_council` (mob_norm > 8)
  - `VIE_lh_ethnic_nationalism` (mob_norm > 8, checks_norm < -4)
- 4 Structural failure/reversal events in `events/VIE_md_axis.txt`:
  - `vie_axis.1`: Developmental state captured by oligarchic interests (`market_norm > 4`, `merit_norm < 2`).
  - `vie_axis.2`: Entropy of extreme right (`mob_norm < 7` after 600 days without war).
  - `vie_axis.3`: Democratization stalls at competitive authoritarianism (`checks_norm < 4` or `merit_norm < 4`).
  - `vie_axis.4`: Multi-dimensional structural crisis warning (`stability < 0.20`, `checks_norm < -5` or `merit_norm < -3`).

### Batch 6 (State-Building Repeatable Decisions)
Category `VIE_statebuilding_category` visible when `VIE_ax_initialized` flag is set:
1. `VIE_civil_service_examination`: merit +1, cadres opinion -5, cost 75, cd 180d.
2. `VIE_provincial_pilot_program`: decent +1, stability +0.01, cost 50, cd 180d.
3. `VIE_streamline_administrative_org`: size -1, calls `decrease_centralization`, cost 100, cd 360d.
4. `VIE_relax_media_scrutiny`: civil +1, checks +1, stability -0.02, cost 50, cd 180d.
5. `VIE_strengthen_internal_discipline`: civil -1, checks -1, stability +0.02, cost 50, cd 180d.
6. `VIE_negotiate_economic_pact`: integ +1, treasury +1, cost 75, cd 240d.

### Batch 7 (Static Checks & Loc Verification)
- Extended `tools/check_static.py` to continuously validate:
  - All 9 statebuilding axis loc keys (names, tooltips, poles).
  - All `custom_trigger_tooltip` keys against `loc`.
  - All variables tested in `check_variable` against known engine/mod variables.
  - All MD spending/budget effects (`increase_*`, `decrease_*`, `change_expected_*_spending`).
- Loc verified: 0 missing keys.
- Backups archived to `D:\HOI4Mods\_backup_v5\`.

## Spacing fix (2026-09-26, `_gen/fix_spacing.py --write`; backup `_backup_v5/VIE_md_focus.pre_spacing.txt`)
The compacted layout had 127 same-row neighbours at dx=1 (focus boxes are ~2 cells wide, so they overlap) and one child above its parent.
Fix: x of the trunk (rows <= 9) and the alt band (rows >= 28) scaled by 2 (columns and connector topology unchanged), the military block moved with the root (+80), one leftover pair repaired by least squares, and the semiconductor chain (`VIE_semiconductor_ambition`, `chip_design`, `chip_engineers`, `semiconductor_fab`, `viettel_global`) moved down 2 rows so every child sits below its parent.
Result: 0 close pairs, 0 same cell, 0 parent-not-above; connector-behind-node spots 152 -> 158 (approximate model). Tree now spans x 14..292, root at (160, 0), military root directly under it at (160, 10).
Check in game: the tree opens on `VIE_doi_moi_continues`; scroll left/right to see the political and economy blocks; no two focus boxes should touch.

## Political branch: 2026 fork + accountability (2026-09-26, `_gen/political_build.py`; backups `_backup_v5/*.pre_political.*`)
Implements the improved plan (`VIE_political_branch_plan_review.md`, section 4). Old focus IDs/costs unchanged; `VIE_era_of_rising` gets one extra prerequisite block (fork) and loses its `checks -2` (moved into `VIE_concentration_of_power`).
- **Fork (row 9, cost 10, mutually exclusive, prerequisite OR two_tier_local_gov/clean_cadres):** `VIE_concentration_of_power` (historical; needs flag `VIE_dual_role_2026`, or non-party rule, or date > 2026.6.30 without `VIE_collective_leadership_2026`, so the historical run is never locked) and `VIE_institutional_opening` (needs `VIE_collective_leadership_2026`, AI factor 0 when `VIE_ai_historical`).
- `vie_pol.9` gets option `.b` (keep collective leadership, sets `VIE_collective_leadership_2026`, AI factor 0 in historical mode). New events `vie_pol.23-26` (immediate effects + delayed crisis after 365+-90 days, only if the matching idea is still active).
- Ideas (`common/ideas/VIE_md_ideas_p3R.txt`): `VIE_unified_leadership_idea`, `VIE_institutional_oversight_idea`, `VIE_era_of_rising_idea_2` (swapped in by `VIE_party_centennial_2030`, now on row 11 under `era_of_rising`).
- New focuses: `VIE_cadre_accountability` (under party_discipline), `VIE_peoples_oversight` (under national_assembly_role, not grassroots_democracy: the latter would draw its connector behind national_assembly_role), `VIE_digital_anticorruption` (under clean_cadres, needs e_government and date > 2021).
- Decisions: 6 old statebuilding decisions now need the matching focus (visible); new `VIE_anticorruption_campaign`, `VIE_public_consultation`, `VIE_cadre_rotation`.
- Loc: `replace/VIE_md_vi_pol2_l_english.yml`. `check_static.py`: 0 errors. Axis SPANs were NOT retuned (delta is +6 checks, +2 merit gross across all focuses).
Check in game: at the fork only the focus matching the 2026 choice is clickable; pick `vie_pol.9.b` (debug: `event vie_pol.9`) to unlock `institutional_opening`; `era_of_rising` must stay reachable after either fork focus; `vie_pol.25/26` fire ~1 year after the fork focus and never if the idea was removed. The new tooltips `VIE_tt_concentration_avail` / `VIE_tt_collective_avail` should read as Vietnamese text.

## Fixes after the first in-game launch (2026-09-26, error.log 20:12-20:36)
- `common/ideas/VIE_md_ideas_p3R.txt` was written with a UTF-8 BOM by `political_build.py`: engine logged `Unexpected token: <BOM>ideas`, the whole file was ignored and all 3 new ideas were "Invalid idea" (1400+ log lines). BOM removed, generator fixed, `check_static.py` now errors on any BOM in script files (`common/**`, `events`, `.gfx`). Only `.yml` needs a BOM.
- Statebuilding decisions: the `has_completed_focus` gate moved from `visible` to `available` (otherwise all 9 decisions are hidden at start and the category disappears). Locked decisions now show greyed out with the focus requirement.
- `VIE_military_rescue_corps` still called the nonexistent `change_military_opinion` (log line 9579); now `change_the_military_opinion` guarded by `has_idea = the_military`. `check_static.py` now scans the focus file for unknown `= yes` effect calls too.
- Not reproduced: `Invalid key name at line 14` in `VIE_md_vi_pol2_l_english.yml` (logged once at 20:12, before the file was regenerated at 20:34; the current file has no malformed line). Re-check `error.log` after the next launch.

## UI polish: statebuilding category (2026-09-26, `_gen/icons_build.py` + `_gen/icons_loc.py`)
- Custom pictograms (TGA 33x32 per decision, 52x40 for the category header) in `gfx/interface/decisions/`, sprites in `interface/VIE_md_decision_icons.gfx` (no BOM). The 9 statebuilding decisions now use `GFX_decision_VIE_<decision id>`; the category uses `GFX_decision_category_VIE_statebuilding_category`.
- Category description: the `<->` glyph is missing from the HOI4 font (rendered as `??`); replaced by a 21-step gauge per axis (`common/scripted_localisation/VIE_md_axis_bars.txt`, called as `[VIE_AxBar_<axis>]`, 21 shared loc keys `VIE_axbar_m10..p10`).
Check in game: icons show (else `error.log` has a texture/sprite error), gauge line for each axis shows a bar and no raw `[VIE_AxBar_...]` text. If the raw text shows, use `[Root.VIE_AxBar_<axis>]` in `VIE_statebuilding_category_desc`.

## Statebuilding decisions not showing (2026-09-26 21:1x)
`error.log` was clean (no VIE errors, dev mod + MD loaded, 19 decisions / 5 categories / p3R ideas loaded). Cause: the decisions file had the focus gate back in `visible` (the `available` fix was lost), so all 9 decisions were invisible at start and the whole category vanished. Re-applied with `_gen/decisions_gate_fix.py` (idempotent; gate lives in `available`, `visible` only has `VIE_ax_initialized`). `political_build.py` no longer touches the gate. Rule: never put a focus requirement in `visible` for every decision of a category.

## Removed: nationalist / street hypothetical branches (2026-09-26, `_gen/delete_nationalism.py` + `reanchor.py`; backup `_backup_v5/pre_delete_alt/`)
- Focuses: `np_*` (14, Populist), `lh_*` (3, Lac Hong), `wk_*` (3, Workers commune) = 20; tree now 487 focuses. 16 Junta/other focuses were positioned relative to `VIE_np_street_mandate`; they are re-anchored on the root with unchanged absolute positions.
- Regimes: Populist (slot 20) and Lac Hong (slot 21) are gone: `VIE_populist_balance` BoP, `VIE_populist_category` + `VIE_np_restore_order`, `VIE_pop_*` effects, `VIE_populist_extreme_trigger`, leaders Lam Van Son / Huynh Tan Loc, 8 ideas, their part in `VIE_transition_regime` / civil-war rebel choice / collapse check / collapse poles.
- Events removed: `vie_alt.15-18, 24, 38, 39`, `vie_int.11`, `vie_news.6`, `vie_axis.2` (+ the axis entropy check #2), option `vie_alt.1.c` (street door). `vie_scs.2.b` keeps its effects minus the dead `VIE_riots_tolerated` flag; `vie_int.2.b` loses the populist-balance call.
- Kept deliberately: the `VIE_NATIONALIST` AI path (drives SCS escalation, Junta gates and military focus weights; description reworded), rebel party 5 logic and `VIE_wk_grievance`, party slots 20/21 (MD defines them).
- Gap left in the alt band where `np_*` stood (x ~ 196-205) and at the right edge; not compacted.
- Check in game: no `error.log` line naming `VIE_np_`, `VIE_lh_`, `VIE_pop_`, `VIE_populist`, `vie_alt.15..18`; the Junta focus tree still opens (its gate `VIE_junta_unlocked` is still set by the security-state door in `VIE_md_alt.txt`); the game rule "Phong trao Dan toc Chu nghia" still works; decision list has no Populist category. **This was true when written; the Junta tree itself was removed in the very next dated entry below, so `VIE_junta_unlocked` no longer gates anything.**

## Removed: Junta, Caretaker government, Monarchy, Green coalition (2026-09-26, `_gen/delete_branches2.py`; backup `_backup_v5/pre_delete_alt2/`)
- Focuses: Junta 8 (`national_salvation_council`, `martial_law`, `military_economy`, `restore_civilian_rule`, `jn_*`), Caretaker `ng_*` 6, Monarchy `mn_*` 10, Green `gr_*` 9 = 33. Tree = 454 focuses; the alt band keeps 8 branches / 106 focuses (defend_the_foundation, tc, developmental_state, round_table_talks, sec, lb, ol, wa).
- Ideas removed (9 + 2 left over from the nationalist round: `VIE_nation_first_idea`, `VIE_federation_of_communes_idea`); events `vie_alt.19, 32-35`, `vie_col.7`, `vie_news.7`, `vie_news.10`; options `vie_col.6.b`; news checks in `VIE_md_effects_p10.txt`; leaders for slots 23 (Monarchist) and 17 (Neutral_green); junta clauses in the axis "Military" faction check; loc for all of it (201 keys + 4 tooltips/notes).
- Edited, not removed: `vie_alt.12.a` (the 15% backlash is now just -3% stability), `vie_col.4.a` (no monarchy flag), `vie_col.6.a` (roadmap to elections, AI chance 100), `vie_soc.16.b` (Hanoi trees: "continue as planned" now gives +25 PP instead of the green unlock).
- Kept on purpose: party slots 13 and 22 as civil-war rebel regimes (rebel choice, leaders, `vie_col.6` options a/c/e still cover winners 13, 22, 19/4, others), the collapse chain, `VIE_gate_security_stability` (door to the security state).
- Not compacted: gaps in the alt band where the removed branches stood (x ~160-210 and ~270-296).
Check in game: no `error.log` line naming `VIE_jn_`, `VIE_ng_`, `VIE_mn_`, `VIE_gr_`, `vie_alt.19`, `vie_col.7`; start a civil war (`event vie_col.2`) and confirm `vie_col.6` shows an option for whichever party wins.

## Trunk redesign: 10 thematic towers + cleanup (2026-09-27, `_gen/trunk_redesign.py` + `_gen/fix_row_order.py`; backup `_backup_v5/pre_trunk_redesign/`)
Reorganised the non-political historical trunk (rows 0-9, abs x>80 -- diplomacy/defense/trade/finance/social/energy/industry/science/vision; the political sub-tree at x<=80 and the military block at rows 10-26 were left untouched) into 10 side-by-side "towers", one per theme, each ordered internally by a 5-pass barycenter sweep (median of parent/child rank, alternating down/up) and centred per row for a pyramid/fan look, with an 8-wide gutter between towers. Only `x` changed; `y`, rewards, icons, costs and loc are untouched.
Order left to right: Quốc phòng & Biển Đông, Đối ngoại, Thương mại & FDI, Tài chính - Ngân hàng, Nông nghiệp, Xã hội (giáo dục/y tế/đô thị/thiên tai), Năng lượng, Công nghiệp - Hạ tầng - GTVT, KHCN & Số hóa, Tầm nhìn 2045.
4 unavoidable cross-tower single links (a focus needs a parent from another theme): `multilateral_champion` (diplomacy, also needs 2 trade-agreement focuses), `net_zero_2050` and the `hcmc_metro -> long_thanh_airport -> north_south_hsr` chain (moved into industry_infra since they're really transport megaprojects, even though their immediate parent `urbanization` is social).
Also fixed while verifying (pre-existing, not caused by this pass): two orphan focuses reparented into a real cluster per user request (`bilateral_trade_agreement_usa` -> child of `fdi_attraction`; `samsung_partnership` -- an electronics/Samsung FDI focus, not a power-plant one despus the "điện" in its name -- -> child of `supporting_industries`); 12 "child not below its own prerequisite" row bugs (`fix_spacing.py`'s cascade, whole file); one impossible triple-AND prerequisite on `north_south_hsr` (redundantly required both mutually-exclusive `hsr_2010_reject` and `hsr_2010_approve`, forcing row>9 -- the `available` block already encodes the same condition, so the prerequisite was dropped).
Also removed per request: the `round_table_talks` / democratic-transition branch (22 focus: `round_table_talks`, `legalize_parties`, `first_free_election`, `consolidate_democracy`, `new_constitution`, `dm_truth_reconciliation`, 16 `dm_*`), plus its event/scheduler tail (`vie_alt.36`, `vie_alt.37`, `vie_news.8`, the coalition-crisis scheduler `VIE_event_scheduler_p9` emptied to a no-op since on_actions still calls it).
Verification: `check_static.py` 0 errors/1 warning (the pre-existing duplicate-loc-key one) on the full 387-focus file.
Note found while checking (not this session's doing): the mod's own file already differs a lot from what this conversation last touched -- `resolution_congress_12/13/14`, an extended political sequence at rows 10-20 (x~176-198, alongside the military block which lives at x~293-350 in the same rows), and the earlier 2026 fork (`concentration_of_power`/`institutional_opening`/`era_of_rising`/`party_centennial_2030`) now sits at rows 18-20 gated by `VIE_two_tier_done` instead of the old `two_tier_local_gov`/`clean_cadres` focuses (removed with a documented "Phase 3 section 8.3" save-compat shim in `on_actions_startup.txt`). None of that was touched by this pass; flagging it only because the focus count (387) is otherwise surprising against this file's own history in `tools/TESTING.md`.
Check in game: open the tree at `VIE_doi_moi_continues`, scroll right past the political columns -- the diplomacy/economy/social/energy/industry section should now read as 10 clearly separated fan-shaped clusters instead of one tangled row.

## Cut the cross-tower connectors (2026-09-27, same trunk redesign)
The 10-tower layout left 3 long horizontal connectors where a focus's hard `prerequisite` pointed into a different tower. Per user feedback ("mỗi thanh nối chỉ nên có nếu quan trọng"), each was judged and fixed without changing what a save actually requires to complete the focus:
- `multilateral_champion` (diplomacy) also hard-required `cptpp_member`/`evfta` (trade_fdi) -- judged not essential to the "multilateral standing" theme; that block moved into its `available` check (`has_completed_focus`), so it's still required to unlock, just not drawn as a tree connector.
- `net_zero_2050` (energy) also hard-required `sustainable_mekong_delta` (social) -- same treatment, moved to `available`.
- `hcmc_metro` hard-required `urbanization` (social) -- this one _is_ the real reason `hcmc_metro`/`long_thanh_airport`/`north_south_hsr` used to sit in the social bucket; rather than drop the requirement, `hcmc_metro` itself moved into the industry_infra tower (it's a transport megaproject like the airport/HSR after it) and its `urbanization` link became an `available` check too. Its own children's other prerequisites (`cai_mep_port`, `lao_cai_haiphong_rail`) were already industry_infra, so the whole three-focus chain is now internal to one tower with zero cross-tower lines.
Result: 0 cross-tower prerequisite connectors left in the 10-tower zone (verified programmatically); `check_static.py` still 0 errors.

## Military redesign — Đợt 1: gộp focus trùng (2026-09-27, `_gen/military_merge.py`; backup `_backup_v5/pre_military_redesign/`)
Theo `VIE_military_redesign_plan.md` mục 3. 44 focus lớp v3 (`_gen/blockA/B/C/DE.py`, không dùng nữa) bị hấp thụ vào 27 focus lớp cũ (giữ nguyên ID/ngày/mutex): hiệu ứng của focus bị gộp (division_template, create_equipment_variant, add_tech_bonus, biến `VIE_af_*`...) được ghép thẳng vào cuối `completion_reward` của focus giữ lại, cost = max(hai bên) + 3, mọi `prerequisite`/`has_completed_focus`/`reduce_focus_completion_cost` trỏ tới focus bị gộp được trỏ lại. 3 "nút nối" của lớp v3 (`army_development`, `navy_development`, `air_development`) cũng bị gộp vào gốc cột tương ứng (`tank_modernization`, `navy_modernization`, `air_force_modernization`); 3 dòng `visible` trong quyết định "Sẵn sàng chiến đấu" đã trỏ lại theo.
Kiểm tra: số lần `add_equipment_to_stockpile`/`division_template`/`create_equipment_variant`/`create_unit` trước và sau bằng nhau (không mất hiệu ứng). `check_static.py`: 0 lỗi, 1 cảnh báo mới `VIE_msl_nuclear_power is not below its prerequisite VIE_air_long_range_sam` (do msl_nuclear_power giờ theo chuỗi tên lửa phòng không đã gộp, hàng bị lệch — sẽ sửa ở Đợt 6 bằng `fix_spacing.py`).
Focus quân sự: 132 → 88 (dự kiến qua các đợt tiếp theo: cộng nội dung lõi mới ở Đợt 2 và các nhánh giả định ở Đợt 3-5 để đạt khoảng 131).
Chưa chạy trong game.

## Military redesign — Đợt 2: nội dung lõi mới (2026-09-27, `_gen/military_core_new.py`, `_gen/mil_lib.py`)
Theo mục 4 của plan. Thêm 6 focus: ngã rẽ nguồn cung vũ khí 3 lựa chọn (`VIE_arms_russia_framework`/`VIE_arms_diversification`/`path_self_reliant_deterrence` đã có, gắn mutex 3 chiều, mở sau 2018), ngã rẽ doanh nghiệp quân đội 2 lựa chọn (`VIE_military_enterprises_core`/`_divest`, sau 2016), ngã rẽ hộ vệ hạm dưới `gepard_frigates` (`VIE_navy_sigma_9814` cần `pivot_to_the_west` hoặc quan hệ tốt với Hà Lan / `VIE_navy_domestic_frigate` cần `shipyards`). Làm dày `corps_restructure` (Nghị quyết 05-NQ/TW: `army_org_factor`, giảm tiêu hao tiếp tế, `size -1`). Thêm thưởng combo A2/AD có điều kiện vào `path_maritime_denial` (đủ `bastion_p_coastal_defence`+`kilo_submarines`+`maritime_militia`+`spratly_fortification`).
`check_static.py`: 0 lỗi, 6 cảnh báo mới (đều là "không nằm dưới cha"/"gần nhau <2" do vị trí x/y tạm — sẽ dồn lại ở Đợt 6).
Công cụ mới `_gen/mil_lib.py`: bản `Focus`/`emit`/`install`/`write_loc` riêng cho các đợt quân sự (khác `_gen/lib.py` vì cần `relative_position_id` tùy focus, không cố định vào gốc thân cây).
Focus quân sự: 343 → 349.

## Military redesign — Đợt 3: nhánh giả định Hải quân + Lục quân (2026-09-27, `_gen/military_hypo_navy_army.py`, `_gen/milpos.py`)
Theo mục B, C của `VIE_military_hypothetical_design.md`. Hải quân: `navy_blue_water` bỏ khóa năm 2028 (dùng `shipyards`+`cam_ranh_port_diplomacy`), khởi động thanh đo `VIE_carrier_readiness`; thêm `VIE_navy_lhd_program` → `VIE_navy_drone_carrier` (lối rẻ, mô hình Anadolu) hoặc `navy_light_carrier` → chọn 1 trong 3 nguồn (`VIE_carrier_ex_russian`/`_stovl_west`/`_domestic`) → `VIE_carrier_air_wing` → `navy_spratly_fleet` (bỏ điều kiện "Bốn Không", thay bằng căng thẳng Biển Đông); thêm `VIE_navy_ssn_lease` (thuê tàu ngầm hạt nhân, cần `msl_nuclear_power` đã có sẵn trong cây + bỏ Bốn Không), `VIE_navy_cam_ranh_access` (mở event chọn đối tác). Lục quân: `VIE_army_hadr_task_force` → `VIE_army_pk_battalion`; `army_exp_brigades` thêm điều kiện phương tiện chở quân; `VIE_army_asean_peace_force` mutex với `army_exp_hubs`; thêm `VIE_army_northern_contingency` → `VIE_army_total_defence` (giữ "Bốn Không", dùng `random_owned_state = { limit = { has_border_with = CHI } }` thay vì đoán ID tỉnh).
Hạ tầng mới: 2 thanh đo (`VIE_carrier_readiness`, `VIE_mandate_legitimacy`, trôi hằng tháng qua `VIE_mil_gauges_monthly` gắn vào `on_monthly` có sẵn), file event `events/VIE_md_mil.txt` (namespace `vie_mil`, 5 event: `.1` cải hoán trễ hạn, `.2` bẫy Chakri Naruebet, `.3` Bắc Kinh phản ứng hạm đội Trường Sa, `.6` chọn đối tác Cam Ranh, `.12` Bóng ma 1979), 2 danh mục quyết định mới ("Hạm đội Xa bờ" 6 mục, "Nhiệm vụ Ngoài Lãnh thổ" 4 mục), 3 ý tưởng mới (`VIE_carrier_upkeep`, `VIE_carrier_idle`, `VIE_hadr_idea`).
Việc rút gọn so với thiết kế: chỉ code 5/8 event mỗi bên (bỏ bớt các event phụ ít quan trọng: sự cố cụ thể cho drone carrier, thương vong PK, sự cố biên giới riêng — có thể bổ sung sau nếu cần); không tạo focus riêng cho "hộ tống/không đoàn nguồn Nga" chi tiết như Su/MiG hải quân, gộp chung vào `VIE_carrier_air_wing`.
Sửa lỗi trong lúc code: cờ nước Thái Lan trong pack này là `SIA` không phải `THA`; 2 chỗ nối `country_event` bằng cách nối chuỗi con (`old` là tiền tố của `new`) làm hàm `edit()` không nhận ra đã áp dụng, chạy script 2 lần từng tạo dòng `country_event` lặp đôi ở `navy_spratly_fleet`/`army_intervention_force` — đã dò và xóa dòng lặp, đồng thời sửa lại thứ tự kiểm tra trong `edit()` (kiểm tra `new` trước `old`) để an toàn khi chạy lại; 3 file script mới (`ideas`, `scripted_effects`, `events`) bị ghi nhầm kèm BOM — đã bỏ.
`check_static.py`: 0 lỗi, 20 cảnh báo (đều là vị trí x/y tạm, dồn vào Đợt 6).
Focus quân sự: 349 → 362.

## Military redesign — Đợt 4: nhánh giả định Không quân + Hạt nhân (2026-09-27, `_gen/military_hypo_air_nuclear.py`)
Theo mục D, E của thiết kế. Không quân: thêm `VIE_air_tanker` (máy bay tiếp dầu, khoảng trống có thật) và `VIE_air_loitering_munitions` dưới `air_deep_strike`; ngã rẽ 3 nền tảng tấn công `VIE_air_su34_strike`/`VIE_air_f16_package`/`VIE_air_kf21_partner`; `VIE_air_hypersonic` ở cuối (cần dự án đặc biệt `sp_hypersonic_missile`). **Giản lược:** nhánh mới này chạy song song với chuỗi `air_long_strike→air_alcm→air_strat_reach` có sẵn (không ép chúng phải đi qua nhau) để tránh rủi ro đứt gãy cấu trúc cũ — cả hai đều là nội dung "học thuyết tấn công chiều sâu" hợp lệ.
Hạt nhân: gắn lại chuỗi có sẵn theo khung pháp lý thật — `msl_nuclear_power` (thực tế) → chọn 1/2: `VIE_nuc_tpnw_champion` (AI lịch sử chọn, khóa hẳn nhánh vũ khí hóa) hoặc `VIE_nuc_fuel_cycle` → chọn 1/2: `VIE_nuc_latent_hedge` (mô hình Nhật/Hàn, ở lại NPT) hoặc `msl_dual_use_threshold` (đổi cha, giữ nguyên là "mô hình Iran") → `VIE_nuc_npt_withdrawal` (chỉ AI chế độ `free` mới đi, có `apply_united_nations_sanctions`) → `msl_minimum_deterrent` (đổi cha) → chọn 1/2 học thuyết: `msl_deterrent_doctrine` (không dùng trước) hoặc `VIE_nuc_ambiguity_doctrine`.
Hạ tầng: mở rộng file gauge (`VIE_air_interop`, `VIE_nuc_progress` 0-3, `VIE_nuc_exposure` 0-100, trôi hằng tháng qua `VIE_mil_gauges_monthly_p2`); thêm 6 event (`vie_mil.21`/`.22`/`.31`/`.34`/`.39`/`.40`); danh mục quyết định "Chương trình Hạt nhân" (5 mục, gồm quyết định **"Thử nghiệm hạt nhân"** đã duyệt — vi phạm CTBT, một lần duy nhất — và lối thoát "Từ bỏ Chương trình" theo tiền lệ Nam Phi/Libya); 2 ý tưởng mới.
Sửa lỗi trong lúc code: cờ Hàn Quốc là `KOR` không phải `ROK`; 2 icon không tồn tại (`GFX_goal_generic_scientist`, `GFX_focus_generic_missile_defense`) đổi sang icon có sẵn; idea picture dùng nhầm tiền tố `GFX_` (idea picture không có tiền tố, khác focus icon) — đổi sang `nuclear_power`; chèn idea mới bị lệch thụt lề (check_static chỉ nhận diện định nghĩa idea thụt đúng 2 tab) và kèm BOM nhầm khi vá tay — đã sửa cả hai.
`check_static.py`: 0 lỗi, 31 cảnh báo (vị trí x/y tạm, dồn vào Đợt 6).
Focus quân sự: 362 → 374.

## Military redesign — Đợt 5: Đa miền + Liên quân (2026-09-27, `_gen/military_hypo_multidomain.py`)
Theo mục F, G. Không gian: `VIE_space_milsat` (nối `earth_observation` ở thân cây, cần dự án đặc biệt `sp_space_program`) → `VIE_space_command` (sau 2030). Không gian mạng: `VIE_cyber_national_shield` ↔ `VIE_cyber_active_ops` (nối `cyber_command` ở thân cây, chọn 1/2). 3 focus liên quân dưới gốc `modernize_vpa`, mọi điều kiện chéo cột đều là `available` (không vẽ dây): `VIE_joint_island_defence`, `VIE_joint_integrated_deterrence`, `VIE_joint_nuclear_triad` (giả định cực cao, chỉ AI chế độ `free` mới đi tới).
Rà lại AI: mỗi ngã rẽ loại trừ nhau ở Đợt 2-5 đều đã có bên "AI lịch sử chọn" (base cao) và bên thay thế (`modifier = { factor = 0 VIE_ai_historical = yes }`) — không cần sửa thêm.
`check_static.py`: 0 lỗi, 31 cảnh báo (như cũ, dồn vào Đợt 6).
Focus quân sự: 374 → 381.

## Military redesign — Đợt 6: bố cục, dọn biến, kiểm tra cuối (2026-09-27, `_gen/fix_spacing.py --write`)
Chạy `fix_spacing.py` trên toàn bộ file: tự động đẩy hàng xuống cho mọi focus có con nằm cùng hàng hoặc trên hàng cha (24 focus mới ở Đợt 3-5 bị lệch hàng do đặt tạm ở Đợt 3-5), giãn lại cột theo tỷ lệ 2x + sửa 18 nút còn chật, dồn khối quân sự theo gốc `modernize_vpa`. Kết quả: 0 same-cell, 0 cặp sát nhau, 0 con nằm trên cha.
Dọn biến `VIE_af_*`: 61 biến khai báo trong `VIE_armed_forces_modifier`, 7 biến chưa từng được focus nào dùng (tồn tại từ trước đợt này, không liên quan các batch mới) — đã xóa, còn lại đúng 54 biến đang dùng. **Không đạt mục tiêu "35-40 biến"** nêu trong plan: con số đó chỉ khả thi nếu gộp bớt các biến ĐANG được dùng (viết lại phần thưởng của hàng chục focus cũ để dùng chung ít biến hơn), việc đó nằm ngoài phạm vi đã làm vì rủi ro cao hơn lợi ích — 54 biến hiện tại không có biến "chết", mỗi biến ứng với đúng một hiệu ứng thật của một focus.
Rà dây nối chéo cột: còn đúng 2 chỗ, cả hai đều có từ trước batch này (`air_air_2030` cần `viettel_military_tech`; `msl_nuclear_power` cần `air_long_range_sam` — hệ quả gián tiếp của việc gộp `msl_missile_defence` vào `air_long_range_sam` ở Đợt 1). Không sinh thêm dây nối chéo cột nào từ nội dung mới (toàn bộ điều kiện chéo cột ở Đợt 2-5 đều dùng `available`, đúng nguyên tắc đã áp dụng cho thân cây).
`check_static.py` cuối cùng: **0 lỗi, 1 cảnh báo** (duy nhất, có từ trước toàn bộ đợt redesign: 5 cặp khóa loc trùng ở nhánh chính trị, không liên quan quân sự).

## Tổng kết Military redesign (Đợt 1-6, 2026-09-27)
- Khối quân sự: **132 → 156 focus** thực (Đợt 1 gộp 44 → 88; Đợt 2 +6 nội dung lõi → 94; Đợt 3 +13 Hải quân/Lục quân giả định → 107; Đợt 4 +12 Không quân/Hạt nhân giả định → 119; Đợt 5 +7 Đa miền/Liên quân → 126; sau đó phát hiện có sai lệch đếm cột vs `check_static` do focus đếm theo toàn file — số focus toàn mod: 387 → 381 (giảm ròng vì Đợt 1 gộp 44, các đợt sau cộng lại 38 focus mới, net −6 trên tổng mod dù riêng khối quân sự tăng)).
- Không còn cặp trùng lặp 1:1 nào giữa lớp cũ và lớp v3 (đã liệt kê trong plan).
- Giữ nguyên toàn bộ nội dung giả định cũ (tàu sân bay, hạt nhân, viễn chinh) và làm sâu thêm theo 4 quân chủng + đa miền, có thanh đo, danh mục quyết định riêng, event, đúng yêu cầu người dùng ("muốn có để chọn lựa, thêm nội dung chi tiết hơn").
- 3 ngã rẽ học thuyết cũ (`path_peoples_war`/`army_expeditionary`, `path_maritime_denial`/`navy_blue_water`, `air_superiority_ops`/`air_deep_strike`) được giữ nguyên và mở rộng thêm nhánh con.
- Chưa chạy trong game (mọi kiểm tra đều qua `check_static.py` — kiểm tra tĩnh, không phải kiểm tra engine thật).
- Save cũ đã hoàn thành các focus bị gộp (44 focus) sẽ mất focus đó — khuyên chơi game mới để kiểm tra.

## Removed: toàn bộ hạ tầng quân sự cũ (2026-09-30, commit `f05cfa1` + bước 0 của Trục 1)

Các mục "Military redesign Đợt 1–6" ở trên là **lịch sử**, không phải test còn sống. Ba file
dưới đây đã bị xoá; mọi ID ghi trong các mục đó đều không còn tồn tại:

| Đã xoá | Từng chứa | Ghi chú |
|---|---|---|
| `events/VIE_md_mil.txt` | namespace `vie_mil`, 11 event (`.1` `.2` `.3` `.6` `.12` `.21` `.22` `.31` `.34` `.39` `.40`) | `f05cfa1` rút còn 1 dòng comment; bước 0 Trục 1 xoá hẳn file |
| `common/scripted_effects/VIE_md_mil_gauges.txt` | `VIE_mil_gauges_monthly`, `VIE_mil_gauges_monthly_p2` | `f05cfa1` rút thành 2 effect rỗng nhưng `on_actions` vẫn gọi mỗi tháng; bước 0 xoá file và gỡ 2 dòng gọi |
| `common/ideas/VIE_md_ideas_mil.txt` | `VIE_carrier_upkeep`, `VIE_carrier_idle`, `VIE_hadr_idea` | `f05cfa1` rút thành `ideas = { country = { } }`; bước 0 xoá file |

Các thanh đo `VIE_carrier_readiness`, `VIE_mandate_legitimacy`, `VIE_air_interop`,
`VIE_nuc_progress`, `VIE_nuc_exposure` **không còn trôi hằng tháng** vì effect gauge đã rỗng
trước khi bị xoá. Đừng gõ chúng vào console expecting một giá trị đang chạy.

45 key loc `vie_mil.*` trong `localisation/english/replace/VIE_md_vi_mil_hypo_navy_army_l_english.yml`
và `VIE_md_vi_mil_hypo_air_nuclear_l_english.yml` **vẫn còn** và giờ là key chết — dọn ở bước 8
của Trục 1 cùng với ~966 key chết khác (xem `VIE_repo_health_report.md` mục 6.4).

## Added: Trục 1 — mua sắm lục quân, bộ khung (2026-09-30, nhánh `truc1-skeleton`, bước 1/8)

Namespace mới `vie_proc_army` trong `events/VIE_proc_army.txt`; scheduler mới
`VIE_event_scheduler_p14` trong `common/scripted_effects/VIE_md_effects_p14.txt`;
gate triggers trong `common/scripted_triggers/VIE_md_triggers_p14.txt`;
rule `rule_vie_alt_procurement` trong `common/game_rules/VIE_md_rules.txt`.
Bảng cờ: `VIE_v9_flag_mapping.md`. Thiết kế và lý do sửa: `VIE_truc1_review_and_plan.md`.

**Trạng thái: bước 1 + 2 + 3 + 4 xong.** Chuỗi 1 (`.1`, `.2`), chuỗi 2 (`.5`, `.6`),
chuỗi 3 (`.8`), chuỗi 4 (`.11`), chuỗi 5 (`.14`–`.16`), chuỗi 6 (`.18`–`.21`) và
chuỗi 7–9 alt-history (`.30`–`.32`, `.35`, `.38`–`.40`) **đã viết thật — HOÀN TẤT** — có title, desc, picture, 2–3 option mỗi event,
`ai_chance` theo `VIE_ai_historical` / `VIE_ai_free` / guard phá sản, và localisation
tiếng Việt trong `localisation/english/VIE_md_events_p14_l_english.yml`.
Người chơi thấy cửa sổ và chọn được. `.6` là class C (giao hàng, `hidden = yes`,
0 option — đúng dạng `vie_pol.1`), cố ý ẩn.

**19/20 event đã viết thật.** Chỉ còn `.6` là `hidden = yes` — và đó là **class C cố ý**
(giao hàng chuyển đổi 100 T-54/55, không có lựa chọn nào để bấm), đúng convention của
`VIE_event_scheduler_p12` (giao tàu Gepard/Kilo). Không còn placeholder, không còn key
loc tạm `"chờ viết"`.

**Q5 đã chốt (2026-09-30): `.15`/`.16`/`.20` CÓ pop-up**, không để im lặng. Người chơi
thấy cửa sổ khi xe về. Hệ quả: 2018 = 7 pop-up, 2019 = 6, 2023 = 6 — xem mục
"Balance sanity" ở đầu file, luật đã nới thành ≤ 7/năm.

Key loc placeholder (khối cuối `VIE_md_events_p14_l_english.yml`) là **key tạm** cho các
event còn ẩn, chỉ để `error.log` sạch. Xoá **từng dòng** khi viết event thật ở bước 4–6;
đừng xoá cả khối một lần.

| Bước | Test | Kỳ vọng |
|---|---|---|
| 1 | Mở game, `error.log` grep `vie_proc_army`, `VIE_proc_`, `VIE_try_proc`, `rule_vie_alt_procurement`, `VIE_event_scheduler_p14`, `MBT_`, `SP_arty`, `SP_R_arty`, `IFV_`, `medium_tank_chassis` | **0 dòng** |
| 2 | Màn hình game rules | có "Việt Nam: Mua sắm quốc phòng giả định" với 2 option |
| 3 | Chơi VIE tới 2005 | **pop-up "Xe tăng cũ từ châu Âu"** hiện ra (không còn ẩn); kho +70 `MBT_1` (hoặc `medium_tank_chassis_0` nếu có NSB) `producer = FIN`; treasury −0.05bn; log có `VIE_proc_reward_t54_finland` |
| 3b | Chọn option A của `.1` | tooltip `VIE_proc_t72_offer_tt` hiện đúng chữ tiếng Việt, cờ `VIE_pl_t72_deal` có |
| 3c | Chọn option B của `.1` | không có cờ `VIE_pl_t72_deal`, `.2` **không bao giờ** nổ |
| 4 | Sau khi chọn A, chờ qua 2006 | **pop-up "Quyết định về 150 chiếc T-72"**; option A → +10 navy XP +10 air XP, opinion POL giảm; option B → −0.40bn, +150 `MBT_2`/`medium_tank_chassis_1` `producer = POL`, +5 army XP |
| 4b | AI chơi VIE ở rule `VIE_alt_history = historical` | AI **luôn** chọn `.1.a` rồi `.2.a` (đúng lịch sử). Ở rule `free` thì đôi khi chọn B |
| 4c | Đang `bankruptcy_incoming_collapse` rồi tới `.2` | AI chọn `.2.a` (hủy) — kiểm tra guard **không** bị đặt ngược: hủy hợp đồng là tiết kiệm tiền nên phải được khuyến khích, không bị `factor = 0` |
| 5 | Hoàn tất `VIE_modernize_vpa` trước 2009 | `.5` `.8` `.14` `.18` mở được; thiếu focus này thì cả 4 chuỗi **không bao giờ** fire và log ghi `window closed unmet` |
| 5b | Tới 2009 với `VIE_modernize_vpa` | **pop-up "Gói nâng cấp T-54 từ Israel"** (3 option) và **"Tên lửa vác vai Igla"** (3 option) hiện ra |
| 5c | `.5` chọn A | −0.05bn; cờ `VIE_t54m3_prototype` **có**; tooltip `VIE_proc_t54m3_prototype_tt` hiện đúng |
| 5d | `.5` chọn B | −0.75bn; cờ `VIE_t54m3_prototype` **KHÔNG có** (D5 khoá); sau ~1095 ngày `.6` chạy **im lặng**: −100 rồi +100 `MBT_1` (NSB: `medium_tank_chassis_0`) `producer = VIE`, `VIE_af_army_armor_defence_factor` +0.02 |
| 5e | `.8` chọn A / B / C | A: −0.35bn + cờ `VIE_igla_license`; B: −0.25bn, **không** cờ; C: không đổi. Cả A và B đều +0.05 `VIE_af_air_defence_factor` — kiểm tra **không cộng dồn** nếu chơi lại |
| 5f | ⚠️ `.6` `add_equipment_to_stockpile amount = -100` | **rủi ro cao nhất bước 3**: nếu kho < 100 xe thì stockpile có bị âm không? Nếu `error.log` báo gì thì đổi sang `destroy_equipment` — cả hai đều chưa xác minh được ngoài máy có HOI4 |
| 6 | Qua 2012 mà chưa có `VIE_modernize_vpa` | log `proc 5 window closed unmet - D5 locked`; cờ `VIE_proc_5_done` có, `VIE_t54m3_prototype` **không** |
| 6b | Qua 2012 **có** `VIE_modernize_vpa` nhưng pop-up bị `VIE_popup_cd` chặn suốt | fallback im lặng: log `VIE_fb_proc_t54m3`, cờ `VIE_t54m3_prototype` **có**, −0.05bn — **đúng convention Class B**, không phải lỗi (xem comment trên `VIE_fb_proc_t54m3`) |
| 6c | Tới 2013 | **pop-up "Súng trường thế hệ mới cho Z111"** (2 option); A → −0.10bn + cờ `VIE_iwi_license`; B → không cờ |
| 6d | ⚠️ `.11` gate theo **ngày** chứ không theo D1 | Q3 chưa chốt: `VIE_proc_gate_z_factories_done` hiện là `date > 2011.6.30`. Khi Trục 2 D1 land thì đổi thành `has_country_flag = VIE_dec_z_factories_done` |

### Variant / equipment — kiểm tra kỹ nhất (xem `VIE_variant_research.md`)

| Bước | Test | Kỳ vọng |
|---|---|---|
| V1 | ⚠️ NSB: `.1` cấp T-54/55 | `type = medium_tank_chassis_0`, `variant_name = "T-55A"`, **`producer = SOV`** (không phải FIN — Phần Lan không có variant T-54/55 trong MD). Xe phải **lắp được vào sư đoàn**, không nằm trần trong kho |
| V2 | NSB: `.2` B cấp T-72 | `medium_tank_chassis_1` + `"T-72M1"` + `producer = POL` |
| V3 | NSB: `.5` B → `.6` chuyển đổi | `VIE_proc_create_t54m_variant` tạo variant **"T-54M"** `producer = VIE`; kiểm `error.log` không báo module/upgrade/model sai; tạo **đúng một lần** (cờ `VIE_t54m_variant`) dù `.6` có chạy lại |
| V4 | NSB: `.15`/`.16` cấp T-90 | `medium_tank_chassis_2` + `"T-90"` + `producer = SOV`. **Không phải `chassis_3`** — báo cáo ghi `_3` là sai, `chassis_2`=1995 mới khớp T-90 |
| V5 | NSB: `.20` cấp K9 | `medium_tank_artillery_chassis_2` + `"K9 Thunder"` + `producer = KOR` |
| V6 | NSB: `.32` B cấp BMP-3 (alt) | `medium_tank_flame_chassis_2` + `"BMP-3"` + `producer = SOV` |
| V7 | **Không có NSB** | mọi nhánh `else` dùng `MBT_1`/`MBT_2`/`MBT_4`/`IFV_3`/`SP_arty_2` — không có `variant_name` |
| V8 | Danh sách variant trong game | "T-54M" xuất hiện trong tab variant của VIE, design team = GDT (`VIE_gdt_manufacturer`) |
| 7 | T-90: qua 2016 với `VIE_modernize_vpa` | **pop-up "Hợp đồng T-90 với Nga"** (4 option). Chọn A → **quốc trái** +1.25bn (kiểm tra `debt`, **không** phải `treasury`); `.15` sau ~1065 ngày, `.16` sau ~1125 ngày |
| 7b | `.15` nổ | **pop-up "T-90 đợt đầu tiên đã về"**; kho +32 `medium_tank_chassis_2` variant `"T-90"` `producer = SOV` (non-NSB: `MBT_4`); `VIE_af_army_armor_attack_factor` = **+0.05**, `VIE_af_army_armor_defence_factor` = **+0.03**, +10 army XP; cờ `VIE_t90_purchased` + `VIE_ev_t90_tanks` |
| 7c | `.16` nổ | **pop-up "T-90 đợt hai đã về"**; kho **+32 nữa** (tổng 64); `VIE_af_army_armor_attack_factor` **vẫn là 0.05, KHÔNG thành 0.10** — đây là lỗi C1 mà `.16` sinh ra để sửa |
| 7d | `.14` chọn B | −2.50bn treasury (không phải nợ); cờ `VIE_t90_batch_large`; `.15` sau ~900 ngày, `.16` sau ~1270 ngày; mỗi đợt **64** xe, tổng 128 |
| 7e | `.14` chọn C | −0.65bn; **chỉ `.15`**, không có `.16`; 32 xe |
| 7f | `.14` chọn D | không xe, không tiền; `vie_def_ind.2` (Trục 2) sẽ không bao giờ nổ |
| 7g | AI ở rule `historical` | AI **luôn** chọn `.14.a` (`add = 200` khi `VIE_ai_historical`) |
| 8 | Bật rule alt, chơi qua 2010 / 2015 / 2016 | log `.30` `.38` `.35`; tắt rule thì **không** có log nào |

### Chuỗi 6 (K9A1) và chuỗi 7–9 (alt-history) — bước 6

| Bước | Test | Kỳ vọng |
|---|---|---|
| K1 | Tới 2023 (hoặc 2021 nếu có `VIE_155mm_study`) với `VIE_modernize_vpa` | **pop-up "Hàn Quốc chào bán pháo tự hành K9"** (2 option) |
| K2 | `.18` chọn A | `.19` nổ sau **900 ngày** (≈08/2025); nếu có `VIE_155mm_study` thì sau **365 ngày** |
| K3 | `.18` chọn B | cờ `VIE_k9_declined`; `.19` **không bao giờ** nổ (bị `trigger` chặn); D8 khoá |
| K4 | `.19` chọn A / B | A: −1.30bn, 20 xe; B: −2.60bn, cờ `VIE_k9_batch_large`, 40 xe. Cả hai → `.20` sau ~365 ngày |
| K5 | `.20` nổ | **pop-up "K9A1 đã về"** (Q5: có pop-up); kho +20/+40 `medium_tank_artillery_chassis_2` variant `"K9 Thunder"` `producer = KOR` (non-NSB: `SP_arty_2`); cờ `VIE_k9_purchased`; tự hẹn `.21` sau ~365 ngày |
| K6 | `.21` chọn A | cờ `VIE_k9_localization` → **mở D8** (Trục 2) |
| K7 | `.21` chọn B | −0.25bn, `VIE_af_army_artillery_attack_factor` **+0.05** |
| K8 | ⚠️ `ai_chance` của `.18` dùng `has_opinion = { target = KOR value > 75 }` | Đã đổi từ cú pháp lồng scope (`KOR = { has_opinion = { target = ROOT … } }`) sang mẫu đã kiểm chứng ở `VIE_md_focus.txt:843`. Kiểm `error.log` không báo trigger sai |
| A1 | Bật rule, tới 2010 | `.30` → chọn A (−0.05bn) → `.31` sau ~180 ngày → `.32` sau ~30 ngày |
| A2 | `.32` chọn A | cờ `VIE_bmp3_lessons` → **D6 còn 1095 ngày** thay vì 1460; +10 army XP; opinion SOV giảm |
| A3 | `.32` chọn B | −0.50bn, +30 `medium_tank_flame_chassis_2` variant `"BMP-3"` `producer = SOV` (non-NSB: `IFV_3`) |
| A4 | Bật rule, tới 2016 | `.35` 2 option; A → −0.40bn, +12 `medium_tank_rocket_chassis_1` variant **`"TOS-1"`** `producer = SOV` (non-NSB: `SP_R_arty_1`) |
| A5 | ⚠️ TOS-1A dùng variant `"TOS-1"` + `chassis_1` | MD có sẵn variant này (`SOV - Russia.txt:3588`) trên `chassis_1`=1985, **không phải** `chassis_2`=2005 như audit đề xuất lúc đầu. Kiểm xe **dùng được trong sư đoàn** |
| A6 | Bật rule, tới 2015 | `.38` → A → `.39` sau ~180 ngày → `.40` sau ~365 ngày |
| A7 | `.40` nổ | cờ `VIE_155mm_study`; opinion FRA giảm; **chuỗi K9 mở từ 2021** và `.19` chỉ chờ 365 ngày |
| A8 | `.38` chọn B | **không** đặt `VIE_155mm_study` (không có lý do gì để VN đi tìm hiểu chuẩn 155mm nếu không đàm phán) → chuỗi K9 vẫn mở 2023 |
| A9 | **Tắt** rule | `.30`/`.35`/`.38` không bao giờ nổ, không log. Bật rule giữa game (vd 2012) thì `.30` (2010) **không** hồi sinh vì đã quá hạn cứng 2011, nhưng `.35`/`.38` vẫn kịp |
| 9 | `effect set_country_flag = { flag = VIE_popup_cd days = 45 }` ngay trước mốc 2009 | chuỗi dời sang tháng sau, **không mất**; cờ `VIE_proc_5_done` chưa có |
| 10 | `effect set_variable = { VIE_catch_up = 1 } VIE_event_scheduler_p14 = yes` | không event nào nổ; `VIE_t90_purchased`, `VIE_k9_purchased`, `VIE_t54m3_prototype`, `VIE_igla_license`, `VIE_iwi_license`, `VIE_ev_t90_tanks` đều **có**; treasury và nợ **không đổi**, kho **không** thêm xe |
| 11 | `add_equipment_to_stockpile` với `producer = SOV` cho `medium_tank_chassis_2` | **cần kiểm tra kỹ nhất**: variant T-90 phải có trong `history/countries/SOV - Russia.txt` của MD, không phải file VIE. Nếu `error.log` báo variant not found thì bỏ `producer` |
| 12 | NSB: chassis vào kho có dùng được trong sư đoàn không | **rủi ro cao nhất của Trục 1**: NSB cần variant đã design. Nếu không dùng được, phải `create_equipment_variant` trong event |
| 13 | `destroy_equipment = { type = MBT_1 amount = 100 }` khi kho < 100 | kiểm tra có đẩy stockpile xuống âm không (`.6`) |

Chưa test được ở bước 1: mọi thứ liên quan D2/D5/D6/D8/D9 (Trục 2 chưa code — cờ
`VIE_t54m3_prototype`, `VIE_igla_license`, `VIE_iwi_license`, `VIE_k9_purchased`,
`VIE_k9_localization`, `VIE_bmp3_lessons` đang được đặt nhưng chưa có gì đọc).

**Đã chốt Q1 = (d), để nguyên có ý:** `VIE_paracel_ultimatum` **vẫn khoá** và sẽ còn
khoá cho tới khi có trục Hải quân. Hai cờ `VIE_ev_kilo_submarines` /
`VIE_ev_bastion_p_coastal_defence` là cờ hải quân / phòng thủ bờ, Trục 1 (lục quân)
không cấp được. **Đây không phải lỗi của bước 1** — đừng grep ra rồi "sửa": focus
cố ý khoá, và gate gốc của nó (`VIE_scs_escalated_trigger`, ngày, quan hệ) vẫn đúng.

Đừng test mở focus này ở bước 1. Muốn xác nhận phần còn lại của chuỗi Hoàng Sa
(`vie_scs.16` trong `VIE_md_p11.txt`, dùng `add_state_claim = 813` + wargoal) thì
dùng console: `focus.autocomplete VIE_paracel_ultimatum`, nhưng biết rằng focus đó
chỉ đi được bằng console chứ không mở tự nhiên.

Khi nào viết trục Hải quân: 2 event ở ID `.50`–`.59` (đã dành sẵn trong
`events/VIE_proc_army.txt`) set hai cờ trên là focus tự mở, không cần sửa gì thêm.
Xem `VIE_v9_flag_mapping.md` mục 3.

## Dọn localisation (2026-09-30, bước 8 của Trục 1)

**2323 → 1886 key. Xoá 514 dòng key chết + xoá nguyên 1 file trùng.**
`verify_all_loc.py` PASS, **0 key trùng** (trước đó: 553).

| Nhóm | Số key | Xử lý | Lý do |
|---|---:|---|---|
| `vie_mil.*` | 43 | **XOÁ** | namespace `vie_mil` không còn — `events/VIE_md_mil.txt` bị `f05cfa1` rút ruột rồi bước 0 xoá hẳn file |
| focus/idea quân sự v7–v11 đã xoá | 396 | **XOÁ** | `VIE_air_*`, `VIE_navy_*`, `VIE_army_*`, `VIE_carrier_*`, `VIE_msl_*`, `VIE_nuc_*`, `VIE_kilo_*`, `VIE_gepard_*`, `VIE_t90_*`, `VIE_su30mk2_*`, `VIE_bastion_*`, `VIE_cam_ranh_*` … |
| 2 decision `VIE_exercise_naval_drill` / `VIE_exercise_air_readiness` | 4 | **XOÁ** | `f05cfa1` xoá decision, loc còn sót |
| **`VIE.<ideology>` — tên đảng** | 8 | **GIỮ** ⚠️ | `VIE.liberalism`, `VIE.socialism`, `VIE.anarchist_communism`, `VIE.Western_Autocracy` (+ `_desc`). HOI4 **tự sinh** key này từ country tag + ideology, không bao giờ xuất hiện trong code. **Xoá là mất tên đảng trên UI** |
| **`VIE_tt_*`** | 29 | **GIỮ** ⚠️ | tooltip cho biến `VIE_af_*` trong `VIE_armed_forces_modifier`. 42/54 biến hiện chưa ai cộng vì focus quân sự bị v11 xoá — nhưng modifier **vẫn đang được gắn** bởi `VIE_modernize_vpa`, Trục 1 vừa dùng lại 4 biến, và **Trục 3 (30 focus modifier) sẽ dùng tiếp**. Xoá giờ = phải viết lại 42 tooltip sau |
| `VIE_axbar_*`, `VIE_ax_*` | 39 → **0 chết** | **GIỮ** | được tham chiếu từ `common/scripted_localisation/VIE_md_axis_bars.txt`. Lúc quét đầu tiên tôi loại nhầm thư mục `scripted_localisation` khỏi corpus nên chúng bị báo chết — đã sửa |

### Xoá nguyên file `localisation/english/VIE_md_p2_l_english.yml` (84 KB, 552 key)

Toàn bộ **552/552** key của file này đều có bản trong `localisation/english/replace/`
(`VIE_md_vi_p2_a/b/c/d`) với **bản dịch khác**. Trong HOI4, `replace/` thắng → file base
là rác thuần. Đã kiểm tra trước khi xoá: **0 key chỉ có ở base**.

Đây là nguồn của 552/553 key trùng. Sau khi xoá: **0 key trùng**.

Pattern `replace/` của repo này là: viết bản dịch thứ nhất vào `localisation/english/`,
rồi tinh chỉnh bằng bản thứ hai trong `replace/`. Cả hai đều tiếng Việt. Từ giờ nên
**sửa thẳng file trong `replace/`** và không tạo thêm bản base mới.

### Thêm 1 key còn thiếu

`VIE_resolution_category_desc` — decision category "Thực hiện Nghị quyết" có `name`
nhưng **không có `desc`**, trong khi 2 category kia (`VIE_statebuilding_category`,
`VIE_military_readiness_category`) đều có. Đã viết, đặt trong
`replace/VIE_md_vi_congress_l_english.yml` cạnh key `name`.

### Sửa xung đột loc key của `.14`

`vie_proc_army.14` là event **duy nhất trong mod có 4 option**. HOI4 dùng hậu tố `.d`
cho cả `desc` lẫn option thứ tư → hai key `vie_proc_army.14.d` trùng nhau, option D sẽ
hiện ra nguyên đoạn mô tả event.

Đã đổi option thành **`vie_proc_army.14.d_opt`**, theo đúng convention của MD:
`events/05_china.txt` → `sino_indian.39` có `desc = sino_indian.39.d` và option thứ tư
`name = sino_indian.39.d_opt`.

**Quy tắc cho mod này:** event có ≥ 4 option thì option thứ tư trở đi đặt `.d_opt`,
`.e_opt`, … — không dùng `.d`, `.e` trần.

### Cách quét lại (script ở `tools/audit/`)

```bash
python3 tools/verify_all_loc.py          # 0 lỗi + đếm focus
python3 tools/audit/live.py         # đối chiếu tham chiếu chéo toàn repo
```

Khi quét key loc chết, **ba bẫy** đã gặp:
1. `_desc` / `_tt` không bao giờ xuất hiện trong code — HOI4 tự suy từ key cha. Phải
   kiểm tra key cha còn sống trước khi kết luận key dẫn xuất là chết.
2. `common/scripted_localisation/` cũng tham chiếu loc key (`VIE_axbar_*`). Đừng loại
   thư mục này khỏi corpus.
3. `VIE.<ideology>` do engine sinh. Không bao giờ xoá.


## Added: Trục 2 — CNQP Lục quân, bước 0–2 (2026-09-30, nhánh `truc1-skeleton`)

Thiết kế và lý do sửa: `VIE_truc2_review_and_plan.md` (Q6–Q9 đều chốt = (a)).

| File | Nội dung |
|---|---|
| `common/scripted_triggers/VIE_md_triggers_p15.txt` | 10 gate, gom mọi quyết định vào một chỗ |
| `common/scripted_effects/VIE_md_effects_p15.txt` | `VIE_event_scheduler_p15` + 9 effect phần thưởng D1–D9 + 3 effect variant + MIO helpers + catch-up |
| `common/ideas/VIE_md_ideas_p15.txt` | 5 idea: 2 của decision (D6, D8) + 3 của focus (Core, Divest, Capstone) |
| `events/VIE_def_ind.txt` | namespace `vie_def_ind` + 4 event nền |
| `common/decisions/categories/VIE_md_categories.txt` | thêm `VIE_def_industry_category` (priority 92, gate `VIE_def_industry_law`) |
| `common/national_focus/VIE_md_focus.txt` | **4 focus mới** dưới `VIE_modernize_vpa` — 260 focus (từ 256) |
| `localisation/english/VIE_md_events_p15_l_english.yml` | 30 key: 4 event + 4 focus + 3 idea + 5 tooltip |

### 4 focus mới (Q6 = a) và layout

```
VIE_modernize_vpa                  abs (266, 1)   [đã có, từng là root mồ côi 0 con]
  └─ VIE_def_industry_law          abs (266, 2)   cost 5,  date > 2008.6.30,  +1 level
       ├─ VIE_military_enterprises_core    (264, 3)  cost 7, ME, level >= 4, +2 level
       └─ VIE_military_enterprises_divest  (268, 3)  cost 7, ME, level >= 4, +1 level, +2 tỷ
                    ▼ (prerequisite OR cả hai)
     VIE_path_self_reliant_deterrence      (266, 4)  cost 10, level >= 8 + đã chọn ngã rẽ
                                                    + (Four Nos hoặc Non-alignment)
```

Đã kiểm bằng `tools/audit/audit.py` + script toạ độ tuyệt đối:
**0 collision · 0 forward-ref · 0 prerequisite cycle · 0 con nằm ngang/trên cha ·
gap 2 nút ngã rẽ = 4 (≥ 2 ✅) · 0 missing x/y.**

Capstone anchor vào `VIE_def_industry_law` (không phải vào một focus ngã rẽ) để rơi
xuống **(266,4)** thẳng hàng với Pháp lệnh và `VIE_modernize_vpa`. Nếu anchor vào
`core` thì nó rơi xuống (264,4), lệch trục giữa của nhánh.

### Nợ bước 0–1 đã trả

`tools/audit/live.py` từng báo `FOCUS refs MISSING=3`
(`VIE_def_industry_law`, `VIE_military_enterprises_core`, `VIE_military_enterprises_divest`)
vì 4 focus thuộc bước 2. **Giờ là 0.** Khối `vie_def_ind.4` (Luật 38/2024/QH15)
trong scheduler p15 **giờ đã chạy được** vì trigger `has_completed_focus =
VIE_def_industry_law` đã có focus thật.

### Test bước 0–2

| Bước | Test | Kỳ vọng |
|---|---|---|
| T1 | `error.log` grep `VIE_def_ind`, `VIE_event_scheduler_p15`, `VIE_gdt_mio`, `VIE_dec_`, `PTH-152`, `XCB-01`, `BM-21M`, `mio:` | **0 dòng** |
| T2 | Cây focus, mở gốc `VIE_modernize_vpa` (x=266) | thấy 4 focus mới, dây nối thẳng, ngã rẽ Core/Divest **ngang hàng** cách nhau 4 ô |
| T3 | `VIE_def_industry_law` trước 01/07/2008 | **xám**; sau ngày đó thì bấm được, cost 5 |
| T4 | Hoàn tất Pháp lệnh | level = 1 (`effect print_variable = { var = VIE_def_industry_level }` hoặc tooltip); **nhóm decision "Công nghiệp Quốc phòng Lục quân" hiện ra** |
| T5 | Level < 4 | cả Core và Divest **xám** với tooltip giải thích |
| T6 | Đạt level 4 | Core và Divest mở; chọn một thì cái kia **biến mất** (ME hai chiều) |
| T7 | Core | level +2, `VIE_def_ind_core_idea`, stability +3%, efficiency +3%, capacity +5%, consumer goods +2% |
| T8 | Divest | level +1, **ngân khố +2 tỷ**, `VIE_ax_market +1`, `VIE_def_ind_divest_idea`, stability −2% |
| T9 | Level 7 | capstone **xám** |
| T10 | Level 8 + đã chọn ngã rẽ + có Four Nos hoặc Non-alignment | capstone mở; đủ 3 điều kiện |
| T11 | Level 8 nhưng **chưa** chọn ngã rẽ | capstone vẫn xám (kiểm `VIE_def_ind_fork_chosen`) |
| T12 | `vie_def_ind.1` 12/2022 và 12/2024 | pop-up Triển lãm; MIO GDT **+100 funds**; opinion SOV và IND +small |
| T13 | Có `VIE_t90_purchased` + D1 xong | `vie_def_ind.2` nổ; MIO GDT **+150 funds**; +10 army XP |
| T14 | Level ≥ 6 sau 2022 | `vie_def_ind.3` nổ **tối đa 5 lần** (Q9=a), mỗi lần **+0.25 tỷ**; sau lần 5 thì dừng hẳn |
| T15 | 2024.6.27 + có Pháp lệnh | `vie_def_ind.4`; **cả 4 MIO** +150 funds |
| T16 | ⚠️ `add_mio_funds` | Q8=a: decision **không** cấp funds, chỉ `add_mio_size`. Kiểm tra MIO GDT size = **+2 sau D1, +1 sau mỗi D2–D7/D9**, tổng **+9** — không bị lên size đôi |
| T17 | ⚠️ `one_state_arms_factory` | Q7=a: D1 gọi 2 lần → treasury **−15 tỷ đúng một lần mỗi nhà máy**, tổng −15 tỷ (không phải −30). Không tự trừ tiền tay |
| T18 | `effect set_variable = { VIE_catch_up = 1 } VIE_event_scheduler_p15 = yes` | không pop-up; level = 9; các cờ `VIE_dec_*_done` có; **không** mất tiền, không được xe, không có nhà máy |
| T19 | Save cũ (trước khi có p15) load lại | `on_startup` đặt `VIE_def_industry_level = 0` và `VIE_def_ind_export_count = 0` → không đọc giá trị rác |

Chưa test được ở bước 0–2: D1–D9 (bước 3–6), 3 variant `PTH-152` / `XCB-01` /
`BM-21M` (bước 3–6).


### Trục 2 bước 3 — D1 và D7 (`common/decisions/VIE_md_def_industry.txt`)

Hai decision đầu tiên, đều `fire_only_once = yes` + `days_remove` + `remove_effect`
theo mẫu `VIE_resolution_category` sẵn có của repo.

| | D1 `VIE_dec_z_factories` | D7 `VIE_dec_bm21` |
|---|---|---|
| `cost` (PP) | 50 | 40 |
| `visible` | `VIE_def_ind_gate_open` (= đã xong Pháp lệnh) | như D1 + `VIE_dec_z_factories_done` |
| `available` | `date > 2008.6.30` + `can_staff_an_arms_industry` + còn slot `arms_factory` | `custom_trigger_tooltip` báo cần D1 xong |
| `days_remove` | 1095 | 730 |
| Tiền | **không trừ tay** — 2× `one_state_arms_factory` = **−15 tỷ** (MD tự trừ 7,5/lần) | **−0,5 tỷ** trong `complete_effect` (tiền nghiên cứu, không phải tiền xây) |
| `remove_effect` | `VIE_d1_reward`: 2 nhà máy, +1 level, MIO +2 size, cờ done · + 2 khối `add_tech_bonus` (30% pháo ×2 uses, 50% `CAT_inf_wep` ×2 uses) | `VIE_d7_reward`: tạo variant `BM-21M` **trước**, đổi 36 BM-21, +5% `VIE_af_army_artillery_attack_factor`, +10 army XP, +1 level, MIO +1 size |

| Bước | Test | Kỳ vọng |
|---|---|---|
| D1-1 | Trước 01/07/2008 | D1 **xám**; tooltip giải thiếu ngày / thiếu nhân lực / thiếu slot |
| D1-2 | Sau 01/07/2008, đã xong Pháp lệnh | D1 bấm được, tốn 50 PP |
| D1-3 | ⚠️ **Q7-a**: chờ 1095 ngày | **2 arms_factory** xuất hiện; treasury **−15 tỷ tổng**, không phải −30. Kiểm tra `one_state_arms_factory` tự trừ 7,5 mỗi lần và `complete_effect` **không** trừ thêm |
| D1-4 | State nào được chọn | **không phải 801** (0 slot). Hai nhà máy có thể ở hai state khác nhau (`random_owned_controlled_state` chạy 2 lần) |
| D1-5 | MIO GDT | size **+2** (không phải +3 hay +4 — kiểm Q8-a: `add_mio_funds` không được gọi ở decision) |
| D1-6 | Level | `VIE_def_industry_level` **+1** |
| D1-7 | Nghiên cứu | thấy 2 khoản bonus: "Hiện đại hóa nhà máy Z — công nghệ pháo" (30%, 2 uses) và "— công nghệ vũ khí bộ binh" (50%, 2 uses). **Tên hiện đúng tiếng Việt**, không phải raw key |
| D7-1 | Chưa xong D1 | D7 **không hiện** (`visible` chặn) |
| D7-2 | Xong D1 | D7 hiện, tốn 40 PP, **−0,5 tỷ ngay khi bấm** |
| D7-3 | Chờ 730 ngày | variant **`BM-21M`** được tạo (kiểm tra trong tab variant, design team = GDT); kho −36 rồi +36 `medium_tank_rocket_chassis_0` (non-NSB: `SP_R_arty_0`) `producer = VIE`; +5% artillery attack; +10 army XP; level +1; MIO +1 size |
| D7-4 | ⚠️ `amount = -36` | Cùng rủi ro `.6` của Trục 1: kho < 36 thì có bị âm không? Nếu `error.log` báo gì thì đổi sang `destroy_equipment` |
| D7-5 | Bấm D1 lần nữa | **không được** — `fire_only_once = yes` |
| D7-6 | Đang `bankruptcy_incoming_collapse` | D1/D7 vẫn **bấm được** (thiếu tiền không chặn, MD tự phát hành nợ); chỉ AI mới bị `factor = 0` |


### Trục 2 bước 4 — D2 (2 biến thể), D3, D4

| | D2 `VIE_dec_stv` | D2 `VIE_dec_stv_fast` | D3 `VIE_dec_pth` | D4 `VIE_dec_ammo` |
|---|---|---|---|---|
| cost | 40 PP | 40 PP | 50 PP | 30 PP |
| `visible` | Pháp lệnh + D1 xong + **KHÔNG** có `VIE_iwi_license` | như vậy nhưng **CÓ** `VIE_iwi_license` | Pháp lệnh + D1 xong | Pháp lệnh + **D3 xong** |
| `available` | `date > 2016.12.31` + chưa started + còn slot | như D2 | `date > 2012.12.31` + treasury > 2 | cần D3 xong |
| `days_remove` | **1095** | **730** | 1460 | 730 |
| tiền | −0,5 (chương trình) + −7,5 (MD tự trừ nhà máy) | như D2 | −2,0 | −1,0 |
| thưởng | `VIE_d2_reward`: 1 nhà máy, 3000 `infantry_weapons_type`, +1 level, MIO +1 size, cờ done · + tech bonus 100% `CAT_infantry_weapons` ×1 | như D2 | `VIE_d3_reward`: variant `PTH-152`, 24 `medium_tank_artillery_chassis_2`/`SP_arty_2`, +1 level, MIO +1 size · + 50% `CAT_self_propelled_artillery` ×2 | `VIE_d4_reward`: `VIE_af_attrition −0.10`, +1 level, MIO +1 size · + 50% `CAT_artillery_ammunition` ×1 |

| Bước | Test | Kỳ vọng |
|---|---|---|
| D2-1 | Chưa có `VIE_iwi_license`, sau 2017 | chỉ **`VIE_dec_stv`** hiện (1095 ngày). `VIE_dec_stv_fast` **không hiện** |
| D2-2 | Có `VIE_iwi_license` (từ `.11` option A của Trục 1), sau 2017 | chỉ **`VIE_dec_stv_fast`** hiện (730 ngày) |
| D2-3 | ⚠️ Bấm một trong hai | cái kia **xám ngay** (`NOT VIE_dec_stv_started`); không thể bấm cả hai |
| D2-4 | Không có race `visible` | cửa sổ `.11` đóng **2015.12.31**, D2 mở **2017.1.1** → cờ license luôn quyết định trước khi D2 hiện lần đầu |
| D2-5 | Xong D2 | +1 nhà máy, treasury −7,5 tỷ (MD tự trừ) + −0,5 tỷ (complete_effect) = **−8 tỷ tổng**; kho +3000 `infantry_weapons_type`; level +1; MIO +1 size |
| D3-1 | Trước 2013 | D3 xám |
| D3-2 | Sau 2013, treasury ≤ 2 | D3 hiện nhưng **xám**, tooltip "Ngân khố trên 2 tỷ" |
| D3-3 | Xong D3 (1460 ngày) | variant **`PTH-152`** tạo (design team GDT); kho +24 `medium_tank_artillery_chassis_2` variant `PTH-152` `producer = VIE` (non-NSB: `SP_arty_2`); −2 tỷ; level +1 |
| D4-1 | Chưa xong D3 | D4 **không hiện** |
| D4-2 | Xong D3 | D4 hiện; bấm tốn 30 PP + −1 tỷ; sau 730 ngày `VIE_af_attrition` = **−0.10** |
| D4-3 | ⚠️ tooltip của D4 | phải hiện "Tổn thất phi chiến đấu: −10%" bằng **tiếng Việt**, không phải raw key `VIE_tt_attrition` (key này mới tạo ở bước 1 vì `attrition_tt` không tồn tại trong MD) |
| CAT-1 | ⚠️ Tab nghiên cứu sau D1/D2/D3/D4 | 4 khoản bonus hiện **tên tiếng Việt**: "Hiện đại hóa nhà máy Z — công nghệ pháo", "— công nghệ vũ khí bộ binh", "Sản xuất súng trường STV — công nghệ vũ khí bộ binh", "Pháo tự hành PTH — công nghệ pháo tự hành", "Đạn pháo nội địa — công nghệ đạn pháo" |
| CAT-2 | ⚠️ `error.log` grep `CAT_` | **0 dòng**. Nếu có `unknown category` thì một token `CAT_*` sai — đã xác minh cả 4 token dùng ở đây (`CAT_artillery`, `CAT_artillery_ammunition`, `CAT_infantry_weapons`, `CAT_self_propelled_artillery`) đều có trong 24 file `common/technologies/` của MD |

**Nợ cũ của repo phát hiện ở bước 4 (không thuộc Trục 2, chưa sửa):**
`VIE_md_organizations.txt:183` liệt kê `CAT_inf_wep CAT_sp_arty CAT_sp_r_arty CAT_at CAT_util`
trong `research_categories` — **cả 5 token này không tồn tại trong MD**. Tổng cộng
**31/41** token `CAT_*` mà repo dùng không có trong `common/technologies/` của MD.
Hệ quả: `research_bonus` của MIO GDT có thể không áp dụng, và `add_tech_bonus`
trong focus cũ có thể không vào đúng category. Cần một đợt rà riêng — danh sách
đầy đủ lấy bằng cách tải 24 file technologies của MD (195 token hợp lệ).


### Trục 2 bước 5 — D5, D6 (2 biến thể), D9: ba decision nối cờ Trục 1

Đây là ba decision **khóa vĩnh viễn** nếu mất cờ từ Trục 1. Đó là ý thiết kế, không phải lỗi.

| | D5 `VIE_dec_t54m` | D6 `VIE_dec_xcb01` | D6 `VIE_dec_xcb01_fast` | D9 `VIE_dec_tl01` |
|---|---|---|---|---|
| cost | 30 PP | 60 PP | 60 PP | 40 PP |
| cờ Trục 1 cần | **`VIE_t54m3_prototype`** (`.5` option A) | **không** | **`VIE_bmp3_lessons`** (`.32` option A, alt) | **`VIE_igla_license`** (`.8` option A) |
| `available` | `date > 2011.12.31` | `date > 2020.12.31` + treasury > 3 | như D6 | `date > 2016.12.31` |
| `days_remove` | 1095 | **1460** | **1095** | 730 |
| tiền | −0,25 | −3,0 | −3,0 | −0,5 |
| thưởng | `VIE_proc_convert_t54m3` (**tái dùng Trục 1**) + level + MIO + 50% `CAT_main_battle_tanks` | variant `XCB-01`, 50 `medium_tank_flame_chassis_4`/`IFV_7`, `VIE_xcb01_mechanized_idea`, level, MIO + 50% `CAT_infantry_fighting_vehicles` ×2 | như D6 | `VIE_af_air_defence_factor +0.03`, level, MIO + 50% `CAT_anti_air` |

| Bước | Test | Kỳ vọng |
|---|---|---|
| D5-1 | ⚠️ `.5` chọn **B** (gói Israel) hoặc **C**, hoặc để mất cửa sổ 2009–2012 | **D5 không bao giờ hiện** trong nhóm decision. Đây là ý thiết kế: báo cáo mục 1.4 ghi *"B thay thế D5 chứ không đi cùng D5"* |
| D5-2 | `.5` chọn A → cờ `VIE_t54m3_prototype` | D5 hiện từ 2012, tốn 30 PP + −0,25 tỷ |
| D5-3 | Xong D5 (1095 ngày) | gọi **`VIE_proc_convert_t54m3` của Trục 1** — cùng effect, cùng variant `T-54M`, cùng modifier. Kiểm tra **không** bị đổi 100 xe hai lần nếu `.6` cũng đã chạy |
| D6-1 | Game lịch sử (rule alt **tắt**) | chỉ **`VIE_dec_xcb01`** hiện, 1460 ngày. `_fast` không hiện |
| D6-2 | Bật rule alt, `.32` chọn A → `VIE_bmp3_lessons` | chỉ **`VIE_dec_xcb01_fast`** hiện, **1095 ngày** |
| D6-3 | ⚠️ Không có race `visible` | chuỗi BMP-3 hết cửa sổ **2011.12.31**, D6 mở **2021.1.1** → cờ quyết định trước ~9 năm |
| D6-4 | treasury ≤ 3 | D6 xám, tooltip "Ngân khố trên 3 tỷ" |
| D6-5 | Xong D6 | variant **`XCB-01`** tạo (design team GDT); kho +50 `medium_tank_flame_chassis_4` variant `XCB-01` `producer = VIE` (non-NSB: **`IFV_7`**, không phải `IFV_5` như báo cáo); idea `VIE_xcb01_mechanized_idea`; `mechanized_attack_factor +5%`; kiểm tra `equipment_bonus` áp cho **`medium_tank_flame_chassis`** chứ không phải MBT |
| D9-1 | ⚠️ `.8` chọn B hoặc C, hoặc mất cửa sổ 2009–2013 | **D9 không bao giờ hiện** |
| D9-2 | `.8` chọn A → `VIE_igla_license` | D9 hiện từ 2017, tốn 40 PP + −0,5 tỷ |
| D9-3 | Xong D9 | `VIE_af_air_defence_factor` **+0.03** → tổng với Igla (Trục 1, +0.05) = **+0.08**. Không cấp equipment (MANPADS) |
| CAT-3 | ⚠️ `error.log` grep `CAT_self_propelled` | **0 dòng**. D3 và D8 từng dùng token này ở bước 4 — **nó không tồn tại trong `common/technologies/`**, chỉ là `research_categories` của MIO. Đã đổi sang `CAT_artillery` |
| CAT-4 | Tab nghiên cứu sau D5/D6/D9 | 3 khoản bonus hiện tên tiếng Việt: "T-54M nội địa — công nghệ xe tăng chủ lực", "XCB-01 — công nghệ xe chiến đấu bộ binh", "TL-01 — công nghệ phòng không" |
| CAT-5 | `add_tech_bonus` có vào **đúng folder** không | D5 → folder Armor; D6 → folder Armor; D9 → folder Anti-Air; D3/D8 → folder Artillery. Nếu bonus hiện ở folder sai thì token `CAT_*` sai |

**Đã xác minh cả 6 token `CAT_*` dùng trong Trục 2** đều có trong 24 file
`common/technologies/` của MD (194 token): `CAT_artillery`, `CAT_artillery_ammunition`,
`CAT_infantry_weapons`, `CAT_main_battle_tanks`, `CAT_infantry_fighting_vehicles`,
`CAT_anti_air`. Danh sách đầy đủ: `tools/audit/md_ref/MD_all_CATS.json`.


### Trục 2 bước 6 — D8 (decision cuối) + hoàn thiện scheduler p15

**11/11 decision đã code.** Trục 2 chỉ còn bước 7 (loc soát lại + trả nợ Q3 + tài liệu).

| D8 `VIE_dec_k9_localization` | |
|---|---|
| cost | 30 PP |
| `days_remove` | 730 |
| `visible` | Pháp lệnh + **`VIE_dec_pth_done`** + **`VIE_k9_purchased`** + **`VIE_k9_localization`** |
| tiền | −0,5 tỷ |
| thưởng | `VIE_k9_localization_idea` (research_bonus `CAT_artillery` 0.50 + artillery attack 2%), MIO +1 size, **không** cộng level |
| tech bonus | 50% `CAT_artillery_ammunition` ×1 |

**Điểm thiết kế:** D8 **không cộng `VIE_def_industry_level`** — báo cáo mục 2.2 ghi rõ,
và điều này giữ đúng số học mục 2.4 (tối đa 11 Core / 10 Divest). Nếu D8 cũng cộng thì
thành 12/11 và mốc capstone ≥ 8 sẽ trượt.

`VIE_k9_localization` đặt trong **`visible`**, không chỉ trong `available`. Lý do: đó là
**điều kiện nội dung**, không phải cờ chống bấm lại như `VIE_dec_stv_started`. Nếu chỉ để
trong `available` thì decision sẽ hiện lên rồi nằm xám mãi mà người chơi không biết vì sao.
Giờ nó chỉ hiện khi đủ cả ba cờ — đúng cách D5 và D9 xử lý.

**Hai lỗi sửa trong scheduler `vie_def_ind.3` (bản nháp bước 1):**
1. **Không tôn trọng `VIE_popup_cd`** trong khi `.1` `.2` `.4` đều tôn trọng → `.3` có thể
   nổ sát ngày một event khác, phá luật "không hai pop-up trong 45 ngày".
2. **Tăng `VIE_def_ind_export_count` trước khi event fire** → nếu event bị chặn thì vẫn mất
   một lần trong trần 5, người chơi chỉ được **4 lần thật**. Giờ biến tăng trong `immediate`
   của event, đúng nguyên tắc "cờ/biến chỉ đặt khi event THỰC SỰ fire" của Trục 1.

Đã mô phỏng: scheduler đọc `count < 5` → fire → event tăng lên 5 → lần sau chặn. **Đúng 5 lần.**

`vie_def_ind.2` **cố ý không có fallback và không có hạn chót**, khác `.1` và `.4`.
Lý do: điều kiện của nó là **hai cờ** (không phải ngày), và cờ một khi đã đặt thì không mất.
Nếu `VIE_popup_cd` đang bận thì khối này chờ tick tháng sau — tự thành vòng lặp cho tới khi
nổ. Thêm fallback ở đây sẽ cấp funds sớm hơn người chơi đáng lẽ được thấy.

| Bước | Test | Kỳ vọng |
|---|---|---|
| D8-1 | Thiếu một trong ba cờ | D8 **không hiện** (không phải hiện rồi xám) |
| D8-2 | Đủ ba cờ | D8 hiện, tốn 30 PP + −0,5 tỷ |
| D8-3 | Xong D8 | idea `VIE_k9_localization_idea`; kiểm tra research bonus **`CAT_artillery` 50%** hiện trong tab Artillery (không phải `CAT_self_propelled_artillery` — token đó không tồn tại) |
| D8-4 | ⚠️ Level sau D8 | **không tăng**. Kiểm tra: D1+D2+D3+D4+D5+D6+D7+D9 = 8 decision cộng level, D8 thì không |
| D8-5 | ⚠️ Tổng level tối đa | Core: Pháp lệnh 1 + 8 decision + 2 = **11**. Divest: 1 + 8 + 1 = **10**. Không phải 12/11 |
| X3-1 | `vie_def_ind.3` khi level ≥ 6, sau 2022 | nổ **tối đa 5 lần**, mỗi lần +0,25 tỷ, cách nhau ≥ 365 ngày |
| X3-2 | ⚠️ `VIE_popup_cd` đang bận | `.3` **dời sang tháng sau**, và **không** mất một lần trong trần 5 |
| X3-3 | `.3` lần thứ 6 | **không nổ nữa** (`VIE_def_ind_export_count = 5`) |
| X2-1 | `vie_def_ind.2` khi `VIE_popup_cd` bận | chờ tick tháng sau rồi nổ — **không mất**, vì không có hạn chót |


### Trục 2 bước 7 — trả nợ Q3 + soát lại toàn bộ (HOÀN TẤT Trục 2)

**Q3 đã trả.** `VIE_proc_gate_z_factories_done` đổi từ gate tạm `date > 2011.6.30`
sang **`has_country_flag = VIE_dec_z_factories_done`** — đúng như báo cáo mục 1.4 muốn
("Trigger: D1 đã xong").

⚠️ **Gate mới CHẶT HƠN gate tạm, và đó là điểm quan trọng.** Gate tạm (ngày) luôn đúng
từ 07/2011 bất kể người chơi có bấm D1 hay không → `.11` luôn nổ, license luôn có,
D2 luôn là bản 730 ngày → người chơi **không bao giờ phải chọn thứ tự**. Gate mới
khôi phục đúng ràng buộc: muốn license sớm thì phải ưu tiên D1.

| Bước | Test | Kỳ vọng |
|---|---|---|
| Q3-1 | Bấm D1 ngày 01/07/2008, chờ 1095 ngày | `VIE_dec_z_factories_done` có từ **07/2011** |
| Q3-2 | Tới 2013 | `.11` nổ (pop-up "Súng trường thế hệ mới cho Z111") |
| Q3-3 | ⚠️ **Không** bấm D1, chờ tới 2016 | `.11` **hết cửa sổ** → log `proc 11 window closed unmet - D2 stays at 1095 days`; D2 là bản **1095 ngày** |
| Q3-4 | Không có race | D1 xong sớm nhất 07/2011, `.11` mở 01/2013 → dư ~18 tháng |
| LOC-1 | `python3 tools/verify_all_loc.py` | PASS, **1959 key**, 0 lỗi, 260 focus, 0 thiếu name/desc |
| LOC-2 | Key trùng | **0** (đã dọn 553 → 0 ở Trục 1 bước 8) |
| LOC-3 | BOM + format dòng | 40/40 file loc có BOM, 0 dòng sai format, 0 key giá trị rỗng |
| NUM-1 | ⚠️ Tổng level tối đa | Core **11**, Divest **10** — khớp báo cáo mục 2.4 |
| NUM-2 | ⚠️ Tổng tiền | 8 decision cố định **30,25 tỷ**; cả 9 **30,75 tỷ** — khớp báo cáo mục 2.2 và V |
| NUM-3 | ⚠️ Timeline | D1 07/2011 · D7 06/2013 · D5 12/2014 · D3 12/2016 · D4 12/2018 · D2/D9 01/2019 · D6 12/2024 — khớp báo cáo mục 2.5 |
| AUD-1 | `python3 tools/audit/audit.py` | 0 dangling · 0 forward-ref · 0 cycle · 0 missing x/y |
| AUD-2 | `python3 tools/audit/prov.py` | TỔNG HỢP LỖI: 0 |
| AUD-3 | `python3 tools/audit/ev.py` | 0 event thiếu loc · 0 orphan · 0 id trùng |
| AUD-4 | `python3 tools/audit/live.py` | 0 missing ở mọi nhóm (trừ dòng DYNAMIC MODIFIERS là dương tính giả đã biết) |

**4 TODO còn lại trong code — tất cả đều cần máy có HOI4, không phải nợ code:**

| Chỗ | TODO |
|---|---|
| `VIE_md_effects_p14.txt:105` | `.6` dùng `amount = -100`; thử cả `destroy_equipment`, cái nào không ghi `error.log` thì giữ |
| `VIE_md_effects_p14.txt:181` | Igla/TL-01 đang dùng `VIE_af_air_defence_factor`; đổi sang `enemy_army_bonus_air_superiority_factor` nếu xác nhận modifier đó tồn tại |
| `VIE_md_effects_p15.txt:218` | D7 cũng dùng `amount = -36` — cùng rủi ro với `.6` |
| `VIE_md_def_industry.txt:508` | ghi chú chéo cho TODO ở trên |

**Trục 2 HOÀN TẤT:** 11/11 decision · 4 focus · 1 category · 5 idea · 4 event ·
scheduler p15 · 4 variant tự tạo · 6/7 cờ Trục 1 đã nối.

## Naval force and Program 1B (Truc 3 hai quan, buoc 0-9)

Thiet ke: `VIE_naval_truc3_review_and_plan.md`. Chua chay trong game. Static: `python tools/gen_p1b.py` (sinh lai 1B),
`python tools/audit/nf_balance.py` (PASS), `verify_all_loc.py`, `tools/audit/live.py` (0 tooltip thieu), `audit.py` (0 forward-ref, 0 cycle).

### Chuoi focus va Decision luc luong
| # | Thao tac | Ket qua mong doi |
|---|---|---|
| NF-1 | Mo cay focus | Cot hai quan x 240 duoi `VIE_modernize_vpa`; T1..T9 thang hang; ba nhanh o y 9-12; duong ke tu T6 toi `VIE_naval_mro` / `VIE_small_combatant_construction` doc duoc |
| NF-2 | Chon D1 (Denial) roi xem G1, B1 | G1 va B1 xam (mutually exclusive) |
| NF-3 | Bam `VIE_nf_d1_surface` (T3 xong) | Tru 50 PP, event `.1` roi `.2`; tru 0,40 hoac 0,60 ty; idea `VIE_nf_prog_surface` hien; 365 / 548 ngay sau `.61` va modifier xuat hien trong `VIE_armed_forces_modifier` |
| NF-4 | Bam `VIE_nf_d2_submarine` | `VIE_nf_sub_prep` dat ngay o `.10`; chi phi 0,30 / 0,45 (lich su) hoac 0,50 / 0,75 (som) |
| NF-5 | Bam D-A va D-B cung luc, roi D-C | D-C xam ("it hon 2 chuong trinh") cho toi khi mot cai xong; D-C can ca `VIE_nf_d1_done` va `_d2_done` |
| NF-6 | D-C: sau 183, 365, 548 ngay | `.50` (XP + coordination 2%), `.51` (2%), `.63` (2% + sub defence 2%) |
| NF-7 | D-D chon Coastal roi chon nhanh B1 (Bluewater) | Idea phat `VIE_nf_branch_mismatch_idea` 365 ngay; chon D1 (Denial) thi +1% to chuc |
| NF-8 | Kilo: co `VIE_nf_sub_prep` | Goi huan luyen 0,15 ty/tau (khong co: 0,2) |
| NF-9 | Noi chien (`VIE_collapse_aftermath`) | `VIE_var_force_program_active` va `VIE_var_procurement_1b_active` ve dung so timed idea con lai |

### Chuong trinh 1B (P1-P4, P6-P8, P10, P11)
| # | Thao tac | Ket qua mong doi |
|---|---|---|
| P1B-1 | Hoan T8 (>= 2016), bam `VIE_p1b_corvette` | Event `vie_p1b.1` (so luong 2/4/6), `.2` (nhap khau/hybrid/noi dia theo dieu kien), tru tien khi ky |
| P1B-2 | Thieu von | `vie_p1b.3`: cat quy mo / vay (no x 1,1) / hoan / huy; hoan khong mat slot; huy dat `_cancelled` |
| P1B-3 | Sau lead (900/1080/1260 ngay cho P1) | Tau dau den, moi tau cach 240 ngay; `VIE_var_hulls_delivered` +1; exp Truc 2 theo muc noi dia hoa; tau cuoi giai phong slot |
| P1B-4 | `error.log` | **Rui ro cao nhat:** khong co "equipment_variant does not exist", khong loi module/slot; variant co `allow_without_tech = yes` |
| P1B-5 | Mo man hinh thiet ke | Variant `VIE Corvette Class` ... `VIE SSN Class` co du module; P8 (destroyer) la bo module tu ghep, de kiem ky |
| P1B-6 | P11 | Can `VIE_nuclear_research`; module `module_sub_early_reactor_power` hien; `tech_nuclear_power_systems_1` duoc cap |
| P1B-7 | P6 (Bastion-P mo rong) | Moi lan giao dat 1 bunker; kiem tra khong loi khi chong len Bastion Truc 1 o cung tinh |
| P1B-8 | P8 + P10 xong, hoan B5 | `VIE_nf_d5_carrier_group` mo (can 1 tau san bay va 2 khu truc); thuong nhan 0,25 / 0,5 lan thuong B5 |
| P1B-9 | AI free-mode | Decision 1B chi AI `VIE_ai_free` bam; moi event AI co it nhat mot lua chon duoc |
| P1B-10 | `python tools/audit/nf_balance.py` | PASS: tran modifier moi duong (org 18, coord 20, detect 15, range 25, ...), tong 1B toi da 24,5 ty |

### Dang cho kiem trong game (khong phai no code)
Thong so thang `VIE_nf_*` la gia tri khoi diem; ngay co moc T5 (Lu doan 162/167), Lu doan 189 (2013 vs 2011) va T1 (2005) chua xac minh;
`navy_personnel_cost_multiplier_modifier` mau/don vi chua kiem; bunker P6 chong len Truc 1.
