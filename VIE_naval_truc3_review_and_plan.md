# REVIEW TRỤC 3 HẢI QUÂN (XÂY DỰNG LỰC LƯỢNG + TRỤC 1B) + PLAN CODE

> Đầu vào: `Báo cáo hải quân Việt Nam – 3 trục … (bản 2.4).md`, mục 10–15 (Trục 3, Program Engine 1B, template), cộng mục 2, 16–18 (quy tắc, đối chiếu MD).
> Đối chiếu với repo @ working tree sau Trục 1 và Trục 2 hải quân (`VIE_naval_truc1_review_and_plan.md`, `VIE_naval_truc2_review_and_plan.md`), Trục 3 lục quân đã code (`VIE_truc3_review_and_plan.md`, tiền tố `VIE_lf_`) và dữ liệu MD (`tools/audit/md_ref/`, bản clone MD `main`).
> Ngày: 2026-10-02. **Chưa có dòng code nào của Trục 3.**
>
> **KẾT LUẬN: khung thiết kế (8 focus chung → 3 nhánh, 4 Decision lực lượng, Program Engine cho 1B) đúng hướng và nối được với Trục 1–2 đã code. Nhưng chưa code được nguyên văn: 7 lỗi chặn, 8 chỗ lệch mod/MD, 8 lỗ hổng logic (trong đó 6 là mâu thuẫn nội bộ của báo cáo). Bản sửa ở Phần 2–5, plan 10 bước ở Phần 6, 12 câu hỏi đã gắn mặc định ở Phần 7.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Vì sao đúng |
|---|---|
| 22 node Focus = 8 chung + 4 (Denial) + 5 (Greenwater) + 5 (Bluewater); mỗi lần chơi đi 12 (Denial) hoặc 13 (Greenwater, Bluewater) | Đếm lại trong bảng 11.1 và 11.5: khớp 10.1, 11, 15.1 và 15.2 |
| Focus chỉ mở Decision và đặt mốc; việc đào tạo là Decision | Cùng mẫu Trục 2 hải quân (`unlock_decision_tooltip`) và Trục 2 lục quân |
| Quy tắc 10: Trục 3 chỉ cấp modifier vận hành, không đụng giá đóng tàu | Khớp thực tế: Trục 2 sở hữu mọi thứ về sản xuất (`VIE_small_combatant_cost_mult`, tier) |
| Quy tắc 11: không ghi `VIE_cap_*` của Trục 2 | Đúng; xem A3 cho phần còn lại của namespace |
| Nhánh Maritime Denial là nhánh lịch sử (có đích cho người chơi đi đúng lịch sử) | Khắc phục lỗi gốc "không có chỗ đi" của bản cũ |
| Hải quân đánh bộ đã gỡ khỏi Trục 3 (sang nhánh Vietnam Special Force) | Kiểm trên repo: không còn tham chiếu live nào tới `VIE_naval_infantry` |
| Chương trình 1B đi qua Decision, không có cửa sổ lịch sử, không event tự kích | Khớp Quy tắc 5; vì vậy 1B **không** tạo pop-up mới ngoài ngân sách `VIE_popup_cd` |
| Trục 3 không ghi gì vào Trục 1 ngoài một thưởng nhỏ cho Kilo (mục 14.5) | Một chiều, không vòng: xem 5.3 |

---

# PHẦN 2 — 7 LỖI CHẶN

## A1 · Focus nền `VIE_navy_modernization` và hai node Doctrine **không còn trong cây live**

Báo cáo: T1 đòi `VIE_navy_modernization`; Quy tắc 8 lấy `VIE_path_maritime_denial` và `VIE_navy_blue_water` làm lối vào hai nhánh ("cần đối chiếu v7"). Đo trên repo: cả ba (và mọi focus hải quân cũ: `VIE_naval_aviation`, `VIE_cam_ranh_base`, `VIE_navy_lhd_program`…) chỉ còn trong `v11_removed_military_all_subbranches.txt` và `.bak`. Cây focus live (296 focus) có đúng một root quân sự `VIE_modernize_vpa` (266, 1).
**Fix:** T1 treo trực tiếp dưới `VIE_modernize_vpa` (đúng điều Trục 2 hải quân đã chốt ở N1: "Trục 3 sau này tự dựng cổng riêng"). Không phụ thuộc `VIE_naval_defence_law` của Trục 2 để Trục 3 không phải chờ Ba Son. Hai node Doctrine trở thành D1/B1 mới (xem A2 về ID).

## A2 · ID của báo cáo **đụng loc chết** và đụng kiểu đặt tên của repo

`localisation/english/VIE_md_p2_l_english.yml` vẫn giữ khóa của các focus đã xóa (`VIE_navy_modernization`, `VIE_naval_aviation`, `VIE_naval_infantry`, `VIE_cam_ranh_base`, `VIE_domestic_corvettes`…). Báo cáo dùng lại `VIE_naval_aviation` (B4): sẽ trùng khóa với loc mới và làm `verify_all_loc.py` báo trùng. Ngoài ra repo đặt ID bằng tiếng Anh với tiền tố nhóm (`VIE_lf_*` cho lục quân Trục 3; `VIE_nav_*`, `VIE_naval_*` cho hải quân Trục 1–2) và báo cáo dùng `VIE_org_*`, `VIE_dec_*`, `VIE_path_*`, `VIE_force_*`, mà `VIE_force_47` đã tồn tại (cùng vấn đề R3 của Trục 3 lục quân).
**Fix:** tiền tố **`VIE_nf_`** (naval force) cho focus, Decision, cờ, biến; **`VIE_p1b_`** cho Program Engine; namespace event `vie_nav_force` và `vie_p1b`. Bảng ánh xạ ở 5.1. Kiểm trước: `VIE_nf_`, `VIE_p1b_`, `vie_nav_force`, `vie_p1b` có 0 kết quả trong repo và MD.

## A3 · Gần như mọi cờ/biến ở mục 14 là **phản chiếu trạng thái** hoặc **chỉ ghi không ai đọc**

Quy tắc của chính báo cáo (16.3) và bài học đã áp ở Trục 2 hải quân (B5) và lục quân (R1): không giữ cờ chép lại trạng thái có sẵn.

| Mục báo cáo | Vấn đề | Xử lý |
|---|---|---|
| `VIE_org_naval_training`, `VIE_path_denial/greenwater/bluewater` | = `has_completed_focus` | **Bỏ**; dùng scripted trigger |
| `VIE_dec_*_active/_done/_waiting`, `_progress` | Trạng thái chờ giữa chừng không tồn tại (xem B1); `_progress` bị 16.3 cấm | **Bỏ** hết |
| `VIE_var_surface_readiness`, `VIE_var_sub_readiness`, `VIE_var_asw_skill`, `VIE_var_fleet_organization` (0–100) | Người đọc duy nhất là "template" (mà Quy tắc 10 cấm đổi giá/hull) và Kilo (chỉ thưởng) | **Bỏ biến số**; hiệu ứng vận hành đi thẳng vào `VIE_af_*` của dynamic modifier (L1 và 5.4). Giữ mức đã chọn (`VIE_nf_surface_level`…) vì không suy ra được |
| `VIE_var_hulls_<lớp>` cho 9 lớp | Chỉ lớp `carrier` và `destroyer` có người đọc (Decision nhóm tác chiến) | Giữ **2 bộ đếm**; `amphib` giữ chỗ cho nhánh Special Force qua `VIE_ext_*` khi nó tồn tại |
| `VIE_org_first_force`, `VIE_org_*_command` | Là kết quả Decision, HOI4 không hỏi được "Decision đã xong" (cùng lý do giữ `VIE_nav_dN_done`) | **Giữ** dưới tên `VIE_nf_dN_done` |

## A4 · `VIE_var_hulls_operational` **không tồn tại**: Trục 1–2 đã code `VIE_var_hulls_delivered`

