# Con đường Kiên định: kế hoạch code

Đi kèm tài liệu nội dung [Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md](Con_duong_Kien_dinh_noi_dung_cay_focus_v2.md) (gọi tắt là "ND"). Bản 04/10/2026.

Chia 6 giai đoạn. Mỗi giai đoạn chạy được và kiểm tra được độc lập, nên có thể dừng giữa chừng mà mod không hỏng.

## 0. Quy ước

| Loại | Quy ước | Ví dụ |
|---|---|---|
| Focus | `VIE_hl_*` | `VIE_hl_unity_of_will` |
| Idea | `VIE_hl_*_idea` | `VIE_hl_ideology_work_idea` |
| Event | namespace `vie_hl` | `vie_hl.1` |
| Biến | `VIE_rp` (Áp lực cải cách) | |
| Cờ | `VIE_hl_*`, trừ `VIE_hardline_unlocked` và `VIE_hardline_retired` | `VIE_hl_rp_recent` |
| Scripted effect, trigger | `VIE_hl_*` | `VIE_hl_add_pressure` |
| Log | Mỗi `completion_reward` và mỗi option có dòng `log = "[GetDateText]: ..."` như file hiện tại | |
| Loc | Tiếng Việt, UTF-8 có BOM, như các file `.yml` khác | |

### Bảng id focus

| ND | Id | ND | Id |
|---|---|---|---|
| H0 | `VIE_hl_unity_of_will` | C1 | `VIE_hl_cyber_ideology` |
| H1 | `VIE_hl_party_rectification` | C2 | `VIE_hl_school_theory` |
| H2 | `VIE_hl_ideological_foundation` | C3 | `VIE_hl_press_planning` |
| H3 | `VIE_hl_cadre_centralisation` | C4 | `VIE_hl_fatherland_front` |
| A1 | `VIE_hl_state_sector_leading` | D1 | `VIE_hl_party_diplomacy` |
| A2 | `VIE_hl_key_sectors` | D2 | `VIE_hl_no_dependence` |
| A3 | `VIE_hl_soe_spearhead` | D3 | `VIE_hl_selective_partners` |
| A4 | `VIE_hl_selective_fdi` | E1 | `VIE_hl_term_review` |
| A5 | `VIE_hl_no_party_business` | X1 | `VIE_hl_steadfast_renewal` |
| A6 | `VIE_hl_five_year_plan` | X2 | `VIE_hl_party_state_fusion` |
| B1 | `VIE_hl_party_leads_army` | X3 | `VIE_hl_handover` |
| B2 | `VIE_hl_army_political_education` | | |
| B3 | `VIE_hl_all_people_defence` | | |
| B4 | `VIE_hl_party_defence_industry` | | |

### File mới

| File | Nội dung |
|---|---|
| `common/scripted_triggers/VIE_md_triggers_hardline.txt` | Trigger `VIE_hl_*` |
| `common/scripted_effects/VIE_md_effects_hardline.txt` | Effect `VIE_hl_*` |
| `common/ideas/VIE_md_ideas_hardline.txt` | Toàn bộ idea của nhánh |
| `common/scripted_localisation/VIE_md_hardline_loc.txt` | `VIE_HlPressureLine` |
| `common/decisions/VIE_md_hardline_decisions.txt` | Decision Hội nghị Trung ương bất thường, decision debug |
| `events/VIE_md_hardline.txt` | `vie_hl.1` đến `vie_hl.8` |
| `localisation/english/VIE_md_hardline_l_english.yml` | Toàn bộ loc của nhánh |

Focus vẫn nằm trong `common/national_focus/VIE_md_focus.txt`, vì đây là cây duy nhất và `check_static.py` chỉ đọc file này.

---

## Giai đoạn 1. Nền tảng: biến, trigger, effect, hiển thị

Mục tiêu: có Áp lực cải cách chạy được, hiện trên tooltip, chưa ai dùng tới.

### 1.1 Trigger (`VIE_md_triggers_hardline.txt`)

