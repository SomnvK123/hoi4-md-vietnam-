# REVIEW TRỤC 2 KHÔNG QUÂN (CÔNG NGHIỆP QUỐC PHÒNG) + PLAN CODE

> Đầu vào: `VIE_air_force_content_report.md` bản 1.3, Phần 6 (Trục 2) và các chỗ Trục 2 chạm tới (4.2, 4.3, 6.5, 7, 8.2, 11, 12.2 mục 10, 13 Q16).
> Đối chiếu với: repo @ `e4f3215` + đợt Trục 1 không quân đã code (chưa commit); MD v2.0.0 trên máy; code Trục 2 hải quân (`VIE_md_nav_ind_decisions.txt`, `VIE_md_effects_nav_ind.txt`, `VIE_naval_truc2_review_and_plan.md`) và lục quân (`VIE_md_def_industry.txt`); Code Style Guide của MD (GitHub `docs/.../code-stylization-guide.md`) và `code-resource.md`.
>
> **KẾT LUẬN: cấu trúc ý tưởng (5 trụ × 3 bậc, bậc là biến, Decision là nút khởi động, Trục 3 và 1B chỉ đọc) ĐÚNG và giữ nguyên.
> Nhưng bản 1.3 chưa code được: 4 lỗi chặn (Phần 1), 7 chỗ lệch game/mod (Phần 2).**
> Báo cáo đã được sửa (bản 1.4, Phần 6 viết lại). Phần 3 là thiết kế chốt, Phần 4 plan code 9 bước, Phần 6 các quyết định cần bạn chốt.

---

# PHẦN 1 — 4 LỖI CHẶN

## A1 · Báo cáo nói "Việt Nam chưa có MIO", nhưng repo đã có 4 MIO và Trục 2 khác đã nuôi chúng

6.5 và 12.2 mục 10 của bản 1.3: MD chưa có MIO cho Việt Nam, nên MIO "làm sau", chỉ là lớp phủ tùy chọn, và đòi AAT làm Trục 2 hỏng. Thực tế `VIE_md_organizations.txt` định nghĩa:

| MIO | Phạm vi | Liên quan Trục 2 không quân |
|---|---|---|
| `VIE_viettel_manufacturer` | `cnc`, `mio_cat_eq_only_uav`, `guided_missile_equipment`, `sam_missile_equipment`; `CAT_drones CAT_a_uav CAT_naval_radar CAT_missile CAT_electrical_tech`; trait radar, EW, UAV, drone trinh sát / tấn công, loitering, tên lửa phòng không | đúng 4 trụ (A31, Radar, Tích hợp, UAV) |
| `VIE_vaeco_manufacturer` | máy bay nhẹ, trực thăng, vận tải | chỉ gần A32 bậc 3 (C-295M, trực thăng) |
| `VIE_gdt_manufacturer`, `VIE_ba_son_manufacturer` | lục quân, hải quân | không |

Trục 2 hải quân và lục quân đã dùng `add_mio_size` bọc `has_dlc = "Arms Against Tyranny"` (`VIE_ba_son_mio_size_N`; ghi chú Q8 = a: không dùng `add_mio_funds` cùng lúc, vì nó tự lên size). Lý do "Q16 chỉ-Decision vì AAT" đã được giải bởi cái bọc `has_dlc`: người không có AAT chỉ không thấy MIO.
**Sửa:** Trục 2 giữ bậc bằng biến + Decision (không đổi), và nuôi `VIE_viettel_manufacturer` bằng `VIE_apm_viettel_mio_size` (+1 ở A31 bậc 2 và 3, Radar bậc 2, UAV bậc 2). A32 không có MIO. Trait sẵn có của Viettel đã cho bonus SAM và UAV, nên modifier Trục 2 không cộng cùng loại (tránh đếm đôi).

## A2 · Hai hiệu ứng trong 6.4 không có token trong MD

