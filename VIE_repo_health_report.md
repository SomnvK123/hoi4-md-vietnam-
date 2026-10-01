# BÁO CÁO ĐỌC REPO — `SomnvK123/hoi4-md-vietnam-`

> Đọc ngày 2026-09-30 · commit `f05cfa1` (main) · clone depth 50 tại `/home/user/repo`
> Mọi con số bên dưới đều **đo bằng script** trên bản clone, không ước lượng.

---

## 1. Repo là gì

| | |
|---|---|
| Tên mod | **MD Vietnam (dev)** — `descriptor.mod` v0.4.1 |
| Loại | **Submod** của *Millennium Dawn: A Modern Day Mod* (`dependencies`) |
| HOI4 | `supported_version="1.19.*"` |
| Tags | Alternative History · Events · National Focuses |
| Nước chơi | `VIE` (Việt Nam), mốc **2000 → 2026** |
| Commits | 38 · nhánh remote: `main`, `claude/busy-gates-11nw9x`, `claude/inspiring-brown-wilngw` (2 nhánh claude đã merge) |
| Dung lượng | 45 MB working tree (`.git` chỉ 4.1 MB) · 223 file |
| Commit mới nhất | `f05cfa1` — *"feat: add new military decisions, events, and focus files while archiving previous subbranches"* (30/9/2026) |

Repo **không có** `README.md`, `.gitignore`, `LICENSE`.

---

## 2. Cấu trúc thư mục

```
common/
  national_focus/     VIE_md_focus.txt (209 KB) + VIE_md_focus.txt.bak (343 KB, bản cũ 409 focus)
  decisions/          VIE_md_decisions.txt (33 decision) + categories/ (3 category)
  ideas/              14 file, 156 idea
  scripted_effects/   16 file, 67 effect
  scripted_triggers/   5 file, 29 trigger
  scripted_localisation/ VIE_md_axis_bars.txt (21 KB — thanh trục 9 chiều)
  bop/                VIE_party_balance + VIE_oligarch_balance
  dynamic_modifiers/  VIE_armed_forces_modifier, VIE_state_modifier
  opinion_modifiers/  14 modifier (ASEAN, HD-981, hiệp định biên giới…)
  game_rules/         VIE_alt_history (Plausible/Historical/Free), VIE_ai_behavior (5 path + RANDOM)
  on_actions/         on_monthly (13 scheduler), on_startup, on_civil_war_end
  bookmarks/          blitzkrieg.txt — copy toàn bộ file của MD, chèn khối "VIE"
  military_industrial_organization/  4 organization
  ai_strategy/ difficulty_settings/
events/               21 file · 164 event · 14 namespace (vie_pol, vie_eco, vie_scs, vie_dip, vie_col, vie_int, vie_alt, vie_cor, vie_soc, vie_axis, vie_news, vie_petro, vie_auto, vie_disaster)
localisation/english/ 17 file gốc + 23 file trong replace/ · 2225 key · 100% tiếng Việt · UTF-8 **có BOM** (đúng chuẩn)
gfx/
  fonts/              26 cặp .fnt + .dds = 38 MB (84% dung lượng repo)
  leaders/VIE/        8 chân dung (Lê Khả Phiêu, Nông Đức Mạnh, Nguyễn Tấn Dũng, Tô Lâm + 4 tướng) + 4 bản small
  interface/decisions/ 10 icon .tga
interface/            fonts.gfx, load_screen_font.gfx, VIE_md_decision_icons.gfx
tools/                6 script Python + TESTING.md (62 KB — vừa là test script vừa là build log)
*.md (19 file)        Bộ tài liệu thiết kế STEP 1–9 + 2 báo cáo redesign + TDD chế độ dân tộc chủ nghĩa
v10/v11_removed_*.txt 3 file lưu trữ focus đã xoá (144 KB)
```

---

## 3. Kiến trúc gameplay

**Xương sống = Đại hội Đảng IX–XIV.** Lịch sử chạy bằng *event có ngày cố định*; focus là *lựa chọn của người chơi*; decision là *lớp thực thi nghị quyết*.

