# Tài liệu Triển khai 3 Trục Lục quân (Mua sắm, CNQP, Lực lượng) — Millennium Dawn

> **Tài liệu tổng hợp đánh giá, nghiên cứu & kế hoạch code (08/10/2026)**  
> Hợp nhất 3 tài liệu phân mảnh của 3 trục Lục quân Việt Nam.

## Mục lục
1. [Phần 1: Review Trục 1 (Mua sắm Lục quân) + Plan Code](#phần-1-review-trục-1-mua-sắm-lục-quân--plan-code)
2. [Phần 2: Review Trục 2 (CNQP Lục quân) + Plan Code](#phần-2-review-trục-2-cnqp-lục-quân--plan-code)
3. [Phần 3: Review Trục 3 (Xây dựng Lực lượng Lục quân) + Plan Code](#phần-3-review-trục-3-xây-dựng-lực-lượng-lục-quân--plan-code)

---
## Phần 1: Review Trục 1 (Mua sắm Lục quân) + Plan Code

# REVIEW TRỤC 1 (MUA SẮM) + PLAN CODE

> Đầu vào: `Báo cáo Lục quân VIE — Trục 1, 2, 3.docx` (29/9/2026), mục **I. Trục 1: Mua sắm**
> Đối chiếu với: `SomnvK123/hoi4-md-vietnam-` @ `f05cfa1` (30/9/2026) và repo gốc
> `MillenniumDawn/Millennium-Dawn` @ `main` (tải trực tiếp qua GitHub API ngày 30/9/2026).
>
> **KẾT LUẬN: Trục 1 CHƯA code được ngay.** Có **3 lỗi chặn**, **6 chỗ sai về phía Millennium Dawn**,
> và **12 lỗi nội tại** trong thiết kế. Phần dưới liệt kê từng lỗi kèm bằng chứng, rồi đưa ra plan
> code đã vá sẵn.

---

# PHẦN 1 — 3 LỖI CHẶN (blocker)

## A1 · Báo cáo viết cho cây focus **v7**; repo đang ở **v11**

Mọi focus mà Trục 1 dùng làm điều kiện đều **đã bị xoá**. Đo trực tiếp trên `common/national_focus/VIE_md_focus.txt` (256 focus live):

| Focus báo cáo dựa vào | Vai trò trong Trục 1 | Còn sống? | Nằm ở đâu |
|---|---|---|---|
| `VIE_t90_tanks` | "→ thay bằng event" | ❌ | chỉ còn trong `.bak` (đã xoá từ **v9**) |
| `VIE_rocket_artillery` | "→ chuyển sang Trục 2 D7" | ❌ | `v11_removed_military_all_subbranches.txt` |
| `VIE_army_short_range_ad` | **trigger của `.8`** + "Trục 1 giữ" | ❌ | `v11_removed_military_all_subbranches.txt` |
| `VIE_mechanization` | "Trục 1 giữ" (mẫu cơ giới) | ❌ | `v11_removed_military_all_subbranches.txt` |
| `VIE_army_c4isr` | "Trục 1 giữ" (planning/recon/EW) | ❌ | `v11_removed_military_all_subbranches.txt` |
| `VIE_tank_modernization` | **trigger của `.5`** + cổng mở nhóm decision | ❌ | `v11_removed_military_all_subbranches.txt` |
| `VIE_russian_arms_deals` | **trigger của `.14`** | ❌ | chỉ còn trong `.bak` (xoá từ **v9**) |
| `VIE_def_industry_law` | Trục 2, nhưng `.11` gate theo D1 | ❌ | `v11_removed_military_other_focuses.txt` |
| `VIE_z_factories`, `VIE_licensed_rifles` | → D1, D2 | ❌ | `v11_removed_military_other_focuses.txt` |
| `VIE_modernize_vpa` | — | ✅ **root mồ côi, 0 con** | live, x=266 y=1 |

**Hệ quả trực tiếp:**
- `.5` (`has_completed_focus = VIE_tank_modernization`) → **không bao giờ nổ**. Cửa sổ 2009–2012 đóng, D5 khoá vĩnh viễn.
- `.8` (`has_completed_focus = VIE_army_short_range_ad`) → **không bao giờ nổ**. D9 khoá vĩnh viễn.
- `.14` (`has_completed_focus = VIE_russian_arms_deals`) → **không bao giờ nổ**. Mất T-90, `vie_def_ind.2` không nổ.
- Mục 3.7 ("ranh giới với ba focus Trục 1 giữ lại") **vô hiệu toàn bộ** — không còn focus nào để giữ.
- Mục 7.1 ("các focus giữ lại còn dùng ID cũ, `VIE_army_short_range_ad` ở 522 và 521") — focus đó không tồn tại.

**Đã có tiền lệ sửa đúng:** commit `f05cfa1` đã re-point gate của decision category từ `VIE_tank_modernization` → `VIE_modernize_vpa`. Trục 1 phải làm y hệt: **mọi trigger focus đổi sang `VIE_modernize_vpa`** (hoặc bỏ hẳn gate focus, chỉ gate theo ngày + cờ).

## A2 · `VIE_paracel_ultimatum` đang **soft-lock vĩnh viễn** — và Trục 1 là chỗ phải vá

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
Quét toàn bộ file live:

| cờ | số lần SET | số lần ĐỌC |
|---|---:|---:|
| `VIE_ev_kilo_submarines` | **0** | 1 |
| `VIE_ev_bastion_p_coastal_defence` | **0** | 1 |

v9 đã đổi 19 gate `has_completed_focus` → `has_country_flag = VIE_ev_<slug>` với ghi chú *"Event mua sam **BAT BUOC** set cac co nay"*. Nhưng commit `f05cfa1` đã **xoá sạch** `events/VIE_md_mil.txt` (300 dòng → 1 dòng comment) nên không còn event nào set cờ. → Focus không bao giờ mở được.

Đây chính là hợp đồng mà **Trục 1 phải thực hiện**. Nhưng Trục 1 là **lục quân** — nó không mua tàu ngầm Kilo hay Bastion-P (hải quân/phòng thủ bờ). Nên phải **quyết định lại gate** (xem Phần 5, câu hỏi Q1).

## A3 · Hai tài liệu v9 **chưa từng được commit** → mapping cờ `VIE_ev_*` đã mất

Header v9 trong focus file ghi:
- *"Khoi focus goc duoc xuat ra `v9_removed_focuses_for_events.txt`"*
- *"Event mua sam BAT BUOC set cac co nay (xem `VIE_v9_flag_mapping.md`)"*

Kiểm tra `git log --all --diff-filter=A` trên **cả 3 nhánh**: **không có commit nào thêm hai file này.** Chúng không tồn tại ở bất kỳ đâu.

→ Phải **dựng lại bảng mapping cờ** từ đầu. Plan ở Phần 4, bước 6 có bảng đề xuất.

---

# PHẦN 2 — 6 CHỖ SAI VỀ PHÍA MILLENNIUM DAWN

## B1 · 🚨 **KHÔNG ĐƯỢC** định nghĩa lại `trigger_year_XXXX_events` (mục 6.3 của báo cáo)

Báo cáo đề nghị:
```pdx
trigger_year_2016_events = {
	if = { limit = { country_exists = VIE } VIE = { VIE_try_proc_14 = yes } }
}
```

**Cách MD thật sự vận hành** (`common/on_actions/MD_on_actions.txt:904`, trong `on_monthly`, tháng 1):
```pdx
meta_effect = {
    text = { trigger_year_[year]_events = yes }
    year = "[?global.year]"
}
```
`trigger_year_2016_events` là **một scripted effect duy nhất, thân phẳng**, chứa event của ~25 nước:
`ENG, HOL, USA, FRA, CHI, ARM, BOS, CAN, DEN, GER, HKG, ITA, JAP, MNT, MOR, NIG, PER, POL, SIA, SIN, SPR, TAI, …`

**Scripted effect trùng tên trong HOI4 = GHI ĐÈ, không gộp.** Submod load sau MD → đoạn code trên **xoá sạch toàn bộ event năm 2016 của MD cho mọi quốc gia khác**. Và phải làm thế cho 70 effect (`trigger_year_2001` … `trigger_year_2040`+).

MD **không có hook mở rộng** nào cho submod trong `00_yearly_effects.txt` (đã grep: 0 kết quả cho `submod|_hook|extra|VIE`).

**→ Bắt buộc dùng scheduler riêng của mod.** Mod đã có sẵn kiến trúc này và đang chạy tốt: `VIE_event_scheduler` … `_p13` treo trên `on_monthly` trong `common/on_actions/VIE_md_on_actions.txt`, guard bằng `original_tag = VIE` (sống sót qua nội chiến), có `VIE_popup_cd` và `VIE_catch_up`. Trục 1 chỉ cần thêm **`VIE_event_scheduler_p14`**.

## B2 · `trigger` **CÓ** chặn event bắn bằng `country_event` — báo cáo ghi "chưa xác minh"

Đã xác minh. HOI4 Wiki, *Event modding*, mục Effect:
> *"`trigger = { ... }` of the event gets checked **when it would fire**, meaning that it's also possible to fire the event on startup of the game with a needed delay … then use the event's trigger to simulate additional requirements."*
> *"…the effect firing it has a delay (**where the trigger would check if when the event is to be received**)."*

**Hệ quả: thiết kế ở mục 1.6 của báo cáo sẽ làm mất chuỗi vĩnh viễn.**
Báo cáo viết: *"Cờ `VIE_proc_N_fired` đặt trong `VIE_try_proc_N` **ngay khi gọi event**, để không nổ đôi"* + *"Event vẫn giữ trigger giống hệt"*.

Kịch bản hỏng: `VIE_try_proc_5` thấy đủ điều kiện → đặt `VIE_proc_5_fired` → hẹn `.5` sau `days = 1`. Trong 1 ngày đó `ISR` bị annex / VIE vào chiến tranh → `trigger` của `.5` chặn → event **không nổ**. Nhưng cờ đã đặt → `VIE_try_proc_5` không bao giờ chạy lại → **chuỗi T-54M3 chết, D5 khoá, không log, không dấu vết.**

**Cách vá (đã đưa vào plan):**
1. Cờ đóng chuỗi (`VIE_proc_N_closed`) đặt trong **`immediate` của event**, không phải trong scheduler.
2. Scheduler **luôn hẹn lại retry** chừng nào chưa thấy cờ và còn trong cửa sổ.
3. Giữ `trigger` của event làm lưới an toàn — giờ nó **an toàn** vì retry sẽ chạy tiếp.

## B3 · `can_staff_an_arms_factory` **không tồn tại** (mục 6.2 của báo cáo)

Đã tải `common/scripted_triggers/00_economic_triggers.txt` của MD. Cả họ staffing trigger thật:

```
can_staff_an_agriculture_district
can_staff_an_arms_industry      ← tên đúng cho nhà máy vũ khí
can_staff_an_composite_plant
can_staff_an_dockyard
can_staff_an_industrial_complex
can_staff_an_microchip_plant
can_staff_an_offices
```

Báo cáo tự ghi *"can_staff_an_arms_factory lấy từ báo cáo gốc của bạn"* — tức chưa kiểm chứng. Kiểm trong repo của bạn: `can_staff_an_arms_factory` xuất hiện **0 lần** (cả live lẫn archive), trong khi `can_staff_an_industrial_complex` dùng **15 lần**. → Đổi thành **`can_staff_an_arms_industry`**.

*(Đây là lỗi Trục 2, nhưng nằm chung trong mục VI "Script theo quy ước MD" mà Trục 1 cũng dùng.)*

## B4 · ~~Cột NSB của bảng equipment (mục 6.5) sai có hệ thống~~ — **ĐÃ RÚT LẠI, báo cáo ĐÚNG**

> ⚠️ **KẾT LUẬN NÀY SAI. Đã xác minh lại ngày 2026-09-30 khi code bước 4.**
> Xem `VIE_variant_research.md` (trong repo) mục 1 để có bản đúng.
>
> Nguyên nhân sai: chỉ grep `MD_x_tank_chassis.txt`, thấy các tên chassis nằm trong khối
> `duplicate_archetypes` nên kết luận "chỉ là archetype, không có tier". Nhưng
> `duplicate_archetypes` + `for_each` **tự sinh tier con** từ tier của archetype cha
> (`medium_tank_chassis_0..6`) → `medium_tank_flame_chassis_0..6`,
> `medium_tank_rocket_chassis_0..6`, `medium_tank_artillery_chassis_0..6`,
> `medium_tank_aa_chassis_0..6` … **đều tồn tại**.
> Bằng chứng: `SOV - Russia.txt` dùng `medium_tank_artillery_chassis_1` 16 lần,
> `medium_tank_aa_chassis_0` 11 lần, **`medium_tank_flame_chassis_2` 2 lần (BMP-3)**, …
>
> **Bảng 6.5 của báo cáo đúng cho cả hai cột NSB và non-NSB.** Chỉ có ba chỗ sai thật,
> đều đã sửa trong code:
> 1. **T-90S → `medium_tank_chassis_3`**: phải là **`_2`**. `chassis_2`=1995 khớp T-90;
>    `chassis_3`=2015. Báo cáo ghi *"v7 lệch: variant chassis_1, NSB chassis_2"* rồi
>    "sửa" thành `_3` — **sửa ngược**. MD cũng dùng `chassis_2` cho variant "T-90".
> 2. **XCB-01 → `IFV_5`** (2005): phải là **`IFV_7`** (2025).
> 3. **T-54/55 → `producer = FIN`**: phải là **`producer = SOV`** — Phần Lan không có
>    variant T-54/55 nào trong MD, và variant thuộc về nước định nghĩa nó.
>
> Phần dưới đây GIỮ LẠI NGUYÊN VĂN để đối chiếu, nhưng **mọi dòng "❌ không tồn tại"
> đều sai**.

### (bản gốc, đã rút lại)

Đã tải `common/units/equipment/MD_x_tank_chassis.txt` và `MD_tank_chassis.txt`.

MD khai báo `medium_tank_aa_chassis`, `medium_tank_artillery_chassis`, `medium_tank_destroyer_chassis`, `medium_tank_amphibious_chassis`, `medium_tank_flame_chassis`, `medium_tank_rocket_chassis` trong khối **`duplicate_archetypes`** — tức chúng là **archetype**, và MD **không khai báo tier `_0/_1/_2/…` nào cho chúng**.

Bảng của báo cáo vs thực tế:

| Báo cáo viết | Thực tế trong MD main |
|---|---|
| `medium_tank_flame_chassis_2` (BMP-3) | ❌ **không tồn tại** → dùng `IFV_3` (1985, archetype `medium_tank_flame_chassis`) |
| `medium_tank_flame_chassis_4` (XCB-01) | ❌ **không tồn tại** → dùng `IFV_6`/`IFV_7` |
| `medium_tank_rocket_chassis_N` (BM-21, TOS-1A) | ❌ **không tồn tại** → dùng `SP_R_arty_0..4` |
| `medium_tank_artillery_chassis_N` (PTH, K9A1) | ❌ **không tồn tại** → dùng `SP_arty_0..4` |
| `medium_tank_aa_chassis_N` (SPAA) | ❌ **không tồn tại** → dùng `SP_Anti_Air_0..4` |
| `medium_tank_chassis_0..6` (NSB designer) | ✅ tồn tại |
| `MBT_1..8`, `IFV_1..8`, `SP_arty_0..4`, `SP_R_arty_0..4`, `SP_Anti_Air_0..4`, `APC_1..8`, `Rec_tank_0..5` | ✅ tồn tại (**không có `MBT_6`**) |

**Bảng năm thật (đo từ MD) — dùng cái này để chọn tier:**

| họ | 1922 | 1965 | 1975 | 1985 | 1995 | 2005 | 2015 | 2025 | 2035 |
|---|---|---|---|---|---|---|---|---|---|
| `medium_tank_chassis_N` (NSB) | `_0` | — | `_1` | — | `_2` | — | `_3` | — | `_4` |
| `MBT_N` | — | `1` | `2` | `3` | `4` | — | `5` | `7` | `8` |
| `IFV_N` | — | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` |
| `SP_arty_N` | — | `0` | — | `1` | — | `2` | — | `3` | `4` |
| `SP_R_arty_N` | — | `0` | — | `1` | — | `2` | — | `3` | `4` |
| `SP_Anti_Air_N` | — | `0` | — | `1` | — | `2` | — | `3` | `4` |

**Suy ra: báo cáo "sửa" T-90S từ `chassis_2` thành `chassis_3` là SỬA NGƯỢC.**
`MBT_4` = **1995**, `medium_tank_chassis_2` = **1995**, `medium_tank_chassis_3` = **2015**.
Cặp đúng là **`MBT_4` ↔ `medium_tank_chassis_2`**. v7 dùng `chassis_2` là đúng; báo cáo ghi *"v7 lệch: variant chassis_1, NSB chassis_2"* rồi đẩy lên `chassis_3` → lệch một thế hệ.

**OOB thật của VIE trong MD** (tải `history/units/VIE_2000_nsb.txt` và `VIE_2000_nonnsb.txt`):
- NSB: `medium_tank_chassis_0`, `artillery_1`, `infantry_weapons_1/2/3`
- non-NSB: `MBT_1`, `IFV_1`, `IFV_3`, `APC_1`, `APC_2`, `SP_arty_0`, `SP_R_arty_0`, `SP_Anti_Air_0`, `artillery_1`, `infantry_weapons_1/2/3`

→ Xác nhận T-54/55 = `medium_tank_chassis_0` (NSB) / `MBT_1` (non-NSB) ✅ báo cáo đúng chỗ này.

## B5 · Mục 7.1 lo **sai** về state ID (tin tốt)

Báo cáo: *"Trong bản đồ vanilla, 517, 518 và 522 là state của Úc; nếu MD giữ số này thì ID 518, 522, 523 trong v7 không phải state Việt Nam."*

**MD đã đánh số lại toàn bộ bản đồ.** Đo từ `history/states/` của MD main:

| ID | MD |
|---|---|
| **517** | `517-Southern Laos.txt` (không phải Úc) |
| **518** | `518-Mekong Delta.txt` — `owner = VIE`, `add_core_of = VIE` ✅ |
| **522** | `522-Red River Delta.txt` — `owner = VIE`, `capital` ✅ |
| **523** | `523-Northern Vietnam.txt` — `owner = VIE` ✅ |

Vậy **518/522/523 trong v7 là state Việt Nam thật**, không phải lỗi. (Chi tiết đầy đủ 12 state + 81 province: `VIE_md_states_reference.md`.)

Kết luận *"D1 và D2 không dùng ID cố định mà chọn state VIE còn slot"* **vẫn nên giữ** — nhưng vì lý do khác: `random_owned_controlled_state` + `free_building_slots` bền hơn qua các bản MD, và tránh dồn hết nhà máy vào một state.

⚠️ **Nhưng có lỗi state thật ở chỗ khác** (đã báo lần trước, vẫn chưa sửa): `VIE_spratly_fortification`, `VIE_dk1_platforms`, `VIE_storm_resilient_islands`, `VIE_paracel_ultimatum` đang nhắm state **526** (Bắc Trường Sa, `owner = CHI`) thay vì **801** (Tây Trường Sa, `owner = VIE`) / **813** (Hoàng Sa). Trục 1 không đụng 4 focus này, nhưng **nên sửa cùng đợt** vì `.14`–`.16` (T-90) và wargoal Hoàng Sa nằm cùng chuỗi logic.

## B6 · Những chỗ báo cáo **ĐÚNG** (đã kiểm chứng, khỏi lo)

| Giả định của báo cáo | Kết quả |
|---|---|
| Tag `SOV` = Nga | ✅ `SOV = "countries/Russia.txt"` |
| Tag `POL`, `FIN`, `ISR`, `KOR`, `FRA` | ✅ tồn tại đủ |
| `modify_treasury_effect` | ✅ `common/scripted_effects/00_budget_effects.txt` |
| `modify_debt_effect` | ✅ cùng file — **báo cáo đúng khi dùng nợ cho T-90** |
| Nhóm rule `MD_FOCUS_TREE_RULES` | ✅ MD có 3 rule dùng nhóm này (`rule_salafist_branch` là mẫu tốt) |
| `infantry_weapons_type` | ✅ `MD_infantry_equipment.txt`; repo bạn đã dùng ở `VIE_md_decisions.txt:40` |
| `has_active_mission = bankruptcy_incoming_collapse` | ✅ repo bạn dùng 20 lần, error.log sạch |
| `is_triggered_only = yes` + `trigger` cùng tồn tại | ✅ hợp lệ (wiki xác nhận) |
| MIO `VIE_gdt_manufacturer` | ✅ `common/military_industrial_organization/organizations/VIE_md_organizations.txt:175`, đã có sẵn 8 trait (`licensed_rifles`, `stv_family`, `mass_production`, `ammunition_plants`, `towed_artillery`, `rocket_artillery`, `vehicle_overhaul`, `arsenal_of_the_people`) |
| Quy ước tab / `log` mọi option / K=5 | ✅ khớp `tools/TESTING.md` và code hiện có |
| Số học 7.95bn (tối đa) | ✅ cộng lại đúng |

---

# PHẦN 3 — 12 LỖI NỘI TẠI TRONG THIẾT KẾ TRỤC 1

## C1 · `.15` fire 2 lần → **cộng modifier 2 lần**

Báo cáo: *"`vie_proc_army.15` (giao hàng, **lặp theo đợt**)"*, option A giao "2 đợt 32 + 32".
Mỗi lần `.15` nổ lại chạy: `army_armor_attack_factor +5%`, `army_armor_defence_factor +3%`, `+10 army XP`, `set_country_flag = VIE_t90_purchased`.
→ Nhánh A và B nhận **+10% / +6%** thay vì +5% / +3%, và **+20 army XP**.

**Vá:** tách `.15` (đợt 1) và **`.16` (đợt 2 — ID mới, báo cáo bỏ trống số này**). `.16` chỉ giao xe, không lặp modifier/XP.

## C2 · `.15` không biết mỗi đợt bao nhiêu xe

A = 32+32, B = 64+64, C = 32 một đợt. Báo cáo không định nghĩa cơ chế truyền số lượng.

**Vá:** `.14` đặt `set_variable = { VIE_t90_batch = 32 }` (A/C) hoặc `64` (B); `.15`/`.16` đọc `add_equipment_to_stockpile = { type = … amount = VIE_t90_batch }` — hoặc an toàn hơn, đặt sẵn 3 scripted effect `VIE_deliver_t90_small/medium/large` và gọi theo cờ.

## C3 · Số ngày giao hàng **lệch lịch sử ~6 tháng**

Báo cáo: A giao "sau ~900 và ~960 ngày". Từ ETD 01/2016: `+900d` ≈ **06/2018**, `+960d` ≈ **08/2018**.
Lịch sử (nguồn Jane's mà chính báo cáo dẫn): ký 2016, **giao 12/2018 và 02/2019**.
→ Cần **~1065 ngày** và **~1125 ngày**. Chuỗi B (`~900` và `~1270`) cũng nên tính lại theo mốc ký.

## C4 · Thiếu tier equipment cho 4 hệ thống

Báo cáo để trống `N` trong `SP_arty_N` (PTH, K9A1), `SP_R_arty_N` (BM-21, TOS-1A). Đề xuất theo bảng năm ở B4:

| Hệ thống | Năm vào biên chế | non-NSB | NSB | producer |
|---|---|---|---|---|
| T-54/55 (≈70, Phần Lan) | 1965 | `MBT_1` | `medium_tank_chassis_0` | `FIN` |
| T-72 (150, Ba Lan, alt) | 1975 | `MBT_2` | `medium_tank_chassis_1` | `POL` |
| T-90S/SK (32/64/128) | 1995 | `MBT_4` | `medium_tank_chassis_2` | `SOV` |
| BMP-3 (30, alt) | 1987 | `IFV_3` | `medium_tank_chassis_2` + variant IFV | `SOV` |
| K9A1 (20/40) | 1999 | `SP_arty_2` | `SP_arty_2` | `KOR` |
| TOS-1A (12, alt) | 2001 | `SP_R_arty_2` | `SP_R_arty_2` | `SOV` |
| BM-21 (D7, Trục 2) | 1963 | `SP_R_arty_0` | `SP_R_arty_0` | — |
| PTH (D3, Trục 2) | ~2017 | `SP_arty_2` | `SP_arty_2` | — |
| XCB-01 (D6, Trục 2) | 2025 | **`IFV_7`** (báo cáo ghi `IFV_5` = 2005, quá cũ) | — | — |
| Igla / TL-01 | — | không cấp equipment, chỉ modifier ✅ | | |

## C5 · 🚨 **Ngân sách pop-up bị phá, báo cáo không nhắc `VIE_popup_cd` một lần nào**

Mod đang có luật riêng (`tools/TESTING.md`, mục *Balance sanity*):
> *"Pop-ups: never two within 30 days (except chained events), **at most 5 in any calendar year**."*

Cơ chế thực thi là cờ `VIE_popup_cd` (45 ngày) — **mọi scheduler p1–p13 đều set cờ này trước khi fire**. Mẫu chuẩn trong `VIE_md_effects.txt:254`:
```pdx
if = {
	limit = { NOT = { check_variable = { VIE_catch_up = 1 } } }
	set_country_flag = { flag = VIE_popup_cd days = 45 }
	country_event = { id = vie_pol.2 days = 3 random_days = 15 }
}
```
Thiết kế Trục 1 (mục 1.4/1.6) **không có** `VIE_popup_cd` ở bất kỳ đâu.

Đếm event đã lên lịch sẵn trong 13 scheduler hiện tại, rồi cộng Trục 1 vào:

| Năm | Đã có | + Trục 1 | Tổng | (+ alt-history) |
|---|---:|---:|---:|---:|
| 2005 | 3 | +1 (`.1`) | **4** | |
| 2006 | 4 | +1 (`.2`) | **5** ⚠️ | |
| 2009 | 2 | +2 (`.5`,`.8`) | **4** | |
| 2010 | 3 | — | 3 | **+3 = 6** ❌ (`.30`,`.31`,`.32`) |
| 2013 | 3 | +1 (`.11`) | **4** | |
| 2015 | 3 | — | 3 | **+2 = 5** ⚠️ (`.38`,`.39`) |
| 2016 | 5 | +1 (`.14`) | **6** ❌ | **+1 = 7** ❌ (`.40`) |
| 2018 | 6 | +1 (`.15`) | **7** ❌ | |
| 2019 | 5 | +1 (`.16`) | **6** ❌ | |
| 2023 | 6 | +1 (`.18`) | **7** ❌ | |
| 2025 | 3 | +1 (`.19`) | **4** | |
| 2026 | 2 | +1 (`.20`) | **3** | |
| 2027 | 0 | +1 (`.21`) | **1** | |

(2021 hiện đã là 12 — nợ cũ của mod, không phải của Trục 1.)

**Vá:** mọi `VIE_try_proc_N` phải (a) đọc `NOT = { has_country_flag = VIE_popup_cd }` như một phần điều kiện fire, và (b) `set_country_flag = { flag = VIE_popup_cd days = 45 }` ngay trước `country_event`. Vì retry chạy mỗi 30 ngày, pop-up bị chặn sẽ tự dời sang tháng sau — **không mất chuỗi**.

## C6 · `VIE_catch_up` không được xử lý

Mod có chế độ catch-up (`VIE_md_effects.txt:229`):
> *"Catch-up mode (temp variable `VIE_catch_up = 1`): only sets the 'already happened' flags, **fires nothing**. Used when a civil-war winner takes over the VIE lineage."*

Nếu Trục 1 không theo, người chơi thắng nội chiến năm 2024 sẽ bị **dội ngược 13 pop-up mua sắm từ 2005–2024** trong vài tick.

**Vá:** `VIE_event_scheduler_p14` mở đầu bằng `if = { limit = { NOT = { check_variable = { VIE_catch_up = 1 } } } } … else = { VIE_proc_catch_up = yes }`, trong đó `VIE_proc_catch_up` chỉ `set_country_flag` các cờ `VIE_proc_*_closed` + cờ kết quả lịch sử (`VIE_t90_purchased`, `VIE_k9_purchased`, `VIE_igla_license`, `VIE_iwi_license`, `VIE_t54m3_prototype`) mà **không** cấp xe / không trừ tiền.

## C7 · Số học "3.10bn treasury" cộng nhầm nợ vào treasury

Mục 1.5 ghi *"Tổng 3.10 (lịch sử)"*, nhưng chính mục 1.4 chuỗi 5 option A ghi *"**nợ** +1.25bn"* và mục 6.1 ghi *"Hợp đồng vay tín dụng (T-90) ghi vào nợ bằng `modify_debt_effect` **thay vì** trừ treasury"*.

Đúng phải là: **treasury 1.85bn + nợ 1.25bn = 3.10bn tổng chi phí**. Mục V ("Tổng kết số liệu") cũng ghi *"Kịch bản lịch sử tốn 33.35bn treasury"* — cùng lỗi cộng gộp. Không phá code, nhưng sẽ làm bạn cân bằng sai ngân sách.

## C8 · Đã xử lý: rule mua sắm riêng

Audit ngày 07/10/2026 xác nhận `VIE_alt_history` chỉ có một lựa chọn mặc định và không có reader trong code. Rule rỗng đã bị xoá. Giữ `rule_vie_alt_procurement` làm gate duy nhất cho các chuỗi mua sắm giả định 7–9; đề xuất tái dùng `VIE_alt_history` trong báo cáo cũ không còn áp dụng.

Lưu ý convention: MD viết `name = yes` / `name = VIE_HISTORICAL` **không có dấu ngoặc kép**. Báo cáo viết `name = "VIE_ALT_OFF"` — bỏ ngoặc kép cho khớp `has_game_rule = { rule = … option = VIE_ALT_ON }`.

## C9 · Thiếu namespace và ~95 key localisation

- `events/VIE_md_mil.txt` hiện **không còn** `add_namespace = vie_mil` (đã bị xoá ở `f05cfa1`). File mới phải có `add_namespace = vie_proc_army`.
- 19 event hiện + 1 event mới (`.16`) + 5 event ẩn = **25 event**. Event ẩn không cần loc. 20 event thường × (`.t` + `.d` + 2–4 option) ≈ **90–95 key**.
- 5 key cho rule: `RULE_VIE_ALT_PROCUREMENT`, `VIE_ALT_OFF_TEXT/_DESC`, `VIE_ALT_ON_TEXT/_DESC`.
- Repo đang có sẵn **966 key loc chết**, trong đó ~249 thuộc nhánh quân sự đã xoá (`VIE_t90_tanks`, `VIE_kilo_submarines`, `VIE_bastion_p_coastal_defence`, …). **Nên dọn cùng đợt** để khỏi nhầm key cũ/mới.
- File loc phải **UTF-8 có BOM** — `tools/verify_all_loc.py` kiểm tra cái này và hiện đang PASS; đừng làm vỡ.

## C10 · `add_equipment_to_stockpile` với `amount` âm — dùng `destroy_equipment` thay thế

Mục 6.5 báo cáo: *"trừ xe cũ bằng `add_equipment_to_stockpile` với amount âm (**cần thử trong game**)"*.

Không cần thử: HOI4 có effect chuyên dụng **`destroy_equipment = { type = X amount = N }`**. Dùng cái đó cho việc "chuyển đổi 100 T-54/55 thành T-54M3" (`.6`, D5) và "chuyển đổi 36 BM-21" (D7). `amount` âm có hành vi không đảm bảo và có thể đẩy stockpile xuống âm.

## C11 · Chuỗi 4 (`.11`) gate theo **D1 của Trục 2** → vòng phụ thuộc

Báo cáo: `.11` trigger = *"D1 đã xong, ISR tồn tại"*, cửa sổ 2013–2015.
Nhưng D1 thuộc Trục 2, `days_remove = 1095`, mở sớm nhất 01/07/2008 → xong sớm nhất **07/2011**. Khớp cửa sổ 2013 ✅.

Vấn đề là **thứ tự thi công**: nếu code Trục 1 trước, D1 chưa tồn tại → `.11` không bao giờ nổ, và license Galil ACE (cờ `VIE_iwi_license`) mất → D2 luôn là bản 1095 ngày.

**Vá:** code Trục 1 với gate tạm `has_completed_focus = VIE_modernize_vpa` + `date > 2011.6.30`, rồi đổi sang `has_country_flag = VIE_dec_z_factories_done` khi Trục 2 D1 land. Ghi rõ `# TODO(truc2)` tại chỗ.

## C12 · `.1` giao xe "tự động" nhưng lại có option từ chối

Mục 1.4: *"`vie_proc_army.1` (ETD 2005) — **Tự động**: Phần Lan chuyển giao ~70 T-54/55 → +70 T-54/55, −0.05bn"* rồi mới tới `├─ A: Nhận lời Ba Lan` / `└─ B: Từ chối`.

Rõ ràng phần giao xe phải nằm ở **`immediate`**, hai option chỉ quyết định vụ Ba Lan. Đúng, nhưng báo cáo không nói thẳng → dễ code nhầm thành effect của option A. Ghi rõ trong plan.

---

# PHẦN 4 — PLAN CODE TRỤC 1 (đã vá toàn bộ 21 lỗi trên)

## 4.0 · Kiến trúc đã chốt

```
on_monthly (VIE_md_on_actions.txt)
   └─ VIE_event_scheduler_p14            ← MỚI, cùng mẫu p1–p13
        ├─ [catch-up?] → VIE_proc_catch_up (chỉ set cờ)
        └─ VIE_try_proc_1 / 2 / 5 / 8 / 11 / 14 / 18
           VIE_try_proc_30 / 35 / 38      (chỉ khi rule_vie_alt_procurement = VIE_ALT_ON)
                 │
                 ├─ đủ điều kiện + popup_cd trống → country_event vie_proc_army.N (days 1, random 14)
                 │                                    └─ immediate: set VIE_proc_N_closed + VIE_popup_cd 45d
                 ├─ còn trong cửa sổ               → country_event vie_proc_army.9x (days 30, hidden)
                 │                                    └─ immediate: gọi lại VIE_try_proc_N
                 └─ hết cửa sổ                     → set VIE_proc_N_closed + log (chuỗi mất)
```

**KHÔNG đụng vào `trigger_year_*` của MD.** Retry 30 ngày thay vì 90 (rẻ, và tự xử lý luôn vụ `VIE_popup_cd` chặn).

## 4.1 · Bảng ID event (đã lấp lỗ hổng của báo cáo)

| ID | Nội dung | Loại |
|---|---|---|
| `.1` | Xe tăng cũ châu Âu — Phần Lan giao ≈70 T-54/55 (`immediate`), option A/B vụ Ba Lan | popup |
| `.2` | Huỷ / giữ hợp đồng T-72 Ba Lan | popup |
| `.5` | T-54M3 — mẫu thử Israel, 3 option | popup |
| `.6` | (nhánh B của `.5`) chuyển đổi 100 T-54/55 sau 1095 ngày | popup |
| `.8` | Igla kèm quyền sản xuất, 3 option | popup |
| `.11` | License Galil ACE cho Z111, 2 option | popup |
| `.14` | T-90S/SK — 4 option, đặt `VIE_t90_batch` | popup |
| `.15` | **Giao T-90 đợt 1** — xe + modifier + XP + `VIE_t90_purchased` + `VIE_ev_t90_tanks` | popup |
| **`.16`** | **MỚI — Giao T-90 đợt 2** — **chỉ** cấp xe, không lặp modifier/XP | popup |
| `.18` | K9A1 — đánh giá (2 option), hẹn `.19` | popup |
| `.19` | K9A1 — mua 20/40/không | popup |
| `.20` | Giao K9A1 + `VIE_k9_purchased` | popup |
| `.21` | Nội địa hoá / mua đạn dẫn hướng / giữ nguyên | popup |
| `.30` `.31` `.32` | BMP-3 (alt) | popup |
| `.35` | TOS-1A (alt) | popup |
| `.38` `.39` `.40` | CAESAR (alt) | popup |
| **`.90` `.91` `.92` `.93` `.94`** | retry ẩn cho `.5` `.8` `.11` `.14` `.18` | `hidden = yes` |
| **`.95` `.96` `.97`** | **MỚI** — retry ẩn cho `.30` `.35` `.38` (alt cũng cần, vì gate rule có thể bật giữa game) | `hidden = yes` |

`.3` `.4` `.7` `.9` `.10` `.12` `.13` `.17` `.22`–`.29` `.33` `.34` `.36` `.37` `.41`–`.89` `.98` `.99` để trống, dành cho Trục 2 (`vie_def_ind.*` dùng namespace riêng).

## 4.2 · Bảng cờ — hợp đồng tích hợp (thay cho `VIE_v9_flag_mapping.md` đã mất)

| Cờ | Đặt bởi | Đọc bởi |
|---|---|---|
| `VIE_proc_N_closed` (N = 1,2,5,8,11,14,18,30,35,38) | `immediate` của event **hoặc** nhánh hết-cửa-sổ | `VIE_try_proc_N` (chặn retry) |
| `VIE_pl_t72_deal` | `.1` option A | `.2` (điều kiện vào) |
| `VIE_t54m3_prototype` | `.5` option A | **D5** (Trục 2) |
| `VIE_igla_license` | `.8` option A | **D9** (Trục 2) |
| `VIE_iwi_license` | `.11` option A | **D2** bản 730 ngày (Trục 2) |
| `VIE_t90_batch` *(variable, 32/64)* | `.14` option A/B/C | `.15`, `.16` |
| `VIE_t90_purchased` | `.15` immediate | `vie_def_ind.2` (Trục 2) |
| **`VIE_ev_t90_tanks`** | `.15` immediate | **v9 contract** — focus còn sống đọc `VIE_ev_*` |
| `VIE_k9_purchased` | `.20` immediate | **D8** (Trục 2) |
| `VIE_bmp3_lessons` | `.32` option A | **D6** bản 1095 ngày (Trục 2) |
| `VIE_155mm_study` | `.40` immediate | `.18` mở từ 2021 + đánh giá 365 ngày |
| `VIE_popup_cd` (45 ngày) | mọi event popup | **toàn bộ scheduler p1–p14** |

🚩 **Hai cờ orphan phải xử lý (A2):** `VIE_ev_kilo_submarines` và `VIE_ev_bastion_p_coastal_defence` — Trục 1 (lục quân) **không thể** set. Xem **Q1**.

## 4.3 · File-by-file

| # | File | Việc | Dòng ước tính |
|---|---|---|---:|
| 1 | `events/VIE_proc_army.txt` | **MỚI** — `add_namespace = vie_proc_army` + 20 event popup + 8 event ẩn | ~1 100 |
| 2 | `events/VIE_md_mil.txt` | **XOÁ** (còn 1 dòng comment, namespace `vie_mil` không ai dùng) | −1 |
| 3 | `common/scripted_effects/VIE_md_effects_p14.txt` | **MỚI** — `VIE_event_scheduler_p14`, 10 × `VIE_try_proc_N`, `VIE_proc_catch_up`, `VIE_deliver_t90`, `VIE_deliver_k9` | ~420 |
| 4 | `common/scripted_effects/VIE_md_mil_gauges.txt` | **XOÁ** (2 effect rỗng) | −5 |
| 5 | `common/ideas/VIE_md_ideas_mil.txt` | **XOÁ** (`ideas = { country = { } }` rỗng) | −4 |
| 6 | `common/on_actions/VIE_md_on_actions.txt` | thêm `VIE_event_scheduler_p14 = yes`; **bỏ** `VIE_mil_gauges_monthly` + `_p2` | ±3 |
| 7 | `common/game_rules/VIE_md_rules.txt` | thêm `rule_vie_alt_procurement` (nếu chốt Q4 = giữ rule riêng) | +16 |
| 8 | `common/national_focus/VIE_md_focus.txt` | sửa gate `VIE_paracel_ultimatum` (A2) theo Q1 | ±6 |
| 9 | `localisation/english/VIE_md_events_p14_l_english.yml` | **MỚI** — ~95 key, UTF-8 **có BOM** | ~95 |
| 10 | `localisation/english/VIE_md_rules_l_english.yml` | thêm 5 key rule | +5 |
| 11 | `localisation/english/replace/VIE_md_vi_proc_army_l_english.yml` | **MỚI** — bản dịch tiếng Việt (repo đang theo pattern base + replace) | ~95 |
| 12 | `tools/TESTING.md` | thêm mục "Trục 1 — chuỗi mua sắm lục quân" vào smoke test + bảng cờ | +40 |
| 13 | `VIE_v9_flag_mapping.md` | **MỚI** — phục hồi tài liệu đã mất, chép bảng 4.2 vào | +60 |

**Không đụng:** `common/decisions/*` (Trục 2), `common/national_focus/*` ngoài focus ở dòng 8, MIO, ideas.

## 4.4 · Code mẫu đã vá

### `VIE_event_scheduler_p14` (file 3)
```pdx
######################################################################
# Scheduler part 14 - Truc 1: mua sam luc quan (namespace vie_proc_army).
# KHONG dung trigger_year_* cua MD: MD goi no bang meta_effect trong on_monthly
# (MD_on_actions.txt:904) va scripted effect trung ten thi GHI DE -> submod dinh
# nghia lai trigger_year_2016_events se xoa sach event 2016 cua moi nuoc khac.
# Dung scheduler rieng, cung mau p1-p13: guard original_tag = VIE o on_actions,
# ton tai qua noi chien, ton trong VIE_popup_cd va VIE_catch_up.
######################################################################
VIE_event_scheduler_p14 = {
	if = {
		limit = { NOT = { check_variable = { VIE_catch_up = 1 } } }

		VIE_try_proc_1 = yes
		VIE_try_proc_2 = yes
		VIE_try_proc_5 = yes
		VIE_try_proc_8 = yes
		VIE_try_proc_11 = yes
		VIE_try_proc_14 = yes
		VIE_try_proc_18 = yes

		if = {
			limit = { has_game_rule = { rule = rule_vie_alt_procurement option = VIE_ALT_ON } }
			VIE_try_proc_30 = yes
			VIE_try_proc_35 = yes
			VIE_try_proc_38 = yes
		}
	}
	else = {
		# Civil-war winner takes over the VIE lineage: record the historical
		# outcome, grant nothing, fire nothing.
		VIE_proc_catch_up = yes
	}
}
```

### `VIE_try_proc_5` — mẫu retry **đúng** (vá B2)
```pdx
# Cua so 2009-2012. Co dong (VIE_proc_5_closed) dat trong IMMEDIATE cua event,
# khong dat o day: trigger cua event co chan country_event (HOI4 wiki, Event
# modding -> Effect), nen dat co o day se lam mat chuoi vinh vien neu dieu kien
# doi trong 1 ngay delay.
VIE_try_proc_5 = {
	if = {
		limit = {
			NOT = { has_country_flag = VIE_proc_5_closed }
			date > 2008.12.31
		}
		if = {
			limit = {
				# v11 da xoa VIE_tank_modernization -> dung root quan su con song
				has_completed_focus = VIE_modernize_vpa
				country_exists = ISR
				NOT = { has_country_flag = VIE_popup_cd }
			}
			set_country_flag = { flag = VIE_popup_cd days = 45 }
			country_event = { id = vie_proc_army.5 days = 1 random_days = 14 }
		}
		else_if = {
			limit = { date < 2013.1.1 }
			# chua dat hoac dang dinh VIE_popup_cd -> thu lai sau 30 ngay
			country_event = { id = vie_proc_army.90 days = 30 }
		}
		else = {
			set_country_flag = VIE_proc_5_closed
			log = "[GetDateText]: [Root.GetName]: VIE_proc_5 window closed - no T-54M3 prototype, D5 locked"
		}
	}
}
```

### Event ẩn retry
```pdx
country_event = {
	id = vie_proc_army.90
	hidden = yes
	is_triggered_only = yes
	immediate = {
		log = "[GetDateText]: [Root.GetName]: Event vie_proc_army.90 (retry proc 5)"
		VIE_try_proc_5 = yes
	}
}
```

### `vie_proc_army.1` — giao xe ở `immediate` (vá C12)
```pdx
country_event = {
	id = vie_proc_army.1
	title = vie_proc_army.1.t
	desc = vie_proc_army.1.d
	picture = GFX_report_event_generic_navy
	is_triggered_only = yes

	immediate = {
		log = "[GetDateText]: [Root.GetName]: Event vie_proc_army.1"
		set_country_flag = VIE_proc_1_closed
		# Finland transfers ~70 T-54/55 - automatic, not an option effect
		if = {
			limit = { has_dlc = "No Step Back" }
			add_equipment_to_stockpile = { type = medium_tank_chassis_0 amount = 70 producer = FIN }
		}
		else = {
			add_equipment_to_stockpile = { type = MBT_1 amount = 70 producer = FIN }
		}
		set_temp_variable = { treasury_change = -0.05 }
		modify_treasury_effect = yes
	}

	option = {
		name = vie_proc_army.1.a	# Accept the Polish offer: 150 T-72 for training (historical)
		log = "[GetDateText]: [Root.GetName]: event vie_proc_army.1.a"
		set_country_flag = VIE_pl_t72_deal
		ai_chance = { base = 90 }
	}
	option = {
		name = vie_proc_army.1.b	# Decline
		log = "[GetDateText]: [Root.GetName]: event vie_proc_army.1.b"
		ai_chance = { base = 10 }
	}
}
```

### `.14` → `.15`/`.16` (vá C1, C2, C3) + `modify_debt_effect` (vá C7)
```pdx
# option A - 64 xe, vay tin dung Nga (lich su)
option = {
	name = vie_proc_army.14.a
	log = "[GetDateText]: [Root.GetName]: event vie_proc_army.14.a"
	set_variable = { VIE_t90_batch = 32 }
	set_country_flag = VIE_t90_two_batches
	set_temp_variable = { debt_change = 1.25 }
	modify_debt_effect = yes
	# ky 2016 -> giao 12/2018 (~1065 ngay) va 02/2019 (~1125 ngay)
	country_event = { id = vie_proc_army.15 days = 1065 random_days = 30 }
	country_event = { id = vie_proc_army.16 days = 1125 random_days = 30 }
	ai_chance = {
		base = 10
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}
```
```pdx
# .15 - dot 1: cap xe + modifier + XP + co
country_event = {
	id = vie_proc_army.15
	...
	immediate = {
		log = "[GetDateText]: [Root.GetName]: Event vie_proc_army.15 (T-90 batch 1)"
		VIE_deliver_t90 = yes			# doc VIE_t90_batch, co nhanh NSB / non-NSB
		if = {
			limit = { NOT = { has_country_flag = VIE_t90_purchased } }
			set_country_flag = VIE_t90_purchased
			set_country_flag = VIE_ev_t90_tanks		# v9 contract
			add_ideas = VIE_t90_fleet_idea			# +5% armor attack, +3% armor defence (idempotent)
			army_experience = 10
		}
	}
}

# .16 - dot 2: CHI cap xe, khong lap modifier / XP
country_event = {
	id = vie_proc_army.16
	...
	immediate = {
		log = "[GetDateText]: [Root.GetName]: Event vie_proc_army.16 (T-90 batch 2)"
		VIE_deliver_t90 = yes
	}
}
```
```pdx
VIE_deliver_t90 = {
	if = {
		limit = { has_dlc = "No Step Back" }
		add_equipment_to_stockpile = { type = medium_tank_chassis_2 amount = VIE_t90_batch producer = SOV }
	}
	else = {
		add_equipment_to_stockpile = { type = MBT_4 amount = VIE_t90_batch producer = SOV }
	}
}
```
> ⚠️ `producer = SOV` đòi variant T-90 phải có trong `history/countries/SOV - Russia.txt` **của MD**, không phải file VIE (báo cáo đã ghi đúng điểm này — giữ nguyên, và thêm vào checklist test).
> ⚠️ `medium_tank_chassis_2` (**1995**), không phải `_3` (2015) — xem B4.

### Game rule (vá C8)
```pdx
# Alternate-history army procurement (BMP-3 / TOS-1A / CAESAR chains).
# Dedicated rule for hypothetical procurement chains only.
rule_vie_alt_procurement = {
	name = "RULE_VIE_ALT_PROCUREMENT"
	group = "MD_FOCUS_TREE_RULES"
	icon = "GFX_production_licenses"
	default = {
		name = VIE_ALT_OFF
		text = "VIE_ALT_OFF_TEXT"
		desc = "VIE_ALT_OFF_DESC"
	}
	option = {
		name = VIE_ALT_ON
		text = "VIE_ALT_ON_TEXT"
		desc = "VIE_ALT_ON_DESC"
	}
}
```

### Chuyển đổi xe cũ (vá C10)
```pdx
# .6 / D5: 100 T-54/55 -> T-54M3. Dung destroy_equipment, KHONG dung amount am.
destroy_equipment = { type = MBT_1 amount = 100 }
add_equipment_to_stockpile = { type = MBT_1 amount = 100 producer = VIE }	# variant T-54M
add_timed_idea = { idea = VIE_t54m3_upgrade days = 3650 }	# army_armor_defence_factor +2%
```

## 4.5 · Thứ tự thi công (8 bước, mỗi bước là 1 commit)

| Bước | Việc | Kiểm chứng |
|---|---|---|
| **0** | Dọn nền: xoá `events/VIE_md_mil.txt`, `VIE_md_mil_gauges.txt`, `VIE_md_ideas_mil.txt`; bỏ 2 dòng gọi gauge trong `on_actions` | `python3 tools/verify_all_loc.py` PASS; brace balance 0 |
| **1** | `common/scripted_effects/VIE_md_effects_p14.txt`: chỉ `VIE_event_scheduler_p14` + `VIE_try_proc_1` + `VIE_proc_catch_up`. Nối vào `on_actions` | console: `effect VIE_event_scheduler_p14 = yes` không lỗi |
| **2** | `events/VIE_proc_army.txt`: namespace + `.1`, `.2`. Chuỗi 1 không cần cửa sổ → đơn giản nhất, dùng để kiểm chứng cả pipeline | chơi tới 2005–2006, thấy 2 pop-up, +70 MBT_1, −0.05bn |
| **3** | Chuỗi 2 + 3 (`.5`, `.6`, `.8`, `.90`, `.91`) — **lần đầu dùng cơ chế retry + cửa sổ** | console `effect set_variable = { global.year = 2009 }` không được; thay bằng chơi thật hoặc `days` ngắn để test |
| **4** | Chuỗi 4 (`.11`, `.92`) với gate **tạm** `VIE_modernize_vpa` + `date > 2011.6.30`, có `# TODO(truc2)` | |
| **5** | Chuỗi 5 (`.14`, `.15`, `.16`, `.93`) — `VIE_t90_batch`, `modify_debt_effect`, `VIE_deliver_t90` | kiểm tra nợ +1.25, xe về 2 đợt đúng 32+32, modifier **chỉ** cộng 1 lần |
| **6** | Chuỗi 6 (`.18`–`.21`, `.94`) + `rule_vie_alt_procurement` + chuỗi 7–9 (`.30`–`.32`, `.35`, `.38`–`.40`, `.95`–`.97`) | bật rule → thấy BMP-3 2010, CAESAR 2015, TOS-1A 2016 |
| **7** | Sửa gate `VIE_paracel_ultimatum` (A2) theo Q1; phục hồi `VIE_v9_flag_mapping.md`; cập nhật `tools/TESTING.md` | quét lại: 0 cờ `VIE_ev_*` đọc mà không set |
| **8** | Loc: `VIE_md_events_p14_l_english.yml` + `replace/VIE_md_vi_proc_army_l_english.yml` + 5 key rule | `python3 tools/verify_all_loc.py` → 0 lỗi, BOM đúng |

## 4.6 · Checklist test trong game

- [ ] `error.log` sạch: grep `vie_proc_army`, `VIE_try_proc`, `VIE_proc_`, `rule_vie_alt_procurement`, `MBT_`, `IFV_`, `SP_arty`, `SP_R_arty`, `medium_tank_chassis`
- [ ] `producer = SOV` cho `medium_tank_chassis_2` có variant T-90 trong MD chưa? Nếu chưa → bỏ `producer` hoặc tự tạo variant trong `history/countries/VIE*.txt` **của submod**
- [ ] NSB: chassis cấp vào stockpile có **dùng được** trong sư đoàn không, hay phải design variant trước? (rủi ro cao nhất của cả Trục 1)
- [ ] `destroy_equipment = { type = MBT_1 amount = 100 }` khi stockpile < 100 → có đẩy xuống âm không?
- [ ] `.15` nổ 2 lần (nếu bạn giữ thiết kế cũ) vs `.15`+`.16` (thiết kế mới) → so sánh `army_armor_attack_factor`
- [ ] Bật `VIE_popup_cd` thủ công (`effect set_country_flag = { flag = VIE_popup_cd days = 45 }`) rồi chờ → chuỗi phải **dời**, không mất
- [ ] `effect set_variable = { VIE_catch_up = 1 }` rồi chạy scheduler → không pop-up nào nổ, cờ kết quả vẫn có
- [ ] Tắt rule → `.30/.35/.38` không bao giờ nổ; bật rule giữa game (2012) → `.30` (2010) **không** hồi sinh, `.35`/`.38` vẫn kịp
- [ ] Đếm pop-up mỗi năm 2005–2027 so với bảng C5; không năm nào > 5 nếu không bật rule
- [ ] `VIE_paracel_ultimatum` mở được sau khi sửa gate

---

# PHẦN 5 — 5 QUYẾT ĐỊNH CHỈ BẠN CHỐT ĐƯỢC

**Q1 · Gate của `VIE_paracel_ultimatum` (A2).** Focus này đang đòi `VIE_ev_kilo_submarines` HOẶC `VIE_ev_bastion_p_coastal_defence` — cả hai là **hải quân / phòng thủ bờ**, Trục 1 (lục quân) không cấp được.
- (a) Bỏ hẳn khối `OR` → gate còn `VIE_scs_escalated_trigger` + `country_exists = CHI` + `NOT has_war_with` + `VIE_modernize_vpa`. Đơn giản nhất, mở ngay.
- (b) Đổi sang cờ Trục 1 thật sự cấp (vd `VIE_t90_purchased`) — nhưng sai ngữ cảnh (T-90 thì liên quan gì Hoàng Sa).
- (c) Thêm **Trục 1b — mua sắm hải quân** tối thiểu: 2 event set `VIE_ev_kilo_submarines` và `VIE_ev_bastion_p_coastal_defence`. Đúng ngữ cảnh nhất, thêm ~2 event.
- (d) Để nguyên, chấp nhận focus chết tới khi có trục Hải quân.

**Q2 · Trigger focus thay `VIE_tank_modernization` / `VIE_army_short_range_ad` / `VIE_russian_arms_deals`.**
- (a) Tất cả → `has_completed_focus = VIE_modernize_vpa` (root mồ côi hiện tại, khớp với decision category đã sửa ở `f05cfa1`).
- (b) Bỏ gate focus, chỉ gate theo ngày + cờ. Chuỗi nổ đúng lịch sử bất kể người chơi làm gì.
- (c) Dựng lại một focus cổng mỏng `VIE_army_modernization_program` dưới `VIE_modernize_vpa` rồi gate vào đó (cũng giải quyết luôn "root mồ côi 0 con").

**Q3 · Thứ tự thi công Trục 1 vs Trục 2.** `.11` gate theo D1 (Trục 2), D1 lại gate theo `VIE_tank_modernization` (đã xoá). Code Trục 1 trước với gate tạm, hay làm Trục 2 D1 trước?

**Q4 · Đã chốt.** Dùng `rule_vie_alt_procurement`; rule `VIE_alt_history` cũ đã bị xoá vì chỉ có lựa chọn mặc định và không có reader.

**Q5 · Ngân sách pop-up.** Năm 2016 / 2018 / 2019 / 2023 sẽ lên 6–7 pop-up, vượt luật "tối đa 5/năm" trong `TESTING.md`. (a) Nới luật lên 7, (b) hạ một số event Trục 1 xuống `hidden = yes` chỉ ghi log + hiệu ứng (mất tính kể chuyện), hay (c) dời một vài event kinh tế/chính trị sẵn có sang năm khác?

---

# PHỤ LỤC — dữ liệu MD đã tải về để kiểm chứng

```
/home/user/md_states/     12 file state VN + VIE - Vietnam.txt + state_names + victory_points
/home/user/tools/audit/md_ref/        00_yearly_effects.txt, MD_on_actions.txt, MD_event_on_actions.txt,
                          00_game_rules.txt, 00_economic_triggers.txt, 00_budget_effects.txt,
                          MD_x_tank_chassis.txt, MD_tank_chassis.txt, MD_artillery.txt,
                          MD_infantry_equipment.txt, VIE_2000_nsb.txt, VIE_2000_nonnsb.txt
/home/user/audit/         4 script audit + focus.json + defined.json + md_paths.txt
```

---

## Phần 2: Review Trục 2 (CNQP Lục quân) + Plan Code

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

---

## Phần 3: Review Trục 3 (Xây dựng Lực lượng Lục quân) + Plan Code

# REVIEW TRỤC 3 (XÂY DỰNG LỰC LƯỢNG LỤC QUÂN) + PLAN CODE

> Đầu vào: `Báo cáo Lục quân VIE — Trục 1, 2, 3.md` (29/9/2026). **Nguồn chính của Trục 3 là mục VIII**; mục III là bản cũ (32 focus), mục IX là nội dung lịch sử viết cho bản VIII trước, đọc kèm bảng ánh xạ 9.10.
> Đối chiếu với: repo @ `f3236f9` (30/9/2026, sau khi Trục 1 và 2 đã code), `tools/audit/md_ref/`, và `MillenniumDawn/Millennium-Dawn` @ `main` (đọc qua GitHub API ngày 1/10/2026).
>
> **KẾT LUẬN: Trục 3 có khung thiết kế tốt nhưng CHƯA code được nguyên văn.** Có **3 lỗi chặn**, **4 chỗ lệch so với repo hiện tại**, **8 chỗ lệch so với game/MD**, và **1 lỗi cũ của Trục 2** tôi gặp khi đọc `on_startup`. Cấu trúc (9 tầng, 30 focus, giới hạn 3/4 và 2/3, hệ điểm balance, ME ba chiều) **giữ nguyên**. Cái đổi là: tiền đề, tên modifier, thang số, cách đặt ngày, decision, event, ID. Sau khi vá, plan ở Phần 6 code được tuần tự 9 bước.

---

# PHẦN 0 — CÁCH ĐỌC VÀ NHỮNG GÌ ĐÃ KIỂM CHỨNG

**Đã kiểm chứng đúng, khỏi tra lại**

| Hạng mục | Kết quả |
|---|---|
| Số focus mục 8.2 | 3 + 7 + 1 + 1 + 6 + 2 + 1 + 6 + 3 = **30**; người chơi đi 21–22 ✅ |
| Cost trên đường đi | 27 + (35–42) + 7 + 7 + 17 + 10 + 10 + 34 + 30 = **177–184 tuần** khớp bảng 8.2 ✅ (nhưng xem G7: đề xuất hạ 2 cost) |
| Hệ điểm 8.11 | Chạy lại bằng script: BB1 2,0 · BB2 2,5 · TG1 2,0 · TG2 2,4 · CB 2,5 · FM1+FM2 gộp 11,2 · FR 9,0 · FD 9,2 · mỗi hướng ròng đúng 6,0 ✅ |
| Không có deadlock ở giới hạn 3/4 và 2/3 | Đã suy lại bằng tay: CB2 cộng cả `count` lẫn `done`; mọi tổ hợp 3 trong 4 đều đủ `done ≥ 3`; mọi cặp 2 trong 3 đều đủ `cap_done ≥ 2` ✅ |
| Mốc lịch sử | Nghị quyết 05-NQ/TW **17/1/2022**, 230-NQ/QUTW **2/4/2022** ✅ · lễ công bố Quân đoàn 12 **2/12/2023** (QĐ 21/11/2023) ✅ · Quân đoàn 34 **15/12/2024** (QĐ 10/12/2024) ✅ · Quyết định 366 ký **24/1/2025**, công bố **5/2/2025** ✅. Chưa tra lại: Nghị quyết 1657-NQ/QUTW (20/12/2022) |
| `VIE_modernize_vpa` AI đi được | `ai_will_do base = 80`, không có `available` → AI hoàn tất sớm, không chặn N1 (báo cáo 7.3 mục 2) ✅ |
| `cost` mặc định, đơn vị | MD `focus-tree-reference.md`: *"Omit defaults: cost = 10"*; `MD_defines.lua` chỉ đổi `NFocus.MAX_SAVED_FOCUS_PROGRESS = 30`, **không** đổi `FOCUS_POINT_DAYS` → 1 điểm cost = 7 ngày ✅ |
| Tên modifier tiền của MD | `army_personnel_cost_multiplier_modifier`, `equipment_cost_multiplier_modifier` có thật (`money_modifier_definitions.txt`, `color_type = bad`, `value_type = percentage`) ✅ |
| Template sư đoàn | MD đã có sẵn `Mechanized Division` cho VIE (`VIE_2000_nsb.txt`, token `Mech_Inf_Bat`, `armor_Bat`, `SP_Arty_Bat`, `SP_AA_Battery`…), NSB và non-NSB **giống hệt** ✅ |

---

# PHẦN 1 — 3 LỖI CHẶN

## B1 · 🚨 Ba focus "Trục 1 giữ lại" **không còn tồn tại** — mục 3.7 và VIII dựa vào chúng

Báo cáo 3.7 và 8.x viết: *"Trục 1 giữ `VIE_mechanization`, `VIE_army_c4isr`, `VIE_army_short_range_ad`; Trục 3 chỉ cho modifier, không tạo mẫu, không cộng planning/recon/tech"*. Cả ba đã bị v11 xoá (`v11_removed_military_all_subbranches.txt`), và Trục 1 chỉ dùng event, **không dựng lại** (Trục 2 mới dựng lại 4 focus của riêng nó). Đo trên file live: 0 kết quả cho cả ba.

**Hệ quả:**
- Các ràng buộc "Trục 3 không cộng planning/recon, AA, tech" **vẫn nên giữ** (giữ nguyên ngân sách điểm), nhưng giờ chúng không còn "chủ sở hữu" nào bù lại. `Phòng không lục quân` (A1/A2) và `Mạng & Điện tử` (Y1/Y2) chỉ là modifier thuần, không có tòa AA hay tech nào đi kèm.
- Phần "Mẫu sư đoàn cơ giới, 200 `util_vehicle`" của `VIE_mechanization` **không cần dựng lại**: MD đã có `Mechanized Division` trong OOB 2000 của VIE. BB1 "cơ giới hóa từng bước" chỉ là modifier tổ chức, đúng ý báo cáo.
- Đây là **nợ thiết kế có chủ đích**, giống `VIE_ev_t90_tanks` của Trục 1: ghi vào Q12 (mặc định: không dựng lại), không chặn code.

## B2 · 🚨 Cụm "Phòng thủ toàn dân" **đã có sẵn** trong cây focus — trùng với FD1, FD2 và 4 decision của báo cáo

Báo cáo viết cho cây v7 rồi bị v11 cắt ba quân chủng, nhưng **một cụm quân sự khác còn sống** (neo vào `VIE_law_of_the_sea`, tiền đề `VIE_modernize_vpa`):

| Focus có sẵn | Làm gì | Trùng với báo cáo |
|---|---|---|
| `VIE_peoples_defence` | `VIE_peoples_defence_idea`: +5% phòng thủ, +2% `conscription_factor`; `VIE_ax_mob +1` | **FD1** "Phòng thủ chiều sâu" |
| `VIE_provincial_defence_zones` | bunker dọc biên giới 4 state, `VIE_provincial_defence_idea` (Nghị quyết 28-NQ/TW 2008) | **FD2** "Dân quân và khu vực phòng thủ"; sự kiện nền 22/9/2008 (9.2) |
| `VIE_militia_law` (`date > 2019.6.30`) | +20 000 nhân lực, +8% `dig_in_speed`, +5% `max_dig_in` | FD2 và sự kiện nền Luật Dân quân tự vệ 2019 (9.2) |
| `VIE_un_peacekeeping` (`date > 2013.12.31`) | +10 XP, +opinion phương Tây | decision "Triển khai gìn giữ hòa bình" (8.14) và sự kiện 27/5/2014 (9.2) |
| `VIE_force_47` → `VIE_cyber_command` | `VIE_cyber_command_idea`, tech mã hoá | **Y1** "Tác chiến mạng và điện tử" |
| `VIE_military_rescue_corps` + cờ `VIE_disaster_prepared` | cứu hộ thiên tai | decision HADR (8.14) |
| `VIE_four_nos_doctrine` | đòi `VIE_militia_law` và `VIE_un_peacekeeping` | điều kiện capstone Trục 2 |

**Quyết định cần chốt (Q11).** Mặc định (a): **giữ cả hai, chấp nhận cộng dồn**, giống cách báo cáo 3.7 đã chấp nhận cộng dồn với ba focus Trục 1. Điều kiện kèm theo: FD2 đổi tên/lời mô tả để không nói lại những gì `VIE_provincial_defence_zones` và `VIE_militia_law` đã nói (FD2 tập trung vào **tổ chức đơn vị** dân quân, kèm mẫu sư đoàn mới). Con số G2 **chưa tính** cụm cũ; người chơi đi đủ cả hai sẽ có thêm khoảng +5% phòng thủ, +5% dig-in (cùng +8% tốc độ đào và +20 000 nhân lực một lần), tức dig-in ≈ 30%. Chấp nhận vì cụm cũ là lựa chọn riêng, tốn thêm 4–5 focus, và Chiều sâu đã là hướng yếu nhất về tấn công/tốc độ.
Hệ quả: các sự kiện nền 2008/2010/2014/2020 của mục 9.2 **bỏ hết** (đã có focus tương ứng), nên cũng giải được vấn đề ngân sách pop-up (G5).

## B3 · 🚨 Decision: report dùng category và thang chi phí **không tồn tại trong repo**

- Báo cáo mở category mới `VIE_readiness_decisions`. Repo **đã có** `VIE_military_readiness_category` (`visible = has_completed_focus = VIE_modernize_vpa`) với 4 decision: `VIE_exercise_military_region` (40 PP, +15 XP, cooldown 365), `VIE_procurement_batch`, `VIE_asean_joint_patrol`, `VIE_extended_conscription` (75 PP, +25 000 nhân lực, −2% ổn định, cooldown 1095).
- Báo cáo tính chi phí = k × thu nhập PP hằng tháng. Mọi decision trong repo dùng **PP nguyên** (20–75). Chưa ai đo thu nhập PP của VIE.
- Hai decision của báo cáo **chồng** decision có sẵn: "Diễn tập hiệp đồng binh chủng" ≈ `VIE_exercise_military_region`; "Động viên toàn dân"/"Tổng động viên" ≈ `VIE_extended_conscription` (nhưng gấp 8 lần nhân lực với chi phí tương đương).

**Vá:** dùng `VIE_military_readiness_category`; chi phí PP nguyên neo vào decision có sẵn (Q13); chỉnh biên độ nhân lực (G10).

---

# PHẦN 2 — 4 CHỖ LỆCH SO VỚI REPO HIỆN TẠI

## R1 · Biến chỉ ghi, không ai đọc

`VIE_combined_arms_level`, `VIE_command_reform_level` (báo cáo 4.2, 8.8: "chỉ Trục 3") và `VIE_force_building_done` (đọc bởi "nhánh Chính trị/Đối ngoại", chưa tồn tại). Review Trục 2 đã coi "cờ đặt mà không đọc là rác" (C4).
**Vá:** bỏ hai biến đầu; trạng thái đã có sẵn dưới dạng `has_completed_focus = VIE_lf_command_reform_N` (CR1/CR2/CR3). Giữ `VIE_lf_done` làm **cờ chờ có chủ đích** (như `VIE_ev_t90_tanks`), ghi rõ trong bảng cờ.

## R2 · "Tên cờ do nhánh Đối ngoại / Chính trị đặt chưa được định nghĩa" — thực ra đã có

6 decision "nhóm chung" (8.14) chờ cờ chưa tồn tại. Repo đã có sẵn trigger thật: `has_completed_focus = VIE_un_peacekeeping` (gìn giữ hòa bình), `has_completed_focus = VIE_asean_integration` (diễn tập đa phương), `VIE_disaster_prepared` (HADR), các focus `VIE_us_comprehensive_partnership` / `VIE_india_partnership` / `VIE_japan_partnership` (song phương). Xem Phụ lục A: nhóm chung tách thành bước tùy chọn, **không chặn** Trục 3.

## R3 · ID: báo cáo dùng slug tiếng Việt không dấu, repo dùng tiếng Anh

Mọi focus quân sự live: `VIE_modernize_vpa`, `VIE_def_industry_law`, `VIE_peoples_defence`… (Trục 2 cũng theo đó). Báo cáo Trục 3: `VIE_cai_cach_quan_doi`, `VIE_phong_thu_chieu_sau`…
Thêm: tiền tố `VIE_force_*` của báo cáo (cờ hướng lực lượng) **đụng** focus `VIE_force_47` và `VIE_force_47_idea` có sẵn; báo cáo hải quân (bản 2.4) cũng dùng `VIE_cap_*`, `VIE_org_*`.
**Vá:** mọi định danh Trục 3 dùng tiền tố **`VIE_lf_`** (land force), tên tiếng Anh; tên hiển thị tiếng Việt như báo cáo. Bảng ánh xạ ở mục 5.2.

## R4 · Quân đoàn 12 và 34 là **quân đoàn chủ lực cơ động chiến lược** — nhãn "ALT" ở ô Chính quy × Cơ động chiến lược là sai

Bảng 8.5 gắn ô *Chính quy × Cơ động chiến lược* là "ALT nhẹ" và chỉ ô *Chính quy × Phòng thủ khu vực* là "gần lịch sử nhất". Nhưng chính nguồn của báo cáo (VOV, Báo Hưng Yên) gọi Quân đoàn 12 và 34 là "quân đoàn chủ lực **cơ động chiến lược**", và 9.9 cũng ghi "Quân đoàn 12 và 34 là quân đoàn chủ lực thật". Lịch sử thật đi **cả hai**: quân đoàn chủ lực cơ động chiến lược **và** khu vực phòng thủ/dự bị.
**Vá:** cả hai ô Chính quy đều `[THẬT]`; AI Historical chia PS và PT ngang nhau (G3). Chỉ các ô Cơ động × * và Chiều sâu × PS còn là hướng giả định.

---

# PHẦN 3 — 8 CHỖ LỆCH SO VỚI GAME / MD

## G1 · Số slot focus: thực tế là **1**, và đã đo ra hệ quả

MD `MD_defines.lua` chỉ chỉnh một dòng `NFocus` (`MAX_SAVED_FOCUS_PROGRESS = 30`); vanilla không có modifier cộng slot. Giả định **1 slot** (chưa kiểm trong game, ghi vào checklist). Hệ quả với báo cáo:
- Mô phỏng 8.12 ở 1 slot: 175–184 tuần, luôn 21–22 focus, **0% vượt giới hạn** → toàn bộ cơ chế bảo hiểm (phần thưởng chỉ áp nếu count còn dưới giới hạn) **không bao giờ chạy** ở 1 slot.
- Vẫn giữ bảo hiểm, nhưng gom vào một scripted effect (không tốn gì thêm), và **bỏ** phần "cancel_if_invalid là chốt chặn" khỏi danh sách rủi ro: ở 1 slot chỉ cần `available` kiểm khi chọn.
- Tranh chấp slot (báo cáo 4.3, lỗ hổng 2): Trục 3 chiếm **3,3–3,4 năm** của slot duy nhất. Điều kiện kích hoạt Trục 1 (`.5`, `.8`, `.14`) đã được Trục 1 chuyển sang `VIE_modernize_vpa` nên **không còn xung đột**.

## G2 · 🚨 Kiểm tra cộng dồn: số liệu 8.11 **quá mạnh** cho một trục tổ chức

Tôi cộng toàn bộ node theo từng đường đầy đủ (3 binh chủng chính + HD + CR1 + hai node hướng + PS/PT + CR2 + hai lĩnh vực + MOD + CR3 + CAP, kể cả ×1,5 sở trường):

| Đường | Tổng theo báo cáo 8.11 |
|---|---|
| Cơ động | **tốc độ +54 đến +60%**, tổ chức +16–22%, tấn công +10–14% |
| Chiều sâu | **dig-in +40 đến +51%**, nhân lực +17%, phòng thủ +14–16% |
| Chính quy | tổ chức +25–30%, phòng thủ +17–23%, hậu cần +11% |

So với Trục 1 và 2 (T-90 +5% giáp, D5 +2%, D7/K9 +5% pháo, Igla −5% địch): mỗi node Trục 3 cùng cỡ, nhưng **18 node cộng lại** thành mức mà không ý tưởng nào của MD đạt tới (tốc độ +57% là gấp vài lần mọi bonus tốc độ phổ thông). Nguyên nhân gốc: **hệ số điểm của tốc độ (0,4) và dig-in (0,5) quá rẻ**, nên balance cho phép số % rất lớn.

**Vá (Q16, mặc định: làm):** giữ nguyên *điểm* của mọi node (nên mọi thứ cân bằng giữa các hướng giữ nguyên), đổi *hệ số* thành `W' = W / s` với `s` = tốc độ 0,4 · dig-in 0,5 · tổ chức/phòng thủ/tấn công/nhân lực 0,7 · hậu cần, XP, chi phí = 1. Giá trị mỗi node = `round(báo cáo × s, 0,5)`. Bảng cuối ở mục 5.4. Kết quả (script kiểm, nằm ở Phụ lục B):

| Đường | Tổng sau chỉnh | Trần đặt ra |
|---|---|---|
| Cơ động | tốc độ +21–25%, tổ chức +12–17%, tấn công +7–10% | tốc độ ≤ 25 |
| Chiều sâu | dig-in +20–26%, nhân lực +12%, phòng thủ +10–12% (**chưa tính** cụm cũ B2: +5% phòng thủ, +5% dig-in, +8% tốc độ đào) | dig-in ≤ 26, nhân lực ≤ 12 |
| Chính quy | tổ chức +18–21%, phòng thủ +11–16%, hậu cần −10% tiêu hao | tổ chức ≤ 21, phòng thủ ≤ 16 |

Cân bằng ròng ba hướng sau chỉnh (cặp First Force Structure): Chính quy 6,14 · Cơ động 5,79 · Chiều sâu 5,86, lệch tối đa 0,35 (báo cáo: đúng 6,0 do làm tròn; chấp nhận được).

## G3 · Trọng số AI: thang sai và tên path không có thật

- Báo cáo dùng `base` 0,5–3 và "Mọi focus khác = 1". Focus trong repo dùng **`base` 40–80** (Trục 2: 60–80; `VIE_modernize_vpa` 80). AI chọn focus theo trọng số tuyệt đối nên `base 1` khiến AI **gần như không bao giờ** đi Trục 3 khi còn việc khác.
- `VIE_path_*` ở bảng 3.9 là **tên giả**. Cờ thật (`VIE_AI_PATH_HISTORICAL/REFORM/WESTERN/HARDLINE/NATIONALIST`) đi qua trigger có sẵn: `VIE_ai_historical`, `VIE_ai_path_reformish` (Reform, Western, Free zones), `VIE_ai_path_security` (Hardline, Nationalist), `VIE_ai_free`.

**Vá:** `base 60` cho mọi node chuỗi (khớp Trục 2), `base 20` cho Công binh và gốc lĩnh vực không sở trường, `base 40` cho ba hướng và hai hướng phát triển kèm `factor` theo path. Bảng ở mục 5.6.

## G4 · Không khóa ngày là **ngoại lệ duy nhất** trong ba trục

Trục 1 dùng cửa sổ + ETD; Trục 2 khóa **hầu hết** decision và focus bằng ngày (`date > 2008.6.30`, `2012`, `2013`, `2017`, `2021`; chỉ D4, D7, D8 đi theo cờ); báo cáo hải quân có cột "Ngày" cho từng focus (T1 ≥ 2005, T6 ≥ 2012…). Trục 3 không khóa gì (mục 3.10: "Không khóa ngày cho #1–#3"), nên AI có thể làm cải cách quân đội kiểu 2022 vào năm 2002.
Các mốc ngày trong repo (`VIE_militia_law`, `VIE_force_47`, `VIE_un_peacekeeping`) là mẫu gate còn hiệu lực. `VIE_alt_history` từng được đề xuất làm rule chế độ, nhưng audit ngày 07/10/2026 cho thấy rule chỉ có lựa chọn mặc định và không có reader; đã xoá, nên đề xuất dùng nó làm gate không còn áp dụng.

**Vá (Q10, mặc định: khóa mềm):** N1 `available = VIE_lf_gate_open`, với
`VIE_lf_gate_open = OR { date > 2019.2.10 ; AND { VIE_ai_free ; date > 2012.12.31 ; VIE_def_ind_level_ge_2 } }`.
Mốc 11/2/2019 là Nghị quyết 109-NQ/QUTW (báo cáo 9.2) và `VIE_def_ind_level_ge_2` chính là "cổng mềm 8.3" của báo cáo, nhưng chỉ ở chế độ `free`. Phần còn lại của cây **không** khóa ngày thêm (chỉ đi theo N1), giữ nguyên ý "đi trước mốc dated là hướng rẽ giả định" của 8.13.

## G5 · Ngân sách pop-up: mục 9.2 làm vỡ luật ≤ 7 pop-up/năm

`tools/TESTING.md` đo trước Trục 3 và trước Trục 2: 2022 = 6, 2023 = 6, 2024 = 7; Trục 2 sau đó thêm `vie_def_ind.1` (12/2024) và `.4` (6/2024) nên 2024 đã **vượt** luật sửa lại ≤ 7/năm (cần đo lại, mục 7). Mục 9.2 liệt kê 14 sự kiện nền (2008, 2010, 2014, 2018, hai cái 2019, 2020, ba cái 2022, 2023, 2024, hai cái 2025), phần lớn là "event nhỏ".
**Vá (Q17):** bỏ tất cả sự kiện đã có focus tương ứng (B2: 2008, 2010, 2014, 2020, 2018, 2019 cờ phụ). Còn **5 event** namespace `vie_lf`: **3 có pop-up** (Nghị quyết 05 · 2022; Quân đoàn 12 · 2023; Hậu cần–Kỹ thuật · 2025) và **2 ẩn** (Nghị quyết 1657 · 12/2022; Quân đoàn 34 · 12/2024, ẩn để không tăng 2024). Bảng ở mục 5.7.

## G6 · "Giảm cost 50% từ mốc" cần một effect cụ thể

HOI4 không có cost phụ thuộc ngày. Repo đã có tiền lệ đúng: `reduce_focus_completion_cost = { focus = VIE_code_of_conduct cost = 14 }` trong `events/VIE_md_p11.txt:193`, cost gốc của focus đó là 7 (tuần), nên đơn vị của tham số **chỉ có thể là ngày** (giảm 14 ngày; nếu là tuần thì tăng cost). Dùng cùng effect trong event mốc:
`reduce_focus_completion_cost = { focus = VIE_lf_army_reform cost = 35 }` (một nửa của 10 tuần = 70 ngày).
Cũng dùng effect này cho "sở trường giảm 2 tuần cost gốc" (`cost = 14`) ngay trong phần thưởng FM1/FR1/FD1. **Test bắt buộc** (checklist mục 7).

## G7 · Cost off-grid so với repo

Phân bố cost live: 5 (57 focus), 7 (156), 10 (mặc định), cá biệt 8 và 16. Báo cáo dùng **13** cho N1 và CAP; Trục 2 capstone và gốc đều ≤ 10. **Vá (Q15):** N1 = 10, CAP = 10. Tổng đường còn **171–178 tuần** (1 197–1 246 ngày).

## G8 · Nhãn `[ALT-HISTORY: cải cách sớm]` theo ngày cần scripted localisation

Loc tĩnh không đổi theo ngày. `common/scripted_localisation/` đã có (`VIE_md_axis_bars.txt`). Thêm bốn `defined_text` (`VIE_lf_alt_n1`, `_n2`, `_n3`, `_cr2`) trả về nhãn khi `date` nhỏ hơn mốc, gọi trong `_desc` bằng `[GetVIE_lf_alt_n1]`. Tên hàm theo mẫu `VIE_AxBar_*` của repo.

---

# PHẦN 4 — NỢ CŨ TÌM THẤY KHI ĐỌC (không thuộc Trục 3, nhưng Trục 3 dùng cùng mẫu)

## X1 · ⚠️ `on_startup` đặt lại biến Trục 2 mỗi lần load save

`common/on_actions/VIE_md_on_actions_startup.txt` (khối Trục 2):
```pdx
set_variable = { VIE_def_industry_level = 0 }
set_variable = { VIE_def_ind_export_count = 0 }
```
**không có guard**. Chính file đó ghi ở đầu khối thứ nhất: *"on_startup also runs on every save load, so the flag keeps this from recruiting twice"*, và khối `VIE_congress_term` ngay dưới **tính lại** biến từ cờ vì lý do đó. Nếu `on_startup` chạy lại khi load, mỗi lần mở save giữa chừng sẽ **đặt `VIE_def_industry_level` về 0**: ngã rẽ Core/Divest (cần ≥ 4) và capstone (cần ≥ 8) khóa lại, và xuất khẩu (`VIE_def_ind_export_count`) được 5 lần nữa.
Review Trục 2 (L4) sửa đúng điều kiện "biến không khởi tạo" nhưng không nghĩ tới chiều ngược lại.
**Vá (Bước 0):** bọc bằng cờ `VIE_def_ind_vars_init`, đặt biến một lần. Trục 3 dùng cùng khuôn (`VIE_lf_vars_init`). Nếu `on_startup` thực ra không chạy lại khi load thì guard vô hại.

---

# PHẦN 5 — THIẾT KẾ SAU ĐIỀU CHỈNH

## 5.0 · Quyết định Q10–Q17

> Mặc định bên dưới là những gì plan ở Phần 6 viết theo. Đổi lựa chọn nào thì sửa đúng bước ghi chú.

| Q | Câu hỏi | Mặc định | Ảnh hưởng nếu đổi |
|---|---|---|---|
| **Q10** | N1 khóa ngày? | **Khóa mềm** (`VIE_lf_gate_open`, G4) | Bỏ khóa: sửa 1 trigger ở bước 0 |
| **Q11** | Cụm "Phòng thủ toàn dân" có sẵn (B2) | **Giữ cả hai, cộng dồn**, FD2 đổi sang tổ chức đơn vị | Muốn loại trùng: FD2 đòi `VIE_militia_law` (bước 3) |
| **Q12** | Dựng lại `VIE_mechanization`/`_c4isr`/`_short_range_ad`? | **Không**; ghi nợ (B1) | Dựng lại là trục riêng, không chặn Trục 3 |
| **Q13** | Chi phí PP | **Nguyên, neo M ≈ 70 PP/tháng** (xem 5.5) | Đo PP thật rồi đổi 6 số ở bước 5 |
| **Q14** | 6 decision "nhóm chung" | **Tách**, Phụ lục A, tùy chọn | Làm cùng lúc: thêm 4 decision ở bước 5 |
| **Q15** | Cost N1 và CAP | **10** (G7) | Giữ 13: 177–184 tuần |
| **Q16** | Chỉnh thang số (G2) | **Làm** | Bỏ: dùng nguyên bảng 8.11, chấp nhận tốc độ +57% |
| **Q17** | Bộ event | **5 event** (G5) | Làm đủ 14: vượt ngân sách pop-up |

## 5.1 · Kiến trúc (giữ nguyên báo cáo VIII)

```
VIE_modernize_vpa (đã có, abs 266,1)
 ├─ Trục 2: VIE_def_industry_law (266,2) → Core/Divest → capstone      [đã code, không đụng]
 └─ Trục 3: [1 Nền tảng] N1 → N2, N3
              [2 Binh chủng] 3 trong 4: Bộ binh │ Tăng thiết giáp │ Pháo binh │ Công binh
              [3] HD   [4] CR1 → mở 3 decision
              [5 First Force Structure] CHỌN 1 (ME 3 chiều): Cơ động │ Chính quy │ Chiều sâu  (mỗi hướng 2 focus)
              [6 Hướng phát triển] CHỌN 1 (ME): Cơ động chiến lược │ Phòng thủ khu vực và dự bị
              [7] CR2   [8 Năng lực] 2 trong 3: Biên giới & Đô thị │ Phòng không lục quân │ Mạng & Điện tử
              [9] MOD → CR3 → CAP (3 biến thể)
```
Không có prerequisite chéo sang Trục 1/2. Trục 3 **đọc** một thứ duy nhất của Trục 2: `VIE_def_ind_level_ge_2` (chỉ ở chế độ `free`, G4). Trục 3 **ghi** các cờ ở 5.3, Trục 1/2 chỉ đọc chúng trong bước tùy chọn 8 (AI).

## 5.2 · Ánh xạ mã báo cáo → ID

Prerequisite viết theo quy ước HOI4: nhiều khối `prerequisite` = AND; nhiều `focus` trong một khối = OR. "Biến" ở cột *Điều kiện* là điều kiện `available`, **luôn đi kèm** prerequisite hiển thị (R1/B-HD): mỗi focus bị gate bằng biến vẫn có ít nhất một đường kẻ từ cha.

| Mã | ID | Tên hiển thị (báo cáo) | Cost | Prerequisite | `available` (ngoài ngày) | Hoàn thành |
|---|---|---|---:|---|---|---|
| N1 | `VIE_lf_army_reform` | Cải cách quân đội, tinh gọn biên chế | 10 | `VIE_modernize_vpa` | `VIE_lf_gate_open` | `VIE_lf_n1_reward` |
| N2 | `VIE_lf_logistics_merge` | Hiện đại hóa hệ thống bảo đảm hậu cần – kỹ thuật | 7 | N1 | — | `VIE_lf_n2_reward` |
| N3 | `VIE_lf_basic_training` | Đào tạo lục quân cơ bản | 7 | N1 | — | `VIE_lf_n3_reward` |
| BB1 | `VIE_lf_arm_infantry_org` | Bộ binh: tổ chức, cơ giới hóa từng bước | 7 | N2 và N3 | `arm_count < 3` | count +1 (có guard), `VIE_lf_bb1_reward` |
| BB2 | `VIE_lf_arm_infantry_train` | Bộ binh: đào tạo sĩ quan, huấn luyện binh sĩ | 7 | BB1 | — | done +1 (có guard), `VIE_lf_bb2_reward` |
| TG1 | `VIE_lf_arm_armor_org` | Tăng thiết giáp: tổ chức | 7 | N2 và N3 | `arm_count < 3` | như BB1 |
| TG2 | `VIE_lf_arm_armor_train` | Tăng thiết giáp: đào tạo sĩ quan, kíp xe | 7 | TG1 | — | như BB2 |
| PB1 | `VIE_lf_arm_arty_org` | Pháo binh: tổ chức, hỏa lực chi viện | 7 | N2 và N3 | `arm_count < 3` | như BB1 |
| PB2 | `VIE_lf_arm_arty_train` | Pháo binh: đào tạo sĩ quan, pháo thủ | 7 | PB1 | — | như BB2 |
| CB | `VIE_lf_arm_engineers` | Công binh: đào tạo, công binh chiến đấu | 7 | N2 và N3 | `arm_count < 3` | count +1 **và** done +1 (guard), `VIE_lf_cb_reward` |
| HD | `VIE_lf_combined_arms` | Hiệp đồng binh chủng | 7 | **OR** BB2, TG2, PB2, CB | `arm_done ≥ 3` | `VIE_lf_hd_reward` |
| CR1 | `VIE_lf_command_reform_1` | Cải cách bộ chỉ huy I: chuẩn hóa tham mưu | 7 | HD | — | `VIE_lf_cr1_reward`; mở 3 decision |
| FM1 | `VIE_lf_fs_mobile_force` | Lực lượng cơ động | 10 | CR1; ME FR1, FD1 | — | cờ `VIE_lf_mobile`, giá, sở trường |
| FM2 | `VIE_lf_fs_mobile_corps` | Cụm cơ động | 7 | FM1 | — | `VIE_lf_fm2_reward` + mẫu cụm cơ động |
| FR1 | `VIE_lf_fs_main_corps` | Quân đoàn chủ lực chính quy | 10 | CR1; ME FM1, FD1 | — | cờ `VIE_lf_regular`, giá, sở trường |
| FR2 | `VIE_lf_fs_lean_corps` | Tổ chức quân đoàn tinh, gọn, mạnh | 7 | FR1 | — | `VIE_lf_fr2_reward` |
| FD1 | `VIE_lf_fs_depth_defence` | Phòng thủ chiều sâu | 10 | CR1; ME FM1, FR1 | — | cờ `VIE_lf_depth`, giá, sở trường |
| FD2 | `VIE_lf_fs_militia_units` | Tổ chức dân quân và đơn vị khu vực phòng thủ | 7 | FD1 | — | `VIE_lf_fd2_reward` + mẫu dân quân |
| PS | `VIE_lf_dev_strategic` | Cơ động chiến lược | 10 | **OR** FM2, FR2, FD2; ME PT | — | cờ `VIE_lf_dev_strategic`, giá |
| PT | `VIE_lf_dev_territorial` | Phòng thủ khu vực và dự bị | 10 | **OR** FM2, FR2, FD2; ME PS | — | cờ `VIE_lf_dev_territorial`, giá |
| CR2 | `VIE_lf_command_reform_2` | Cải cách bộ chỉ huy II: bộ tư lệnh cấp chiến dịch | 10 | **OR** PS, PT | — | `VIE_lf_cr2_reward` (theo cờ hướng) |
| L1 | `VIE_lf_cap_border_urban` | Tác chiến biên giới và đô thị | 10 | CR2 | `cap_count < 2` | cap_count +1 (guard), `VIE_lf_l1_reward` |
| L2 | `VIE_lf_cap_area_control` | Khống chế địa bàn | 7 | L1 | — | cờ `VIE_lf_cap_land`, cap_done +1 (guard), `VIE_lf_l2_reward` |
| A1 | `VIE_lf_cap_army_ad` | Phòng không lục quân và bảo vệ lực lượng | 10 | CR2 | `cap_count < 2` | như L1 |
| A2 | `VIE_lf_cap_ad_coord` | Hiệp đồng phòng không với Phòng không – Không quân | 7 | A1 | — | cờ `VIE_lf_cap_ad`, như L2 |
| Y1 | `VIE_lf_cap_cyber_ew` | Tác chiến mạng và điện tử | 10 | CR2 | `cap_count < 2` | như L1 |
| Y2 | `VIE_lf_cap_info_ops` | Tác chiến thông tin hiệp đồng | 7 | Y1 | — | cờ `VIE_lf_cap_cyber`, như L2 |
| MOD | `VIE_lf_selective_modernization` | Hiện đại hóa chọn lọc | 10 | **OR** L2, A2, Y2 | `cap_done ≥ 2` | `VIE_lf_mod_reward` (theo lĩnh vực) |
| CR3 | `VIE_lf_command_reform_3` | Cải cách bộ chỉ huy III: chỉ huy số hiệp đồng | 7 | MOD | — | `VIE_lf_cr3_reward` |
| CAP | `VIE_lf_force_complete` | Hoàn thiện lực lượng vũ trang | 10 | CR3 | — | `VIE_lf_cap_reward` (3 biến thể), cờ `VIE_lf_done` |

`arm_count/arm_done/cap_count/cap_done` là `VIE_lf_arm_count`… Chỉ **bảy** node có điều kiện `count`: BB1, TG1, PB1, CB (< 3) và L1, A1, Y1 (< 2). Node giữa và node cuối **không** đòi count (đúng 3.3: nếu đòi, hai lĩnh vực đã chọn sẽ tự khóa nhau).

## 5.3 · Biến và cờ

| Tên | Loại | Đặt bởi | Đọc bởi |
|---|---|---|---|
| `VIE_lf_arm_count`, `VIE_lf_arm_done` | biến 0–3 | node đầu / node đào tạo binh chủng, CB | `available` BB1/TG1/PB1/CB; HD |
| `VIE_lf_cap_count`, `VIE_lf_cap_done` | biến 0–2 | L1/A1/Y1; L2/A2/Y2 | `available` gốc lĩnh vực; MOD |
| `VIE_lf_mobile` / `VIE_lf_regular` / `VIE_lf_depth` | cờ | FM1 / FR1 / FD1 | CR2, năng lực, MOD, CAP, AI, decision, Trục 1/2 (bước 8) |
| `VIE_lf_dev_strategic` / `VIE_lf_dev_territorial` | cờ | PS / PT | decision Phản ứng nhanh / Động viên toàn dân |
| `VIE_lf_cap_land` / `_ad` / `_cyber` | cờ | L2 / A2 / Y2 | MOD, CAP (−2% duy trì nếu đúng sở trường) |
| `VIE_lf_done` | cờ **chờ** | CAP | **chưa ai** (nhánh Chính trị/Đối ngoại tương lai); không xoá |
| `VIE_lf_vars_init` | cờ | startup | startup |
| `VIE_lf_ms_nq05` … `_corps12`, `_corps34`, `_logistics` | cờ | event mốc | scheduler |

Sở trường **không** có cờ riêng: Cơ động → Mạng & Điện tử, Chính quy → Phòng không, Chiều sâu → Biên giới & Đô thị, suy ra từ `VIE_lf_mobile/regular/depth` (scripted trigger `VIE_lf_fav_land/_ad/_cyber`).

## 5.4 · Hiệu ứng từng node (thang đã chỉnh, Q16)

Đơn vị: % cộng vào biến `VIE_af_*`, ví dụ "+1,5" = `add_to_variable = { VIE_af_army_org_factor = 0.015 }`. Cột *Biến* ở 5.5. "Hậu cần −X" = `supply_consumption_factor −X%`. Cột **báo cáo** để đối chiếu.

**Chung mọi hướng** (điểm báo cáo, giá trị mới)

| Node | Báo cáo 8.11 | **Giá trị mới** |
|---|---|---|
| N1 | không số | +25 PP; 10 XP; đặt `VIE_lf_vars_init` nếu chưa |
| N2 | không số (+ thưởng event 5/2/2025) | +15 điểm chỉ huy |
| N3 | không số | +10 XP |
| BB1 | +2 tổ chức | +1,5 tổ chức |
| BB2 | +2 phòng thủ, +1 hậu cần | +1,5 phòng thủ, hậu cần −1 |
| TG1 | +5 tốc độ | +2 tốc độ |
| TG2 | +2 tấn công | +1,5 tấn công |
| PB1 | +4 dig-in | +2 dig-in |
| PB2 | +2 tấn công pháo | +1,5 tấn công pháo |
| CB | +5 dig-in | +2,5 dig-in |
| HD | +3 tổ chức | +2 tổ chức |
| CR1 | +2 tổ chức, +2 hậu cần; mở decision | +1,5 tổ chức, hậu cần −2 |

**First Force Structure và hướng phát triển** (cái giá áp ở node đầu)

| Node | Báo cáo | **Giá trị mới** |
|---|---|---|
| FM1 | +8 tốc độ, +2 tổ chức; giá −2 nhân lực, +2 chi phí sản xuất, −4 dig-in | +3 tốc độ, +1,5 tổ chức; giá: nhân lực −1,5, `equipment_cost` +2, dig-in −2 |
| FM2 | +6 tốc độ, +3 tấn công; mẫu | +2,5 tốc độ, +2 tấn công; mẫu cụm cơ động |
| FR1 | +3 tổ chức, +2 phòng thủ; giá +2 duy trì, −1 XP | +2 tổ chức, +1,5 phòng thủ; giá: `army_personnel_cost` +2, XP −1 |
| FR2 | +2 tổ chức, +4 hậu cần | +1,5 tổ chức, hậu cần −4 |
| FD1 | +6 dig-in, +2 phòng thủ; giá −2 tấn công, −2 tốc độ | +3 dig-in, +1,5 phòng thủ; giá: tấn công −1,5, tốc độ −1 |
| FD2 | +7 nhân lực; mẫu | +5 nhân lực; mẫu dân quân (đã bỏ phần trùng `VIE_militia_law`, B2) |
| PS | +5 tốc độ, +2 tổ chức, +2 hậu cần; giá +1 sản xuất | +2 tốc độ, +1,5 tổ chức, hậu cần −2; giá `equipment_cost` +1 |
| PT | +5 nhân lực, +4 dig-in; giá +1 duy trì | +3,5 nhân lực, +2 dig-in; giá `army_personnel_cost` +1 |

Ròng sau chỉnh (cặp FFS): Chính quy 6,14 · Cơ động 5,79 · Chiều sâu 5,86.

**Năng lực** (gốc / cuối; ô sở trường nhân 1,5 làm tròn 0,5 cho node cuối, nên ghi riêng)

| Lĩnh vực | Hướng | Gốc | Cuối | Cuối **nếu sở trường** |
|---|---|---|---|---|
| Biên giới & Đô thị (L1/L2) | Chính quy | phòng thủ +2 | tổ chức +2, phòng thủ +2 | — |
| | Cơ động | tốc độ +2, phòng thủ +0,5 | tấn công +2, tốc độ +2,5 | — |
| | **Chiều sâu (sở trường)** | dig-in +2, phòng thủ +0,5 | dig-in +4, phòng thủ +1,5 | **dig-in +6, phòng thủ +2,5** |
| Phòng không lục quân (A1/A2) | **Chính quy (sở trường)** | phòng thủ +2 | tổ chức +2, phòng thủ +2 | **tổ chức +3, phòng thủ +3** |
| | Cơ động | tổ chức +1,5, tốc độ +1 | tổ chức +3, tốc độ +2 | — |
| | Chiều sâu | dig-in +2, phòng thủ +0,5 | phòng thủ +3, dig-in +2 | — |
| Mạng & Điện tử (Y1/Y2) | Chính quy | tổ chức +2 | tổ chức +2, phòng thủ +2 | — |
| | **Cơ động (sở trường)** | tốc độ +2, tổ chức +0,5 | tấn công +2, tốc độ +2,5 | **tấn công +3, tốc độ +4** |
| | Chiều sâu | dig-in +3 | phòng thủ +3, dig-in +2 | — |

Sở trường còn giảm 14 ngày cost của gốc (`reduce_focus_completion_cost`, G6).

**CR2, MOD, CR3, CAP**

| Node | Chính quy | Cơ động | Chiều sâu |
|---|---|---|---|
| CR2 | tổ chức +1,5, phòng thủ +0,5 | tổ chức +1,5, tốc độ +1 | phòng thủ +1,5, dig-in +1 |
| CAP | tổ chức +2, phòng thủ +2; −2% `army_personnel_cost` nếu đã xong lĩnh vực sở trường (Phòng không) | tốc độ +3,5, tấn công +1,5; mở decision Phản ứng nhanh (đã mở bởi PS) | nhân lực +3,5, dig-in +3; mở decision Động viên toàn dân (đã mở bởi PT) |

| Node | Mỗi lĩnh vực đã xong (MOD) | CR3 |
|---|---|---|
| MOD | Biên giới & Đô thị: dig-in +1,5 · Phòng không: phòng thủ +1 · Mạng & Điện tử: tổ chức +1 | — |
| CR3 | — | tổ chức +1, hậu cần −3 (không cộng planning/recon) |

Các hàng "mở decision" ở CAP thực ra đã được mở sớm hơn bởi PS/PT (báo cáo 3.8 viết cho bản cũ); CAP chỉ thêm `VIE_lf_done` và phần số. Ghi rõ vào loc để người chơi không tưởng CAP mở thêm decision.

## 5.5 · Ánh xạ modifier (đã kiểm chứng với repo và MD)

| Khái niệm báo cáo | Modifier | Biến `VIE_af_*` | Trạng thái |
|---|---|---|---|
| tổ chức | `army_org_factor` | `VIE_af_army_org_factor` | có trong `VIE_armed_forces_modifier` |
| phòng thủ | `army_defence_factor` | `VIE_af_army_defence_factor` | có |
| tốc độ | `army_speed_factor` | `VIE_af_army_speed_factor` | có |
| dig-in | `max_dig_in_factor` | `VIE_af_max_dig_in_factor` | có (cụm cũ dùng thêm `dig_in_speed_factor`) |
| hậu cần | `supply_consumption_factor` (âm) | `VIE_af_supply_consumption_factor` | có |
| XP | `experience_gain_army_factor` | `VIE_af_experience_gain_army_factor` | có |
| tấn công pháo | `army_artillery_attack_factor` | `VIE_af_army_artillery_attack_factor` | có |
| **tấn công chung** | `army_attack_factor` | `VIE_af_army_attack_factor` | **thiếu, thêm** (key tooltip `VIE_tt_army_attack_factor` đã có) |
| **max manpower** | `conscription_factor` (vanilla không có "max manpower"; cụm cũ dùng đúng nó) | `VIE_af_conscription_factor` | **thiếu, thêm** |
| chi phí duy trì | `army_personnel_cost_multiplier_modifier` (MD) | `VIE_af_army_personnel_cost_multiplier_modifier` | **thiếu, thêm** |
| chi phí sản xuất | `equipment_cost_multiplier_modifier` (MD) | `VIE_af_equipment_cost_multiplier_modifier` | **thiếu, thêm** |

Mẫu ghi: `add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }`, đúng mẫu của cụm cũ (`VIE_militia_law`) và Trục 1/2 (`VIE_af_army_artillery_attack_factor`). Sáu key tooltip mới trong `localisation/english/replace/VIE_md_vi_tt_l_english.yml`: `VIE_tt_army_org_factor`, `VIE_tt_experience_gain_army_factor`, `VIE_tt_supply_consumption_factor`, `VIE_tt_conscription_factor`, `VIE_tt_army_personnel_cost`, `VIE_tt_equipment_cost`. Hai modifier chi phí MD có `color_type = bad` và đơn vị chưa kiểm trong game: ghi vào checklist.

## 5.6 · AI

`ai_will_do` mọi focus: `base` như bảng, thêm `modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }` (cùng cách Trục 2). Mốc dated: `modifier = { factor = 3 date > <mốc> }` cho N1 (> 2022.1.16), N3 (> 2022.12.19), CR2 (> 2023.12.1), N2 (> 2025.2.4).

| Nhóm | `base` | Historical (`VIE_ai_historical`) | Western/Reform (`VIE_ai_path_reformish`) | Hardline/Nationalist (`VIE_ai_path_security`) |
|---|---:|---|---|---|
| Node chuỗi chung | 60 | — | — | — |
| Công binh (CB) | 20 | — | — | — |
| FM1 Cơ động | 40 | ×0,25 | ×1,5 | ×0,25 |
| FR1 Chính quy | 40 | ×1,5 | ×1 | ×1 |
| FD1 Chiều sâu | 40 | ×1 | ×0,25 | ×1,5 |
| PS Cơ động chiến lược | 40 | ×1,5 | ×1,5 | ×0,5 |
| PT Phòng thủ khu vực và dự bị | 40 | ×1,5 | ×0,75 | ×1,5 |
| Gốc lĩnh vực sở trường (`VIE_lf_fav_*`) | 60 | | | |
| Gốc lĩnh vực không sở trường | 20 | | | |

PS và PT ngang nhau ở Historical (R4). Tỉ lệ này khác 3.9 của báo cáo (0,5 : 3) có chủ ý.

## 5.7 · Event (`namespace = vie_lf`, scheduler p17)

Ba pop-up và hai ẩn, đều `is_triggered_only`. Mỗi event: **một** scripted effect `VIE_lf_ms_*_apply` chứa phần hiệu ứng để option và fallback không lệch nhau (mẫu của Trục 2, mục 6.2). Điều kiện lịch dùng khuôn `VIE_event_scheduler_p15`: ngày → `VIE_popup_cd` → fallback im lặng sau 6 tháng.

| ID | Mốc | Loại | Nếu focus liên quan **chưa** xong | Nếu **đã** xong |
|---|---|---|---|---|
| `vie_lf.1` | 2022.1.17 Nghị quyết 05 | pop-up | N1: `reduce_focus_completion_cost` −35 ngày | +15 XP, +25 PP |
| `vie_lf.2` | 2022.12.20 Nghị quyết 1657 | **ẩn** | N3: −24 ngày | +10 XP |
| `vie_lf.3` | 2023.12.2 Quân đoàn 12 | pop-up | CR2: −35 ngày; **mọi người chơi** tổ chức +1 (`VIE_af_army_org_factor`); thêm +0,5 nếu `VIE_lf_regular` | như bên trái, không giảm cost |
| `vie_lf.4` | 2024.12.15 Quân đoàn 34 | **ẩn** | tổ chức +0,5 cho mọi người chơi | như bên trái |
| `vie_lf.5` | 2025.2.5 hợp nhất Hậu cần – Kỹ thuật | pop-up | N2: −24 ngày; hậu cần −2 cho mọi người chơi | hậu cần −2 (đã có) và +10 điểm chỉ huy |

Chiều ngược lại, event **không** phụ thuộc người chơi đã đi N1 hay chưa ("nổ cho mọi người chơi", báo cáo 8.4). Catch-up (`VIE_catch_up = 1`): chỉ đặt cờ mốc, không pop-up. Ảnh event: dùng tạm ảnh có sẵn (`GFX_VIE_report_event_vie_proc_army_14`…) cho đến khi thêm 5 mục vào `EVENTS` của `tools/build_vie_event_pictures.py`.

## 5.8 · Decision (6, trong `VIE_military_readiness_category`)

Tất cả: `icon = GFX_decision_generic_army_support`, `visible` theo focus, `available = { has_war = no }` (trừ ghi chú), `ai_will_do = { base = 10–20 ; factor 0 khi VIE_def_ind_bankrupt }`. Phần thưởng đặt trong `remove_effect` (sau `days_remove`), log đầu mỗi khối effect (chuẩn MD `decision-reference.md`).

| ID | Mở từ | PP | Thời gian | Cooldown (`days_re_enable`) | Thưởng | So với báo cáo |
|---|---|---:|---:|---:|---|---|
| `VIE_dec_lf_train_terrain` | CR1 | 35 | 90 | 545 | +10 XP; ý tưởng tạm `terrain_penalty_reduction` +5% 180 ngày | gộp "rừng núi" |
| `VIE_dec_lf_train_urban` | CR1 | 35 | 90 | 545 | +10 XP; ý tưởng tạm `urban_attack_factor` +5% 180 ngày (**kiểm tên**) | giữ |
| `VIE_dec_lf_joint_arms` | CR1 | 35 | 90 | 545 | +10 XP (+15 nếu `VIE_lf_regular` và CAP xong); tổ chức +2% 90 ngày | giữ, đọc trạng thái CR/CAP (R1) |
| `VIE_dec_lf_rapid_response` | PS | 50 | 60 | 545 | +20 XP; tốc độ +5% 90 ngày | +10% → +5% (G2) |
| `VIE_dec_lf_mobilize_people` | PT | 40 | 120 | 730 | +40 000 nhân lực; dig-in +2,5% 180 ngày | 50 000 → 40 000, +5% → +2,5% |
| `VIE_dec_lf_total_mobilization` | CR1 | 65 | 90 | 1095 | +100 000 nhân lực; −5% ổn định (`add_stability = -0.05`, một lần); dig-in +5% 180 ngày | 200 000 → 100 000 |

`VIE_dec_lf_total_mobilization` `available`: `OR { VIE_lf_depth ; VIE_lf_dev_territorial ; has_war = yes ; VIE_scs_escalated_trigger = yes }` ("căng thẳng cao" dùng trigger có thật của repo; báo cáo không nêu tên).
XP dùng đúng mẫu repo: `has_selected_land_grand_doctrine = yes → add_mastery { folder = land }`, ngược lại `army_experience` (mẫu `VIE_limited_war_doctrine`, `VIE_un_peacekeeping`); bọc thành `VIE_lf_xp_10/15/20/25` (literal, tránh nhận biến ở `add_mastery`).

Ước tính XP: ≈ 29 XP/năm từ các decision mới (báo cáo) cộng 15 XP/năm của `VIE_exercise_military_region`; trần XP của MD là 1000 nên không chạm trần.

## 5.9 · Mẫu sư đoàn (FM2, FD2)

Báo cáo 3.7 cho phép Trục 3 tạo hai mẫu mới. Token lấy từ `VIE_2000_nsb.txt` (NSB và non-NSB giống nhau):

- **Cụm cơ động** (FM2): `armor_Bat ×2` · `Mech_Inf_Bat ×4` · `SP_Arty_Bat ×2`, `support = { SP_AA_Battery }`, `regimental_support = { armor_Recce_Comp }`. Không cấp trang bị, không tạo đơn vị: chỉ `add_division_template`.
- **Dân quân khu vực** (FD2): `L_Inf_Bat ×6` (hai cột × ba hàng), không support.

Template trống không tốn gì; người chơi tự đặt sản xuất.

## 5.10 · Layout

Cả 29 focus còn lại neo vào **N1** (`relative_position_id = VIE_lf_army_reform`, khai báo trước tất cả, 0 forward-ref); N1 neo vào `VIE_modernize_vpa` với `x = 12, y = 1`, tức abs **(278, 2)**. Vùng x 215–299 trống hoàn toàn (đo: chỉ có `VIE_modernize_vpa` và 4 focus Trục 2 ở x 264–268; dải an ninh x 304–308 ở y 24–27).

| Hàng (abs y) | Focus (dx, dy so với N1 → abs x) |
|---|---|
| 2 | N1 (0,0 → 278) |
| 3 | N2 (−2,1 → 276) · N3 (+2,1 → 280) |
| 4 | BB1 (−6,2 → 272) · TG1 (−2,2 → 276) · PB1 (+2,2 → 280) · CB (+6,2 → 284) |
| 5 | BB2 (−6,3) · TG2 (−2,3) · PB2 (+2,3) |
| 6 | HD (0,4 → 278) |
| 7 | CR1 (0,5) |
| 8 | FM1 (−6,6 → 272) · FR1 (0,6 → 278) · FD1 (+6,6 → 284) |
| 9 | FM2 (−6,7) · FR2 (0,7) · FD2 (+6,7) |
| 10 | PS (−3,8 → 275) · PT (+3,8 → 281) |
| 11 | CR2 (0,9) |
| 12 | L1 (−6,10) · A1 (0,10) · Y1 (+6,10) |
| 13 | L2 (−6,11) · A2 (0,11) · Y2 (+6,11) |
| 14 | MOD (0,12) |
| 15 | CR3 (0,13) |
| 16 | CAP (0,14) |

Khoảng cách tối thiểu cùng hàng = 4 (quy tắc "gap ≥ 2"), con luôn `y >` cha. Đường kẻ CB → HD và PS/PT chéo nhau nhìn xấu nhưng đúng; `tools/audit/audit.py` không kiểm đường kẻ, nên cần mở cây trong game chỉnh bằng tay sau bước 2–4 (đã làm vậy ở Trục 2).

---

# PHẦN 6 — PLAN CODE TRỤC 3

Nhánh: `truc3-force-building` từ `main`. Mỗi bước một commit; chạy bộ kiểm tĩnh (mục 6.4) trước khi commit.

## 6.1 · File-by-file

| # | File | Việc | Ước lượng dòng |
|---:|---|---|---:|
| 1 | `common/scripted_triggers/VIE_md_triggers_p17.txt` | **MỚI**: `VIE_lf_gate_open`, `VIE_lf_arm_slot_free`, `VIE_lf_cap_slot_free`, `VIE_lf_arm_done_3`, `VIE_lf_cap_done_2`, `VIE_lf_fav_land/_ad/_cyber`, `VIE_lf_mobilize_gate` | ~70 |
| 2 | `common/scripted_effects/VIE_md_effects_p17.txt` | **MỚI**: `VIE_lf_refresh`, `VIE_lf_xp_10/15/20/25`, 30 `VIE_lf_<mã>_reward`, `VIE_lf_ms_*_apply` ×5, `VIE_lf_create_template_mobile/_militia`, `VIE_event_scheduler_p17` | ~520 |
| 3 | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` | thêm 4 dòng modifier (5.5) trước `# GEN:vars end` | +4 |
| 4 | `common/on_actions/VIE_md_on_actions_startup.txt` | **vá X1** + khối `VIE_lf_vars_init` | +16 |
| 5 | `common/on_actions/VIE_md_on_actions.txt` | nối `VIE_event_scheduler_p17 = yes` | +1 |
| 6 | `common/scripted_effects/VIE_md_effects_p3.txt` | nối p17 vào `VIE_catch_up_schedule` | +1 |
| 7 | `common/national_focus/VIE_md_focus.txt` | 30 focus ở cuối file, sau khối Trục 2 | ~1 050 |
| 8 | `common/ideas/VIE_md_ideas_lf.txt` | **MỚI**: 6 ý tưởng tạm (`VIE_lf_idea_terrain_drill`, `_urban_drill`, `_joint_arms`, `_rapid_response`, `_mobilized_people`, `_total_mobilization`) | ~80 |
| 9 | `common/decisions/VIE_md_decisions_lf.txt` | **MỚI**: 6 decision, khối `VIE_military_readiness_category = { }` | ~230 |
| 10 | `events/VIE_land_force.txt` | **MỚI**: `add_namespace = vie_lf` + 5 event | ~150 |
| 11 | `common/scripted_localisation/VIE_md_lf_alt.txt` | **MỚI**: 4 `defined_text` nhãn ALT | ~50 |
| 12 | `localisation/english/VIE_md_events_p17_l_english.yml` | **MỚI** (BOM): ~115 key | ~140 |
| 13 | `localisation/english/replace/VIE_md_vi_tt_l_english.yml` | +6 key `VIE_tt_*` | +6 |
| 14 | `tools/audit/lf_balance.py` | **MỚI**: bảng 5.4 + kiểm ròng + trần (Phụ lục B) | ~120 |
| 15 | `tools/TESTING.md` | thêm mục Trục 3 (mục 7 dưới đây) | +60 |
| 16 | `events/VIE_proc_army.txt`, `common/decisions/VIE_md_def_industry.txt` | **tùy chọn** (bước 8): `ai_chance` / `ai_will_do` theo cờ hướng | +20 |

## 6.2 · Thứ tự thi công (9 bước)

| Bước | Việc | Kiểm chứng |
|---|---|---|
| **0** | File 1, 3, 4, 13, 14. **Vá X1.** Thêm 4 modifier. | `live.py` 0 missing; `lf_balance.py` in đúng bảng 5.4 (ròng ba hướng ≤ 0,4 chênh, trần G2); console `effect add_to_variable = { VIE_af_conscription_factor = 0.01 }` thấy dòng trong tooltip `VIE_armed_forces_modifier` |
| **1** | File 2 (khung): `VIE_lf_refresh`, `VIE_lf_xp_*`, scheduler **rỗng** + file 5, 6 | `on_monthly` chạy không báo lỗi; `error.log` sạch |
| **2** | File 7 phần 1: N1–N3, 7 node binh chủng, HD, CR1 (12 focus) + reward tương ứng | `audit.py`: 0 dangling, 0 forward-ref, 0 cycle, 0 trùng tọa độ; chơi: N1 xám trước 11/2/2019 (plausible), mở khi `free` + level 2 |
| **3** | File 7 phần 2: FM1/FR1/FD1, FM2/FR2/FD2, PS, PT, CR2 (9 focus) + 2 mẫu sư đoàn | ME ba chiều: chọn FR1 thì FM1 và FD1 xám; PS/PT loại trừ nhau; `reduce_focus_completion_cost` −14 ngày gốc sở trường |
| **4** | File 7 phần 3: 6 node năng lực, MOD, CR3, CAP (9 focus) | Giới hạn 2/3: sau 2 gốc thì gốc thứ ba xám; MOD xám khi `cap_done < 2`; audit 30/30 |
| **5** | File 8, 9: 6 ý tưởng tạm + 6 decision | Decision hiện sau CR1/PS/PT; cooldown; ý tưởng tạm hiện 180 ngày rồi mất |
| **6** | File 10, 11, scheduler p17 đầy đủ | Event đúng ngày; `VIE_popup_cd` tôn trọng; catch-up chỉ đặt cờ; nhãn ALT đổi tại mốc |
| **7** | File 12: loc toàn bộ | `verify_all_loc.py` PASS (BOM, 0 trùng, 0 mồ côi); `ev.py` 0 thiếu loc |
| **8** | (Tùy chọn) AI soft-link Trục 1/2, bảng 6.3 | Không đổi điều kiện mở; chỉ đổi trọng số |
| **9** | File 15 + cập nhật `VIE_cross_axis_review.md` (thêm bảng cờ Trục 3) | Checklist mục 7 |

## 6.3 · Bước 8: AI soft-link (tùy chọn)

Báo cáo 4.2, chuyển sang cờ thật. Chỉ **cộng trọng số** `ai_chance` / `ai_will_do`, không đổi `visible/available`/hiệu ứng. Nếu bỏ bước này Trục 1 và 2 vẫn nguyên vẹn.

| Nơi | Hướng | Việc |
|---|---|---|
| `vie_proc_army.18` option A, `.19` option A/B, `.30` option B, `.35` option A, `.38` option A | `VIE_lf_regular` | thêm `modifier = { factor = 1.3 has_country_flag = VIE_lf_regular }` |
| `vie_proc_army.8` option A (Igla kèm quyền SX) | `VIE_lf_depth` | cùng khuôn |
| `VIE_dec_pth` (D3), `VIE_dec_xcb01`, `VIE_dec_xcb01_fast` (D6) | `VIE_lf_regular` | trong `ai_will_do` |
| `VIE_dec_tl01` (D9) | `VIE_lf_depth` | trong `ai_will_do` |

## 6.4 · Bộ kiểm tĩnh sau mỗi bước

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py     # 0 missing ở mọi nhóm
python3 tools/audit/ev.py       # 0 trùng, 0 orphan, 0 thiếu loc
python3 tools/audit/audit.py    # 0 dangling, 0 forward-ref, 0 cycle, 0 trùng tọa độ
python3 tools/audit/lf_balance.py
```

## 6.5 · Khung code (mẫu để bước 2–6 chép theo)

**Khởi tạo biến (bước 0), thay khối Trục 2 hiện tại**
```pdx
if = {
	limit = { NOT = { has_country_flag = VIE_def_ind_vars_init } }
	set_variable = { VIE_def_industry_level = 0 }
	set_variable = { VIE_def_ind_export_count = 0 }
	set_country_flag = VIE_def_ind_vars_init
}
if = {
	limit = { NOT = { has_country_flag = VIE_lf_vars_init } }
	set_variable = { VIE_lf_arm_count = 0 }
	set_variable = { VIE_lf_arm_done = 0 }
	set_variable = { VIE_lf_cap_count = 0 }
	set_variable = { VIE_lf_cap_done = 0 }
	set_country_flag = VIE_lf_vars_init
}
```

**Trigger cổng (file 1)**
```pdx
VIE_lf_gate_open = {
	OR = {
		date > 2019.2.10
		AND = {
			VIE_ai_free = yes
			date > 2012.12.31
			VIE_def_ind_level_ge_2 = yes
		}
	}
}
VIE_lf_fav_land  = { has_country_flag = VIE_lf_depth }
VIE_lf_fav_ad    = { has_country_flag = VIE_lf_regular }
VIE_lf_fav_cyber = { has_country_flag = VIE_lf_mobile }
```

**Focus gốc (N1) và node đầu binh chủng (file 7)**
```pdx
focus = {
	id = VIE_lf_army_reform
	icon = army_reform
	x = 12
	y = 1
	relative_position_id = VIE_modernize_vpa
	cost = 10
	prerequisite = { focus = VIE_modernize_vpa }
	search_filters = { FOCUS_FILTER_ARMY }
	available = { VIE_lf_gate_open = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_army_reform"
		VIE_lf_n1_reward = yes
	}
	ai_will_do = {
		base = 60
		modifier = { factor = 3 date > 2022.1.16 }
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}

focus = {
	id = VIE_lf_arm_infantry_org
	icon = army_planning
	x = -6
	y = 2
	relative_position_id = VIE_lf_army_reform
	cost = 7
	prerequisite = { focus = VIE_lf_logistics_merge }
	prerequisite = { focus = VIE_lf_basic_training }
	search_filters = { FOCUS_FILTER_ARMY }
	available = { VIE_lf_arm_slot_free = yes }
	completion_reward = {
		log = "[GetDateText]: [Root.GetName]: Focus VIE_lf_arm_infantry_org"
		if = {
			limit = { VIE_lf_arm_slot_free = yes }
			add_to_variable = { VIE_lf_arm_count = 1 }
			VIE_lf_bb1_reward = yes
		}
	}
	ai_will_do = {
		base = 60
		modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
	}
}
```
HD đòi **OR** bốn binh chủng:
```pdx
focus = {
	id = VIE_lf_combined_arms
	...
	prerequisite = {
		focus = VIE_lf_arm_infantry_train
		focus = VIE_lf_arm_armor_train
		focus = VIE_lf_arm_arty_train
		focus = VIE_lf_arm_engineers
	}
	available = { VIE_lf_arm_done_3 = yes }
```
ME ba chiều (FR1; FM1 và FD1 lặp lại đối xứng):
```pdx
	prerequisite = { focus = VIE_lf_command_reform_1 }
	mutually_exclusive = { focus = VIE_lf_fs_mobile_force focus = VIE_lf_fs_depth_defence }
```

**Phần thưởng theo cờ hướng (file 2), ví dụ CR2**
```pdx
VIE_lf_cr2_reward = {
	if = {
		limit = { has_country_flag = VIE_lf_regular }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_defence_factor = 0.005 tooltip = VIE_tt_army_defence_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_mobile }
		add_to_variable = { VIE_af_army_org_factor = 0.015 tooltip = VIE_tt_army_org_factor }
		add_to_variable = { VIE_af_army_speed_factor = 0.01 tooltip = VIE_tt_army_speed_factor }
	}
	else_if = {
		limit = { has_country_flag = VIE_lf_depth }
		add_to_variable = { VIE_af_army_defence_factor = 0.015 tooltip = VIE_tt_army_defence_factor }
		add_to_variable = { VIE_af_max_dig_in_factor = 0.01 tooltip = VIE_tt_max_dig_in_factor }
	}
	VIE_lf_refresh = yes
}
VIE_lf_refresh = { force_update_dynamic_modifier = yes }
```
Số cho từng node chép từ bảng 5.4. Dùng literal như trên (không dùng biến tạm) vì tooltip của repo đã chạy tốt với literal; ô sở trường (×1,5) viết thành nhánh `if = { limit = { VIE_lf_fav_ad = yes } ... } else = { ... }` riêng.

**Decision (file 9), ví dụ**
```pdx
VIE_military_readiness_category = {
	VIE_dec_lf_train_terrain = {
		icon = GFX_decision_generic_army_support
		cost = 35
		days_re_enable = 545
		visible = { has_completed_focus = VIE_lf_command_reform_1 }
		available = { has_war = no }
		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_lf_train_terrain"
		}
		days_remove = 90
		remove_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_dec_lf_train_terrain (complete)"
			VIE_lf_xp_10 = yes
			add_timed_idea = { idea = VIE_lf_idea_terrain_drill days = 180 }
		}
		ai_will_do = {
			base = 15
			modifier = { factor = 0 VIE_def_ind_bankrupt = yes }
		}
	}
}
```

**Scheduler (file 2), ví dụ `vie_lf.3`** (cùng khuôn `VIE_event_scheduler_p15`)
```pdx
VIE_event_scheduler_p17 = {
	if = {
		limit = { NOT = { check_variable = { VIE_catch_up = 1 } } }
		if = {
			limit = {
				date > 2023.11.30
				NOT = { has_country_flag = VIE_lf_ms_corps12 }
			}
			if = {
				limit = { NOT = { has_country_flag = VIE_popup_cd } }
				set_country_flag = VIE_lf_ms_corps12
				set_country_flag = { flag = VIE_popup_cd days = 45 }
				country_event = { id = vie_lf.3 days = 3 random_days = 15 }
			}
			else_if = {
				limit = { date > 2024.5.31 }
				set_country_flag = VIE_lf_ms_corps12
				VIE_lf_ms_corps12_apply = yes
			}
		}
		# ... .1 .2 .4 .5 tương tự
	}
}
```

---

# PHẦN 7 — CHECKLIST TEST (cần máy có HOI4)

**Cấu hình và log**
- [ ] `error.log` grep `VIE_lf_`, `vie_lf`, `VIE_dec_lf_`, `reduce_focus_completion_cost`, `force_update_dynamic_modifier`, `army_personnel_cost`, `urban_attack_factor`.
- [ ] Số slot focus của MD thật = 1? (G1) Nếu ≥ 2: chạy lại bảng 8.12 và test vượt giới hạn.
- [ ] **X1**: load một save năm 2015 sau khi làm xong vài decision Trục 2: `VIE_def_industry_level` không về 0.

**Cổng và cây**
- [ ] N1 xám trước 11/2/2019 ở `plausible`/`historical`; ở `free` mở khi `VIE_def_industry_level ≥ 2` và sau 2012.
- [ ] Binh chủng: sau 3 node đầu, node đầu thứ tư xám; BB2/TG2/PB2 vẫn bấm được; HD xám đến khi `arm_done ≥ 3`; mọi tổ hợp 3/4 mở được HD (đặc biệt BB+TG+CB).
- [ ] ME ba chiều FM1/FR1/FD1 và hai chiều PS/PT; PS/PT mở được từ FM2, FR2 **hoặc** FD2.
- [ ] Lĩnh vực: sau hai gốc, gốc thứ ba xám; MOD xám khi `cap_done < 2`; chọn hai lĩnh vực bất kỳ đều ra MOD.
- [ ] Cờ sở trường: sau FR1, gốc A1 rẻ hơn 14 ngày so với gốc L1/Y1 (tooltip thời gian).

**Số và modifier**
- [ ] Tooltip `VIE_armed_forces_modifier` đổi ngay sau mỗi node (nếu không, `force_update_dynamic_modifier` có hiệu lực?).
- [ ] `army_attack_factor`, `conscription_factor` hiện dòng riêng; hai modifier chi phí MD: +2% là +2% hay ×1,02? (ảnh hưởng FM1/FR1/PS/PT).
- [ ] `reduce_focus_completion_cost cost = 35` làm N1 từ 70 xuống 35 **ngày** (G6), không phải tuần.
- [ ] Tổng cuối đường đầy đủ khớp `lf_balance.py` (tốc độ ≤ 25, dig-in ≤ 26, tổ chức ≤ 21).
- [ ] Mẫu "Cụm cơ động" và "Dân quân" xuất hiện trong bảng mẫu sư đoàn, không báo lỗi regiment.

**Decision và event**
- [ ] 6 decision nằm đúng `VIE_military_readiness_category` (khối trùng tên ở hai file có gộp không?), cạnh 4 decision cũ.
- [ ] `days_re_enable` đếm từ lúc bấm hay lúc xong? (ảnh hưởng ước tính XP/năm, mục 5.8.)
- [ ] Ý tưởng tạm biến mất sau 180 ngày; tên modifier đô thị đúng.
- [ ] Event: `event vie_lf.1` … `.5`; ngày; không hai pop-up trong 45 ngày; 2024 không có pop-up `vie_lf`; catch-up chỉ đặt cờ.
- [ ] Đo lại số pop-up 2022/2023/2024/2025 sau khi thêm (luật ≤ 7/năm).

**AI (bước 8)**
- [ ] Quan sát một ván AI (`observe`): có đi Trục 3 sau 2019, hướng chọn đúng theo path, không kẹt (`bankruptcy_incoming_collapse`).

---

# PHỤ LỤC A — 6 decision "nhóm chung" (Q14, tùy chọn)

Báo cáo 8.14 đặt ngoài Trục 3 Lục quân. Nếu làm, cổng dùng trigger **có thật** (R2), cũng vào `VIE_military_readiness_category`:

| Decision | Cổng đề xuất | Ghi chú |
|---|---|---|
| Huấn luyện chống ngầm | thuộc plan Hải quân | Cần `VIE_var_hulls_*` của báo cáo hải quân |
| Huấn luyện BVR | thuộc plan Không quân | Cần trục Không quân |
| Diễn tập song phương | `has_completed_focus = VIE_us_comprehensive_partnership` hoặc `VIE_india_partnership` hoặc `VIE_japan_partnership` | thay "quan hệ ≥ ngưỡng" chưa định nghĩa |
| Diễn tập đa phương | `has_completed_focus = VIE_asean_integration` | thay cờ chưa tồn tại |
| Cứu trợ thảm họa (HADR) | `has_country_flag = VIE_disaster_prepared` | `VIE_disaster_events.txt` đã có sự kiện thiên tai |
| Triển khai gìn giữ hòa bình | `has_completed_focus = VIE_un_peacekeeping` | focus đã có XP + opinion; decision chỉ lặp lại phần XP |

Chỉ bốn dòng cuối là việc của Lục quân/Chung; hai dòng đầu để plan Hải quân và Không quân.

---

# PHỤ LỤC B — `tools/audit/lf_balance.py` (bước 0)

Dữ liệu: bảng 5.4 (giá trị mới) và hệ số `W`, `S`. In ba thứ và **fail** nếu vượt ngưỡng:
1. điểm từng node theo `W' = W/S` so với điểm báo cáo (lệch ≤ 0,4);
2. ròng ba hướng FFS (lệch nhau ≤ 0,4);
3. tổng cộng dồn cho 9 đường (3 hướng × 3 cặp lĩnh vực) và so với trần: tốc độ ≤ 25, dig-in ≤ 26, tổ chức ≤ 21, phòng thủ ≤ 16, nhân lực ≤ 12, tấn công ≤ 10, hậu cần ≥ −10.

Kết quả tôi đã chạy (cùng dữ liệu): tốc độ tối đa 24,5 · dig-in 25,5 · tổ chức 21 · phòng thủ 15,5 · nhân lực 12 · tấn công 10 · hậu cần −10.

---

# PHỤ LỤC C — Những gì chưa kiểm chứng

| Hạng mục | Rủi ro | Cách xử lý |
|---|---|---|
| Số slot focus = 1 | trung bình | checklist mục 7; bảo hiểm count đã có |
| `on_startup` chạy lại khi load (X1) | cao nếu đúng | guard vô hại cả hai trường hợp |
| `reduce_focus_completion_cost` đơn vị ngày | trung bình | suy từ tiền lệ `VIE_code_of_conduct`; test bắt buộc |
| Đơn vị hai modifier chi phí MD | trung bình | test; đổi 4 số nếu sai |
| `urban_attack_factor` có tồn tại | thấp | thay `terrain_penalty_reduction` nếu không |
| Hai khối category trùng tên ở hai file có gộp | thấp | nếu không: chuyển 6 decision vào `VIE_md_decisions.txt` |
| `days_re_enable` bắt đầu đếm lúc nào | thấp | ảnh hưởng XP/năm |
| Nghị quyết 1657-NQ/QUTW (20/12/2022) | thấp | chưa tra lại; đổi mốc của `vie_lf.2` nếu sai |
| PP thu nhập thật của VIE (M ≈ 70) | trung bình | neo vào decision cũ; đo rồi chỉnh 6 số |

---

# NGUỒN

- Báo cáo Lục quân VIE — Trục 1, 2, 3, mục III, VIII, IX, bảng 9.10 (repo).
- Repo: `common/national_focus/VIE_md_focus.txt` (cụm `VIE_peoples_defence`, Trục 2), `common/decisions/VIE_md_decisions.txt`, `common/decisions/categories/VIE_md_categories.txt`, `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt`, `common/on_actions/VIE_md_on_actions_startup.txt`, `common/scripted_triggers/VIE_md_triggers_p4.txt` và `_p15.txt`, `common/scripted_effects/VIE_md_effects_p15.txt`, `common/ideas/VIE_md_ideas_p2.txt`, `events/VIE_md_p11.txt:193`, `tools/TESTING.md`, `tools/audit/md_ref/VIE_2000_nsb.txt`.
- Các review sẵn có: `VIE_truc1_review_and_plan.md` (A1), `VIE_truc2_review_and_plan.md` (A1, L4), `VIE_cross_axis_review.md`, báo cáo hải quân bản 2.4 (mục 2, 3.1, 11).
- MD (GitHub): [`common/defines/MD_defines.lua`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/defines/MD_defines.lua), [`.claude/docs/focus-tree-reference.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/focus-tree-reference.md), [`.claude/docs/decision-reference.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/decision-reference.md), [`.claude/docs/md-custom-modifiers.md`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/.claude/docs/md-custom-modifiers.md), [`common/modifier_definitions/money_modifier_definitions.txt`](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/modifier_definitions/money_modifier_definitions.txt).
- Mốc lịch sử đã đối chiếu: [Báo Pháp luật VN / Chính phủ về Nghị quyết 05-NQ/TW](https://xaydungchinhsach.chinhphu.vn/co-ban-hoan-thanh-dieu-chinh-to-chuc-luc-luong-quan-doi-tinh-gon-manh-119250213160854185.htm), [Quân đoàn 12](https://xaydungchinhsach.chinhphu.vn/cong-bo-quyet-dinh-thanh-lap-quan-doan-12-quan-doan-tinh-gon-manh-dau-tien-cua-quan-doi-nhan-dan-viet-nam-119231202122003205.htm), [Quân đoàn 34](https://xaydungchinhsach.chinhphu.vn/cong-bo-quyet-dinh-thanh-lap-quan-doan-34-119241215103454169.htm), [Hậu cần – Kỹ thuật](https://dantri.com.vn/thoi-su/bo-quoc-phong-sap-nhap-tong-cuc-hau-can-va-tong-cuc-ky-thuat-20250205151535963.htm).