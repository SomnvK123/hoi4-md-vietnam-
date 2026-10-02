# REVIEW TRỤC 2 HẢI QUÂN (CNQP) + PLAN CODE

> Đầu vào: `Báo cáo hải quân Việt Nam – 3 trục … (bản 2.4).md`, mục 2, 3.2–3.3, 5, 6, 7, 8.1, 9, 16–18 (phần Trục 2).
> Đối chiếu với repo @ working tree sau bước 0–7 của Trục 1 hải quân (`VIE_naval_truc1_review_and_plan.md`),
> Trục 2 lục quân đã code (`VIE_md_def_industry.txt`, `VIE_truc2_review_and_plan.md`) và dữ liệu MD trong `tools/audit/md_ref/`.
>
> **KẾT LUẬN: thiết kế Trục 2 hải quân (6 Focus + 5 Decision, năng lực → kinh nghiệm → trưởng thành) đúng hướng và nối
> được với Trục 1 đã code. Nhưng chưa code được nguyên bản: 4 lỗi chặn, 6 chỗ lệch so với mod/MD, 6 lỗ hổng logic
> (trong đó A4 làm hỏng lựa chọn 8 và 10 tàu của Trục 1 nếu không sửa). Bản sửa ở Phần 3–5, plan 9 bước ở Phần 6. Chưa có dòng code nào của Trục 2.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Vì sao đúng |
|---|---|
| Sáu Focus mở năng lực, năm Decision biến thành hiện thực; không Decision/Focus nào cấp tàu | Khớp Quy tắc 1–3 và code Trục 1 (tàu chỉ đến từ `VIE_event_scheduler_naval`) |
| Focus chỉ đọc: Focus tiền đề, ngày, trạng thái thế giới, năng lực nhánh khác | Cùng mẫu Trục 1 lục quân (`VIE_def_industry_law`: ngày + root) |
| Mốc 40% đặt `VIE_cap_ba_son_yard` sớm để không chặn Molniya pha 2 | Đúng nguyên tắc, và Trục 1 đã đọc cờ này ở `VIE_naval_sched_molniya_p2` |
| Không có vòng prerequisite (5 lớp một chiều) | Kiểm lại trên code Trục 1: Trục 1 chỉ đọc lớp 1 (cờ xưởng, tier) và ghi biến cho lớp 2+ |
| Giới hạn 2 chương trình CNQP chạy cùng lúc | Giữ, nhưng đổi cách đếm (xem L4) |
| Ba Son MIO dùng `add_mio_size` | Đúng bài học Trục 2 lục quân (Q8 = a: `add_mio_funds` tự lên size, không dùng cả hai) |
| Giá dockyard dùng effect của MD, MD tự trừ 7,5 tỷ | Đúng bài học A2 của Trục 2 lục quân (không trừ tay hai lần) |

---

# PHẦN 2 — 4 LỖI CHẶN

## A1 · Focus nền không tồn tại; chuỗi Focus không có chỗ treo

Báo cáo: Focus 1 `VIE_naval_defence_law` đòi `VIE_defence_industry_modernization`. Focus này **không có ở bất kỳ file nào** (live, `.bak`, `v11_removed_*`).
Cây focus live (290 focus, root quân sự duy nhất `VIE_modernize_vpa` ở toạ độ tuyệt đối (266, 1)) **không có focus hải quân nào**; `VIE_navy_modernization`, `VIE_domestic_corvettes`... đều trong `v11_removed_*.txt`.
Cũng **không** nên dùng `VIE_def_industry_law` (cổng Trục 2 lục quân) làm tiền đề: nó mở từ `date > 2008.6.30`, nên Focus 1 + 2 + milestone 146 ngày của Decision 1 sẽ đến sớm nhất đầu 2009, sát cửa sổ Molniya pha 2 (mở 2009-06) và không còn biên an toàn.
**Fix:** Focus 1 treo trực tiếp dưới `VIE_modernize_vpa` (root quân sự còn sống, cùng cổng mà Trục 1 lục quân dùng), ngày `> 2004.12.31`. Vị trí lưới xem 5.1.

## A2 · Ba cờ `VIE_ext_*` không có chủ, nên Focus 5 và Decision 4 không bao giờ mở

`VIE_ext_viettel_mil_tech`, `VIE_ext_c4isr` không được đặt ở đâu trong repo (grep: 0 kết quả live). Nhánh "Viettel / C4ISR" của v7 đã bị xoá. Chỉ `VIE_ext_naval_missile` có người đặt (Trục 1: `VIE_naval_deliver_bastion` đặt khi giao đủ Bastion).
**Fix:** không chờ nhánh khác. Định nghĩa ba **scripted trigger** trong `VIE_md_triggers_naval.txt` (một chỗ để đổi, đúng mẫu `VIE_proc_gate_*`), mặc định ánh xạ sang focus còn sống (Phần 7). Bỏ biến `VIE_var_ext_support` (xem B4).

## A3 · Ngưỡng kinh nghiệm của Decision 5 không đạt được trên đường lịch sử

Liệt kê toàn bộ 972 tổ hợp lựa chọn mang exp (script `python tools/audit/naval_balance.py`, mục 1) theo bảng 7.3 của báo cáo:

| Đường (tất cả Basic, Nga hỗ trợ, Molniya pha 2 = 6 tàu) | `shipbuilding_exp` | `mro_exp` |
|---|---:|---:|
| Định hướng Shipbuilding trước | 46 | 10 |
| Định hướng MRO trước | 34 | 22 |
| Định hướng Cân bằng | 40 | 16 |

Ngưỡng của báo cáo là `shipbuilding_exp ≥ 50` và `mro_exp ≥ 30`: **không đường Basic nào đạt** (chỉ 233/972 tổ hợp đạt, tất cả đều là đầu tư nặng). Đây là lỗi thiết kế vì đường lịch sử không có đích (Quy tắc 5).
(Bản nháp đầu của tài liệu này đề xuất 40/20 trên một phép tính trộn hai định hướng khác nhau; phép tính đúng ở bảng trên cho thấy 40/20 cũng không đạt trên đường Basic nào, nên đã bỏ.)
**Fix:** hạ còn **`shipbuilding_exp ≥ 30` và `mro_exp ≥ 15`**. Kết quả: 779/972 tổ hợp đạt (80%). Cân bằng + Basic + Molniya pha 2 đạt (40/16); MRO trước đạt; Shipbuilding trước cần nâng D2 lên Chuyên sâu (mro_exp 20). Bỏ Molniya pha 2 mà chỉ đầu tư Basic thì không đạt (22 < 30), nên nội địa hoá vẫn được thưởng. Số này là giá trị khởi điểm, cần playtest.

