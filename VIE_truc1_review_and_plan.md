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

## C8 · `rule_vie_alt_procurement` trùng chức năng với rule đã có

Mod đã có `VIE_alt_history` (`common/game_rules/VIE_md_rules.txt`) với 3 option **Plausible / Historical / Free**, và `VIE_ai_behavior` với 5 path. Thêm rule thứ ba tên `rule_vie_alt_procurement` → người chơi thấy 3 nút "alt history" khác nhau cho một nước.

Hai lựa chọn: (a) tái dùng `VIE_alt_history` — chuỗi 7–9 chỉ vào lịch khi `option = free`; (b) giữ rule riêng nhưng đặt `group = "MD_FOCUS_TREE_RULES"` ✅ (hợp lệ) và ghi rõ trong loc rằng nó **chỉ** điều khiển mua sắm. → **cần bạn chốt (Q4)**.

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
# Separate from VIE_alt_history, which drives the regime bands.
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

**Q4 · Rule alt-history.** Tái dùng `VIE_alt_history` sẵn có (option `free`), hay thêm `rule_vie_alt_procurement` riêng như báo cáo?

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
