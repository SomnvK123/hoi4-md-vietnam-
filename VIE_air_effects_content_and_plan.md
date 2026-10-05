# EFFECT NHÁNH KHÔNG QUÂN — NỘI DUNG CHI TIẾT + PLAN CODE

> Mục tiêu: đưa effect của nhánh không quân (Trục 2 CNQP: 7 focus `VIE_apm_*`; Trục 3 lực lượng: 22 focus `VIE_airf_*`) lên mức chi tiết của lục quân (`VIE_lf_*`, 30 node) và hải quân (`VIE_nf_*`, 22 node + 6 node Trục 2, đã code ở commit `f07ac5d`).
> Nguồn đối chiếu: lục quân `VIE_md_effects_p17.txt`, `VIE_md_decisions_lf.txt`; hải quân `VIE_md_effects_nav_force.txt`, `VIE_md_effects_nav_ind.txt` (dòng 436–472), `VIE_md_decisions_nf_drills.txt`, `VIE_naval_effects_content_and_plan.md`; không quân `VIE_md_focus.txt` (dòng 11097–12097), `VIE_md_effects_air_force.txt`, `VIE_md_effects_air_ind.txt`, `VIE_md_air_force_decisions.txt`, `VIE_air_truc2/3_review_and_plan.md`, `VIE_air_force_content_report.md`.
> Ngày: 2026-10-05. **Chưa sửa dòng code mod nào.** Số liệu Phần 2–4 và 6 đã được kiểm bằng script `tools/audit/air_effects_v2_check.py` (file mới, chỉ là công cụ kiểm; bước 0 gộp nó vào `air_force_balance.py`).
> Trục 1 (mua sắm, sự kiện) và Trục 1B (chưa dựng) **ngoài phạm vi**, giống tài liệu hải quân.

---

# PHẦN 0 — HIỆN TRẠNG: KHÔNG QUÂN THIẾU GÌ SO VỚI LỤC QUÂN VÀ HẢI QUÂN

| Hạng mục | Lục quân | Hải quân (đã code) | Không quân (hiện tại) |
|---|---|---|---|
| Nơi đặt effect | `VIE_lf_<mã>_reward` ×30 | `VIE_nf_<mã>_reward` ×22, `VIE_nav_f<n>_reward` ×6 | Viết thẳng trong `completion_reward`, lặp 4 dòng (`ensure` + `dm_tt` + `add_to_variable` + `force_update`) cho **mỗi** modifier |
| XP | Hầu hết node | Mọi node | **5/22** node Trục 3 (T1, T5, A4, B5, C5); Trục 2 chỉ XP 10 và còn gọi thẳng `air_experience = 10`, bỏ qua nhánh `add_mastery` khi đã chọn học thuyết |
| Political power / command power | N1 +25, N2 +15 CP, `def_industry_law` +50 | T1 +25, capstone +50, 4 node CP | **0 node** |
| Cái giá ở node đầu hướng | FM1, FR1, FD1… | D1 range −2%, G1/B1 personnel cost | A1/B1/C1 chỉ có thưởng/phạt `branch_fit`, **không có khoản âm** |
| Hướng đã chọn đổi effect node sau | CR2, L1/L2, A1/A2… | T7 đọc `VIE_nf_force_priority` | Chỉ A1/B1/C1 đọc `VIE_airf_force_priority`; T6, B2 và các node giữa không đọc gì |
| Giảm cost theo hướng | `VIE_lf_fav_discount` | `VIE_nf_fav_discount` (trong `d4_finish`) | Không có |
| Tech bonus | — | 4 node (xem Phần 7, rủi ro R1) | Không có |
| Mốc lịch sử → giảm cost | 5 event | 3 event | 0 event cho Trục 2/3 |
| Decision huấn luyện lặp lại | 6 | 4 | **0** (5 Decision lực lượng đều `fire_only_once`) |
| Số chiều modifier mới | — | thêm 3 (`hit_chance`, `capital_ship_atk/def`) | thêm 3 chưa dùng (Phần 1.2) |
| Công cụ cân bằng | `lf_balance.py` | `nf_balance.py` (PASS) | `air_force_balance.py` **FAIL 28 dòng**, `air_ind_balance.py` **FAIL 16 dòng** (xem dưới) |

## Hai phát hiện ngoài phạm vi "thiếu effect"