- **Hệ trục 9 chiều** (`VIE_ax_size / merit / decent / checks / market / civil / mob / integ / west`), chuẩn hoá mỗi tháng bằng `VIE_ax_normalize`, hiển thị qua `scripted_localisation/VIE_md_axis_bars.txt`, đổ vào `VIE_state_modifier` (dynamic modifier).
- **Balance of Power** `VIE_party_balance`: *Bảo tồn nền tảng* (−) ↔ *Đổi mới sâu rộng* (+), 5 range, khởi tạo ở −0.1 bởi `vie_pol.1`.
- **Biến nhiệm kỳ** `VIE_congress_term` (8→14), tự suy lại mỗi `on_startup` từ cờ scheduler → tương thích save cũ.
- **3 decision category**: `VIE_military_readiness_category` (gate `VIE_modernize_vpa`), `VIE_statebuilding_category` (gate cờ `VIE_ax_initialized`), `VIE_resolution_category` ("Thực hiện Nghị quyết", gate `VIE_party_rule_active` + term > 8).
- **13 event scheduler** (`VIE_event_scheduler` … `_p13`) treo trên `on_monthly`, guard bằng `original_tag = VIE` để vẫn chạy sau nội chiến.
- **Game rule** `VIE_alt_history` điều khiển dải chế độ giả định; `VIE_ai_behavior` → cờ global `VIE_AI_PATH_*` đọc bởi `ai_will_do` và `ai_chance`.

---

## 4. Lịch sử tiến hoá của cây focus (đọc từ comment header)

| Bản | Focus | Thay đổi chính |
|---|---|---|
| v2–v8 | 409 | Tách khối Chính trị, chuẩn hoá MD4, nén layout 824×42 → 322×37, giá xây dựng theo script chuẩn MD |
| **v9** | 409 → **388** | Tách 21 focus *mua sắm vũ khí* ra khỏi cây, chuyển thành event |
| **v10** | 388 → **360** | Gỡ 28 focus nhánh *dân tộc chủ nghĩa* (`VIE_nat_*`) để thiết kế lại theo báo cáo nghiên cứu |
| **v11** | 360 → **256** | Rút gọn tối đa nhánh quân đội: **chỉ giữ root `VIE_modernize_vpa`**, xoá toàn bộ 3 quân chủng Lục quân / Hải quân / PK-KQ |

---

## 5. KIỂM TRA TỰ ĐỘNG — phần SẠCH ✅

| Hạng mục | Kết quả |
|---|---|
| Brace mất cân bằng (mọi file `.txt` live) | **0** |
| Focus parse được | **256** (khớp `verify_all_loc.py`) |
| Trùng toạ độ **tuyệt đối** (đã resolve `relative_position_id`) | **0** |
| `relative_position_id` trỏ tới focus khai báo **sau** (forward-ref → engine báo lỗi) | **0** |
| Chu trình `prerequisite` | **0** |
| Con nằm ngang/trên cha (`y_child ≤ y_parent`) | **0** |
| `prerequisite` / `mutually_exclusive` / anchor treo (trỏ focus không tồn tại) | **0** |
| Scripted effect/trigger gọi mà không định nghĩa (76 lời gọi) | **0** |
| Idea `add_ideas/has_idea/remove_idea` không tồn tại (126 tham chiếu) | **0** |
| Event được fire mà không có `id` | **0** |
| Event `id` trùng lặp · file thiếu `add_namespace` | **0** · **0** |
| Focus thiếu loc name / loc desc | **0 / 0** |
| Key loc dùng làm `tooltip`/`custom_*_tooltip` không tồn tại (31 key) | **0** |
| Game rule option dùng trong `on_startup` không khai báo | **0** |
| `tools/verify_all_loc.py` | **PASS — 2225 key, 0 lỗi** |

→ **Về mặt tham chiếu chéo, repo hiện không có lỗi gãy nào.** Commit v11 đã re-point đúng các gate decision từ focus đã xoá sang `VIE_modernize_vpa`.

---

## 6. NỢ & VẤN ĐỀ TỒN ĐỘNG ⚠️

