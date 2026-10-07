# REVIEW CHÉO TRỤC 1 ↔ TRỤC 2

> Ngày 2026-09-30 · nhánh `truc1-skeleton` · soát lại toàn bộ sau khi code xong cả hai trục.
> Đối chiếu với `MillenniumDawn/Millennium-Dawn` @ `main` (dữ liệu thật trong `tools/audit/md_ref/`).
>
> **KẾT LUẬN: hai trục khớp nhau, không có lỗi logic chặn.** Nhưng soát ra
> **5 lỗi convention** (tôi gây ra khi code) và **3 điểm đáng lưu ý về thiết kế**.
> Tất cả 5 lỗi convention **đã sửa** trong commit này.

---

## PHẦN 1 — HAI TRỤC KHỚP NHAU: 6/7 cờ đã nối

| Cờ Trục 1 đặt | Đặt ở | Trục 2 đọc ở | Kết quả |
|---|---|---|---|
| `VIE_t54m3_prototype` | `.5` option A | **D5** `VIE_dec_t54m` (`visible`) | ✅ mở D5 |
| `VIE_igla_license` | `.8` option A | **D9** `VIE_dec_tl01` (`visible`) | ✅ mở D9 |
| `VIE_iwi_license` | `.11` option A | **D2** — chọn `VIE_dec_stv` (1095) hay `_fast` (730) | ✅ rút 365 ngày |
| `VIE_bmp3_lessons` | `.32` option A (alt) | **D6** — chọn `VIE_dec_xcb01` (1460) hay `_fast` (1095) | ✅ rút 365 ngày |
| `VIE_k9_purchased` | `.20` immediate | **D8** (`visible`) | ✅ mở D8 |
| `VIE_k9_localization` | `.21` option A | **D8** (`visible`) | ✅ mở D8 |
| `VIE_t90_purchased` | `.15` immediate | **`vie_def_ind.2`** (scheduler p15) | ✅ +150 funds, +10 XP |
| `VIE_ev_t90_tanks` | `.15` immediate | — | ⏳ chờ Trục 1b / trục Hải quân (Q1 = d). **Đừng xoá** |

Chiều ngược lại (Trục 2 → Trục 1) cũng đã nối: `VIE_proc_gate_z_factories_done`
đọc `VIE_dec_z_factories_done` (Q3 đã trả nợ ở bước 7).

**Kiểm tra:** 135 effect/trigger `VIE_*` được gọi, **0 thiếu định nghĩa**.
`live.py` báo 0 missing ở mọi nhóm. `prov.py` TỔNG HỢP LỖI: 0.
`ev.py` 187 event, 0 trùng, 0 orphan, 0 thiếu loc. `audit.py` 260 focus,
0 dangling, 0 forward-ref, 0 cycle.

---

## PHẦN 2 — 5 LỖI CONVENTION (đã sửa)

Đối chiếu với **MD gốc** và với **chính repo cũ** (16 file `scripted_effects`,
33 decision trong `VIE_md_decisions.txt`, 66 event trong `VIE_md_p10.txt`).

### C1 · `log` trong `scripted_effects` — MD **không** làm vậy

| | Số effect | Số effect có `log` |
|---|---:|---:|
| MD `00_budget_effects.txt` | 65 | **0** |
| MD `00_scripted_effects.txt` | 97 | **0** |
| MD `00_mio_scripted_effects.txt` | 9 | **0** |
| repo cũ (16 file `VIE_md_effects*`) | ~60 | **1** (`VIE_md_effects_p2.txt`) |
| **p14 + p15 của tôi** | 50 | **35** ❌ |

→ **Đã bỏ 30 dòng `log`** (21 ở p14, 9 ở p15). MD đặt `log` trong **event option**
và **decision effect**, không phải trong scripted effect — vì scripted effect được gọi
từ nhiều nơi, log ở đó sẽ lặp và không cho biết ai gọi.

Sau khi bỏ, `VIE_fb_proc_alt_none` thành **effect rỗng** → đã xoá và đổi 3 chỗ gọi
sang **`VIE_fb_none`** sẵn có của repo (`VIE_md_effects_p2.txt:17`), vốn được tạo
đúng cho mục đích này và **có log** nên vẫn truy vết được.

### C2 · `log` trong `immediate` của event — repo **không** làm vậy

| | Số event | `log` trong option | `log` trong `immediate` |
|---|---:|---:|---:|
| repo cũ (`VIE_md_p10.txt` + `p11.txt`) | 71 | 133 | **0** |
| **`VIE_proc_army.txt` + `VIE_def_ind.txt` của tôi** | 24 | 42 | **12** ❌ |

