# REVIEW TRỤC 1 KHÔNG QUÂN (MUA SẮM LỊCH SỬ) + PLAN CODE

> Đầu vào: `VIE_air_force_content_report.md` bản 1.2, Phần 5 (Trục 1) và các chỗ Trục 1 chạm tới (4.2, 4.3, 8.2, 9, 12, 13).
> Đối chiếu với: repo @ `e4f3215`; MD v2.0.0 cài trên máy (`workshop/content/394360/2777392649`: `history/countries`, `history/units`, `common/technologies/missile_defense.txt`, `common/units/equipment/MD_sam_missile.txt`, `common/national_focus/05_algeria.txt`, `Changelog.txt`); mẫu code Trục 1 lục quân (`VIE_md_effects_p14.txt`) và hải quân (`VIE_md_effects_naval.txt`, `VIE_naval_truc1_review_and_plan.md`).
> Phạm vi: chỉ Trục 1. Trục 2, Trục 3, 1B chỉ nhắc khi Trục 1 phải nối vào.
>
> **KẾT LUẬN: logic cốt lõi (cửa sổ + thử lại hằng tháng, lựa chọn lịch sử là mặc định, dữ kiện lịch sử, tổng chi ≈ 3,9 tỷ) ĐÚNG và giữ nguyên.
> Nhưng bản 1.2 chưa code được: 5 lỗi chặn (Phần 1), 7 chỗ không khớp game/mod (Phần 2).**
> Báo cáo gốc đã được sửa theo Phần 3 (bản 1.3, Phần 5 viết lại). Phần 4 là plan code, Phần 6 là các quyết định cần bạn chốt (mỗi dòng có mặc định).

---

# PHẦN 1 — 5 LỖI CHẶN

## A1 · Mã quốc gia sai: `IND` là Indonesia, `ESP` không tồn tại

Đếm từ `history/countries` của MD:

| Báo cáo dùng | Thực tế trong MD | Hệ quả |
|---|---|---|
| `IND` cho Ấn Độ (E1, E13) | `IND - Indonesia.txt`; Ấn Độ là **`RAJ`** | Cổng `country_exists = IND` luôn đúng nhưng **trỏ nhầm nước**; `producer`/opinion cũng nhầm |
| `ESP` cho Tây Ban Nha (E8, P6) | **`SPR`** | `country_exists = ESP` sai tag, engine bỏ im lặng hoặc báo lỗi |

Các tag còn lại đúng: `SOV`, `ROM`, `BLR`, `CZE`, `ISR`, `USA`, `FRA`, `SWE`. Mod đã dùng `RAJ` đúng cho Ấn Độ (`events/VIE_def_ind.txt:43`).

## A2 · Tiền tố và tên đã bị roster chỉ huy không quân (đã code 01/10) chiếm

Mục 4.3 báo cáo nói "phải grep 0 kết quả"; thực tế **không phải 0**:

| Thứ báo cáo định dùng | Đã có trong repo |
|---|---|
| tiền tố `VIE_air_` | 20 character `VIE_air_<tên>` (`VIE_md_air_commanders.txt`), cờ `VIE_air_phase0_done`, `VIE_air_step_1…7`, idea `VIE_air_dominance_idea` |
| scheduler `VIE_event_scheduler_air` (suy ra từ nhóm tên) | **đã có**, là scheduler *chỉ huy* (`VIE_md_effects_air.txt`), đã gọi trong `on_monthly` |
| file `VIE_md_effects_air.txt` | đã có (chỉ huy) |
| namespace `vie_air` | trống, nhưng `vie_air_commanders` đã được kế hoạch roster giữ chỗ làm phương án dự phòng |

Nếu code Trục 1 vào đúng tên cũ, scripted effect trùng tên **ghi đè** chứ không gộp (cùng lý do mod không dùng `trigger_year_*`), làm mất scheduler chỉ huy.
**Sửa:** namespace **`vie_air_proc`** (khớp `vie_proc_army`), scheduler `VIE_event_scheduler_air_proc`, tiền tố cờ/biến **`VIE_ap_`** (grep 0 kết quả, đã kiểm), file `VIE_md_effects_air_proc.txt` / `VIE_md_triggers_air_proc.txt` / `events/VIE_air_proc.txt` / `VIE_md_ideas_air_proc.txt`. Biến đếm dùng chung giữ `VIE_var_air_delivered` (grep 0, T5 của Trục 3 đọc). Trục 2 và 1B giữ `VIE_air_`… **không dùng**; cần chọn tiền tố khác khi tới lượt (đề xuất `VIE_apm_` và `VIE_a1b_`); ghi vào 4.3.

## A3 · Nhánh tên lửa phòng không (SAM) của MD chỉ tồn tại khi có DLC Götterdämmerung

Đọc `missile_defense.txt`: tech `SAM` có `allow_branch = { has_dlc = "Gotterdammerung" }`. `VIE - Vietnam.txt` chỉ cấp `SAM`, `SAM0` và kho `sam_missile_equipment_1` ×280 (S-125/S-75) **trong nhánh `has_dlc = "Gotterdammerung"`**. Báo cáo 12.2 mục 4 nói "Việt Nam được cấp sẵn tech SAM/SAM0" mà không nêu điều kiện DLC, và Q15 chỉ chốt BBA/non-BBA, không có GOT.