Báo cáo (T6, 14.2) đọc `VIE_var_hulls_operational ≥ 4`. Trục 1 đã đổi tên thành `VIE_var_hulls_delivered` (đếm giao hàng tích lũy, mọi tàu trừ 1B; xem review Trục 1 B7) và Focus 3 của Trục 2 đã đọc nó (`> 3`).
**Fix:** T6 đọc `VIE_var_hulls_delivered > 3`. Chương trình 1B cộng `VIE_var_hulls_delivered` **chỉ cho thân tàu chủ lực** (FAC, corvette, khinh hạm, khu trục, tàu ngầm, tàu đổ bộ, tàu sân bay), đúng ý 14.2; tàu ngầm mini và tàu tiếp tế (bị hoãn, Q5) không cộng. Ghi rõ "từng giao" trong loc, vì tàu bị chìm vẫn tính.

## A5 · `VIE_var_naval_budget_room` không tồn tại; Funding Gate của 1B phải dùng cổng đã code

Mục 12.1 bước 4 dùng `VIE_var_naval_budget_room ≥ cost`. Trục 1 đã chốt dùng thẳng ngân khố: `VIE_naval_can_fund` (`treasury > VIE_naval_cost`) và nhánh thất bại kiểu event `vie_naval.43` (cắt quy mô / vay nợ ×1,1 / hoãn / hủy). **Fix:** 1B tái dùng đúng trigger và mẫu `VIE_naval_sigma_cost` → `…_funding_check` → `…_contract`; không tạo biến mới.

## A6 · Program Engine "dữ liệu thay cho event" **không thực hiện được nguyên văn** trong script HOI4

Mục 12.1 và 13.5: "thêm tàu mới chỉ thêm một dòng bảng". Nhưng `create_ship`, `create_equipment_variant`, tên tàu, `add_tech_bonus`, tên cờ/biến đều là **literal**; Trục 1 đã phải sinh mã bằng script (`gen4.py`, `gen6.py`). Bản clone MD không có mẫu tham số hóa tên biến bằng `$X$` trong scripted effect để dựa vào.
**Fix:** kiến trúc hai tầng.
1. **Dùng chung (viết tay):** 3 event pop-up (`vie_p1b.1` số lượng, `.2` mức nội địa hóa, `.3` thiếu vốn) đọc biến `VIE_p1b_cur` (mã chương trình 1–11) và các biến cấu hình `VIE_p1b_max_qty`, `VIE_p1b_unit_cost`… do effect nạp dữ liệu đặt; Funding Gate, slot, hoàn tất.
2. **Theo chương trình (sinh bằng `tools/gen_p1b.py` từ một bảng dữ liệu):** `VIE_p1b_load_<p>` (nạp dữ liệu), `VIE_p1b_ensure_variant_<p>`, `VIE_p1b_deliver_<p>` (có `create_ship` literal), event ẩn giao hàng `vie_p1b.1x`.
Số event thực tế ≈ 12 (3 chung + 9 ẩn), không phải "khoảng 7"; số effect sinh ra ~40.

## A7 · Tàu của 1B cần **hull tech + module tech** mà VIE không có; rủi ro lớn nhất của cả Trục 3

VIE mở đầu chỉ có `corvette_hull_1` (`VIE_Vietnam.txt:51`), đã hoàn tất `sp_naval_vessel_project`. MD đặt mỗi hull là một tech cùng tên (`destroyer_hull_4`, `carrier_hull_3`…, `start_year` = năm hull) và module (`module_sub_early_reactor_power` cần `tech_nuclear_power_systems_1`, mà tech này đòi `sp_medium_naval_nuclear_engines`). Trục 1 chưa cấp tech và đã ghi "rủi ro cao nhất" vào checklist; 1B không thể lặp lại cách đó cho 9 chương trình.
**Fix:** `VIE_p1b_load_<p>` kèm `set_technology = { <hull> = 1 … }` cho hull và các tech module chính khi **ký hợp đồng** (nhập khẩu = chuyển giao công nghệ). Bậc hull chọn theo năm (5.6). Kiểm trong game mục đầu của checklist (Phần 8); nếu `set_technology` không đủ thì lùi về `add_tech_bonus` + đòi nghiên cứu.

---

# PHẦN 3 — 8 CHỖ LỆCH SO VỚI MOD VÀ MD

## B1 · Trạng thái chờ giữa chừng (`_waiting`, "Decision chờ không chiếm slot")
Cùng lỗi B1 của Trục 2: HOI4 không có trạng thái này. **Fix:** cổng ở **lúc bấm** (`available` + `custom_trigger_tooltip` nói đúng điều còn thiếu); Decision đã bắt đầu thì chạy hết. Bỏ mọi `_waiting`.

## B2 · "Decision chạy nhiều sự kiện nối tiếp 12–18 tháng" cần cấu trúc đã dùng ở Trục 2
Decision = nút khởi động (`fire_only_once`, 50 PP), bấm xong bắn chuỗi event chọn, lựa chọn cuối trao **timed idea** hiển thị đang chạy (`add_timed_idea … days = <biến tạm>`, đã xác minh với MD) và hẹn event ẩn hoàn tất. Mọi hiệu ứng thật nằm ở event ẩn hoàn tất.

## B3 · Bộ đếm slot và nội chiến
`VIE_var_force_program_active` và `VIE_var_procurement_1b_active` (cap 2) cần **đếm lại theo timed idea** sau nội chiến, đúng như `VIE_nav_program_recount` đã làm cho Trục 2 (`VIE_collapse_aftermath`). Nếu không, event hoàn tất bị mất khi đổi tag sẽ kẹt bộ đếm ở 2.

## B4 · Nơi đặt modifier vận hành đã có sẵn
`VIE_armed_forces_modifier` (dynamic modifier gắn một lần bởi `VIE_modernize_vpa`, ghi bằng `add_to_variable = { VIE_af_* … tooltip = VIE_tt_* }`) đã có 14 modifier hải quân: `experience_gain_navy_factor`, `navy_max_range_factor`, `naval_coordination`, `navy_org_factor`, `naval_detection`, `navy_submarine_attack_factor`, `naval_strike_attack_factor`, `naval_speed_factor`, `naval_invasion_capacity`, `naval_invasion_planning_bonus_speed`, `navy_anti_air_attack_factor`, `naval_mines_effect_reduction`, `mines_planting_by_fleets_factor`, `navy_submarine_defence_factor`. Trục 3 hải quân dùng lại cơ chế này; chỉ **thiếu** `navy_personnel_cost_multiplier_modifier` (token MD có thật: `common/modifier_definitions/money_modifier_definitions.txt:30`) cho đánh đổi "chi phí duy trì cao" của Extended Range (11.4). Thêm 1 dòng ngoài khối `GEN:vars`, và **8 khóa tooltip `VIE_tt_*` còn thiếu** (xem bước 0). Bỏ ý "giảm chi phí duy trì" cũ khỏi Trục 2 là đúng: nay token đã có.

## B5 · Mã nguồn tàu "nhập khẩu" nên dùng variant VIE, không dùng variant của đối tác
Báo cáo không nói; Trục 1 đã chọn `creator = SOV` cho nhập khẩu (variant có sẵn của SOV) và variant VIE cho nội địa. Với 1B, đối tác (HOL, KOR, IND…) không có variant tương ứng trong MD cho mọi hull. **Fix:** **mọi** tàu 1B dùng variant do VIE tự tạo (`create_equipment_variant` có cờ chặn trùng, mẫu `VIE_naval_ensure_variants`), `creator = VIE`. Mức nội địa hóa chỉ đổi giá, thời gian và exp.

## B6 · Hull và slot ở bảng 16.2 cần bậc theo năm, tàu ngầm mini và tàu tiếp tế không khả thi
Bậc hull đã sửa ở review Trục 1 (corvette 1–8, frigate 1–8, destroyer 1–7, attack_submarine 1–8, helicopter_operator 1–6, carrier 1–7; `year` của từng bậc ở 5.6). Tàu ngầm mini không có hull riêng; tàu tiếp tế là `support_ship_N` không có module (mở bằng `tech_landing_craft_*`). **Fix:** hoãn P5 và P9 (Q5).