→ **Đã bỏ 12 dòng `log` trong `immediate`** (8 ở `VIE_proc_army.txt`, 4 ở `VIE_def_ind.txt`).
`log` trong option vẫn giữ — đó là convention đúng (repo 133 lần, MD 167 lần trong
`01_pmc_decisions.txt`).

Lý do convention này hợp lý: `immediate` chạy kể cả khi event bị fallback hay
người chơi không chọn gì, nên log ở đó không cho biết **lựa chọn** nào đã xảy ra.

### C3 · `custom_trigger_tooltip` **thừa** ở 5 decision

5 decision (D4, D5, D8, D9, D7) có `custom_trigger_tooltip` lặp lại **đúng điều kiện
đã có trong `visible`**:

```pdx
visible   = { has_completed_focus = VIE_def_industry_law  has_country_flag = VIE_dec_pth_done }
available = { custom_trigger_tooltip = { tooltip = VIE_dec_ammo_tt
                has_country_flag = VIE_dec_pth_done } }     # ← THỪA
```

Vì `visible` chặn trước, người chơi **không bao giờ thấy** decision ở trạng thái
"hiện nhưng xám vì thiếu cờ đó" → tooltip không bao giờ hữu ích.

→ **Đã bỏ 5 `custom_trigger_tooltip` thừa**, thay bằng `NOT = { has_country_flag = VIE_dec_*_started }`
(cờ này **có** ý nghĩa: nó chặn bấm lại và, với D2/D6, chặn biến thể kia).

**Giữ lại 3 tooltip có ý nghĩa thật:**
- `VIE_dec_pth_tt` — che `check_variable = { treasury > 2 }` (engine không tự sinh tooltip cho `check_variable`)
- `VIE_dec_xcb01_tt` — che `treasury > 3`
- `VIE_dec_z_factories_avail_tt` (**mới**) — che `can_staff_an_arms_industry` + `free_building_slots`, cả hai là trigger phức mà engine không mô tả rõ

Đây đúng là mẫu repo đang dùng: `VIE_procurement_batch_tt` che `check_variable = { treasury > 3 }`.

### C4 · 2 cờ `_started` được set nhưng không ai đọc

`VIE_dec_z_started` (D1) và `VIE_dec_pth_started` (D3) được đặt trong `complete_effect`
nhưng không xuất hiện trong `available`.

Về kỹ thuật không gây lỗi — `fire_only_once = yes` đã chặn bấm lại. Nhưng:
- **không nhất quán**: 7 decision kia đều có `NOT started` trong `available`
- cờ đặt mà không đọc là **rác**, sẽ bị người dọn dep sau này xoá nhầm

→ **Đã thêm `NOT = { has_country_flag = … }` vào `available` của D1 và D3.**
Giờ **9/9 cờ `_started` cân bằng** (set = đọc).

### C5 · 6 loc key tooltip mồ côi

Sau C3, 6 key không còn ai dùng: `VIE_dec_ammo_tt`, `VIE_dec_t54m_tt`,
`VIE_dec_tl01_tt`, `VIE_dec_k9_localization_tt`, `VIE_dec_bm21_tt`,
`VIE_dec_z_factories_tt`.

→ **Đã xoá 6 key** (1959 → 1953), rồi thêm 1 key mới cho C3 (`VIE_dec_z_factories_avail_tt`)
→ **1954 key, 0 trùng, 0 mồ côi**.

⚠️ Script dò key mồ côi của tôi **bỏ sót 6 key này** ở lần chạy đầu, vì quy tắc
"key dẫn xuất" coi `_tt` là hậu tố tự sinh từ key cha. Nhưng `VIE_dec_ammo_tt`
**không phải** dẫn xuất của `VIE_dec_ammo` — nó là key tooltip riêng. Đã kiểm tra
lại bằng cách grep trực tiếp từng tên.

---

## PHẦN 3 — 3 ĐIỂM ĐÁNG LƯU Ý VỀ THIẾT KẾ (không sửa, cần bạn biết)

### D1 · Thứ tự trường trong decision **lệch nhẹ** so với MD — nhưng khớp repo

