# REVIEW TRỤC 2 (CNQP LỤC QUÂN) + PLAN CODE

> Đầu vào: `Báo cáo Lục quân VIE — Trục 1, 2, 3.docx` (29/9/2026), mục **II. Trục 2: CNQP Lục quân**
> Đối chiếu với: repo @ nhánh `truc1-skeleton` commit `15ffe81`, và `MillenniumDawn/Millennium-Dawn` @ `main`
> (dữ liệu MD thật nằm trong `tools/audit/md_ref/`).
>
> **KẾT LUẬN: Trục 2 có nền tốt hơn Trục 1** — số học timeline, level, và 8/8 trait MIO đều
> đã kiểm chứng đúng. Nhưng có **2 lỗi chặn**, **5 lỗi về phía MD**, và **7 lỗi logic nội tại**.
> Phần lớn là do báo cáo viết trước khi v11 xoá nhánh quân sự, và chưa tra `one_state_arms_factory`
> thật của MD.

---

# PHẦN 0 — TRẠNG THÁI SAU KHI CODE XONG (2026-09-30, bước 7)

**Trục 2 đã code xong toàn bộ 7 bước.** 11/11 decision (9 ID, D2 và D6 mỗi cái 2 biến thể),
4 focus, 1 decision category, 5 idea, 4 event, scheduler p15, 3 variant tự tạo.

## 0.1 · Kiểm chứng lại số học báo cáo bằng code thật

Đo trực tiếp từ `common/decisions/VIE_md_def_industry.txt`,
`common/scripted_effects/VIE_md_effects_p15.txt` và `common/national_focus/VIE_md_focus.txt`:

**Level (mục 2.4) — khớp 100%**

| Nguồn | Báo cáo | Code thật |
|---|---:|---:|
| D1–D7 + D9 (8 decision) × +1 | +8 | ✅ đúng 8 decision gọi `VIE_def_ind_add_level` |
| D8 | **không cộng** | ✅ `VIE_d8_reward` **không** gọi |
| Pháp lệnh CNQP (focus) | +1 | ✅ `VIE_def_ind_add_level` |
| Ngã rẽ Core (focus) | +2 | ✅ `add_to_variable … = 2` |
| Ngã rẽ Divest (focus) | +1 | ✅ `VIE_def_ind_add_level` |
| **Tối đa** | **11 (Core) / 10 (Divest)** | ✅ **11 / 10** |

**Tiền (mục 2.2 và V) — khớp 100%**

| | Báo cáo | Code thật |
|---|---:|---:|
| Chi phí chương trình, 8 decision cố định (D1–D7, D9) | 7,75 | ✅ 0 + 0,5 + 2,0 + 1,0 + 0,25 + 3,0 + 0,5 + 0,5 |
| 3 nhà máy (D1×2 + D2×1, MD tự trừ 7,5/cái) | 22,50 | ✅ 3 × `one_state_arms_factory` |
| **Kịch bản lịch sử (8 decision)** | **30,25** | ✅ **30,25** |
| D8 (có điều kiện) | +0,5 | ✅ |
| **Tối đa (cả 9)** | **30,75** | ✅ **30,75** |

**Timeline (mục 2.5) — khớp 100%**

| | Báo cáo | Tính lại từ `days_remove` + ngày mở |
|---|---|---|
| D1 xong | 07/2011 | 2008-07-01 + 1095 = **2011-07-01** ✅ |
| D7 xong | 07/2013 | 2011-07-01 + 730 = **2013-06-30** ✅ |
| D5 xong | 01/2015 | 2012-01-01 + 1095 = **2014-12-31** ✅ |
| D3 xong | 01/2017 | 2013-01-01 + 1460 = **2016-12-31** ✅ |
| D4 / D2 / D9 xong | 01/2019 | **2018-12-31 / 2019-01-01 / 2019-01-01** ✅ |
| D6 xong | 01/2025 | 2021-01-01 + 1460 = **2024-12-31** ✅ |
| Hoàn tất muộn nhất | ~01/2025 | **2024-12-31** ✅ |

## 0.2 · Bốn quyết định đã chốt và áp dụng

| | Quyết định | Áp dụng ở đâu |
|---|---|---|
| **Q6 = (a)** | Dựng lại 4 focus dưới `VIE_modernize_vpa`; level sống trên focus tree | `VIE_md_focus.txt` (260 focus), layout (266,2) → (264/268,3) → (266,4), 0 collision / 0 forward-ref / 0 cycle |
| **Q7 = (a)** | `one_state_arms_factory`, **không** trừ tiền tay | `VIE_build_arms_factory_auto`; D1 = −15 tỷ, D2 = −7,5 tỷ |
| **Q8 = (a)** | MIO chỉ `add_mio_size`; funds chỉ qua `vie_def_ind.*` | `VIE_gdt_mio_size_1/2`; total +9 size khớp bảng mục V |
| **Q9 = (a)** | `vie_def_ind.3` trần **5 lần** | `VIE_def_ind_export_open` + biến đếm tăng trong `immediate` của event |

## 0.3 · Q3 đã trả nợ ở bước 7

Gate của `.11` (license Galil ACE) đổi từ `date > 2011.6.30` sang
**`has_country_flag = VIE_dec_z_factories_done`** — đúng như báo cáo mục 1.4 muốn
("Trigger: D1 đã xong").

**Gate mới chặt hơn gate tạm, và đó là điểm quan trọng.** Gate tạm (ngày) luôn đúng
từ 07/2011 bất kể người chơi có bấm D1 hay không → `.11` luôn nổ, license luôn có,
D2 luôn là bản 730 ngày → **người chơi không bao giờ phải chọn thứ tự**, mất ý nghĩa.
Gate mới khôi phục đúng ràng buộc: muốn license sớm thì phải ưu tiên D1.

Race check: D1 xong sớm nhất 07/2011, `.11` mở 01/2013 → **dư ~18 tháng**, không race.
Nếu người chơi đi chậm tới 2016 mà D1 chưa xong thì `.11` hết cửa sổ, fallback kiểm
gate → fail → log `window closed unmet`, D2 là bản 1095 ngày. Đó là hệ quả đúng.

## 0.4 · 6/7 cờ Trục 1 đã có người đọc

| Cờ Trục 1 | Ai đọc |
|---|---|
| `VIE_t54m3_prototype` | **D5** `VIE_dec_t54m` |
| `VIE_igla_license` | **D9** `VIE_dec_tl01` |
| `VIE_iwi_license` | **D2** — chọn `VIE_dec_stv` (1095) hay `_fast` (730) |
| `VIE_bmp3_lessons` | **D6** — chọn `VIE_dec_xcb01` (1460) hay `_fast` (1095) |
| `VIE_k9_purchased` | **D8** |
| `VIE_k9_localization` | **D8** |
| `VIE_ev_t90_tanks` | ⏳ vẫn chờ Trục 1b / trục Hải quân (Q1 = d). **Đừng xoá** |

## 0.5 · Hai lỗi của chính tôi trong lúc code, đã sửa