1. **Hai script cân bằng không quân đang hỏng, không phải do con số sai.** Commit `f51d488` ("uodate", 2026-10-03) đã bung mọi lời gọi `VIE_airf_add_exp = { V = 0.04 }` thành khối inline; script vẫn tìm dạng cũ nên mục 4 và 5 của `air_force_balance.py` đọc ra `{}` (28 FAIL). `air_ind_balance.py` mục 5 không đọc được chi phí/thời gian trong event (16 FAIL; cần mở ra xem nguyên nhân chính xác ở bước 0). Hậu quả: bảng 4.2 của review Trục 3 hiện **không còn được máy kiểm** so với code. Bước 0 sửa việc này trước khi thêm số mới. Mười helper `VIE_airf_add_*` và bốn `VIE_apm_add_*` hiện có **0 nơi gọi** (chỉ còn định nghĩa), nên header ghi "ghi bằng `VIE_airf_add_<token>`" đang sai.
2. **Hải quân có thể đang dùng tên category tech không tồn tại.** `VIE_nf_d2/d3/g2/b2_reward` gọi `add_tech_bonus` với `CAT_as_missiles`, `CAT_sub`, `CAT_atk_sub`, `CAT_frigate`, `CAT_destroyer`. `VIE_repo_health_report.md` (dòng 218) đã ghi `CAT_as_missiles`, `CAT_frigate`… là token "cần tra" và không có trong `MD_all_CATS.json`; MD có `CAT_frigates`, `CAT_destroyers`, `CAT_submarines`, `CAT_attack_submarines`, `CAT_naval_anti_ship_missiles`. Nếu đúng thì 4 tech bonus hải quân không có tác dụng (engine bỏ qua im lặng). Tôi **không sửa** (ngoài phạm vi), nhưng nên xử lý riêng; kế hoạch không quân dưới đây chỉ dùng category đã thấy trong file tech của MD (Phần 3).

Ba chỗ nhỏ khác: (a) comment đầu khối Trục 3 trong `VIE_md_focus.txt:11101` ghi "T1 neo x+36", thực tế `x = 20`; (b) `VIE_airf_iads_command`, `VIE_airf_multirole_wing`, `VIE_airf_teaming`, `VIE_apm_mature` không có `cost` (mặc định 10), đúng ý capstone, chỉ cần ghi comment; (c) T6 và T8 hiện lặp `ensure` + `dm_tt` hai lần trong một reward.

---

# PHẦN 1 — NGUYÊN TẮC VÀ THANG ĐIỂM

## 1.1 Sáu nguyên tắc (giống hải quân, đã chỉnh cho không quân)

1. **Một node = một effect đặt tên**: `VIE_airf_<mã>_reward` (Trục 3: t1…t8, a1…a4, b1…b5, c1…c5) và `VIE_apm_f<n>_reward` (Trục 2: f1…f7). Focus chỉ còn `log` + `unlock_decision_tooltip` (nếu có) + gọi effect. `VIE_ap_ensure_af_modifier` gọi **một lần** ở đầu effect, `VIE_airf_dm_tt` và `force_update_dynamic_modifier` một lần ở cuối.
2. **Mỗi node có hơn một loại hiệu ứng**: modifier + XP, hoặc PP/command power, hoặc tech bonus.
3. **Node đầu hướng trả giá** (A1, B1, C1): một khoản âm đo bằng cùng thang điểm; điểm ròng ≈ 1,7–2,0.
4. **Hướng đã chọn đổi effect node sau**: T6 đọc `VIE_airf_force_priority` (đặt ngay lúc chọn ở `vie_air_force.30`); B2 đọc `VIE_airf_fighter_specialty`; D-D mở giảm cost 14 ngày cho node đầu nhánh khớp.
5. **Mốc lịch sử không khóa ngày**: chỉ giảm cost focus chưa làm, hoặc thưởng nhỏ nếu đã làm (mẫu `VIE_nf_ms*_apply`).
6. **Trục 3 không ghi `VIE_cap_*`/bậc của Trục 2** (R5) và **không đụng `air_defence_factor`** (đã 18/20 từ Trục 1, 2 và lục quân; A3 review Trục 3).

## 1.2 Ba chiều modifier mới

Cả ba **đã khai báo** trong `VIE_armed_forces_modifier` (khối `GEN:vars`, dòng 55–57) và **đã có tooltip** trong `VIE_md_vi_tt_l_english.yml` (dòng 31–33), 0 chỗ nào dùng trước nay; không cần sửa dynamic modifier hay loc tooltip. Dấu: `night`, `wx` là *penalty*, giá trị âm = tốt hơn, tooltip hiển thị `-=` (cùng quy ước `VIE_full_spectrum_idea`: `air_night_penalty = -0.2`).

| Chiều | Biến | Ý nghĩa dùng cho | Trần (đề xuất) |
|---|---|---|---:|
| `air_ace_generation_chance_factor` (ACE) | `VIE_af_air_ace_generation_chance_factor` | Đào tạo phi công, văn hóa huấn luyện (T1, T2, B5, A1, B1, C1, C5, mốc 2011) | 10 |
| `air_night_penalty` (NIGHT) | `VIE_af_air_night_penalty` | Bay đêm, EW, ISR (T4, A3, A4, B3, C1, C2, C5) | 6 |
| `air_weather_penalty` (WX) | `VIE_af_air_weather_penalty` | Mọi thời tiết, bảo đảm kỹ thuật (T7, A2, A3, B1, B3, C2, C3) | 6 |

