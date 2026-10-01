# NGHIÊN CỨU VARIANT & EQUIPMENT TRONG MILLENNIUM DAWN

> Nguồn: repo `MillenniumDawn/Millennium-Dawn` @ `main`, tải qua GitHub API ngày 2026-09-30.
> File gốc lưu tại `/home/user/tools/audit/md_ref/`.
>
> Tài liệu này **sửa lại kết luận B4** trong `VIE_truc1_review_and_plan.md` — kết luận đó sai.

---

## 1. ⚠️ Audit B4 SAI — báo cáo Trục 1 ĐÚNG

`VIE_truc1_review_and_plan.md` mục B4 kết luận rằng `medium_tank_flame_chassis_2`,
`medium_tank_rocket_chassis_N`, `medium_tank_artillery_chassis_N`, `medium_tank_aa_chassis_N`
**không tồn tại**. **Kết luận đó sai.**

Nguyên nhân sai: chỉ grep `common/units/equipment/MD_x_tank_chassis.txt`, thấy các tên đó nằm
trong khối `duplicate_archetypes` nên kết luận "chỉ là archetype, không có tier". Nhưng
`duplicate_archetypes` + `for_each` **tự sinh tier con** từ tier của archetype cha:

```pdx
# MD_x_tank_chassis.txt
duplicate_archetypes = {
	#IFV
	medium_tank_flame_chassis = {
		archetype = medium_tank_chassis
		type = { armor flame }
		for_each = {
			variant_name = { find_and_replace = { "chassis" "equipment" } }
		}
	}
	#MLRS
	medium_tank_rocket_chassis = { ... archetype = medium_tank_chassis ... }
	#SP Arty
	medium_tank_artillery_chassis = { ... }
	#SPAA
	medium_tank_aa_chassis = { ... }
	#APC
	medium_tank_amphibious_chassis = { ... }
	#Light Tank / TD
	medium_tank_destroyer_chassis = { ... }
}
```

Vì `medium_tank_chassis_0..6` tồn tại, nên `medium_tank_flame_chassis_0..6`,
`medium_tank_rocket_chassis_0..6`, `medium_tank_artillery_chassis_0..6`,
`medium_tank_aa_chassis_0..6`, `medium_tank_amphibious_chassis_0..6`,
`medium_tank_destroyer_chassis_0..6` **đều tồn tại**.

**Bằng chứng trực tiếp** — MD dùng chúng trong `history/countries/`:

| Tên chassis tier | Số lần dùng trong `SOV - Russia.txt` |
|---|---:|
| `medium_tank_artillery_chassis_1` | 16 |
| `medium_tank_aa_chassis_0` | 11 |
| `medium_tank_amphibious_chassis_0` | 10 |
| `medium_tank_amphibious_chassis_1` | 8 |
| `medium_tank_aa_chassis_1` | 8 |
| `medium_tank_rocket_chassis_1` | 7 |
| `medium_tank_destroyer_chassis_0` | 7 |
| `medium_tank_rocket_chassis_0` | 5 |
| `medium_tank_flame_chassis_1` | 4 |
| `medium_tank_flame_chassis_0` | 4 |
| **`medium_tank_flame_chassis_2`** | **2** ← BMP-3 |
| `medium_tank_destroyer_chassis_2` | 3 |
| `medium_tank_artillery_chassis_2` | 3 |
| `medium_tank_flame_chassis_2` | 2 |

Cũng xuất hiện trong `CHI - China.txt` và `KOR - Korea.txt`.

→ **Bảng equipment ở mục 6.5 của báo cáo Trục 1 là ĐÚNG cho cả hai cột NSB và non-NSB.**
Chỉ có một chỗ báo cáo sai thật: **T-90S dùng `medium_tank_chassis_3`** — phải là `_2` (xem mục 3).

---

## 2. Cách MD tổ chức equipment armor

Có **hai họ song song**, cùng tồn tại, không loại trừ nhau:

| Họ | Định nghĩa ở | Dùng khi | Năm từng tier |
|---|---|---|---|
| **Chassis NSB** — `medium_tank_chassis_N`, `medium_tank_flame_chassis_N`, `medium_tank_artillery_chassis_N`, `medium_tank_rocket_chassis_N`, `medium_tank_aa_chassis_N`, `medium_tank_amphibious_chassis_N`, `medium_tank_destroyer_chassis_N` | `MD_tank_chassis.txt` (tier cha) + `duplicate_archetypes` trong `MD_x_tank_chassis.txt` (tier con tự sinh) | có DLC *No Step Back* — phải design variant | `_0`=1922 · `_1`=1975 · `_2`=1995 · `_3`=2015 · `_4`=2035 · `_5`=2055 · `_6`=2075 |
| **Equipment non-NSB** — `MBT_N`, `IFV_N`, `APC_N`, `SP_arty_N`, `SP_R_arty_N`, `SP_Anti_Air_N`, `Rec_tank_N` | `MD_x_tank_chassis.txt` khối `equipments` | không có NSB — cấp thẳng, không cần variant | xem bảng dưới |