Đối chiếu `code-resource.md` của MD và `common/modifier_definitions`:
- "**Giá thay thế tên lửa phòng không** (A31)": MD chỉ có `olv_/gnss_/comsat_/spysat_/killsat_production_*` (vệ tinh, phóng) và `equipment_cost_multiplier_modifier` (= **chi phí duy trì** trang bị, tên hiển thị "Equipment upkeep"). Không có modifier giá/tốc độ sản xuất SAM. Mod đã có `VIE_af_equipment_cost_multiplier_modifier` trong `VIE_armed_forces_modifier`.
- R6 báo cáo cho Trục 2 sở hữu "tuổi thọ / độ tin cậy": **độ tin cậy** chỉ chỉnh được qua `equipment_bonus` của MIO (`reliability`), không có modifier quốc gia; **tuổi thọ** không có cơ chế nào trong MD.
Token thật dùng được: `air_accidents_factor` (A32), `air_detection` (Radar), `air_defence_factor` (A31, mod đã dùng cho SAM/Igla), `equipment_cost_multiplier_modifier` (chi phí duy trì), `air_experience`, `add_mio_size`.
**Sửa:** bảng hiệu ứng 6.4 viết lại bằng các token trên; bỏ "nửa mức phạt phụ tùng nếu SOV không còn hỗ trợ" và "kéo dài tuổi thọ" (không có cơ chế; phần Nga ngần ngại nằm ở Decision 1B, E17 đã chuyển).

## A3 · Bộ đếm slot: bỏ hook `VIE_collapse_aftermath`, dùng bộ đếm tự chữa

R9 (3.1) và 6.6 của bản 1.3 dựa vào `VIE_collapse_aftermath` để đếm lại. **Đã chốt (2026-10-02): bỏ hook này, không dùng nữa.** Mod đã gỡ collapse/civil war (`tools/TESTING.md`: "Removed 2026-10-02"); grep repo cho `VIE_collapse_aftermath`, `VIE_civil_war_end`, `recount` ra **0 kết quả trong code** (dòng "Kept: `VIE_civil_war_end`" trong TESTING là chú thích cũ, đã sửa). Hệ quả: mất event hoàn tất thì slot kẹt ở 2 nếu không có cơ chế khác.

Ghi chú: các tài liệu hải quân (`VIE_naval_truc2/3_review_and_plan.md`) còn ghi recount "gọi trong `VIE_collapse_aftermath`", nhưng code tương ứng không có trong repo; coi các dòng đó là tài liệu cũ, hải quân chưa có đếm lại (nợ riêng, Q-B4).
**Sửa cho Trục 2 không quân (và ghi nợ cho hải quân):** bộ đếm **tự chữa**. Hàm tháng `VIE_apm_slot_heal` (gọi từ cùng scheduler): nếu không còn timed idea `VIE_apm_prog_*` nào thì đặt `VIE_var_apm_active = 0`. Không gắn vào bất kỳ hook nội chiến nào, và không cần `VIE_catch_up`.

## A4 · Tiền tố và tên: focus còn `VIE_air_*`, biến còn tên trần

Bản 1.3 chốt (4.3) Trục 2 dùng `VIE_apm_`/`vie_air_ind`, nhưng 6.2 vẫn ghi focus `VIE_air_industry_law`, `VIE_air_mro_a32`…, 6.3 ghi `VIE_var_a32_tier`, `VIE_var_air_industry_active`… Tiền tố `VIE_air_` đã bị roster chỉ huy chiếm (Trục 1 đã phải né, xem `VIE_air_truc1_review_and_plan.md` A2); `VIE_var_a32_tier` là tên chung chung dễ đụng nhánh khác.
**Sửa:** đổi hết sang `VIE_apm_*` (focus `VIE_apm_law/_a32/_a31/_radar/_integration/_uav/_mature`; bậc `VIE_apm_a32_tier`, `VIE_apm_a31_tier`, `VIE_apm_radar_tier`, `VIE_apm_integ_tier`, `VIE_apm_uav_tier`; slot `VIE_var_apm_active`; category `VIE_apm_category`; Decision `VIE_apm_d_*`; idea `VIE_apm_prog_*`). Đã grep: 0 kết quả trong repo.