Lý do chọn: chúng là chiều **chưa dùng** nên không đụng trần B/C đang chạm 16/16 (MIS) và 20/20 (RNG); chúng khớp nội dung lịch sử (Su-30MK2 bay đêm, T-6C/L-39NG đào tạo) và các trait chỉ huy sẵn có (`air_chief_all_weather_*`, `air_high_command_night_operations_*`). Trần là **đề xuất của tôi** theo thang các chiều khác (5–10%), chưa phải dữ kiện lịch sử.

Đổi một trần cũ: `pers` (chi phí duy trì không quân) từ +3 lên **+6** để ngang hải quân (+6); node mới chỉ dùng thêm +2 (B1) và −1 (B3), D-D cơ cấu 3 vẫn +3 (đỉnh B = +4).

Các trần cũ giữ nguyên: exp 10, atk 10, sup 10, cas 10, mis 16, rng 20, det 20, home 20, int 8.

---

# PHẦN 2 — TRỤC 3: NỘI DUNG EFFECT TỪNG FOCUS (22 NODE)

Ký hiệu: **(giữ)** = đã có trong code, không đổi; **(mới)** = thêm. Số trong ngoặc là % modifier. "Điểm" = tổng trọng số của modifier (chưa tính XP/PP/CP/tech bonus), trọng số trong `air_effects_v2_check.py`. Điểm cột "cũ → mới".

## 2.1 Chuỗi dùng chung (8 node)

| Mã | Focus | Modifier | Ngoài modifier | Điểm |
|---|---|---|---|---|
| T1 | `VIE_airf_training_standardization` | EXP +4 (giữ); ACE +3 (mới) | XP 15 (giữ); **+25 PP (mới)** | 2,0 → 4,4 |
| T2 | `VIE_airf_fighter_force` | ATK +1 (giữ); ACE +2 (mới) | **XP 10, tech bonus 0,25 `CAT_air_to_air_weapons` ×1 (mới)**; mở D-A (giữ) | 1,0 → 2,6 |
| T3 | `VIE_airf_sam_force` | HOME +2 (giữ) | **XP 10, tech bonus 0,25 `CAT_surface_to_air_missiles` ×1 (mới)**; mở D-B (giữ) | 1,6 |
| T4 | `VIE_airf_command_reform_1` | MIS +2 (giữ); NIGHT −1 (mới) | **+15 command power (mới)**; mở D-C (giữ) | 2,0 → 3,0 |
| T5 | `VIE_airf_first_force` | — | XP 10 (giữ); **+10 command power (mới)**; mở D-D (giữ) | 0 |
| T6 | `VIE_airf_command_reform_2` | MIS +2, DET +1 (giữ); **theo D-D (mới)**: cơ cấu 1 INT +1 · cơ cấu 2 INT +0,5, RNG +0,5, NIGHT −0,5 · cơ cấu 3 RNG +1 · chưa chọn: không thêm | **XP 10 (mới)** | 2,8 + 0,6–1,2 |
| T7 | `VIE_airf_medium_force` | RNG +3 (giữ); WX −1 (mới) | **XP 10 (mới)** | 1,8 → 2,6 |
| T8 | `VIE_airf_operating_range` | RNG +4, DET +1 (giữ) | **XP 15, +15 command power (mới)** | 3,2 |

T6 đọc `VIE_airf_force_priority` (đặt ngay ở `vie_air_force.30`, không đợi 12 tháng của D-D) nên đúng cả khi người chơi làm T6 trước khi D-D kết thúc; giá trị 0 = không thưởng, không phạt. Giá trị cơ cấu 3 chỉ +1 RNG (không +1,5 như hải quân) vì nhánh B đã chạm RNG 20/20.

**Giảm cost theo D-D** (`VIE_airf_fav_discount`, gọi cuối `VIE_airf_d4_finish`, mẫu `VIE_nf_fav_discount`): cơ cấu 1 (Phòng thủ lãnh thổ) → `VIE_airf_iads` −14 ngày; cơ cấu 3 (Tầm xa) → `VIE_airf_multirole` và `VIE_airf_unmanned` mỗi cái −14 ngày; cơ cấu 2 không giảm. Chỉ áp khi focus tương ứng chưa xong. Giữ nguyên thưởng MIS +1 khi đúng nhánh và timed idea phạt khi lệch nhánh như hiện tại.

## 2.2 Nhánh A — Phòng không tích hợp (lịch sử, 4 node, 19,9 điểm; cũ 12,4)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| A1 | `VIE_airf_iads` | HOME +2 (giữ); INT +0,5, ACE +1,5 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | RNG −2 (mới) | 2,0 |
| A2 | `VIE_airf_layered_defence` | DET +2, HOME +2 (giữ); WX −1, SUP +1,5 (mới) | **XP 10 (mới)** | — | 5,5 |
| A3 | `VIE_airf_ew_antistealth` | INT +3, DET +2 (giữ); NIGHT −1, WX −1, SUP +1 (mới) | **XP 10, tech bonus 0,25 `CAT_air_countermeasures` ×1 (mới)** | — | 6,8 |
| A4 | `VIE_airf_iads_command` (capstone) | MIS +2, HOME +2 (giữ); NIGHT −1, ATK +1 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,6 |

