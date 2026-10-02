# REVIEW TRỤC 3 KHÔNG QUÂN (XÂY DỰNG LỰC LƯỢNG) + PLAN CODE

> Đầu vào: `VIE_air_force_content_report.md` bản 1.4, Phần 7 (Trục 3) và các chỗ Trục 3 chạm tới (3.1 R5/R9/R11, 4.2, 4.3, 4.4, 10, 11, 13).
> Đối chiếu với: repo đang có Trục 1 + Trục 2 không quân (chưa commit, đã qua review 2026-10-03); Trục 3 hải quân (`VIE_naval_truc3_review_and_plan.md`, `VIE_md_effects_nav_force.txt`, `VIE_md_nav_force_decisions.txt`, `events/VIE_nav_force.txt`) và lục quân (`VIE_md_effects_p17.txt`); MD v2.0.0 và HOI4 trên máy (`documentation/modifiers_documentation.md`, `common/modifier_definitions`); cây focus live (323 focus, đo toạ độ tuyệt đối).
> Phạm vi: chỉ Trục 3 (22 focus + 5 Decision). 1B chưa dựng nên mọi chỗ Trục 3 nối sang 1B được tách ra, xem A2, A4.
>
> **KẾT LUẬN: khung (8 focus chung → 3 nhánh loại trừ, 5 Decision, modifier ghi vào `VIE_armed_forces_modifier`) ĐÚNG và giống hải quân, giữ nguyên.
> Nhưng bản 1.4 chưa code được: 4 lỗi chặn (Phần 2), 4 chỗ lệch với Trục 1–2 và mod (Phần 3). Báo cáo đã sửa thành bản 1.5. Phần 4 là thiết kế chốt, Phần 5 plan code 9 bước.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Lý do |
|---|---|
| 22 focus = 8 chung + A (4) + B (5) + C (5), ba nhánh loại trừ nhau ở A1/B1/C1 | Cùng khuôn `VIE_nf_*` hải quân (D/G/B) |
| T1 treo `VIE_modernize_vpa`, không phụ thuộc cây hải quân hay lục quân | Giống `VIE_nf_training_standardization` |
| Focus chỉ cấp XP, modifier và tooltip mở Decision; việc đào tạo là Decision (R2) | Giống hải quân |
| 5 Decision `fire_only_once`, 50 PP (D-E 60), cổng ở lúc bấm, chuỗi event chọn nối tiếp (miễn `VIE_popup_cd`), hoàn tất bằng event hẹn giờ | Cùng mẫu `VIE_nf_d1…d5` |
| Chuyên môn D-A chọn ngay trong chuỗi, không "event giữa chừng" | Hải quân đã sửa như vậy |
| Cặp lệch nhánh / đúng nhánh nhỏ, đối xứng (7.4) | Giống `VIE_nf_branch_mismatch_idea` |
| Trục 3 không ghi `VIE_cap_*` và bậc Trục 2 (R5), chỉ cộng thưởng ngược cho Trục 1 | Giữ nguyên |
| Token: `experience_gain_air_factor`, `air_range_factor`, `air_cas_efficiency`, `air_mission_efficiency`, `air_superiority_efficiency`, `air_detection`, `air_defence_factor` | Đối chiếu `modifiers_documentation.md` hôm nay: đều có |

---

# PHẦN 2 — 4 LỖI CHẶN

## A1 · T5 và các cổng đọc Trục 1 không có đường dự phòng, và prerequisite viết sai

Bản 1.4: T5 = "T4, hoặc `VIE_apm_a32`", cổng `VIE_var_air_delivered > 11`.
- "T4 **hoặc** A32" cho phép bỏ qua T4 nếu đã xong A32. Hải quân viết ngược lại: T6 = T5 **và** (một trong hai focus Trục 2). Hai cách mở T5 loại trừ ý nghĩa của chuỗi chung.
- `VIE_var_air_delivered > 11` chỉ tăng khi Su-30 được giao (Trục 1). Nếu SOV không còn hoặc đang có chiến tranh với VIE trong cả bốn cửa sổ, biến đứng ở 0 và T5 khóa vĩnh viễn, kéo theo T6, T7, T8 và cả ba nhánh. Đây là đúng lỗi #1 của review Trục 2 (hợp đồng tùy chọn thành cổng cứng).

**Sửa:** T5 = `prerequisite = { focus = VIE_airf_command_reform_1 }` **và** `prerequisite = { focus = VIE_apm_a32 focus = VIE_apm_a31 focus = VIE_apm_radar }` (một trong ba focus Trục 2, đúng mẫu hải quân). `available`: `date > 2011.12.31` và `OR = { VIE_var_air_delivered > 11, date > 2014.12.31 }` (hết cửa sổ Su-30 cuối thì tự phát triển).

