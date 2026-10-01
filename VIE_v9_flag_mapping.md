# BẢNG CỜ `VIE_ev_*` VÀ HỢP ĐỒNG TÍCH HỢP TRỤC 1

> **Tài liệu này phục hồi file đã mất.** Header v9 trong `common/national_focus/VIE_md_focus.txt`
> ghi *"Event mua sam BAT BUOC set cac co nay (xem `VIE_v9_flag_mapping.md`)"*, nhưng
> `git log --all --diff-filter=A` trên cả ba nhánh xác nhận file **chưa từng được commit**.
> `v9_removed_focuses_for_events.txt` cũng vậy.
>
> Bối cảnh: v9 (28/09/2026) xoá 21 focus mua sắm vũ khí và đổi **19 gate** `has_completed_focus`
> ở 12 focus còn sống thành `has_country_flag = VIE_ev_<slug>`, với điều kiện các event mua sắm
> phải set cờ thay thế. Commit `f05cfa1` (30/09/2026) sau đó **xoá sạch** `events/VIE_md_mil.txt`
> (300 dòng → 1 dòng comment) nên không còn event nào set cờ.
>
> Cập nhật cho Trục 1 (bước 1, nhánh `truc1-skeleton`).

---

## 1. Cờ `VIE_ev_*` — trạng thái sau bước 1

| Cờ | Set bởi | Đọc bởi | Trạng thái |
|---|---|---|---|
| `VIE_ev_t90_tanks` | `VIE_proc_reward_t90_in_service` (từ `vie_proc_army.15`) | *chưa có focus live nào đọc* | ✅ **đã nối lại**, sẵn sàng cho focus dùng |
| `VIE_ev_kilo_submarines` | — | `VIE_paracel_ultimatum` (`VIE_md_focus.txt:1123`) | 🚩 **VẪN ORPHAN** — xem mục 3 |
| `VIE_ev_bastion_p_coastal_defence` | — | `VIE_paracel_ultimatum` (`VIE_md_focus.txt:1124`) | 🚩 **VẪN ORPHAN** — xem mục 3 |

16 gate `VIE_ev_*` còn lại mà v9 tạo ra nằm trong các focus **đã bị v11 xoá**
(`v11_removed_military_all_subbranches.txt:1819, 1820, 1841, 1842, 2296`). Chúng không còn
trong cây live nên không cần cờ tương ứng nữa.

Kiểm tra lại bằng:
```bash
python3 tools/verify_all_loc.py          # loc + focus
grep -rn "VIE_ev_" common/ events/ --include=*.txt | grep -v '\.bak'
```

---

## 2. Cờ Trục 1 (mua sắm lục quân)

### 2.1 Cờ điều khiển chuỗi — scheduler đọc

| Cờ | Đặt bởi | Ý nghĩa |
|---|---|---|
| `VIE_proc_1_done` | scheduler / `VIE_proc_catch_up` | chuỗi 1 đã fire hoặc đã fallback |
| `VIE_proc_2_done` | như trên | chuỗi 1b (T-72 Ba Lan) |
| `VIE_proc_5_done` | như trên | chuỗi 2 (T-54M3) |
| `VIE_proc_8_done` | như trên | chuỗi 3 (Igla) |
| `VIE_proc_11_done` | như trên | chuỗi 4 (Galil ACE) |
| `VIE_proc_14_done` | như trên | chuỗi 5 (T-90) |
| `VIE_proc_18_done` | như trên | chuỗi 6 (K9A1) |
| `VIE_proc_30_done` | như trên | chuỗi 7 (BMP-3, alt) |
| `VIE_proc_35_done` | như trên | chuỗi 8 (TOS-1A, alt) |
| `VIE_proc_38_done` | như trên | chuỗi 9 (CAESAR, alt) |

**Quy tắc quan trọng:** cờ `VIE_proc_N_done` chỉ được đặt khi event **thực sự fire**
(nhánh `NOT = { has_country_flag = VIE_popup_cd }`) hoặc khi **đã fallback im lặng**
(nhánh quá hạn cứng). Nếu `VIE_popup_cd` đang bận và chưa quá hạn thì **không đặt cờ** —
đó chính là cơ chế thử lại: tick `on_monthly` kế tiếp chạy lại khối ấy.

