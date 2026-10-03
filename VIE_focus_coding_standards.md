# VIE Focus Tree — Coding Standards & Architecture Guide
> Áp dụng cho: `common/national_focus/VIE_md_focus.txt`  
> Cơ sở: MD4 conventions từ `.claude/docs/` + audit thực tế file v14 (11 929 dòng, 357 focus)  
> Cập nhật: 03/10/2026

---

## 1. CẤU TRÚC FILE TỔNG QUAN

### 1.1 Bộ khung file

```pdx
## Vietnam focus tree header comment (file-level)
## Changelog ## vN (dd/mm/yyyy): ...
focus_tree = {
    id = VIE_md_focus

    country = { factor = 0; modifier = { add = 100; original_tag = VIE } }

    continuous_focus_position = { x = 765 y = 2850 }
    initial_show_position = { focus = VIE_doi_moi_continues }

    shortcut = { name = ... target = ... scroll_wheel_factor = 0.60 }
    ...

    ###############################
    ## TÊN NHÁNH / KHỐI
    ###############################
    focus = { ... }
}
```

### 1.2 Thứ tự khai báo trong `focus_tree = {}`

| Vị trí | Nội dung |
|--------|----------|
| 1 | `id`, `country` block |
| 2 | Changelog comments `## vN` |
| 3 | `continuous_focus_position`, `initial_show_position` |
| 4 | Các `shortcut = { ... }` theo thứ tự UI |
| 5 | Các khối `focus = { ... }` theo nhóm logic, có section header |

---

## 2. FOCUS BLOCK — THỨ TỰ TRƯỜNG BẮT BUỘC

### 2.1 Chuẩn MD4

```pdx
focus = {
    id = VIE_<slug>
    icon = <icon_name>

    x = <N>
    y = <N>
    relative_position_id = VIE_<anchor>   # bỏ nếu tọa độ tuyệt đối

    cost = <5|7|16>                        # BỎ QUA nếu = 10 (default MD)

    prerequisite = { focus = VIE_<parent> }
    mutually_exclusive = { focus = VIE_<mx> }

    will_lead_to_war_with = TAG            # chỉ khi tạo wargoal

    search_filters = { FOCUS_FILTER_<A> FOCUS_FILTER_<B> }

    available = { ... }
    bypass = { ... }

    completion_reward = {
        log = "[GetDateText]: [Root.GetName]: Focus VIE_<slug>"
        <effects>
    }

    ai_will_do = { base = <N> }
}
```

### 2.2 Quy tắc từng trường

| Trường | Quy tắc |
|--------|---------|
| `id` | Đầu tiên, prefix `VIE_`, snake_case |
| `icon` | Sau `id`, trước `x`/`y` |
| `cost` | **Bỏ nếu = 10** (omit defaults). Viết khi = 5, 7, hay bất thường |
| `prerequisite` | AND = nhiều block `prerequisite = {}` riêng. OR = một block với nhiều `focus =` |
| `search_filters` | Luôn có |
| `completion_reward` | Dòng đầu: `log = "..."` |
| `ai_will_do` | Trường CUỐI CÙNG |

---

## 3. `cost` — THANG GIÁ

| Giá trị | Ý nghĩa |
|---------|---------|
| `cost = 5` | Focus cơ bản / chuẩn bị (25 ngày) |
| `cost = 7` | Focus hành động thực chất (35 ngày) — phổ biến nhất |
| _(omit)_ | Default = 10 (50 ngày) |
| `cost = 16` | Chỉ `VIE_spratly_fortification` — ngoại lệ có chủ đích |

> ❌ **KHÔNG** viết `cost = 10` tường minh — MD validator báo lỗi "Omit defaults".

---

## 4. `search_filters` — DANH SÁCH HỢP LỆ

```
FOCUS_FILTER_POLITICAL
FOCUS_FILTER_ECONOMY
FOCUS_FILTER_INDUSTRY
FOCUS_FILTER_STABILITY
FOCUS_FILTER_ARMY
FOCUS_FILTER_AIRCRAFT     # KHÔNG dùng FOCUS_FILTER_AIR (alias cũ)
FOCUS_FILTER_RESEARCH
FOCUS_FILTER_MILITARY_LAWS
FOCUS_FILTER_MANPOWER
```

> ⚠️ **FOCUS_FILTER_NAVY** đã xóa khỏi cây VIE (v12) — không dùng lại.

---

## 5. `ai_will_do` — PATTERN CHUẨN

### Simple base (1 dòng)

```pdx
ai_will_do = { base = 70 }
```

### Multi-line khi có modifier