### 6.1 Nhánh quân sự hiện là **vỏ rỗng** (nghiêm trọng nhất)
Commit `f05cfa1` xoá nội dung nhưng để lại khung chết:

| File | Trạng thái |
|---|---|
| `events/VIE_md_mil.txt` | **29 byte** — chỉ còn `# Events for military branch`. Đã **mất** `add_namespace = vie_mil` |
| `common/ideas/VIE_md_ideas_mil.txt` | **28 byte** — `ideas = { country = { } }` rỗng |
| `common/scripted_effects/VIE_md_mil_gauges.txt` | 2 effect **rỗng** `VIE_mil_gauges_monthly` / `_p2` — **vẫn được gọi mỗi tháng** trong `VIE_md_on_actions.txt` |
| `common/national_focus/VIE_md_focus.txt` | `VIE_modernize_vpa` là **root mồ côi**: 0 con, đứng một mình ở x=266 y=1 |
| `VIE_military_readiness_category` | gate `visible = { has_completed_focus = VIE_modernize_vpa }` → **mở ngay sau 1 focus duy nhất**, 4 decision quân sự trở thành nguồn exp miễn phí gần như không điều kiện |

Commit message nói *"add new military decisions, events, and focus files"* nhưng thực tế events/ideas quân sự bị **rút ruột**, không có file mới thay thế.

### 6.2 24 idea mồ côi (định nghĩa, không còn ai cấp)
`VIE_air_dominance_idea`, `VIE_bastion_idea`, `VIE_blue_water_idea`, `VIE_cam_ranh_idea`, `VIE_corps_restructure_idea`, `VIE_expeditionary_idea`, `VIE_full_spectrum_idea`, `VIE_iron_triangle_idea`, `VIE_pilot_training_idea`, `VIE_reserve_force_idea`, `VIE_sea_control_idea`, `VIE_strategic_air_idea`, `VIE_yugoslav_model_idea`, `VIE_bubble_burst_mild_idea` (đều trong `VIE_md_ideas_p2.txt`);
`VIE_light_carrier_idea`, `VIE_spratly_fleet_idea`, `VIE_modern_navy_2030_idea` (`p3B`); `VIE_modern_air_2030_idea`, `VIE_strategic_air_idea` (`p3C`); `VIE_modern_vpa_2030_idea`, `VIE_regional_intervention_idea` (`p3A`); `VIE_negotiated_transition_idea`, `VIE_fragile_transition_idea` (`p3Q`); `VIE_democratic_consolidation`, `VIE_democratic_transition_idea` (`p2`).

### 6.3 Balance of Power oligarch chết hoàn toàn
`common/bop/VIE_md_bop_p3.txt` (`VIE_oligarch_balance`, 5 range) + 4 effect `VIE_oli_*` trong `VIE_md_effects_p3b.txt` đều gate bằng cờ `VIE_bop_oli_active` — **không còn chỗ nào set cờ này** (TESTING.md xác nhận band oligarch đã bị xoá). Cộng ~20 loc key `VIE_oli_*` chết theo.

### 6.4 43% localisation là key chết
**966 / 2225** key không được bất kỳ file code live nào tham chiếu. Trong đó ~**249 key** thuộc focus quân sự/dân tộc chủ nghĩa đã xoá ở v9–v11 (`VIE_su30mk2_fleet`, `VIE_kilo_submarines`, `VIE_t90_tanks`, `VIE_gepard_frigates`, `VIE_navy_modernization`, `VIE_air_force_modernization`, `VIE_cam_ranh_base`…).

### 6.5 627 key loc trùng lặp giữa thư mục gốc và `replace/`
Cả hai đều tiếng Việt nhưng **bản dịch khác nhau**. Ví dụ `VIE_16_words`:
- `localisation/english/VIE_md_p2_l_english.yml:356` → *"Phương châm 16 Chữ Vàng"*
- `localisation/english/replace/VIE_md_vi_p2_c_l_english.yml:50` → *"Phương châm 16 chữ và tinh thần 4 tốt"*

`replace/` thắng → 627 key ở file gốc là rác cần dọn, và mỗi lần sửa text phải nhớ sửa đúng file.