| Nguồn | Thứ tự |
|---|---|
| MD (`01_pmc_decisions.txt`, mẫu phổ biến) | `visible → available → fire_only_once → days_remove → days_re_enable → complete_effect → remove_effect → ai_will_do` |
| repo cũ (`VIE_md_decisions.txt`, 5 decision có `days_remove`) | `icon → cost → fire_only_once → visible → available → complete_effect → **days_remove** → remove_effect → ai_will_do` |
| **Trục 2 (của tôi)** | `icon → cost → fire_only_once → visible → available → complete_effect → **days_remove** → remove_effect → ai_will_do` |

Tôi theo **repo**, không theo MD. Lý do: trong cùng một mod thì nhất quán nội bộ
quan trọng hơn nhất quán với mod mẹ, và `VIE_md_decisions.txt` là file decision
duy nhất mà người bảo trì mod này sẽ đọc cùng lúc.

**Thứ tự trường không ảnh hưởng engine** — HOI4 đọc theo tên key, không theo vị trí.
Nếu bạn muốn theo MD thì đó là việc của một đợt chuẩn hoá riêng (phải sửa cả 33
decision cũ), không nên làm lẫn vào Trục 1/2.

### D2 · `D8` không bao giờ hoàn thành trong khung thời gian của mod

Tính từ mốc lịch sử thật (báo cáo mục 1.3: đánh giá 02/2023, xác nhận 08/2025):

```
.18 đánh giá        2023-02-01
.19 quyết định mua  2025-07-20   (+900 ngày)
.20 giao xe         2026-07-20   (+365)  ← VIE_k9_purchased
.21 nội địa hóa     2027-07-20   (+365)  ← VIE_k9_localization
D8 hoàn thành       2029-07-19   (+730)
```

Bookmark chính của MD là `MILLENNIUM_DAWN` (2000) và mod chạy tới ~2026–2035.
→ **D8 xong năm 2029**, ngoài khung của một ván game bình thường.

**Đây không phải lỗi code** — báo cáo mục 2.5 **đã tính đúng và đã ghi**:
*"D8, nhánh chuẩn: khoảng 2027 → khoảng 2029"*. Code khớp báo cáo 100%.

Nhưng đáng nêu vì D8 là decision **duy nhất** trong 9 cái không thể hoàn thành.
Người chơi tốn 30 PP + 0,5 tỷ mà gần như không bao giờ thấy kết quả.

Ba lựa chọn nếu bạn muốn đổi:
- **(a) Để nguyên** — D8 là "nội dung tương lai", đúng như báo cáo tính
- **(b)** Giảm `days_remove` của D8 từ 730 → 365: xong 2028, vẫn ngoài khung
- **(c)** Rút chuỗi `.19` từ 900 → 365 ngày: D8 xong ~2025 ✅ nhưng **lệch lịch sử thật**

Tôi **không sửa** vì cả ba đều là quyết định thiết kế, không phải sửa lỗi.

### D3 · `VIE_def_ind_has_factory_slot` gần như không bao giờ chặn

Điều kiện này nằm trong `available` của D1, D2, D6. Nhưng đo slot thật của 7 state
lục địa VIE từ `tools/audit/md_ref/`:

| State | Category | `local_building_slots` |
|---|---|---:|
| 522 Red River Delta | `state_11` | 40 |
| 519 Southern Vietnam | `state_11` | 40 |
| 518 Mekong Delta | `state_10` | 36 |
| 521 Central Vietnam | `state_10` | 36 |
| 520 Vietnamese Highlands | `state_06` | 22 |
| 523 Northern Vietnam | `state_06` | 22 |
| 524 Northwest Vietnam | `state_04` | 14 |
| **Tổng** | | **~210** |

Trục 2 chỉ xây **3** nhà máy (D1×2 + D2×1). → Không bao giờ hết slot.

**Vẫn giữ**, vì ba lý do:
1. `one_state_arms_factory` của MD **đã có fallback** (`every_controlled_state` + `random_select_amount = 1`), nên kể cả hết slot cũng không fail
2. Nếu MD sau này đổi `state_category` (giảm slot) thì đây là lưới an toàn
3. Nó cho tooltip giải thích rõ thay vì decision biến mất không lý do

Và điều kiện này **tự loại 801** (Tây Trường Sa, `state_inhospitable`, 0 slot) —
đúng như B4 trong review Trục 2 yêu cầu, mà không cần trigger chưa xác minh
(`has_state_category`, `is_island_state` đều không có trong MD).

---

## PHẦN 4 — NHỮNG GÌ ĐÃ KIỂM CHỨNG LÀ **ĐÚNG**, khỏi soát lại