Hệ quả cho E2, E7, E10 (cả ba là SAM):
- Có GOT: `set_technology` chuỗi tới bậc cần (tech `SAM1` → `SAM2`…, mỗi bậc đòi bậc trước) rồi `add_equipment_to_stockpile` loại `sam_missile_equipment_N`. Tiền lệ MD: **S-300P/PMU = `sam_missile_equipment_3`** (Slovakia, Ukraine); S-125 = `_1`. Bậc tech theo năm: SAM0 1965→`_1`, SAM1 1975→`_2`, SAM2 1985→`_3`, SAM3 1995→`_4`, SAM4 2005→`_5`.
- Không có GOT: không có thiết bị SAM nào để cấp. Chỉ còn timed idea + `VIE_af_air_defence_factor` (đúng quy ước mod: MANPADS Igla cũng "tác dụng nằm ở modifier").

Mục 5.1 báo cáo ("làm trên hệ tên lửa của MD") đúng về hướng nhưng thiếu nhánh không-GOT. Thêm vào Q15: **ba nhánh DLC**: BBA (máy bay), GOT (SAM), và NSB không liên quan Trục 1 không quân.

## A4 · Chưa có ánh xạ từ mỗi sự kiện sang trang bị thật của MD

Báo cáo Phần 9 bàn variant cho 1B nhưng Trục 1 chỉ ghi "cấp máy bay…". Đối chiếu MD cho từng thứ (xem bảng đầy đủ ở 3.2):

- **Cách cấp đã có tiền lệ MD, không cần chép module:** `add_equipment_to_stockpile = { type variant_name amount producer }` với `has_dlc = "By Blood Alone"` / `else` dùng loại non-BBA. MD tự dùng đúng mẫu này (focus `ALG_purchase_russian_su30`: `medium_plane_airframe_2` + `variant_name = "Su-30MKI"`, `else` `MR_Fighter2`; trừ tiền `treasury_change` + `modify_treasury_effect`). Hệ quả: Phần 9 ("chép module từ MD") **chỉ cần cho 1B**, Trục 1 không phải tạo variant, trừ T-6C và L-39NG.
- **Variant có sẵn trong MD:** SOV `"Su-30"` (`medium_plane_airframe_2`), SOV `"Yak-130"` (`small_plane_strike_airframe_2`), SPR `"Airbus C-295"` (`large_plane_air_transport_airframe_2`), CZE `"Aero L-39"` (`small_plane_strike_airframe_1`).
- **Không có:** T-6C (USA), L-39NG (CZE), Yak-52 (ROM); MD không có loại thiết bị cho tiêu kích huấn luyện cơ bản piston.
- Loại non-BBA tương ứng: Su-30 → `AS_Fighter2` (đã chốt, khớp CHI và `vie_dip.16`; ALG/RAJ dùng `MR_Fighter2` nhưng không theo); trainer → `L_Strike_fighter2` (L-39, T-6 của CAN); C-295 → `transport_plane3`.
- **Không có "vũ khí cấp kèm" cho máy bay:** vũ khí là module trong variant, không phải kho đạn. E5 "8 chiếc không kèm vũ khí" / "kèm vũ khí" không có hiệu ứng nào nếu chỉ cấp thiết bị (xem B3).

## A5 · Cách chạy sự kiện không theo kiến trúc đã dùng trong mod

Mục 5.1 mô tả "thử lại hằng tháng, hết cửa sổ thì lỡ hẹn" và 5.3 có sự kiện ẩn giao hàng và 4 sự kiện Funding Gate. Mod đã có hai tiền lệ (p13/p14 lục quân, naval) và review hải quân đã sửa đúng các lỗi này:

| Báo cáo 1.2 | Mod / review hải quân | Sửa |
|---|---|---|
| Hết cửa sổ ⇒ "lỡ hẹn" | Class B: popup chỉ bị `VIE_popup_cd` chặn tới hết cửa sổ ⇒ **áp dụng kết quả lịch sử im lặng** (`VIE_fb_*`); `_missed` chỉ khi **cổng không bao giờ đạt** | Theo mod (naval B5) |
| Không nhắc `VIE_catch_up` | Mọi scheduler có nhánh catch-up (nội chiến xong, người thắng chỉ nhận cờ "đã xảy ra", không popup, không máy bay); `VIE_catch_up_schedule` (`VIE_md_effects_p3.txt:15`) phải gọi scheduler mới | Thêm |
| Không nhắc `on_monthly_VIE` | Dùng `on_monthly` chung với `original_tag = VIE`, vì người thắng nội chiến có thể là tag nổi loạn; MD đã có `on_monthly_VIE` riêng (bắn `vietnam.1`) | Theo mod |
| `vie_air.50` sự kiện ẩn giao hàng, `vie_air.51` lỡ hẹn | Giao hàng là **Class C** trong scheduler, một cờ cho mỗi đợt (`VIE_ap_<p>_dN`), không event | Bỏ `.50`; `.51` thành thông báo nhỏ |
| Funding Gate cho cả 17 sự kiện (`.40–.43`) | Lựa chọn lịch sử **luôn có** (R1); MD tự phát hành nợ khi thiếu tiền; Funding Gate chỉ ở lựa chọn *ngoài lịch sử* (Sigma). Ngân khố VIE lúc đầu là 5 tỷ, nên chi 1,0 tỷ cho E6 là hợp lệ | Bỏ `.40–.43`; chỉ lựa chọn "mở rộng" mới có `trigger` ngân khố, tooltip rõ (xem 3.3) |

---

