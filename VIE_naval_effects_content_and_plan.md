# EFFECT NHÁNH HẢI QUÂN — NỘI DUNG CHI TIẾT + PLAN CODE

> Mục tiêu: đưa effect của nhánh hải quân (Trục 2 CNQP: 6 focus; Trục 3 lực lượng: 22 focus) lên mức chi tiết của nhánh lục quân (`VIE_lf_*`, 30 focus).
> Nguồn đối chiếu: `common/scripted_effects/VIE_md_effects_p17.txt` (30 effect `VIE_lf_*_reward`), `Báo cáo Lục quân VIE — Trục 1, 2, 3.md` mục 8.11, 8.13, 8.14, `tools/audit/lf_balance.py`; phía hải quân: `common/national_focus/VIE_md_focus.txt` (dòng 2991–3910), `VIE_md_effects_nav_force.txt`, `VIE_md_effects_nav_ind.txt`, `VIE_naval_truc2/3_review_and_plan.md`, `tools/audit/nf_balance.py`.
> Ngày: 2026-10-05. **Chưa sửa dòng code nào.** Mọi con số ở Phần 2–5 đã được kiểm bằng script (Phần 6), không phải ước lượng.

---

# PHẦN 0 — HIỆN TRẠNG: HẢI QUÂN THIẾU GÌ SO VỚI LỤC QUÂN

| Hạng mục | Lục quân (đã code) | Hải quân (hiện tại) |
|---|---|---|
| Nơi đặt effect | Mỗi node một scripted effect `VIE_lf_<mã>_reward` (30 effect) | Viết thẳng trong `completion_reward` của focus, không có effect đặt tên |
| Số hiệu ứng mỗi node | 2–5 dòng: modifier, XP/PP/command power, cờ, mẫu sư đoàn, giảm cost | 1–2 dòng modifier + `VIE_nf_dm_tt`; Trục 2 chỉ có XP + tooltip |
| PP / command power | N1 +25 PP, N2 +15 CP, `VIE_def_industry_law` +50 PP… | **0 node** hải quân cấp PP hoặc CP |
| Cái giá ở node đầu hướng | FM1, FR1, FD1, PS, PT đều có 1–4 khoản âm | D1/G1/B1 không có khoản âm nào, chỉ có timed idea khi lệch nhánh |
| Hướng đã chọn đổi effect node sau | CR2, L1/L2, A1/A2, Y1/Y2, MOD, CAP đọc cờ hướng | Chỉ D1/G1/B1 đọc `VIE_nf_force_priority`; T7, các node giữa và capstone không đọc gì |
| Sở trường (cost −14 ngày, node cuối ×1,5) | `VIE_lf_fav_discount` | Không có |
| Mốc lịch sử → giảm cost focus | 5 event + `VIE_event_scheduler_p17` + catch-up sau nội chiến | 0 event mốc cho Trục 3 |
| Decision huấn luyện lặp lại | 6 decision (cooldown 545 ngày, timed idea) | 5 decision một lần; **decision "Huấn luyện chống ngầm" mà báo cáo lục quân 8.14 giao cho Hải quân chưa tồn tại** |
| Số chiều modifier | ~12 (org, phòng thủ, tấn công, tốc độ, dig-in, nhân lực, hậu cần, chi phí, XP, pháo…) | 8 chiều, trong đó 5 chiều đã ở ≥ 95% trần: coordination 19,5/20, detection 14,5/15, range 25/25, subatk 9,5/10, strike 9,5/10 |
| Công cụ cân bằng | `lf_balance.py`: điểm từng node, ròng từng hướng, trần | `nf_balance.py`: chỉ trần và tiền |

Hệ quả: nhánh hải quân hiện tại không còn chỗ trong trần để thêm modifier cũ. Hướng giải: thêm **chiều mới** (3 modifier) và effect **ngoài modifier** (PP, CP, XP, tech bonus, giảm cost), không nâng trần cũ.

