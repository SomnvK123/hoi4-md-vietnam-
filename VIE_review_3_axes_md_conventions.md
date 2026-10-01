# REVIEW TỔNG 3 TRỤC LỤC QUÂN SO VỚI MILLENNIUM DAWN GỐC

> Ngày 1/10/2026 · repo @ `f3236f9` + thay đổi chưa commit của Trục 3 và icon.
> Phương pháp: (1) chạy **bộ validator thật của MD** (`tools/validation/run_all_validators.py`, sparse-clone từ `MillenniumDawn/Millennium-Dawn@main`) lên `common/`, `events/`, `localisation/`, `interface/` của mod; (2) so đường dẫn file với cây MD; (3) tự soát tham chiếu chéo (effect, trigger, event, flag, focus, idea).
> Chú ý khi đọc kết quả validator: bản clone chỉ có `tools/` và `.claude/docs/`, không có `common/` của MD, nên các cảnh báo "unknown modifier", "has_active_mission ... names no decision", "variables", "unreferenced-triggered-only" **là nhiễu**, đã loại. Phần dưới chỉ gồm lỗi đã kiểm chứng bằng cách đọc code.

## KẾT LUẬN

Logic nội tại của 3 trục chặt: 0 effect/trigger gọi mà thiếu định nghĩa (trừ ca C1 bên dưới), 0 event bắn mà thiếu định nghĩa, 0 focus/idea tham chiếu thiếu, 0 va chạm tọa độ focus, loc đủ key. **Nhưng có 5 lỗi nghiêm trọng** (một số nằm sẵn từ trước Trục 1/2, một số do tôi), trong đó 2 lỗi có thể làm hỏng cả game MD, không chỉ mod này. Sau đó là 8 lỗi convention và vài nợ nhỏ.

---

## A. LỖI NGHIÊM TRỌNG (nên sửa trước khi chơi thử)

### C1 · 🚨 `common/scripted_effects/00_yearly_effects.txt` ghi đè file cùng tên của MD

| | |
|---|---|
| Bằng chứng | Mod có file `common/scripted_effects/00_yearly_effects.txt` (92 dòng). MD có file **cùng đường dẫn** (2 737 dòng). HOI4 thay **nguyên file** theo đường dẫn, không gộp. |
| Hệ quả | Mọi `trigger_year_XXXX_events` của MD cho **mọi quốc gia** biến mất (mod chỉ định nghĩa 6 năm). Chưa kể file gọi `VIE_try_proc_1/2/5/8/11/14/18`, **không có định nghĩa nào** (7 lệnh gọi treo), và đọc game rule `VIE_alt_procurement` không tồn tại. |
| Nguồn gốc | Bộ khung Trục 1 cũ (commit `c32aecc`). `VIE_truc1_review_and_plan.md` B1 đã cảnh báo đúng điều này và thay bằng scheduler `VIE_event_scheduler_p14`, nhưng file cũ vẫn còn. |
| **Fix** | `git rm common/scripted_effects/00_yearly_effects.txt`. Không cần thay thế: Trục 1 đã chạy qua `VIE_event_scheduler_p14` (xác nhận: `VIE_try_proc_*` không được định nghĩa ở nơi nào khác). |

### C2 · 🚨 Event trùng ID: `events/VIE_md_mil.txt` (bộ khung cũ) và `events/VIE_proc_army.txt`

19 ID `vie_proc_army.N` được định nghĩa ở **cả hai file** (validator MD báo lỗi `duplicate-event-id` ×19; `tools/audit/ev.py` của repo cũng báo). File cũ dùng key loc khác (`vie_proc_army.1a`) và trigger rỗng. Engine giữ một bản, không đảm bảo là bản đúng (thứ tự nạp theo tên file), nên Trục 1 có thể chạy bằng event khung.
**Fix:** kiểm tra `events/VIE_md_mil.txt` còn nội dung riêng không (`grep -n "id = " events/VIE_md_mil.txt`; có tham chiếu `VIE_ALT_ON` ở dòng 344), rồi `git rm` file đó. Giữ `events/VIE_proc_army.txt`.

### C3 · 🚨 `check_variable = { X >= N }` bị parse sai âm thầm (6 chỗ, cả Trục 2 và Trục 3)

MD (validator `COMMON SCRIPTING MISTAKE`): *"check_variable does not accept '>=' inline (silently mis-parsed)"*. Các chỗ trong code của chúng ta:

| File | Trigger | Hệ quả nếu parse sai |
|---|---|---|
| `VIE_md_triggers_p15.txt` | `VIE_def_ind_level_ge_2` (>= 2), `_ge_4`, `_ge_8`, `VIE_def_ind_export_open` (>= 6) | ngã rẽ Core/Divest, capstone Trục 2, triển lãm và xuất khẩu mở sai điều kiện |
| `VIE_md_triggers_p17.txt` | `VIE_lf_arm_done_3` (>= 3), `VIE_lf_cap_done_2` (>= 2) | HD và MOD mở sớm hoặc không bao giờ mở; `VIE_lf_gate_open` (nhánh `free`) đọc `level_ge_2` |

**Fix:** biến đều là số nguyên, đổi sang bất đẳng thức chặt: `level_ge_2` → `> 1`, `_ge_4` → `> 3`, `_ge_8` → `> 7`, export `> 5`, `arm_done > 2`, `cap_done > 1`. Giữ tên trigger (`_ge_N`) để khỏi sửa chỗ gọi. Sau đó chạy lại validator, mục này phải về 0.

### C4 · 🚨 `set_country_flag = { flag = X days = N }` thiếu `value = 1` (163 chỗ trong toàn repo)

MD: *"flag defaults to 0 and fails the shortform has_country_flag check"*. `VIE_popup_cd` đặt kiểu này (cả Trục 1, 2, 3 và các scheduler cũ p2–p13) nên `NOT = { has_country_flag = VIE_popup_cd }` **có thể không bao giờ chặn**, tức luật "không hai pop-up trong 45 ngày" (`tools/TESTING.md`) không có hiệu lực. Cũng áp cho `VIE_def_ind_export_clock` (365 ngày, Trục 2).
**Fix:** thêm `value = 1` cho mọi `set_country_flag = { flag = ... days = ... }`. Đây là thay thế máy móc, làm bằng một lệnh `sed` hoặc script Python và chạy lại validator. Nên test trong game: bắn hai event pop-up liên tiếp xem có bị chặn không.

### C5 · 🚨 Loc: `[THẬT]`, `[ĐỀ XUẤT]`, `[ALT-HISTORY...]` bị hiểu là lệnh scripted loc

Ngoặc vuông trong loc HOI4 là lời gọi hàm. Validator báo `missing-scripted-loc` ("thật", "alt-history"). 31 chỗ trong `VIE_md_events_p17_l_english.yml` (mô tả focus Trục 3) và hàm nhãn `VIE_lf_alt_early` (tôi tự thêm ở bước 6).
**Hệ quả:** trong game các nhãn này hiển thị trống hoặc thành chuỗi lỗi, mô tả focus bị cụt.
**Fix:** đổi dấu ngoặc vuông thành ngoặc đơn hoặc thẻ màu, ví dụ `(THẬT)`, `(ĐỀ XUẤT)`, `§R(ALT-HISTORY: cải cách sớm)§!`. Giữ nguyên `[VIE_lf_alt_n1]` (đây là lời gọi scripted loc thật). Tài liệu thiết kế (báo cáo, plan) vẫn dùng ngoặc vuông được vì không nạp vào game.

---

## B. LỖI CONVENTION SO VỚI MD (validator MD báo, chỉ cần sửa cú pháp)

| # | Lỗi | Nơi | Fix |
|---|---|---|---|
| M1 | `log` là effect duy nhất trong `complete_effect` ("delete the block") | 6 decision Trục 3 (`VIE_md_decisions_lf.txt`) | xóa 6 khối `complete_effect`; log đã nằm ở `remove_effect` |
| M2 | `log` là effect duy nhất trong `option` | `vie_lf.1.a/.3.a/.5.a`, 2 option `vie_def_ind`, 11 option `VIE_proc_army.txt` | bỏ dòng `log` trong option không có hiệu ứng (giữ `name`, `ai_chance`) |
| M3 | `allowed = { always = no }` và `allowed_civil_war = { always = no }` thừa trong ý tưởng | 6 ý tưởng Trục 3, 5 ý tưởng Trục 2 (`VIE_md_ideas_p15.txt`), phần lớn ý tưởng cũ | xóa hai dòng (với `add_ideas` / `add_timed_idea` không bị ảnh hưởng) |
| M4 | khai `cost = 10` (mặc định) | 13 focus: 12 focus Trục 3, capstone Trục 2 | xóa dòng `cost = 10`; MD `focus-tree-reference.md`: *"Omit defaults: cost = 10"* |
| M5 | `has_country_flag = VIE_dec_*_started` trong `available` không có loc | 9 decision Trục 2 (`VIE_md_def_industry.txt`) | thêm key loc mang tên cờ (ví dụ `VIE_dec_stv_started:0 "Chương trình đã bắt đầu"`), hoặc bọc `custom_trigger_tooltip` |
| M6 | em dash `—` trong loc | `VIE_md_events_p15_l_english.yml` (16 dòng) | đổi thành dấu chấm, phẩy hoặc hai chấm (`localisation-rules.md`) |
| M7 | cờ chỉ set bởi một focus nhưng đọc như cờ | `VIE_lf_cap_land/ad/cyber` | thay đọc cờ bằng `has_completed_focus = VIE_lf_cap_area_control` / `_ad_coord` / `_info_ops` (tùy chọn, 4 chỗ đọc ở `VIE_lf_mod_reward`, `VIE_lf_cap_reward`) |
| M8 | add_tech_bonus `name` không trùng ID decision (cảnh báo) | 11 chỗ ở `VIE_md_def_industry.txt` | chỉ là cảnh báo, giữ nếu cố ý (D1 cần hai tên khác nhau như đã ghi chú) |