## B7 · Điều kiện tàu sân bay/SSN: `VIE_ext_nuclear_tech` chưa có chủ
Mục 14.5 đề xuất cờ cho "nhánh năng lượng" chưa có. Trong cây live **đã có** `VIE_nuclear_research` (focus nghiên cứu, `CAT_nuclear`). **Fix:** trigger `VIE_naval_has_nuclear_tech = { has_completed_focus = VIE_nuclear_research }` (một chỗ để đổi), cùng mẫu `VIE_naval_has_electronics` của Trục 2. Tech reactor thật được cấp lúc ký hợp đồng (A7).

## B8 · Quy ước event/decision/loc
Namespace chữ thường; log câu đầu mỗi option (không log nếu option chỉ đóng cửa sổ); `ai_chance` option tốn tiền có guard `bankruptcy_incoming_collapse` (và `ai_has_high_deficit` cho option không lịch sử); loc `localisation/english/VIE_md_events_nav_force_l_english.yml` (BOM, tiếng Việt, `:0`); `verify_all_loc.py`, `ev.py`, `audit.py`, `live.py` sau mỗi bước; category mới `allowed = { original_tag = VIE }`; mọi focus `search_filters = { FOCUS_FILTER_NAVY }`, `log` đầu `completion_reward`, `ai_will_do` base 60 (chuỗi) hoặc 40 (mở nhánh), `factor = 0` khi `bankruptcy_incoming_collapse`.

---

# PHẦN 4 — LỖ HỔNG LOGIC (6 mâu thuẫn nội bộ của báo cáo + 2 nối trục)

| # | Vấn đề | Vị trí báo cáo | Sửa |
|---|---|---|---|
| **L1** | "Readiness" 0–100 chỉ được đọc bởi template, mà Quy tắc 10 cấm template đổi giá/hull; thành ra biến không có người dùng thật | 13.5, 14.2 | Readiness = **mức đã chọn + modifier thật** (5.4). Hiệu ứng "độ sẵn sàng" là `navy_org_factor`, `naval_coordination`, `naval_detection` |
| **L2** | T9 đòi "T7 và T8" nhưng T8 đã đòi T7 | 11.1 | T9 chỉ đòi T8 |
| **L3** | P4 đòi `VIE_org_submarine_command` ở 14.1 nhưng bảng 12.2 không có điều kiện này | 12.2 vs 14.1 | Thêm vào `available` của P4: `VIE_nf_d2_done` |
| **L4** | P4 đòi `VIE_cap_naval_mro_sub`, cờ **không tồn tại**: Trục 2 đã code `VIE_var_mro_tier`, `VIE_mro_scope` (1 tàu ngầm, 2 tàu mặt nước, 3 cả hai), `VIE_nav_d2_done` | 12.2 | Trigger `VIE_naval_has_sub_mro = { has_country_flag = VIE_nav_d2_done NOT = { check_variable = { VIE_mro_scope = 2 } } }` |
| **L5** | Decision "thành lập nhóm tác chiến tàu sân bay" (B5) **không có trong danh sách 4 Decision** ở mục 11 và mục 15.2 | 11.5 vs 15.2 | Thêm làm Decision thứ 5 (`VIE_nf_d5_carrier_group`), điều kiện 1 tàu sân bay và 2 khu trục qua `VIE_var_hulls_carrier/_destroyer`. Bảng khối lượng: 5 Decision lực lượng |
| **L6** | "Mức chuyên môn… hướng còn lại mở lại bằng Event trễ với chi phí cao hơn" **không có event nào** định nghĩa; "lệch nhánh thì giảm `fleet_organization` 12 tháng" cần biến vừa bị bỏ | 11.2, 11.4 | Chuyên môn là lựa chọn một lần; hướng kia được bù một phần bởi event Hiệp đồng số 3 (mạng chống ngầm ven bờ). Lệch nhánh = `add_timed_idea` 365 ngày trừ org/coordination, đặt ngay ở focus mở nhánh |
| **L7** | **Kilo đọc readiness của Trục 3** (14.5) nhưng Kilo (đặt ngay 2009–2010) đến **trước** khi Decision tàu ngầm kết thúc | 14.2, 14.5 | Cờ `VIE_nf_sub_prep` đặt **ngay khi bấm** Decision tàu ngầm (event `.10`, mọi lựa chọn). Trục 1 `vie_naval.21` option A: nếu có cờ thì phí gói huấn luyện 0,15 tỷ/tàu thay vì 0,2. Chi phí huấn luyện không phải chi phí đóng/trang bị, không vi phạm Quy tắc 10; vẫn không phải điều kiện (Quy tắc 5) |
| **L8** | Cơ cấu lực lượng ban đầu (T6) chỉ so với T9 để phạt lệch; không có hiệu ứng nếu đi **đúng** nhánh | 11.4 | Đi đúng nhánh (Coastal→Denial, Balanced→bất kỳ, Extended→Greenwater/Bluewater): +1 mức thưởng nhỏ ở focus mở nhánh. Đối xứng với phạt |

---

# PHẦN 5 — THIẾT KẾ CHỐT CHO CODE

## 5.1 Hai mươi hai Focus (tọa độ tuyệt đối)

Anchor: toàn bộ neo vào **T1** (`relative_position_id = VIE_nf_training_standardization`, khai báo trước tất cả); T1 neo vào `VIE_modernize_vpa` (266, 1) với `x = -26, y = 1` → abs **(240, 2)**. Vùng x 216–254 trống ở mọi hàng, vùng x ≥ 200, y ≥ 9 trống (đo bằng `layout.py` ngày 2026-10-02); Trục 2 hải quân ở x 256–260, y 2–6; lục quân Trục 3 ở x 272–284, y 2–16.

| Mã | ID | Tên hiển thị | (dx,dy) → abs | Prerequisite | Ngày / điều kiện `available` |
|---|---|---|---|---|---|
| T1 | `VIE_nf_training_standardization` | Chuẩn hóa đào tạo hải quân | gốc → (240,2) | `VIE_modernize_vpa` | `date > 2004.12.31` |
| T3 | `VIE_nf_surface_force` | Phát triển lực lượng tàu mặt nước | (−4,1) → (236,3) | T1 | `date > 2004.12.31` |
| T4 | `VIE_nf_submarine_force` | Phát triển lực lượng tàu ngầm | (+4,1) → (244,3) | T1 | `date > 2007.12.31` |
| T5 | `VIE_nf_command_reform_1` | Cải cách bộ chỉ huy hải quân I | (0,2) → (240,4) | T3 **và** T4 | `date > 2009.12.31` (cần xác minh) |
| T6 | `VIE_nf_first_force` | Cơ cấu lực lượng ban đầu | (0,3) → (240,5) | T5; **OR** {`VIE_naval_mro`, `VIE_small_combatant_construction`} | `date > 2011.12.31`; `VIE_var_hulls_delivered > 3` |
| T7 | `VIE_nf_command_reform_2` | Cải cách bộ chỉ huy hải quân II | (0,4) → (240,6) | T6 | `date > 2013.12.31` |
| T8 | `VIE_nf_medium_force` | Lực lượng hải quân trung bình | (0,5) → (240,7) | T7 | `date > 2015.12.31` |
| T9 | `VIE_nf_operating_range` | Mở rộng phạm vi hoạt động | (0,6) → (240,8) | T8 | `date > 2017.12.31` |
| D1 | `VIE_nf_denial` | Ngăn chặn biển (Maritime Denial) | (−12,7) → (228,9) | T9; loại trừ G1, B1 | — |
| D2 | `VIE_nf_denial_defence` | Phòng thủ ven bờ tích hợp | (−12,8) → (228,10) | D1 | — |
| D3 | `VIE_nf_denial_subs` | Lực lượng tàu ngầm ngăn chặn | (−12,9) → (228,11) | D2 | — |
| D4 | `VIE_nf_denial_command` | Bộ chỉ huy phòng thủ ven bờ | (−12,10) → (228,12) | D3 | — |
| G1 | `VIE_nf_greenwater` | Hải quân khu vực | (0,7) → (240,9) | T9; loại trừ D1, B1 | — |
| G2 | `VIE_nf_regional_frigates` | Khinh hạm viễn hành | (−4,8) → (236,10) | G1 | — |
| G3 | `VIE_nf_amphibious_fleet` | Hạm đội đổ bộ | (+4,8) → (244,10) | G1 | — |
| G4 | `VIE_nf_lhd_program` | Chương trình tàu đổ bộ trực thăng | (0,9) → (240,11) | G2 **và** G3 | `date > 2021.12.31` |
| G5 | `VIE_nf_regional_command` | Bộ chỉ huy hạm đội khu vực | (0,10) → (240,12) | G4 | — |
| B1 | `VIE_nf_bluewater` | Hải quân viễn dương | (+16,7) → (256,9) | T9; loại trừ D1, G1 | — |
| B2 | `VIE_nf_ocean_escort` | Chương trình hộ tống viễn dương | (+10,8) → (250,10) | B1 | `date > 2023.12.31` |
| B3 | `VIE_nf_replenishment` | Bảo đảm hậu cần hạm đội | (+16,8) → (256,10) | B1 | `date > 2021.12.31` |
| B4 | `VIE_nf_naval_aviation` | Không quân hải quân | (+22,8) → (262,10) | B1 | `date > 2027.12.31` |
| B5 | `VIE_nf_carrier_group` | Nhóm tác chiến tàu sân bay | (+16,9) → (256,11) | B2, B3, B4 (ba khối riêng = AND) | `date > 2029.12.31` |

