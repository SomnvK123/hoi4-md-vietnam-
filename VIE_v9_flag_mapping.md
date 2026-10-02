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

## Cờ hải quân đã chết (bước 0 Trục 1 hải quân, 2026-10-02)

`VIE_event_scheduler_p12` (giao Gepard/Kilo) đã bị gỡ cùng `VIE_md_effects_p12.txt`. Các cờ
`VIE_gepard_contract`, `VIE_kilo_contract`, `VIE_gepard_b1/b2`, `VIE_kilo_b1..b6` không còn chỗ đọc
lẫn chỗ đặt. Giữ `VIE_kilo_flotilla_idea` (idea + loc), Trục 1 hải quân sẽ đặt lại khi đủ 6 tàu.
Hai cờ `VIE_ev_kilo_submarines` và `VIE_ev_bastion_p_coastal_defence` vẫn do trục Hải quân đặt
(xem `VIE_naval_truc1_review_and_plan.md` mục 3.7).

## Truc 1 hai quan (namespace vie_naval) - bang co

Thiet ke: `VIE_naval_truc1_review_and_plan.md`. Code: `VIE_md_effects_naval*.txt`, `events/VIE_naval.txt`,
`VIE_md_naval_decisions.txt`. Moi chuong trinh `<p>` thuoc {`molniya_p1`, `molniya_p2`, `gepard1`, `gepard2`, `kilo`, `bastion`, `sigma`}.

### Co chuyen tien (dat boi scheduler hoac event)
| Co | Dat boi | Doc boi |
|---|---|---|
| `VIE_<p>_offered` | scheduler khi ban event (hoac fallback), catch-up | scheduler (chan ban lai) |
| `VIE_<p>_gate_seen` | scheduler khi cong dat nhung `VIE_popup_cd` ban | scheduler (het cua so -> fallback im lang) |
| `VIE_<p>_missed` | scheduler het cua so khi cong khong tung dat; event chon "hoan" | category + Decision `VIE_naval_late_*` |
| `VIE_<p>_contracted` | `VIE_naval_contract_*` / reward Molniya | giao hang, Trục 2, Decision (an) |
| `VIE_<p>_cancelled` | `.12` C, `.40` C, `.43` D | Decision (an) |
| `VIE_<p>_late` | Decision `VIE_naval_late_*` | pay effect + `VIE_naval_late_start_*`, Sigma +25% |
| `VIE_sigma_historical` | `.40` A | `VIE_naval_sigma_review` |
| `VIE_sigma_suspended` | `VIE_fb_naval_sigma` / review `.44` | Decision `VIE_naval_late_sigma` |
| `VIE_sigma_use_debt` | `.43` B | `VIE_naval_contract_sigma` |
| `VIE_kilo_training_full` | `.21` A / fallback | giao hang cham, XP, idea doi tau ngam |

### Co giao hang (Class C, im lang, mot co moi tau)
`VIE_molniya_s1..s4` (pha 1), `VIE_molniya_v1..v10` (pha 2), `VIE_gepard1_s1..s4`, `VIE_gepard2_s1..s4`,
`VIE_kilo_s1..s8`, `VIE_bastion_s1..s4`. Ky muon (`_late`) dat het cac co nay truoc de chan giao theo ngay.
Sigma khong co co giao hang: chuoi su kien an `.45`.

### Co dau ra cho nhanh khac
| Co / bien | Dat khi | Doc boi |
|---|---|---|
| `VIE_ev_kilo_submarines` | tau Kilo dau tien giao | `VIE_paracel_ultimatum` (Q1 = d, muc 3 ben tren) |
| `VIE_ev_bastion_p_coastal_defence` | he thong Bastion dau tien giao | `VIE_paracel_ultimatum` |
| `VIE_opp_sub_mro` | giao du so Kilo da dat | Truc 2 Decision 2 (co hoi MRO, chua phai nang luc) |
| `VIE_ext_naval_missile` | giao du Bastion da dat | Truc 2 Focus 5 / Decision 4 (nguon tuy chon) |
| `VIE_molniya_domestic_started` | 2010-06 sau khi ky pha 2 | Truc 2 Decision 3 bac 3 |
| `VIE_var_hulls_delivered` | +1 moi than tau giao (Molniya, Gepard, Kilo, Sigma, 1B; **khong** tinh Bastion-P, he thong bo) | Truc 2 Focus 3 (>= 4), Truc 3 T6 |
| `VIE_var_shipbuilding_exp` | Molniya pha 2: +3 moi tau | Truc 2 Decision 5 |
| `VIE_var_integration_exp` | Sigma Domestic +8 / Hybrid +4 khi giao du | Truc 2 Decision 4/5 |