## A4 · Tier Ba Son đặt khi *kết thúc* Decision làm hỏng lựa chọn 8 và 10 tàu của Trục 1

Báo cáo 5.2: `VIE_var_ba_son_tier` đặt ở Event 3 (kết thúc, 12–24 tháng). Trục 1 đã code: `vie_naval.3` option B (8 tàu) và C (10 tàu) có `trigger = { check_variable = { VIE_var_ba_son_tier > 1 } }`, và event bắn ngay khi `VIE_cap_ba_son_yard` xuất hiện (mốc 40%, tức khi tier **vẫn bằng 0**). Hậu quả: hai lựa chọn không bao giờ hiện, dù người chơi đầu tư Trọng điểm.
**Fix (đề xuất):** đặt `VIE_var_ba_son_tier` **ở mốc 40%** cùng lúc với `VIE_cap_ba_son_yard`, bằng đúng mức đã chọn (1/2/3), vì báo cáo 3.3 đã nêu nguyên tắc "đầu tư Trọng điểm không làm trễ chương trình đang chờ". Phần thưởng thật (dockyard, MIO, exp mức đầu tư) vẫn trao khi kết thúc. Đổi cách khác: bắn `vie_naval.3` chậm lại sau mốc, nhưng sẽ chạm lên hạn cửa sổ 2012-12 và làm sai lịch sử.

---

# PHẦN 3 — LỆCH SO VỚI MOD VÀ MD

## B1 · Decision không có "trạng thái chờ giữa chừng"

Báo cáo 3.2 và 7.5: Decision bắt đầu rồi chuyển sang `_waiting` khi Event kế thiếu năng lực, tự tiếp tục khi đủ. HOI4 không có trạng thái này; muốn giả lập phải có cờ + polling hàng tháng, tức đúng loại biến phản chiếu mà mục 16.3 cấm.
**Fix:** cổng ở **lúc bấm**. `available` của mỗi Decision kèm `custom_trigger_tooltip` nêu đúng điều kiện còn thiếu (mẫu `VIE_dec_z_factories`). Decision đã bắt đầu thì chạy hết, không chờ. Bỏ toàn bộ cờ `_active`, `_done`, `_waiting` và biến `_progress`.

## B2 · Cách hiển thị "đang chạy"

Decision của MD/mod chỉ có hai kiểu thời gian: `days_remove` cố định hoặc mission cố định. Báo cáo cần thời lượng động (12/18/24 tháng × hệ số nguồn hỗ trợ × hướng). Trục 2 lục quân giải bằng hai Decision riêng cho hai thời lượng (`dec_stv`, `dec_stv_fast`).
**Fix cho hải quân:** Decision chỉ là **nút khởi động** (`fire_only_once`, tốn 50 PP như lục quân). Bấm xong bắn chuỗi event chọn; lựa chọn cuối trao một **timed idea** hiển thị đang chạy (`add_timed_idea`) và hẹn event ẩn hoàn tất. Hiệu ứng thật (exp, tier, MIO, dockyard) nằm ở event ẩn hoàn tất. `days = <biến>` đã được xác minh trong mã MD cho cả `country_event` lẫn `add_timed_idea` (Phần 10), nên thời lượng động dùng `set_temp_variable` rồi truyền thẳng, không cần sinh nhánh literal.

## B3 · MIO Ba Son hiện có dùng category sai (nợ cũ, ảnh hưởng thẳng Trục 2)

`VIE_md_organizations.txt:316`: `research_categories = { CAT_patrolboat CAT_corvette CAT_frigate CAT_green_water_navy CAT_naval_sonar }`.
Đối chiếu `md_ref/MD_all_CATS.json` (194 category của MD): **chỉ `CAT_naval_sonar` tồn tại**. Tên đúng: `CAT_patrol_boats`, `CAT_corvettes`, `CAT_frigates`; `CAT_green_water_navy` không có (gần nhất `CAT_surface_ships`). Đây cùng loại nợ mà `VIE_repo_health_report.md` đã ghi cho lục quân.
Tác động: `add_tech_bonus` và thưởng nghiên cứu của MIO Ba Son sẽ im lặng hỏng; mọi `add_tech_bonus` mới của Trục 2 phải dùng token đã xác minh (danh sách ở 5.4).
**Fix:** bước 0 sửa dòng 316 (và kiểm `equipment_type = { mio_cat_only_small_ships … submarine }` với MIO reference của MD, chưa kiểm được ở đây). Chưa rõ trait khởi đầu dùng `production_efficiency_gain_factor` có nằm trong bốn khoá `production_bonus` hợp lệ của MIO hải quân (báo cáo 16.1) không: cần kiểm.

## B4 · Biến `VIE_var_ext_support` là biến phản chiếu

"Số flag `VIE_ext_*` đang được đặt, tính lại mỗi tháng" là đúng cái 16.3 cấm. Focus 5 cần "ít nhất một nguồn": dùng `OR = { … }` trực tiếp. Bỏ biến và việc tính lại hàng tháng.

## B5 · Flag năng lực dư

`VIE_cap_naval_institution`, `VIE_cap_ba_son_complete`, `VIE_cap_naval_mro`, `VIE_cap_small_combatant`, `VIE_cap_integration` đều phản chiếu trạng thái đã có (`has_completed_focus`, biến tier > 0, cờ Decision hoàn tất). Theo 16.3 chỉ giữ cờ cho **chuyển tiếp** hoặc cờ **đã có người đọc**:

| Giữ | Lý do |
|---|---|
| `VIE_cap_ba_son_yard` | Trục 1 đọc (cổng Molniya pha 2, đã code) |
| `VIE_cap_mature_naval_industry` | Trục 1B đọc (P10, P11) |
| `VIE_mro_russia_dependent` | lựa chọn không thể suy ra từ biến khác |
| `VIE_nav_d1_done`, `…_d2_done`, `…_d3_done`, `…_d4_done` | HOI4 không hỏi được "Decision đã hoàn tất", mà D4 và D5 cần biết |

Mọi thứ còn lại dùng biến tier (>0 là "có năng lực") và scripted trigger.

## B6 · Quy ước mod cho file, event, decision