Hai lỗi nhỏ tìm thấy khi đọc:
1. Dòng 2991 ghi header "TRUC 2 HAI QUAN (CNQP)" nhưng bên dưới là T1 của Trục 3 (`VIE_nf_training_standardization`) rồi mới đến 5 focus Trục 2. Chỉ cần sửa comment.
2. `VIE_naval_defence_2030` không có `cost` (dùng mặc định 10), trong khi 5 focus còn lại của Trục 2 là 5 hoặc 7. Đề xuất giữ (capstone) nhưng ghi comment cho rõ.

---

# PHẦN 1 — NGUYÊN TẮC VÀ THANG ĐIỂM

## 1.1 Sáu nguyên tắc (rút từ lục quân)

1. **Một node = một effect đặt tên** `VIE_nf_<mã>_reward` (Trục 3) hoặc `VIE_nav_f<n>_reward` (Trục 2); focus chỉ còn `log` + gọi effect.
2. **Mỗi node có hơn một loại hiệu ứng**: modifier + (XP hoặc PP hoặc CP) + (tech bonus hoặc giảm cost ở node chọn lọc).
3. **Node đầu hướng trả giá** (D1, G1, B1): khoản âm đo bằng cùng thang điểm; ròng mỗi node đầu ≈ 2,4–4,2 điểm.
4. **Hướng đã chọn đổi effect node sau**: T7 đọc `VIE_nf_force_priority` (như CR2 đọc hướng); D-D mở giảm cost 14 ngày cho node đầu nhánh khớp (như `VIE_lf_fav_discount`).
5. **Mốc lịch sử không khóa ngày** (`available` giữ nguyên `date >`): chỉ giảm cost focus chưa làm hoặc thưởng nhỏ nếu đã làm (mẫu `VIE_lf_ms*_apply`).
6. **Trục 3 chỉ cấp modifier vận hành** (Quy tắc 10) và **không ghi `VIE_cap_*`/tier của Trục 2** (Quy tắc 11). Trục 2 chỉ ghi biến exp của chính nó.

## 1.2 Ba modifier mới và thang điểm

Ba modifier bổ sung vào `VIE_armed_forces_modifier` (token đã có trong repo/MD, loc tooltip đã có sẵn trừ `naval_hit_chance`):

| Modifier | Biến `VIE_af_*` | Token có thật ở | Loc `VIE_tt_*` |
|---|---|---|---|
| `naval_hit_chance` | `VIE_af_naval_hit_chance` | `common/ideas/VIE_md_ideas_p2.txt:1188`, `tools/audit/md_ref/tech_custom_tech.txt:490` | **thiếu**, thêm |
| `navy_capital_ship_attack_factor` | `VIE_af_navy_capital_ship_attack_factor` | `common/ideas/VIE_md_ideas_p3B.txt:10` | có (`VIE_md_vi_tt_l_english.yml:20`) |
| `navy_capital_ship_defence_factor` | `VIE_af_navy_capital_ship_defence_factor` | `common/ideas/VIE_md_ideas_p3B.txt:11` | có (`:21`) |

Hai modifier đã khai báo trong dynamic modifier nhưng Trục 3 chưa dùng: `naval_speed_factor`, `naval_strike_targetting_factor` (chỉ dùng `naval_speed_factor`).

Trọng số điểm (1 điểm = +1% tổ chức): org 1,0 · coordination 1,0 · strike 1,0 · subatk 1,0 · subdef 1,0 · detection 0,8 · AA 0,8 · capital atk/def 0,8 · range 0,6 · speed 0,7 · hit chance 1,2 · mines_plant 0,2 · mines_reduction 0,5 · invasion_plan 0,3 · invasion_cap 3,0/đơn vị · XP 0,5 · chi phí nhân sự −1,0 mỗi +1%.

Trần toàn đường (v2): các trần cũ giữ nguyên (org 18, coord 20, detect 15, range 25, subatk 10, subdef 10, strike 10, exp 10); trần mới: hit 10, speed 10, capital atk 8, capital def 8, AA 12, chi phí nhân sự ròng +6.

---

# PHẦN 2 — TRỤC 3: NỘI DUNG EFFECT TỪNG FOCUS (22 NODE)

Ký hiệu: **(giữ)** = đã có trong code, không đổi; **(mới)** = thêm. Số trong ngoặc là điểm theo 1.2. Mọi modifier đi qua `add_to_variable = { VIE_af_* … tooltip = VIE_tt_* }` rồi `VIE_nf_refresh = yes`.