```
VIE_hl_in_power = {
	original_tag = VIE
	check_variable = { ruling_party = 4 }
}

# Đường A: tại Đại hội (không cần cờ)
VIE_hl_can_take_power_congress = {
	check_variable = { ruling_party = 19 }
	VIE_hl_bop_leads_conservative = yes	# BoP < -0.3 (bản đầu dùng -0.6 nhưng không đạt được trước 2011)
	NOT = { has_country_flag = VIE_regime_changed_recently }
	NOT = { has_country_flag = VIE_hardline_retired }
}

# Đường B: Hội nghị Trung ương bất thường (cần cờ)
VIE_hl_can_take_power_plenum = {
	VIE_hl_can_take_power_congress = yes
	has_country_flag = VIE_hardline_unlocked
	has_country_flag = VIE_sched_congress_11
}

VIE_hl_pillars_three = {
	custom_trigger_tooltip = {
		tooltip = VIE_hl_pillars_three_tt
		count_triggers = {
			amount = 3
			has_completed_focus = VIE_hl_five_year_plan
			has_completed_focus = VIE_hl_party_defence_industry
			has_completed_focus = VIE_hl_fatherland_front
			has_completed_focus = VIE_hl_no_dependence
		}
	}
}

VIE_hl_pillars_all = {
	has_completed_focus = VIE_hl_five_year_plan
	has_completed_focus = VIE_hl_party_defence_industry
	has_completed_focus = VIE_hl_fatherland_front
	has_completed_focus = VIE_hl_no_dependence
}
```

### 1.2 Effect (`VIE_md_effects_hardline.txt`)

| Effect | Việc làm |
|---|---|
| `VIE_hl_add_pressure` | Đọc `VIE_rp_add` (temp). Cộng vào `VIE_rp`, kẹp 0–100. Nếu dương thì đặt cờ `VIE_hl_rp_recent` 120 ngày. Gọi `VIE_hl_update_pressure_idea`. Có `custom_effect_tooltip` "Áp lực cải cách +N". |
| `VIE_hl_update_pressure_idea` | Gỡ hai idea mức. ≥ 80 thì thêm `VIE_hl_pressure_crisis_idea`, ≥ 56 thì `VIE_hl_pressure_tense_idea`. |
| `VIE_hl_monthly` | Chỉ chạy khi `VIE_hl_in_power`. Không có `VIE_hl_rp_recent` thì `VIE_rp` −1. Gọi `VIE_hl_update_pressure_idea`. Gọi các event phản ứng (giai đoạn 4). |
| `VIE_hl_take_power` | Gọi từ `vie_hl.1` (giai đoạn 2). |
| `VIE_hl_cleanup` | Gọi khi rời đảng 4. Gỡ idea, xóa `VIE_rp`. Nếu temp `VIE_hl_keep_legacy = 1` (X3) thì giữ `VIE_hl_ideology_work_idea` và `VIE_hl_army_party_work_idea`. |

Mẫu cho focus:

```
set_temp_variable = { VIE_rp_add = 6 }
VIE_hl_add_pressure = yes
```

### 1.3 Idea mức áp lực (`VIE_md_ideas_hardline.txt`)

Theo đúng mẫu `VIE_md_ideas_congress.txt` (`allowed = { always = no }`, `cancel_if_invalid = no`).

| Idea | Modifier |
|---|---|
| `VIE_hl_pressure_tense_idea` | `stability_factor = -0.03`, `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_pressure_crisis_idea` | `stability_factor = -0.08`, `country_productivity_growth_modifier = -0.03` |

### 1.4 Hiển thị

- `common/scripted_localisation/VIE_md_hardline_loc.txt`: `defined_text VIE_HlPressureLine`.
  - Không phải hardline: key rỗng.
  - Bốn mức: `VIE_hl_rp_line_1` … `_4`, dạng `\n• Áp lực cải cách: §G[?VIE_rp|0]§! (Ổn định)`. Màu theo mức (§G, §Y, §O, §R). Kèm "khủng hoảng từ 80".