### Co do Truc 2 phai dat (Truc 1 hai quan chi doc)
`VIE_cap_ba_son_yard` (Molniya pha 2), `VIE_var_ba_son_tier` (>= 2 mo 8 va 10 tau). Chua co ai dat: dung console de thu.

### Bien so luong
`VIE_molniya_ru_qty`, `VIE_molniya_ru_delivered`, `VIE_molniya_vn_qty_ordered`, `VIE_molniya_vn_qty_delivered`,
`VIE_<gepard1|gepard2|kilo|bastion|sigma>_qty_ordered`, `_qty_delivered`;
`VIE_gepard1_config` (1 tieu chuan, 2 ASW), `VIE_bastion_deploy` (1 Bac, 2 Trung, 3 Nam, 4 phan tan), `VIE_bastion_site`
(tam), `VIE_sigma_config` (1 Full Western, 2 Hybrid, 3 Noi dia).

### Da bo so voi bao cao
`VIE_<p>_complete` (= `qty_delivered = qty_ordered`), `VIE_var_naval_budget_room` (dung thang bien `treasury`),
cac bien `_progress`, config Gepard 3 (phong khong), `VIE_gepard_contract` / `VIE_kilo_contract` (p12 cu).

## Truc 2 hai quan (namespace vie_nav_ind) - bang co va bien

Thiet ke: `VIE_naval_truc2_review_and_plan.md`. Code: `VIE_md_effects_nav_ind.txt`, `events/VIE_nav_ind.txt`,
`VIE_md_nav_ind_decisions.txt`, 6 focus `VIE_naval_defence_law` ... `VIE_naval_defence_2030`.

### Co
| Co | Dat boi | Doc boi |
|---|---|---|
| `VIE_cap_ba_son_yard` | `vie_nav_ind.60` (moc 40% cua D1) | **Truc 1:** `VIE_naval_sched_molniya_p2` (cua so pha 2), Decision `VIE_naval_late_molniya`; D3 |
| `VIE_cap_mature_naval_industry` | `VIE_nav_d5_finish` | Truc 1B: hybrid cua P10 va P11 (`VIE_md_effects_p1b.txt`, sinh boi `tools/gen_p1b.py`) |
| `VIE_mro_russia_dependent` | `vie_nav_ind.11` A | `VIE_nav_add_mro_exp` (tran 50) |
| `VIE_nav_d1_done`, `_d2_done`, `_d3_done`, `_d4_done` | `VIE_nav_dN_finish` | D2 bac 2-3, D5 uu tien |

### Bien (so luong that, khong phan chieu)
| Bien | Khoang | Dat / cong boi | Doc boi |
|---|---|---|---|
| `VIE_var_shipbuilding_exp` | 0-100 | D1 (dinh huong +12/+6, dau tu +5/+10/+15), D3 (chuyen hoa +5..+8, muc +5/+10/+15), **Truc 1:** Molniya pha 2 +3 moi tau | D5 (>= 30) |
| `VIE_var_mro_exp` | 0-100, tran 50 neu phu thuoc Nga | D1 dinh huong, D2 (+10/+20/+30) | D5 (>= 15) |
| `VIE_var_integration_exp` | 0-100 | D4 (+10/+20/+30, +5 Sigma), **Truc 1:** Sigma Domestic +8, Hybrid +4 | (D5 khong doc truc tiep) |
| `VIE_var_ba_son_tier` | 0-3 | `.60` (moc 40%, bang muc dau tu) | **Truc 1:** `vie_naval.3` B, C (>= 2); D5 bac tu chu |
| `VIE_var_small_combatant_tier`, `VIE_var_integration_tier` | 0-3 | D2, D3, D4 khi ket thuc | `VIE_var_integration_tier` doc boi D5 (High) |
| `VIE_small_combatant_cost_mult` | 0,8-0,9 | D3 khi ket thuc | **Truc 1:** `VIE_naval_pay_molniya_p2` va phu phi ky muon |
| `VIE_var_naval_program_active` | 0-2 | `VIE_nav_program_start/end`, `VIE_nav_program_recount` (sau noi chien) | tooltip `VIE_nav_slot_tt` cua moi Decision |
| `VIE_ba_son_orientation` | 1 dong tau, 2 bao duong, 3 can bang | `vie_nav_ind.1` (Focus 2) | thoi luong D2, D3; phu phi 15% cua D1 |
| `VIE_ba_son_invest`, `VIE_mro_scope` / `_source` / `_level`, `VIE_smallcomb_spec` / `_level`, `VIE_integration_field` / `_level`, `VIE_naval2030_priority` / `_autonomy` | lua chon da luu | cac event chon cua D1-D5 | event ket thuc cua cung Decision |