# PHẦN 2 — 7 CHỖ KHÔNG KHỚP GAME/MOD

## B1 · Bước ngoặt vòng phụ thuộc: E7 và E17 đọc ngược chiều R11

R11 của báo cáo: Trục 1 → Trục 2 → {Trục 3, 1B}; cạnh ngược chỉ được **cộng thưởng**, không gate. Nhưng:
- **E7 lựa chọn C** ("để A31 tự làm") đòi `VIE_var_a31_tier ≥ 1`, trong khi A31 bậc 1 của Trục 2 *chính là* "Pechora-2TM (2009–2011)" (6.3). Vừa vòng, vừa trả hai lần cho một sự kiện lịch sử.
- **E17** đọc `VIE_var_a32_tier = 3` để *không kích hoạt*: Trục 1 gate bằng trạng thái Trục 2 (ngược chiều), và nguồn là [~] (tin Nga ngần ngại), trái R1 ("Trục 1 chỉ chứa việc đã xảy ra").
**Sửa:** E7 bỏ lựa chọn C; Trục 2 A31 bậc 1 sau này *đọc* cờ kết quả `VIE_ap_pechora_scope` để giảm giá/thời gian (cạnh thưởng hợp lệ). **E17 chuyển sang 1B** (Decision, cạnh tranh nguồn hỗ trợ Nga/phương Tây), không còn thuộc Trục 1 (Phần 6, Q-A2). Trục 1 còn **16 sự kiện**.

## B2 · Exp cộng vào Trục 2 chưa có người đọc

E7 (exp A31 +25/+40), E11-C (exp radar +30), E17-B (exp A32 +40) ghi vào một biến "exp" mà Trục 2 chưa có; đó đúng là loại biến phản chiếu mà R3 cấm. Mục 5.1 gợi ý "helper kiểu `VIE_nav_add_*_exp`": các helper này có thật (`VIE_md_effects_nav_ind.txt:34-51`) nhưng là của Trục 2 *hải quân*; Trục 2 không quân chưa tồn tại nên không có nơi nhận.
**Sửa:** Trục 1 **không ghi exp**. Nó ghi *cờ kết quả* (`VIE_ap_pechora_scope` 1/2, `VIE_ap_radar_viettel_fast`), Trục 2 đọc khi dựng. Trong khi chờ, các cờ này nằm trong danh sách "đặt trước, chưa ai đọc" trong `VIE_v9_flag_mapping.md` (mẫu của `VIE_cap_ba_son_yard` ở hải quân).

## B3 · Bốn sự kiện có nội dung game không thể hiện được

| Sự kiện | Vấn đề | Cách làm trong game |
|---|---|---|
| E5 "không kèm vũ khí / kèm vũ khí" | Không có kho đạn máy bay | A (lịch sử): cờ `VIE_ap_su30_no_munitions` + timed idea −X% hiệu suất nhiệm vụ tới khi E6 chốt; B: +0,12 tỷ, không idea |
| E12 MiG-21 nghỉ hưu | `destroy_equipment` chưa được xác minh ở MD (0 lần dùng), mod cũng từ chối dùng (`VIE_md_effects_p14.txt:95-103`); MiG-21 của VIE nằm trong air wing | Không loại thiết bị. Chỉ gỡ timed idea của E1, thêm hiệu ứng XP/chi phí; cấp quyền Trục 3 đọc cờ |
| E4 Yak-52 | Không có thiết bị tiêm kích huấn luyện cơ bản trong MD | Chỉ XP + timed idea đào tạo cơ bản; bỏ "cấp trang bị huấn luyện" |
| E11 VERA-NG ×4 | Helper `one_state_radar_station` tự trừ **1,75 tỷ mỗi trạm** (đặt `skip_payment = 1` để bỏ), gấp ~30 lần giá 0,06 của báo cáo | Chỉ cộng `VIE_af_air_detection` (modifier); không xây công trình radar trong Trục 1 |

## B4 · E14 và E16 cùng mua L-39NG

E14-B "L-39NG ×12, 0,12" và E16-A "L-39NG ×12, 0,12" là cùng một đơn hàng; chọn B rồi A ra 24 chiếc; chọn C (cả hai) cũng vậy. Lịch sử: L-39NG chỉ đặt một lần (2021, 12 chiếc), còn Yak-130 là [~] (chưa xác nhận hợp đồng/giao).
**Sửa:** E14 chỉ còn **Yak-130** (A mua 12 / B từ chối / C hoãn); L-39NG chỉ ở E16. Lựa chọn E14-B đặt `VIE_ap_yak130_declined`; E16 khi có cờ này có thêm tùy chọn mở rộng 18 chiếc (Funding Gate nhỏ). Tổng chi bỏ 0,12 trùng.

## B5 · Ngân sách pop-up viết sai

Mục 5.4: "17 sự kiện, dưới 1 pop-up mỗi năm… cao điểm 2009–2013 đúng ngân sách". Số đo của repo (`tools/TESTING.md`, "Balance sanity"): **các năm đã vượt 5 trước khi thêm không quân: 2003=6, 2008=6, 2012=8, 2014=8, 2018=6, 2020=6, 2021=12, 2022=6, 2023=6, 2024=7**, hải quân thêm vào 2003, 2006, 2009, 2011. Mục tiêu hiện hành: **≤ 7 mỗi năm**, không có code ép. Báo cáo không đọc số này.
**Sửa:** xếp lại cửa sổ (E2/E3 đầu 2004 thay 2003, E8/E9 sang 2013 thay 2012, E15 sang 2022.1 thay 2021.6), hạ E1/E4/E12/E16 xuống **Class C** (không popup). Bảng đếm theo năm ở 3.4.