---

# PHẦN 2 — 7 CHỖ LỆCH GAME / MOD

## B1 · 15 Decision `fire_only_once` thay vì 5 Decision lặp lại

MD Code Style Guide: "Use `fire_only_once` sparingly". Hải quân dùng 5 Decision cho 5 chương trình; lục quân 9. 15 Decision (mỗi bậc một cái) làm category dài, 30 khóa loc chỉ để mở bậc kế của cùng một trụ.
**Sửa:** **5 Decision lặp lại** (một mỗi trụ), `visible` = focus xong và bậc < 3, `available` = slot < 2, không còn timed idea của trụ, và trigger cổng của bậc kế `VIE_apm_<p>_ok`. Bấm ⇒ `VIE_apm_program_start` ⇒ event chọn của bậc kế (đọc `VIE_apm_<p>_tier`) ⇒ timed idea ⇒ event ẩn hoàn tất tăng bậc. Số event ≈ 20 (15 chọn + 5 ẩn), không đổi nội dung.

## B2 · Cổng đọc từ Trục 1 chưa được viết ra

Bản 1.3 mô tả bằng lời ("điều kiện cho E17", "Pechora-2TM") và vẫn nói "Trục 1 cộng exp vào Trục 2". Trục 1 đã code **không ghi exp**, chỉ ghi cờ/biến (`VIE_ap_pechora_scope`, `VIE_ap_radar_viettel_fast`, `VIE_var_air_delivered`, `VIE_var_sam_lr`, `VIE_ap_spyder_qty`, `VIE_ap_c295_qty`, `VIE_ap_t6c_qty`, `VIE_ap_l39ng_qty`).
**Sửa:** bảng cổng trong 6.3 (mỗi bậc một cột "Cổng") và ba cờ có người đọc thật ngay trong Trục 2:

| Cờ/biến Trục 1 | Người đọc trong Trục 2 |
|---|---|
| `VIE_ap_pechora_scope` (1/2) | cổng A31 bậc 1; scope 2 ⇒ chi phí ×0,8, −3 tháng |
| `VIE_ap_radar_viettel_fast` | Radar bậc 1: ×0,8 chi phí, −3 tháng |
| `VIE_var_air_delivered ≥ 12` | cổng A32 bậc 3 |
| `VIE_ap_c295_qty > 0` | lựa chọn "C-295M và trực thăng" của A32 bậc 3 |
| `VIE_var_sam_lr ≥ 1` | cổng A31 bậc 3, Tích hợp bậc 2 |
| `VIE_ap_spyder_qty > 0` | cổng Tích hợp bậc 1 (Python-5/Derby đến cùng SPYDER) |
| `VIE_ap_t6c_qty > 0` hoặc `VIE_ap_l39ng_qty > 0` | cổng Tích hợp bậc 3 |

## B3 · Cổng "ít nhất hai trong F2, F3, F4" không biểu diễn được bằng `prerequisite`

`prerequisite` chỉ có OR (một khối nhiều focus) và AND (nhiều khối). "Hai trong ba" cần scripted trigger.
**Sửa:** F5 `prerequisite = { focus = F2 focus = F3 focus = F4 }` (OR) + `available` gọi `VIE_apm_two_of_three` (đếm `has_completed_focus`).

## B4 · F7 không định nghĩa "đủ điều kiện bậc"

6.2 ghi "đặt `VIE_cap_mature_air_industry` khi đủ điều kiện bậc" nhưng không nói điều kiện.
**Sửa:** scripted trigger `VIE_apm_mature_ok` = `a32_tier = 3`, `a31_tier ≥ 2`, `radar_tier = 3`, `integ_tier ≥ 2`, `uav_tier ≥ 2` (một chỗ để đổi). F7 `available` đòi trigger này.

## B5 · Trục 3 T5 còn tham chiếu `VIE_air_mro_a32`

7.1 T5: "T4, hoặc `VIE_air_mro_a32`". Đã đổi sang `VIE_apm_a32` (bản 1.4). Trục 3 chỉ đọc, không viết ngược (R12).