## 2.1 Chuỗi dùng chung (8 node)

| Mã | Focus | Modifier | Ngoài modifier | Điểm |
|---|---|---|---|---|
| T1 | `VIE_nf_training_standardization` | `experience_gain_navy` +5% (giữ); `naval_hit_chance` +1% (mới) | XP 15 (giữ); **+25 PP (mới)**; tooltip mở category (giữ) | 3,7 |
| T3 | `VIE_nf_surface_force` | `navy_org` +2% (giữ); `naval_hit_chance` +1% (mới) | **XP 10 (mới)**; mở D-A (giữ) | 3,2 |
| T4 | `VIE_nf_submarine_force` | `navy_submarine_attack` +2% (giữ); `navy_submarine_defence` +1% (mới) | **XP 10 (mới)**; mở D-B (giữ) | 3,0 |
| T5 | `VIE_nf_command_reform_1` | `navy_org` +2%, `naval_coordination` +3% (giữ) | **+15 command power (mới)**; mở D-C (giữ) | 5,0 |
| T6 | `VIE_nf_first_force` | — | XP 10 (giữ); **+10 command power (mới)**; mở D-D (giữ) | 0 |
| T7 | `VIE_nf_command_reform_2` | `navy_org` +2%, `naval_coordination` +3% (giữ); **theo hướng D-D (mới)**: Coastal `naval_hit_chance` +1,5% · Balanced `navy_org` +0,5% và hit +0,5% và speed +0,5% · Extended `naval_speed` +1,5% · chưa chọn: không thêm | **XP 10 (mới)** | 5,0 + 1,1–1,8 |
| T8 | `VIE_nf_medium_force` | `navy_max_range` +3% (giữ); `naval_speed` +1% (mới) | **XP 10 (mới)**; mở P1/P2/P3 (giữ tooltip) | 2,5 |
| T9 | `VIE_nf_operating_range` | `navy_max_range` +5%, `naval_detection` +5% (giữ) | **XP 15, +15 command power (mới)** | 7,0 |

T7 đọc `VIE_nf_force_priority` (đặt ngay lúc chọn ở `vie_nav_force.30`, không đợi 12 tháng của D-D) nên hoạt động đúng cả khi người chơi bấm D-D xong mới làm T7. Giá trị "chưa chọn" = 0 → không thưởng, không phạt.

**Giảm cost theo hướng D-D** (áp trong `VIE_nf_d4_finish`, mẫu `VIE_lf_fav_discount`): Coastal → `VIE_nf_denial` −14 ngày; Extended Range → `VIE_nf_greenwater` và `VIE_nf_bluewater` mỗi cái −14 ngày; Balanced → không giảm. Chỉ áp khi focus tương ứng chưa hoàn thành. Giữ thưởng +1% org khi đúng nhánh (L8) và phạt timed idea khi lệch nhánh (L6) như code hiện tại.

## 2.2 Nhánh Maritime Denial (lịch sử, 4 node, tổng 22,9 điểm)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| D1 | `VIE_nf_denial` | `naval_strike_attack` +3% (giữ); `naval_hit_chance` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_max_range` −2% (mới) | 4,2 |
| D2 | `VIE_nf_denial_defence` | `mines_planting_by_fleets` +10%, `naval_mines_effect_reduction` +5% (giữ); `naval_hit_chance` +1% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_as_missiles` ×1 lượt (mới)**; mở Bastion-P2 (giữ) | — | 5,7 |
| D3 | `VIE_nf_denial_subs` | `navy_submarine_attack` +3% (giữ); `navy_submarine_defence` +2% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_sub`+`CAT_atk_sub` (mới)**; mở P4 (giữ) | — | 5,0 |
| D4 | `VIE_nf_denial_command` (capstone) | `navy_org` +3%, `naval_detection` +4% (giữ); `naval_hit_chance` +1,5% (mới, thay cho strike +2% vì strike đã sát trần) | **XP 25, +50 PP (mới)** | — | 8,0 |