### Doc tu Truc 1 hai quan
`VIE_kilo_qty_delivered`, `VIE_gepard1_qty_delivered`, `VIE_gepard2_qty_delivered`, `VIE_molniya_ru_delivered`, `VIE_molniya_vn_qty_delivered`
(trigger `VIE_naval_has_sub`, `VIE_naval_has_surface`), `VIE_var_hulls_delivered` (Focus 3), `VIE_opp_sub_mro` (D2 nhanh hon 15%),
`VIE_ext_naval_missile` (D4 Weapons), `VIE_molniya_domestic_started` (D3 bac 3), `VIE_sigma_qty_delivered` (D4 Can bang).

### Nguon nang luc thay cho VIE_ext_* (trigger trong `VIE_md_triggers_naval.txt`)
`VIE_naval_has_electronics` = `VIE_semiconductor_fab` hoac `VIE_chip_design`; `VIE_naval_has_c4isr` = `VIE_earth_observation` hoac `VIE_vinasat`;
`VIE_naval_has_missile` = co `VIE_ext_naval_missile`. Doi mot dong khi nhanh Viettel/C4ISR that duoc xay.

### Da bo so voi bao cao
`VIE_cap_naval_institution`, `VIE_cap_ba_son_complete`, `VIE_cap_naval_mro`, `VIE_cap_small_combatant`, `VIE_cap_integration`,
`VIE_var_ext_support`, cac co `_active` / `_waiting` va bien `_progress` (phan chieu trang thai co san hoac khong can vi cong dat o luc bam).

## Truc 3 hai quan - luc luong (tien to VIE_nf_, namespace vie_nav_force) va Truc 1B (VIE_p1b_, namespace vie_p1b)

Thiet ke: `VIE_naval_truc3_review_and_plan.md`. Code: `VIE_md_effects_nav_force.txt`, `events/VIE_nav_force.txt`,
`VIE_md_nav_force_decisions.txt`, 22 focus `VIE_nf_*`; 1B do `tools/gen_p1b.py` sinh ra `VIE_md_effects_p1b.txt`,
`events/VIE_p1b.txt`, `VIE_md_p1b_decisions.txt`, `VIE_md_ideas_p1b.txt`, scripted loc `VIE_p1b_name`.

### Co
| Co | Dat boi | Doc boi |
|---|---|---|
| `VIE_nf_d1_done`, `_d2_done` | event an ket thuc `vie_nav_force.61 .62` | D-C (d1, d2), 1B P4 (d2) |
| `VIE_nf_sub_prep` | `vie_nav_force.10` (moi lua chon, ngay khi bam D-B) | **Truc 1:** `VIE_naval_pay_kilo`, `VIE_naval_late_start_kilo` (goi huan luyen 0,15 thay 0,2 ty/tau; chi thuong) |
| `VIE_p1b_<p>_contracted`, `_cancelled` | `VIE_p1b_contract_<p>`, `VIE_p1b_cancel` | Decision 1B (visible), giao hang |
| `VIE_p1b_variant_<p>_done` | `VIE_p1b_ensure_variant_<p>` | chan tao trung variant |
| `VIE_p1b_use_debt` | `vie_p1b.3` B | `VIE_p1b_pay` (no x 1,1; xoa sau khi tra) |