## B6 · Tồn dư `vie_dip.16` chồng lên 1B P2

`events/VIE_md_p7.txt` còn event `vie_dip.16` "Ai cấp tiêm kích mới?" (Su-30SM của SOV hoặc Gripen), được mở bởi focus `VIE_fighter_replacement` đã xóa ở v9. Không ai kích hoạt nó (đã grep). Nó dùng `AS_Fighter2` cho Su-30, khác tiền lệ `MR_Fighter2` của MD (ALG, RAJ). Không chặn Trục 1; ghi chú để **1B P2 thay hẳn event này** (xóa khi làm 1B), và Q-A3 chốt loại non-BBA cho Su-30.

## B7 · Cạnh ngược E15 tham chiếu focus chưa có

E15 giảm giá nếu `has_completed_focus = VIE_airf_training_standardization`. Focus này thuộc Trục 3 (chưa tồn tại); `live.py` sẽ báo tham chiếu focus treo. Làm đúng mẫu naval 3.8: một scripted trigger `VIE_ap_training_standardized = { always = no }` trong file gate, đổi một dòng khi Trục 3 có focus thật.

---

# PHẦN 3 — TRỤC 1 SAU KHI SỬA

## 3.1 Quy ước (thay cho 5.1 cũ; bản 1.3 của báo cáo đã cập nhật)

- Scheduler `VIE_event_scheduler_air_proc`, gọi từ `on_monthly` (khối có `original_tag = VIE`) **và** `VIE_catch_up_schedule`. Mẫu p13/naval:

```
catch-up                         -> chỉ đặt cờ "đã xảy ra", không popup, không máy bay
cổng đạt + popup_cd trống        -> đặt _offered + popup_cd 45 ngày + fire event
cổng đạt + popup_cd bận          -> đặt _gate_seen, thử lại tháng sau
hết cửa sổ + _gate_seen          -> VIE_fb_ap_<p> (kết quả lịch sử, im lặng)
hết cửa sổ, cổng chưa từng đạt   -> _missed (tin nhắn nhỏ, 1B đọc cờ)
Class C (E4, E12, E16)           -> áp dụng thẳng kết quả lịch sử khi vào cửa sổ, không popup
giao hàng                        -> Class C, cờ VIE_ap_<p>_dN mỗi đợt
```

- Cổng đối tác chỉ gồm `country_exists` và `NOT = { has_war_with }` (R1), gom vào file triggers: `VIE_ap_gate_sov`, `_raj`, `_rom`, `_blr`, `_spr`, `_isr`, `_cze`, `_usa`.
- Tiền: `set_temp_variable = { treasury_change = -X } modify_treasury_effect = yes` (tỷ USD, như MD và Trục 1 lục quân). Từ 0,4 tỷ trở lên chia ngân khố/nợ như T-90 (`modify_debt_effect`); đề xuất: E5 0,40 / E6 1,00 / E9 0,60 trả 60% ngân khố + 40% nợ. Giá có nguồn [✓] giữ nguyên báo cáo; giá [?] ghi `TODO(giá)`.
- AI: option lịch sử là mặc định (`ai_chance`), mọi option phải chọn được (bài học zero-weight).
- Trục 1 chỉ cộng `VIE_var_air_delivered` (máy bay chiến đấu Su-30 giao) và `VIE_var_sam_lr`; không ghi bậc/exp Trục 2 (R11, B2).

## 3.2 Ánh xạ trang bị (BBA / non-BBA / GOT)

Cách viết chung: `has_dlc = "By Blood Alone"` ⇒ loại BBA + `variant_name` + `producer`; `else` ⇒ loại non-BBA (mẫu `05_algeria.txt`). Số lượng giữ 1:1 giữa hai nhánh ở bản đầu (`TODO(balance)`: MD tự lệch, ví dụ ALG Su-30 72 so với 40).