## B6 · Hiệu ứng nặng về Nga hỗ trợ đã chuyển sang 1B

6.3 A32 bậc 3 "nếu SOV không còn hỗ trợ, nửa mức phạt phụ tùng; điều kiện cho E17": E17 đã sang 1B (Trục 1 review B1), và MD không có cơ chế phụ tùng. A32 bậc 3 chỉ còn: tai nạn −2%, XP, và **là dữ kiện mà Decision hỗ trợ Su-27/30 của 1B đọc** (`VIE_apm_a32_tier`).

## B7 · Chi phí: thang giá thật trong khi hai Trục 2 kia dùng thang giá công trình của MD

Hải quân 34,7 tỷ, lục quân 30,25 tỷ, vì Decision xây công trình bằng helper `one_state_*` của MD (mỗi dockyard 7,5 tỷ, airbase 3,0, radar 1,75). Trục 2 không quân không xây công trình nào nên 3,1 tỷ (giá thật, cùng thang Trục 1 = 3,7 tỷ) là nhất quán, nhưng người chơi sẽ thấy hiệu ứng nhỏ so với hai trục kia. Giữ (Q-B2), ghi rõ trong 6.3.

---

# PHẦN 3 — THIẾT KẾ CHỐT

Toàn bộ bảng focus (7), bậc (15), token, MIO nằm ở `VIE_air_force_content_report.md` Phần 6 (bản 1.4). Tóm tắt dữ kiện cần để code:

## 3.1 Ba hợp đồng với phần còn lại

| Cạnh | Qua |
|---|---|
| Trục 1 → Trục 2 | bảng B2 |
| Trục 2 → Trục 3 | T5 đọc `VIE_apm_a32` (hoặc T4); không ghi ngược |
| Trục 2 → 1B | `*_tier`, `VIE_apm_sam_production`, `VIE_apm_radar_orient`, `VIE_cap_mature_air_industry` (điều kiện hybrid/nội địa P2, P3, P8, P9, P10; Decision hỗ trợ Su-27/30) |

## 3.2 Biến và cờ (đề xuất)

| Tên | Đặt bởi | Đọc bởi |
|---|---|---|
| `VIE_apm_a32_tier`, `VIE_apm_a31_tier`, `VIE_apm_radar_tier`, `VIE_apm_integ_tier`, `VIE_apm_uav_tier` (0–3) | event ẩn hoàn tất | cổng bậc kế, `VIE_apm_mature_ok`, 1B |
| `VIE_var_apm_active` (0–2) | `VIE_apm_program_start/_end`, `VIE_apm_slot_heal` | `available` của Decision |
| `VIE_apm_<p>_choice` (lựa chọn của bậc đang chạy, 1–3) | event chọn | event ẩn hoàn tất (đọc xong thì không cần nữa) |
| `VIE_apm_radar_orient` (1 chống tàng hình / 2 ưu tiên 3D), `VIE_apm_sam_production` (cờ) | Radar bậc 3, A31 bậc 3 | 1B (P10, P8) |
| `VIE_cap_mature_air_industry` (cờ) | F7 | 1B |
| timed idea `VIE_apm_prog_a32/_a31/_radar/_integ/_uav` | event chọn | chỉ báo "đang chạy", dùng để tự chữa slot |

Không giữ cờ `_active/_done/_waiting` cho Decision, `_progress`, `VIE_cap_*` thừa (xem naval B5).

## 3.3 Việc tránh (để khỏi lặp lỗi hải quân)

- Không có trạng thái "chờ giữa chừng": cổng ở lúc bấm, `custom_trigger_tooltip` nêu điều kiện thiếu.
- Event chọn do người chơi bấm Decision: miễn `VIE_popup_cd`. Event ẩn hoàn tất không tính vào ngân sách pop-up.
- `days = <biến>` cho `add_timed_idea` và `country_event` đã được xác minh trong mã MD (naval Phần 10).
- Mọi `ai_chance` có tốn tiền có guard `bankruptcy_incoming_collapse`.

---