## 2.3 Nhánh B — Đa nhiệm (5 node, 21,6 điểm; cũ 16,8)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| B1 | `VIE_airf_multirole` | RNG +4 (giữ); WX −1, ACE +1 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | PERS +2 (mới) | 2,0 |
| B2 | `VIE_airf_multirole_fleet` | ATK +3, SUP +2, CAS +2 (giữ); **theo `VIE_airf_fighter_specialty` (mới)**: 1 Không chiến SUP +1 · 2 Tấn công đất/biển CAS +1 | **XP 10, tech bonus 0,25 `CAT_medium_aircraft` ×1 (mới)** | — | 6,6 (+0,8–1) |
| B3 | `VIE_airf_sustainment` | MIS +2 (giữ); WX −2, NIGHT −1, PERS −1 (mới; bảo đảm tốt hơn giảm duy trì) | **XP 10 (mới)** | — | 5,6 |
| B4 | `VIE_airf_airlift_tanker` | RNG +3 (giữ) | **XP 15, +10 command power (mới)** | — | 1,8 |
| B5 | `VIE_airf_multirole_wing` (capstone) | MIS +2, ATK +2 (giữ); ACE +2 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,6 |

## 2.4 Nhánh C — Không người lái và mạng hóa (5 node, 19,2 điểm; cũ 11,8)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| C1 | `VIE_airf_unmanned` | DET +1 (giữ); ACE +1,5, NIGHT −0,5 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | HOME −1 (mới) | 1,7 |
| C2 | `VIE_airf_isr_uav` | DET +3 (giữ); NIGHT −1,5, WX −1 (mới) | **XP 10, tech bonus 0,25 `CAT_air_drones` ×1 (mới)** | — | 4,7 |
| C3 | `VIE_airf_datalink` | MIS +2 (giữ); WX −1, SUP +1 (mới) | **XP 10, +10 command power (mới)** | — | 3,8 |
| C4 | `VIE_airf_strike_uav` | ATK +3 (giữ); RNG +1 (mới) | **XP 15 (mới)** | — | 3,6 |
| C5 | `VIE_airf_teaming` (capstone) | MIS +2, INT +2 (giữ); ACE +1, NIGHT −1 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,4 |

Tổng chuỗi chung 20,2 điểm (cũ 14,4). Tổng ba nhánh lệch nhau trong ±8% (A 19,9 · B 21,6 · C 19,2). B cao nhất vì đắt nhất và phụ thuộc 1B nhiều nhất; A là hướng lịch sử nên không bị phạt thêm; không cần cân lại nếu bạn chấp nhận Q2.

---

# PHẦN 3 — TECH BONUS (7 CHỖ, TÙY CHỌN)

Dùng `add_tech_bonus = { name = VIE_airf_tb_<…> bonus = 0.25 uses = 1 category = <CAT> }`; `name` duy nhất và cần loc. **Chỉ dùng category có thật trong file tech của MD** (`tools/audit/md_ref/tech_*.txt`), đã đối chiếu từng cái:

| Chỗ | `name` | Category | Có trong |
|---|---|---|---|
| T2 | `VIE_airf_tb_a2a` | `CAT_air_to_air_weapons` | `tech_BBA_aircraft.txt` |
| T3 | `VIE_airf_tb_sam` | `CAT_surface_to_air_missiles` | `tech_missile_defense.txt` |
| A3 | `VIE_airf_tb_ew` | `CAT_air_countermeasures` | `tech_BBA_aircraft.txt` |
| B2 | `VIE_airf_tb_multirole` | `CAT_medium_aircraft` | `tech_BBA_aircraft.txt`, `tech_fixed_wing.txt` |
| C2 | `VIE_airf_tb_uav` | `CAT_air_drones` | `tech_BBA_aircraft.txt`, `tech_fixed_wing.txt` |
| F4 (Trục 2) | `VIE_apm_tb_radar` | `CAT_airborne_early_warning` | `tech_BBA_aircraft.txt`, `tech_bombers.txt` (gần nhất với radar; MD không có category radar mặt đất riêng) |
| F5, F6 (Trục 2) | `VIE_apm_tb_avionics`, `VIE_apm_tb_drones` | `CAT_avionics`, `CAT_drones` | `tech_BBA_aircraft.txt` |

Tech bonus không tính điểm; bỏ cả Phần 3 không làm đổi bảng nào.

---

# PHẦN 4 — TRỤC 2 KHÔNG QUÂN: EFFECT 7 FOCUS