```pdx
ai_will_do = {
    base = 70
    modifier = { factor = 0 can_staff_an_industrial_complex = no }
    modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }
}
```

### Các condition chuẩn MD

| Condition | Khi nào dùng |
|-----------|-------------|
| `factor = 0 can_staff_an_industrial_complex = no` | Focus xây IC/AF/dockyard |
| `factor = 0 has_active_mission = bankruptcy_incoming_collapse` | Focus chi ≥ 5 bn treasury |
| `factor = 0 VIE_ai_historical = yes` | Focus alt-history |
| `factor = 4 VIE_ai_historical = yes` | Focus lịch sử bắt buộc (AI ưu tiên mạnh) |

---

## 6. `completion_reward` — QUY TẮC REWARD

### Dòng đầu bắt buộc

```pdx
completion_reward = {
    log = "[GetDateText]: [Root.GetName]: Focus VIE_<slug>"
    ...
}
```

### Scripted effects chuẩn (ưu tiên hơn `add_building_construction` trực tiếp)

| Effect | Chi phí treasury | Dùng khi |
|--------|-----------------|----------|
| `one_state_industrial_complex = yes` | -7.5 bn | Xây IC |
| `one_state_air_force_base = yes` | -7.5 bn | Xây AF |
| `one_state_dockyard = yes` | -7.5 bn | Xây dockyard |
| `one_state_infrastructure = yes` | -3.5 bn | Xây infra lv1 |
| `one_state_anti_air = yes` | -3.25 bn | Xây AA |
| `one_state_air_base = yes` | -3.0 bn | Xây air base |
| `one_state_radar_station = yes` | -1.75 bn | Xây radar |
| `increase_economic_growth = yes` | — | Tăng GDP |
| `decrease_corruption = yes` | — | Giảm tham nhũng |

### Treasury thủ công

```pdx
set_temp_variable = { treasury_change = -3 }
modify_treasury_effect = yes
```

### Opinion groups hợp lệ trong VIE

```pdx
set_temp_variable = { temp_opinion = 5 }
change_industrial_conglomerates_opinion = yes
# Các group: communist_cadres, industrial_conglomerates, farmers, the_military
```

### Lỗi cần tránh trong reward

| ❌ Sai | ✅ Đúng |
|--------|--------|
| `set_country_flag = { flag = X days = N }` | `set_country_flag = { flag = X days = N value = 1 }` |
| `check_variable = { X >= N }` | `check_variable = { X > M }` (M = N-1) |
| `[TEXT]` trong localisation | `(TEXT)` hoặc `§RTEXT§!` |
| `add_building_construction` trực tiếp | Dùng `one_state_*` scripted effect |

---

## 7. LAYOUT & TỌA ĐỘ

### 7.1 Quy tắc gap (khoảng cách y trong chuỗi)

| Gap y hiện tại | Chuẩn hóa thành |
|----------------|-----------------|
| ≤ 2 | Giữ nguyên |
| 3–9 | → 2 |
| 10–19 | → 4 |
| ≥ 20 | → 8 |

### 7.2 ENGINE RULE: forward reference trong `relative_position_id`

HOI4 giải quyết `relative_position_id` theo **thứ tự khai báo trong file**.  
**Anchor PHẢI khai báo TRƯỚC tất cả node con dùng nó.**

```pdx
# ✅ ĐÚNG
focus = { id = VIE_anchor  x = 10  y = 0 }
focus = { id = VIE_child   x = 0   y = 1  relative_position_id = VIE_anchor }

# ❌ SAI — forward reference
focus = { id = VIE_child   x = 0   y = 1  relative_position_id = VIE_anchor }
focus = { id = VIE_anchor  x = 10  y = 0 }
```

### 7.3 State references quan trọng

| State ID | Tên | Chủ | Ghi chú |
|----------|-----|-----|---------|
| 519 | Red River Delta | VIE | Hà Nội |
| 522 | Mekong Delta South | VIE | TP.HCM |
| 518 | Mekong Delta West | VIE | Cần Thơ, Phú Quốc |
| 801 | Western Spratlys | VIE | naval_base tại 11134/11140/11149/11168 ✅ |
| 813 | Paracel Islands | CHI | VIE có claim |
| 526 | Northern Spratlys | CHI | ❌ KHÔNG build — CHI sở hữu |

---

## 8. SECTION HEADER FORMAT

### Cấu trúc chuẩn (1 tab indent, 31 dấu `#`)

```pdx
	###############################
	## TÊN NHÁNH
	###############################
	focus = { ... }
```

### Comment anchor (v-fix)