### 6.6 Layout chưa được nén lại sau v9/v10/v11
| Chỉ số | Giá trị |
|---|---|
| Span tuyệt đối | **x 2 → 308 (306 unit) × y 0 → 27** |
| Mật độ | 256 / 8596 ô = **3.0%** |
| Dải trống > 8 unit | `x 214 → 266` (hổng **52**), `x 266 → 304` (hổng **38**) |
| Cụm bị tách khỏi thân cây | `VIE_modernize_vpa` (x=266) · 8 focus `VIE_sec_*` (x=304–308, y=24–27) |

v9 có "dọn layout" cho band quân sự, nhưng **v10 và v11 chỉ xoá, không re-layout** → để lại hai khoảng trống lớn.

### 6.7 4 root mồ côi (root không có con)
`VIE_modernize_vpa` · `VIE_defence_hotline` · `VIE_code_of_conduct` · `VIE_hcmc_metro`

### 6.8 `VIE_md_focus.txt.bak` (343 KB) nằm trong thư mục game load
Engine bỏ qua vì đuôi `.bak`, nhưng: (a) nó là bản **409 focus cũ** dễ gây nhầm khi grep/sửa; (b) `tools/check_static.py` glob `common/**/*.txt` nên không bắt — nhưng script khác glob `common/**/*` sẽ ra dương tính giả; (c) nên xoá khỏi repo vì git đã giữ lịch sử.

### 6.9 3 file archive ở **gốc mod** (144 KB)
`v10_removed_nationalist_focuses.txt`, `v11_removed_military_all_subbranches.txt`, `v11_removed_military_other_focuses.txt` chứa focus cũ + tham chiếu tới **17 idea và 8 event đã xoá**. Không được game load (không nằm trong `common/`), nhưng gây nhiễu mọi công cụ quét toàn repo. Nên chuyển sang `docs/archive/` hoặc `.txt` → `.md.txt`.

### 6.10 Tooling hardcode đường dẫn Windows
| Script | Đường dẫn cứng |
|---|---|
| `tools/check_static.py` | `MD = 'D:/SteamLibrary/steamapps/workshop/content/394360/2777392649'` |
| `tools/recalc_triangle_layout.py` | `MOD_ROOT = r"d:\HOI4Mods\md_vietnam"` |
| `tools/audit_mod.py`, `tools/unify.py` | hardcode checkout local (TESTING.md ghi rõ dòng 12 / dòng 5) |

Chỉ `tools/verify_all_loc.py` là portable. → Không chạy được CI.

### 6.11 Font: 38 MB, **có lý do chính đáng** nhưng nên tối ưu
Đã kiểm tra `.fnt` (định dạng BMFont text): mỗi font chứa **90 glyph tiếng Việt tiền tổ hợp U+1EA0–U+1EF9** + 192 glyph Latin-1/Ext-A → đây là font **build lại riêng** để hiển thị dấu tiếng Việt, không phải copy vanilla. Đúng và cần thiết.
Nhưng: 26 cặp font chiếm **84% dung lượng repo**. Cân nhắc (a) chỉ giữ những font thật sự override trong `interface/fonts.gfx`, (b) dùng Git LFS.
Lưu ý phụ: `page id=0 file="Arial_14_link_0.dds"` trong `.fnt` **không khớp** tên file thật `Arial_14.dds` (cả 26 font). HOI4 đọc cặp file theo `fontfiles` trong `.gfx` nên không sao, nhưng nên đồng bộ để tránh công cụ ngoài hiểu nhầm.

### 6.12 Việc nhỏ khác
- `descriptor.mod` ghi `name="MD Vietnam (dev)"` nhưng `tools/TESTING.md` hướng dẫn thêm **"Millennium Dawn - Vietnam"** vào playset → tên không khớp, người dùng sẽ không tìm thấy.
- **Không có `LICENSE`**, trong khi `CREDITS.txt` ghi rõ 4 chân dung là dẫn xuất **CC BY-SA** (Le Kha Phieu, Mai Xuan Vinh) → nghĩa vụ share-alike chưa được khai báo ở cấp repo.
- Không có `.gitignore` → `.bak` và file tạm dễ lọt vào commit.
- Không có `README.md` → 19 file `.md` thiết kế không có mục lục/điểm vào.
- `common/bookmarks/blitzkrieg.txt` là **bản copy đầy đủ** file của MD (24 KB) chỉ để chèn 1 khối `"VIE"` — sẽ vỡ mỗi lần MD cập nhật (chính comment trong file đã cảnh báo *"diff it after MD updates"*).