Trục 2 không có "kinh nghiệm công nghiệp" như hải quân (bậc nằm ở biến `VIE_apm_*_tier`, Decision lo), nên effect focus chỉ gồm PP/CP, XP chuẩn hóa và tech bonus, cộng một khoản `accidents` nhỏ. Bậc, MIO, chi phí giữ nguyên.

| Mã | Focus | Effect mới | Giữ nguyên |
|---|---|---|---|
| F1 | `VIE_apm_law` | **+25 PP** | category tooltip; XP 10 (đổi sang `VIE_airf_xp_10`) |
| F2 | `VIE_apm_a32` | **+15 PP**; `air_accidents_factor` −1 (tổng Trục 2 −8 → −9, trần đề xuất −10) | XP 10; mở `VIE_apm_d_a32` |
| F3 | `VIE_apm_a31` | **+10 PP** | XP 10; mở `VIE_apm_d_a31` |
| F4 | `VIE_apm_radar` | **+10 command power**; tech bonus `CAT_airborne_early_warning` | XP 10; mở `VIE_apm_d_radar` |
| F5 | `VIE_apm_integration` | **+10 command power**; tech bonus `CAT_avionics` | XP 10; mở `VIE_apm_d_integ` |
| F6 | `VIE_apm_uav` | tech bonus `CAT_drones` | XP 10; mở `VIE_apm_d_uav` |
| F7 | `VIE_apm_mature` (capstone) | **+50 PP**, `add_war_support` +3% | cờ `VIE_cap_mature_air_industry`; XP 10 |

Không thêm modifier DET/MIS/RNG vào Trục 2: DET đã 11 từ Trục 1+2, A/C đã 19,5/20. Tổng PP Trục 2 = 100; Trục 3 = 25 + 50 = 75 (một capstone). Hải quân: 100 và 75, lục quân cùng cỡ.

Bug nhỏ sửa kèm: F2–F7 hiện gọi `air_experience = 10` trực tiếp; khi đã chọn học thuyết lớn thì XP phải đi vào `add_mastery` (đúng như F1, mọi node Trục 3 và lục quân/hải quân). Dùng `VIE_airf_xp_10` cho cả bảy.

---

# PHẦN 5 — NĂM DECISION HUẤN LUYỆN KHÔNG QUÂN (LẶP LẠI ĐƯỢC)

Mẫu `VIE_dec_nf_train_*` (không `complete_effect`; thưởng ở `remove_effect` sau `days_remove`; `days_re_enable = 545`; category có sẵn `VIE_military_readiness_category`; `available = { has_war = no }`; `ai_will_do` base 15 với `factor 0` khi `VIE_def_ind_bankrupt = yes` hoặc `bankruptcy_incoming_collapse`). Timed idea là hiệu ứng tạm, **không tính vào trần** (cùng quy ước lục quân và hải quân).

| Decision | Hiện khi | PP | Chạy | Thưởng | Ghi chú |
|---|---|---:|---:|---|---|
| `VIE_dec_airf_train_aa` Huấn luyện không chiến | `VIE_airf_fighter_force` | 35 | 90 | +10 XP; SUP +3% 180 ngày | Chung |
| `VIE_dec_airf_train_night` Huấn luyện bay đêm, mọi thời tiết | `VIE_airf_command_reform_1` | 35 | 120 | +10 XP; NIGHT −3%, WX −2% 180 ngày | Chung; đúng nguồn báo Nghệ An về Su-30MK2 bay đêm |
| `VIE_dec_airf_train_sam` Diễn tập phòng không tích hợp | `VIE_airf_layered_defence` | 35 | 90 | +10 XP; HOME +4% 180 ngày | Chỉ nhánh A |
| `VIE_dec_airf_train_strike` Diễn tập đánh mặt đất, mặt biển | `VIE_airf_multirole_fleet` | 40 | 120 | +10 XP; CAS +3%, ATK +1,5% 180 ngày | Chỉ nhánh B |
| `VIE_dec_airf_train_uav` Diễn tập UAV và liên kết dữ liệu | `VIE_airf_datalink` | 35 | 90 | +10 XP; MIS +3% 180 ngày | Chỉ nhánh C |

Cần 5 idea tạm `VIE_airf_idea_aa_drill`, `_night_drill`, `_sam_drill`, `_strike_drill`, `_uav_drill` trong `VIE_md_ideas_air_force.txt` (khác 5 idea chỉ-báo `VIE_airf_prog_*` đang có). Icon: `GFX_decision_generic_form_nation` (đang dùng ở mọi Decision không quân); nếu muốn icon không quân riêng thì kiểm tên trong vanilla trước.

---

# PHẦN 6 — MỐC LỊCH SỬ (BA EVENT, TÙY CHỌN)

Mẫu `VIE_nf_ms*_apply` + `VIE_event_scheduler_nf`: không khóa ngày; focus mục tiêu **chưa xong** → giảm 24 ngày; **đã xong** → thưởng XP 10. Chung cho mọi người chơi kèm thưởng nhỏ. Namespace `vie_air_force`, id `.70 .71 .72` (đang trống; đã dùng `.1 .2 .10 .11 .30 .50 .51 .61–.65`).