Archetype của họ non-NSB chính là họ chassis:

| Equipment | Archetype |
|---|---|
| `MBT_1..8` | `medium_tank_chassis` |
| `IFV_1..8` | `medium_tank_flame_chassis` |
| `APC_1..8` | `medium_tank_amphibious_chassis` |
| `SP_arty_0..4` | `medium_tank_artillery_chassis` |
| `SP_R_arty_0..4` | `medium_tank_rocket_chassis` |
| `SP_Anti_Air_0..4` | `medium_tank_aa_chassis` |

### Bảng năm (đo từ MD, dùng để chọn tier)

| Năm | 1965 | 1975 | 1985 | 1995 | 2005 | 2015 | 2025 | 2035 |
|---|---|---|---|---|---|---|---|---|
| `MBT_N` | 1 | 2 | 3 | 4 | — | 5 | 7 | 8 |
| `IFV_N` / `APC_N` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| `SP_arty_N` / `SP_R_arty_N` / `SP_Anti_Air_N` | 0 | — | 1 | — | 2 | — | 3 | 4 |
| `medium_tank_chassis_N` | 0 (1922) | 1 | — | 2 | — | 3 | — | 4 |

**⚠️ Không có `MBT_6`.** MD nhảy từ `MBT_5` (2015) sang `MBT_7` (2025).

---

## 3. Bảng equipment ĐÚNG cho Trục 1 (đã sửa)

| Hệ thống | Năm vào biên chế | NSB (`type` + `variant_name`) | non-NSB (`type`) | `producer` |
|---|---|---|---|---|
| T-54/55 (≈70, Phần Lan chuyển giao) | 1965 | `medium_tank_chassis_0` + **"T-55A"** | `MBT_1` | **SOV** ← không phải FIN |
| T-72 (150, Ba Lan, alt) | 1975 | `medium_tank_chassis_1` + **"T-72M1"** | `MBT_2` | POL |
| T-54M (nâng cấp nội địa Z153) | — | `medium_tank_chassis_0` + **"T-54M"** *(tự tạo)* | `MBT_1` | VIE |
| **T-90S/SK** (32/64/128) | 1995 | `medium_tank_chassis_2` + **"T-90"** | `MBT_4` | SOV |
| BMP-3 (30, alt) | 1987 | `medium_tank_flame_chassis_2` + **"BMP-3"** | `IFV_3` | SOV |
| K9A1 (20/40) | 1999 | `medium_tank_artillery_chassis_2` + **"K9 Thunder"** | `SP_arty_2` | KOR |
| TOS-1A (12, alt) | 2001 | `medium_tank_rocket_chassis_1` + **"TOS-1"** | `SP_R_arty_1` | SOV |
| BM-21 (D7, Trục 2) | 1963 | `medium_tank_rocket_chassis_0` | `SP_R_arty_0` | VIE |
| PTH (D3, Trục 2) | ~2017 | `medium_tank_artillery_chassis_2` | `SP_arty_2` | VIE |
| XCB-01 (D6, Trục 2) | 2025 | `medium_tank_flame_chassis_4` | **`IFV_7`** ← báo cáo ghi `IFV_5` (2005), quá cũ | VIE |
| Igla / TL-01 | — | không cấp equipment, chỉ modifier | — | — |

### Sai sót của báo cáo đã sửa

| Báo cáo ghi | Đúng | Lý do |
|---|---|---|
| T-90S → `medium_tank_chassis_3` | **`medium_tank_chassis_2`** | `chassis_2`=1995 khớp T-90; `chassis_3`=2015 lệch một thế hệ. MD cũng dùng `chassis_2` cho variant "T-90" và "T-90A". Báo cáo ghi *"v7 lệch: variant chassis_1, NSB chassis_2"* rồi "sửa" thành `_3` — **sửa ngược** |
| XCB-01 → `IFV_5` | **`IFV_7`** | `IFV_5`=2005, XCB-01 ra mắt 2025. `IFV_7`=2025 |
| T-54/55 → `producer = FIN` | **`producer = SOV`** | Phần Lan **không có** variant T-54/55 nào trong MD. Variant thuộc về nước định nghĩa nó, nên `producer` phải là nước đó. Hàng này do SOV sản xuất, Phần Lan chỉ chuyển giao → SOV đúng cả kỹ thuật lẫn lịch sử |