1. **Bước 4: kết luận sai về `CAT_self_propelled_artillery`.** Tôi ghi nó "✅ có thật"
   vì JSON đối chiếu bị lẫn nguồn. Grep lại từng file trong **24 file**
   `common/technologies/` của MD (194 token): token đó **không tồn tại** ở đó, chỉ là
   `research_categories` của MIO. Đã đổi D3 và D8 sang `CAT_artillery`.
   → Bài học: **`CAT_*` có hai loại** — token của tech folder và token chỉ của MIO.
   Chỉ loại đầu dùng được trong `add_tech_bonus` / `research_bonus` của idea.
2. **Bước 1: scheduler `vie_def_ind.3` có 2 lỗi** — không tôn trọng `VIE_popup_cd`,
   và tăng biến đếm trần **trước** khi event fire (khiến người chơi chỉ được 4 lần
   thật thay vì 5). Đã sửa ở bước 6.

---

# PHẦN 1 — NHỮNG GÌ BÁO CÁO LÀM **ĐÚNG** (đã kiểm chứng, khỏi tra lại)

## 1.1 Số học timeline — chính xác tuyệt đối

Tính lại bằng script, khớp từng mốc báo cáo ghi ở mục 2.5:

| Decision | Mở | `days_remove` | Xong sớm nhất | Báo cáo ghi | |
|---|---|---:|---|---|---|
| D1 | 2008-07-01 | 1095 | **2011-07-01** | 07/2011 | ✅ |
| D7 | sau D1 | 730 | **2013-06-30** | 07/2013 | ✅ |
| D5 | 2012-01-01 | 1095 | **2014-12-31** | 01/2015 | ✅ |
| D3 | 2013-01-01 | 1460 | **2016-12-31** | 01/2017 | ✅ |
| D4 | sau D3 | 730 | **2019-01-01** | 01/2019 | ✅ |
| D2 | 2017-01-01 | 730 (có license IWI) | **2019-01-01** | 01/2019 | ✅ |
| D9 | 2017-01-01 | 730 | **2019-01-01** | 01/2019 | ✅ |
| D6 | 2021-01-01 | 1460 (1095 nếu có `VIE_bmp3_lessons`) | **2024-12-31** | 01/2025 | ✅ |

Tổng `days_remove` = 8030 ngày = **22,0 năm** — khớp con số "22 năm" của báo cáo (nhưng xem L4).

## 1.2 Số học `VIE_def_industry_level` — đúng

```
D1–D7 + D9  (8 decision) × +1  = +8
Pháp lệnh CNQP                 = +1
Ngã rẽ Core / Divest           = +2 / +1
────────────────────────────────────
Tối đa                         = 11 (Core) / 10 (Divest)   ✅
```
Capstone cần level ≥ 8: **Core** = 1 + 5 decision + 2 = 8 ✅ · **Divest** = 1 + 6 decision + 1 = 8 ✅.
Cả hai ngã rẽ đều đạt được — không có nhánh chết.

Kiểm tra thêm (báo cáo không ghi): ngã rẽ cần level ≥ 4, mà level 4 sớm nhất = **01/2015**
(Pháp lệnh 1 + D1 + D7 + D5). Vậy ngã rẽ không bao giờ mở trước 2015 → không phá thứ tự.

## 1.3 MIO `VIE_gdt_manufacturer` — **đã có sẵn cây trait hoàn chỉnh**

Đây là tin tốt nhất của Trục 2. `common/military_industrial_organization/organizations/VIE_md_organizations.txt:175`
đã định nghĩa đầy đủ, **có cả `all_parents`, `mutually_exclusive`, `relative_position_id`**:

| Trait token (đã có) | `position` | Phụ thuộc | Báo cáo gắn với |
|---|---|---|---|
| `VIE_gdt_mio_trait_initial` | (initial) | — | — |
| `VIE_gdt_mio_trait_licensed_rifles` | x0 y1 | — | D2 |
| `VIE_gdt_mio_trait_stv_family` | x−1 y1 | parent: licensed_rifles · **ME** với mass_production | D2 |
| `VIE_gdt_mio_trait_mass_production` | x1 y1 | parent: licensed_rifles · **ME** với stv_family | D1 |
| `VIE_gdt_mio_trait_ammunition_plants` | x0 y3 | any_parent: stv_family **hoặc** mass_production | D4 |
| `VIE_gdt_mio_trait_towed_artillery` | x3 y1 | — | D3 |
| `VIE_gdt_mio_trait_rocket_artillery` | x3 y2 | parent: towed_artillery | D7 |
| `VIE_gdt_mio_trait_vehicle_overhaul` | x3 y3 | parent: rocket_artillery | D5 |
| `VIE_gdt_mio_trait_arsenal_of_the_people` | x1 y4 | any_parent: ammunition_plants **hoặc** vehicle_overhaul · `special_trait_background` | — |

Mọi trait đều có `on_complete = { expenditure_for_mio_upgrade = yes }`.
`equipment_type` phủ `infantry_weapons_type artillery_equipment util_vehicle_type AA_Equipment L_AT_Equipment mio_cat_all_armor`;
`research_categories` phủ `CAT_inf_wep CAT_inf CAT_artillery CAT_sp_arty CAT_sp_r_arty CAT_at CAT_util`.

→ **Khớp chính xác** với bảng "MIO VIE_gdt_manufacturer nhận size và funds" ở mục V của báo cáo.
Không phải tạo MIO mới, không phải tạo trait mới.

## 1.4 Những chỗ khác báo cáo đúng

- `modify_debt_effect` / `modify_treasury_effect` ✅ (`00_budget_effects.txt`)
- Quyết định "D1 và D2 không dùng ID state cố định" ✅ — nhưng lý do báo cáo đưa ra sai, xem **B5**
- `infantry_weapons_type` cho D2 ✅ (MD có, repo đang dùng ở `VIE_md_decisions.txt:40`)
- "MANPADS không cấp equipment, tác dụng nằm ở modifier" ✅ (D9)
- 7 flag nối Trục 1 ↔ Trục 2 ✅ — **Trục 1 đã đặt sẵn cả 7**, xem `VIE_v9_flag_mapping.md` mục 2.2b
- `equipment_bonus = { medium_tank_flame_chassis = { build_cost_ic = -0.05 } }` cho XCB-01 ✅ đúng cú pháp
- Cảnh báo "Buff MBT không tự áp cho IFV hay APC" ✅ đúng
- `days_remove` cố định lúc kích hoạt → phải dùng 2 decision loại trừ nhau (mục 6.4) ✅ **đúng và cần thiết**

---

# PHẦN 2 — 2 LỖI CHẶN

## A1 · 🚨 Toàn bộ focus nền của Trục 2 **đã bị v11 xoá**

Báo cáo mục 2.1 viết "Focus v7 → Xử lý" với 6 dòng **Giữ**. Thực tế đo trên code live:

| Focus báo cáo dựa vào | Vai trò | Còn? |
|---|---|---|
| `VIE_z_factories` | → **D1** | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_licensed_rifles` | → **D2** | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_def_industry_law` | **"Giữ, đổi tên thành Pháp lệnh CNQP"** | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_military_enterprises_core` | **"Giữ"** — ngã rẽ, +2 level | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_military_enterprises_divest` | **"Giữ"** — ngã rẽ, +1 level | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_path_self_reliant_deterrence` | **"Giữ"** — capstone | ❌ `v11_removed_military_other_focuses.txt` |
| `VIE_missile_program`, `VIE_def_research_partnership` | "giữ nguyên, không thuộc báo cáo" | ❌ |
| `VIE_tank_modernization` | cổng mở nhóm decision | ❌ (Trục 1 đã gặp, đổi sang `VIE_modernize_vpa`) |
| `VIE_modernize_vpa` | — | ✅ **root mồ côi, 0 con** |

**Hệ quả nghiêm trọng hơn Trục 1.** Trục 1 chỉ mất *trigger* (đổi sang `VIE_modernize_vpa` là xong).
Trục 2 mất **cả cấu trúc**: 4 focus "Giữ" (Pháp lệnh, Core, Divest, Capstone) là **xương sống**
của hệ `VIE_def_industry_level` — mà level lại là điều kiện mở ngã rẽ và capstone.

Số học 1.2 ở trên **vẫn đúng về mặt logic**, nhưng hiện **không có chỗ nào** để:
- cộng +1 cho "Pháp lệnh CNQP"
- cộng +2 / +1 cho ngã rẽ Core / Divest
- kiểm tra `level >= 4` để mở ngã rẽ
- kiểm tra `level >= 8` + "đã chọn ngã rẽ" cho capstone

→ **Quyết định Q6 (mới, bắt buộc):** dựng lại 4 focus đó, hay chuyển toàn bộ hệ level sang decision/event?
Xem Phần 5.

## A2 · 🚨 `one_state_arms_factory` của MD **đã tự trừ 7,5 tỷ** — thiết kế 6.2 sẽ trừ đôi

Đọc `tools/audit/md_ref/00_scripted_effects.txt:20` (MD `common/scripted_effects/00_scripted_effects.txt`):

```pdx
one_state_arms_factory = {
	if = {
		limit = { free_building_slots = { building = arms_factory size > 0 include_locked = yes } }
		add_extra_state_shared_building_slots = 1          # ← TỰ CỘNG SLOT
		add_building_construction = { type = arms_factory level = 1 instant_build = yes }
	}
	else = {
		ROOT = {
			every_controlled_state = {                      # ← FALLBACK: state khác
				limit = { free_shared_building_slots = yes }
				random_select_amount = 1
				add_extra_state_shared_building_slots = 1
				add_building_construction = { type = arms_factory level = 1 instant_build = yes }
			}
			custom_effect_tooltip = no_building_construction_TT
		}
	}
	CONTROLLER = {
		if = { limit = { NOT = { check_variable = { skip_payment = 1 } } } }
			set_temp_variable = { treasury_change = -7.5 }  # ← TỰ TRỪ 7,5 TỶ
			modify_treasury_effect = yes
		}
	}
}
```

Báo cáo mục 6.2 viết:
```pdx
complete_effect = {
	set_temp_variable = { treasury_change = -15 }     # trừ tay 15 tỷ
	modify_treasury_effect = yes
}
remove_effect = {
	random_owned_controlled_state = { limit = { free_building_slots = … }
		add_building_construction = { type = arms_factory level = 1 instant_build = yes } }
	# × 2
}
```
và giải thích: *"Nhà máy được xây bằng `add_building_construction` và trả tiền trực tiếp, nên giá
không phụ thuộc vào việc hiệu ứng `one_state_arms_factory` của MD có tự trừ tiền hay không."*

**Vấn đề:** lập luận đó chỉ đúng *nếu* không gọi `one_state_arms_factory`. Nhưng `add_building_construction` thô
**thiếu ba thứ** mà bản MD có:
1. **không cộng `add_extra_state_shared_building_slots`** → nếu state hết slot, build **fail im lặng**, mất 15 tỷ
2. **không có fallback** sang state khác
3. `free_building_slots = { … include_locked = no }` (báo cáo dùng `no`) khác MD (`include_locked = yes`) → điều kiện chặt hơn, dễ xám hơn

Trong khi đó **repo đang dùng `one_state_*` ở 31 chỗ** (focus kinh tế), theo đúng mẫu:
```pdx
522 = { one_state_industrial_complex = yes }     # không trừ tiền tay — MD tự trừ
```

→ **Hai đường, phải chọn một (Q7):**
- **(a) Dùng `one_state_arms_factory`** (khuyên dùng): gọi trong scope state, **không** trừ tiền tay.
  D1 gọi 2 lần = 15 tỷ, D2 gọi 1 lần = 7,5 tỷ → tổng **22,5 tỷ, khớp đúng con số báo cáo**.
  Muốn đổi giá thì dùng cờ `skip_payment` rồi tự trừ.
- **(b) Giữ `add_building_construction` thô** như báo cáo: phải tự thêm
  `add_extra_state_shared_building_slots = 1` và tự viết fallback, nếu không sẽ có quyết định
  mất tiền mà không được nhà máy.

Con số 22,5 tỷ của báo cáo **chỉ đúng với phương án (a)** — đây có vẻ là ý thật của tác giả,
nhưng code mẫu ở 6.2 lại là (b) và tự trừ tiền. Nếu làm theo code mẫu 6.2 *mà* gọi
`one_state_arms_factory` thì thành **45 tỷ** (trừ đôi).

---

# PHẦN 3 — 5 LỖI VỀ PHÍA MILLENNIUM DAWN

## B1 · `can_staff_an_arms_factory` không tồn tại → **`can_staff_an_arms_industry`**

Đã tra `tools/audit/md_ref/00_economic_triggers.txt`. Cả họ:
```
can_staff_an_agriculture_district   can_staff_an_arms_industry   can_staff_an_composite_plant
can_staff_an_dockyard               can_staff_an_industrial_complex
can_staff_an_microchip_plant        can_staff_an_offices
```
Báo cáo tự ghi *"can_staff_an_arms_factory lấy từ báo cáo gốc của bạn"* — tức chưa kiểm chứng.
Trong repo: `can_staff_an_arms_factory` **0 lần**, `can_staff_an_industrial_complex` **15 lần**.

⚠️ Lưu ý: `can_staff_an_arms_industry` kiểm **nhân lực/việc làm**, không kiểm **slot trống**.
D1/D2 cần **cả hai** — xem mẫu code ở Phần 4.

## B2 · Effect MIO: cú pháp đúng là `mio:<org> = { … }`

Báo cáo viết "MIO GDT +2 size, +500 funds, +2 trait" nhưng không cho cú pháp.
Đã xác minh trong MD (`00_mio_scripted_effects.txt:218, 236, 250`; `00_startup_effects.txt:69`):

```pdx
mio:VIE_gdt_manufacturer = {
	add_mio_size = 2
	add_mio_funds = 500
}
```
- `add_mio_size` — **không nhận giá trị âm** (hoi4doc: *"Input value cannot be negative"*)
- `add_mio_funds` — **nhận âm được**; nếu vượt ngưỡng Size Up thì MIO **tự lên size**
  (hoi4doc: *"If the new total funds go over the Size Up limit, the MIO will gain size(s)"*)

⚠️ **Hệ quả logic:** báo cáo cho mỗi decision cả `+size` **và** `+funds`. Vì `add_mio_funds`
tự lên size khi vượt ngưỡng, cộng cả hai sẽ **lên size hai lần**. Cần quyết định:
chỉ `add_mio_size`, hay chỉ `add_mio_funds` và để MIO tự lên? Xem **Q8**.

## B3 · **Không thể "mở trait" bằng decision** — trait MIO do người chơi tự mua

Báo cáo mục 2.2 cột "Hoàn tất (remove_effect)" ghi *"MIO GDT +2 size, +500 funds, **+2 trait**"*.

Trong HOI4, MIO trait được **người chơi bấm mở** bằng funds, không có effect nào
"unlock trait" từ script. MD cũng không có — đã tra toàn bộ `md_ref/`: chỉ có
`add_mio_size`, `expenditure_for_mio_upgrade`, `mio_catalog_*`.

Cây trait đã có sẵn `all_parents` / `any_parent` / `mutually_exclusive` (bảng 1.3), tức là
**người chơi tự chọn đường đi**. Decision chỉ nên cấp **size + funds** để người chơi mở trait.

→ Bỏ "+2 trait" khỏi đặc tả. Nếu muốn decision **ép** mở một trait cụ thể thì phải dùng
`unlock_mio_trait_token` — nhưng token đó không có trong MD lẫn repo, và sẽ phá
`mutually_exclusive` sẵn có (`stv_family` ↔ `mass_production`). **Không nên làm.**

## B4 · `state_inhospitable` = 0 slot — đừng xây nhà máy ở đảo

`801` (Tây Trường Sa) là `state_inhospitable`, `local_building_slots = 0`.
Nếu dùng `random_owned_controlled_state` **không có `limit`** thì có thể rơi vào 801 → build fail.
Phải có `limit = { free_building_slots = { building = arms_factory size > 0 } }`.

Slot thật của 7 state lục địa VIE (đo từ `tools/audit/md_ref/`):

| State | `state_category` | `local_building_slots` | `arms_factory` sẵn |
|---|---|---:|---:|
| 522 Red River Delta | `state_11` | 40 | 1 |
| 519 Southern Vietnam | `state_11` | 40 | 0 |
| 518 Mekong Delta | `state_10` | 36 | 0 |
| 521 Central Vietnam | `state_10` | 36 | 0 |
| 520 Vietnamese Highlands | `state_06` | 22 | 0 |
| 523 Northern Vietnam | `state_06` | 22 | 0 |
| 524 Northwest Vietnam | `state_04` | 14 | 0 |
| 801 Western Spratlys | `state_inhospitable` | **0** | 0 |

Tổng ~210 slot cho 7 state → **không bao giờ thiếu slot** cho 3 nhà máy. Rủi ro duy nhất là
chọn nhầm 801.

## B5 · Mục 7.1 lo sai về state ID (giống Trục 1)

Báo cáo: *"Trong bản đồ vanilla, 517, 518 và 522 là state của Úc; nếu MD giữ số này thì ID
518, 522, 523 trong v7 không phải state Việt Nam."*

**MD đã đánh số lại toàn bộ.** Đo từ `history/states/`: `517-Southern Laos`,
`518-Mekong Delta` (VIE), `522-Red River Delta` (VIE, capital), `523-Northern Vietnam` (VIE).
→ 518/522/523 **là state Việt Nam thật**. Chi tiết: `VIE_md_states_reference.md`.

Kết luận "không dùng ID cố định" **vẫn nên giữ**, nhưng vì lý do đúng: bền qua các bản MD,
và tránh dồn hết nhà máy vào một state.

---

# PHẦN 4 — 7 LỖI LOGIC NỘI TẠI

## L1 · Cột "Giới hạn bởi" của D2 sai, báo cáo tự mâu thuẫn

Mục 2.5 dòng D2: *"Thực tế = max của 2017.1.1, D1 xong"* nhưng cột "Giới hạn bởi" ghi **"D1"**.
D1 xong 07/2011, còn mốc 2017.1.1 muộn hơn nhiều → **ràng buộc thật là "Ngày mở", không phải D1**.
Cùng lỗi ở D9. (D7 và D4 ghi đúng: giới hạn bởi D1 và D3.)

Không phá code, nhưng nếu ai đọc bảng để quyết định "muốn D2 sớm hơn thì làm D1 nhanh hơn"
sẽ mất công vô ích.

## L2 · "Chạy tuần tự 8 decision mất 22 năm" — **quá bi quan**

HOI4 **không giới hạn số decision chạy song song** (khác focus có slot). Nhìn lại bảng 1.1:
D5 (2012–2015), D3 (2013–2017), D7 (2011–2013) chồng lấn nhau; D2/D4/D9 cùng 2017–2019.

Chạy song song tối đa theo đúng ràng buộc:
```
D1   2008-07 → 2011-07
D7   2011-07 → 2013-06     (cần D1)
D5   2012-01 → 2014-12     (cần D1 + cờ T-54M3, mở 2012)
D3   2013-01 → 2016-12     (cần D1, mở 2013)
D4   2017-01 → 2019-01     (cần D3)
D2   2017-01 → 2019-01     (mở 2017)
D9   2017-01 → 2019-01     (mở 2017, cần cờ Igla)
D6   2021-01 → 2024-12     (mở 2021)
```
→ **hoàn tất 01/2025, tức ~17 năm** kể từ 2008, không phải 22. Con số 22 chỉ đúng nếu
người chơi cố tình không bao giờ chạy 2 decision cùng lúc.

Ràng buộc thật sự **không phải thời gian** mà là **tiền**: 30,25 tỷ cho 8 decision,
trong khi ngân khố VIE năm 2000 chỉ có **5 tỷ** (`history/countries/VIE - Vietnam.txt`:
`set_variable = { var = treasury value = 5 }`, `debt = 77.514`).
→ Đây mới là chỗ cần cân bằng, và báo cáo không phân tích.

## L3 · ⚠️ D2 có **hai** biến thể thời gian nhưng báo cáo chỉ tính một

Mục 2.2: D2 `days_remove` = **730 nếu có `VIE_iwi_license`, 1095 nếu không**.
Mục 2.5: chỉ ghi mốc 730 ngày ("01/2019, 01/2020 nếu không có license IWI") — chỗ này báo cáo
**có** ghi, nhưng bảng 4.1 của Trục 1 nói license chỉ có từ `.11` option A, mà `.11` có cửa sổ
2013–2015 và **có thể mất**.

Nếu người chơi mất `.11` → D2 là bản 1095 ngày → xong **01/2020** thay vì 01/2019.
Không phá gì, nhưng mục 2.4 (level) và mốc capstone "sớm nhất 01/2019" sẽ trượt một năm.
Báo cáo ghi capstone sớm nhất 01/2019 mà **không nói** con số đó giả định có license IWI.

## L4 · `VIE_def_industry_level` không được khởi tạo

Báo cáo dùng `check_variable = { VIE_def_industry_level >= 4 }` và `>= 8`.
Biến này **không tồn tại ở đâu trong repo** (đã grep: 0 kết quả).

HOI4 coi biến chưa đặt = 0, nên về mặt kỹ thuật vẫn chạy. Nhưng chính
`VIE_nationalist_regime_TDD.md` mục 7.3 của bạn đã tự nhắc:
*"Đặt rõ `VIE_arm_count`, `VIE_arm_done`, `VIE_capability_count`, `VIE_capability_done = 0`
ở N1, dù biến chưa đặt mặc định bằng 0."*
→ Áp dụng cùng nguyên tắc: đặt `set_variable = { VIE_def_industry_level = 0 }` ở
`on_startup` (`VIE_md_on_actions_startup.txt`) cùng chỗ với `VIE_congress_term`.

## L5 · Pháp lệnh CNQP: focus đã xoá, nhưng mốc ngày vẫn hợp lệ

Báo cáo: *"Giữ, đổi tên thành Pháp lệnh CNQP (02/2008/PL-UBTVQH12);
`available = { date > 2008.6.30 }`; không còn là cổng mở; +1 level.
Mốc theo ngày hiệu lực 01/07/2008, không theo ngày ký 26/01/2008."*

Lập luận về ngày hiệu lực vs ngày ký **đúng và nên giữ**. Nhưng focus đã bị v11 xoá →
phải dựng lại (Q6) hoặc chuyển +1 level sang một decision/event.

Lưu ý thêm: `date > 2008.6.30` nghĩa là **từ 01/07/2008** ✅ đúng ý.

## L6 · Ngã rẽ Core/Divest "Giữ" nhưng đã xoá — và `mutually_exclusive` cần focus

Báo cáo: *"VIE_military_enterprises_core / _divest — Giữ. Ngã rẽ loại trừ nhau, điều kiện ở 2.4."*

Hai focus này đã bị v11 xoá. Dựng lại thì phải đặt `mutually_exclusive` **đúng chiều**:
cả hai cùng trỏ nhau, và cả hai phải chung một `relative_position_id` để engine vẽ được.
Đây chính là loại lỗi mà `focus_tree_prerequisite_audit.md` của bạn từng phải dọn
("0 forward-ref, 0 duplicate cell").

Nếu chuyển ngã rẽ sang **decision** (phương án Q6-b) thì dùng đúng mẫu 6.4 của báo cáo:
hai decision loại trừ nhau bằng cờ (`visible = { NOT = { has_country_flag = … } }`) —
mẫu đó **đúng và đã kiểm chứng** (báo cáo viết chuẩn ở mục 6.4).

## L7 · `vie_def_ind.*` — 4 event chưa có namespace, và 2 cái trùng chức năng với decision

Mục 2.3:

| ID | Trigger theo báo cáo | Vấn đề |
|---|---|---|
| `vie_def_ind.1` Triển lãm | "ETD tháng 12 các năm 2022, 2024 và mỗi 2 năm sau đó; level ≥ 2" | **"mỗi 2 năm sau đó" là vô hạn** — mod kết thúc 2026/2035? Phải chốt năm cuối. Và "ETD" → dùng scheduler p15, không dùng `trigger_year_*` (lý do: `VIE_md_effects_p14.txt` header) |
| `vie_def_ind.2` Chuyển giao bảo dưỡng T-90 | `VIE_t90_purchased` + D1 xong | ✅ Trục 1 đã đặt `VIE_t90_purchased` |
| `vie_def_ind.3` Xuất khẩu vũ khí | "level ≥ 6, sau 2022" → **+0,25bn mỗi năm** | ⚠️ **"mỗi năm" cần `on_monthly` chia 12, hoặc event lặp**. Báo cáo không nói cơ chế. Đây là nguồn thu **vĩnh viễn** — cần trần |
| `vie_def_ind.4` Luật 38/2024/QH15 | ETD 2024.6.27; cần `VIE_def_industry_law` | ⚠️ `VIE_def_industry_law` **đã bị xoá** (A1) → trigger này không bao giờ đúng |

Thêm: **chưa có `add_namespace = vie_def_ind`** ở đâu. Phải tạo `events/VIE_def_ind.txt`.

`vie_def_ind.1` (+100 funds mỗi lần triển lãm) và `.4` (+150 funds cả 4 MIO) chồng lấn về
chức năng với `add_mio_funds` của decision — cần tính tổng để không phá cân bằng (xem Q8).

---

# PHẦN 5 — 4 QUYẾT ĐỊNH · **ĐÃ CHỐT CẢ BỐN = (a)** ngày 2026-09-30

> **Q6 = (a)** Dựng lại 4 focus (`VIE_def_industry_law`, `VIE_military_enterprises_core`,
> `VIE_military_enterprises_divest`, `VIE_path_self_reliant_deterrence`) dưới
> `VIE_modernize_vpa`. Hệ `VIE_def_industry_level` sống trên focus tree.
> **Q7 = (a)** Xây nhà máy bằng `one_state_arms_factory` trong scope state,
> **không** trừ tiền tay. D1 = 2 lần gọi = 15 tỷ, D2 = 1 lần = 7,5 tỷ → tổng 22,5 tỷ.
> **Q8 = (a)** MIO chỉ dùng `add_mio_size`. Funds chỉ cấp qua `vie_def_ind.*`.
> **Q9 = (a)** `vie_def_ind.3` (xuất khẩu vũ khí) trần **5 lần** rồi dừng.
>
> Plan ở Phần 6 viết theo đúng bốn lựa chọn này. Ghi chú "(Q6-a)"… trong phần dưới
> không còn là giả định nữa mà là quyết định đã chốt.

---

# PHẦN 5 (bản gốc) — 4 QUYẾT ĐỊNH CẦN BẠN CHỐT

## Q6 · Hệ `VIE_def_industry_level` sống ở đâu? (chặn)

4 focus nền (Pháp lệnh, Core, Divest, Capstone) đã bị v11 xoá. Ba đường:

| | Làm gì | Ưu | Nhược |
|---|---|---|---|
| **(a)** Dựng lại 4 focus dưới `VIE_modernize_vpa` | Pháp lệnh (cost 5, `date > 2008.6.30`) → ngã rẽ Core/Divest (ME, `level >= 4`) → Capstone (`level >= 8` + đã chọn ngã rẽ) | Đúng ý báo cáo nhất; lấp luôn "root mồ côi 0 con"; người chơi **thấy** quyết định chiến lược trên cây | Phải lo layout (x/y, `relative_position_id`, forward-ref) — đúng loại việc từng sinh ra `focus_tree_prerequisite_audit.md` |
| **(b)** Chuyển hết sang **decision** | 4 decision trong `VIE_def_industry_category`, loại trừ nhau bằng cờ theo mẫu 6.4 | Không đụng focus tree, không rủi ro layout; làm nhanh | Người chơi không thấy "ngã rẽ chiến lược" trên cây; mất tính kể chuyện |
| **(c)** Pháp lệnh + Capstone = focus; ngã rẽ = decision | Lai | Cân bằng | Phức tạp nhất, khó theo dõi |

**Đề xuất: (a)** — vì `VIE_modernize_vpa` đang là root mồ côi 0 con, và ngã rẽ Core/Divest
là quyết định lớn đáng được nhìn thấy. Nhưng (b) thì code nhanh hơn nhiều và an toàn hơn.

## Q7 · Xây nhà máy bằng gì? (chặn — xem A2)

| | | Tiền D1 | Rủi ro |
|---|---|---|---|
| **(a)** `one_state_arms_factory` trong scope state, **không** trừ tiền tay | khuyên dùng | 2 lần gọi = **15 tỷ** (MD tự trừ 7,5/lần) → khớp 22,5 tỷ của báo cáo | thấp — MD tự cộng slot + fallback |
| **(b)** `add_building_construction` thô + tự trừ 15 tỷ (đúng code mẫu 6.2) | | 15 tỷ | **cao** — hết slot thì fail im lặng, mất tiền |

**Đề xuất: (a)**, và dùng `limit` state để tránh 801 (B4).

## Q8 · MIO: `add_mio_size` hay `add_mio_funds`? (xem B2)

`add_mio_funds` **tự lên size** khi vượt ngưỡng. Báo cáo cho cả hai → lên size đôi.

| | | Kết quả |
|---|---|---|
| **(a)** chỉ `add_mio_size` | chắc chắn, đoán trước được | D1 +2, D2–D9 mỗi cái +1 → tổng +9 (khớp bảng mục V) |
| **(b)** chỉ `add_mio_funds` | MIO tự lên size theo ngưỡng | không đoán trước được tổng size |
| **(c)** cả hai như báo cáo | | **lên size đôi** — sai |

**Đề xuất: (a)** cho size, và funds chỉ dùng cho `vie_def_ind.*` (triển lãm, Luật 2024) —
đúng như bảng "Funds thêm ngoài decision" ở mục V. Nghĩa là decision **không** cấp funds.

## Q9 · `vie_def_ind.3` (xuất khẩu vũ khí, +0,25bn/năm) có trần không?

Hiện báo cáo để mở: level ≥ 6, sau 2022, **+0,25bn mỗi năm vĩnh viễn**.
Mod chạy tới 2035+ → 13 năm × 0,25 = **3,25 tỷ miễn phí**, trong khi cả Trục 2 tốn 30,25 tỷ.

Ba lựa chọn: (a) trần 5 năm rồi dừng · (b) giữ vĩnh viễn nhưng giảm còn 0,10bn/năm ·
(c) giữ nguyên. **Đề xuất (a)**.

---

# PHẦN 6 — PLAN CODE TRỤC 2 (đã vá toàn bộ lỗi trên)

> Plan này giả định **Q6=(a), Q7=(a), Q8=(a), Q9=(a)**. Nếu bạn chọn khác thì các bước
> 2 và 5 đổi, còn lại giữ nguyên.

## 6.0 · Kiến trúc

```
on_monthly (VIE_md_on_actions.txt)
   └─ VIE_event_scheduler_p15           ← MỚI, cùng mẫu p1–p14
        ├─ [catch-up?] → VIE_def_ind_catch_up (chỉ set cờ)
        ├─ vie_def_ind.1  Triển lãm      (12/2022, 12/2024, trần 2026 — Q9/a)
        ├─ vie_def_ind.2  Chuyển giao bảo dưỡng T-90   (cờ VIE_t90_purchased + D1 xong)
        ├─ vie_def_ind.3  Xuất khẩu vũ khí               (level ≥ 6, sau 2022, tối đa 5 lần)
        └─ vie_def_ind.4  Luật 38/2024/QH15              (2024.6.27)