| Hạng mục | Kết quả |
|---|---|
| Số học `VIE_def_industry_level` | ✅ 8 decision +1, D8 không cộng, Pháp lệnh +1, Core +2, Divest +1 → **11/10** khớp báo cáo |
| Số học tiền | ✅ 8 decision cố định **30,25 tỷ**; cả 9 **30,75 tỷ** — khớp báo cáo mục 2.2 và V |
| Timeline | ✅ D1 07/2011 · D7 06/2013 · D5 12/2014 · D3 12/2016 · D4 12/2018 · D2/D9 01/2019 · D6 12/2024 — khớp báo cáo mục 2.5 |
| `fire_only_once` + `days_remove` | ✅ MD dùng cặp này **626 lần** trong 60 file decisions đầu tiên |
| `[Root.GetName]` trong decision/effect, `[This.GetName]` trong event | ✅ khớp repo (47/0 và 133/0) và MD (167/0) |
| 6 token `CAT_*` | ✅ cả 6 có trong 194 token của 24 file `common/technologies/` MD |
| 4 variant tự tạo | ✅ 23/23 module + 2/2 upgrade xác minh trong `MD_tank_modules.txt` (295) + `MD_arty_modules.txt` (170) + `MD_land_upgrades.txt` |
| Variant tạo **trước** khi cấp xe | ✅ cả 4 (D3, D6, D7, và `.6` của Trục 1) |
| `producer` khớp nước sở hữu variant | ✅ `T-55A`/`T-90`/`BMP-3`/`TOS-1` = SOV, `T-72M1` = POL, `K9 Thunder` = KOR, 4 variant VIE = VIE |
| 20 event `vie_proc_army` + 4 event `vie_def_ind` | ✅ 0 id trùng, 0 orphan, 0 thiếu loc, `add_namespace` đủ cả hai file |
| Race `visible` ở D2/D6 | ✅ không có: cửa sổ `.11` đóng 2015, D2 mở 2017; chuỗi BMP-3 đóng 2011, D6 mở 2021 |
| Trần 5 lần của `vie_def_ind.3` | ✅ mô phỏng đúng 5 lần; biến đếm tăng trong `immediate` nên không mất lượt khi bị `popup_cd` chặn |
| `VIE_popup_cd` | ✅ cả 4 event p15 và 10 chuỗi p14 đều tôn trọng |
| `VIE_catch_up` | ✅ cả p14 và p15 đều có nhánh catch-up riêng, chỉ đặt cờ |
| Layout 4 focus mới | ✅ 0 collision tuyệt đối · 0 forward-ref · 0 cycle · 0 con nằm ngang cha · gap ngã rẽ = 4 |
| `loc` | ✅ 1954 key · 0 trùng · 40/40 file có BOM · 0 dòng sai format · 0 key rỗng |

---

## PHẦN 5 — CÒN LẠI 4 TODO (đều cần máy có HOI4, không phải nợ code)

| Chỗ | TODO | Rủi ro |
|---|---|---|
| `VIE_md_effects_p14.txt` (`.6`) | `add_equipment_to_stockpile amount = -100` — thử cả `destroy_equipment`, cái nào không ghi `error.log` thì giữ | **cao** — chưa xác minh được cách nào hoạt động |
| `VIE_md_effects_p15.txt` (D7) | `amount = -36` — cùng rủi ro | **cao** |
| `VIE_md_effects_p14.txt` (Igla) | đang dùng `VIE_af_air_defence_factor`; đổi sang `enemy_army_bonus_air_superiority_factor` nếu xác nhận modifier đó tồn tại | thấp — modifier hiện tại hợp lệ, chỉ khác ý báo cáo |
| `VIE_md_def_industry.txt` (D9) | ghi chú chéo cho TODO trên | — |

**Cộng 2 rủi ro chỉ test được trong game** (đã ghi trong `tools/TESTING.md`):
- 6 variant NSB (`T-55A`, `T-90`, `T-72M1`, `K9 Thunder`, `BMP-3`, `TOS-1`) có lắp được vào sư đoàn không
- 4 variant VIE tự tạo (`T-54M`, `PTH-152`, `XCB-01`, `BM-21M`) có báo lỗi module/upgrade không

---

## PHẦN 6 — NỢ CŨ CỦA REPO PHÁT HIỆN TRONG LÚC SOÁT (không thuộc Trục 1/2)

### N1 · 🚨 31/41 token `CAT_*` repo dùng không tồn tại trong MD