- Namespace riêng, chữ thường: **`vie_nav_ind`** (`events/VIE_nav_ind.txt`), không dùng chung `vie_naval` của Trục 1 (Trục 2 lục quân cũng tách `vie_def_ind`).
- Log câu đầu tiên của mỗi option/effect; option chỉ đóng cửa sổ không log (quy tắc MD). Mọi `ai_chance` của option có tốn tiền có guard `bankruptcy_incoming_collapse` (và `ai_has_high_deficit` cho option không-lịch-sử), mẫu đã áp ở Trục 1 hải quân.
- Loc: `localisation/english/VIE_md_events_nav_ind_l_english.yml` (BOM, tiếng Việt, `:0` như toàn repo).
- Ảnh event: tạo bằng `tools/build_vie_event_pictures.py`; hoặc `GFX_report_event_generic_read_write` tạm.
- Icon focus: thêm 6 mục vào `FOCI` của `tools/build_vie_focus_icons.py` (sprite `GFX_focus_VIE_<stem>`); tạm dùng icon generic của MD cho tới khi có ảnh.

---

# PHẦN 4 — LỖ HỔNG LOGIC VÀ THIẾT KẾ ĐÃ SỬA

## L1 · Orientation của Decision 1 nên chọn ở Focus 2, không ở Decision

Event 1 "chọn định hướng" của báo cáo là lựa chọn một lần, không phụ thuộc Decision. Đặt nó ở **hoàn thành Focus 2** (focus bắn event, đúng Quy tắc 6: Focus không đọc kết quả Decision, nhưng được phép *bắn* event). Hệ quả: Decision 1 chỉ còn một event chọn mức đầu tư, và định hướng đã sẵn khi bấm. Không phá Quy tắc 6 vì Focus 3 và 4 không đọc `VIE_ba_son_orientation`.

## L2 · Công thức thời lượng và chi phí cần số thật

Báo cáo chỉ có hệ số. Đề xuất thang tuyệt đối (tỷ USD; ngày). Chi phí dùng effect có sẵn của MD khi có thể, phần còn lại `modify_treasury_effect`:

| Decision | Cơ bản | Mở rộng | Trọng điểm | Cách trả |
|---|---|---|---|---|
| D1 Ba Son (365 / 548 / 730 ngày) | 7,5 | 12,0 | 18,0 | `one_state_dockyard` ×1 / ×1 + 4,5 tay / `two_state_dockyards` hoặc ×2 + 3,0 tay (MD tự trừ 7,5 mỗi cái, **không** trừ tay phần đó nữa) |
| D2 MRO (cơ sở 4,0) | ×0,8 Nga / ×1,4 tự chủ; ×1,3 toàn hạm đội | | | `modify_treasury_effect` |
| D3 Small Combatant (cơ sở 6,0) | ×1,0 | ×1,6 | ×2,4 | `modify_treasury_effect` |
| D4 Integration (cơ sở **7,0**) | bậc ×1,0 / 1,6 / 2,4; lĩnh vực Full ×1,5 | | | `modify_treasury_effect` |
| D5 Naval 2030 (cơ sở 10,0) | Limited ×1,0 | Integrated ×1,5 | High ×2,2 | `modify_treasury_effect` |

Tổng đường lịch sử Trục 2 (tất cả Basic, Nga hỗ trợ, Limited) = **33,7 tỷ**, tối đa 97,1 (mọi bậc cao nhất, hiếm gặp); cộng Trục 1 (5,45 tỷ sau khi sửa giá Bastion-P) = 39,15 tỷ (Trục 2 lục quân: 30,25). Mọi mục đều dưới p90 của chi phí event MD (26,45 tỷ; trung vị 4,0). Đây là **giá trị khởi điểm cần cân bằng**, không có nguồn lịch sử. Đo bằng `python tools/audit/naval_balance.py`.
Thời lượng D2 = mức (365/548/730) × 0,75 nếu Nga hỗ trợ, × 1,25 nếu tự chủ, × 0,85 nếu Trục 1 đã đặt `VIE_opp_sub_mro` (đủ Kilo giao). D1 và D3 chịu hệ số ±25% theo định hướng như báo cáo 5.2.

## L3 · Điều kiện nguồn tàu của Decision 2 phải đọc đúng biến của Trục 1

Báo cáo 5.3 ghi "đã giao ít nhất 1 Gepard hoặc Molniya". Trục 1 đã code:

| Cần | Biến / cờ thật trong code Trục 1 |
|---|---|
| Có tàu ngầm Kilo | `VIE_kilo_qty_delivered > 0` |
| Có tàu mặt nước | `VIE_gepard1_qty_delivered > 0` hoặc `VIE_gepard2_qty_delivered > 0` hoặc `VIE_molniya_ru_delivered > 0` hoặc `VIE_molniya_vn_qty_delivered > 0` |
| Cơ hội MRO tàu ngầm đủ bộ | `VIE_opp_sub_mro` (giảm thời lượng 15%, không phải cổng) |
| Số thân tàu cho Focus 3 | `VIE_var_hulls_delivered ≥ 4` (báo cáo ghi `hulls_operational`; Trục 1 đã đổi tên) |

Gom thành scripted trigger `VIE_naval_has_sub`, `VIE_naval_has_surface` trong file trigger để Focus/Decision/test cùng dùng.

## L4 · Bộ đếm slot `VIE_var_naval_program_active` cần chốt biên

+1 khi Decision bắt đầu, −1 khi event ẩn hoàn tất. Nếu người chơi lưu/tải giữa chừng biến vẫn đúng (biến lưu theo save). Nếu event hoàn tất bị mất (đổi tag sau nội chiến) bộ đếm kẹt ở 2 và chặn cả nhánh. **Fix:** `available` của Decision gắn thêm `OR = { check_variable = { VIE_var_naval_program_active < 2 } has_country_flag = VIE_civil_war_reset }`, và `VIE_collapse_aftermath` (đã tồn tại) reset biến về 0 khi nội chiến xong. Ghi vào checklist.

## L5 · Trục 2 phải cung cấp ngược cho Trục 1: giá Molniya pha 2 theo hệ số Decision 3

Báo cáo 5.4: Decision 3 cấp "hệ số giảm chi phí cho chương trình đóng tàu nhỏ". Trục 1 chưa đọc hệ số này. **Fix (sửa nhỏ Trục 1):** `VIE_naval_pay_molniya_p2` nhân thêm `VIE_small_combatant_cost_mult` nếu biến có giá trị > 0 (0,8–1,0), xem bước 7.

## L6 · Cổng thưởng của Trục 1 có nguồn thật từ Trục 2

Hai trigger `VIE_naval_bonus_modernization` và `VIE_naval_bonus_russian_deals` hiện mặc định `always = no`. Gợi ý: `bonus_modernization = has_completed_focus = VIE_naval_defence_law` (Focus 1 xong thì mở các lựa chọn quy mô lớn hơn của Gepard/Bastion/Sigma). `bonus_russian_deals` giữ tắt cho tới khi có focus ngoại giao Nga (không thuộc Trục 2).