| Event | Ngày kích hoạt | Mốc | Focus mục tiêu | Thưởng chung | Độ tin cậy |
|---|---|---|---|---|---|
| `.70` | `date > 2011.5.31` | Trung đoàn 923 bắt đầu thay Su-22 bằng Su-30MK2V; Su-27 chuyển sang Trung đoàn 940 | `VIE_airf_first_force` (T5) | ACE +1 | Năm 2011 đã xác minh trên web; **tháng 6 chỉ có trong báo cáo nội bộ mục 2.2** |
| `.71` | `date > 2016.2.29` | Hai Su-30MK2 cuối giao đầu tháng 2/2016, đủ 36 chiếc, hoàn tất 3 trung đoàn | `VIE_airf_medium_force` (T7) | +10 XP, +10 command power | Cao (armyrecognition, defence-blog) |
| `.72` | `date > 2022.12.7` | Triển lãm Quốc phòng quốc tế VN lần đầu, 8–10/12/2022, Gia Lâm; Không quân – Phòng không, Viettel trưng bày | `VIE_apm_radar` (F4) | +15 PP | Cao (VietnamPlus) |

Cả ba là pop-up dùng `VIE_popup_cd` (45 ngày) và fallback im lặng sau 6 tháng nếu cờ cooldown còn; catch-up sau nội chiến chỉ đặt cờ. Lưu ý Trục 1 cũng bắn pop-up quanh 2011–2016 (E5–E9 Su-30): cooldown chung giải quyết, mốc nào bị hoãn sẽ rơi vào fallback. Nếu chưa muốn thêm event, bỏ nguyên Phần 6; không phần nào khác phụ thuộc nó.

Ứng viên **không đưa vào** vì chưa đủ nguồn: ngày chính xác T-6C (nguồn lệch 2023/2024), ngày hợp đồng Yak-130, mọi tin 2025–2026 (F-16V, Rafale, Su-57) đang là [~].

---

# PHẦN 7 — KIỂM SỐ LIỆU VÀ RỦI RO

## 7.1 Kết quả script (`tools/audit/air_effects_v2_check.py`)

Duyệt 2 chuyên môn × 3 cơ cấu D-D × 2 mức × có/không D-B sớm = 24 tổ hợp mỗi nhánh (72 tổng); cộng Trục 3 mới, D-A…D-E, mốc `.70`, và DET Trục 1+2 (11). Trường hợp xấu nhất, tất cả PASS:

| Chiều | A (cũ → mới) | B | C | Trần |
|---|---|---|---|---:|
| exp | 4 | 4 | 4 | 10 |
| atk | 3,5 → 4,5 | 9,5 | 6,5 | 10 |
| sup | 6,5 → 9,0 | 8,5 → 9,5 | 6,5 → 7,5 | 10 |
| cas | 4,5 | 6,5 → 7,5 | 4,5 | 10 |
| mis | 13 | **16** | **16** | 16 |
| rng | 12 → 11 | 19 → **20** | 12 → 14 | 20 |
| det | 19,5 | 15,5 | 19,5 | 20 |
| home | 18,5 | 11,5 | 11,5 → 10,5 | 20 |
| int | 6 → 7,5 | 3 → 4 | 6 → 7 | 8 |
| pers | 3 | 3 → 4 | 3 | 6 (nâng từ 3) |
| **ace (mới)** | 7,5 | 9,0 | 8,5 | 10 |
| **night (mới)** | 3,5 | 2,5 | 4,5 | 6 |
| **wx (mới)** | 3,0 | 4,0 | 3,0 | 6 |

Ba chiều chạm trần đúng bằng (B: mis 16/16, rng 20/20; DET A/C 19,5/20) nên **mọi thay đổi sau này phải chạy lại script**; đừng nâng trần để chữa. Accidents Trục 2: −9 so với trần đề xuất −10 (chưa có trong script; thêm ở bước 0). EXP đỉnh với timed idea vẫn 10,00/10 như cũ (không thêm EXP).

## 7.2 Rủi ro