```pdx
	## v6-fix: anchor moved above its dependents (engine resolves relative_position_id in file order)
	focus = { id = VIE_<anchor> ... }
```

### Comment WARNING

```pdx
	# WARNING focus: creates a limited wargoal on the Paracels.
	focus = { id = VIE_paracel_ultimatum ... }
```

---

## 9. VẤN ĐỀ HIỆN TẠI TRONG FILE (Audit v14, 03/10/2026)

### Số liệu nhanh

| Chỉ số | Giá trị |
|--------|---------|
| Tổng focus | 357 |
| `cost = 5` | 62 |
| `cost = 7` | 233 |
| `cost` bỏ qua (= 10 default) | 60 |
| `cost = 16` (ngoại lệ) | 1 |
| `ai_will_do` 1 dòng | 201 |
| `ai_will_do` multi-line | 153 |
| Double blank lines | 6 |
| Trailing whitespace | 0 ✅ |

### Bugs cần fix

| # | Mức | Mô tả | Số lượng | Fix |
|---|-----|-------|----------|-----|
| **B1** | 🔴 Critical | `00_yearly_effects.txt` ghi đè MD | 1 file | `git rm` |
| **B2** | 🔴 Critical | `VIE_md_mil.txt` trùng event ID | 1 file | `git rm` |
| **B3** | 🔴 Critical | `check_variable >= N` parse sai | 6 triggers | `> N-1` |
| **B4** | 🔴 Critical | Timed flag thiếu `value = 1` | ~163 | Thêm `value = 1` |
| **B5** | 🟡 High | `[TEXT]` trong localisation | ~31 | → `(TEXT)` |
| **B6** | 🟡 Minor | Double blank lines | 6 | Xóa |
| **B7** | ℹ️ Info | `allowed = { always = no }` thừa trong ideas | nhiều | Xóa (convention) |

---

## 10. KIẾN TRÚC CÂY — NHÓM LOGIC

### 10.1 Multi-root design (4 root từ v2)

| Root | Nhóm | Ghi chú |
|------|------|---------|
| `VIE_doi_moi_continues` | Kinh tế (master) | Shortcut target chính |
| `VIE_prepare_congress_9` | Đại hội Đảng | Timeline 2001–2030+ |
| `VIE_asean_integration` | Ngoại giao | ASEAN + quốc tế |
| `VIE_modernize_vpa` | Quân sự | Root duy nhất sau v11 |

Mỗi root guard bởi `VIE_ax_init` + `VIE_ax_initialized` flag (init 1 lần duy nhất).

### 10.2 Nhóm focus chính

```
CHINH TRI
  Đại hội (congress 9→14) → institutional_opening / concentration_of_power → era_of_rising
  Chống tham nhũng: anti_corruption_steering → party_discipline → party_inspection
  Nhà nước pháp quyền: rule_of_law_state → constitution_2013

KINH TE
  Đổi mới: enterprise_law → fdi_attraction → wto
  Tài chính: state_bank → state_conglomerates → cashless
  Công nghiệp: industrialization_strategy → samsung → supporting_industries
  Năng lượng: power_plan_8 → jetp → offshore_wind → net_zero
  Hạ tầng: north_south_expressway → HSR → urbanization
  Digital: internet_expansion → 3G/4G → 5G → AI

BIEN DONG
  Luật Biển (law_of_the_sea root)
    ├── maritime_militia → spratly_fortification
    ├── fisheries_surveillance → coast_guard_law
    ├── legal_warfare (alt: assert_maritime_rights → paracel_ultimatum ⚠️)
    └── dk1_platforms
  Hợp tác: scs_maritime_cooperation → multilateral_exercise → cam_ranh_port → joint_training

NGOAI GIAO
  ASEAN: asean_integration → border_settlement → asean_chair → code_of_conduct
  Trung Quốc: 16_words → defence_hotline → shared_future
  Lào/Campuchia: special_relations_laos, cambodia_relations, indochina_solidarity

QUAN SU
  VIE_modernize_vpa
  Không quân (airf_*): ~50 focus, nhiều nhánh (iads, multirole, unmanned)
```

---

## 11. KẾ HOẠCH CODING (PRIORITIZED PLAN)

### Phase 0 — Dọn dẹp bắt buộc (trước khi code mới bất cứ thứ gì)