## 2.3 Nhánh Greenwater (5 node, tổng 27,0 điểm)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| G1 | `VIE_nf_greenwater` | `navy_max_range` +5% (giữ); `naval_speed` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_personnel_cost` +2% (mới) | 2,4 |
| G2 | `VIE_nf_regional_frigates` | `navy_max_range` +3%, `navy_org` +2% (giữ); `navy_anti_air_attack` +2% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_frigate` (mới)**; mở P4 (giữ) | — | 5,4 |
| G3 | `VIE_nf_amphibious_fleet` | `naval_invasion_planning_bonus_speed` +10%, `naval_invasion_capacity` +1 (giữ); `naval_speed` +1% (mới) | **+10 command power (mới)** | — | 6,7 |
| G4 | `VIE_nf_lhd_program` | `naval_invasion_capacity` +1 (giữ); `navy_anti_air_attack` +2% (mới) | XP 15 (mới); mở P7 (giữ) | — | 4,6 |
| G5 | `VIE_nf_regional_command` (capstone) | `navy_org` +3%, `naval_coordination` +3% (giữ); `naval_hit_chance` +1%, `naval_speed` +1% (mới) | **XP 25, +50 PP (mới)** | — | 7,9 |

## 2.4 Nhánh Bluewater (5 node, tổng 30,8 điểm; B5 cho thêm khi có tàu sân bay)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---|
| B1 | `VIE_nf_bluewater` | `navy_max_range` +5% (giữ); `naval_speed` +2%, `navy_capital_ship_defence` +2% (mới) | XP 15 (mới); khớp/lệch nhánh (giữ) | `navy_personnel_cost` +3% (mới) | 3,0 |
| B2 | `VIE_nf_ocean_escort` | `navy_anti_air_attack` +5% (giữ); `navy_submarine_defence` +1% (mới) | XP 10 (mới); **tech bonus 0,25 `CAT_destroyer` (mới)**; mở khu trục (giữ) | — | 5,0 |
| B3 | `VIE_nf_replenishment` | `navy_max_range` +3% (giữ); `navy_org` +2% (mới); `navy_personnel_cost` −1% (mới, hậu cần tốt hơn giảm duy trì) | XP 10 (mới) | — | 4,8 |
| B4 | `VIE_nf_naval_aviation` | `navy_anti_air_attack` +3%, `naval_detection` +4% (giữ); `naval_hit_chance` +1% (mới) | XP 15 (mới); mở tàu sân bay (giữ) | — | 6,8 |
| B5 | `VIE_nf_carrier_group` (capstone) | `navy_org` +3%, `naval_coordination` +5% (giữ); `navy_capital_ship_attack` +2%, `navy_capital_ship_defence` +2% (mới) | **XP 25, +50 PP (mới)**; mở SSN (giữ). D-E `VIE_nf_d5_finish` vẫn cộng thêm 0,25–0,5× org/coord (giữ) | — | 11,2 |

Vì sao tổng ba hướng lệch (22,9 / 27,0 / 30,8): Denial có 4 node và mua sắm rẻ nhất (8,85 tỷ), Greenwater 5 node (9,6 tỷ), Bluewater 5 node và đắt nhất (15,0 tỷ, từ `nf_balance.py` mục 4). Điểm bình quân mỗi focus 5,7 / 5,4 / 6,2 và Denial là hướng lịch sử nên không bị phạt thêm. Nếu muốn ngang nhau hơn, nâng D2 hoặc D3 thêm 1 điểm (xem Q2).

---

# PHẦN 3 — TRỤC 2 HẢI QUÂN: NỘI DUNG EFFECT TỪNG FOCUS (6 NODE)

Quy ước (giống `VIE_def_industry_law`): focus cho PP, XP và một khoản kinh nghiệm công nghiệp nhỏ; việc lớn (dockyard, MIO, tier, tech bonus lớn) vẫn thuộc Decision D1–D5. Exp cộng bằng `VIE_nav_add_*_exp` (đã có kẹp 0–100, riêng MRO kẹp 50 nếu phụ thuộc Nga). Cộng 3 điểm exp ở mỗi focus không làm đổi kết luận A3 của review Trục 2 (ngưỡng 30/15 đạt 80%); sẽ chạy lại `naval_balance.py`.

| Mã | Focus | Effect mới | Giữ nguyên |
|---|---|---|---|
| F1 | `VIE_naval_defence_law` (cost 5) | **+25 PP**; idea `VIE_nav_law_idea`: `industrial_capacity_dockyard` +3%, `experience_gain_navy` +1% | XP 15; tooltip category |
| F2 | `VIE_ba_son_shipyards` (cost 5) | **+15 PP**; `shipbuilding_exp` +3 | XP 10; unlock D1; event `vie_nav_ind.1` |
| F3 | `VIE_naval_mro` (cost 7) | **+10 PP**; `mro_exp` +3 | XP 10; unlock D2 |
| F4 | `VIE_small_combatant_construction` (cost 7) | `shipbuilding_exp` +3; `naval_speed` +2% (tàu tấn công nhanh) | XP 10; unlock D3 |
| F5 | `VIE_naval_systems_integration` (cost 7) | `integration_exp` +3; `naval_hit_chance` +1% (hệ thống điều khiển hỏa lực) | XP 15; unlock D4 |
| F6 | `VIE_naval_defence_2030` (capstone, cost mặc định 10) | **+50 PP**, `add_war_support` +3% | XP 25; unlock D5 |

Idea mới cho F1 nằm trong `common/ideas/VIE_md_ideas_nav_ind.txt` (cùng mẫu `VIE_nav_mature_industry_idea`). `industrial_capacity_dockyard` đã dùng ở 13 chỗ trong repo/MD nên token chắc chắn tồn tại.

---

# PHẦN 4 — DECISION HUẤN LUYỆN HẢI QUÂN (BỐN CÁI, LẶP LẠI ĐƯỢC)

Mẫu giống `VIE_dec_lf_*` (`VIE_md_decisions_lf.txt`): không `complete_effect`, thưởng ở `remove_effect` sau `days_remove`, `days_re_enable` làm cooldown, đặt trong category có sẵn `VIE_military_readiness_category`, `ai_will_do` base 15 với `factor 0` khi `VIE_def_ind_bankrupt = yes`. Timed idea là hiệu ứng tạm nên **không tính vào trần** (giống lục quân; tạm thời có thể vượt trần).

| Decision | Hiện khi | PP | Chạy | Cooldown | Thưởng | Ghi chú |
|---|---|---:|---:|---:|---|---|
| `VIE_dec_nf_train_asw` Huấn luyện chống ngầm | `has_completed_focus = VIE_nf_surface_force` và (`VIE_kilo_qty_delivered > 0` hoặc `VIE_nf_d2_done`) | 35 | 120 | 545 | +10 XP hải quân; `naval_detection` +5% trong 180 ngày | Đúng dòng 8.14 báo cáo lục quân, giao cho Hải quân |
| `VIE_dec_nf_train_firing` Diễn tập bắn đạn thật trên biển | `VIE_nf_surface_force` | 35 | 90 | 545 | +10 XP; `naval_hit_chance` +3% trong 180 ngày | Dùng modifier mới |
| `VIE_dec_nf_train_mines` Diễn tập thủy lôi và phòng thủ bờ | `VIE_nf_denial_defence` | 35 | 90 | 545 | +10 XP; `mines_planting_by_fleets` +10% trong 180 ngày | Chỉ nhánh Denial |
| `VIE_dec_nf_train_replenish` Diễn tập tiếp tế và hộ tống viễn dương | `VIE_nf_replenishment` | 40 | 120 | 545 | +10 XP; `navy_max_range` +5% trong 180 ngày | Chỉ nhánh Bluewater |

Cần 4 idea tạm `VIE_nf_idea_asw_drill`, `_firing_drill`, `_mines_drill`, `_replenish_drill` trong `VIE_md_ideas_nav_force.txt`.

---

# PHẦN 5 — MỐC LỊCH SỬ (BA EVENT, TÙY CHỌN)

Mẫu `VIE_lf_ms*_apply` + scheduler (không dùng `trigger_year_*` của MD). Không khóa ngày: nếu focus mục tiêu **chưa xong** → giảm cost 24 ngày; **đã xong** → thưởng nhỏ. Mỗi event còn cộng một modifier nhỏ cho mọi người chơi.

| Event | Ngày | Mốc | Focus mục tiêu | Cho mọi người chơi | Độ tin cậy ngày |
|---|---|---|---|---|---|
| `vie_nav_force.70` | 2016-03 | Khai trương Cảng quốc tế Cam Ranh | `VIE_nf_operating_range` (T9) | `navy_org` +1% | Cao (8/3/2016, đã xác minh) |
| `vie_nav_force.71` | 2018-03 | Tàu sân bay Hoa Kỳ thăm Đà Nẵng (5–9/3/2018) | không (chỉ thưởng) | +10 XP, +10 command power | Cao |
| `vie_nav_force.72` | 2023-07 | Ấn Độ trao tặng một hộ vệ hạm tên lửa cho Hải quân | `VIE_nf_ocean_escort` (B2) | `naval_hit_chance` +1% | Cao (INS Kirpan, 22/7/2023, đã xác minh) |

Event .70 và .72 là pop-up; .71 ẩn để không tăng số pop-up năm 2018 (cùng cách `vie_lf.4`). Dùng `VIE_popup_cd` giống lục quân, fallback im lặng sau 6 tháng, catch-up sau nội chiến chỉ đặt cờ. Nếu bạn chưa muốn thêm event, bỏ nguyên Phần 5; các phần còn lại không phụ thuộc nó.

Ứng viên chưa đủ nguồn nên **không đưa vào**: thành lập Lữ đoàn Tàu ngầm 189 (báo cáo hải quân ghi 2013, bản gốc 2011, đã nằm trong danh sách cần xác minh ở review Trục 3, mục 5.1).

---

# PHẦN 6 — KIỂM SỐ LIỆU

Script scratch `nf_v2_check.py` (sẽ thành `tools/audit/nf_balance.py` mục 1 ở bước 0) duyệt 144 tổ hợp đường (3 nhánh × 2 mức D-A/D-B × chuyên môn × định hướng sâu × cơ cấu D-D × có hay không Luật Biển), cộng cả Trục 2, mốc Phần 5 và idea hiện có (`VIE_coast_guard_idea`, `VIE_cam_ranh_idea`: exp +5%). Trường hợp xấu nhất:

| Modifier | Xấu nhất | Trần | | Modifier | Xấu nhất | Trần |
|---|---:|---:|---|---|---:|---:|
| org | 18,0 | 18 | | strike | 9,5 | 10 |
| coordination | 19,5 | 20 | | subatk | 9,5 | 10 |
| detection | 14,5 | 15 | | subdef | 9,5 | 10 |
| range | 25,0 | 25 | | **hit chance (mới)** | 10,0 | 10 |
| experience gain | 10,0 | 10 | | **speed (mới)** | 8,5 | 10 |
| AA | 8,0 | 12 | | capital atk / def (mới) | 3,0 / 5,0 | 8 / 8 |
| chi phí nhân sự | +5,0 | +6 | | | | |

Tất cả PASS. Hai chiều chạm trần đúng bằng (org 18,0 và hit 10,0) nên **mọi thay đổi sau này đều phải chạy lại script**; không thêm modifier cùng chiều vào mốc hoặc decision mà không giảm chỗ khác. Phần thưởng PP: tổng Trục 3 chỉ +25 (T1) +50 (capstone nhánh đã chọn) = +75 và Trục 2 +25 +15 +10 +50 = +100; so với lục quân (+25 N1, +50 `VIE_def_industry_law`, các focus Trục 2 khác) là cùng cỡ.

---

# PHẦN 7 — PLAN CODE (9 BƯỚC, MỖI BƯỚC MỘT COMMIT, NHÁNH `naval-effects-v2`)

Bước 0–3 đủ để người chơi thấy khác biệt; bước 4–6 là phần tùy chọn thêm; bước 7–8 hoàn thiện.

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+3 dòng, ngoài khối `GEN:vars`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+`VIE_tt_naval_hit_chance`); `tools/audit/nf_balance.py` (thay hằng số bằng bảng ở Phần 2–5, thêm chiều mới) | Thêm 3 biến `VIE_af_*` và loc; cập nhật script cân bằng | `nf_balance.py` PASS; console `effect add_to_variable = { VIE_af_naval_hit_chance = 0.01 }` thấy dòng trong tooltip `VIE_armed_forces_modifier` |
| **1** | `common/scripted_effects/VIE_md_effects_nav_force.txt` | `VIE_nf_refresh`, 22 effect `VIE_nf_<mã>_reward` (T1…T9, D1…D4, G1…G5, B1…B5), `VIE_nf_fav_discount`, `VIE_nf_t7_dir` | brace; `live.py` không báo effect thiếu |
| **2** | `common/national_focus/VIE_md_focus.txt` | 22 focus Trục 3: thay `completion_reward` bằng `log` + `VIE_nf_<mã>_reward = yes`; giữ nguyên prerequisite, `available`, `ai_will_do`, tọa độ; sửa comment header dòng 2991 | `audit.py` 0 dangling/cycle/trùng tọa độ; so diff: không đổi dòng nào ngoài `completion_reward` |
| **3** | `VIE_md_effects_nav_ind.txt`, `VIE_md_ideas_nav_ind.txt`, `VIE_md_focus.txt` (6 focus Trục 2) | 6 effect `VIE_nav_f<n>_reward`, idea `VIE_nav_law_idea`; focus gọi effect | `naval_balance.py` PASS (ngưỡng exp 30/15 vẫn ≥ 75% tổ hợp đạt) |
| **4** | `VIE_nf_d4_finish` (nav_force effects), `VIE_md_ideas_nav_force.txt` | Gọi `VIE_nf_fav_discount` ở cuối D-D; kiểm đơn vị `reduce_focus_completion_cost` (ngày) cùng mục checklist lục quân | chơi: chọn Coastal ở D-D thì `VIE_nf_denial` rẻ hơn 14 ngày so với `VIE_nf_greenwater` |
| **5** | `common/decisions/VIE_md_decisions_nf_drills.txt`, `VIE_md_ideas_nav_force.txt` (+4 idea tạm) | 4 decision huấn luyện (Phần 4) | `live.py`: 0 decision/idea treo; chơi: cooldown 545 ngày, timed idea 180 ngày hiện đúng |
| **6** | `events/VIE_nav_force.txt` (+`.70 .71 .72`), `VIE_md_effects_nav_force.txt` (`VIE_nf_ms1..3_apply`, `VIE_event_scheduler_nf`), `common/on_actions/VIE_md_on_actions.txt` (+1 dòng), `VIE_md_effects_p3.txt` (catch-up) | Mốc lịch sử; dùng `VIE_popup_cd` và fallback 6 tháng | `ev.py` sạch; `debug` đặt ngày 2016-03 thấy event; catch-up không bắn event |
| **7** | `localisation/english/VIE_md_events_nav_force_l_english.yml` (BOM, `:0`), `VIE_md_events_naval_l_english.yml` nếu cần | Loc: 4 decision, 4+1 idea, 3 event (title/desc/option), tech bonus name (`VIE_nf_tb_*`), cập nhật mô tả focus ngắn gọn khi effect đổi | `verify_all_loc.py` sạch |
| **8** | `ai_will_do`, `tools/TESTING.md`, `VIE_v9_flag_mapping.md` | Rà `ai_will_do`: capstone base 60 và guard phá sản như hiện có, thêm vào TESTING mục "Naval effects v2" | `ev.py`, `audit.py`, `live.py`, `nf_balance.py`, `naval_balance.py` đều sạch |

Mẫu code cho bước 1 (theo `VIE_lf_fm1_reward` và `VIE_lf_cr2_reward`):

```
VIE_nf_refresh = { force_update_dynamic_modifier = yes }