`VIE_md_organizations.txt:183` liệt kê trong `research_categories`:
`CAT_inf_wep CAT_sp_arty CAT_sp_r_arty CAT_at CAT_util` — **cả 5 không tồn tại**.
Thêm `VIE_md_focus.txt` và `events/VIE_md_p7.txt` dùng `CAT_ai`, `CAT_computing_tech`,
`CAT_microchips`, `CAT_fighter`, `CAT_mr_fighter`, `CAT_satellite`, `CAT_genes`, …

**Hệ quả:** `research_bonus = 0.06` của **cả 4 MIO** có thể không áp dụng;
mọi `add_tech_bonus` dùng token sai sẽ không vào đúng folder nghiên cứu.

Chi tiết đầy đủ + bảng token sai → đúng: `VIE_repo_health_report.md` **mục 6.13**.
Danh sách 194 token hợp lệ: `tools/audit/md_ref/MD_all_CATS.json`.

⚠️ **Đừng "sửa" `CAT_artillery` và `CAT_artillery_ammunition`** — chúng có thật.

### N2 · `VIE_ev_kilo_submarines` / `VIE_ev_bastion_p_coastal_defence` vẫn orphan

`VIE_paracel_ultimatum` vẫn soft-lock. **Q1 = (d) đã chốt: giữ nguyên** cho tới khi
có trục Hải quân. Chỗ sửa duy nhất đã chuẩn bị: `VIE_proc_gate_paracel_capable`.

### N3 · Những khoản khác (đã ghi ở `VIE_repo_health_report.md`)

24 idea mồ côi · `VIE_oligarch_balance` chết · `VIE_md_focus.txt.bak` 343 KB ·
3 file archive ở gốc mod · layout cây focus chưa nén (2 dải trống 52 và 38 unit) ·
4 root mồ côi (giờ còn 3 vì `VIE_modernize_vpa` đã có con) ·
tools hardcode `D:\` · không có README/LICENSE · 38 MB font.

---

## PHỤ LỤC (1/10/2026) — TRỤC 3 VÀ LIÊN KẾT VỚI TRỤC 1, 2

Thiết kế và plan: `VIE_truc3_review_and_plan.md`. Trục 3 (30 focus `VIE_lf_*`, 6 decision, 5 event `vie_lf`) **không có prerequisite chéo** sang Trục 1 hay 2.

**Trục 3 đọc từ Trục 2 (một thứ duy nhất)**

| Đọc | Ở đâu | Điều kiện |
|---|---|---|
| ~~`VIE_def_ind_level_ge_2`~~ | ~~`VIE_lf_gate_open`~~ | Thiết kế gate cũ, không còn áp dụng: `VIE_alt_history` đã bị xoá ngày 07/10/2026 vì chỉ có lựa chọn mặc định và không có reader. |

**Trục 3 đặt, Trục 1 và 2 đọc (bước 8, chỉ chỉnh trọng số AI)**

| Cờ Trục 3 | Đặt bởi | Đọc ở | Hiệu lực |
|---|---|---|---|
| `VIE_lf_regular` | `VIE_lf_fs_main_corps` | `vie_proc_army.18.a`, `.19.a`, `.19.b`, `.30.b`, `.35.a`, `.38.a`; `VIE_dec_pth`, `VIE_dec_xcb01`, `VIE_dec_xcb01_fast` | `ai_chance` / `ai_will_do` ×1,3 |
| `VIE_lf_depth` | `VIE_lf_fs_depth_defence` | `vie_proc_army.8.a` (Igla kèm quyền sản xuất); `VIE_dec_tl01` | ×1,3 |
| `VIE_lf_mobile` | `VIE_lf_fs_mobile_force` | không ai ở Trục 1, 2 | — |

**Cờ chờ có chủ đích (như `VIE_ev_t90_tanks`, đừng xoá):** `VIE_lf_done` (do `VIE_lf_force_complete` đặt, chưa ai đọc; dành cho nhánh Chính trị/Đối ngoại sau này).

**Nợ thiết kế đã ghi:** `VIE_mechanization`, `VIE_army_c4isr`, `VIE_army_short_range_ad` không còn (v11) và không được dựng lại; Trục 3 chỉ cho modifier thuần (plan, B1, Q12).

**Lỗi cũ của Trục 2 tìm thấy và đã vá khi làm Trục 3 (bước 0):** `on_startup` đặt lại `VIE_def_industry_level` và `VIE_def_ind_export_count` về 0 mỗi lần load save; nay bọc bằng cờ `VIE_def_ind_vars_init`.