### Bien
| Bien | Khoang | Dat boi | Doc boi |
|---|---|---|---|
| `VIE_var_force_program_active` | 0-2 | `VIE_nf_program_start/end`, `VIE_nf_program_recount` (sau noi chien) | `VIE_nf_slot_free` |
| `VIE_var_procurement_1b_active` | 0-2 | `VIE_p1b_program_start/end` (luc ky va giao tau cuoi), `VIE_p1b_program_recount` | `VIE_p1b_slot_free` |
| `VIE_nf_surface_level`, `VIE_nf_surface_specialty`, `VIE_nf_sub_level`, `VIE_nf_sub_orientation` | lua chon da luu | event chon D-A, D-B | `VIE_nf_d1_finish`, `VIE_nf_d2_finish` |
| `VIE_nf_force_priority` | 1 ven bo / 2 can bang / 3 tam xa | `vie_nav_force.30` (ngay luc chon) | focus D1/G1/B1 (khop +1% to chuc; lech: idea phat 365 ngay), `VIE_nf_d4_finish` |
| `VIE_var_hulls_carrier`, `VIE_var_hulls_destroyer` | >= 0 | `VIE_p1b_deliver_carrier`, `_destroyer` | D-E (`VIE_nf_d5_carrier_group`) |
| `VIE_var_hulls_delivered` | >= 0 | **1B**: +1 moi than tau chu luc (khong tinh P6) | Focus T6, Focus 3 Truc 2 |
| `VIE_p1b_<p>_qty_ordered`, `_qty_delivered`, `_localization` | 0-2 cho localization | hop dong, giao hang | giao hang, exp |
| `VIE_p1b_cur`, `_unit`, `_q1`-`_q3`, `_qty`, `_loc`, `_ok_import`, `_ok_hybrid`, `_ok_domestic` | bien chung cua Program Engine | `VIE_p1b_load_<p>` va event `vie_p1b.1 .2` | event `vie_p1b.1-.3`, `VIE_p1b_cost` |
| `VIE_af_*` (navy_org, naval_coordination, naval_detection, navy_max_range, navy_submarine_attack, navy_submarine_defence, naval_strike_attack, experience_gain_navy, navy_personnel_cost_multiplier_modifier, ...) | % cong don | focus T1-T9, D1-D4, G1-G5, B1-B5, ket thuc D-A..D-E | dynamic modifier `VIE_armed_forces_modifier` |

### Doc tu Truc 2
Focus `VIE_naval_mro` / `VIE_small_combatant_construction` (T6), `VIE_var_hulls_delivered > 3` (T6), `VIE_var_ba_son_tier`,
`VIE_var_small_combatant_tier`, `VIE_var_integration_tier` (dieu kien hybrid/noi dia), `VIE_cap_mature_naval_industry` (P10, P11),
`VIE_nav_d2_done` va `VIE_mro_scope` (trigger `VIE_naval_has_sub_mro`, P4), `VIE_nuclear_research` (trigger `VIE_naval_has_nuclear_tech`, P11).
Truc 3 khong ghi `VIE_cap_*` hay bien exp cua Truc 2; 1B chi cong exp qua helper `VIE_nav_add_shipbuilding_exp` / `_integration_exp`.

### Da bo so voi bao cao
`VIE_org_naval_training`, `VIE_path_denial/greenwater/bluewater` (= `has_completed_focus`, trigger `VIE_nf_branch_*`),
`VIE_dec_*_active/_waiting/_progress`, `VIE_var_surface_readiness`, `VIE_var_sub_readiness`, `VIE_var_asw_skill`, `VIE_var_fleet_organization`
(thay bang modifier that), `VIE_var_hulls_operational` (= `VIE_var_hulls_delivered`), `VIE_var_naval_budget_room` (= `treasury`),
bo dem lop `VIE_var_hulls_<lop>` ngoai `carrier` va `destroyer`, `VIE_ext_nuclear_tech` (= trigger tren `VIE_nuclear_research`), `_complete`/`_offered`/`_missed` cua 1B.