| Sự kiện | BBA (loại / variant / producer) | non-BBA | GOT | Ghi chú |
|---|---|---|---|---|
| E1 hợp tác Ấn Độ (RAJ) | — | — | — | Timed idea `VIE_ap_mig21_extension_idea` + XP; không thiết bị |
| E2 S-300PMU1 (SOV) | — | — | **có**: `set_technology` SAM1+SAM2; `sam_missile_equipment_3` ×~60/tiểu đoàn, `producer = SOV`; **không**: chỉ idea | `VIE_var_sam_lr` +2 (A) / +1 (B) luôn tăng (đếm, không phụ thuộc kho); `VIE_af_air_defence_factor` +0,02 / +0,01 |
| E3, E5, E6, E9 Su-30MK2 (SOV) | `medium_plane_airframe_2`, `"Su-30"`, SOV | `AS_Fighter2` (Q-A3 đã chốt), SOV | — | `VIE_var_air_delivered` mỗi đợt; E5/E6 có idea (B3) |
| E4 Yak-52 (ROM) | — | — | — | Chỉ XP + idea |
| E7 Pechora-2TM (BLR) | — | — | **có**: tech SAM1; `sam_missile_equipment_2` ×N, `producer = BLR` | Bỏ lựa chọn C (B1); đặt `VIE_ap_pechora_scope` |
| E8 C-295M (SPR) | `large_plane_air_transport_airframe_2`, `"Airbus C-295"`, SPR | `transport_plane3`, SPR | — | |
| E10 SPYDER (ISR) | — | — | **có**: `sam_missile_equipment_2` (TODO bậc), `producer = ISR`; SPAA lục quân `SP_Anti_Air_2` **không** cấp (thuộc lục quân) | Không cộng `VIE_var_sam_lr` (chỉ S-300 tầm xa) |
| E11 radar (CZE/ISR) | — | — | — | Chỉ `VIE_af_air_detection` (B3) |
| E12 MiG-21 nghỉ hưu | — | — | — | Không loại thiết bị (B3) |
| E13 đào tạo (RAJ) | — | — | — | XP + timed idea 36 tháng |
| E14 Yak-130 (SOV) | `small_plane_strike_airframe_2`, `"Yak-130"`, SOV | `L_Strike_fighter2`, SOV | — | Đã xác nhận mua 12 chiếc (bạn xác nhận); năm hợp đồng/giao chưa rõ |
| E15 T-6C (USA) | `small_plane_strike_airframe_1`, **không có variant USA**: thử không `variant_name`; dự phòng `"Aero L-39"` CZE (T4) | `L_Strike_fighter2`, USA | — | Rủi ro T4 (dưới) |
| E16 L-39NG (CZE) | `small_plane_strike_airframe_1`, `"Aero L-39"`, CZE | `L_Strike_fighter2`, CZE | — | NG chưa có variant; dùng L-39 gần nhất, ghi `TODO(names)` |

Đối chiếu cấp thiết bị trước khi tin (T1–T4, Phần 5): variant `"Su-30"` của SOV nằm trong khối BBA của `SOV - Russia.txt`, nên `producer = SOV` chỉ chạy được khi SOV còn tồn tại; nếu SOV mất tag thì rơi về `MR_Fighter2` không variant (cổng E3/E5/E6/E9 đã đòi `country_exists = SOV`, nên không phát sinh).

## 3.3 Bảng 16 sự kiện sau khi sửa

Số tiền là tỷ USD [✓] nếu có nguồn ở báo cáo, còn lại `[?]`. Không đổi giá so với báo cáo 1.2 trừ các dòng ghi chú.

| ID | Cửa sổ (đổi so với 1.2) | Lớp | Cổng | Lựa chọn (đã sửa) | Kết quả |
|---|---|---|---|---|---|
| `.1` DCA Ấn Độ | 2000.3 – 2002.12 | B | RAJ | A đại tu + đào tạo 0,05 (lịch sử); B chỉ đào tạo 0,02; C từ chối | A: idea `VIE_ap_mig21_extension_idea` + 10 XP; B: 5 XP |
| `.2` S-300PMU1 | **2004.3** – 2006.12 | B | SOV | A 2 tiểu đoàn 0,30 (lịch sử); B 1 tiểu đoàn 0,16; C hoãn | A: `sam_lr`+2; B +1; GOT ⇒ thiết bị (3.2) |
| `.3` Su-30MK2 đợt 1 | **2004.1** – 2005.12 | B | SOV | A 4 chiếc 0,12; B 6 chiếc + chuyển loại 0,20 (giao +6 tháng, +10 XP); C hoãn | `air_delivered` +4/+6 |
| `.4` Yak-52 | 2007 – 2009 | **C** | ROM | Kết quả lịch sử: 10 chiếc, 0,02 | XP + idea đào tạo cơ bản |
| `.5` Su-30MK2 đợt 2 | 2008.6 – 2010.6 | B | SOV | A 8 chiếc không vũ khí 0,40 (lịch sử); B 8 chiếc + vũ khí 0,52; C 6 chiếc 0,30 | A đặt idea thiếu đạn tới `.6`; +8/+6 |
| `.6` Su-30MK2V đợt 3 | 2009.9 – 2011.6 | B | SOV | A 12 chiếc + vũ khí 1,00 (lịch sử, 60% ngân khố/40% nợ); B 12 chiếc chỉ thân 0,62 (idea −3% nhiệm vụ 24 tháng); C 8 chiếc 0,70 | +12/+8; gỡ idea thiếu đạn của `.5`; `T5` cần > 11 |
| `.7` Pechora-2TM | 2009 – 2012 | B | BLR | A trên 30 bệ 0,15 (lịch sử); B 15 bệ 0,08 | `VIE_ap_pechora_scope` 2/1; GOT ⇒ thiết bị (3.2). **Bỏ C** (B1) |
| `.8` C-295M | **2013.1** – 2014.12 | B | SPR | A 3 chiếc 0,10 (lịch sử); B 2 chiếc 0,07; C 4 chiếc 0,14 | Vận tải (3.2) |
| `.9` Su-30MK2 đợt 4 | **2013.6** – 2014.12 | B | SOV | A 12 chiếc 0,60 (lịch sử); B 6 chiếc 0,30 + `VIE_ap_su35_talks`; C hoãn | +12/+6 |
| `.10` SPYDER | **2015.1** – 2016.12 | B | ISR | A 5 hệ thống 0,25 (lịch sử); B 3 hệ thống + nghiên cứu Barak-8 0,18 (cờ `VIE_ap_barak_research`) | GOT ⇒ thiết bị; không cộng `sam_lr` |
| `.11` Radar cảnh giới | 2013.1 – 2015.12 | B | CZE (A), ISR (B) | A VERA-NG ×4 0,06 (lịch sử); B thêm ELM-2288 0,10; C đẩy radar Viettel 0,04 (cờ `VIE_ap_radar_viettel_fast`, phát hiện thấp hơn 24 tháng) | Chỉ `air_detection` (3.2) |
| `.12` MiG-21 nghỉ hưu | 2016.1 – 2017.12 | **C** | — | Kết quả lịch sử: giải ngũ, tiết kiệm 0,03; −3% XP không quân 24 tháng (idea) | Gỡ idea `.1` |
| `.13` Đào tạo Su-30 tại Ấn Độ | 2016.12 – 2018.12 | B | RAJ | A Ấn Độ 0,05, 10 XP (lịch sử); B Nga 0,08, 15 XP; C tự đào tạo (cần T1 Trục 3: không có thì ẩn) | Idea tăng tốc huấn luyện 36 tháng (A) |
| `.14` Yak-130 | 2017 – 2021 | B | SOV | A 12 chiếc 0,35 (đã mua 12 chiếc, lịch sử); B từ chối (`VIE_ap_yak130_declined`); C hoãn | Huấn luyện nâng cao (3.2). **Bỏ L-39NG** (B4) |
| `.15` T-6C | **2022.1** – 2024.12 | B | USA | A 12 chiếc 0,15 (lịch sử); B 6 chiếc 0,08 | Gói đào tạo 0,12 nếu `VIE_ap_training_standardized` (B7) |
| `.16` L-39NG | 2022 – 2024 | **C** | CZE | Kết quả lịch sử: 12 chiếc 0,12 (+6 chiếc 0,06 nếu `yak130_declined` và ngân khố đủ, tooltip rõ) | Huấn luyện nâng cao |