## A2 · D-E của nhánh B và C đọc biến của 1B, mà 1B chưa tồn tại

Bản 1.4: B cần `VIE_var_air_multirole4 ≥ 12` (chỉ 1B P2 ghi), C cần `VIE_var_uav_delivered ≥ 4` (chỉ 1B P9 ghi). Không có 1B thì D-E của B và C không bao giờ bấm được, chương trình đỉnh của hai trong ba nhánh bị khóa. Nhánh A: `VIE_var_sam_lr ≥ 1` chỉ tăng khi S-300 giao (lại thiếu dự phòng như A1).

**Sửa:** mức đầu của D-E dùng chỉ dữ liệu Trục 1–2 đã có; mức hai (thưởng cao hơn) mới đọc 1B, nên 1B ra sau chỉ mở thêm thưởng, không mở khóa.

| Nhánh | Mức 1 (bấm được) | Mức 2 (thưởng +50%) |
|---|---|---|
| A | (`VIE_var_sam_lr ≥ 1` hoặc `VIE_apm_a31_tier ≥ 2`) và `VIE_apm_radar_tier ≥ 2` | `VIE_var_sam_lr ≥ 3` (hai tiểu đoàn S-300 của Trục 1 đã cho 2; cần 1B P8) |
| B | `VIE_var_air_delivered ≥ 24` và `VIE_apm_a32_tier ≥ 2` | `VIE_var_air_multirole4 ≥ 12` (1B P2) |
| C | `VIE_apm_uav_tier ≥ 2` | `VIE_var_uav_delivered ≥ 4` (1B P9) |

Tuân R11: Trục 3 chỉ đọc biến của 1B để cộng thưởng, không dùng làm cổng.

## A3 · "Phòng không" và "phòng thủ" của 7.5 không có token riêng, và biến modifier đang dùng chung

- 12.2 báo cáo thừa nhận dòng "phòng không" chưa có token. Hiện `air_defence_factor` (= "Air Defense") đã bị Trục 1 không quân (0,06), Trục 2 (0,04) và lục quân (Igla 0,05 + TL-01 0,03) cộng chung, tổng 0,18 trên trần 0,20. Nếu Trục 3 cũng cộng vào đó (nhánh A ≈ 0,175) thì vượt hẳn.
- `VIE_armed_forces_modifier` thiếu `air_attack_factor` (T2, D-A, B2…) và `airforce_personnel_cost_multiplier_modifier` (D-D), và chưa có khóa tooltip `VIE_tt_*` cho `experience_gain_air_factor`, `air_superiority_efficiency`, `air_home_defence_factor`, `air_intercept_efficiency`. Hai token mới đã xác nhận có trong MD/HOI4 (`air_attack_factor` trong `modifiers_documentation.md`, `airforce_personnel_cost_multiplier_modifier` trong `money_modifier_definitions.txt`).
- Detection là biến dùng chung: Trục 1 (tối đa 0,05) + Trục 2 (0,06) = 0,11 trên trần 0,20, nên Trục 3 chỉ còn **0,09**. Bản 1.4 đặt 0,165 cho nhánh C và nhánh A.

**Sửa:**
1. "Phòng không" của Trục 3 = `air_home_defence_factor` ("Home defence", đã nằm sẵn trong modifier, chưa ai dùng). "Phòng thủ" = `air_intercept_efficiency` (cũng nằm sẵn, chưa ai dùng). **Trục 3 không đụng `air_defence_factor`**, nên khoản #3 còn treo của review Trục 1–2 (trần phòng không) tự hết: 0,18 ≤ 0,20, không cần bạn chọn nữa.
2. Thêm 2 dòng vào `VIE_armed_forces_modifier` (ngoài khối `GEN`) và 6 khóa `VIE_tt_*` (bước 0).
3. Hạ phát hiện của Trục 3 xuống 4,5% ở phần chung và 4% ở nhánh A/C (bảng 4.5). Làm theo quy tắc của báo cáo: **hạ giá trị, không nâng trần**.

## A4 · Phần thưởng "mở 1B" gọi `unlock_decision_tooltip` tới Decision chưa tồn tại

7.2: T7 mở P1, P6, P7; A2 mở P8, P10; A3 mở P4; B2 mở P2, P3; B4 mở P5; C2 mở P9; C3 mở P4, P10. 1B chưa có, tooltip tới Decision không tồn tại sinh lỗi.
**Sửa:** bỏ các dòng này khỏi reward khi code Trục 3. Việc 1B đọc `has_completed_focus` của các focus này (như hải quân: quyền mở ghi ở `available` của Decision 1B, không ở focus) đã đủ; khi dựng 1B thì thêm `unlock_decision_tooltip` một lần.