---

## 4. Variant: cơ chế và những gì MD đã có sẵn

### 4.1 Quy tắc bắt buộc

1. **NSB cần `variant_name`** thì xe mới dùng được trong sư đoàn. Cấp `type` trần = chassis
   không thiết kế nằm trong kho, không lắp vào division template được.
2. **`producer` phải là nước định nghĩa variant.** MD định nghĩa variant trong
   `history/countries/<TAG> - <Name>.txt`. Ghi `producer` sai → lỗi "no variant found".
3. **`create_equipment_variant` trùng tên sẽ tạo bản version 2, 3…** → phải guard bằng cờ
   nếu gọi từ event có thể chạy nhiều lần.
4. **`model`** phải là entity có thật (MD dùng `SOV_T55A_entity`, `SOV_BMP3_entity`, …).
5. **`design_team = mio:<org>`** — org phải có `equipment_type` phủ loại xe.
   `VIE_gdt_manufacturer` có `mio_cat_all_armor` ✅ nên nhận được armor.

### 4.2 Variant MD đã có sẵn — **không cần tạo**

| Variant | `type` | Định nghĩa trong | Dùng cho |
|---|---|---|---|
| **`T-90`** | `medium_tank_chassis_2` | `SOV - Russia.txt:2230` | T-90S/SK ✅ |
| `T-90A` | `medium_tank_chassis_2` | `SOV - Russia.txt:2257` | (bản nội địa Nga, không dùng) |
| `T-55A` / `T-55AD` / `T-55AM` / `T-55AMV` / `T-55AMD-1` | `medium_tank_chassis_0` | `SOV - Russia.txt` | T-54/55 ✅ (dùng `T-55A`) |
| `T-62` / `T-62M` / `T-62MV` | `medium_tank_chassis_0` | `SOV - Russia.txt` | — |
| `T-72 Ural` / `T-72A` / `T-72AV` / `T-72B` / `T-72B obr.1989` | `medium_tank_chassis_1` | `SOV - Russia.txt` | — |
| `T-80` / `T-80B` / `T-80BV` / `T-80U` | `medium_tank_chassis_1` | `SOV - Russia.txt` | — |
| **`BMP-3`** | `medium_tank_flame_chassis_2` | `SOV - Russia.txt` | BMP-3 (alt) ✅ |
| `BMP-1` / `BMP-2` / `BMD-1..3` | `flame_chassis_0/1/2` | `SOV - Russia.txt` | — |
| **`T-72M1`** / `PT-91` | `medium_tank_chassis_1` | `POL - Poland.txt` | T-72 Ba Lan ✅ |
| **`K9 Thunder`** | `medium_tank_artillery_chassis_2` | `KOR - Korea.txt:340` | K9A1 ✅ |
| `KIFV Vulcan SPAAG` | `medium_tank_aa_chassis_1` | `KOR - Korea.txt` | — |

`SOV - Russia.txt` có tổng cộng **289** `create_equipment_variant`.

### 4.3 Variant phải TỰ TẠO (VIE có 0 variant trong MD)

`history/countries/VIE - Vietnam.txt` có **0** `create_equipment_variant`.
OOB của VIE dùng chassis trần:
- `VIE_2000_nsb.txt`: `medium_tank_chassis_0`, `artillery_1`, `infantry_weapons_1/2/3`
- `VIE_2000_nonnsb.txt`: `MBT_1`, `IFV_1`, `IFV_3`, `APC_1`, `APC_2`, `SP_arty_0`, `SP_R_arty_0`, `SP_Anti_Air_0`

Nghĩa là **mọi nâng cấp nội địa** (T-54M ở Z153, PTH ở Z751, XCB-01, TL-01…) đều phải tự tạo
variant với `producer = VIE`.

Đã tạo ở bước 4: **`VIE_proc_create_t54m_variant`** trong
`common/scripted_effects/VIE_md_effects_p14.txt`, có guard `VIE_t54m_variant`.

Module set lấy theo mẫu `T-55AM` của MD + `reactive_armor_gen1` (T-54M thật gắn giáp phản
ứng nổ; báo cáo mục 2.2 D5 ghi "FCS Indra, ERA trong nước"):