| # | Rủi ro | Giảm |
|---|---|---|
| R1 | Tên category tech sai bị engine bỏ qua im lặng (đang nghi với 4 tech bonus hải quân) | Phần 3 chỉ dùng category thấy trong file tech MD; bước 7 thêm kiểm tra `add_tech_bonus` ↔ `MD_all_CATS.json` + file tech; ghi mục riêng cho hải quân |
| R2 | `air_night_penalty`, `air_weather_penalty`, `air_ace_generation_chance_factor` không hiển thị/áp dụng khi là biến của dynamic modifier | Bước 0 kiểm bằng console `effect add_to_variable = { VIE_af_air_night_penalty = -0.01 }`; nếu lỗi, bỏ chiều đó và chuyển điểm sang chiều còn trần (A: sup, atk; C: rng) |
| R3 | Script cân bằng không bắt được sai lệch vì parse sai | Bước 0 viết lại parser theo dạng `add_to_variable = { VIE_af_<token> = <giá trị> … }` trong từng `VIE_airf_*_reward`; chạy trên code hiện tại phải ra 22/22 khớp bảng cũ trước khi thêm số mới |
| R4 | Đơn vị `reduce_focus_completion_cost` (ngày/tuần) | Dùng chung kết quả kiểm của lục quân/hải quân (TESTING.md), không test riêng |
| R5 | Pop-up mốc đụng pop-up Trục 1 | `VIE_popup_cd` + fallback 6 tháng, như hải quân |
| R6 | `.70` tháng 6/2011 chỉ có một nguồn | Giữ `date > 2011.5.31` (ngày chỉ làm nền cho cooldown, không khóa gì); sửa nếu có nguồn tháng khác |
| R7 | Sửa 29 `completion_reward` cùng lúc | Mỗi bước một commit; diff chỉ được đổi khối `completion_reward` (kiểm bằng `git diff` lọc dòng) |

---

# PHẦN 8 — PLAN CODE (9 BƯỚC, MỖI BƯỚC MỘT COMMIT, NHÁNH `air-effects-v2`)

Bước 0–3 đủ để người chơi thấy khác biệt; 4–6 tùy chọn thêm; 7–8 hoàn thiện.

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `tools/audit/air_force_balance.py` (gộp `air_effects_v2_check.py`, parser mới, trần mới, bảng 29 focus); `tools/audit/air_ind_balance.py` (sửa parser mục 5) | Đưa script về trạng thái PASS **trên code hiện tại** trước, rồi mới thêm số mới. Console thử 3 chiều mới (R2) | `air_force_balance.py` ALL PASS (22/22 focus + 5 Decision khớp); `air_ind_balance.py` ALL PASS |
| **1** | `common/scripted_effects/VIE_md_effects_air_force.txt` | `VIE_airf_refresh`; 22 effect `VIE_airf_<mã>_reward`; `VIE_airf_t6_dir` (đọc `force_priority`); `VIE_airf_b2_spec` (đọc `fighter_specialty`); `VIE_airf_fav_discount` | brace; `live.py` không báo effect thiếu |
| **2** | `common/national_focus/VIE_md_focus.txt` (22 focus Trục 3) | Thay `completion_reward` bằng `log` + `unlock_decision_tooltip` + `VIE_airf_<mã>_reward = yes`; giữ nguyên prerequisite, `available`, `ai_will_do`, tọa độ; sửa comment dòng 11101 | `audit.py` 0 dangling/cycle/trùng tọa độ; `git diff` không đổi dòng nào ngoài `completion_reward` |
| **3** | `VIE_md_effects_air_ind.txt` (+7 effect `VIE_apm_f<n>_reward`), `VIE_md_focus.txt` (7 focus Trục 2) | PP/CP, accidents, tech bonus, đổi `air_experience` → `VIE_airf_xp_10` | `air_ind_balance.py` PASS (không đổi tổng chi 3,10 tỷ) |
| **4** | `VIE_airf_d4_finish` | Gọi `VIE_airf_fav_discount`. Kiểm đơn vị giảm cost | chơi: chọn cơ cấu 1 → `VIE_airf_iads` rẻ hơn 14 ngày |
| **5** | `common/decisions/VIE_md_decisions_af_drills.txt` (mới), `VIE_md_ideas_air_force.txt` (+5 idea) | 5 Decision huấn luyện (Phần 5) | `live.py`: 0 decision/idea treo; chơi: cooldown 545, timed idea 180 ngày |
| **6** | `events/VIE_air_force.txt` (+`.70 .71 .72`), `VIE_md_effects_air_force.txt` (`VIE_airf_ms1..3_apply`, `VIE_event_scheduler_airf`), `VIE_md_on_actions.txt` (+1 dòng cạnh `VIE_event_scheduler_nf`), `VIE_md_effects_p3.txt` (catch-up) | Mốc lịch sử | `ev.py` sạch; `debug` đặt ngày 2011-06 thấy event; catch-up không bắn |
| **7** | `localisation/english/VIE_md_events_air_force_l_english.yml` (BOM, `:0`), loc cho 7 tech bonus, 5 Decision, 5 idea, 3 event; mô tả focus nếu đổi | Loc đầy đủ; thêm kiểm tra category tech vào `air_force_balance.py` | `verify_all_loc.py` sạch |
| **8** | `tools/TESTING.md` (mục "Air effects v2"), `VIE_v9_flag_mapping.md`, rà `ai_will_do` (capstone base 60 và guard phá sản giữ như hiện có), xóa 10 + 4 helper `VIE_airf_add_*`/`VIE_apm_add_*` không còn ai gọi (hoặc ghi chú "legacy") | Hoàn thiện | `ev.py`, `audit.py`, `live.py`, hai script cân bằng đều sạch |