# PHẦN 4 — PLAN CODE (9 bước, mỗi bước 1 commit, nhánh `claude/air-truc2`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | báo cáo + `VIE_v9_flag_mapping.md` | Báo cáo bản 1.4 (đã làm). Thêm mục "Truc 2 khong quan" vào bảng cờ | grep `VIE_apm_`, `vie_air_ind`, `VIE_apm_category` 0 kết quả |
| **1** | `common/scripted_triggers/VIE_md_triggers_air_ind.txt` (mới) | `VIE_apm_<p>_ok` (5 cổng bậc kế, đọc cờ Trục 1), `VIE_apm_two_of_three`, `VIE_apm_mature_ok`, `VIE_apm_slot_free` | `live.py` sạch |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc + `tools/build_vie_focus_icons.py` (7 mục `FOCI`) + `common/decisions/categories/VIE_md_categories.txt` | 7 focus (6.2), category `VIE_apm_category` (priority **87**; đã dùng 88–95 và 100) | `tools/audit/audit.py` (toạ độ x ≥ 288, gap, forward-ref); `verify_all_loc.py` |
| **3** | `common/scripted_effects/VIE_md_effects_air_ind.txt` (mới), `common/ideas/VIE_md_ideas_air_ind.txt` (mới) | `VIE_apm_pay`, `VIE_apm_program_start/_end`, `VIE_apm_slot_heal`, `VIE_apm_viettel_mio_size`, helper cộng modifier (`VIE_apm_add_accidents/_detection/_air_def/_upkeep`, có `VIE_ap_ensure_af_modifier` và tooltip, kẹp theo trần), 5 timed idea | `live.py` sạch |
| **4** | `events/VIE_air_ind.txt` (`add_namespace = vie_air_ind`) + `common/decisions/VIE_md_air_ind_decisions.txt` | **A32 trọn vẹn**: Decision lặp lại, 3 event chọn (`.11 .12 .13`), event ẩn hoàn tất `.19` | chơi tới 2011 (console mở F2), bấm Decision: event, timed idea, bậc 1 |
| **5** | cùng file | **A31** (`.21–.23`, `.29`) và **Radar** (`.31–.33`, `.39`); đọc cờ Trục 1 | `VIE_ap_pechora_scope` đổi giá; MIO Viettel +1 (có AAT) |
| **6** | cùng file | **Tích hợp** (`.41–.43`, `.49`) và **UAV** (`.51–.53`, `.59`); UAV bậc 2–3 AI chỉ `VIE_ai_free` | cổng đọc Trục 1 đúng |
| **7** | focus F7 + `VIE_cap_mature_air_industry`; nối `VIE_apm_slot_heal` vào `on_monthly` | mở F7 bằng console ngày | slot tự chữa: xóa timed idea bằng console, tháng sau slot = 0 |
| **8** | `localisation/english/VIE_md_events_air_ind_l_english.yml` (BOM), `tools/TESTING.md` (mục "Air industry"), `VIE_v9_flag_mapping.md`, `tools/audit/air_ind_balance.py` | loc ≈ 120 khóa; script cộng chi/bậc, trần modifier, MIO size | `verify_all_loc.py`; script PASS |
| **9** | `tools/build_vie_air_event_pictures.py` | ảnh cho event chọn (13 tệp Commons như Trục 1) hoặc dùng `GFX_report_event_generic_read_write` tạm | không lỗi `texturefile` |

Ước lượng: 7 focus, 5 Decision, ≈ 20 event (5 ẩn), 5 timed idea, ≈ 600 dòng script, ≈ 120 khóa loc.

---

# PHẦN 5 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào TESTING.md ở bước 8)