---

# PHẦN 5 — THIẾT KẾ CHỐT CHO CODE

## 5.1 Sáu Focus (tọa độ tuyệt đối, tương đối từ `VIE_modernize_vpa` = (266, 1))

Vùng x 216–262 trống ở mọi hàng (kiểm bằng script layout 2026-10-02); cột quân sự hiện nằm x 264–284.

| # | Focus | Treo từ | `relative_position_id` | (x, y) tương đối → tuyệt đối | Điều kiện mở | Khi hoàn thành |
|---|---|---|---|---|---|---|
| 1 | `VIE_naval_defence_law` | root | `VIE_modernize_vpa` | (−8, 1) → (258, 2) | prerequisite `VIE_modernize_vpa`; `date > 2004.12.31`; `NOT has_active_mission = bankruptcy_incoming_collapse` | XP hải quân (hoặc mastery nếu `has_selected_naval_grand_doctrine`), `unlock_decision_category_tooltip = VIE_naval_industry_category`; đồng thời `VIE_naval_bonus_modernization` thành đúng (L6) |
| 2 | `VIE_ba_son_shipyards` | F1 | F1 | (0, 1) → (258, 3) | F1; `date > 2004.12.31` | bắn event chọn định hướng (L1), `unlock_decision_tooltip = VIE_nav_d1_ba_son` |
| 3 | `VIE_naval_mro` | F2 | F2 | (−2, 1) → (256, 4) | F2; `date > 2011.12.31`; `VIE_var_hulls_delivered ≥ 4` | `unlock_decision_tooltip = VIE_nav_d2_mro` |
| 4 | `VIE_small_combatant_construction` | F2 | F2 | (+2, 1) → (260, 4) | F2; `date > 2009.12.31` | `unlock_decision_tooltip = VIE_nav_d3_small` |
| 5 | `VIE_naval_systems_integration` | F3 **và** F4 | F3 | (+2, 1) → (258, 5) | `prerequisite` F3 và F4 (hai khối riêng = AND); `date > 2017.12.31`; ít nhất một trong `VIE_naval_has_electronics`, `VIE_naval_has_c4isr`, `VIE_naval_has_missile` | `unlock_decision_tooltip = VIE_nav_d4_integration` |
| 6 | `VIE_naval_defence_2030` | F3, F4, F5 | F5 | (0, 1) → (258, 6) | F3, F4, F5; `date > 2027.12.31` | `unlock_decision_tooltip = VIE_nav_d5_2030` |

Mọi Focus: `search_filters = { FOCUS_FILTER_NAVY FOCUS_FILTER_INDUSTRY }`, `cost = 7` (F1 và F2 `cost = 5`), `log` đầu `completion_reward`, `ai_will_do` base 90 với `date > 2004.12.31` cho F1 và F2 (AI cần Ba Son trước 2009), 60–70 cho F3–F6; mọi cái `factor = 0` khi `bankruptcy_incoming_collapse`. Chạy `python tools/audit/audit.py` kiểm lưới, không prerequisite quá dài.
Không có `FOCUS_FILTER_NAVY` thừa: filter này đã có 11 chỗ dùng trong file focus.

## 5.2 Năm Decision (category `VIE_naval_industry_category`)