```pdx
create_equipment_variant = {
	name = "T-54M"
	type = medium_tank_chassis_0
	parent_version = 0
	modules = {
		main_armament_slot = tank_small_medium_cannon
		secondary_armament_slot = afv_coax_machine_gun_2
		ammunition_load_slot = mixed_main_ammo_2
		turret_type_slot = tank_soviet_turret
		suspension_type_slot = tank_torsion_bar_suspension_medium
		armor_type_slot = tank_steel_armor_gen1
		engine_type_slot = tank_diesel_engine_gen2
		reload_type_slot = manual_loading
		special_type_slot_1 = smoke_launchers
		special_type_slot_2 = additional_mg
		special_type_slot_3 = smoothbore_atgm_gen1
		special_type_slot_4 = tank_battlestation_2
		special_type_slot_6 = reactive_armor_gen1
	}
	upgrades = { tank_nsb_armor_upgrade = 2 }
	model = "SOV_T55A_entity"
	design_team = mio:VIE_gdt_manufacturer
}
```

Tất cả 14 module và `tank_nsb_armor_upgrade` **đã xác minh tồn tại**:
- Module: `MD_tank_modules.txt` (295 module) — `reactive_armor_gen1` dòng 5684, `tank_battlestation_2` dòng 5301, `tank_steel_armor_gen1` dòng 4695
- Upgrade: `MD_land_upgrades.txt` — `tank_nsb_armor_upgrade` (MD dùng 48 lần trong `SOV - Russia.txt`, 8 lần `KOR`, 6 lần `POL`)
- Model: `SOV_T55A_entity` dùng 5 lần trong `SOV - Russia.txt`
- Không module nào có `required_tech` → không cần `set_technology` kèm

`allow_using_required_premium_dlc` **không** được dùng — MD không dùng tham số này ở bất kỳ
variant nào (0 lần trong SOV/KOR/POL/CHI). Đã bỏ.

### 4.4 Variant TOS-1 — phát hiện ở bước 6

`SOV - Russia.txt:3588` **có sẵn** variant `"TOS-1"` trên `medium_tank_rocket_chassis_1`,
và MD tự cấp 8 xe variant này cho SOV ở dòng 3610. Variant có đầy đủ module
(`main_armament`, `ammunition_load`, `engine`, `tank_nsb_fire_upgrade = 3`) và icon riêng
`gfx/interface/technologies/SOV/LAND/TOS-1.dds`.

→ **Không cần tự tạo variant cho TOS-1A.** Dùng `"TOS-1"` + `chassis_1` (1985).
TOS-1A là bản nâng cấp 2001 của TOS-1; MD không tách variant riêng nên dùng chung và
ghi chú trong loc rằng đây là bản A.

Lưu ý: audit lúc đầu đề xuất `medium_tank_rocket_chassis_2` / `SP_R_arty_2` (tier 2005,
khớp năm TOS-1A nhập ngũ). **Đổi sang `chassis_1` / `SP_R_arty_1`** vì có variant sẵn —
xe dùng được trong sư đoàn ngay quan trọng hơn khớp năm một tier.

### 4.5 Variant — ĐÃ TẠO XONG CẢ BỐN (Trục 1 bước 4 + Trục 2 bước 1)

| Variant | `type` | Effect tạo | Guard | Đã xác minh |
|---|---|---|---|---|
| `T-54M` | `medium_tank_chassis_0` | `VIE_proc_create_t54m_variant` (p14) | `VIE_t54m_variant` | module theo mẫu `T-55AM` của MD + `reactive_armor_gen1` |
| `PTH-152` | `medium_tank_artillery_chassis_2` | `VIE_proc_create_pth_variant` (p15) | `VIE_pth_variant` | module theo mẫu `K9 Thunder` của KOR |
| `XCB-01` | `medium_tank_flame_chassis_4` | `VIE_proc_create_xcb01_variant` (p15) | `VIE_xcb01_variant` | module theo mẫu `BMP-3` của SOV |
| `BM-21M` | `medium_tank_rocket_chassis_0` | `VIE_proc_create_bm21m_variant` (p15) | `VIE_bm21m_variant` | module theo mẫu `TOS-1` của SOV |
| `TL-01` | — | không cần | — | MANPADS không cấp equipment, chỉ modifier |

Cả bốn đều `producer = VIE`, `design_team = mio:VIE_gdt_manufacturer` (hợp lệ vì org
này có `mio_cat_all_armor` trong `equipment_type`), và **không** đặt `model`
(VIE không có entity riêng; đặt model sai sẽ lỗi — MD đặt `model = "SOV_T55A_entity"`
cho T-55 vì entity đó có thật).