- [ ] `error.log`: grep `vie_air_ind`, `VIE_apm_`, `add_mio_size`, `mio:`, `texturefile`.
- [ ] Chạy hai lượt: có AAT (MIO Viettel nhận +1) và không AAT (không lỗi, không MIO).
- [ ] F1 xong ⇒ category `VIE_apm_category` hiện; F2–F4 xong ⇒ Decision tương ứng hiện, chỉ khi cổng đạt.
- [ ] Decision lặp lại: bấm A32 lần 1 ⇒ bậc 1; ngay sau đó Decision mờ (còn timed idea); xong ⇒ hiện lại cho bậc 2, đòi `date > 2016.12.31`.
- [ ] Slot: chạy A32 + A31 cùng lúc thì Radar mờ (slot = 2); xóa timed idea bằng console ⇒ tháng sau slot về 0.
- [ ] Cổng Trục 1: không ký E7 ⇒ A31 bậc 1 mờ với tooltip "cần hợp đồng Pechora"; `VIE_ap_radar_viettel_fast` ⇒ Radar bậc 1 rẻ hơn.
- [ ] Modifier: `VIE_af_air_accidents_factor`, `air_detection`, `air_defence_factor` tăng đúng, tooltip hiện, không vượt trần.
- [ ] Tổng chi đủ 15 bậc ≈ 3,1 tỷ; AI chỉ đi bậc dựa tin [~] khi `VIE_ai_free`.
- [ ] Size tối đa MIO của MD không bị vượt (tổng +4 từ Trục 2).

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đề xuất)

| # | Câu hỏi | Mặc định |
|---|---|---|
| Q-B1 | 5 Decision lặp lại thay vì 15 Decision `fire_only_once` (B1) | **5 Decision** |
| Q-B2 | Giữ thang giá thật 3,1 tỷ (B7), hay nâng lên thang MD để ngang hải quân/lục quân | **Giữ giá thật** |
| Q-B3 | Nuôi MIO Viettel bằng `add_mio_size` (+4 tổng) (A1) | **Có** |
| Q-B4 | Slot tự chữa bằng hàm tháng (A3); đồng thời vá cho hải quân | **Có**; vá hải quân tách riêng |
| Q-B5 | Bậc dựa tin [~] (UAV 2–3, A31 bậc 3 sản xuất) AI chỉ khi `VIE_ai_free` | **Có** |
| Q-B6 | Trần modifier: phát hiện Trục 1 ≤ 5%, Trục 2 = 6%, Trục 3 theo 7.5 (≈ 16%): tổng ≈ 27%, chấp nhận hay đặt trần chung | **Chấp nhận**, đo bằng script bước 8 |
| Q-B7 | Ảnh event Trục 2 lấy từ Commons như Trục 1 (bước 9) | **Có** |

---

# TRẠNG THÁI

Bước 1 (triggers) và bước 2 (7 focus, category, loc 16 khóa) đã code, chưa chạy game, chưa commit. Focus dùng icon generic của vanilla (`GFX_focus_generic_*`) như hải quân; icon riêng thêm 7 mục vào `FOCI` khi có ảnh. Tooltip `unlock_decision_tooltip = VIE_apm_d_*` trỏ Decision chưa tồn tại tới bước 4–6.

Review và sửa báo cáo xong (2026-10-02). **Chưa có dòng code nào cho Trục 2.** Bước 0 đã làm (báo cáo 1.4); bước 1–9 chờ bạn chốt Phần 6.

## Tiến độ code (2026-10-02)
Bước 1–8 đã code, chưa chạy game, chưa commit: triggers, 7 focus + category, helper + 5 timed idea, 5 Decision lặp lại, 20 event (15 chọn + 5 hoàn tất), `VIE_apm_slot_heal` nối vào `on_monthly` (bước 7; F7 đã nằm trong bước 2), loc 117 khóa, `tools/audit/air_ind_balance.py` (ALL PASS: tổng 3,10 tỷ, đường lịch sử xong khoảng 2030-07 với 2 slot, MIO +4), mục "Air industry" trong `tools/TESTING.md`, bảng cờ trong `VIE_v9_flag_mapping.md`.
Còn: bước 9 (ảnh event) và thử trong game theo TESTING.md. Nợ chung: `VIE_ai_free` được `VIE_md_p1b_decisions.txt` dùng nhưng không được định nghĩa ở đâu; hải quân chưa có đếm lại slot.