focus tree (dưới VIE_modernize_vpa)     ← Q6(a)
   VIE_def_industry_law          (Pháp lệnh CNQP, date > 2008.6.30, +1 level)
        ├─ VIE_military_enterprises_core    (+2 level)  ┐ ME
        └─ VIE_military_enterprises_divest  (+1 level)  ┘  available: level >= 4
                    ▼ (OR)
   VIE_path_self_reliant_deterrence  (capstone, available: level >= 8 + đã chọn ngã rẽ)

common/decisions/VIE_md_def_industry.txt   ← MỚI, 9 decision D1–D9
common/decisions/categories/…              ← thêm VIE_def_industry_category
```

## 6.1 · Bảng decision (đã sửa theo B1, B2, A2)

| ID | Tên | `visible` | `available` | `days_remove` | `complete_effect` | `remove_effect` |
|---|---|---|---|---:|---|---|
| **D1** `VIE_dec_z_factories` | Hiện đại hóa nhà máy Z lục quân | `has_completed_focus = VIE_def_industry_law` | `date > 2008.6.30` + `can_staff_an_arms_industry` + `any_owned_state` còn slot `arms_factory` + `NOT has_country_flag VIE_dec_z_started` | 1095 | log + `set_country_flag VIE_dec_z_started` + `VIE_gdt_mio_size_2` | **2× `one_state_arms_factory`** (không trừ tiền tay) + `+1 level` + cờ `VIE_dec_z_factories_done` + MIO trait funds |
| **D2** `VIE_dec_stv` / `VIE_dec_stv_fast` | Súng STV (Z111) | `VIE_dec_z_factories_done` | `date > 2016.12.31` + `NOT VIE_dec_stv_started` | **1095 / 730** (hai decision ME theo cờ `VIE_iwi_license`, mẫu 6.4) | log + `VIE_dec_stv_started` | 1× `one_state_arms_factory` (−7,5 tỷ MD tự trừ) + 3000 `infantry_weapons_type` + `+1 level` + `VIE_dec_stv_done` |
| **D3** `VIE_dec_pth` | Pháo tự hành bánh lốp PTH (Z751) | `VIE_dec_z_factories_done` | `date > 2012.12.31` | 1460 | log + cờ started | 24× `SP_arty_2`/`medium_tank_artillery_chassis_2` + `+1 level` + `VIE_dec_pth_done` |
| **D4** `VIE_dec_ammo` | Đạn pháo nội địa 122/130/152mm | `VIE_dec_pth_done` | — | 730 | log + cờ started | `attrition −0.10` + `+1 level` |
| **D5** `VIE_dec_t54m` | T-54M nội địa (Z153) | `VIE_dec_z_factories_done` + `VIE_t54m3_prototype` | `date > 2011.12.31` | 1095 | log + cờ started | `VIE_proc_convert_t54m3` (**tái dùng effect Trục 1**) + `+1 level` |
| **D6** `VIE_dec_xcb01` / `_fast` | XCB-01 | `VIE_dec_z_factories_done` | `date > 2020.12.31` | **1460 / 1095** (ME theo `VIE_bmp3_lessons`) | log + cờ started | 50× `IFV_7`/`medium_tank_flame_chassis_4` + variant VIE tự tạo + `mechanized_attack_factor +5%` + `equipment_bonus` flame chassis −5% + `+1 level` |
| **D7** `VIE_dec_bm21` | Hiện đại hóa BM-21, đạn rocket 122mm | `VIE_dec_z_factories_done` | — | 730 | log + cờ started | chuyển đổi 36 BM-21 (`destroy_equipment`/amount âm — **cùng rủi ro `.6` Trục 1**) + `VIE_af_army_artillery_attack_factor +0.05` + `+10 army XP` + `+1 level` |
| **D8** `VIE_dec_k9_localization` | Nội địa hóa bảo dưỡng và đạn K9 | `VIE_dec_pth_done` + `VIE_k9_purchased` + `VIE_k9_localization` | — | 730 | log + cờ started | `+50% CAT_artillery` + MIO + **không** `+1 level` (đúng báo cáo) |
| **D9** `VIE_dec_tl01` | Tên lửa vác vai TL-01 (Z131) | `VIE_dec_z_factories_done` + `VIE_igla_license` | `date > 2016.12.31` | 730 | log + cờ started | `VIE_af_air_defence_factor +0.03` + `+1 level` |

**Ba cặp decision hai biến thể** (D2, D6) dùng đúng mẫu 6.4 của báo cáo — mẫu đó **đúng**:
`visible` theo cờ, `available` chặn bằng cờ `_started`, `remove_effect` gọi chung một
scripted effect để không lệch phần thưởng.

`+1 level` = `add_to_variable = { VIE_def_industry_level = 1 tooltip = VIE_tt_def_industry_level }`.

## 6.2 · Scripted effect dùng chung (chống lệch)

```pdx
# MIO: chi size, khong funds (Q8/a). add_mio_funds tu len size -> cong ca hai se len doi.
VIE_gdt_mio_size_2 = { mio:VIE_gdt_manufacturer = { add_mio_size = 2 } }
VIE_gdt_mio_size_1 = { mio:VIE_gdt_manufacturer = { add_mio_size = 1 } }