Báo cáo mục 1.6 đặt cờ *"ngay khi gọi event"* trong `VIE_try_proc_N`. Cách đó **làm mất chuỗi
vĩnh viễn**: `trigger` của event **có** chặn event bắn bằng `country_event` (HOI4 wiki,
*Event modding* → *Effect*: "`trigger = {...}` of the event gets checked **when it would fire**"),
nên nếu điều kiện đổi trong khoảng delay `days = 1..15` thì event không nổ mà cờ đã đặt →
không có đường thử lại, không log, không dấu vết.

### 2.2 Cờ kết quả — Trục 2 và các nhánh khác đọc

| Cờ | Đặt bởi | Đọc bởi | Nếu chuỗi mất (hết cửa sổ) |
|---|---|---|---|
| `VIE_pl_t72_deal` | `vie_proc_army.1` option A | `VIE_event_scheduler_p14` (mở chuỗi 2) | không đặt → chuỗi 2 không bao giờ chạy |
| `VIE_t54m3_prototype` | `VIE_proc_reward_t54m3_prototype` | **D5** T-54M nội địa (Trục 2) | D5 khoá |
| `VIE_igla_license` | `VIE_proc_reward_igla_license` | **D9** TL-01 (Trục 2) | D9 khoá |
| `VIE_iwi_license` | `VIE_proc_reward_iwi_license` | **D2** STV: `days_remove` 730 thay vì 1095 | D2 vẫn mở, bản 1095 ngày |
| `VIE_t90_batch_large` | `VIE_proc_reward_t90_128` (option B) | `VIE_proc_deliver_t90_batch` (64/đợt thay vì 32) | — |
| `VIE_t90_purchased` | `VIE_proc_reward_t90_in_service` | **`vie_def_ind.2`** chuyển giao bảo dưỡng T-90 | event đó không nổ |
| `VIE_ev_t90_tanks` | như trên | hợp đồng v9 (focus `VIE_ev_*`) | — |
| `VIE_k9_batch_large` | `VIE_proc_reward_k9_40` (option B) | `VIE_proc_deliver_k9` (40 thay vì 20) | — |
| `VIE_k9_purchased` | `VIE_proc_deliver_k9` | **D8** nội địa hoá K9 (Trục 2) | D8 khoá |
| `VIE_k9_localization` | `vie_proc_army.21` option A | **D8** (Trục 2) | D8 khoá |
| `VIE_bmp3_lessons` | `vie_proc_army.32` option A (alt) | **D6** XCB-01: `days_remove` 1095 thay vì 1460 | D6 bản 1460 ngày |
| `VIE_155mm_study` | `vie_proc_army.40` (alt) | `VIE_proc_gate_k9_early` → chuỗi 6 mở từ 2021, `.19` sau 365 ngày | chuỗi 6 mở 2023, `.19` sau 900 ngày |

### 2.2b ✅ Đã trả nợ (Trục 2 bước 3–6): 6/7 cờ Trục 1 giờ CÓ người đọc

Cập nhật 2026-09-30 sau khi Trục 2 code xong D1–D9:

| Cờ | Ai đọc | Trạng thái |
|---|---|---|
| `VIE_t54m3_prototype` | **D5** `VIE_dec_t54m` (`visible` + `available`) | ✅ đã nối |
| `VIE_igla_license` | **D9** `VIE_dec_tl01` | ✅ đã nối |
| `VIE_iwi_license` | **D2** — chọn giữa `VIE_dec_stv` (1095 ngày) và `VIE_dec_stv_fast` (730) | ✅ đã nối |
| `VIE_bmp3_lessons` | **D6** — chọn giữa `VIE_dec_xcb01` (1460) và `_fast` (1095) | ✅ đã nối |
| `VIE_k9_purchased` | **D8** `VIE_dec_k9_localization` | ✅ đã nối |
| `VIE_k9_localization` | **D8** | ✅ đã nối |
| `VIE_ev_t90_tanks` | — | ⏳ **vẫn chưa ai đọc** — chờ Trục 1b / trục Hải quân (Q1 = d) |

**Đừng xoá `VIE_ev_t90_tanks`.** Nó là một nửa còn lại của hợp đồng v9; nửa kia
(`VIE_ev_kilo_submarines`, `VIE_ev_bastion_p_coastal_defence`) thuộc trục Hải quân.

### 2.2c (bản gốc, giữ để đối chiếu) Sáu cờ Trục 1 ĐẶT nhưng chưa ai ĐỌC

Đo lại ngày 2026-09-30 sau bước 6:

| Cờ | Đặt bởi | Ai **sẽ** đọc (Trục 2, chưa code) |
|---|---|---|
| `VIE_t54m3_prototype` | `.5` option A / fallback | **D5** T-54M nội địa — điều kiện bắt buộc |
| `VIE_igla_license` | `.8` option A / fallback | **D9** TL-01 — điều kiện bắt buộc |
| `VIE_iwi_license` | `.11` option A / fallback | **D2** STV — `days_remove` 730 thay vì 1095 |
| `VIE_k9_purchased` | `.20` immediate | **D8** nội địa hóa K9 — điều kiện bắt buộc |
| `VIE_k9_localization` | `.21` option A | **D8** — điều kiện bắt buộc (cùng `VIE_k9_purchased`) |
| `VIE_bmp3_lessons` | `.32` option A (alt) | **D6** XCB-01 — `days_remove` 1095 thay vì 1460 |
| `VIE_ev_t90_tanks` | `.15` immediate | hợp đồng v9 — focus `VIE_ev_*` (hiện chưa focus live nào đọc) |

**Đừng xoá những cờ này khi dọn cờ chết.** Chúng đã được đặt đúng chỗ và đúng lúc;
phần còn thiếu nằm ở Trục 2. Khi code D2/D5/D6/D8/D9 thì nối vào là xong.

Ngược lại, các cờ sau **đã có người đọc** nên không cần lo:
`VIE_pl_t72_deal` (scheduler mở chuỗi 2), `VIE_t90_batch_large` / `VIE_k9_batch_large`
(delivery chọn 32/64 và 20/40), `VIE_t90_purchased` (guard chống cộng dồn modifier),
`VIE_t54m_variant` (guard chống tạo variant trùng), `VIE_k9_declined` (`trigger` của `.19`),
`VIE_155mm_study` (gate mở sớm chuỗi K9).

### 2.3 Cờ dùng chung với toàn mod

| Cờ | Ý nghĩa |
|---|---|
| `VIE_popup_cd` (45 ngày) | chống hai pop-up sát nhau. Scheduler p1–p14 đều tôn trọng. Xem `VIE_md_effects.txt:225-231` |
| `VIE_catch_up` (temp variable) | người thắng nội chiến tiếp quản dòng VIE: chỉ đặt cờ, không cấp tiền/xe. `VIE_proc_catch_up` xử lý |
| `VIE_ax_initialized` | không liên quan Trục 1, ghi ở đây để khỏi nhầm với các cờ `VIE_proc_*` |

---

## 3. `VIE_paracel_ultimatum` — soft-lock, ĐÃ CHỐT GIỮ NGUYÊN (Q1 = d)

**Quyết định 2026-09-30: Q1 = (d). Không sửa.** Focus này khoá cho tới khi có trục
Hải quân cấp hai cờ dưới đây. Đây là tình trạng **có ý**, không phải lỗi mới phát sinh —
đừng "sửa" nó bằng cách nối `VIE_proc_gate_paracel_capable` vào focus hay bỏ khối `OR`.

`common/national_focus/VIE_md_focus.txt:1117-1125`:
```pdx
available = {
    VIE_scs_escalated_trigger = yes
    country_exists = CHI
    NOT = { has_war_with = CHI }
    NOT = { has_idea = VIE_peoples_war_idea }
    OR = {
        has_country_flag = VIE_ev_kilo_submarines
        has_country_flag = VIE_ev_bastion_p_coastal_defence
    }
}
```

Cả hai cờ là **hải quân / phòng thủ bờ**. Trục 1 là **lục quân** nên không cấp được.

Bốn phương án đã đưa ra:

| Phương án | Việc phải làm | Trạng thái |
|---|---|---|
| (a) bỏ khối `OR` | xoá 4 dòng `OR { ... }` trong focus; xoá trigger | không chọn |
| (b) đổi sang cờ Trục 1 | thay bằng `has_country_flag = VIE_t90_purchased` — sai ngữ cảnh | không chọn |
| (c) thêm Trục 1b hải quân | viết 2 event ở `.50`–`.59` set hai cờ trên | không chọn **bây giờ** |
| **(d) để nguyên** | không sửa gì; focus khoá tới khi có trục Hải quân | ✅ **ĐÃ CHỌN** |