---

### 6.13 🚨 31/41 token `CAT_*` repo dùng **không tồn tại trong Millennium Dawn** (phát hiện 2026-09-30, bước 4 Trục 2)

Đã tải **toàn bộ 24 file** `common/technologies/` của MD (`BBA_aircraft`, `NSB_anti_air`,
`NSB_armor`, `NSB_artillery`, `anti_air`, `anti_tank`, `armor`, `artillery`,
`ballistic_missiles`, `bombers`, `cruise_missiles`, `custom_tech`, `engineering`,
`fixed_wing`, `helicopter_techs`, `industry`, `infantry`, `land_doctrine`,
`missile_defense`, `naval`, `naval_modules`, `non_got_missiles`, `space`,
`special_project_hidden_techs`) → **194 token `CAT_*` hợp lệ**. Danh sách lưu ở
`tools/audit/md_ref/MD_all_CATS.json`.

⚠️ **Phân biệt hai loại `CAT_*`.** Có những token tồn tại trong MD nhưng **chỉ** là
`research_categories` của MIO, **không** phải category của tech folder — dùng chúng
trong `add_tech_bonus` / `research_bonus` của idea sẽ không có tác dụng:

| Token | Trong `common/technologies/`? | Chỉ là MIO category? |
|---|---|---|
| `CAT_self_propelled_artillery` | ❌ **không** | ✅ chỉ có trong `00_generic_defense_companies.txt` |
| `CAT_artillery` | ✅ có (57 lần) | — |
| `CAT_main_battle_tanks` | ✅ có (`armor.txt`, `NSB_armor.txt`) | — |
| `CAT_infantry_fighting_vehicles` | ✅ có (`armor.txt`, `NSB_armor.txt`) | — |
| `CAT_infantry_weapons` | ✅ có (`infantry.txt`) | — |
| `CAT_artillery_ammunition` | ✅ có | — |
| `CAT_anti_air` | ✅ có (5 file) | — |

Bản nháp đầu của mục này ghi `CAT_self_propelled_artillery` là "✅ có thật" — **sai**,
vì JSON đối chiếu lúc đó bị lẫn nguồn. Đã kiểm tra lại từng file và sửa.

Đối chiếu: repo dùng **41** token khác nhau, **31 không có trong MD**:

| Token repo dùng | Token đúng trong MD | Chỗ dùng |
|---|---|---|
| `CAT_inf_wep` | **`CAT_infantry_weapons`** | `VIE_md_organizations.txt:183` + focus |
| `CAT_sp_arty` | **`CAT_self_propelled_artillery`** | `VIE_md_organizations.txt:183` |
| `CAT_sp_r_arty` | *(không có tương đương 1-1; gần nhất `CAT_artillery`)* | `VIE_md_organizations.txt:183` |
| `CAT_at` | **`CAT_anti_tank`** | `VIE_md_organizations.txt:183` |
| `CAT_util` | *(không có; gần nhất `CAT_armored_personnel_carriers`)* | `VIE_md_organizations.txt:183` |
| `CAT_art_ammo` | **`CAT_artillery_ammunition`** | báo cáo Trục 2 mục 2.2 |
| `CAT_inf` | **`CAT_infantry`** | `VIE_md_organizations.txt:183` |
| `CAT_air_eqp`, `CAT_a_uav`, `CAT_as_missiles`, `CAT_cnc`, `CAT_corvette`, `CAT_frigate`, `CAT_green_water_navy`, `CAT_heli`, `CAT_missile`, `CAT_patrolboat`, `CAT_training`, `CAT_trans_heli`, `CAT_trans_plane`, `CAT_naval_radar`, `CAT_naval_sonar`, `CAT_electrical_tech` | cần tra từng cái | `VIE_md_organizations.txt` (4 MIO) |
| `CAT_ai`, `CAT_computing_tech`, `CAT_decryption_tech`, `CAT_encryption_tech`, `CAT_internet_tech`, `CAT_fighter`, `CAT_mr_fighter`, `CAT_fuel_oil`, `CAT_genes`, `CAT_naval_all`, `CAT_satellite`, `CAT_space` | cần tra từng cái | `VIE_md_focus.txt`, `events/VIE_md_p7.txt` |