# Nha may: goi trong scope STATE. MD tu tru 7.5 ty, tu cong slot, tu fallback.
# KHONG tru tien tay o day (A2). limit loai 801 (state_inhospitable, 0 slot).
VIE_pick_state_for_arms_factory = {
	random_owned_controlled_state = {
		limit = {
			free_building_slots = { building = arms_factory size > 0 include_locked = yes }
		}
		one_state_arms_factory = yes
	}
}
```
**Không cần loại 801 bằng trigger riêng.** Đã tra: `has_state_category` **không xuất hiện**
trong bất kỳ file MD hay repo nào đã tải → chưa xác minh được là trigger hợp lệ, nên không dùng
(tránh lỗi `error.log`). Mà cũng không cần: `801` là `state_inhospitable` với
`local_building_slots = 0`, nên `free_building_slots = { … size > 0 }` **tự loại nó**.

`free_building_slots` là đủ, và là lựa chọn an toàn nhất vì nó đã được dùng 15 lần trong repo
(`can_staff_an_industrial_complex` cũng dựa trên họ trigger này) nên chắc chắn hợp lệ.
Không thêm `is_island_state` hay `has_state_category`: cả hai đều **không xuất hiện** trong
bất kỳ file MD hay repo nào đã tải, tức chưa xác minh được.

## 6.3 · Focus (Q6-a) — 4 focus, layout an toàn

```
VIE_modernize_vpa (x=266 y=1, đang là root mồ côi)
   └─ VIE_def_industry_law            x=0 y=1  rel=VIE_modernize_vpa   cost 5
        ├─ VIE_military_enterprises_core    x=-2 y=2  rel=VIE_def_industry_law  cost 7  ME divest
        └─ VIE_military_enterprises_divest  x= 2 y=2  rel=VIE_def_industry_law  cost 7  ME core
                    ▼ (prerequisite OR cả hai)
   VIE_path_self_reliant_deterrence   x=0 y=3  rel=VIE_def_industry_law  cost 10