Chuyển đi: `.17` Khủng hoảng hỗ trợ Su-27/30 ⇒ 1B (B1). Tổng chi lịch sử ≈ **3,7 tỷ** (3,96 trừ E17 0,12 cộng chênh lệch E14): kiểm bằng script cân bằng (bước 7).

Lịch giao (nội suy là `TODO(nguồn)`, mẫu naval 3.2/3.3: đợt N giao tại `max(mốc lịch sử, ngày ký + lead_min)`, đợt vượt số lịch sử giao cách 6 tháng):

| Chương trình | Đợt | Ngày |
|---|---|---|
| Su-30 đợt 1 (4) | 1 | 2004.11 |
| Su-30 đợt 2 (8) | 2 đợt × 4 | 2010.12, 2011.6 (nội suy) |
| Su-30 đợt 3 (12) | 3 đợt × 4 | 2011.12, 2012.6, 2012.12 (nội suy; "xong cuối 2012") |
| Su-30 đợt 4 (12) | 3 đợt × 4 | 2014.12, 2015.8, 2016.2 (có mốc 2015.8 và đầu 2016) |
| S-300 | 2 tiểu đoàn | 2005.8 (có nguồn), 2006.12 (nội suy) |
| C-295M | 3 | 2015.3, 2015.9, 2016.3 (nội suy; "biên chế từ 2015") |
| T-6C | 2 đợt | 2024.11 (5 chiếc, có nguồn), 2026.6 (nội suy; "giao tới 2027") |
| L-39NG | 2 đợt × 6 | 2024.8, 2025.3 (có nguồn) |
| Yak-130 (12) | 2 đợt × 6 | `TODO(nguồn)`: năm giao chưa rõ; tạm 2021.6 và 2022.6 (nội suy, tìm nguồn trước bước 5) |

Hệ quả cho T5 của Trục 3: 4 + 8 = 12 sau 2011.6 ⇒ `VIE_var_air_delivered > 11` đạt trước `date > 2011.12.31` (đúng ý đồ).

## 3.4 Pop-up theo năm (ước tính, chỉ đếm Class B có title)

| Năm | Đã có (đo 30/9) | + naval | + air B | Tổng | Ghi chú |
|---|---|---|---|---|---|
| 2000 | chưa đo | — | `.1` | ? | |
| 2003 | 6 | `.1` | 0 | **7** | E2/E3 dời sang 2004 |
| 2004 | ≤ 5? | — | `.2`, `.3` | ≤ 7 | |
| 2008 | 6 | — | `.5` | **7** | |
| 2009 | ? | `.3`, `.20` | `.6`, `.7` | ? | **phải đo** |
| 2013 | ≤ 5? | — | `.8`, `.9`, `.11` | ≤ 8 | **phải đo**; hạ `.8` xuống Class C nếu vượt |
| 2015–2017 | ? | — | `.10`, `.13`, `.14` | ? | |
| 2022 | 6 | — | `.15` | **7** | |

Đòn bẩy nếu một năm vượt 7: hạ lần lượt `.8`, `.13`, `.10`, `.11` xuống Class C (áp dụng lựa chọn lịch sử im lặng). `.12`, `.4`, `.16` đã là Class C.

---

# PHẦN 4 — PLAN CODE (7 bước, mỗi bước 1 commit, nhánh `claude/air-truc1`)