VIE_nf_d1_reward = {
	add_to_variable = { VIE_af_naval_strike_attack_factor = 0.03 tooltip = VIE_tt_naval_strike_attack_factor }
	add_to_variable = { VIE_af_naval_hit_chance = 0.02 tooltip = VIE_tt_naval_hit_chance }
	add_to_variable = { VIE_af_navy_max_range_factor = -0.02 tooltip = VIE_tt_navy_max_range_factor }
	VIE_nf_xp_15 = yes
	# khop/lech nhanh: giu nguyen khoi if/else_if theo VIE_nf_force_priority hien co
	VIE_nf_refresh = yes
}

VIE_nf_t7_reward = {
	add_to_variable = { VIE_af_navy_org_factor = 0.02 tooltip = VIE_tt_navy_org_factor }
	add_to_variable = { VIE_af_naval_coordination = 0.03 tooltip = VIE_tt_naval_coordination }
	if = { limit = { check_variable = { VIE_nf_force_priority = 1 } }
		add_to_variable = { VIE_af_naval_hit_chance = 0.015 tooltip = VIE_tt_naval_hit_chance } }
	else_if = { limit = { check_variable = { VIE_nf_force_priority = 3 } }
		add_to_variable = { VIE_af_naval_speed_factor = 0.015 tooltip = VIE_tt_naval_speed_factor } }
	else_if = { limit = { check_variable = { VIE_nf_force_priority = 2 } }
		add_to_variable = { VIE_af_navy_org_factor = 0.005 tooltip = VIE_tt_navy_org_factor }
		add_to_variable = { VIE_af_naval_hit_chance = 0.005 tooltip = VIE_tt_naval_hit_chance }
		add_to_variable = { VIE_af_naval_speed_factor = 0.005 tooltip = VIE_tt_naval_speed_factor } }
	VIE_nf_xp_10 = yes
	VIE_nf_refresh = yes
}
```

Khối lượng ước tính: 28 effect (~330 dòng), 28 focus sửa `completion_reward` (không đổi cấu trúc), 4 decision (~100 dòng), 5 idea, 3 event + scheduler (~150 dòng), ~110 khóa loc, 1 script kiểm tra.

## Rủi ro và cách giảm

| Rủi ro | Giảm |
|---|---|
| `naval_hit_chance` hoặc `navy_capital_ship_*` bị engine từ chối khi là biến của dynamic modifier | Bước 0 kiểm bằng console ngay; nếu lỗi, đổi chiều này sang `naval_strike_attack` giảm bớt chỗ khác hoặc dùng idea tĩnh |
| `force_update_dynamic_modifier` cần hay không (comment p17 tự ghi "bỏ nếu tooltip tự cập nhật") | Test cùng lúc ở bước 0; chốt một hướng cho cả lục quân lẫn hải quân |
| Đơn vị `reduce_focus_completion_cost` (ngày hay tuần) | Đã có mục kiểm trong `tools/TESTING.md` cho lục quân; dùng chung kết quả, đừng test riêng |
| Tech bonus trùng `name` hoặc categories không tồn tại | Dùng đúng categories Trục 2 đã dùng (`CAT_sub`, `CAT_atk_sub`, `CAT_frigate`, `CAT_destroyer`, `CAT_as_missiles`); tên `VIE_nf_tb_*` duy nhất |
| Hai chiều chạm trần đúng bằng | `nf_balance.py` fail cứng khi vượt; đừng nâng trần để chữa |

---

# PHẦN 8 — CÂU HỎI CẦN CHỐT (mặc định đã gắn)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | Giữ trần cũ, thêm 3 chiều mới thay vì nâng trần? | **Giữ trần, thêm chiều** | Nâng trần thì lệch với thang lục quân (25–26% mỗi chiều) |
| Q2 | Denial (22,9 điểm) thấp hơn Greenwater (27,0) và Bluewater (30,8)? | **Chấp nhận** vì rẻ nhất và là hướng lịch sử | Muốn ngang: D2 thêm `naval_hit_chance` +1% (hit đang 10,0/10 nên phải bớt ở nơi khác) |
| Q3 | Có làm Phần 5 (3 event mốc)? | **Có**, nhưng .70 và .72 cần xác minh ngày | Bỏ: bỏ bước 6, không ảnh hưởng bước khác |
| Q4 | Tech bonus ở D2, D3, G2, B2 (0,25 ×1 lượt)? | **Có** | Bỏ: bớt 4 dòng, điểm không đổi vì tech bonus không tính điểm |
| Q5 | Trục 2 hải quân cho PP và exp ở focus? | **Có** (Phần 3) | Bỏ: giữ XP + tooltip hiện tại |
| Q6 | Tướng/đô đốc hải quân? | **Ngoài phạm vi**; lục quân và không quân đã có roster (`common/characters/`), hải quân chưa có file nào | Làm riêng một task "roster đô đốc" sau bước 8 |