Việc cần làm khi nào bắt tay vào trục Hải quân (phương án (c) về bản chất):
viết 2 event ở ID `.50`–`.59` — khoảng này **đã dành sẵn** trong
`events/VIE_proc_army.txt` — set `VIE_ev_kilo_submarines` và
`VIE_ev_bastion_p_coastal_defence`. Focus tự mở, không cần sửa gì thêm.
`VIE_proc_gate_paracel_capable` trong `common/scripted_triggers/VIE_md_triggers_p14.txt`
được giữ làm chỗ tập trung cho việc đó.

---

## 4. Bảng cửa sổ thời gian (đã hiện thực trong `VIE_md_effects_p14.txt`)

| Chuỗi | Event | Mở khi | Hạn cứng (fallback im lặng) | Fallback |
|---|---|---|---|---|
| 1 | `.1` | `date > 2004.12.31` | `date > 2005.12.31` | `VIE_proc_reward_t54_finland` |
| 1b | `.2` | có `VIE_pl_t72_deal` | `date > 2007.6.30` | +10 navy XP, +10 air XP (đúng lịch sử: huỷ) |
| 2 | `.5` | `date > 2008.12.31` | `date > 2012.12.31` | `VIE_fb_proc_t54m3` → option A |
| 3 | `.8` | `date > 2008.12.31` | `date > 2013.12.31` | `VIE_fb_proc_igla` → option A |
| 4 | `.11` | `date > 2012.12.31` | `date > 2015.12.31` | `VIE_fb_proc_galil` → option A |
| 5 | `.14` | `date > 2015.12.31` | `date > 2018.12.31` | `VIE_fb_proc_t90` → option A |
| 6 | `.18` | `date > 2022.12.31`, hoặc `> 2020.12.31` nếu có `VIE_155mm_study` | `date > 2026.12.31` | `VIE_fb_proc_k9` → option A |
| 7 | `.30` | `date > 2009.12.31` + rule bật | `date > 2011.12.31` | `VIE_fb_proc_alt_none` |
| 8 | `.35` | `date > 2015.12.31` + rule bật | `date > 2017.12.31` | `VIE_fb_proc_alt_none` |
| 9 | `.38` | `date > 2014.12.31` + rule bật | `date > 2016.12.31` | `VIE_fb_proc_alt_none` |

Ba chuỗi alt-history **không có fallback nội dung**: hết cửa sổ thì đóng, không áp kết quả nào.

---

## 5. Ngân sách pop-up sau khi thêm Trục 1

Luật của mod (`tools/TESTING.md`, *Balance sanity*): *"never two within 30 days (except chained
events), at most 5 in any calendar year"*. `VIE_popup_cd` 45 ngày là cơ chế thực thi, và
scheduler p14 tôn trọng nó — nên **hai pop-up Trục 1 không bao giờ sát nhau**.

Nhưng tổng theo năm thì vượt luật ở vài năm:

| Năm | Có sẵn (p1–p13) | + Trục 1 | Tổng | Bật rule alt |
|---|---:|---:|---:|---:|
| 2005 | 3 | +1 (`.1`) | 4 | |
| 2006 | 4 | +1 (`.2`) | **5** ⚠️ đúng mức | |
| 2009 | 2 | +2 (`.5`, `.8`) | 4 | |
| 2010 | 3 | — | 3 | **+3 = 6** ❌ |
| 2013 | 3 | +1 (`.11`) | 4 | |
| 2015 | 3 | — | 3 | **+2 = 5** ⚠️ |
| 2016 | 5 | +1 (`.14`) | **6** ❌ | **+1 = 7** ❌ |
| 2018 | 6 | +1 (`.15`) | **7** ❌ | |
| 2019 | 5 | +1 (`.16`) | **6** ❌ | |
| 2023 | 6 | +1 (`.18`) | **7** ❌ | |
| 2025 | 3 | +1 (`.19`) | 4 | |
| 2026 | 2 | +1 (`.20`) | 3 | |
| 2027 | 0 | +1 (`.21`) | 1 | |

`.15`/`.16`/`.20` là class C (im lặng, `hidden = yes`) nên **không chiếm ngân sách pop-up** —
bảng trên tính chúng là pop-up cho tới khi bước 5–6 quyết định có cho hiện cửa sổ hay không.
Nếu giữ `.15`/`.16`/`.20` im lặng thì 2018 → 6, 2019 → 5, 2026 → 2. **Còn Q5 chưa chốt.**

(2021 hiện đã là 12 — nợ cũ của mod, không phải của Trục 1.)