Mẫu code bước 1 (theo `VIE_nf_t7_reward` và `VIE_lf_cr2_reward`):

```
VIE_airf_refresh = { force_update_dynamic_modifier = yes }

VIE_airf_t1_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_experience_gain_air_factor = 0.04 tooltip = VIE_tt_experience_gain_air_factor }
	add_to_variable = { VIE_af_air_ace_generation_chance_factor = 0.03 tooltip = VIE_tt_air_ace_generation_chance_factor }
	VIE_airf_xp_15 = yes
	add_political_power = 25
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}

VIE_airf_t6_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_air_mission_efficiency = 0.02 tooltip = VIE_tt_air_mission_efficiency }
	add_to_variable = { VIE_af_air_detection = 0.01 tooltip = VIE_tt_air_detection }
	if = { limit = { check_variable = { VIE_airf_force_priority = 1 } }
		add_to_variable = { VIE_af_air_intercept_efficiency = 0.01 tooltip = VIE_tt_air_intercept_efficiency } }
	else_if = { limit = { check_variable = { VIE_airf_force_priority = 3 } }
		add_to_variable = { VIE_af_air_range_factor = 0.01 tooltip = VIE_tt_air_range_factor } }
	else_if = { limit = { check_variable = { VIE_airf_force_priority = 2 } }
		add_to_variable = { VIE_af_air_intercept_efficiency = 0.005 tooltip = VIE_tt_air_intercept_efficiency }
		add_to_variable = { VIE_af_air_range_factor = 0.005 tooltip = VIE_tt_air_range_factor }
		add_to_variable = { VIE_af_air_night_penalty = -0.005 tooltip = VIE_tt_air_night_penalty } }
	VIE_airf_xp_10 = yes
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}

VIE_airf_b2_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_air_attack_factor = 0.03 tooltip = VIE_tt_air_attack_factor }
	add_to_variable = { VIE_af_air_superiority_efficiency = 0.02 tooltip = VIE_tt_air_superiority_efficiency }
	add_to_variable = { VIE_af_air_cas_efficiency = 0.02 tooltip = VIE_tt_air_cas_efficiency }
	if = { limit = { check_variable = { VIE_airf_fighter_specialty = 1 } }
		add_to_variable = { VIE_af_air_superiority_efficiency = 0.01 tooltip = VIE_tt_air_superiority_efficiency } }
	else_if = { limit = { check_variable = { VIE_airf_fighter_specialty = 2 } }
		add_to_variable = { VIE_af_air_cas_efficiency = 0.01 tooltip = VIE_tt_air_cas_efficiency } }
	VIE_airf_xp_10 = yes
	add_tech_bonus = { name = VIE_airf_tb_multirole bonus = 0.25 uses = 1 category = CAT_medium_aircraft }
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}
```

Khối lượng ước tính: 29 effect reward (~400 dòng), 29 focus sửa `completion_reward`, 5 Decision (~130 dòng), 5 idea, 3 event + scheduler (~150 dòng), ~100 khóa loc, 1 script cân bằng viết lại. Không đụng: 5 Decision lực lượng D-A…D-E và các effect `*_finish` (giá trị giữ nguyên; có thể rút gọn chúng sau bằng cùng kiểu, không nằm trong plan này).

---

# PHẦN 9 — CÂU HỎI CẦN CHỐT (mặc định đã gắn)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | Thêm 3 chiều mới ACE/NIGHT/WX thay vì nâng trần các chiều cũ? | **Có** (đã khai báo, đã có loc) | Nâng trần: lệch với thang lục quân/hải quân |
| Q2 | A 19,9 · B 21,6 · C 19,2 điểm có chấp nhận? | **Chấp nhận** | Muốn ngang: thêm 1–2 điểm vào B1/B4 ngược lại bớt B3, hoặc thêm vào A/C ở chiều còn chỗ (sup, atk, rng) |
| Q3 | Làm 3 event mốc (Phần 6)? | **Có**; `.70` cần tháng chính xác | Bỏ bước 6, không ảnh hưởng bước khác |
| Q4 | Tech bonus 7 chỗ (Phần 3)? | **Có** | Bỏ: bớt 7 dòng, điểm không đổi |
| Q5 | Trục 2 không quân cho PP/CP/tech bonus (Phần 4)? | **Có** | Bỏ: giữ XP + tooltip hiện tại |
| Q6 | Nâng trần `pers` từ +3 lên +6? | **Có** (cho B1 +2) | Giữ +3: bỏ khoản phạt PERS của B1, đổi sang RNG −1,5 |
| Q7 | Xóa 14 helper `VIE_airf_add_*` / `VIE_apm_add_*` không còn ai gọi? | **Xóa ở bước 8** | Giữ và ghi chú legacy |
| Q8 | Xử lý riêng lỗi category tech hải quân (R1)? | **Nên làm**, một task riêng sau bước 8 | Bỏ qua: 4 tech bonus hải quân có thể vô tác dụng |