- Sửa `VIE_state_modifier_desc` trong [VIE_md_vi_axis_l_english.yml:3](localisation/english/replace/VIE_md_vi_axis_l_english.yml#L3): thêm `[VIE_HlPressureLine]` sau dòng "Định hướng Đối ngoại".

### 1.5 Tick tháng

[VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt): thêm `VIE_hl_monthly = yes` vào danh sách scheduler, trước `VIE_ax_normalize = yes`.

### 1.6 Decision debug

Category `VIE_hl_debug_category`, `visible = { is_debug = yes }`, chỉ hiện khi chạy game với `-debug`. Gồm các decision:
- Đặt `VIE_rp` = 30 / 60 / 85.
- Ép `vie_hl.1` (lên nắm quyền ngay).

### Kiểm tra giai đoạn 1

- `python tools/check_static.py` không có lỗi mới.
- Trong game, dùng decision debug: tooltip modifier đổi số, đổi màu, idea mức xuất hiện và biến mất đúng ngưỡng. `VIE_rp` giảm 1 mỗi tháng.

---

## Giai đoạn 2. Đường lên nắm quyền

Mục tiêu: người chơi lên được hardline từ Đại hội XI, và hardline không bị nhánh khác cướp quyền.

### 2.1 Event `vie_hl.1` "Nhận quyền" và `VIE_hl_take_power`

```
VIE_hl_take_power = {
	set_temp_variable = { party_index = 4 }
	set_temp_variable = { party_popularity_increase = 0.15 }
	set_temp_variable = { temp_outlook_increase = 0.15 }
	hidden_effect = { change_relative_party_popularity = yes }
	set_temp_variable = { rul_party_temp = 4 }
	VIE_transition_regime = yes
	# transition đặt BoP = 0
	set_power_balance = { id = VIE_party_balance set_value = -0.5 }
	set_variable = { VIE_rp = 20 }
	VIE_hl_update_pressure_idea = yes
	# Lãnh đạo lịch sử không quay lại sau thời hardline
	clr_country_flag = VIE_congress_controls_leader
	clr_country_flag = VIE_trong_third_term
	clr_country_flag = VIE_to_lam_era
}
```

`set_power_balance` cần `left_side`/`right_side` giống [VIE_md_effects.txt:192-197](common/scripted_effects/VIE_md_effects.txt#L192-L197). Phải chép đủ khi code.

Việc xóa `VIE_trong_third_term` và `VIE_to_lam_era` làm các lựa chọn lịch sử ở `vie_pol.6.a`, `vie_pol.7`, `vie_pol.8.a`, `vie_pol.9` không còn hiện. Các lựa chọn dự phòng (`.6.c`, `.8.b`) sẽ thay vào.

### 2.2 Lựa chọn tại Đại hội (đường A)

| Event | File | Thêm |
|---|---|---|
| `vie_pol.4` (XI, 2011) | [VIE_md_pol.txt:112](events/VIE_md_pol.txt#L112) | Option `hl_take` (tên `.b` ở bản đầu đã trùng key mô tả event): trigger `VIE_hl_can_take_power_congress`. Gọi `country_event = { id = vie_hl.1 }`. |
| `vie_pol.5` (XII, 2016) | [VIE_md_pol.txt:137](events/VIE_md_pol.txt#L137) | Option `hl_take` như trên. Option `hl_keep` "Đại hội khẳng định đường lối Kiên định" khi `VIE_hl_in_power`. `.a` và `.b` thêm `NOT = { VIE_hl_in_power = yes }` (`.b` gọi `VIE_new_leader_dung`). |
| `vie_pol.6` (XIII, 2021) | [VIE_md_pol.txt:185](events/VIE_md_pol.txt#L185) | Option `hl_take` (lên nắm quyền), `hl_keep` (khẳng định đường lối). `.a`, `.b`, `.c` thêm `NOT = { VIE_hl_in_power = yes }`. |
| `vie_pol.7` (HNTW 2024) | [VIE_md_pol.txt:233](events/VIE_md_pol.txt#L233) | `trigger` thêm `NOT = { VIE_hl_in_power = yes }` (gọi `VIE_new_leader_to_lam`). |
| `vie_pol.8` (XIV, 2026) | [VIE_md_pol.txt:255](events/VIE_md_pol.txt#L255) | Option `hl_take` (lên nắm quyền), `hl_keep` (khẳng định). `.a`, `.b` thêm `NOT = { VIE_hl_in_power = yes }`. |
| `vie_pol.12`, `.13` (XV, XVI) | [VIE_md_p10.txt:53](events/VIE_md_p10.txt#L53) | Như `vie_pol.8`. |

AI: option lên nắm quyền có `ai_chance = { base = 5  modifier = { factor = 0 VIE_ai_historical = yes } }`.

**Lưu ý:** `gen_ev6.py` (nguồn sinh `VIE_md_effects_p10.txt`) không có trong repo lẫn lịch sử git. Tiêu đề của file đó đã đổi thành "bảo trì bằng tay" (04/10/2026), nên sửa tay `VIE_md_p10.txt` là an toàn.

### 2.3 Cờ mở khóa (đường B)

[VIE_md_alt.txt](events/VIE_md_alt.txt):
- `vie_alt.1.b` (dòng 26): thêm `set_country_flag = VIE_hardline_unlocked`.
- `vie_alt.3.b` (dòng 95): thêm như trên.
- `vie_alt.7.a` (dòng 169): thêm trong `if = { limit = { has_country_flag = VIE_bop_active power_balance_value = { id = VIE_party_balance value < -0.4 } } ... }`.

### 2.4 Decision `VIE_hl_extraordinary_plenum`

File `VIE_md_hardline_decisions.txt`, đặt trong category có sẵn `VIE_resolution_category` (hiện khi Đảng cầm quyền, [VIE_md_categories.txt:14](common/decisions/categories/VIE_md_categories.txt#L14)).

```
VIE_hl_extraordinary_plenum = {
	icon = generic_political_discourse
	allowed = { original_tag = VIE }
	visible = { has_country_flag = VIE_hardline_unlocked  check_variable = { ruling_party = 19 } }
	available = { VIE_hl_can_take_power_plenum = yes }
	cost = 100
	days_remove = 30
	fire_only_once = yes
	complete_effect = { log = ... }
	remove_effect = { country_event = { id = vie_hl.1 } }
	ai_will_do = { base = 0 }
}
```

### 2.5 Dọn dẹp khi rời đảng 4

[VIE_md_effects.txt:150](common/scripted_effects/VIE_md_effects.txt#L150) `VIE_transition_regime`, đặt trước `change_ruling_party_effect = yes` (dòng 181):

```
if = {
	limit = {
		check_variable = { ruling_party = 4 }
		NOT = { check_variable = { rul_party_temp = 4 } }
	}
	VIE_hl_cleanup = yes
}
```

### 2.6 Chặn nhánh an ninh cướp quyền

[VIE_md_focus.txt:4474](common/national_focus/VIE_md_focus.txt#L4474) `VIE_sec_cyber_control`. Sửa `limit` của khối chuyển quyền thành:

```
limit = {
	NOT = { check_variable = { ruling_party = 7 } }
	NOT = { check_variable = { ruling_party = 4 } }
}
```

Thêm nhánh `else_if` cho đảng 4: `set_temp_variable = { VIE_rp_add = 10 }` và `VIE_hl_add_pressure = yes`.

### Kiểm tra giai đoạn 2

- Ván mới, kéo BoP xuống dưới −0,3 trước 2011. Ở Đại hội XI có lựa chọn mới, chọn thì thành đảng 4, lãnh đạo "Pham Dinh Tuan", BoP −0,5, `VIE_rp` = 20.
- Ở Đại hội XII dưới hardline chỉ hiện lựa chọn "khẳng định đường lối".
- Không lên hardline, chơi tới 2016: các event Đại hội không đổi gì (kiểm tra hồi quy).
- Với AI lịch sử: không bao giờ chọn hardline.

---

## Giai đoạn 3. Cây focus (25 focus)

### 3.1 Khung chung mỗi focus

```
focus = {
	id = VIE_hl_party_rectification
	icon = ...
	x = ...  y = ...
	relative_position_id = VIE_hl_unity_of_will
	cost = 7
	prerequisite = { focus = VIE_hl_unity_of_will }
	search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY }
	available = { VIE_hl_in_power = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_hl_party_rectification"
		...
		set_temp_variable = { VIE_rp_add = 6 }
		VIE_hl_add_pressure = yes
		VIE_ax_normalize = yes
	}
	ai_will_do = { ... }
}
```

- Mọi focus: `available = { VIE_hl_in_power = yes ... }`. Không dùng `allow_branch`, để cây luôn hiển thị như ND mục 1.1.
- Focus đổi trục: kết thúc bằng `VIE_ax_normalize = yes`, như `vie_alt.6.b`.
- Focus tốn ngân quỹ hoặc xây công trình: guard `bankruptcy_incoming_collapse` như các focus kinh tế hiện có.
- Vị trí: theo bảng ND mục 8. H0 neo `VIE_party_discipline` (x = 15, y = 4), các focus khác neo H0.
- Icon: dùng GFX có sẵn trong MD trước (`communist_purge`, `generic_political_reform`…), thay icon riêng sau.

### 3.2 Loại trừ

| Cặp | Cách làm |
|---|---|
| X1 / X2 / X3 | `mutually_exclusive` ba chiều. Ba focus nằm cạnh nhau nên không có đường vẽ chéo cây. |
| A5 và `private_champions`, `private_sector_engine` | Không dùng `mutually_exclusive` (hai focus kia ở xa, đường vẽ sẽ cắt ngang cây). Dùng `available` hai chiều: A5 cần `NOT = { has_completed_focus = ... }`, hai focus kia cần `NOT = { has_completed_focus = VIE_hl_no_party_business }`. |

### 3.3 Idea của cây

| Idea | Focus | Modifier |
|---|---|---|
| `VIE_hl_ideology_work_idea` | H2 | `stability_factor = 0.02`, `drift_defence_factor = 0.05` |
| `VIE_hl_state_leading_idea` | A1 | `stability_factor = 0.02`, `industrial_capacity_factory = 0.05` |
| `VIE_hl_state_transition_idea` (730 ngày) | A1 | `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_soe_spearhead_idea` (730 ngày) | A3 | `production_speed_buildings_factor = 0.05` |
| `VIE_hl_fdi_slowdown_idea` (365 ngày) | A4 | `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_planning_idea` | A6 | `industrial_capacity_factory = 0.05`, `country_productivity_growth_modifier = -0.01` |
| `VIE_hl_army_party_work_idea` | B1 | `army_org_regain = 0.05` |
| `VIE_hl_all_people_defence_idea` | B3 | `conscription_factor = 0.03` |
| `VIE_hl_cyber_content_idea` | C1 | `drift_defence_factor = 0.05`, `stability_factor = 0.01` |
| `VIE_hl_school_theory_idea` (730 ngày) | C2 | `research_speed_factor = -0.02` |
| `VIE_hl_controlled_renewal_idea` | X1 | `stability_factor = 0.03`, `country_productivity_growth_modifier = 0.01` |
| `VIE_hl_fusion_idea` | X2 | `political_power_factor = 0.10`, `stability_factor = 0.03`, `research_speed_factor = -0.03` |

Idea có thời hạn dùng `add_timed_idea = { idea = ... days = ... }`.
`check_static.py` kiểm tra key modifier có tồn tại trong MD, nên chạy script để bắt lỗi tên như `army_org_regain` hay `conscription_factor`.

### 3.4 Gọi thẳng effect có sẵn

| Việc | Effect hoặc biến |
|---|---|
| Thiện cảm nhóm lợi ích | `set_temp_variable = { temp_opinion = N }` rồi `change_communist_cadres_opinion`, `change_industrial_conglomerates_opinion`, `change_farmers_opinion`, `change_the_military_opinion` |
| Ngân quỹ | `set_temp_variable = { treasury_change = N }`, `modify_treasury_effect = yes` |
| Tăng trưởng | `increase_economic_growth = yes` |
| Tham nhũng | `decrease_corruption = yes` |
| Nhà máy | `one_state_industrial_complex` (theo mẫu [VIE_md_focus.txt:777](common/national_focus/VIE_md_focus.txt#L777)) |
| Công nghiệp quốc phòng | `VIE_def_industry_level` (theo mẫu [VIE_md_focus.txt:10249](common/national_focus/VIE_md_focus.txt#L10249)) |
| Vinashin | `VIE_vinashin_risk` |
| BoP | `VIE_bop_conservative_small` / `VIE_bop_reform_small` |
| Thận trọng trong bộ máy | `VIE_official_caution` (theo mẫu [VIE_md_focus.txt:2129](common/national_focus/VIE_md_focus.txt#L2129)) |

### 3.5 AI (ND mục 7)

```
ai_will_do = {
	base = 50
	modifier = { factor = 0.3  check_variable = { VIE_rp > 55 } }   # focus siết
}
```

C4, D3: `factor = 3` khi `VIE_rp > 55`. X1 base 60, X2 base 20 (`factor = 0` khi `VIE_ai_historical` hoặc `VIE_rp > 69`), X3 base 20.

### Kiểm tra giai đoạn 3

- `check_static.py`: không trùng ô, không có hàng xóm gần hơn 2, con không nằm trên cha, prerequisite và idea đều tồn tại.
- Trong game: cây hiện xám khi không phải hardline. Lên hardline bằng debug, làm hết focus, rồi đối chiếu `VIE_rp` cuối với bảng ND mục 3.2 (khoảng 82 nếu không xả van).
- Đối chiếu bốn trục hiển thị với ND mục 3.3 (B khoảng −3, C khoảng −2,6).

---

## Giai đoạn 4. Event phản ứng `vie_hl.2` đến `vie_hl.8`

Tất cả `is_triggered_only = yes`, gọi từ `VIE_hl_monthly`, theo mẫu scheduler hiện có (cờ một lần và `VIE_popup_cd` 45 ngày).

| Event | Gọi trong `VIE_hl_monthly` khi |
|---|---|
| `.2` Thư kiến nghị | `VIE_rp > 30`, có H1, chưa có cờ `VIE_hl_ev2_done` |
| `.3` FDI tạm hoãn | `VIE_rp > 39`, có A4 hoặc A5, chưa có cờ |
| `.4` Cảnh báo EVFTA/CPTPP | Có `VIE_evfta` hoặc `VIE_cptpp_member`, có C1 hoặc C3, chưa có cờ |
| `.5` HNTW giữa nhiệm kỳ | `VIE_rp > 55` lần đầu, hoặc gọi trực tiếp từ E1. Cờ chặn 730 ngày. |
| `.6` Dư luận Biển Đông | `VIE_scs_escalated_trigger`, có D1, chưa có cờ |
| `.7` Khủng hoảng chính danh | `VIE_rp > 79`, không có `VIE_hl_self_reliance_idea`. **Bỏ qua `VIE_popup_cd`** (bắt buộc). |
| `.8` Đánh giá lại | Có cờ `VIE_hl_self_reliance_running` nhưng idea đã hết hạn |

Idea `VIE_hl_self_reliance_idea` (`add_timed_idea`, 730 ngày): `stability_factor = 0.05`, `country_productivity_growth_modifier = -0.04`, `trade_opinion_factor = -0.10`, `production_speed_industrial_complex_factor = 0.10`. Khi idea này đang chạy, `VIE_hl_add_pressure` kẹp `VIE_rp` tối đa 80.

### Kiểm tra giai đoạn 4

- Debug đặt `VIE_rp` = 85: `.7` bắn trong vòng 1 tháng. Chọn "kiên trì" thì idea chạy. Rút ngắn thời hạn để test: `.8` bắn khi idea hết.
- Mỗi event có ít nhất một lựa chọn không phạt nặng (ND mục 5: không bế tắc).

---

## Giai đoạn 5. Sửa cây cũ

| Focus | Dòng | Sửa |
|---|---|---|
| `VIE_private_champions` | [2493](common/national_focus/VIE_md_focus.txt#L2493) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_no_party_business }` |
| `VIE_private_sector_engine` | [7601](common/national_focus/VIE_md_focus.txt#L7601) | Như trên |
| `VIE_soe_rapid_divestment` | [7487](common/national_focus/VIE_md_focus.txt#L7487) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_state_sector_leading }` |
| `VIE_investment_grade` | [5583](common/national_focus/VIE_md_focus.txt#L5583) | `available`: thêm `NOT = { has_completed_focus = VIE_hl_party_state_fusion }`. Thưởng: thêm khối van xả (bên dưới). |
| `VIE_international_financial_centre` | [5557](common/national_focus/VIE_md_focus.txt#L5557) | Như trên |
| `VIE_evfta` | [2565](common/national_focus/VIE_md_focus.txt#L2565) | Thêm khối van xả |
| `VIE_cptpp_member` | [2529](common/national_focus/VIE_md_focus.txt#L2529) | Thêm khối van xả |

Khối van xả (nên thành effect `VIE_hl_integration_valve`):

```
if = {
	limit = { VIE_hl_in_power = yes }
	set_temp_variable = { VIE_rp_add = -4 }
	VIE_hl_add_pressure = yes
	if = {
		limit = { NOT = { has_completed_focus = VIE_hl_steadfast_renewal } }
		set_temp_variable = { temp_opinion = -2 }
		change_communist_cadres_opinion = yes
		VIE_bop_reform_small = yes
	}
}
```

H1 giảm áp lực nếu đã làm `VIE_clean_cadres`. H3 thêm phạt nếu đã làm `VIE_decentralization`. B4 rẽ nhánh theo `VIE_military_enterprises_core` / `_divest` ([10230](common/national_focus/VIE_md_focus.txt#L10230), [10263](common/national_focus/VIE_md_focus.txt#L10263)). Ba việc này viết trong chính focus hardline, không sửa focus cũ.

### Kiểm tra giai đoạn 5

- Không phải hardline: bốn focus hội nhập cho đúng thưởng như cũ (hồi quy).
- Hardline: `VIE_rp` −4 mỗi focus hội nhập.

---

## Giai đoạn 6. Loc, icon, hoàn thiện

- `VIE_md_hardline_l_english.yml`: khoảng 25 focus × 2 key, 8 event (khoảng 40 key), 16 idea × 2 key, tooltip và decision. Tổng khoảng 170 key.
- Loc các option mới trong `vie_pol.*` thêm vào file loc hiện có của từng event.
- `python tools/verify_all_loc.py`: không thiếu key.
- Icon focus và ảnh event: làm sau bằng các script `tools/build_*` hiện có, nếu muốn icon riêng.
- `python tools/check_static.py` lần cuối.

## Ước lượng khối lượng

| Giai đoạn | Dòng code (ước tính) |
|---|---|
| 1. Nền tảng | khoảng 200 |
| 2. Lên nắm quyền | khoảng 200 (phần lớn là sửa file cũ) |
| 3. Cây focus | khoảng 1.000 |
| 4. Event | khoảng 400 |
| 5. Sửa cây cũ | khoảng 60 |
| 6. Loc | khoảng 170 key |

## Rủi ro đã biết

| Rủi ro | Cách xử lý |
|---|---|
| `gen_ev6.py` sinh lại `VIE_md_p10.txt` và xóa thay đổi | Script không còn trong repo; header file đã ghi "bảo trì bằng tay". Nếu bạn còn bản ở máy khác thì không chạy lại. |
| `VIE_transition_regime` đặt BoP về 0 | `VIE_hl_take_power` đặt lại −0,5 ngay sau đó. |
| Event lịch sử dựng lại lãnh đạo thật dưới hardline | Xóa cờ lịch sử trong `VIE_hl_take_power` và chặn option (mục 2.2). |
| Hardline đẩy B xuống, mở `sec_cyber_control` | Không còn chuyển đảng khi đang là đảng 4 (mục 2.6). |
| Thứ tự nạp scripted effect | Effect không có tham số nên không bị ràng buộc thứ tự. Nếu sau này thêm effect có tham số thì phải đặt trước nơi gọi, theo ghi chú trong `VIE_md_effects_axis.txt`. |
| Tên modifier sai | `check_static.py` đối chiếu với MD. |