Category: `allowed = { original_tag = VIE }`, `priority = 90`, `visible = { has_completed_focus = VIE_naval_defence_law }`. Mỗi Decision: `fire_only_once = yes`, `cost = 50`, `visible` theo Focus của nó, `available` có `custom_trigger_tooltip` cho từng điều kiện, `complete_effect` log đầu + tăng `VIE_var_naval_program_active` + bắn event chọn. `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Focus mở | `available` (cổng lúc bấm) | Chuỗi event chọn | Hoàn tất |
|---|---|---|---|---|
| D1 `VIE_nav_d1_ba_son` | F2 | `VIE_var_naval_program_active < 2` | `.2` mức đầu tư (3 lựa chọn, L2) | mốc 40% (146 / 219 / 292 ngày): đặt `VIE_cap_ba_son_yard`, `VIE_var_ba_son_tier` = mức (A4). Kết thúc: dockyard, MIO `+1/+2/+3`, exp `+5/+10/+15`, `VIE_nav_d1_done`, −1 slot |
| D2 `VIE_nav_d2_mro` | F3 | slot; `VIE_naval_has_sub` hoặc `VIE_naval_has_surface` | `.10` trọng tâm, `.11` nguồn hỗ trợ (Nga = lịch sử), `.12` mức nội địa hóa (mức sau cần `mro_exp` đủ ngưỡng) | exp `+10/+20/+30`; `VIE_var_mro_tier`; cờ `VIE_mro_russia_dependent` nếu chọn Nga (trần `mro_exp` 50); địa điểm MRO tàu ngầm ghi **Cam Ranh** trong loc |
| D3 `VIE_nav_d3_small` | F4 | slot | `.20` chuyên hoá (Tuần tra / Tốc độ cao / Đa dụng), `.21` mức sản xuất (tier 3 cần `VIE_molniya_domestic_started`, cờ Trục 1) | exp `+5…+8` rồi `+5/+10/+15`; `VIE_small_combatant_cost_mult` = 0,80 / 0,85 / 0,90 (L5); `VIE_var_small_combatant_tier`; MIO `+1` |
| D4 `VIE_nav_d4_integration` | F5 | slot; lĩnh vực cần nguồn đúng (Electronics: `VIE_naval_has_electronics` hoặc `…_c4isr`; Weapons: `VIE_naval_has_missile`; Full: một nguồn điện tử và missile, ×1,5) | `.30` lĩnh vực, `.31` mức nội địa hoá | exp `+10/+20/+30`; `VIE_var_integration_tier`; nếu đã giao Sigma thì Cân bằng cho thêm exp |
| D5 `VIE_nav_d5_2030` | F6 | slot; `shipbuilding_exp ≥ 30`, `mro_exp ≥ 15` (A3) | `.40` ưu tiên (4 lựa chọn), `.41` mức tự chủ (Limited: không thêm; Integrated: `ba_son_tier ≥ 2`; High: `ba_son_tier = 3` và `integration_tier ≥ 2`) | đặt `VIE_cap_mature_naval_industry`; không cấp tàu |

Event ẩn hoàn tất: `.61` D1 kết thúc, `.62` D2, `.63` D3, `.64` D4, `.65` D5; `.60` mốc 40% của D1. Chuỗi event chọn là event nối tiếp nên miễn `VIE_popup_cd` (do người chơi chủ động bấm Decision).
Bấm xong, `add_timed_idea` hiển thị đang chạy; hẹn event ẩn bằng `days`.

## 5.3 Quy tắc dòng chảy giữa Trục 1 và Trục 2 (hợp đồng cờ/biến, sau sửa)

| Cạnh | Hướng | Qua | Trạng thái |
|---|---|---|---|
| Ba Son → Molniya pha 2 | T2 → T1 | `VIE_cap_ba_son_yard` (mốc 40%), `VIE_var_ba_son_tier` (cũng ở mốc 40%, A4) | Trục 1 đọc rồi; Trục 2 chưa ghi |
| Molniya pha 2 → Small Combatant | T1 → T2 | `VIE_molniya_domestic_started`, `VIE_var_shipbuilding_exp` | Trục 1 ghi rồi; Trục 2 chưa đọc |
| Kilo → MRO tàu ngầm | T1 → T2 | `VIE_kilo_qty_delivered`, `VIE_opp_sub_mro` | Trục 1 ghi rồi |
| Gepard / Molniya → MRO mặt nước, Focus 3 | T1 → T2 | `…_delivered`, `VIE_var_hulls_delivered` | Trục 1 ghi rồi |
| Bastion → Weapons | T1 → T2 | `VIE_ext_naval_missile` | Trục 1 ghi rồi |
| Sigma → Integration (tuỳ chọn) | T1 → T2 | `VIE_sigma_qty_delivered`, `VIE_var_integration_exp` | Trục 1 ghi rồi; Sigma Domestic/Hybrid đã cộng `integration_exp` |
| Decision 3 → giá Molniya pha 2 | T2 → T1 | `VIE_small_combatant_cost_mult` | **Cần sửa Trục 1** (L5) |
| Focus 1 → quy mô lớn của Trục 1 | T2 → T1 | `VIE_naval_bonus_modernization` | **Cần sửa trigger** (L6) |

## 5.4 Phần thưởng và token đã kiểm chứng

Chỉ dùng token đã xác minh trong repo hoặc `md_ref`:
- **Tech bonus (`add_tech_bonus`):** `CAT_patrol_boats`, `CAT_corvettes`, `CAT_frigates`, `CAT_attack_submarines`, `CAT_naval_sonar`, `CAT_naval_electronics`, `CAT_naval_fire_control`, `CAT_naval_missiles`, `CAT_naval_radar` (đều có trong `MD_all_CATS.json`). **Không** dùng `CAT_patrolboat`, `CAT_corvette`, `CAT_frigate`, `CAT_green_water_navy`.
- **MIO:** chỉ `mio:VIE_ba_son_manufacturer = { add_mio_size = N }` qua helper `VIE_ba_son_mio_size_N` (mẫu `VIE_gdt_mio_size_N`). Không mở trait bằng script (bài học B3 của Trục 2 lục quân). Không dùng `add_mio_funds` cùng `add_mio_size`.
- **Modifier trong idea hiển thị/thưởng:** chỉ token đã xuất hiện trong repo: `experience_gain_navy_factor`, `navy_submarine_attack_factor`, `naval_speed_factor`, `naval_hit_chance`, `naval_detection`, `naval_coordination`. "Giảm chi phí duy trì hạm đội" của báo cáo **chưa có token đã kiểm**: bỏ cho tới khi xác minh token (bước 3 của plan).
- **Building:** `one_state_dockyard` và `two_state_dockyards` của MD (tự trừ tiền, `CONTROLLER`); không dùng `add_building_construction` trần cho dockyard.

---

# PHẦN 6 — PLAN CODE (9 bước, mỗi bước 1 commit)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `VIE_md_organizations.txt` | Sửa `research_categories` của Ba Son (B3); kiểm `equipment_type`; ghi nợ nếu còn token sai | `python tools/audit/live.py` và thử MIO mở trong game, `error.log` |
| **1** | `common/scripted_triggers/VIE_md_triggers_naval.txt` | Thêm `VIE_naval_has_sub`, `VIE_naval_has_surface`, `VIE_naval_has_electronics`, `VIE_naval_has_c4isr`, `VIE_naval_has_missile` (ánh xạ Phần 7); đổi `VIE_naval_bonus_modernization` (L6) | brace; `check6.py`-kiểu quét trigger đã định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Sáu Focus (5.1), reward chỉ XP + tooltip, **chưa** có event; ảnh/icon tạm | `python tools/audit/audit.py` (lưới, prerequisite); `verify_all_loc.py`; mở cây focus, thấy cột hải quân dưới root |
| **3** | `common/scripted_effects/VIE_md_effects_nav_ind.txt` | Helper: `VIE_ba_son_mio_size_1/2/3`, `VIE_nav_add_shipbuilding_exp` (kẹp 0–100), `…_mro_exp` (trần 50 nếu `VIE_mro_russia_dependent`), `…_integration_exp`, `VIE_nav_program_start/end` (slot), hàm quy đổi mức → ngày/chi phí (L2) | brace; undefined-call scan |
| **4** | `events/VIE_nav_ind.txt` (`add_namespace = vie_nav_ind`) + `common/decisions/VIE_md_nav_ind_decisions.txt` + category | **Decision 1** trọn vẹn: event định hướng (bắn từ F2), `.2` mức đầu tư, `.60` mốc 40%, `.61` kết thúc; timed idea với `days = <biến tạm>` (Phần 10) | chơi: F1 → F2 → định hướng → D1 → 146–292 ngày sau `VIE_cap_ba_son_yard` và `VIE_var_ba_son_tier` > 0; `vie_naval.3` B/C hiện khi tier ≥ 2 |
| **5** | cùng file | **Decision 3, 2** (cần dữ liệu Trục 1: `VIE_molniya_domestic_started`, các `_delivered`), exp, `VIE_small_combatant_cost_mult` | thử với console đặt biến Trục 1 |
| **6** | cùng file | **Decision 4, 5** + Sigma bonus + `VIE_cap_mature_naval_industry` | thử Focus 5–6 bằng console ngày; ngưỡng exp (A3) |
| **7** | `VIE_md_effects_naval_ships.txt` | Sửa nhỏ Trục 1: `VIE_naval_pay_molniya_p2` nhân `VIE_small_combatant_cost_mult` (L5) | ghi chú trong TESTING; thử giá |
| **8** | `common/scripted_effects/VIE_md_effects_p3.txt` (`VIE_collapse_aftermath`) | Reset `VIE_var_naval_program_active` sau nội chiến (L4); catch-up Trục 2 | checklist nội chiến |
| **9** | `localisation/english/VIE_md_events_nav_ind_l_english.yml`; `tools/TESTING.md`; `VIE_v9_flag_mapping.md`; `tools/build_vie_focus_icons.py` (6 mục `FOCI`) | Loc (BOM), mục "Naval industry" trong TESTING, bảng cờ Trục 2, ảnh/icon | `python tools/verify_all_loc.py`; `python tools/audit/ev.py` không orphan |

Ước lượng: 6 Focus, 5 Decision, khoảng 16 event (5 chuỗi chọn + 6 ẩn), ~800 dòng script, ~120 khóa loc. Nhỏ hơn báo cáo vì `_waiting`/`_active`/`_progress` bị bỏ.

---

# PHẦN 7 — ÁNH XẠ NGUỒN `VIE_ext_*` (đề xuất, A2)

Focus live, không phụ thuộc nhánh chưa xây:

| Trigger | Định nghĩa đề xuất | Ghi chú |
|---|---|---|
| `VIE_naval_has_electronics` | `OR = { has_completed_focus = VIE_semiconductor_fab has_completed_focus = VIE_chip_design }` | Điện tử bán dẫn dân sự ứng dụng quân sự (dual-use). Cần kiểm tên focus còn sống và `date` hợp lý (fab xuất hiện muộn) |
| `VIE_naval_has_c4isr` | `OR = { has_completed_focus = VIE_earth_observation has_completed_focus = VIE_vinasat }` | Vệ tinh quan sát/viễn thông. Ứng viên thay thế: `VIE_lf_cap_cyber_ew` hoặc `VIE_lf_cap_info_ops` của Trục 3 lục quân (nối chéo quân chủng, không khuyến nghị) |
| `VIE_naval_has_missile` | `has_country_flag = VIE_ext_naval_missile` | Trục 1 đặt khi giao đủ Bastion; có thể thêm nguồn ngành tên lửa sau |

Quy tắc 6(d) gốc nói "năng lực do nhánh khác sở hữu"; ở đây chủ sở hữu là focus còn sống, vẫn đúng tinh thần. Khi nhánh Viettel/C4ISR thật được xây, đổi một dòng.

---

# PHẦN 8 — CÂU HỎI ĐÃ CHỐT (2026-10-03: N1–N6 theo mặc định, N7 = Có)

| # | Câu hỏi | Mặc định |
|---|---|---|
| N1 | Focus 1 treo dưới `VIE_modernize_vpa` (A1) hay dựng một focus cổng hải quân mới (`VIE_navy_modernization` làm lại)? | **ĐÃ CHỐT:** treo thẳng dưới `VIE_modernize_vpa`; Trục 3 sau này tự dựng cổng riêng |
| N2 | Đặt `VIE_var_ba_son_tier` ở mốc 40% (A4) hay chỉ khi kết thúc? | **ĐÃ CHỐT:** mốc 40% |
| N3 | Ngưỡng Decision 5 (A3): 30 và 15 (đã tính lại), hay giữ 50 và 30 và tăng nguồn exp? | **ĐÃ CHỐT:** 30 và 15 |
| N4 | Nguồn `VIE_naval_has_electronics` / `…_c4isr` (Phần 7) | **ĐÃ CHỐT:** như bảng Phần 7 |
| N5 | Thang chi phí (L2) là giá trị tự đặt (tổng đường lịch sử 34,7 tỷ). Chấp nhận để cân bằng sau? | **ĐÃ CHỐT:** có |
| N6 | `bonus_modernization` mở bởi Focus 1 (L6), còn `bonus_russian_deals` giữ tắt? | **ĐÃ CHỐT:** có |
| N7 | Bấm Decision nay là nút khởi động + chuỗi event (B2), không còn Decision hiển thị đang chạy. Chấp nhận timed idea làm chỉ báo? | **ĐÃ CHỐT: Có** (2026-10-02) |

---

# PHẦN 9 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào TESTING.md ở bước 9)

- [ ] `error.log`: grep `vie_nav_ind`, `VIE_nav_`, `VIE_naval_has_`, `CAT_`, `add_tech_bonus`, `add_mio_size`, `add_timed_idea`.
- [x] `days = <biến>` đã xác minh bằng mã nguồn MD (Phần 10); không cần nhánh literal. Vẫn thử một lần trong game.
- [ ] Đường lịch sử: F1 → F2 (2005) → định hướng → D1 Cơ bản: `VIE_cap_ba_son_yard` sau 146 ngày; năm 2009-06 `vie_naval.3` xuất hiện; tier = 1 nên chỉ A và E hiện. Với Mở rộng: B và C hiện (A4).
- [ ] D1 trả tiền đúng 1 lần: kiểm `treasury` trước/sau, chỉ trừ 7,5 cho dockyard và phần tay còn lại, không 15 (bài học A2 lục quân).
- [ ] D2: đủ điều kiện sau khi giao tàu đầu của Kilo; "Toàn hạm đội" yêu cầu cả hai; chọn Nga: `VIE_mro_russia_dependent` đặt và `mro_exp` kẹp ở 50.
- [ ] D3: tier 3 chỉ hiện khi `VIE_molniya_domestic_started`; sau D3, `VIE_naval_pay_molniya_p2` rẻ hơn.
- [ ] D4: Weapons cần `VIE_ext_naval_missile` (giao đủ Bastion trong Trục 1); Electronics cần `VIE_naval_has_electronics` hoặc `…_c4isr`.
- [ ] D5: Cân bằng + Basic + Molniya pha 2 mở được (40/16 so với ngưỡng 30/15); Shipbuilding trước cần D2 Chuyên sâu; kiểm ba mức tự chủ và điều kiện tier.
- [ ] Slot: bấm D2 và D3 cùng lúc, D4 phải bị chặn bởi 2/2; hoàn tất một cái thì mở lại.
- [ ] Nội chiến: `VIE_var_naval_program_active` về 0, Decision không kẹt.
- [ ] AI-only đến 2020: AI VIE có `VIE_cap_ba_son_yard` trước 2009-06 (nếu không, Molniya pha 2 mất; xem `ai_will_do` F1, F2, D1).
- [ ] Đếm pop-up: các event chọn là chuỗi do người chơi bấm Decision nên không ảnh hưởng ngân sách pop-up tự động.

---

# PHẦN 10 — KIỂM CHỨNG CHÉO VỚI MD VÀ GAME GỐC (2026-10-02)

## 10.1 `days = <biến>`: **được**, bằng chứng từ mã nguồn MD

Tải mã nguồn MD (`MillenniumDawn/Millennium-Dawn`, nhánh `main`, sparse clone `common/` và `events/`) và quét toàn bộ cú pháp `days = <tên>` (không phải số, không phải `@hằng`):

| Effect | Có biến? | Ví dụ thật trong MD |
|---|---|---|
| `add_timed_idea` | **Có** (10 chỗ) | `HKG_scripted_effects.txt:470`: `set_temp_variable = { idea_len = … }` rồi `add_timed_idea = { idea = HKG_contract_dockyard_revenue days = idea_len }`; `BOS_scripted_effects.txt:421`: `days = BOS_recovery_days` (biến quốc gia); `eu_scripted_effects.txt:1163`: `days = potef_term_temp` |
| `country_event` | **Có** | `events/United States.txt` (usa.202): `set_temp_variable = { USA_f22_next_days = { value = USA_f22_stage_base multiply = 0.6 round = yes } }` rồi `country_event = { id = usa.203 days = USA_f22_next_days }` |
| `set_country_flag` | **Có** | `CZE_scripted_effects.txt:1154`: `flag = … days = CZE_petr_pavel_mission_duration value = 1` |

Ghi chú:
- Dạng tính trước dùng khối `set_temp_variable = { tên = { value = … multiply = … round = yes } }`. Nên có `round = yes` vì số ngày phải nguyên.
- MD cũng dùng `days = @HẰNG` (hằng biên dịch, `@HOL_D66_time_tier_1`) ở nhiều nơi: đó là hằng số, không phải biến thời gian chạy; không dùng để suy ra biến.
- **Không có** ví dụ nào trong MD cho `months = <biến>`, `hours = <biến>` hay `random_days = <biến>`. Trục 2 chỉ dùng `days`, nên không ảnh hưởng.
- Wiki HOI4 (hoi4.paradoxwikis.com, Event modding) chỉ liệt kê ví dụ số, không nói rõ; bằng chứng thực tế là mã MD ở trên. Kiểm lại một lần trong game vẫn nên làm (checklist).

**Áp dụng cho Trục 2 và cả Trục 1 hải quân:** Sigma hiện chia ba nhánh `if` literal (900 / 1080 / 1260 và 1125 / 1350 / 1575 ngày) vì lúc viết chưa chắc; có thể gọn lại bằng `set_temp_variable` rồi `days = <biến>`. Không cần sửa ngay (không lỗi), ghi lại làm việc dọn tuỳ chọn.

## 10.2 Quy ước MD cho phần bấm giờ

- Ví dụ MD đặt biến tạm trong **cùng option/effect** với lệnh dùng nó (`USA_f22_next_days` đặt rồi dùng ngay): làm vậy, không truyền biến tạm qua event khác.
- Thời lượng cần lưu cho event hoàn tất thì đã biết lúc hẹn; event ẩn không cần đọc lại (dữ liệu lựa chọn nằm ở biến quốc gia `VIE_ba_son_invest`, v.v.).
- Hệ số thời lượng: `value = base multiply = 0.75 round = yes` (Nga), `1.25` (tự chủ), `0.85` (`VIE_opp_sub_mro`).

## 10.3 Con số cân bằng: kết quả `tools/audit/naval_balance.py` (PASS)

| Kiểm tra | Kết quả |
|---|---|
| Ngưỡng exp D5 | Báo cáo (50/30) không đạt trên đường Basic nào; ngưỡng mới 30/15 cho 80% tổ hợp đạt; bỏ Molniya pha 2 thì Basic không đủ |
| Chi phí | Trục 1 lịch sử 5,45 tỷ; Trục 2 lịch sử 33,7 tỷ (tối đa 97,1); tổng 39,15 tỷ; mục đơn lớn nhất 25,2 tỷ (D4 Tự chủ cao + toàn hệ thống) < p90 MD (26,45) |
| So với MD | 1807 giá trị `treasury_change = -N` trong event MD: p25 0,3; trung vị 4,0; p75 10,0; p90 26,45. Giá hải quân Trục 1 (0,06–3,2) thuộc nửa thấp, Trục 2 (3,2–22) quanh p50–p90 |
| Ngân khố VIE đầu game | `history/countries/VIE`: `treasury = 5`, `debt = 77,514`. Funding Gate Sigma (≤ 0,86 tỷ cho 2 tàu Domestic) đạt từ đầu game |
| Mốc 40% của D1 | Sớm nhất 2005-08 / 2005-10 / 2005-12 (Cơ bản / Mở rộng / Trọng điểm); Focus 1 chậm nhất 2008-06-04 vẫn kịp tier 3 trước 2009-06 |
| Dockyard | MD `one_state_dockyard` 7,5 tỷ, `two_state_dockyards` 15 tỷ (tự trừ). `gdp_total` của MD cộng GDP từ dockyard (`gdp_from_dockyards`), nên dockyard mới có hoàn vốn qua GDP |

Giới hạn của phép kiểm: MD không công bố thu nhập hàng tháng của VIE trong dữ liệu đã tải, nên chưa mô phỏng được dòng tiền theo năm; chi phí chỉ so với phân bố chi phí event của MD và ngân khố đầu game. Cần observe-run trong game để xem `treasury` thật quanh 2009–2012 (Kilo 3,2 tỷ) và 2012–2020 (D1 7,5–18 tỷ, D3, D4).

---

# TRẠNG THÁI THI CÔNG (2026-10-03)

| Bước | Trạng thái |
|---|---|
| 0 Sửa MIO Ba Son | Xong: `research_categories` đổi thành `CAT_patrol_boats CAT_corvettes CAT_frigates CAT_surface_ships CAT_naval_sonar` (đều có trong MD). Kiểm với mã MD: `equipment_type = { mio_cat_only_small_ships mio_cat_frigates mio_cat_destroyers submarine }` hợp lệ; `production_efficiency_gain_factor` hợp lệ (495 chỗ dùng trong MD), nên mối lo ở B3 về khoá của trait khởi đầu **không còn**. Nợ cũ còn lại (ngoài phạm vi): ba MIO khác của repo (Viettel, GDT, VAECO) vẫn dùng `CAT_cnc`, `CAT_inf_wep`, `CAT_heli`... |
| 1 Trigger | Xong: `VIE_naval_has_sub`, `_has_surface`, `_has_electronics`, `_has_c4isr`, `_has_missile`, `_has_ext_source`; `VIE_naval_bonus_modernization` = Focus 1 xong |
| 2 Sáu Focus | Xong: 6 focus ở (258,2) (258,3) (256,4) (260,4) (258,5) (258,6); reward chỉ XP/mastery; loc trong `VIE_md_events_nav_ind_l_english.yml`. Chưa có event định hướng và `unlock_decision_tooltip` (thuộc bước 4 vì Decision chưa tồn tại) |
| 3 Helper | Xong: `VIE_md_effects_nav_ind.txt` (MIO size 1–3, exp shipbuilding/mro/integration có kẹp, slot start/end, `VIE_nav_d1_start`, `VIE_nav_d1_finish`) |
| 4 Decision 1 | Xong: Focus 2 bắn `vie_nav_ind.1` (định hướng); Decision `VIE_nav_d1_ba_son` (50 PP, cổng slot < 2 và đã chọn định hướng) bắn `.2` (mức đầu tư); `days = <biến tạm>` cho timed idea và hai event hẹn giờ; `.60` mốc 40% đặt `VIE_cap_ba_son_yard` và `VIE_var_ba_son_tier`; `.61` xây dockyard ở state 519 (TP Hồ Chí Minh), MIO +1/+2/+3, exp +5/+10/+15, đặt `VIE_nav_d1_done`, trả slot. Chi phí: dockyard do MD tự trừ, phần còn lại trừ tay tại lúc bắt đầu; định hướng Cân bằng +15% tổng giá. Idea `VIE_nav_prog_ba_son` hiển thị đang chạy |
| 5 Decision 3 và 2 | Xong: `VIE_nav_d3_small` (cổng: Ba Son dùng được) với `.20` chuyên hóa, `.21` mức sản xuất, `.63` kết thúc; `VIE_nav_d2_mro` (cổng: đã có tàu ngầm hoặc tàu mặt nước từ Trục 1) với `.10` trọng tâm, `.11` nguồn hỗ trợ, `.12` mức nội địa hóa, `.62` kết thúc. Thời lượng D2 = gốc × nguồn (Nga 0,75, tự chủ 1,25) × định hướng (MRO trước 0,75, đóng tàu trước 1,25) × 0,85 nếu `VIE_opp_sub_mro`; D3 chịu hệ số định hướng ngược lại. Chi phí D2 = 4,0 × bậc (1/1,6/2,4) × nguồn (0,8/1,4) × 1,3 nếu toàn hạm đội. **Lệch với báo cáo:** điều kiện "mức sau cần `mro_exp` đủ ngưỡng" của D2 đổi thành "cần Ba Son đã hoàn tất" (bậc 2) và "cần thêm đầu tư Mở rộng trở lên hoặc D3 xong" (bậc 3), vì `mro_exp` chưa có nguồn nào trước D2 (định hướng Đóng tàu trước chỉ có 0) nên điều kiện theo `mro_exp` sẽ khóa vĩnh viễn hướng đó khỏi Decision 5 |
| 6 Decision 4 và 5 | Xong: `VIE_nav_d4_integration` (cổng: có một nguồn điện tử, C4ISR hoặc tên lửa) với `.30` lĩnh vực (mỗi lĩnh vực cần đúng nguồn, Full cần cả điện tử/C4ISR và tên lửa, ×1,5), `.31` mức nội địa hóa (giá gốc **7,0** × bậc), `.64` kết thúc (+10/+20/+30 exp tích hợp, +5 nếu Cân bằng và đã giao Sigma, thưởng công nghệ). `VIE_nav_d5_2030` (cổng: `shipbuilding_exp ≥ 30`, `mro_exp ≥ 15`) với `.40` ưu tiên (Đóng tàu cần D1 xong, Bảo dưỡng cần D2 xong, Tích hợp cần D4 xong, Toàn diện cần cả ba), `.41` mức tự chủ (Limited 24 tháng 10 tỷ; Integrated 30 tháng 15 tỷ cần `ba_son_tier ≥ 2`; High 36 tháng 22 tỷ cần `ba_son_tier = 3` và `integration_tier ≥ 2`), `.65` kết thúc: MIO +1/+2/+3, thưởng công nghệ theo ưu tiên, idea `VIE_nav_mature_industry_idea`, đặt `VIE_cap_mature_naval_industry`. Giá D4 đổi từ gốc 8,0 xuống 7,0 để mục đắt nhất (24 × 1,5 ở bậc cao) nằm dưới p90 của MD |
| 7 Trục 1 đọc hệ số Decision 3 | Xong: `VIE_naval_pay_molniya_p2` và phụ phí ký muộn `VIE_naval_late_start_molniya_p2` nhân thêm `VIE_small_combatant_cost_mult` (0,8–0,9) khi biến > 0 |
| 8 Nội chiến | Xong: `VIE_nav_program_recount` đếm lại slot theo các timed idea chương trình đang giữ, gọi trong `VIE_collapse_aftermath`. Tag nổi loạn thắng thì về 0; cùng tag thì giữ số chương trình còn chạy. Giới hạn đã biết: event hoàn tất đã hẹn bị mất khi đổi tag, nên chương trình của tag cũ không tự hoàn tất cho tag mới |
| 9 Tài liệu | Xong: mục "Naval industry" trong `tools/TESTING.md` (checklist ~20 mục, mục đầu tiên là kiểm `days = <biến>` trong game), bảng cờ và biến trong `VIE_v9_flag_mapping.md`, sáu mục `FOCI` trong `tools/build_vie_focus_icons.py`. Icon riêng **chưa tạo** (cần chạy `search` rồi duyệt ảnh); sáu focus giữ icon generic cho tới lúc đó |

Bước 0–9 xong về code và tài liệu; toàn bộ chưa chạy trong game.

---

# SỬA SAU RÀ SOÁT (2026-10-03)

Rà soát cả hai trục (đối chiếu mã MD `main`) tìm ra bốn lỗi, đã sửa:
1. Decision 5 có thể mở khi chưa chương trình nào xong, làm event ưu tiên `.40` không còn lựa chọn và kẹt slot: cổng thêm `VIE_nav_d1_done` (tooltip `VIE_nav_d1_done_tt`).
2. AI có thể không chọn được ở `.10` và `.30` (mọi option khả dụng trọng số 0): A, B của `.10` và B của `.30` nay có trọng số lịch sử và tự tắt khi option khác phù hợp hơn khả dụng.
3. `add_mio_size` thiếu guard `has_dlc = "Arms Against Tyranny"` như mọi chỗ MD gọi: ba helper `VIE_ba_son_mio_size_N` đã bọc. Helper `VIE_gdt_mio_size_*` của Trục 2 lục quân còn thiếu guard (nợ cũ, ngoài phạm vi).
4. Hai đoạn loc (`vie_nav_ind.1.d`, `vie_nav_ind.12.d`) mô tả sai điều kiện/hệ quả: đã sửa.