**23/23 module và 2/2 upgrade đã xác minh tồn tại** trong
`tools/audit/md_ref/MD_tank_modules.txt` (295 module) + `MD_arty_modules.txt`
(170 module) + `MD_land_upgrades.txt`. Ba module viết sai lúc đầu và đã sửa:
`afv_autocannon_3` → `afv_assault_gun_3` + `afv_coax_autocannon_3`;
`rocket_launcher_gen1` → `art_med_rocket_gen1` + `thirty_two_missile_pack`;
`rocket_ammo_1` → `artillery_heavy_ammo_1`.

**Thứ tự bắt buộc:** gọi effect tạo variant **TRƯỚC** khi `add_equipment_to_stockpile`.
Nếu cấp xe trước mà variant chưa tồn tại thì xe nằm trong kho không lắp được vào
sư đoàn. `VIE_d7_reward` từng bị thiếu bước này và đã sửa ở Trục 2 bước 5.

**Trước khi tự tạo variant, luôn grep `history/countries/<TAG>.txt` của MD trước** —
như trường hợp TOS-1, có sẵn thì khỏi tạo và khỏi phải lo module/upgrade/model sai.

---

## 5. Checklist khi cấp equipment trong mod này

```pdx
# MẪU CHUẨN — dùng cho mọi lần cấp xe
if = {
	limit = { has_dlc = "No Step Back" }
	add_equipment_to_stockpile = {
		type = <chassis tier>
		variant_name = "<tên variant>"
		amount = <N>
		producer = <TAG sở hữu variant>
	}
}
else = {
	add_equipment_to_stockpile = { type = <equipment non-NSB> amount = <N> producer = <TAG> }
}
```

- [ ] `type` NSB tra bảng năm mục 2, **không** đoán
- [ ] `variant_name` có thật trong `history/countries/<producer>.txt` của MD, **hoặc** đã tự tạo với `producer = VIE`
- [ ] `producer` = nước định nghĩa variant
- [ ] non-NSB dùng đúng họ (`MBT`/`IFV`/`APC`/`SP_arty`/`SP_R_arty`/`SP_Anti_Air`) — không có `MBT_6`
- [ ] Nếu tự tạo variant: guard bằng cờ để không tạo trùng
- [ ] Nếu tự tạo variant: mọi module tra trong `MD_tank_modules.txt`, upgrade trong `MD_land_upgrades.txt`, `model` trong danh sách entity MD dùng
- [ ] `design_team = mio:VIE_gdt_manufacturer` chỉ dùng khi org đó có `equipment_type` phủ loại xe

---

## 6. File MD đã tải về để tra

```
tools/audit/md_ref/SOV_Russia.txt          history/countries/SOV - Russia.txt      (289 variant)
tools/audit/md_ref/POL.txt                 history/countries/POL - Poland.txt
tools/audit/md_ref/KOR.txt                 history/countries/KOR - Korea.txt
tools/audit/md_ref/CHI.txt                 history/countries/CHI - China.txt
tools/audit/md_ref/VIE_Vietnam.txt         history/countries/VIE - Vietnam.txt     (0 variant)
tools/audit/md_ref/VIE_2000_nsb.txt        history/units/VIE_2000_nsb.txt
tools/audit/md_ref/VIE_2000_nonnsb.txt     history/units/VIE_2000_nonnsb.txt
tools/audit/md_ref/MD_tank_chassis.txt     common/units/equipment/                 (chassis tier cha)
tools/audit/md_ref/MD_x_tank_chassis.txt   common/units/equipment/                 (duplicate_archetypes + non-NSB)
tools/audit/md_ref/MD_tank_modules.txt     .../modules/                            (295 module)
tools/audit/md_ref/MD_land_upgrades.txt    .../upgrades/
tools/audit/md_ref/MD_artillery.txt        common/units/equipment/
tools/audit/md_ref/MD_infantry_equipment.txt
tools/audit/md_ref/equipment_archetypes.md common/units/equipment/                 (bảng ID ↔ tên hiển thị)
tools/audit/md_ref/00_budget_effects.txt   modify_treasury_effect, modify_debt_effect
tools/audit/md_ref/00_economic_triggers.txt  can_staff_an_*
tools/audit/md_ref/00_yearly_effects.txt   trigger_year_* (70 effect)
tools/audit/md_ref/MD_on_actions.txt       chỗ gọi trigger_year_[year]_events (dòng 904)
tools/audit/md_ref/00_game_rules.txt       MD_FOCUS_TREE_RULES, rule_salafist_branch
```