---

# PHẦN 3 — 4 CHỖ LỆCH VỚI TRỤC 1–2 VÀ MOD

| # | Lệch | Sửa |
|---|---|---|
| B1 | R9 và 3.2 B3 còn nói "đếm lại slot sau nội chiến" và 4.2 nhắc hook. Hook `VIE_collapse_aftermath` đã bỏ. | Bộ đếm `VIE_var_airf_program_active` tự chữa bằng `VIE_airf_slot_heal` (monthly, cùng scheduler với `VIE_apm_slot_heal`): đặt 0 khi không còn timed idea `VIE_airf_prog_*` nào **và** không có cờ `VIE_airf_d?_pending`. Cờ chờ không hết hạn trong 2 ngày: dùng 30 ngày, xóa bởi mọi option (bài học review Trục 2, lỗi #5). |
| B2 | Báo cáo dùng `VIE_air_force_category`, trùng tiền tố `VIE_air_` mà 4.3 cấm (roster chỉ huy). Trục 2 dùng `VIE_apm_category`. | Đổi thành `VIE_airf_category`, `priority = 86` (86 chưa dùng; 87 Trục 2 không quân, 88 hợp tác an ninh biển, 89 1B hải quân). Cổng: `has_completed_focus = VIE_airf_training_standardization`. |
| B3 | `VIE_ap_training_standardized` (Trục 1) đang là `always = no`, chờ T1; E13 option c và E15 giá rẻ đều đọc nó. | Bước 3: đổi thành `has_completed_focus = VIE_airf_training_standardization`. Đây là cạnh ngược duy nhất Trục 3 → Trục 1 (chỉ thưởng, không gate). |
| B4 | `ai_free`: bản 1.4 viết "chỉ khi `VIE_ai_free`" cho nhánh B, C và UAV. `VIE_ai_free` **chưa được định nghĩa** (lỗi có sẵn của 1B). | Dùng mẫu đang chạy của Trục 2 và hải quân: `modifier = { factor = 0 VIE_ai_historical = yes }` (trigger này luôn đúng, nên AI không bao giờ đi B/C). Nhánh A là mặc định của AI. Không thêm `VIE_ai_free` mới. |

Lưu ý nhỏ: báo cáo ghi D-E "nhân thưởng nhánh ×1,0/×1,5". Hải quân thực tế: focus B5 cho thưởng gốc, D-E cộng thêm **25% (mức 1) hoặc 50% (mức 2)** của thưởng gốc. Trục 3 không quân làm y như vậy: focus capstone A4/B5/C5 cho thưởng gốc (+XP), D-E cộng +0,25× / +0,5×. Tổng tối đa = ×1,5, trùng ý bản gốc.

---

# PHẦN 4 — THIẾT KẾ CHỐT CHO CODE

## 4.1 Hai mươi hai Focus (tọa độ tuyệt đối, đã kiểm trống)

Neo: tất cả vào **T1** (`relative_position_id = VIE_airf_training_standardization`, khai báo trước các focus còn lại); T1 neo `VIE_modernize_vpa` (266, 1) với `x = 36, y = 1` → (302, 2). Vùng x ≥ 298 và y 2–13 hoàn toàn trống (cây live: Trục 2 không quân ở x 290–296 y 3–8; lục quân Trục 3 tới x 284; khối `VIE_sec_*` ở y ≥ 24). Đã kiểm: không đè focus nào, cùng hàng cách nhau ≥ 4 (thực tế ≥ 6), con luôn `y >` cha.

| Mã | ID | Tên | (dx,dy) → abs | Prerequisite | `available` |
|---|---|---|---|---|---|
| T1 | `VIE_airf_training_standardization` | Chuẩn hóa đào tạo phi công và kỹ thuật viên | → (302,2) | `VIE_modernize_vpa` | `date > 2004.12.31` |
| T2 | `VIE_airf_fighter_force` | Phát triển lực lượng tiêm kích | (−4,1) → (298,3) | T1 | `date > 2007.12.31` |
| T3 | `VIE_airf_sam_force` | Phát triển lực lượng tên lửa phòng không và radar | (+4,1) → (306,3) | T1 | `date > 2005.12.31` |
| T4 | `VIE_airf_command_reform_1` | Cải cách chỉ huy PK-KQ I | (0,2) → (302,4) | T2 **và** T3 | `date > 2009.12.31` |
| T5 | `VIE_airf_first_force` | Cơ cấu lực lượng ban đầu | (0,3) → (302,5) | T4 **và** (một trong `VIE_apm_a32`, `VIE_apm_a31`, `VIE_apm_radar`) | `date > 2011.12.31`; `OR = { VIE_var_air_delivered > 11, date > 2014.12.31 }` |
| T6 | `VIE_airf_command_reform_2` | Cải cách chỉ huy PK-KQ II | (0,4) → (302,6) | T5 | `date > 2013.12.31` |
| T7 | `VIE_airf_medium_force` | Lực lượng không quân trung bình | (0,5) → (302,7) | T6 | `date > 2015.12.31` |
| T8 | `VIE_airf_operating_range` | Mở rộng bán kính hoạt động và căn cứ tiền phương | (0,6) → (302,8) | T7 | `date > 2017.12.31` |
| A1 | `VIE_airf_iads` | Phòng không tích hợp (loại trừ B1, C1) | (−12,7) → (290,9) | T8 | — |
| A2 | `VIE_airf_layered_defence` | Mạng radar – tên lửa nhiều tầng | (−12,8) → (290,10) | A1 | `date > 2019.12.31` |
| A3 | `VIE_airf_ew_antistealth` | Tác chiến điện tử và chống tàng hình | (−12,9) → (290,11) | A2 | `date > 2021.12.31` |
| A4 | `VIE_airf_iads_command` | Bộ chỉ huy phòng không khu vực | (−12,10) → (290,12) | A3 | `date > 2024.12.31` |
| B1 | `VIE_airf_multirole` | Không quân đa nhiệm (loại trừ A1, C1) | (0,7) → (302,9) | T8 | — |
| B2 | `VIE_airf_multirole_fleet` | Chương trình tiêm kích đa nhiệm 4.5 | (−6,8) → (296,10) | B1 | `date > 2024.12.31` |
| B3 | `VIE_airf_sustainment` | Bảo đảm kỹ thuật đa nguồn | (0,8) → (302,10) | B1 | `date > 2022.12.31` |
| B4 | `VIE_airf_airlift_tanker` | Vận tải và tiếp dầu trên không | (+6,8) → (308,10) | B1 | `date > 2026.12.31` |
| B5 | `VIE_airf_multirole_wing` | Cánh không quân đa nhiệm | (0,9) → (302,11) | B2, B3, B4 (ba khối riêng = AND) | `date > 2028.12.31` |
| C1 | `VIE_airf_unmanned` | Không người lái và mạng hóa (loại trừ A1, B1) | (+16,7) → (318,9) | T8 | — |
| C2 | `VIE_airf_isr_uav` | UAV trinh sát và mục tiêu | (+12,8) → (314,10) | C1 | `date > 2020.12.31` |
| C3 | `VIE_airf_datalink` | Mạng liên kết dữ liệu (C4ISR) | (+20,8) → (322,10) | C1 | `date > 2022.12.31` |
| C4 | `VIE_airf_strike_uav` | UAV tấn công | (+12,9) → (314,11) | C2 | `date > 2025.12.31` |
| C5 | `VIE_airf_teaming` | Phối hợp có người – không người | (+16,10) → (318,12) | C3 **và** C4 (khối riêng) | `date > 2029.12.31` |

`FOCUS_FILTER_AIRCRAFT`, cost 7 cho chuỗi (10 cho capstone), icon generic tạm. `ai_will_do`: 60 cho chuỗi; A1 = 40; B1, C1 `factor = 0 VIE_ai_historical = yes`; `factor = 0` khi `bankruptcy_incoming_collapse`. Cổng một chiều không quân → Biển Đông (Q7) là việc phía Biển Đông đọc `has_completed_focus = VIE_airf_operating_range`; Trục 3 không viết gì thêm.

## 4.2 Phần thưởng focus (đã đổi token theo A3, bỏ mở 1B theo A4)

Ký hiệu: EXP `experience_gain_air_factor`, ATK `air_attack_factor`, SUP `air_superiority_efficiency`, CAS `air_cas_efficiency`, MIS `air_mission_efficiency`, RNG `air_range_factor`, DET `air_detection`, HOME `air_home_defence_factor`, INT `air_intercept_efficiency`, PERS `airforce_personnel_cost_multiplier_modifier`. XP dùng helper `VIE_airf_xp_10/15/20/25` (mastery `folder = air` nếu đã chọn học thuyết, không thì `air_experience`).

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP 15; EXP +4% | category `VIE_airf_category` (tooltip) |
| T2 | ATK +1% | D-A |
| T3 | HOME +2% | D-B |
| T4 | MIS +2% | D-C |
| T5 | XP 10 | D-D |
| T6 | MIS +2%, DET +1% | — |
| T7 | RNG +3% | — |
| T8 | RNG +4%, DET +1% | ba nhánh |
| A1 / A2 / A3 / A4 | HOME +2% / DET +2%, HOME +2% / INT +3%, DET +2% / MIS +2%, HOME +2% | A4: D-E |
| B1 / B2 / B3 / B4 / B5 | RNG +4% / ATK +3%, SUP +2%, CAS +2% / MIS +2% / RNG +3% / MIS +2%, ATK +2% | B5: D-E |
| C1 / C2 / C3 / C4 / C5 | DET +1% / DET +3% / MIS +2% / ATK +3% / MIS +2%, INT +2% | C5: D-E |
| A1, B1, C1 thêm | lệch/đúng nhánh theo `VIE_airf_force_priority` (7.4): lệch → timed idea 365 ngày (MIS −3%, DET −3% ⇒ dùng idea, không qua biến); đúng → MIS +1% | — |

## 4.3 Năm Decision (category `VIE_airf_category`, priority 86)

Mỗi Decision: `cost = 50` (D-E 60), `fire_only_once = yes`, `available` có `custom_trigger_tooltip` cho slot và từng điều kiện, `complete_effect` = log + cờ chờ 30 ngày + `VIE_airf_program_start` + bắn chuỗi; `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Mở từ | `available` | Chuỗi chọn | Hoàn tất |
|---|---|---|---|---|
| D-A `VIE_airf_d1_fighters` | T2 | slot | `.1` mức (Cơ bản 0,40 tỷ / 12 tháng; Chuyên sâu 0,60 / 18) → `.2` chuyên môn (Không chiến / Tấn công mặt đất–biển) | `.61` ẩn: modifier theo bảng 4.4, `VIE_airf_d1_done`, −1 slot |
| D-B `VIE_airf_d2_sam` | T3 | slot | `.10` định hướng (Lịch sử 0,30 / Sớm 0,50, đặt `VIE_airf_sam_orientation` ngay) → `.11` mức (×1,0 / ×1,5) | `.62` ẩn, `VIE_airf_d2_done` |
| D-C `VIE_airf_d3_coordination` | T4 | slot; `d1_done`; `d2_done` | không chọn: 0,50 tỷ / 18 tháng | `.50` ẩn (giai đoạn 1), `.51` ẩn (giai đoạn 2), `.63` ẩn (giai đoạn 3) |
| D-D `VIE_airf_d4_first_force` | T5 | slot | `.30` ba cơ cấu (1 Phòng thủ lãnh thổ, 2 Cân bằng, 3 Tầm xa): 0,60 tỷ / 12 tháng, đặt `VIE_airf_force_priority` | `.64` ẩn |
| D-E `VIE_airf_d5_capstone` | A4, B5 hoặc C5 | slot; cổng nhánh mức 1 (A2) | không chọn: 1,0 tỷ / 18 tháng | `.65` ẩn: +0,25× (mức 1) hoặc +0,5× (mức 2) thưởng của focus capstone |

Event hoàn tất là `hidden = yes` hoặc `minor_flavor` như hải quân; hẹn giờ bằng `days = <biến tạm>` (đã được MD xác nhận cho `country_event` và `add_timed_idea`). Chuỗi chọn do người chơi bấm nên miễn `VIE_popup_cd`. Số event chọn: 6 (`.1 .2 .10 .11 .30` và D-E không chọn), cộng 7 event ẩn/nhỏ.

## 4.4 Hiệu ứng Decision (đã đổi token)

| Nguồn | Hiệu ứng |
|---|---|
| D-A × Không chiến, mức 1/2 | SUP +3% / +4,5% |
| D-A × Tấn công đất/biển, mức 1/2 | CAS +3% / +4,5%; ATK +1% / +1,5% |
| D-B mức 1/2 | HOME +3% / +4,5%; DET +1% / +1,5% (Sớm: HOME +1% thêm) |
| D-C ba giai đoạn | MIS +2%; HOME +2%, SUP +2%; DET +1%, MIS +2% |
| D-D Phòng thủ | INT +3%, HOME +2%, RNG −3% |
| D-D Cân bằng | ATK +1%, INT +1%, RNG +1% |
| D-D Tầm xa | RNG +5%, MIS +2%, PERS +3% |

## 4.5 Ngân sách modifier (biến dùng chung, tổng mọi trục)

| Token | Trần | Trục khác đã dùng | Dành cho Trục 3 | Trục 3 tối đa (A / B / C) |
|---|---:|---|---:|---|
| EXP | 10% | (timed idea Trục 1–2 là tạm thời) | 10% | 4 / 4 / 4 |
| ATK | 10% | — | 10% | 3,5 / 9,5 / 6,5 |
| SUP | 10% | — | 10% | 6,5 / 8,5 / 6,5 |
| CAS | 10% | — | 10% | 4,5 / 6,5 / 4,5 |
| MIS | 16% | — | 16% | 13 / 16 / 16 |
| RNG | 20% | — | 20% | 12 / 19 / 12 |
| **DET** | **20%** | **Trục 1 + 2 = 11%** | **9%** | **8,5 / 4,5 / 8,5** |
| HOME | 20% | — | 20% | 18,5 / 11,5 / 11,5 |
| INT | 8% | — | 8% | 6 / 3 / 6 |
| PERS | +3% (chi phí) | — | 3% | 3 (chỉ D-D Tầm xa) |
| `air_defence_factor` | 20% | Trục 1 0,06 + Trục 2 0,04 + lục quân 0,08 = 18% | **0** | không dùng |

Các tổng đã tính bằng script thử (mọi tổ hợp nhánh × chuyên môn × cơ cấu D-D, mức hai, D-E +50%): **tất cả dưới trần**. Bước 0 biến script này thành `tools/audit/air_force_balance.py` và thêm phần cộng chéo Trục 1–2–lục quân để kiểm `air_defence_factor` và DET luôn.

## 4.6 Hợp đồng cờ/biến giữa các trục

| Cạnh | Qua | Ghi chú |
|---|---|---|
| Trục 1 → Trục 3 | `VIE_var_air_delivered` (T5), `VIE_var_sam_lr` (D-E A) | luôn có dự phòng theo ngày hoặc theo bậc Trục 2 (A1, A2) |
| Trục 2 → Trục 3 | `has_completed_focus` của `VIE_apm_a32/_a31/_radar` (T5); `VIE_apm_a32_tier`, `_a31_tier`, `_radar_tier`, `_uav_tier` (D-E) | một chiều |
| Trục 3 → Trục 1 | `VIE_ap_training_standardized` (B3) | chỉ thưởng |
| Trục 3 → Trục 2 | không | R5 |
| 1B → Trục 3 | `VIE_var_air_multirole4`, `_sam_lr ≥ 2`, `_uav_delivered` | chỉ mức 2 của D-E |
| Trục 3 → 1B | `has_completed_focus` của T7, A2, B2… đọc ở `available` của Decision 1B | 1B làm sau |
| Trục 3 → Biển Đông | `has_completed_focus = VIE_airf_operating_range` | Biển Đông đọc |

Biến/cờ mới (tiền tố `VIE_airf_`, mọi cái đều có người đọc): `VIE_var_airf_program_active` (0–2); `VIE_airf_fighter_level`, `VIE_airf_fighter_specialty`, `VIE_airf_sam_level`, `VIE_airf_sam_orientation`, `VIE_airf_force_priority`; cờ `VIE_airf_d1_done`, `VIE_airf_d2_done` (D-C đọc), `VIE_airf_d1_pending`, `_d2_pending`, `_d4_pending`. Idea: `VIE_airf_prog_fighters/_sam/_coord/_first/_capstone` (timed, chỉ báo đang chạy), `VIE_airf_branch_mismatch_idea` (365 ngày). Trigger mới (file `VIE_md_triggers_air_force.txt`): `VIE_airf_slot_free`, `VIE_airf_branch_a/_b/_c` (= `has_completed_focus`), `VIE_airf_capstone_ok_a/_b/_c` (mức 1), `VIE_airf_capstone_lvl2_a/_b/_c`.

## 4.7 AI

Focus: 4.1. Decision: base 100, `factor 0` khi `bankruptcy_incoming_collapse`. Event: option Cơ bản / Lịch sử `base 90` + `add 100 VIE_ai_historical`; option khác `modifier = { factor = 0 VIE_ai_historical = yes }` và guard `bankruptcy_incoming_collapse`, `ai_has_high_deficit`. Mỗi option có ít nhất một đường chọn được (bài học zero-weight).

---

# PHẦN 5 — PLAN CODE (9 bước, nhánh `claude/air-truc3`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+`air_attack_factor`, +`airforce_personnel_cost_multiplier_modifier`, ngoài `GEN`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+6 khóa: `VIE_tt_experience_gain_air_factor`, `_air_attack_factor`, `_air_superiority_efficiency`, `_air_home_defence_factor`, `_air_intercept_efficiency`, `_airforce_personnel_cost`); `tools/audit/air_force_balance.py`; `common/scripted_triggers/VIE_md_triggers_air_force.txt` | Hạ tầng modifier, trigger, script cân bằng cộng chéo | `air_force_balance.py` PASS; brace; `verify_all_loc.py` sạch |
| **1** | `common/scripted_effects/VIE_md_effects_air_force.txt` | `VIE_airf_xp_*`, `VIE_airf_dm_tt`, `VIE_airf_add_*` (ghi `VIE_af_*` + `force_update_dynamic_modifier`), `VIE_airf_program_start/end`, `VIE_airf_slot_heal`, `VIE_airf_start_timer`, chi phí/thời gian như `VIE_apm_*` | scan effect chưa định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Chuỗi chung T1–T8, reward theo 4.2 | `audit.py`: 0 dangling/forward-ref/cycle/trùng toạ độ; chạy `live.py` bản sed |
| **3** | cùng file; `VIE_md_triggers_air_proc.txt` | 14 focus nhánh (ME A1/B1/C1; phạt/thưởng lệch/đúng nhánh), icon generic; đổi `VIE_ap_training_standardized` | `audit.py` 22/22; `ev.py` |
| **4** | `common/decisions/VIE_md_air_force_decisions.txt`, category `VIE_airf_category` (priority 86), `common/ideas/VIE_md_ideas_air_force.txt`, `events/VIE_air_force.txt` (`add_namespace = vie_air_force`) | D-A (`.1 .2 .61`) và D-B (`.10 .11 .62`) | `ev.py`; tooltip `VIE_airf_slot_tt` |
| **5** | cùng file | D-C (`.50 .51 .63`), D-D (`.30 .64`), D-E (`.65`) với cổng 2 mức (A2) | slot ≤ 2; D-C cần cả `d1_done` và `d2_done` |
| **6** | `common/on_actions/VIE_md_on_actions.txt` (+`VIE_airf_slot_heal = yes`); loc `VIE_md_events_air_force_l_english.yml` (focus + decision + event + tooltip, BOM, `:0`) | Nối scheduler tháng, loc toàn bộ | `verify_all_loc.py` ZERO errors |
| **7** | `tools/build_vie_air_event_pictures.py`, `tools/build_vie_focus_icons.py` | Ảnh cho 6 event chọn (Commons, giấy phép tự do, ghi CREDITS) và icon cho 29 focus (7 Trục 2 + 22 Trục 3) | không lỗi `texturefile` |
| **8** | `tools/TESTING.md`; `VIE_v9_flag_mapping.md` (mục "Truc 3 khong quan"); cập nhật báo cáo | Checklist thử + bảng cờ | `ev.py`, `audit.py`, `air_force_balance.py` sạch |
| **9** | rà soát `ai_chance` / `ai_will_do` | Không option nào mọi trọng số 0; AI đi A, không đi B/C | script quét option |

Ước lượng: 22 focus, 5 Decision, 13 event (6 chọn + 7 ẩn/nhỏ), ~600 dòng script, ~140 khóa loc, ~8 trigger, 6 idea.

Lỗi cần tránh khi code (rút từ review Trục 1–2): cờ chờ 30 ngày thay vì 2 ngày, xóa bởi mọi option; `slot_heal` bỏ qua khi có cờ chờ; mọi `add_to_variable` modifier kèm `force_update_dynamic_modifier`; mọi cổng đọc hợp đồng tùy chọn có đường dự phòng; file mới ghi CRLF.

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đã gắn; chỉ trả lời khi muốn đổi)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q-C1 | "Phòng không" = `air_home_defence_factor`, "phòng thủ" = `air_intercept_efficiency`, Trục 3 không dùng `air_defence_factor` | **Có** (khoản #3 treo của Trục 1–2 tự hết) | Dùng `air_defence_factor`: phải hạ phòng không Trục 3 xuống 2% hoặc nâng trần 0,20 |
| Q-C2 | D-E mức 1 chỉ đọc Trục 1–2, mức 2 đọc 1B (A2) | **Có** | Đòi 1B cho cả mức 1: Trục 3 nhánh B, C bị khóa tới khi dựng 1B |
| Q-C3 | Cột Trục 3 đặt x 290–322, T1 neo `x = 36` so với `VIE_modernize_vpa` | **Có** | Đặt x ≤ 200 (bên trái hải quân): đổi một dòng neo |
| Q-C4 | Category `VIE_airf_category`, priority 86 | **Có** | Đổi một dòng |
| Q-C5 | T5 đòi một trong ba focus Trục 2 (không chỉ A32) | **Có** | Chỉ A32: người không muốn làm A32 bị chặn |
| Q-C6 | Capstone A4/B5/C5 cho thưởng gốc, D-E cộng +25% / +50% (giống hải quân) | **Có** | Đổi hệ số trong `VIE_airf_d5_finish` |

---

# PHẦN 7 — CHECKLIST THỬ TRONG GAME (đưa vào `tools/TESTING.md` ở bước 8)

- [ ] `error.log`: grep `VIE_airf_`, `vie_air_force`, `air_attack_factor`, `airforce_personnel_cost`, `air_home_defence`.
- [ ] Cây focus: cột Trục 3 ở x 298–322, y 2–12, không đè Trục 2 (x 290–296); A1/B1/C1 loại trừ nhau.
- [ ] T5: mở khi T4 xong và một trong ba focus Trục 2; với SOV bị loại khỏi thế giới (`VIE_var_air_delivered` = 0) T5 vẫn mở sau 2014-12-31.
- [ ] D-A…D-D: tiền trừ, timed idea hiện, modifier xuất hiện đúng lúc; bấm hai lần liên tiếp không mở hai chương trình; slot ≤ 2.
- [ ] D-E: mức 1 bấm được với dữ liệu Trục 1–2 thuần (không 1B); thưởng +25%; mức 2 khi có biến 1B (thử bằng console `set_variable`).
- [ ] Detection tổng (Trục 1+2+3) ≤ 20% ở đường A và C đầy đủ; `air_defence_factor` không đổi so với trước Trục 3.
- [ ] `VIE_ap_training_standardized` trở thành đúng sau T1: E15 (T-6C) rẻ hơn, option `.13.c` hiện.
- [ ] Mismatch: D-D cơ cấu 1 rồi chọn B1 → timed idea phạt 365 ngày; cơ cấu 3 rồi chọn B1 → +1% nhiệm vụ.
- [ ] Quan sát AI tới 2030: đi nhánh A, không bao giờ B/C, không kẹt slot.

---

# TIẾN ĐỘ CODE (2026-10-03)

- **Bước 0–3 xong** (chưa chạy trong game): hạ tầng modifier, helper, 22 focus (chuỗi chung + 14 nhánh), loc, `air_force_balance.py` (22/22 focus khớp bảng, ALL PASS).
- Hai chỗ lệch nhỏ so với bảng 4.2, vì trần MIS 16%: C3 `VIE_airf_datalink` MIS +2% (thay vì +3%); thưởng "đúng nhánh" là MIS +1% (A1 khớp cơ cấu 1; B1, C1 khớp cơ cấu 3) bằng `VIE_airf_branch_fit_a/_wide`, còn cơ cấu 2 hoặc chưa chọn là trung tính. Lệch nhánh = timed idea 365 ngày.
- `VIE_ap_training_standardized` (Trục 1) đã đổi sang `has_completed_focus = VIE_airf_training_standardization`.
- **Bước 4–5 xong**: 5 Decision (`VIE_md_air_force_decisions.txt`), 12 event (`events/VIE_air_force.txt`: 5 chọn `.1 .2 .10 .11 .30`, 2 ẩn `.50 .51`, 5 thông báo `.61–.65`), `unlock_decision_tooltip` ở T2–T5 và A4/B5/C5; `air_force_balance.py` có thêm mục 5 đối chiếu Decision (ALL PASS). Cổng B của D-E thêm `OR date > 2030.12.31` (hợp đồng Su-30 tùy chọn). `VIE_airf_slot_heal` chỉ chờ cờ của D-A, D-B, D-D (D-C và D-E không có khoảng giữa bấm và chọn).
- **Bước 6–8 xong**: `VIE_airf_slot_heal` nối vào on_monthly; ảnh cho 5 event chọn (`vie_air_force.1 .2 .10 .11 .30`, plan ghi 6 nhưng chỉ có 5 event chọn) và icon ảnh thật cho 29 focus (7 Trục 2 + 22 Trục 3) bằng `tools/build_vie_air_focus_icons.py` (tái dùng ảnh Commons đã tải, ghi giấy phép vào `assets/focus_icons/CREDITS.json`); mục TESTING "Air force (Truc 3)" và bảng cờ trong `VIE_v9_flag_mapping.md`.
- Còn: bước 9 (rà AI), chạy thử trong game theo TESTING.md, commit.
- **Bước 9 xong**: `tools/audit/air_ai_options.py` quét mọi event có lựa chọn của Trục 1–3: mọi event còn ít nhất một option AI chọn được (option lịch sử `base 90` + `add 100`); các option không lịch sử đều `factor = 0 VIE_ai_historical`, nên AI không đi nhánh B/C, UAV bậc 2–3 hay option phi lịch sử. 3 cặp "conditional zero" (`vie_air_ind.13`, `.21`, `vie_air_proc.11`) bù nhau với `trigger` của option kia nên an toàn.