Kiến trúc: scheduler riêng, gọi từ `on_monthly` và `VIE_catch_up_schedule`, không dùng `on_monthly_VIE`, không dùng `trigger_year_*`. Không đụng `VIE_event_scheduler_air` (chỉ huy).

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | báo cáo + `VIE_v9_flag_mapping.md` | Báo cáo đã sửa (bản 1.3). Thêm mục "Truc 1 khong quan" vào bảng cờ, với danh sách cờ đặt trước chưa ai đọc (`VIE_ap_pechora_scope`, `_radar_viettel_fast`, `_su35_talks`, `_barak_research`, `_yak130_declined`) | Đọc lại; grep `VIE_ap_` 0 kết quả trước khi code |
| **1** | `common/scripted_triggers/VIE_md_triggers_air_proc.txt` (mới) | Gom cổng: `VIE_ap_gate_sov/_raj/_rom/_blr/_spr/_isr/_cze/_usa`; `VIE_ap_training_standardized = { always = no }` (đã bỏ `has_bba`, `has_got`, `can_fund`: không ai gọi); comment trạng thái Q-list như p14 | `python tools/audit/live.py` sạch |
| **2** | `common/scripted_effects/VIE_md_effects_air_proc.txt` (mới) | (a) Phần thưởng dùng chung (mỗi chuỗi một effect `VIE_ap_reward_<p>_a/b/c`, dùng cho cả fallback và option, giống p14); (b) helper cấp thiết bị: `VIE_ap_give_su30`, `VIE_ap_give_sam` (có GOT), `VIE_ap_give_trainer` (BBA/non-BBA); (c) `VIE_event_scheduler_air_proc` (catch-up → cờ; popup_cd; fallback; `_missed`); (d) `VIE_ap_deliver_<p>` (Class C, cờ `_dN`); nối vào `on_monthly` **và** `VIE_catch_up_schedule` | console `effect VIE_event_scheduler_air_proc = yes` không lỗi; `effect set_variable = { VIE_catch_up = 1 }` rồi chạy: không popup, không máy bay |
| **3** | `events/VIE_air_proc.txt` (mới, `add_namespace = vie_air_proc`), `common/ideas/VIE_md_ideas_air_proc.txt` | **Lát cắt Su-30 trước** (`.3 .5 .6 .9` + giao hàng + `VIE_var_air_delivered` + idea thiếu đạn / chỉ thân máy). Đây là rủi ro lớn nhất (T1, T2) | chơi tới 2004.1: một popup `.3`; 2004.11 +4 chiếc trong kho; BBA có `"Su-30"`, non-BBA có `MR_Fighter2`; `error.log` sạch |
| **4** | cùng file | **Lát cắt SAM** (`.2 .7 .10`) với hai nhánh: có GOT (tech chuỗi + `sam_missile_equipment_N`) và không GOT (chỉ idea + modifier) | chạy hai lượt (có và không GOT): kho SAM tăng/không; tech `SAM2` có; không có "equipment does not exist" |
| **5** | cùng file | **Huấn luyện, vận tải, radar** (`.1 .4 .8 .11 .12 .13 .14 .15 .16`), hai nhánh BBA/non-BBA, các idea; E15/E16 theo T4 | chơi tới 2025: không lỗi; `.4 .12 .16` không popup |
| **6** | `localisation/english/VIE_md_events_air_proc_l_english.yml` (+ `replace/` theo mẫu repo), `tools/TESTING.md` mục "Air procurement", `tools/audit/air_proc_balance.py` | Loc có BOM; checklist mục Phần 5; script cộng chi theo năm, đếm popup/năm từ `ev.py`, in PASS khi tổng chi và popup nằm trong dải | `python tools/verify_all_loc.py` PASS; `python tools/audit/ev.py` không orphan; script PASS |
| **7** | `VIE_v9_flag_mapping.md`, báo cáo | Ghi cờ thực tế, ghi trạng thái vào cuối tài liệu này (mẫu naval) | — |

Ước lượng: 13 event Class B + 3 Class C (chỉ ở scheduler), ~700 dòng script, ~110 khóa loc, 7–8 timed idea. Không có Decision (cửa sổ lỡ hẹn chỉ đặt `_missed`, 1B tự đọc).

---

# PHẦN 5 — CHECKLIST THỬ TRONG GAME

- [ ] `error.log`: grep `vie_air_proc`, `VIE_ap_`, `equipment`, `variant`, `sam_missile`, `stockpile`, `technology`.
- [ ] **T1 (rủi ro cao nhất):** BBA — `add_equipment_to_stockpile = { type = medium_plane_airframe_2 variant_name = "Su-30" producer = SOV }` cho VIE: kho có máy bay tên "Su-30" không, có dùng được trong air wing không (VIE chưa nghiên cứu khung này).
- [ ] **T2:** non-BBA — `AS_Fighter2` có hiện trong kho (Su-27 đầu game của VIE cũng là loại này: cộng dồn đúng).
- [ ] **T3:** GOT — sau `set_technology` SAM1+SAM2 và cấp `sam_missile_equipment_3`, thiết bị có hiện ra, triển khai được không; không GOT: không có lỗi, chỉ có idea.
- [ ] **T4:** BBA — cấp `small_plane_strike_airframe_1` **không** có `variant_name` (T-6C): có tạo thiết bị mặc định không; nếu không, dùng `"Aero L-39"` producer CZE.
- [ ] Đặt `VIE_popup_cd` thủ công (`effect set_country_flag = { flag = VIE_popup_cd days = 45 }`) vào 2004.1 rồi chờ: `.3` dời sang tháng sau, không mất; giữ tới hết cửa sổ: fallback im lặng, không `_missed`.
- [ ] Cho Nga biến mất trước 2008 (console): `.5 .6 .9` đặt `_missed`, không popup; không máy bay; không lỗi.
- [ ] Chiến tranh với SOV giữa cửa sổ rồi hòa: cửa sổ còn thì offer vẫn bắn.
- [ ] Nội chiến: người thắng có cờ lịch sử, không nhận máy bay, không popup.
- [ ] Đếm popup/năm 2000–2024 (`ev.py`, rồi chơi quan sát); mục tiêu ≤ 7, ghi các năm vượt.
- [ ] `treasury` thực tế của VIE tại 2009-09 và 2013-06: chi 1,0 tỷ (E6) và 0,6 tỷ (E9) trừ đúng, nợ tăng đúng phần 40%.
- [ ] Chơi AI tới 2020: AI chọn lịch sử mọi sự kiện, tổng `VIE_var_air_delivered` = 36 vào đầu 2016.
- [ ] Chạy **hai lượt**: có BBA / không BBA; có GOT / không GOT.

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đề xuất)