**Hệ quả:** `research_categories` của cả 4 MIO (`VIE_viettel_manufacturer`,
`VIE_gdt_manufacturer`, `VIE_ba_son_manufacturer`, `VIE_vaeco_manufacturer`) chứa token
không tồn tại → **`research_bonus = 0.06` của MIO có thể không áp dụng cho đúng
category**. Và mọi `add_tech_bonus` trong focus dùng token sai sẽ **không vào đúng
folder nghiên cứu** (engine có thể bỏ qua im lặng hoặc báo lỗi).

**Phạm vi:** đây là **nợ cũ của repo**, không do Trục 1/Trục 2 gây ra. Các file
Trục 2 **chỉ dùng token đã xác minh**: `CAT_artillery`, `CAT_artillery_ammunition`,
`CAT_infantry_weapons`, `CAT_self_propelled_artillery`.

**Việc cần làm (một đợt riêng):** viết script đối chiếu toàn bộ `CAT_*` trong
`common/` với `tools/audit/md_ref/MD_all_CATS.json`, in ra bảng token sai → đúng,
rồi sửa hàng loạt. Ước tính 31 token × ~50 chỗ dùng.

⚠️ **Lưu ý cho người sửa:** `CAT_artillery` và `CAT_artillery_ammunition` **có thật**
(57 và 6 lần trong `artillery.txt`). Đừng "sửa" chúng. Chỉ sửa những token nằm trong
danh sách 31 ở trên.

---

## 7. Đề xuất thứ tự xử lý

**Đợt 1 — dọn rác không rủi ro (không đổi gameplay)**
1. Xoá `common/national_focus/VIE_md_focus.txt.bak`, thêm `.gitignore`.
2. Chuyển 3 file `v1*_removed_*.txt` sang `docs/archive/`.
3. Xoá 24 idea mồ côi + `VIE_oligarch_balance`/`VIE_oli_*` + 4 effect rỗng `VIE_mil_gauges_*` (kèm dòng gọi trong `on_actions`).
4. Xoá ~966 loc key chết; hợp nhất 627 key trùng bằng cách **chọn bản `replace/` làm chuẩn** rồi xoá bản gốc.
5. Đổi `descriptor.mod` `name` cho khớp TESTING.md, thêm `README.md` + `LICENSE` (CC BY-SA cho asset).

**Đợt 2 — layout**
6. Chạy lại nén layout theo đúng quy tắc gap v5 (`≤2` giữ · `3–9→2` · `10–19→4` · `≥20→8`) để lấp hai dải trống x 214–266 và 266–304, kéo cụm `VIE_sec_*` về gần thân cây.

**Đợt 3 — quyết định thiết kế**
7. **Nhánh quân sự**: rebuild theo `VIE_military_branch_design_v3.md` / TDD, hay giữ mô hình "mua sắm = event" của v9 và chỉ để `VIE_modernize_vpa` làm cổng mở decision? Hiện tại đang ở trạng thái lưng chừng.
8. **Nhánh dân tộc chủ nghĩa**: rebuild theo `VIE_nationalism_branch_research_report.md` + `VIE_nationalist_regime_TDD.md` (125 KB, mới sửa ở commit cuối).
9. Siết lại gate `VIE_military_readiness_category` (đang mở sau 1 focus).

**Đợt 4 — hạ tầng**
10. Bỏ đường dẫn cứng trong 4 script tools → đọc từ biến môi trường/đối số, để chạy được `check_static.py` + `audit_mod.py` ngoài máy Windows.

---

*Báo cáo sinh bởi script trong `tools/audit/` — xem `tools/audit/README.md` để biết cách chạy lại.*