Khoảng cách cùng hàng tối thiểu 6 (quy tắc ≥ 4 của repo); con luôn `y >` cha. Ngày cổng 1B (P1…P11) lấy từ bảng 12.2 và đặt ở **Decision**, không ở focus (Quy tắc 6). Ba ngày gốc của báo cáo chưa kiểm: Lữ đoàn 162/167 (T5), Lữ đoàn 189 (báo cáo ghi 2013, bản gốc 2011), Cơ quan quản lý đóng tàu 2005 (T1): dùng như giá trị khởi điểm, ghi vào checklist. `ai_will_do`: 60 cho chuỗi; 40 cho D1/G1/B1 với `factor` theo path (Denial ×1,5 Historical, ×0,5 Reform; Greenwater ×1,5 Reform/Western, ×0,5 Historical; Bluewater ×1 Reform, ×0,25 Historical/Security; chỉ khi `VIE_ai_free` cho G và B), nhóm 40 trở lên còn lại 60.

**Phần thưởng focus** (chỉ XP, modifier và `unlock_decision_tooltip`; helper `VIE_nf_xp_10/15/20/25` theo mẫu `VIE_lf_xp_*`, có `has_selected_naval_grand_doctrine` → `add_mastery { folder = naval }`):

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP +15; `experience_gain_navy_factor` +5% | category `VIE_naval_force_category` (tooltip) |
| T3 | `navy_org_factor` +2% | D-A (mặt nước) |
| T4 | `navy_submarine_attack_factor` +2% | D-B (tàu ngầm) |
| T5 | `navy_org_factor` +2%, `naval_coordination` +3% | D-C (hiệp đồng) |
| T6 | XP +10 | D-D (cơ cấu ban đầu) |
| T7 | `navy_org_factor` +2%, `naval_coordination` +3% | — |
| T8 | `navy_max_range_factor` +3% | lối vào 1B: P1, P2, P3 (từ ngày) |
| T9 | `navy_max_range_factor` +5%, `naval_detection` +5% | ba nhánh |
| Nhánh | Bảng 5.4 | Bảng 5.5 |

## 5.2 Năm Decision lực lượng (category `VIE_naval_force_category`, priority 92)