| # | Câu hỏi | Mặc định |
|---|---|---|
| Q-A1 | Tiền tố/namespace Trục 1: `VIE_ap_`, `vie_air_proc`, scheduler `VIE_event_scheduler_air_proc` (A2) | **Theo đề xuất** |
| Q-A2 | E17 (khủng hoảng hỗ trợ Su-27/30) chuyển sang 1B (B1) | **ĐÃ CHỐT: chuyển** |
| Q-A3 | Loại non-BBA cho Su-30MK2: `MR_Fighter2` (RAJ/ALG) hay `AS_Fighter2` (CHI, `vie_dip.16`) | **ĐÃ CHỐT: `AS_Fighter2`** |
| Q-A4 | Funding Gate chỉ cho lựa chọn "mở rộng", không cho lịch sử (A5) | **Có** |
| Q-A5 | Hạ E4, E12, E16 xuống Class C (im lặng) để giữ ngân sách pop-up (B5) | **Có** |
| Q-A6 | E14 (Yak-130, [~]) vẫn nằm ở Trục 1 hay chuyển hẳn sang 1B P1 | **ĐÃ CHỐT: giữ ở Trục 1, Yak-130 đã mua 12 chiếc** (bỏ nhãn [~]; 1B P1 chỉ còn Yak-130M/L-39/FA-50/M-346 bổ sung) |
| Q-A7 | Q15 mở rộng: nhánh không-GOT chỉ còn timed idea + modifier cho E2/E7/E10 (A3) | **Có** |
| Q-A8 | E5 mô tả "vũ khí" bằng idea thiếu đạn (B3) thay vì bỏ lựa chọn này | Giữ lựa chọn bằng idea |

---

# TRẠNG THÁI

Phân tích và sửa báo cáo xong (2026-10-02). **Chưa có dòng code nào.** Bước 0 trong Phần 4 đã làm (báo cáo bản 1.3); bước 1–7 chờ bạn chốt Phần 6.

---

# TIẾN ĐỘ CODE (2026-10-02)

Bước 1–7 đã code/ghi tài liệu, chưa chạy game, chưa commit: trigger cổng, scheduler + template, Su-30 (`.3 .5 .6 .9`), SAM (`.2 .7 .10`), huấn luyện/vận tải/radar (`.1 .8 .11 .13 .14 .15` + Class C `yak52`, `mig21_retire`, `l39ng`).
Thay đổi so với plan khi code:
- L-39NG (Class C, không popup) không có "tùy chọn mở rộng": nếu `VIE_ap_yak130_declined` và `treasury > 0,3` thì tự động đặt 18 chiếc 0,18, ngược lại 12 chiếc 0,12.
- E11 A đòi `VIE_ap_gate_cze`; khi Séc không tồn tại, AI chọn được C (không bị zero-weight).
- `VIE_var_sam_lr` chỉ cộng theo tiểu đoàn S-300.
Bước 6: `tools/audit/air_proc_balance.py` (ALL PASS; tổng chi lịch sử 3,69 tỷ) và mục "Air procurement" trong `tools/TESTING.md`. Bước 7: bảng cờ trong `VIE_v9_flag_mapping.md` (mục "Truc 1 khong quan"). Còn lại: thử trong game theo TESTING.md (T0–T4), rồi commit. Cờ đặt trước chưa ai đọc: `VIE_ap_pechora_scope`, `VIE_ap_radar_viettel_fast`, `VIE_ap_su35_talks`, `VIE_ap_barak_research`, `VIE_ap_yak130_declined` (E16 đọc).

## Đợt sửa sau review (2026-10-02)
1. Idea thiếu đạn (E5): chỉ thêm khi E6 chưa ký; gỡ khi E6 `_missed`.
2. Lead time: cờ `VIE_ap_<p>_lead` đặt lúc ký (150–480 ngày), mọi đợt giao đòi hết cờ.
3. Su-30 khi SOV đã mất tag: cấp loại mặc định không `producer` (không variant).
4. Helper `VIE_ap_ensure_af_modifier`: gắn `VIE_armed_forces_modifier` nếu chưa có (trước đó chỉ focus `VIE_modernize_vpa` gắn).
5. Ảnh hưởng bên bán: `VIE_ap_seller_influence` (1% mỗi hợp đồng, mẫu focus Algeria của MD).
6. Dọn convention MD: bỏ cờ `_contracted` (dùng `qty > 0`), bỏ 3 trigger không dùng, idea theo kiểu MD (không `allowed`, `allowed_civil_war = yes`), bỏ log ở option không hiệu ứng.