| Task | File | Priority | Est. |
|------|------|----------|------|
| P0-1 | `git rm common/scripted_effects/00_yearly_effects.txt` | 🔴 | 1 phút |
| P0-2 | `git rm events/VIE_md_mil.txt` | 🔴 | 1 phút |
| P0-3 | Fix `check_variable >=` → `>` (6 trigger files) | 🔴 | 30 phút |
| P0-4 | Fix timed flag thiếu `value = 1` (script sed/python) | 🔴 | 1 giờ |
| P0-5 | Fix `[TEXT]` → `(TEXT)` trong localisation | 🟡 | 30 phút |
| P0-6 | Xóa double blank lines (6 chỗ) | 🟡 | 10 phút |
| P0-7 | Xóa `allowed = { always = no }` thừa trong ideas | 🟡 | 30 phút |

### Phase 1 — Nhánh Chủ nghĩa Dân tộc (v10 đã remove, cần redesign)

Xem: `VIE_nationalism_branch_research_report.md`
- ~20–30 focus mới
- Root: cần xác định (kết nối với Đảng hay Chính phủ?)
- Shortcut: `VIE_nat_shortcut` (đã xóa, sẽ thêm lại)

### Phase 2 — Mua sắm vũ khí (v9 extracted → events)

Xem: `VIE_v9_flag_mapping.md`
- Events trong `events/VIE_md_arms.txt` (hoặc tên tương đương)
- Mỗi event **BẮT BUỘC** set `has_country_flag = VIE_ev_<slug>`
- Gate focus còn sống dùng `has_country_flag` (không `has_completed_focus`)

### Phase 3 — Nhánh Quân sự mở rộng

Xem: `v11_removed_military_all_subbranches.txt`, `VIE_military_branch_design_v3.md`
- Quyết định nhánh nào phục hồi
- Gắn vào `VIE_modernize_vpa` như các sub-chain

### Phase 4 — QA & Polish

```bash
# Sparse clone MD để chạy validator
git clone --depth 1 --filter=blob:none --sparse https://github.com/MillenniumDawn/Millennium-Dawn.git md
cd md && git sparse-checkout set tools .claude/docs
# Copy mod content
python tools/validation/run_all_validators.py --no-color --output report.txt
```

Test theo `tools/TESTING.md`:
- VIE_popup_cd chặn double pop-up (sau B4 fix)
- Tất cả focus localisation hiển thị đúng (sau B5 fix)
- Axis system `VIE_ax_*` khởi tạo đúng với bất kỳ root nào taken first

---

## 12. CHECKLIST KHI VIẾT FOCUS MỚI

```
□ id = VIE_<slug>  (snake_case, prefix VIE_)
□ icon hợp lệ (GFX tồn tại trong gfx/ hoặc MD base)
□ Tọa độ x,y không trùng với focus khác trong cùng cây
□ relative_position_id anchor khai báo TRƯỚC trong file
□ cost bỏ nếu = 10; viết nếu = 5, 7, hoặc bất thường
□ prerequisite: AND = nhiều block riêng; OR = một block nhiều focus
□ mutually_exclusive: đảm bảo A mx B VÀ B mx A
□ search_filters dùng đúng tên filter (xem Section 4)
□ available: dùng has_country_flag thay vì has_completed_focus cho focus có thể skip
□ completion_reward: dòng đầu là log = "..."
□ KHÔNG dùng check_variable >= / <=  →  dùng > / <
□ Timed flag: set_country_flag = { flag = X days = N value = 1 }
□ Treasury: dùng scripted effect one_state_* hoặc modify_treasury_effect
□ KHÔNG viết allowed = { always = no } trong idea liên quan
□ ai_will_do: trường cuối; thêm modifier bankruptcy nếu chi >= 5bn
□ Localisation: không dùng [] ngoại trừ scripted loc thực sự
□ Sau viết xong: grep để verify không duplicate id
□ Chạy validator sau mỗi batch focus mới
```

---

## 13. TÀI LIỆU THAM KHẢO

| File | Nội dung |
|------|----------|
| [`VIE_review_3_axes_md_conventions.md`](file:///d:/HOI4Mods/md_vietnam/VIE_review_3_axes_md_conventions.md) | Audit lỗi convention chi tiết |
| [`VIE_md_states_reference.md`](file:///d:/HOI4Mods/md_vietnam/VIE_md_states_reference.md) | State ID, owner, province |
| [`VIE_v9_flag_mapping.md`](file:///d:/HOI4Mods/md_vietnam/VIE_v9_flag_mapping.md) | Flag mapping cho vũ khí extract v9 |
| [`VIE_nationalism_branch_research_report.md`](file:///d:/HOI4Mods/md_vietnam/VIE_nationalism_branch_research_report.md) | Thiết kế nhánh dân tộc chủ nghĩa |
| [`VIE_military_branch_design_v3.md`](file:///d:/HOI4Mods/md_vietnam/VIE_military_branch_design_v3.md) | Thiết kế nhánh quân sự |