Category: `allowed = { original_tag = VIE }`, `visible = { has_completed_focus = VIE_nf_training_standardization }`. Mỗi Decision: `cost = 50` PP (D-E 60), `fire_only_once = yes`, `available` có `custom_trigger_tooltip` cho slot và từng điều kiện, `complete_effect` log đầu + `VIE_nf_program_start` + bắn chuỗi event; `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Mở từ | `available` | Chuỗi chọn | Hoàn tất (event ẩn) |
|---|---|---|---|---|
| D-A `VIE_nf_d1_surface` | T3 | slot (`VIE_var_force_program_active < 2`) | `.1` mức (Cơ bản 0,40 tỷ / 12 tháng; Chuyên sâu 0,60 tỷ / 18 tháng); `.2` chuyên môn: **Hỏa lực** hoặc **Chống ngầm** | `.61`: `VIE_nf_surface_level` = 1/2, `VIE_nf_surface_specialty`, modifier theo 5.4, `VIE_nf_d1_done`, −1 slot |
| D-B `VIE_nf_d2_submarine` | T4 | slot | `.10` định hướng: **Lịch sử** (chuẩn bị nhân lực trước khi nhận tàu, 0,30 tỷ) hoặc **Sớm** (đắt hơn, 0,50 tỷ, thưởng ban đầu cao hơn); đặt `VIE_nf_sub_prep` ngay; `.11` mức Cơ bản/Chuyên sâu (×1,0 / ×1,5) | `.62`: `VIE_nf_sub_level`, modifier, `VIE_nf_d2_done`, −1 slot |
| D-C `VIE_nf_d3_fleet_coord` | T5 | slot; `VIE_nf_d1_done`; `VIE_nf_d2_done` | không có lựa chọn (chuỗi cố định, 0,50 tỷ, 18 tháng) | `.50` (1/3: XP + org), `.51` (2/3: phối hợp tàu ngầm – tàu mặt nước, coordination), `.63` (hết: mạng chống ngầm ven bờ), `VIE_nf_d3_done` |
| D-D `VIE_nf_d4_first_force` | T6 | slot | `.30` ba lựa chọn đặt `VIE_nf_force_priority` (1 Coastal, 2 Balanced, 3 Extended Range), 0,60 tỷ / 12 tháng | `.64`: modifier theo lựa chọn, `VIE_nf_d4_done` |
| D-E `VIE_nf_d5_carrier_group` | B5 | slot; `VIE_var_hulls_carrier > 0`; `VIE_var_hulls_destroyer > 1` | không có lựa chọn (1,0 tỷ / 18 tháng) | `.65`: org/coordination nhân theo số tàu sân bay đã giao (1 hoặc 2+), `VIE_nf_d5_done` |

Thời lượng cố định theo mức (`set_temp_variable` rồi `days = <biến>`, mẫu `VIE_nav_d1_start`). Chuỗi chọn là event nối tiếp nên miễn `VIE_popup_cd` (người chơi chủ động bấm). **Mọi lựa chọn có đánh đổi số** (Quy tắc 9): mức đầu tư (chi phí/thời gian/trần), hướng hỏa lực–chống ngầm (modifier khác nhau), Historical–Sớm (chi phí vs thưởng), ba cơ cấu lực lượng.

Hai thay đổi so với báo cáo (cả hai nhằm giữ ngân sách pop-up và bỏ trạng thái chờ): (1) chuyên môn của D-A chọn ngay ở chuỗi, không ở "Event 2" giữa chừng; (2) D-C có hai milestone ẩn thay cho ba pop-up.

## 5.3 Hợp đồng cờ/biến giữa ba trục (sau sửa)

| Cạnh | Hướng | Qua | Trạng thái |
|---|---|---|---|
| Trục 3 T1 ← lục quân root | gate | `has_completed_focus = VIE_modernize_vpa` | có sẵn |
| Trục 2 → T6 | T2 → T3 | prerequisite `VIE_naval_mro` / `VIE_small_combatant_construction`; `VIE_var_hulls_delivered > 3` | Trục 2 ghi rồi |
| Trục 2 → 1B nội địa | T2 → 1B | `VIE_var_ba_son_tier`, `VIE_var_small_combatant_tier`, `VIE_var_integration_tier`, trigger `VIE_naval_has_sub_mro`, cờ `VIE_cap_mature_naval_industry` | Trục 2 ghi rồi |
| 1B → Trục 2 | 1B → T2 | helper `VIE_nav_add_shipbuilding_exp` / `VIE_nav_add_integration_exp` (đã có, kẹp 0–100) khi hoàn tất, theo mức nội địa hóa (0% / 50% / 100% của `exp_reward`) | Dùng lại helper |
| 1B → Trục 1/2 | 1B → T1/T2 | `VIE_var_hulls_delivered` +1 mỗi thân tàu chủ lực | Dùng lại biến |
| Trục 3 → Trục 1 | T3 → T1 | `VIE_nf_sub_prep` (L7). **Đây là sửa duy nhất vào Trục 1** | Cần sửa nhỏ `vie_naval.21` |
| Trục 3 → 1B | T3 → 1B | focus T8, D1, D3, G2, G4, B2, B4, B5, `VIE_nf_d2_done`; quyền mở ghi ở `available` của Decision 1B | Mới |
| Trục 1 → Trục 3 | không | — | Trục 3 không đọc cờ Trục 1 nào |
| Trục 3 → Trục 2 | không | Trục 3 không ghi `VIE_cap_*` hay biến exp (Quy tắc 11) | Giữ |

Một chiều, không vòng: Trục 1 → Trục 2 → {Trục 3, 1B}; chỉ có hai cạnh ngược (1B → exp/hulls của Trục 2, Trục 3 → Kilo) và cả hai chỉ **cộng thưởng**, không gate.

## 5.4 Hiệu ứng modifier (thang khởi điểm, Q: cần cân bằng)

Mẫu ghi: `add_to_variable = { VIE_af_navy_org_factor = 0.02 tooltip = VIE_tt_navy_org_factor }` + `custom_effect_tooltip { localization_key = modifies_dynamic_modifier_tt MODIFIER = VIE_armed_forces_modifier }` (đúng mẫu `VIE_d4_reward`). Trần đặt ra cho **đường đầy đủ** (như G2 của Trục 3 lục quân): `navy_org_factor` ≤ +18%, `naval_coordination` ≤ +20%, `naval_detection` ≤ +15%, `navy_max_range_factor` ≤ +25%, `navy_submarine_attack_factor` ≤ +10%, `navy_submarine_defence_factor` ≤ +10%, `naval_strike_attack_factor` ≤ +10%, `experience_gain_navy_factor` ≤ +10%. `tools/audit/nf_balance.py` cộng cả ba đường và kiểm các trần này.

| Nguồn | Modifier (+ = bonus) |
|---|---|
| D-A mức 1/2 × hỏa lực | `naval_strike_attack_factor` +3% / +4,5%; `navy_org_factor` +1% / +1,5% |
| D-A mức 1/2 × chống ngầm | `navy_submarine_defence_factor` +3% / +4,5%; `naval_detection` +2% / +3% |
| D-B mức 1/2 | `navy_submarine_attack_factor` +3% / +4,5%; `naval_detection` +1% / +1,5% (định hướng Sớm: +1% thêm) |
| D-C (ba giai đoạn) | `naval_coordination` +2% +2% +2%; `navy_submarine_defence_factor` +2% (giai đoạn 3); XP +10 |
| D-D Coastal | `naval_strike_attack_factor` +2%; `navy_max_range_factor` −3% |
| D-D Balanced | `navy_org_factor` +1%, `naval_strike_attack_factor` +1%, `navy_max_range_factor` +1% |
| D-D Extended Range | `navy_max_range_factor` +4%, `navy_org_factor` +2%; `navy_personnel_cost_multiplier_modifier` +3% |
| D1 / D2 / D3 / D4 | strike +3% / mines (`mines_planting_by_fleets_factor` +10%, `naval_mines_effect_reduction` +5%) / sub attack +3% / org +3%, detection +4% |
| G1 / G2 / G3 / G4 / G5 | range +5% / range +3%, org +2% / `naval_invasion_planning_bonus_speed` +10%, `naval_invasion_capacity` +1 / `naval_invasion_capacity` +1 / org +3%, coordination +3% |
| B1 / B2 / B3 / B4 / B5 | range +5% / `navy_anti_air_attack_factor` +5% / range +3% / AA +3%, detection +4% / org +3%, coordination +5% (nhân 1,0 / 1,5 theo số tàu sân bay đã giao, qua D-E) |
| Lệch nhánh so với `force_priority` | timed idea 365 ngày: `navy_org_factor` −3%, `naval_coordination` −3% (L6) |
| Đúng nhánh | +1% `navy_org_factor` (L8) |

Không có modifier sản xuất, chi phí đóng hoặc trang bị (Quy tắc 10). `navy_personnel_cost_multiplier_modifier` là chi phí nhân sự, không phải chi phí tàu.

## 5.5 Trục 1B — Program Engine (Decision, category `VIE_naval_program_category`, priority 90)

Bảng chương trình. Ngày lấy từ báo cáo 12.2; **giá thực tế** (tỷ USD mỗi tàu, mức nhập khẩu; nguồn ở cuối tài liệu) thay cho "giá trị khởi điểm" trừu tượng; mức nội địa hóa nhân ×1,0 / ×1,15 / ×1,3 (13.2); thời gian đóng nhân ×1,0 / ×1,2 / ×1,4.

| Mã | Chương trình | Lối vào (focus + ngày) | Hull MD | Giá/tàu | Số lượng (min–max) | Đến tàu đầu (tháng) | Điều kiện nội địa (Trục 2) |
|---|---|---|---|---|---:|---:|---|
| P1 | Hộ vệ hạm nhẹ | T8, ≥ 2016 | `corvette_hull_4` | 0,40 | 2–6 | 30 | `small_combatant_tier ≥ 2` và `ba_son_tier ≥ 2` |
| P2 | Khinh hạm cỡ trung | T8, ≥ 2018 | `frigate_hull_4` | 0,45 | 2–4 | 40 | `integration_tier ≥ 1` và `ba_son_tier ≥ 2` |
| P3 | Chống ngầm cơ động | T8, ≥ 2018 | `frigate_hull_4` (variant ASW) | 0,50 | 2–4 | 40 | `integration_tier ≥ 1` |
| P4 | Tàu ngầm tấn công khu vực | T8 và (D3 hoặc G2), ≥ 2020; `VIE_nf_d2_done` | `attack_submarine_hull_4` | 0,55 | 2–4 | 54 | `ba_son_tier = 3`, `integration_tier ≥ 2`, `VIE_naval_has_sub_mro` |
| P5 | Tàu ngầm mini | — | — | — | — | — | **Hoãn** (Q5) |
| P6 | Bastion-P mở rộng | D2 | (hệ thống bờ, không phải tàu) | 0,15 | 1–3 | 18 | Chỉ nhập khẩu |
| P7 | Tàu đổ bộ trực thăng/LHD | G4, ≥ 2022 | `helicopter_operator_hull_3` | 0,60 | 1–2 | 54 | `ba_son_tier = 3` |
| P8 | Khu trục | B2, ≥ 2024 | `destroyer_hull_4` | 0,70 | 2–3 | 48 | `integration_tier ≥ 2` và `ba_son_tier = 3` |
| P9 | Tàu tiếp tế | — | — | — | — | — | **Hoãn** (Q5) |
| P10 | Tàu sân bay hạng nhẹ | B4, ≥ 2028 | `carrier_hull_3` | 2,70 | 1 | 84 | `VIE_cap_mature_naval_industry` |
| P11 | Tàu ngầm hạt nhân | B5, ≥ 2030, `VIE_naval_has_nuclear_tech` | `attack_submarine_hull_5` | 2,00 | 1–2 | 96 | `VIE_cap_mature_naval_industry` |

Tổng chi phí tối đa nếu mua mọi chương trình ở mức nội địa (×1,3): ≈ 24,5 tỷ (số lượng tối đa mỗi chương trình) trong ~14 năm; chương trình đơn lẻ lớn nhất P11 ×2 ở nội địa = 5,2 tỷ, dưới p90 chi phí event MD (26,45 tỷ; trung vị 4,0). Chi phí Decision lực lượng: D-A + D-B + D-C + D-D ≈ 1,8 tỷ (mọi mức Cơ bản, D-B Lịch sử) tới ≈ 2,45 tỷ (mọi mức Chuyên sâu, D-B Sớm), cộng D-E 1,0. Đo bằng `tools/audit/nf_balance.py`.

**Chuỗi chương trình (mỗi chương trình, dùng chung):** Decision (`available`: focus, ngày, `VIE_var_procurement_1b_active < 2`, đối tác tồn tại và không chiến tranh nếu nhập khẩu, `NOT contracted`) → `vie_p1b.1` số lượng → `vie_p1b.2` nhập khẩu / hybrid / nội địa (mức sau đòi tier Trục 2) → Funding Gate (A5; thiếu vốn → `vie_p1b.3`: cắt quy mô / vay ×1,1 / hoãn / hủy) → `VIE_p1b_contract_<p>` (trừ tiền, `set_technology`, variant, hẹn giao, timed idea hiển thị) → event ẩn giao từng chiếc mỗi 8 tháng → chiếc cuối: cộng exp Trục 2 theo mức nội địa hóa, `VIE_p1b_<p>_complete`, −1 slot. Không có cửa sổ lịch sử, không event tự kích, không `P_late`.

**Mã dữ liệu mỗi chương trình (tiền tố `VIE_p1b_<p>_`):** cờ `contracted`, `cancelled`; biến `qty_ordered`, `qty_delivered`, `localization` (0–2). Không có `_complete`, `_offered`, `_missed` (cùng lý do A3). `<p>` ∈ {`corvette`, `frigate_med`, `asw_frigate`, `ssk_reg`, `bastion2`, `amphib`, `destroyer`, `carrier`, `ssn`}.

**Đối tác nhập khẩu (mặc định, Q6):** P1, P3: HOL hoặc SOV; P2: HOL hoặc KOR; P4, P6, P11: SOV; P7: KOR hoặc FRA; P8, P10: IND. Cổng = `country_exists` và `NOT has_war_with`; nếu cả hai đối tác không còn thì chỉ mở hybrid/nội địa (nếu đủ tier) hoặc không mở.

## 5.6 Hull, tech và variant (template = cặp variant + create_ship)

Bậc hull và năm (từ `MD_mtg_ships.txt`; hull tech cùng tên với hull, `start_year` = năm):

| Lớp | Bậc → năm | Chọn cho |
|---|---|---|
| corvette | 3→1995, 4→2010, 5→2025 | P1: `corvette_hull_4` |
| frigate | 3→1995, 4→2010, 5→2025 | P2, P3: `frigate_hull_4` (Sigma/Gepard đã dùng bậc 3) |
| destroyer | 3→2005, 4→2025 | P8: `destroyer_hull_4` |
| helicopter_operator | 3→2020, 4→2045 | P7 |
| carrier | 3→2005, 4→2025 | P10: `carrier_hull_3` |
| attack_submarine | 4→2010, 5→2025 | P4: bậc 4; P11: bậc 5 |

Mỗi chương trình có `VIE_p1b_ensure_variant_<p>` (cờ chặn trùng, mẫu `VIE_naval_ensure_variants`): `type`, `parent_version`, `modules` chép từ một variant MD có sẵn của tàu thật tương đương (tìm ở bước 7 trong `history/countries/` của HOL, KOR, IND, SOV, FRA), `role_icon_index`, `icon`. P11 dùng `module_sub_early_reactor_power`; P3 là variant con của P2 (thêm module sonar kéo, ngư lôi). Tên slot phải là slot của hull đó (slot sai bị bỏ im lặng). Tên tàu: placeholder, `TODO(names)`.

## 5.7 Biến và cờ cuối cùng

| Tên | Loại | Đặt bởi | Đọc bởi |
|---|---|---|---|
| `VIE_var_force_program_active` | biến 0–2 | `VIE_nf_program_start/end`, `VIE_nf_program_recount` | `available` của 5 Decision lực lượng |
| `VIE_var_procurement_1b_active` | biến 0–2 | `VIE_p1b_program_start/end`, recount | `available` của Decision 1B |
| `VIE_nf_surface_level`, `VIE_nf_surface_specialty`, `VIE_nf_sub_level`, `VIE_nf_sub_orientation` | biến | event chọn | `.61`/`.62` (modifier), Decision 1B (hiển thị) |
| `VIE_nf_force_priority` | biến 1–3 | `.30` | focus D1/G1/B1 (L6, L8) |
| `VIE_nf_d1_done` … `VIE_nf_d5_done` | cờ | event ẩn hoàn tất | D-C, P4, D-E |
| `VIE_nf_sub_prep` | cờ | `vie_nav_force.10` | `vie_naval.21` (Kilo, chỉ thưởng) |
| `VIE_var_hulls_carrier`, `VIE_var_hulls_destroyer` | biến ≥ 0 | `VIE_p1b_deliver_carrier/_destroyer` | D-E |
| `VIE_p1b_cur`, `VIE_p1b_max_qty`, `VIE_p1b_unit_cost`, `VIE_p1b_*` tạm | biến | `VIE_p1b_load_<p>` | event chung `vie_p1b.1–.3` |
| `VIE_p1b_<p>_contracted/_cancelled`; `…_qty_ordered/_qty_delivered/_localization` | cờ/biến | engine | giao hàng, hiển thị |
| `VIE_var_hulls_delivered` | biến (đã có) | 1B +1 mỗi thân tàu chủ lực | T6, Focus 3 Trục 2 |

Trigger mới (file `VIE_md_triggers_naval_force.txt`): `VIE_nf_branch_denial/_greenwater/_bluewater` (= `has_completed_focus`), `VIE_naval_has_sub_mro`, `VIE_naval_has_nuclear_tech`, `VIE_nf_slot_free`, `VIE_p1b_slot_free`. Idea (file `VIE_md_ideas_nav_force.txt`): `VIE_nf_prog_surface/_sub/_coord/_first/_csg`, `VIE_p1b_prog_<p>`, `VIE_nf_branch_mismatch_idea` (timed 365 ngày).

## 5.8 AI

Focus: 5.1. Decision lực lượng: `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`; lựa chọn event: option Historical/Cơ bản có `base 90` + `add 100 VIE_ai_historical`; option khác `factor 0 NOT VIE_ai_free`, có guard bankruptcy và `ai_has_high_deficit`. Decision 1B: base 20 và chỉ khi `VIE_ai_free` (AI không đi alt-history ngoài chế độ free), cùng guard tài chính, đảm bảo tránh slot bị giữ vô ích (bài học của review rà soát hai trục trước: option AI luôn phải có đường chọn được).

---

# PHẦN 6 — PLAN CODE (10 bước, mỗi bước 1 commit, nhánh `naval-truc3-force`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+1 dòng `navy_personnel_cost_multiplier_modifier`, ngoài `GEN`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+8 khóa: `VIE_tt_experience_gain_navy_factor`, `_navy_max_range_factor`, `_naval_coordination`, `_navy_org_factor`, `_naval_detection`, `_navy_submarine_attack_factor`, `_naval_strike_attack_factor`, `_navy_personnel_cost`); `tools/audit/nf_balance.py` (cộng ba đường + trần + chi phí); `common/scripted_triggers/VIE_md_triggers_naval_force.txt` | Thêm biến đổi và trigger của 5.7; số liệu của 5.4 | `nf_balance.py` PASS; brace; console `effect add_to_variable = { VIE_af_navy_org_factor = 0.01 }` thấy dòng trong tooltip |
| **1** | `common/scripted_effects/VIE_md_effects_nav_force.txt` (phần 1) | `VIE_nf_xp_10/15/20/25`, `VIE_nf_add_*` (ghi `VIE_af_*`), `VIE_nf_program_start/end`, mở rộng recount | brace; scan effect chưa định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Chuỗi chung T1, T3–T9 (8 focus), reward chỉ modifier + XP + tooltip | `audit.py`: 0 dangling/forward-ref/cycle/trùng tọa độ; `layout.py`; mở cây: cột hải quân x 240 |
| **3** | cùng file | 14 focus nhánh (ME D1/G1/B1; phạt/thưởng lệch/đúng nhánh); icon generic tạm; thêm 22 mục vào `FOCI` của `tools/build_vie_focus_icons.py` | ME đúng; `audit.py` 22/22 |
| **4** | `common/decisions/VIE_md_nav_force_decisions.txt`, category (`VIE_md_categories.txt`), `common/ideas/VIE_md_ideas_nav_force.txt`, `events/VIE_nav_force.txt` (`add_namespace = vie_nav_force`) | D-A và D-B (event `.1 .2 .10 .11 .61 .62`); sửa Kilo `vie_naval.21` (L7) | chơi: T1→T3→D-A: tiền trừ, timed idea, 12/18 tháng sau modifier xuất hiện; D-B đặt `VIE_nf_sub_prep` ngay; Kilo A rẻ hơn khi có cờ |
| **5** | cùng file | D-C (`.50 .51 .63`), D-D (`.30 .64`), D-E (`.65`) | slot không vượt 2; D-C cần cả hai `_done` |
| **6** | `tools/gen_p1b.py` (bảng dữ liệu) → `common/scripted_effects/VIE_md_effects_p1b_*.txt`; `events/VIE_p1b.txt` (`vie_p1b.1–.3`, ẩn `.11–.19`); `common/decisions/VIE_md_p1b_decisions.txt` + category `VIE_naval_program_category` | Lát cắt P1, P2, P3 trước; Funding Gate dùng `VIE_naval_can_fund` | chơi đến 2016: Decision P1 hiện sau T8; hợp đồng trừ tiền; tàu đến; `error.log` không có `equipment_variant does not exist` |
| **7** | cùng file generator | P4, P6, P7, P8, P10, P11; `set_technology` hull/module (A7); chép module từ variant MD tương đương | `error.log`: grep `module`, `slot`, `hull`; mở màn hình thiết kế thấy variant; SSN có module reactor |
| **8** | `VIE_md_effects_p3.txt` (`VIE_collapse_aftermath`) | Đếm lại hai bộ đếm slot mới theo timed idea | checklist nội chiến |
| **9** | `localisation/english/VIE_md_events_nav_force_l_english.yml` (+ `VIE_md_events_p1b_l_english.yml` nếu tách); `tools/TESTING.md`; `VIE_v9_flag_mapping.md` (bảng "Truc 3 hai quan"); cập nhật báo cáo | Loc toàn bộ (BOM, `:0`); mục TESTING "Naval force" | `verify_all_loc.py`, `ev.py`, `live.py`, `audit.py`, `nf_balance.py` sạch |
| **10** | `ai_chance`/`ai_will_do` rà soát | Kiểm AI chọn được ở mọi event (bài học zero-weight) | `review.py`-kiểu quét: không option nào mọi trọng số 0 |

Ước lượng: 22 focus, 5 Decision lực lượng + 9 Decision 1B, ~24 event (12 lực lượng + 12 của 1B), ~1 700 dòng script (≈ 1 000 do generator sinh), ~330 khóa loc.

Bộ kiểm tĩnh sau mỗi bước: `python tools/verify_all_loc.py`, `tools/audit/live.py`, `ev.py`, `audit.py`, `nf_balance.py`, và các script quét cờ/biến/option (`review.py`, `check6.py` trong scratchpad của phiên Trục 2).

---

# PHẦN 7 — CÂU HỎI CẦN CHỐT (mặc định đã gắn; chỉ ghi lại khi bạn muốn đổi)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | T1 treo dưới `VIE_modernize_vpa` hay sau `VIE_naval_defence_law`? | **Dưới `VIE_modernize_vpa`** (A1, N1 của Trục 2) | Sau F1: đổi prerequisite và tọa độ T1, 1 dòng |
| Q2 | Readiness 0–100 hay mức + modifier? | **Mức + modifier thật** (L1) | Giữ biến số: thêm 4 biến, nhưng cần người đọc thật |
| Q3 | Chuyên môn ở chuỗi chọn đầu thay cho "Event 2" giữa chừng? | **Có** (5.2) | Muốn event giữa chừng: thêm 1 pop-up mỗi Decision, vượt ngân sách pop-up |
| Q4 | Tiền tố `VIE_nf_` / `VIE_p1b_`; namespace `vie_nav_force` / `vie_p1b` | **Như trên** (A2) | Đổi hàng loạt trước bước 1 |
| Q5 | Hoãn P5 (tàu ngầm mini) và P9 (tàu tiếp tế)? | **Hoãn**: không có hull/slot tương ứng (B6). Focus B3 và lựa chọn "tàu ngầm mini" của D-B chỉ còn modifier | Làm P5 bằng `attack_submarine_hull_1` tối giản; P9 cần kiểm `support_ship_2` |
| Q6 | Đối tác nhập khẩu theo 5.5? | **Như bảng** | Đổi bảng dữ liệu của generator |
| Q7 | Giá thực tế của 5.5 làm mặc định? | **Có**, nguồn cuối tài liệu | Đổi một cột bảng |
| Q8 | Bậc hull của 5.6? | **Như bảng**; kiểm chỉ số thật ở bước 7 | Đổi bảng dữ liệu |
| Q9 | Cổng SSN: `VIE_nuclear_research` + cấp tech reactor khi ký? | **Có** (B7) | Đổi trigger 1 dòng |
| Q10 | Chỉ giữ 2 bộ đếm lớp (`carrier`, `destroyer`)? | **Có** (A3) | Thêm bộ đếm khi có người đọc |
| Q11 | Thưởng Kilo bằng giá gói huấn luyện 0,15 thay 0,2 tỷ khi có `VIE_nf_sub_prep`? | **Có** (L7) | Đổi số hoặc bỏ thưởng |
| Q12 | Thang modifier và trần ở 5.4 | **Giá trị khởi điểm**, cần cân bằng bằng `nf_balance.py` | Đổi số |

---

# PHẦN 8 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào `tools/TESTING.md` ở bước 9)

- [ ] **Rủi ro cao nhất:** `set_technology = { destroyer_hull_4 = 1 }` (và hull/module khác) có đủ để `create_equipment_variant` + `create_ship` dựng được tàu cho VIE không? Có dòng "equipment_variant does not exist" nào trong `error.log`?
- [ ] Module của variant 1B có bị bỏ im lặng vì thiếu tech không (màn hình thiết kế)? SSN có module reactor?
- [ ] Cây focus: cột hải quân x 240, ba nhánh đúng chỗ, ME D1/G1/B1; đường kẻ từ T6 tới hai focus Trục 2 đọc được.
- [ ] Pop-up/năm sau khi thêm Trục 3 (chỉ các pop-up chuỗi chọn do người chơi bấm): vẫn ≤ 7 theo luật `TESTING.md`.
- [ ] D-B đặt `VIE_nf_sub_prep` ngay; Kilo (sau 2009-12) rẻ hơn 0,05 tỷ/tàu khi có cờ; không có cờ thì giữ 0,2.
- [ ] Cổng `VIE_var_hulls_delivered > 3` của T6 mở đúng sau Gepard I + Molniya trên đường lịch sử.
- [ ] Hai bộ đếm slot: bấm 2 Decision lực lượng thì Decision thứ 3 xám; sau nội chiến về đúng số timed idea đang chạy.
- [ ] 1B: Funding Gate thất bại → `vie_p1b.3` mở đủ 4 lựa chọn; vay nợ nhân 1,1; hủy không trừ tiền; giao đúng 8 tháng/tàu; chiếc cuối cộng exp cho Trục 2 và `VIE_var_hulls_delivered`.
- [ ] `navy_personnel_cost_multiplier_modifier` hiển thị và đúng dấu (MD đánh dấu `color_type = bad`; đơn vị chưa kiểm).
- [ ] Lệch nhánh so với `force_priority`: timed idea phạt 365 ngày hiện và tự mất.

---

# NGUỒN GIÁ (tỷ USD, chọn làm mặc định ở 5.5)

- Gowind 2500: ≈ 0,425/tàu (Abu Dhabi, 850 triệu cho 2 tàu, 2019); Ai Cập ≈ 0,27. [Gowind-class design](https://en.wikipedia.org/wiki/Gowind-class_design) → P1 0,40.
- Arrowhead 140 (Indonesia): 0,36/tàu theo hợp đồng 2 tàu 720 triệu. [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/sea/indonesia-to-implement-arrowhead-140-design-on-iver-huitfeldt-variant-contract) → P2 0,45, P3 0,50 (thêm sonar, ngư lôi, trực thăng).
- Type 214: 0,33 (2008), tàu mới 0,5–0,7; Soryu ≈ 0,665; Scorpène ≈ 0,45. [Type 214](https://en.wikipedia.org/wiki/Type_214_submarine), [Sōryū-class](https://en.wikipedia.org/wiki/S%C5%8Dry%C5%AB-class_submarine) → P4 0,55.
- Juan Carlos I: € 462 triệu. [Wikipedia](https://en.wikipedia.org/wiki/Spanish_amphibious_assault_ship_Juan_Carlos_I) → P7 0,60.
- Kolkata ≈ 0,64–0,73; Type 052DM ≈ 0,6. [Kolkata-class](https://en.wikipedia.org/wiki/Kolkata-class_destroyer), [Type 052D](https://en.wikipedia.org/wiki/Type_052D_destroyer) → P8 0,70.
- INS Vikrant: ≈ 2,7 (₹23.000 crore). [INS Vikrant](https://en.wikipedia.org/wiki/INS_Vikrant_(2013)) → P10 2,70.
- Suffren ≈ € 1,73 tỷ (2014); Astute ≈ £ 1,5–1,65 tỷ; Virginia ≈ 4,3–4,5. [Suffren-class](https://en.wikipedia.org/wiki/Suffren-class_submarine), [Astute-class](https://en.wikipedia.org/wiki/Astute-class_submarine) → P11 2,00 (mức Suffren/Astute, không phải Virginia).
- Bastion-P 0,15/tổ hợp: giữ giá đã chốt ở Trục 1.

---

# TRẠNG THÁI THI CÔNG (2026-10-02)

Bước 0–9 đã code, chưa chạy trong game, chưa commit. Bước 10 (rà AI) làm bằng đọc: mọi option của event đều có ít nhất một lựa chọn khả dụng với trọng số dương; Decision 1B chỉ AI `VIE_ai_free` bấm.

| Bước | Trạng thái | Lệch so với plan |
|---|---|---|
| 0 | Xong: `navy_personnel_cost_multiplier_modifier`, 8 khóa `VIE_tt_*`, `nf_balance.py`, `VIE_md_triggers_naval_force.txt` | Số trong 5.4 đã chỉnh sau khi script báo vượt trần: T8 range +3%, T9 +5%, B1 +5%, B3 +3%, D-D Extended +4%, D4/B4 detect +4% |
| 1 | Xong: `VIE_md_effects_nav_force.txt` (XP, dm tooltip, slot) | — |
| 2–3 | Xong: 22 focus; `VIE_nf_branch_mismatch_idea`; 22 mục `FOCI` | — |
| 4 | Xong: D-A, D-B, 5 idea, recount (gọi trong `VIE_collapse_aftermath`), Kilo L7 | Category priority 94 (92 đã bị `VIE_def_industry_category` dùng) |
| 5 | Xong: D-C, D-D, D-E | Thưởng D-E = thêm 0,25× (1 tàu sân bay) hoặc 0,5× (từ 2) thưởng B5 |
| 6–7 | Xong: `tools/gen_p1b.py`; 9 chương trình P1–P4, P6–P8, P10, P11 | Variant dùng `allow_without_tech = yes` (mẫu `05_netherlands.txt`); hybrid đòi điều kiện Trục 2 nhẹ hơn nội địa một bậc; category 1B priority 89; P5, P9 hoãn (Q5) |
| 8 | Xong: hai hàm recount nối vào `VIE_collapse_aftermath` | Làm cùng bước 4 và 6 |
| 9 | Xong: loc, `tools/TESTING.md` (mục "Naval force and Program 1B"), bảng cờ trong `VIE_v9_flag_mapping.md` | — |

Mở: module variant P8 và P7 chưa có mẫu MD đầy đủ; bunker P6 chồng lên Bastion Trục 1; icon/ảnh event chưa tạo; ngày T5/T1 và Lữ đoàn 189 chưa xác minh.

## Cap nhat 2026-10-02: cum Luat Bien chuyen sang nhanh Bien Dong

- 10 focus (law_of_the_sea, maritime_militia, fisheries_surveillance, dk1_platforms, legal_warfare, spratly_fortification, coast_guard_law, assert_maritime_rights, paracel_ultimatum, limited_war_doctrine) gom thanh mot khoi trong `VIE_md_focus.txt`, bo `FOCUS_FILTER_NAVY`; ID, vi tri luoi, prerequisite khong doi.
- `VIE_assert_maritime_rights` mo som qua `VIE_nf_branch_denial` (Truc 3) thay cho `VIE_maritime_denial_idea` (da xoa). Chieu phu thuoc duy nhat: nang luc hai quan -> mo focus Bien Dong.
- Ngan sach modifier chung `VIE_armed_forces_modifier`: Truc 3 da cham tran coord 19.5/20 va detect 14.5/15 -> Bien Dong chi con `VIE_af_navy_max_range_factor` +0.05 (spratly_fortification); `nf_balance.py` tinh them SCS, PASS.
- 1B: doi tac `destroyer`/`carrier` doi `IND` -> `RAJ` (An Do), sinh lai file.

## Cap nhat 2026-10-02: giai doan 2 - Hop tac an ninh bien (nhanh Bien Dong)

- 4 focus moi: `VIE_scs_maritime_cooperation` (goc, sau `VIE_law_of_the_sea`), `VIE_scs_multilateral_exercise`, `VIE_scs_cam_ranh_port` (cap `VIE_cam_ranh_idea`, can Bon Khong / khong lien minh), `VIE_scs_joint_training` (can ca hai nhanh + doi tac An Do/Nhat hoac co kilo).
- Category `VIE_scs_cooperation_category` (priority 88), 5 decision (tap tran, tham cang, huan luyen chung RAJ/SOV/JAP), event `vie_scs_coop.1` / `.10`, scripted trigger `VIE_scs_pc_ok` / `VIE_scs_pc_any` / `VIE_scs_non_aligned`.
- Khong cong vao `VIE_armed_forces_modifier`; `VIE_cam_ranh_idea` experience 0.05 -> 0.01 de tong `experience_gain_navy_factor` (truc luc luong 5 + coast guard 4 + Cam Ranh 1) khop tran 10; `nf_balance.py` doc truc tiep file idea.
- MD da dat san naval_base 8 tai Nha Trang (province 10162, state 519) nen khong xay them ha tang o Cam Ranh.