Ngoài ra validator báo `not-standardized` cho mọi file mới: chạy `python tools/standardization/standardize.py <loại> <file>` của MD nếu muốn đúng chuẩn trình bày, nhưng đây là tùy chọn.

---

## C. CỜ VÀ HÀM MỒ CÔI (không phải lỗi, cần quyết định)

| Mục | Ghi chú | Hướng |
|---|---|---|
| `VIE_lf_dev_strategic` (cờ) | set bởi PS nhưng không ai đọc (decision đọc `has_completed_focus`) | bỏ `set_country_flag` hoặc đọc cờ ở decision; ưu tiên bỏ |
| `VIE_lf_done` (cờ) | chờ nhánh Chính trị/Đối ngoại | giữ, đã ghi trong cross-axis review |
| `VIE_dec_*_done` ×7 (Trục 2) | set nhưng không đọc (trừ `VIE_dec_z_factories_done`, `VIE_dec_pth_done`) | giữ nếu muốn dùng cho nhánh khác, nếu không thì bỏ |
| `VIE_ev_t90_tanks`, `VIE_ev_kilo_submarines`, `VIE_ev_bastion_p_coastal_defence` | đã biết (Trục 1 Q1) | giữ |
| `VIE_lf_xp_25`, `VIE_d2_open_tt`, `VIE_proc_gate_paracel_capable` | không ai gọi | xóa `VIE_lf_xp_25`; hai cái kia đã ghi chú giữ |

---

## D. NHỮNG GÌ ĐÃ ĐÚNG (khỏi soát lại)

- 3 file ghi đè MD **có chủ đích** và có chú thích: `common/bookmarks/blitzkrieg.txt`, `common/scripted_effects/VIE_political_leaders.txt`, `descriptor.mod` (ngoài 00_yearly_effects.txt ở C1, không còn file nào trùng đường dẫn MD).
- 0 `VIE_*` gọi mà thiếu định nghĩa (trừ 7 lệnh gọi ở C1), 0 event bắn mà thiếu định nghĩa, 0 focus tham chiếu thiếu, 0 ý tưởng dùng mà thiếu.
- Focus tree: 0 dangling, 0 forward-ref, 0 cycle, 0 va chạm tọa độ tuyệt đối; validator `FOCUS TREE STRUCTURAL` không báo gì ở vùng Trục 2 và 3.
- `ai_will_do`, log trong `completion_reward`, `search_filters`, tab, BOM của loc: đúng chuẩn MD.
- Trục 3 ↔ Trục 1/2: một chiều đọc (`VIE_def_ind_level_ge_2`) và một chiều ghi cờ hướng (bước 8), không có prerequisite chéo.

---

## E. THỨ TỰ SỬA ĐỀ XUẤT

1. **C1, C2** (xóa 2 file thừa): 10 phút, loại bỏ rủi ro hỏng MD và trùng event.
2. **C3** (6 trigger) và **C4** (163 flag): sửa máy móc, chạy lại validator.
3. **C5** (31 nhãn ngoặc vuông): thay chuỗi trong loc và hàm nhãn.
4. **M1–M6**: dọn convention, một commit.
5. Test trong game theo `tools/TESTING.md` (thêm hai ý: `VIE_popup_cd` chặn thật sau C4, và mô tả focus hiển thị đúng sau C5).
6. Chạy lại: `python tools/validation/run_all_validators.py` trên bản MD đầy đủ (cần clone cả `common/`), hoặc ít nhất lặp lại phép chạy bản sparse và so số lỗi.

## F. CÁCH TÁI TẠO PHÉP CHẠY

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/MillenniumDawn/Millennium-Dawn.git md
cd md && git sparse-checkout set tools .claude/docs
cp -r <mod>/common <mod>/events <mod>/localisation <mod>/interface .   # xoá *.bak trong common/national_focus
python tools/validation/run_all_validators.py --no-color --output report.txt
```
Lọc theo tên file của mod; bỏ các cảnh báo `unknown-modifier`, `bankruptcy_incoming_collapse names no decision`, `variables`, `unreferenced-triggered-only` vì thiếu nội dung MD trong bản sparse.