```
Quy tắc layout lấy từ `focus_tree_prerequisite_audit.md` + `tools/audit/audit.py`:
- `relative_position_id` **chỉ trỏ focus khai báo TRƯỚC** trong file (0 forward-ref)
- không trùng toạ độ tuyệt đối, gap ≥ 2, con luôn `y > ` cha
- `mutually_exclusive` hai chiều
- sau khi thêm: chạy `python3 tools/audit/audit.py` phải ra **0** ở cả 5 kiểm tra

## 6.4 · File-by-file

| # | File | Việc | Dòng |
|---|---|---|---:|
| 1 | `common/scripted_effects/VIE_md_effects_p15.txt` | **MỚI** — scheduler p15, 4 effect `VIE_def_ind_*`, `VIE_gdt_mio_size_1/2`, `VIE_pick_state_for_arms_factory`, `VIE_def_ind_catch_up`, 9 effect `VIE_dN_reward` | ~380 |
| 2 | `common/scripted_triggers/VIE_md_triggers_p15.txt` | **MỚI** — `VIE_def_ind_gate_*` (gom Q6/Q9 như Trục 1 đã làm với `VIE_proc_gate_*`) | ~50 |
| 3 | `common/decisions/VIE_md_def_industry.txt` | **MỚI** — 11 decision (D1–D9, D2 và D6 mỗi cái 2 biến thể) | ~450 |
| 4 | `common/decisions/categories/VIE_md_categories.txt` | thêm `VIE_def_industry_category` (`visible = { has_completed_focus = VIE_def_industry_law }`) | +8 |
| 5 | `common/national_focus/VIE_md_focus.txt` | thêm 4 focus dưới `VIE_modernize_vpa` (Q6-a) | +140 |
| 6 | `events/VIE_def_ind.txt` | **MỚI** — `add_namespace = vie_def_ind` + 4 event | ~180 |
| 7 | `common/on_actions/VIE_md_on_actions.txt` | nối `VIE_event_scheduler_p15` | +1 |
| 8 | `common/on_actions/VIE_md_on_actions_startup.txt` | `set_variable = { VIE_def_industry_level = 0 }` (L4) | +2 |
| 9 | `common/scripted_effects/VIE_md_effects_p3.txt` | nối p15 vào `VIE_catch_up_schedule` | +1 |
| 10 | `localisation/english/VIE_md_events_p15_l_english.yml` | **MỚI** — loc 4 event + 11 decision name/desc + 4 focus name/desc + tooltip | ~90 |
| 11 | `localisation/english/replace/VIE_md_vi_mio_l_english.yml` | đã có 65 key trait MIO — **kiểm tra đủ chưa**, thêm nếu thiếu | ±5 |
| 12 | `common/scripted_effects/VIE_md_effects_p14.txt` | đổi gate `.11` từ `date > 2011.6.30` → `has_country_flag = VIE_dec_z_factories_done` (**trả nợ Q3**) | ±2 |
| 13 | `tools/TESTING.md` | thêm mục Trục 2 | +50 |
| 14 | `VIE_v9_flag_mapping.md` | cập nhật: 7 cờ Trục 1 giờ **đã có người đọc** | ±10 |

## 6.5 · Thứ tự thi công (7 bước, mỗi bước 1 commit)

| Bước | Việc | Kiểm chứng |
|---|---|---|
| **0** | `VIE_md_triggers_p15.txt` + `set_variable VIE_def_industry_level = 0` ở startup | `live.py` 0 missing |
| **1** | `VIE_md_effects_p15.txt`: chỉ `VIE_gdt_mio_size_*`, `VIE_pick_state_for_arms_factory`, `VIE_def_ind_catch_up`, scheduler **rỗng** + nối `on_actions` | console `effect VIE_pick_state_for_arms_factory = yes` trong scope state → 1 arms_factory, −7,5 tỷ |
| **2** | 4 focus (Q6-a) + category | `tools/audit/audit.py`: 0 dangling, 0 forward-ref, 0 cycle, 0 trùng toạ độ, 0 con ngang cha |
| **3** | D1 + D7 (hai decision đơn giản nhất, không có biến thể) | D1: 1095 ngày → 2 nhà máy, −15 tỷ, level +1, MIO +2 size |
| **4** | D2 (2 biến thể) + D3 + D4 | D2 bản 730 khi có `VIE_iwi_license`, 1095 khi không |
| **5** | D5 + D6 (2 biến thể) + D9 — nối 3 cờ Trục 1 | `VIE_t54m3_prototype` / `VIE_bmp3_lessons` / `VIE_igla_license` giờ **có người đọc** |
| **6** | D8 + 4 event `vie_def_ind.*` + scheduler p15 đầy đủ | `VIE_k9_purchased` + `VIE_k9_localization` có người đọc; `.3` dừng sau 5 lần (Q9-a) |
| **7** | Loc + đổi gate `.11` (trả nợ Q3) + cập nhật 2 tài liệu | `verify_all_loc.py` PASS; `live.py` 0 missing; **0 cờ Trục 1 mồ côi** |

## 6.6 · Checklist test

- [ ] `error.log` grep `vie_def_ind`, `VIE_dec_`, `VIE_def_industry`, `mio:VIE_gdt`, `one_state_arms_factory`, `add_mio_size`
- [ ] D1 bấm được từ 01/07/2008; trước đó decision **xám** với `custom_trigger_tooltip` giải thích
- [ ] D1 xong: **đúng 2** arms_factory xuất hiện, treasury **−15 tỷ đúng một lần** (không phải −30)
- [ ] Không có nhà máy nào rơi vào **801** (Tây Trường Sa, 0 slot)
- [ ] `can_staff_an_arms_industry` — tên đúng chưa? (B1: không phải `..._arms_factory`)
- [ ] MIO GDT: size +2 sau D1, +1 sau mỗi D2–D7/D9; **không lên size đôi** (Q8)
- [ ] Trait MIO: người chơi **tự mở** được bằng funds; `stv_family` ↔ `mass_production` vẫn loại trừ nhau
- [ ] D2 có `VIE_iwi_license` → 730 ngày; không có → 1095 ngày; không bao giờ thấy **cả hai** cùng lúc
- [ ] D6 có `VIE_bmp3_lessons` → 1095; không → 1460
- [ ] D5 chỉ hiện khi có `VIE_t54m3_prototype` (tức `.5` option A)
- [ ] D9 chỉ hiện khi có `VIE_igla_license` (tức `.8` option A)
- [ ] D8 chỉ hiện khi có **cả** `VIE_dec_pth_done` + `VIE_k9_purchased` + `VIE_k9_localization`
- [ ] Level đạt 4 → ngã rẽ Core/Divest mở; chọn Core thì Divest **biến mất** (ME)
- [ ] Level đạt 8 + đã chọn ngã rẽ → capstone mở; level 7 → **không** mở
- [ ] `vie_def_ind.3` dừng sau **5 lần** (Q9-a), không chạy vĩnh viễn
- [ ] `vie_def_ind.4` (Luật 2024) nổ 2024.6.27 — **trigger phải đổi** vì `VIE_def_industry_law` giờ là focus mới, không phải focus v7
- [ ] Catch-up: `effect set_variable = { VIE_catch_up = 1 } VIE_event_scheduler_p15 = yes` → không pop-up, cờ vẫn có
- [ ] Ngân khố: 8 decision tốn 30,25 tỷ nhưng VIE năm 2000 chỉ có **5 tỷ** — kiểm tra `modify_treasury_effect` có cho âm không, và MD có tự phát hành nợ không (báo cáo mục 6.1 nói có)

---

# PHỤ LỤC — những gì đã tra và lưu ở đâu

| Câu hỏi | Trả lời | Nguồn |
|---|---|---|
| `one_state_arms_factory` có tự trừ tiền? | **Có, −7,5 tỷ**, có `skip_payment`, tự cộng slot, có fallback | `tools/audit/md_ref/00_scripted_effects.txt:20` |
| `can_staff_an_arms_industry`? | ✅ có (không phải `..._arms_factory`) | `tools/audit/md_ref/00_economic_triggers.txt` |
| Cú pháp MIO? | `mio:<org> = { add_mio_size = N add_mio_funds = N }` | `tools/audit/md_ref/00_mio_scripted_effects.txt:218` + hoi4doc.dev |
| `add_mio_size` âm được không? | **Không** | hoi4doc.dev/item/effect-add_mio_size |
| `add_mio_funds` âm được không? | **Được**, và vượt ngưỡng thì **tự lên size** | hoi4doc.dev/item/effect-add_mio_funds |
| Có `unlock_mio_trait` trong MD? | **Không** | grep toàn bộ `md_ref/` |
| `modify_debt_effect`? | ✅ `00_budget_effects.txt:1499`, input `debt_change` | `tools/audit/md_ref/00_budget_effects.txt` |
| `small_expenditure` = ? | −0,2% GDP (MIO trait dùng cái này khi hết `free_trait_picks`) | `00_budget_effects.txt:1464` |
| State VIE và slot? | 7 lục địa (14–40 slot) + 801 (0 slot) | `tools/audit/md_ref/*.txt` + `VIE_md_states_reference.md` |
| Variant cho XCB-01? | **phải tự tạo** — VIE có 0 variant trong MD | `VIE_variant_research.md` mục 4.3 |
| `IFV_7` = năm nào? | 2025 (khớp XCB-01); `IFV_5` = 2005 (báo cáo ghi sai) | `VIE_variant_research.md` mục 2 |
