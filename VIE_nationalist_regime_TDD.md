# VIE: Chế độ Dân tộc chủ nghĩa (Alt-history) — Technical Design Document v1

*Ngày 27/9/2026. Tài liệu này chuyển báo cáo "Submod Việt Nam: cây focus cho chế độ dân tộc chủ nghĩa (alt-history), phiên bản 1" thành một đặc tả có thể code ngay. Báo cáo được coi là bản ý tưởng; mọi chỗ tài liệu này khác báo cáo đều có lý do ghi kèm.*

*Nền tham chiếu: Millennium Dawn nhánh `main`, commit `d462627` (clone ngày 27/9/2026); mod này ở commit `3c684f1` (nhánh `claude/inspiring-brown-wilngw`).*

---

## 0. Kết luận (BLUF)

1. **Không làm cây focus riêng nạp bằng `load_focus_tree`.** Làm một **dải chế độ** (regime band) 49 focus nằm trong cây `VIE_md_focus` hiện có, đúng như dải An ninh (slot 7, `VIE_sec_*`) đang làm. Nạp cây riêng sẽ làm người chơi mất 108 focus kinh tế và khoảng 80 focus quân sự/Biển Đông, trong khi nhánh M, D, T của báo cáo trùng phần lớn với chính các focus đó (mục 4, I-03).
2. **Bốn thước đo tự chế được thay bằng một Balance of Power và ba hệ thống MD có sẵn.** Chỉ còn một thứ mới: BoP `VIE_nat_balance` (Kỷ cương ↔ Phong trào) thay cho "cực đoan hóa" và toàn bộ idea phân tầng. "Nhiệt huyết" là **war support**. "Trung thành quân đội" là **`the_military_opinion`** (internal faction của MD). "Cô lập" là **thang trừng phạt 4 bậc của MD**, tư cách ASEAN và opinion modifier. Cả tính năng chỉ cần **một biến lưu trữ mới** (`VIE_nat_leader_id`).
3. **Bốn đường vào được giữ về ý, nhưng gắn vào cơ chế có thật của mod.** Biến "cây gốc" mà báo cáo dùng (`VIE_grievance`, `VIE_crisis_score`, `VIE_east_sea_level`, `VIE_line`, focus H1/H2) **không tồn tại**. Bảng ánh xạ ở mục 3.2. Vào chế độ được **phát hiện** qua `ruling_party ∈ {20, 21, 22}` chứ không chỉ qua event riêng, nên bầu cử MD, nội chiến và đảo chính đều tự đi vào đúng dải.
4. **Đường vào C (thắng cử) chuyển sang giai đoạn 2.** Chuỗi event dân chủ của mod (`vie_alt.12–14`) hiện chưa có nơi gọi.
5. **Tầng lãnh thổ 3 ("Bách Việt") không còn claim, wargoal hay đổi tên.** Còn lại đúng một event nhãn **[FR]**, không có phần thưởng. Quảng Tây (574) và Quảng Đông (534) trong MD là hai state khổng lồ, mỗi tỉnh một state. Claim chúng không phải là "các state ven biển" như báo cáo hình dung.
6. **Không có event MTTH mở.** MD cấm dùng loại này (`MD:.claude/docs/event-reference.md:310`). Mọi xác suất chạy qua bộ lập lịch hàng tháng của mod.
7. **Sửa các lỗi dữ liệu của báo cáo.** `CAM` là Cameroon, Campuchia là `CBD`. Ấn Độ là `RAJ`. `military_industrial_complex` không tồn tại; faction tương ứng là `the_military` hoặc `defense_industry`. VIE đã có claim trên 526, 802, 813 và 816 ngay từ đầu game. VIE chỉ có 7 state lục địa (518–524).
8. **Phải thay cờ.** Nếu chuyển sang ideology `nationalist` mà giữ cosmetic tag hiện tại, MD sẽ hiển thị cờ gắn với tổ chức lịch sử có thật: `VIE_AUTH_S_nationalist.tga` (nền vàng, một sọc đỏ ngang giữa, trùng cờ Đại Việt Quốc dân Đảng) và `VIE_nationalist.tga` (nền vàng ba sọc đỏ, cờ VNCH). Nhận dạng dựa trên xem trực tiếp ảnh trong repo MD. Đặc tả này thêm cosmetic tag riêng.

---

## 1. Phạm vi, nguồn và quy ước

**Nguồn đã đọc trực tiếp:**
- Mã nguồn MD (sparse clone: `common/`, `events/`, `history/`, `localisation/english/`, `.claude/docs/`).
- Toàn bộ `common/`, `events/` và các tài liệu thiết kế của mod này, đặc biệt `VIE_transition_graph_step8.md` và `VIE_nationalism_branch_research_report.md`.

**Ký hiệu:**

| Ký hiệu | Nghĩa |
|---|---|
| ✅ `path:line` | Đã xác minh trong mã nguồn. `MD:` là đường dẫn trong repo MD, `mod:` là đường dẫn trong repo này |
| ❗NEED_VERIFY | Chưa xác minh được bằng đọc mã. Phải thử in-game hoặc đọc thêm trước khi code phần đó |
| **[LS]** | Sự kiện hoặc chính sách có thật |
| **[AH]** | Alternate history: giả định, không có trong lịch sử |
| **[FR]** | Fringe: diễn ngôn bên lề, chưa từng là chính sách nhà nước |
| *(kìm hãm)* | Lựa chọn giảm cực đoan hóa. Mọi tầng đều phải có ít nhất một lựa chọn loại này |
| `BoP` | Giá trị của `VIE_nat_balance`, từ −1 (Kỷ cương) đến +1 (Phong trào) |
| `mil` | `the_military_opinion`, từ 0 đến 100 |
| `WS` | War support |

**Giới hạn nội dung.** Năm giới hạn ở mục 0 của báo cáo được giữ nguyên và nâng thành **quy tắc bắt buộc** cho developer (mục 7.13). Đặc tả này không nới lỏng giới hạn nào.

---

## 2. Bước 1: Phân tích báo cáo

### 2.1 Báo cáo đề xuất gì

| Hạng mục | Số lượng trong báo cáo |
|---|---|
| Focus | 88 focus trong cây riêng: N 10, V1–V3 30, S 8, M 18, D 14, T 8 |
| Event | 37 (31 `vietnam_nat`, 6 news) |
| Decision | 22 (gồm 2 mission) |
| Biến hệ thống mới | 4 thước đo 0–100 và 6 idea phân tầng |
| Dynamic modifier | 1, với 13 khóa |
| Game rule mới | 1 (`VIE_nat_ai_behavior`) |
| Đường vào | 4 (A, B, C, D) |

### 2.2 Điểm mạnh cần giữ

1. Năm giới hạn nội dung: cực đoan hóa là quá trình; không có phần thưởng cho đàn áp; luôn có đường kìm hãm; claim phân tầng theo mức lịch sử; lãnh đạo hư cấu.
2. Gate các biến thể bằng **ruling party thực tế**, không bằng flag (bài học Thái Lan, PR #4362 của MD).
3. Nguyên tắc chi phí của V3 phải lớn hơn lợi ích của nó.
4. Không có focus vũ khí hạt nhân.
5. Đảo chính ngược như một **phanh**, không phải phần thưởng.
6. Có lối ra khỏi chế độ (chuyển giao dân sự).
7. Phân tích điểm yếu của nhánh Đức: focus "chỉ cộng popularity" và phần nội trị mỏng.

### 2.3 Giả định ngầm của báo cáo và kết quả kiểm tra

| # | Giả định | Kết quả |
|---|---|---|
| G1 | Cây gốc có `VIE_grievance`, `VIE_crisis_score`, `VIE_east_sea_level`, `VIE_line`, focus H1b, H1c, H2a | **Sai.** Không biến hay ID nào tồn tại trong mod (đã grep toàn bộ `common/`, `events/`). Mod có các hệ thống tương đương, xem 3.2 |
| G2 | Đảng 20 có thể được tạo và thắng bầu cử | **Chỉ đúng trên con đường dân chủ**, mà con đường này chưa nối dây. VIE bắt đầu với mọi đảng trừ 19 bị cấm (✅ `MD:history/countries/VIE - Vietnam.txt:292,297`) và `elections_allowed = no` |
| G3 | State ID chi tiết theo tỉnh (Lạng Sơn, Khánh Hòa, Hà Nội…) | **Sai.** VIE chỉ có 7 state lục địa lớn (518–524) và 801 |
| G4 | Tag `CAM` là Campuchia, `IND` là Ấn Độ | **Sai.** Campuchia là `CBD` (✅ `MD:history/countries/VIE - Vietnam.txt`, opinion `historic_friends` với `CBD`). Ấn Độ là `RAJ` (✅ cùng file, `influence_array` có `RAJ`) |
| G5 | Có faction `military_industrial_complex` | **Sai.** MD có `the_military` và `defense_industry` (✅ `MD:common/scripted_effects/00_internal_faction_effects.txt`) |
| G6 | Có thể dùng event MTTH | **Trái quy tắc MD** (✅ `MD:.claude/docs/event-reference.md:310`) |
| G7 | Cần 4 thước đo mới | **Không cần.** MD và mod đã có hệ tương đương (mục 5) |
| G8 | `load_focus_tree` là cách hợp lý | **Không phù hợp với mod này** (I-03) |
| G9 | Claim Hoàng Sa, Trường Sa là một bước | **Thừa.** VIE đã có claim trên 526, 802, 813, 816 (✅ `MD:history/states/526-Northern Spratlys.txt`, `802-…`, `813-Paracel.txt`, `816-…`) |
| G10 | Cờ mặc định của MD là trung lập | **Sai.** Xem I-15 |

### 2.4 Vấn đề thiết kế (ngoài tương thích)

1. **Thước đo chồng lấn nhau.** "Nhiệt huyết" và war support cùng đo một thứ: báo cáo cho nhiệt huyết ≥ 70 cộng `war_support_factor`. "Cô lập" và trừng phạt cũng vậy. Người chơi sẽ phải theo dõi 4 thanh riêng cộng với các thanh MD vốn đã có.
2. **Nhiều focus chỉ là cộng biến.** Khoảng 40% focus của báo cáo có phần thưởng chính là `DM:reg.x ±v` cộng một thước đo. Theo checklist của MD (✅ `MD:.claude/docs/content-guidelines.md`, mục Variety), quá 20% focus chỉ cộng biến là cây quá mỏng.
3. **Ngã rẽ khác nhau về độ lớn, không về loại.** Ví dụ V1-07/V1-08: cả hai chủ yếu là `RAD ±`, `ISO ±`.
4. **Trùng lặp với nhánh quân sự hiện có** (danh sách ở I-03).
5. **Quá nhiều tham số ngoại lai.** Ví dụ tỷ lệ sức mạnh ≥ 0,4 so với CHI, MTTH ×0,5 ×2. Đặc tả này giữ lại các hệ số nhưng đưa chúng vào một chỗ duy nhất (mục 7.6).

---

## 3. Bước 2–3: Đối chiếu với HOI4 và Millennium Dawn

### 3.1 Bảng đối chiếu theo 14 hạng mục

| Hạng mục | Báo cáo giả định | Thực tế trong MD và mod | Hệ quả thiết kế |
|---|---|---|---|
| **Focus tree** | Cây riêng 88 focus, `load_focus_tree`, `default = no` | Mod có một cây `VIE_md_focus` với 384 focus. Dải chế độ An ninh (slot 7) nằm ngay trong cây, gate bằng `ruling_party` và trục (✅ `mod:common/national_focus/VIE_md_focus.txt:3436`). MD dùng `load_focus_tree` chủ yếu khi đổi quốc gia hoặc sau nội chiến (✅ `MD:events/Iraq.txt:6044`) | Dải trong cây chính. Có thể đặt dải trong file riêng dưới dạng `shared_focus` (❗NEED_VERIFY N-01) |
| **Parties/ideologies** | Slot 20, 21, 22 | ✅ 24 slot. 20 `Nat_Populism`, 21 `Nat_Fascism`, 22 `Nat_Autocracy`, đều thuộc ideology `nationalist` (`MD:.claude/docs/party-loc-reference.md`). VIE bắt đầu ở 19 (`Neutral_Communism`). MD chỉ có hook tên đảng VIE cho slot 0, 2, 3, 4, 5, 19, 22, 23. **Slot 20 và 21 không có hook** (✅ `MD:common/scripted_localisation/00_MD_politicsview_scripted_localisation.txt`) | Tên đảng 20 và 21 cần hook: NEED_VERIFY N-02 |
| **Đổi chế độ** | Tự viết `VIE_nat_enter_regime` | ✅ Mod có cổng duy nhất `VIE_transition_regime` (`mod:common/scripted_effects/VIE_md_effects.txt:150`). Cổng này gỡ cấm đảng mới, đặt `disable_elections`, gọi `change_ruling_party_effect` (✅ `MD:common/scripted_effects/00_MD_politicsview_scripted_effects.txt:1975`), đổi BoP, và đặt `VIE_regime_changed_recently` 180 ngày | Tái sử dụng. Chỉ mở rộng thêm lệnh gọi init và exit (H1) |
| **Elections** | Đường C thắng cử | ✅ MD chọn đảng có popularity cao nhất (`MD:events/MD_Elections.txt:96`). Chuỗi dân chủ của mod (`vie_alt.12–14`) **không có nơi gọi** | Đường C ở giai đoạn 2. Khi `ruling_party` thành 20 vì bất kỳ lý do gì, cơ chế phát hiện tự đưa VIE vào dải |
| **Decisions** | 22 decision, chi phí bằng "nhiệt huyết" | ✅ `custom_cost_trigger` có tiền lệ (`MD:common/decisions/05_CHI_decisions.txt:197`). Decision có ngẫu nhiên và lặp lại phải có `fixed_random_seed = no` | Chi phí bằng war support qua `custom_cost_trigger` |
| **Missions** | 2 mission | ✅ Có 74 file dùng `days_mission_timeout`. Mẫu ở `MD:.claude/docs/decision-reference.md` | Giữ 2 mission, thêm 1 mission lộ trình dân sự |
| **Events** | MTTH; namespace `vietnam_nat` | ❌ Không được dùng MTTH mở. Mod dùng namespace `vie_*` và bộ lập lịch hàng tháng có cooldown pop-up `VIE_popup_cd` (✅ `mod:common/scripted_effects/VIE_md_effects.txt:232`) | Namespace `vie_nat`, `vie_nat_news`. Xác suất chạy qua `VIE_event_scheduler_nat` |
| **Variables** | 4 thước đo 0–100 | MD: `the_military_opinion` (✅ `MD:common/ideas/AA_law_internal_factions.txt:313`), `protest_strength`. Mod: 9 trục `VIE_ax_*`, `VIE_scs_tension` (0–3) | Chỉ thêm 1 BoP và 1 biến |
| **Scripted effects/triggers** | Nhiều effect và trigger mới | Mod có sẵn `VIE_party_rule_active`, `VIE_scs_escalated_trigger`, `VIE_crisis_count_ge_2`, `VIE_collapse_pole`, `VIE_ai_historical`, `VIE_ai_free` | 8 trigger mới; 8 effect và 6 helper BoP mới (mục 7.5, 7.6) |
| **Dynamic modifiers** | `VIE_nat_regime_modifier` với 13 khóa | Mod đã có `VIE_armed_forces_modifier` (biến `VIE_af_*`) và `VIE_state_modifier` (trục) | **Không tạo dynamic modifier mới.** Quân sự dùng `VIE_af_*`. Chính trị dùng range của BoP và idea |
| **Economy** | Treasury −10 đến −15 mỗi focus | ✅ Treasury tính bằng tỷ USD; VIE bắt đầu với 5 (`MD:history/countries/VIE - Vietnam.txt`). Nhà máy giá 7,5 (`MD:.claude/docs/focus-tree-reference.md`). Bắt buộc có bankruptcy guard. Mod có sẵn các idea sốc: `VIE_fdi_confidence_shock`, `VIE_china_pressure_idea` | Chi phí −2 đến −8. Tái sử dụng idea sốc |
| **Foreign influence** | "Ảnh hưởng ≥ 50%" ⚠10 | ✅ `influence_higher_40/50/60…` gọi trong scope nước bị ảnh hưởng (`MD:common/scripted_triggers/00_influence_scripted_triggers.txt:327,341`). `change_influence_percentage` (`MD:common/scripted_effects/00_influence_scripted_effects.txt:1054`) | Dùng trực tiếp |
| **Diplomacy** | Faction mới; gỡ ASEAN ⚠9; cấm vận ⚠ | ✅ `create_faction_from_template` với `faction_template_generic_regional_security` (`MD:common/factions/templates/01_generic_archetypes.txt:198`). ✅ ASEAN là idea `ASEAN_Member`; `on_remove` tự gỡ khỏi `global.ASEAN_Member` (`MD:common/ideas/asean.txt:3`), tiền lệ `BRM_leave_asean`. ✅ Thang trừng phạt `increase_sanctions`/`decrease_sanctions` (`MD:common/scripted_effects/00_sanctions_scripted_effects.txt:2,30`) | Dùng trực tiếp. Không tự thêm `unsc_arms_embargo` vì idea đó thuộc hệ thống UNSC |
| **Civil war** | `MD_start_scaled_protest_civil_war` | ✅ Có (`MD:common/scripted_effects/00_protests_effects.txt:435`), nhưng mod đã có hệ sụp đổ riêng: `VIE_collapse_check`, `VIE_col_start_civil_war` với phe nổi dậy 22, 20, 13, 5 và state cụ thể (✅ `mod:common/scripted_effects/VIE_md_effects_p3.txt:18,42,158`). `VIE_col_pick_rebel` **chưa bao giờ chọn 20** | Đường D đi qua hệ sụp đổ của mod (hook H3) |
| **AI** | Game rule mới `VIE_nat_ai_behavior` | ✅ Mod có `VIE_alt_history` (historical/plausible/free) và `VIE_ai_behavior` với cờ `VIE_AI_PATH_*` (`mod:common/game_rules/VIE_md_rules.txt:2,28`). Cờ `VIE_AI_PATH_NATIONALIST` **đã được focus đọc nhưng chưa bao giờ được đặt** | Thêm 2 option vào `VIE_ai_behavior`, không tạo rule mới |

### 3.2 Ánh xạ biến "cây gốc" của báo cáo sang mod thật

| Báo cáo | Cơ chế thật trong mod | Ghi chú |
|---|---|---|
| `VIE_east_sea_level` (0–3) | `VIE_scs_tension` (0–3), `VIE_scs_escalated_trigger` (≥ 2), `VIE_hd981_response` (1 kiềm chế, 2 cứng rắn, 3 quốc tế hóa) | ✅ `mod:common/scripted_effects/VIE_md_effects.txt:29`; `mod:events/VIE_md_scs.txt` |
| `VIE_east_sea_level = 3` (xung đột vũ trang) | `has_war_with = CHI` | Không cần mức 3 riêng |
| `VIE_crisis_score ≥ 85` | `VIE_crisis_count_ge_2` + `has_stability < 0.20` + `VIE_collapse_pole` (tức `VIE_collapse_check`) | ✅ `mod:common/scripted_triggers/VIE_md_triggers_p3.txt:13,33` |
| `VIE_grievance` | Trục `VIE_ax_mob_norm` và `VIE_ax_checks_norm` cộng các idea `VIE_public_anger`, `VIE_civil_unrest_idea` | Ngưỡng trục theo `VIE_transition_graph_step8.md:111–117` |
| H2a `VIE_loosen_a_no` | Cửa D4 `vie_alt.1`, option b "cứng rắn" | ✅ `mod:events/VIE_md_alt.txt:11`. Hiện option b **không đặt flag nào**, nên cần hook H2 |
| `VIE_line ≠ 3` | Không cần | — |
| H1b/H1c (bầu cử cạnh tranh) | `vie_alt.12–14`, flag `VIE_democracy_path_open`, `VIE_democracy_elected` | Chưa nối dây; xem I-06 |
| event vietnam.74 (cải cách H1 đình trệ) | Không có | Đường B đi qua `vie_col.1` |
| "Bốn không" | Idea `VIE_four_nos` / `VIE_non_alignment_policy`; `VIE_transition_regime` gỡ chúng khi vào slot 22 hoặc 0 | ✅ `mod:common/scripted_effects/VIE_md_effects.txt:150` |
| Lãnh đạo hư cấu | `set_leader_VIE` (bản ghi đè của mod) tạo lãnh đạo hư cấu cho mọi slot thay thế. Slot 22 là "Gen. Trinh Van Hieu". **Slot 20 và 21 chưa có** | ✅ `mod:common/scripted_effects/VIE_political_leaders.txt:10,178` |

---

## 4. Bước 4: Không tương thích hoặc quá phức tạp

Mức độ: **Chặn** (không code được như viết), **Cao** (code được nhưng sai hoặc hỏng gameplay), **TB** (thừa hoặc khó bảo trì), **Thấp** (sửa nhỏ).

| Mã | Thành phần của báo cáo | Vấn đề | Mức |
|---|---|---|---|
| I-01 | Mọi điều kiện đường vào | Dựa trên biến không tồn tại (G1) | Chặn |
| I-02 | Event MTTH (vietnam_nat.1, .30, .31, .42) | Trái quy tắc MD | Chặn |
| I-03 | Cây riêng qua `load_focus_tree` | (a) Người chơi mất 108 focus kinh tế và nhánh quân sự; `keep_completed = yes` chỉ giữ các ID có mặt trong cây mới. (b) Lối ra V2 phải nạp lại cây gốc; focus đã làm sẽ mất nếu `keep_completed = no`. (c) Nhánh M trùng các focus đã có: `VIE_kilo_submarines`, `VIE_bastion_p_coastal_defence`, `VIE_integrated_air_defense`, `VIE_uav_program`, `VIE_fighter_replacement`, `VIE_z_factories`, `VIE_maritime_militia`, `VIE_spratly_fortification`, `VIE_militia_law`, `VIE_mechanization`. Nhánh D trùng `VIE_russian_arms_deals`, `VIE_india_partnership`, `VIE_cam_ranh_base`, `VIE_special_relations_laos`, `VIE_indochina_solidarity`. T02 trùng `VIE_paracel_ultimatum` (claim 813 + wargoal, ✅ `mod:…/VIE_md_focus.txt:1021`). (d) MD yêu cầu cây quốc gia ≥ 114 focus (✅ `MD:.claude/docs/content-guidelines.md:11`); cây riêng 88 focus mỏng hơn cây generic | Cao |
| I-04 | `VIE_nat_fervor` | Trùng war support | TB |
| I-05 | `VIE_nat_isolation` và 3 idea cô lập | Trùng thang trừng phạt MD, ASEAN, opinion | TB |
| I-06 | Đường C (thắng cử) | Con đường dân chủ của mod chưa nối dây. Đảng 20 bị cấm từ đầu game | Cao |
| I-07 | T01 `CLAIM` Hoàng Sa, Trường Sa | Claim đã có sẵn | Thấp |
| I-08 | Công sự ở "Lạng Sơn, Cao Bằng…", phòng không ở "Hà Nội, Hải Phòng, TP HCM" | Không có các state đó. Biên giới phía Bắc là 523 và 524; Hà Nội và Hải Phòng nằm trong 522; TP HCM nằm trong 519 | Thấp |
| I-09 | Tầng 3: claim các state "ven biển" Quảng Tây, Quảng Đông; decision đổi tên; quản lý quân sự | Mỗi tỉnh là một state khổng lồ (534 Quảng Đông gồm 29 province). Chiến tranh chiếm Quảng Đông không có cơ sở và làm nội dung trượt khỏi mức "giả định có kiểm soát" | Cao |
| I-10 | `CAM`, `IND`, `military_industrial_complex` | Sai tag hoặc faction (G4, G5) | Chặn |
| I-11 | Dynamic modifier 13 khóa | Làm cây thành danh sách bonus. Trùng `VIE_armed_forces_modifier` | TB |
| I-12 | `unsc_arms_embargo` do event thêm vào | Idea thuộc hệ thống UNSC (`MD:common/scripted_effects/01_international_systems_effects.txt:1473`); tự thêm sẽ lệch logic gỡ của UNSC | TB |
| I-13 | Game rule mới `VIE_nat_ai_behavior` | Trùng `VIE_ai_behavior` và `VIE_alt_history` | TB |
| I-14 | `ban_party_scripted_call` với "index của đảng cũ" | VIE đã `set_partyall_banned`; chỉ đảng cầm quyền không bị cấm | Thấp |
| I-15 | "Cờ nguyên bản" chỉ là ghi chú | Không đổi cosmetic tag thì MD tự hiện cờ Đại Việt hoặc VNCH (✅ `MD:gfx/flags/VIE_AUTH_S_nationalist.tga`, `VIE_nationalist.tga`). Biến thể thứ ba `VIE_AUTH_SS_nationalist.tga` (sao trắng trong vòng xanh trên nền đỏ–vàng) chưa nhận dạng được nguồn gốc | Cao |
| I-16 | Đổi biến thể bằng `change_ruling_party_effect` trực tiếp | Bỏ qua `VIE_transition_regime`, nên BoP và các flag của mod bị lệch | Cao |
| I-17 | Event .9 chọn nguyên mẫu lãnh đạo bằng `create_country_leader` | MD gọi `set_leader` mỗi lần đổi ruling party; override `set_leader_VIE` giết và tạo lại lãnh đạo, nên lựa chọn phải được lưu vào biến | Cao |
| I-18 | `vietnam_nat.41` quay về "cây gốc với cấu hình nhiều đảng từ H1" | Không có cấu hình đó | Cao |
| I-19 | Bạo lực bài ngoại: idea mới `VIE_nat_investor_flight` | Mod đã có `VIE_fdi_confidence_shock`, và idea này đã nằm trong `VIE_crisis_count_ge_2`, nên nó tự nối với hệ sụp đổ | Thấp |
| I-20 | Nhiều treasury −10/−15 | Quá lớn so với ngân sách VIE trong MD | TB |
| I-21 | V1, V2, V3 mỗi cột 10 focus | Đi theo kiểu số lượng. Mỗi cột chỉ cần một cơ chế riêng và một ngã rẽ thật | TB |
| I-22 | `VIE_col_pick_rebel` khi chính phủ đã là `nationalist` | Nhánh `else` chọn phe 22 cũng `nationalist`, tức nội chiến cùng ideology (❗NEED_VERIFY N-05) | Cao |

---

## 5. Bước 5: Cơ chế thay thế

| Thành phần báo cáo | Thay bằng | Mục đích gameplay |
|---|---|---|
| Cây riêng + `load_focus_tree` | Dải chế độ trong `VIE_md_focus`, gốc là `VIE_nat_salvation_government` | Giữ toàn bộ cây kinh tế và quân sự; dải chỉ chứa phần mà chế độ mới có |
| `VIE_nat_radicalization` + idea phân tầng | BoP `VIE_nat_balance`: trái `VIE_nat_order_side` (Kỷ cương), phải `VIE_nat_movement_side` (Phong trào) | Có thanh UI sẵn; range của BoP mang modifier nên không cần idea phân tầng; ngưỡng đọc bằng `power_balance_value` |
| `VIE_nat_fervor` | War support | Nhiệt huyết là thứ người chơi **tiêu** được (decision có `custom_cost_trigger`) và thấy được trên UI gốc |
| `VIE_nat_army_loyalty` | `the_military_opinion` + mission đảo chính | MD đã tự áp modifier theo opinion (✅ `MD:…/00_internal_faction_effects.txt:894`) và nhân đôi opinion dương cho slot 21 và 22 (✅ `:1001`). Mod đã tự đổi `farmers` thành `the_military` khi `VIE_ax_mob_norm > 7` (✅ `mod:common/scripted_effects/VIE_md_effects_axis.txt:179`) |
| `VIE_nat_isolation` + 3 idea | Thang trừng phạt MD (`Reduced_Western_Sanctions` → `Western_Sanctions` → `international_sanctions` → `Massive_International_Sanctions`); `ASEAN_Member`; opinion modifier; `trade_opinion_factor` và `receiving_investment_cost_modifier` trong range BoP | Hậu quả hiện ra bằng các idea mà người chơi MD đã quen |
| `VIE_nat_enter_regime` | `VIE_transition_regime` (có sẵn) + `VIE_nat_regime_init` | Một cổng duy nhất cho mọi thay đổi chế độ |
| Đường vào bằng event riêng | Phát hiện qua `VIE_nat_regime_active` trong bộ lập lịch | Bầu cử, nội chiến, đảo chính đều vào dải mà không cần sửa MD |
| MTTH | `random = { chance = … }` trong `VIE_event_scheduler_nat` | Theo quy tắc MD; có cooldown `VIE_popup_cd` của mod |
| Dynamic modifier 13 khóa | Idea swap (charter, capstone) + `VIE_af_*` | Mỗi focus có phần thưởng khác **loại** |
| `VIE_nat_investor_flight` | `VIE_fdi_confidence_shock` (timed) | Tự nối với hệ sụp đổ |
| `unsc_arms_embargo` | `international_sanctions` (đã chặn thị trường vũ khí qua `can_access_market = no`) | Không đụng hệ UNSC |
| Game rule mới | Option mới trong `VIE_ai_behavior` + ngưỡng nới trong chế độ `free` của `VIE_alt_history` | Một chỗ cấu hình |
| Tầng 3: claim, wargoal, đổi tên | Event [FR] `vie_nat.25` không có phần thưởng | Giữ hiện tượng bên lề như một cám dỗ có giá, không vẽ bản đồ |
| T02 chiến dịch Hoàng Sa | Focus có sẵn `VIE_paracel_ultimatum` | Không trùng |
| Nhánh M 18 focus | 4 focus riêng của chế độ; capstone đọc các focus quân sự đã có | Dải thưởng cho nhánh quân sự hiện có, không nhân đôi nó |
| Nhánh D 14 focus | 6 focus: ngã ba chỗ dựa + khối lục địa + rời ASEAN | Giữ quyết định chiến lược, bỏ phần trùng |
| Lối ra "cây gốc nhiều đảng" | Hai lối ra có thật: Đảng phục hồi (slot 19, lãnh đạo hư cấu `VIE_create_leader_restored_party`) hoặc chuyển tiếp (slot 13 + `VIE_democracy_path_open`, như `vie_col.6.a`) | Dùng trạng thái mod đã hỗ trợ |

---

## 6. Bước 6: Gameplay loop thiết kế lại

### 6.1 Ý tưởng cốt lõi

*Người chơi điều hành một chế độ sinh ra từ khủng hoảng chủ quyền. Nguồn năng lượng giữ chế độ tồn tại, tức phong trào quần chúng, cũng chính là thứ đẩy nó về phía một cuộc chiến gần như không thể thắng và một sự cô lập bóp nghẹt kinh tế. Kỹ năng là "cưỡi hổ": tiêu nhiệt huyết để làm việc, giữ quân đội đứng về phía mình, và biết lúc nào phải dừng.* **[AH]**

### 6.2 Vòng lặp chính

```
      ┌──────────── Sự kiện Biển Đông, chiến thắng, mít tinh ────────────┐
      ▼                                                                   │
  WAR SUPPORT (nhiệt huyết) ──tiêu──▶ decision: dân quân, trái phiếu,     │
      │                                huy động, nhiệm vụ                │
      │ WS > 0,6 kéo sang phải                                           │
      ▼                                                                   │
  BoP VIE_nat_balance  ◀── focus "kìm hãm" / decision kìm hãm kéo sang trái
      │
      ├─ BoP ≥ 0,2 : range Phong trào (WS+, lính+, đầu tư−, thương mại−);
      │              có thể nổ event bạo lực bài ngoại (vie_nat.30)
      ├─ BoP ≥ 0,6 : range Cuồng nhiệt; Bước ngoặt (vie_nat.20) → slot 21?
      ├─ BoP ≥ 0,8 : (chỉ slot 21) event [FR] "Bách Việt"; trừng phạt leo thang
      └─ BoP > 0,85: thành một "cực" của hệ sụp đổ → có thể nội chiến
                                  │
  the_military_opinion ◀──────────┘  thanh trừng, cực đoan, thua trận làm giảm
      │ < 35 → mission đảo chính (180 ngày) → thất bại: quân đội nắm quyền (slot 22), BoP −0,3
      ▼
  ĐẦU RA: thang trừng phạt · ASEAN · opinion · FDI shock · wargoal của CHI
```

### 6.3 Ba trục căng thẳng

| Trục | Cơ chế | Người chơi muốn | Cái giá |
|---|---|---|---|
| Nhiệt huyết | War support | Cao, để tiêu vào decision và để chiến tranh | Cao kéo BoP sang Phong trào |
| Kỷ cương ↔ Phong trào | BoP `VIE_nat_balance` | Vùng giữa hoặc hơi phải | Trái quá: mất tính chính danh huy động (PP, WS giảm). Phải quá: cô lập, bạo lực, sụp đổ |
| Quân đội | `the_military_opinion` | ≥ 50 | Dưới 35: đảo chính. Slot 20 tự giảm mỗi tháng |

### 6.4 Nhịp độ một ván

| Giai đoạn | Thời gian | Người chơi làm gì | Áp lực |
|---|---|---|---|
| Củng cố | 0–18 tháng | Trunk N; mission `VIE_nat_consolidation_deadline` (540 ngày) | Thế giới phản ứng (trừng phạt bậc 1 nếu vào không hợp hiến); tháo chạy vốn |
| Định hình | 6–36 tháng | Cột biến thể V1, V2 hoặc V3; nhánh S | Ngã rẽ bầu cử (V1) hoặc lộ trình dân sự (V2); quân đội |
| Phóng chiếu | 18 tháng trở đi | Nhánh D (chọn chỗ dựa), M, T | Bước ngoặt; bạo lực; CHI; ASEAN |
| Kết cục | Bất kỳ lúc nào | Một trong các lối ra (6.5) | — |

### 6.5 Lối ra khỏi chế độ

| Lối ra | Điều kiện | Kết quả |
|---|---|---|
| Chuyển giao dân sự | V2 chọn "Hứa trao quyền dân sự", mission lộ trình thành công, event `vie_nat.41` | Slot 19 (Đảng phục hồi) hoặc slot 13 + `VIE_democracy_path_open` |
| Thua bầu cử | V1 giữ bầu cử có kiểm soát; bầu cử MD chọn đảng khác | Phát hiện rời chế độ → `VIE_nat_regime_exit` |
| Đảo chính ngược | Mission đảo chính thất bại | 20 hoặc 21 → 22; nếu đã là 22: đổi lãnh đạo |
| Sụp đổ | `VIE_collapse_check` với cực BoP > 0,85 | Nội chiến; phe nổi dậy là 13 (hook H3) |
| Thua chiến tranh | `vie_nat.53` | BoP về trái mạnh; có thể dẫn tới đảo chính |

### 6.6 Mục tiêu cân bằng (dùng khi playtest)

| Chỉ số | Người chơi "kìm hãm" sau 3 năm | Người chơi "cưỡi hổ" sau 3 năm | Người chơi cực đoan (slot 21) |
|---|---|---|---|
| BoP | −0,3 đến 0 | 0,1 đến 0,4 | ≥ 0,6 |
| Bậc trừng phạt | 0 | 0–1 | 2–3 |
| ASEAN | Còn | Còn | Thường đã rời |
| Tăng trưởng GDP so với lịch sử | −0,5 đến −1 điểm % | −1 đến −2 | −3 trở lên |
| Sức mạnh quân sự | + nhẹ | + vừa | + mạnh |

Nguyên tắc: **slot 21 mạnh nhất về quân sự và yếu nhất về kinh tế và ngoại giao.** Chiến tranh với CHI không được buff để bù (giữ nguyên nguyên tắc của báo cáo, mục 6.8).

---

## 7. Bước 7: Specification

### 7.1 Kiến trúc và file

**File mới.** Tất cả dùng tiền tố `VIE_md_*_nat` theo quy ước tên file của mod.

| File | Nội dung |
|---|---|
| `common/national_focus/VIE_md_focus_nat.txt` | 49 focus của dải, viết dưới dạng `shared_focus`. Cây `VIE_md_focus` thêm đúng một dòng `shared_focus = VIE_nat_salvation_government`. Nếu N-01 thất bại, chuyển sang viết trực tiếp trong `VIE_md_focus.txt` |
| `common/bop/VIE_md_bop_nat.txt` | `VIE_nat_balance` |
| `common/ideas/VIE_md_ideas_nat.txt` | 14 idea (mục 7.4) |
| `common/scripted_triggers/VIE_md_triggers_nat.txt` | 8 trigger (mục 7.5) |
| `common/scripted_effects/VIE_md_effects_nat.txt` | 8 effect + 6 helper BoP (mục 7.3, 7.6) |
| `common/decisions/VIE_md_decisions_nat.txt` | 14 decision + 3 mission (mục 7.10) |
| `common/decisions/categories/VIE_md_categories_nat.txt` | 2 category |
| `events/VIE_md_nat.txt` | `add_namespace = vie_nat` và `add_namespace = vie_nat_news` |
| `localisation/english/VIE_md_nat_l_english.yml` | Tiếng Anh (bắt buộc, UTF-8 BOM) |
| `localisation/english/replace/VIE_md_vi_nat_l_english.yml` | Tiếng Việt, theo đúng cách mod đang làm với `replace/` |
| `gfx/flags/VIE_NAT_nationalist.tga`, `VIE_NATR_nationalist.tga` + `medium/`, `small/` | Cờ (mục 7.13) |

**File hiện có phải sửa.** Mỗi hook là một thay đổi nhỏ, có chỗ đặt cụ thể.

| Hook | File | Thay đổi |
|---|---|---|
| H1 | `mod:common/scripted_effects/VIE_md_effects.txt:150` (`VIE_transition_regime`) | (a) Gỡ `VIE_four_nos`/`VIE_non_alignment_policy` cả khi vào 20 và 21 (hiện chỉ 22 và 0). (b) Trước `change_ruling_party_effect`: lưu slot cũ vào temp `VIE_nat_prev_party`. (c) Sau đó: vào nhóm 20/21/22 từ ngoài nhóm → `VIE_nat_regime_init`; rời nhóm → `VIE_nat_regime_exit`; đổi trong nhóm → `VIE_nat_on_variant_change` |
| H2 | `mod:events/VIE_md_alt.txt:11` (`vie_alt.1`) | Option b thêm `set_country_flag = VIE_d4_hard_line`. Thêm option c "Để đường phố dẫn dắt" (mục 7.7, đường D) |
| H3 | `mod:common/scripted_effects/VIE_md_effects_p3.txt:18` (`VIE_col_pick_rebel`) | Nhánh đầu tiên: nếu `VIE_nat_regime_active` → phe nổi dậy 13. Thêm nhánh: nếu có `VIE_d4_street` và `VIE_ax_mob_norm > 6` → phe nổi dậy 20 |
| H4 | `mod:events/VIE_md_int_col.txt` (`vie_col.1`) | Thêm option c "Ủy ban Cứu quốc" (đường B) |
| H5 | `mod:common/scripted_triggers/VIE_md_triggers_p3.txt:33` (`VIE_collapse_pole`) | Thêm vào `OR`: `has_country_flag = VIE_bop_nat_active` và `power_balance_value = { id = VIE_nat_balance value > 0.85 }` |
| H6 | `mod:common/scripted_effects/VIE_political_leaders.txt:10` (`set_leader_VIE`) | Thêm reset `Nat_Populism_leader`, `Nat_Fascism_leader`. Nhánh 20, 21, 22 gọi `VIE_nat_create_leader` (đọc `VIE_nat_leader_id`) thay cho lãnh đạo cố định |
| H7 | `mod:common/on_actions/VIE_md_on_actions.txt:5` | Thêm `VIE_event_scheduler_nat = yes` vào danh sách scheduler |
| H8 | `mod:common/game_rules/VIE_md_rules.txt:28` + `VIE_md_on_actions_startup.txt` | Thêm option `VIE_NATIONALIST` và `VIE_NATIONALIST_RADICAL` (mục 7.11) |
| H9 | `mod:common/opinion_modifiers/VIE_md_opinion_modifiers.txt` | Thêm 5 opinion modifier (mục 7.4.3) |

### 7.2 Biến và flag

Theo quy tắc MD: không tạo flag lặp lại trạng thái có thể truy vấn (✅ `MD:AGENTS.md`, mục KISS). Vì vậy "đang ở trong chế độ" là trigger đọc `ruling_party`, không phải flag, và "đã làm focus S5" là `has_completed_focus`.

**Biến lưu trữ mới (1):**

| Biến | Scope | Giá trị | Ghi bởi | Đọc bởi | Mục đích |
|---|---|---|---|---|---|
| `VIE_nat_leader_id` | VIE | 1–6 | `vie_nat.9`, `vie_nat.40` | `VIE_nat_create_leader` | Nhớ nguyên mẫu lãnh đạo, vì `set_leader_VIE` tạo lại lãnh đạo mỗi lần đổi ruling party (I-17). 1 Tướng lĩnh, 2 Nhà hùng biện, 3 Kỹ trị; 4–6 là thế hệ sau đảo chính |

**Biến tạm (temp):**

| Biến | Ghi bởi | Ý nghĩa |
|---|---|---|
| `VIE_nat_route` | Nơi gọi `VIE_transition_regime` | 1 A, 2 B, 3 C, 4 D, 0 không rõ (effect init tự suy ra) |
| `VIE_nat_prev_party` | H1 | Slot trước khi đổi |
| `VIE_nat_roll` | `VIE_nat_monthly` | Xác suất tính trong tháng |

**Flag (chỉ trạng thái không truy vấn được hoặc chuyển tiếp lịch sử):**

| Flag | Loại | Đặt bởi | Ý nghĩa |
|---|---|---|---|
| `VIE_nat_regime_init` | country | `VIE_nat_regime_init` | Đã khởi tạo; phát hiện "rời chế độ" khi flag còn mà `ruling_party` đã khác |
| `VIE_bop_nat_active` | country | init/exit | Theo mẫu `VIE_bop_active` của mod: guard cho mọi lệnh ghi BoP |
| `VIE_d4_hard_line` | country | `vie_alt.1.b` (H2) | Đã chọn đường cứng rắn sau HD-981 |
| `VIE_d4_street` | country | `vie_alt.1.c` (H2) | Đã để đường phố dẫn dắt |
| `VIE_nat_plenum_cd` | country, 730 ngày | `vie_nat.1.a` | Cooldown đường A |
| `VIE_nat_turning_point_done` | country | `vie_nat.20` | Bước ngoặt chỉ xảy ra một lần |
| `VIE_nat_elite_split` | country | `vie_nat.12.b` | Một phần tinh hoa đã ly khai (điều kiện cấu trúc của slot 21) |
| `VIE_nat_violence_cd` | country, 730 ngày | `vie_nat.30` | Cooldown event bạo lực |
| `VIE_nat_fringe_done` | country | `vie_nat.25` | Event [FR] chỉ một lần |
| `VIE_nat_war_with_chi` | country | `VIE_nat_monthly` | Đang có chiến tranh với CHI; dùng để nhận ra lúc chiến tranh kết thúc |
| `VIE_nat_paracels_held` | country | `VIE_nat_monthly` | Đã báo tin chiếm 813 |
| `VIE_nat_party_founded` | country | `vie_nat.4` (giai đoạn 2) | Đảng 20 đã ra đời trên con đường dân chủ |

**Tái sử dụng (không tạo mới):** `ruling_party`, `the_military_opinion`, `VIE_scs_tension`, `VIE_hd981_response`, `VIE_ax_*_norm`, `VIE_af_*`, `VIE_popup_cd`, `VIE_regime_changed_recently`, `VIE_post_collapse`, `VIE_democracy_path_open`, `VIE_democracy_elected`.

### 7.3 Balance of Power `VIE_nat_balance`

Theo mẫu `mod:common/bop/VIE_md_bop.txt` và `VIE_md_bop_p3.txt`. Chỉ tồn tại khi `ruling_party ∈ {20, 21, 22}`.

- Trái (âm): `VIE_nat_order_side`, "Kỷ cương Nhà nước". Biểu tượng: tái sử dụng một `GFX_idea_*` có sẵn (❗N-08).
- Phải (dương): `VIE_nat_movement_side`, "Phong trào".

| Range | Khoảng | Modifier | Ý nghĩa gameplay |
|---|---|---|---|
| `VIE_nat_technocratic_range` | −1 đến −0,6 | `stability_factor +0.05`, `war_support_factor −0.08`, `conscription_factor −0.10`, `political_power_factor −0.10` | Chế độ đã giải huy động, mất tính chính danh quần chúng |
| `VIE_nat_order_range` | −0,6 đến −0,2 | `stability_factor +0.04`, `war_support_factor −0.03`, `drift_defence_factor 0.05`, `trade_opinion_factor 0.02` | Kỷ cương, dễ làm ăn |
| `VIE_nat_mid_range` | −0,2 đến 0,2 | `stability_factor +0.02`, `political_power_factor +0.05` | Vùng "cưỡi hổ" |
| `VIE_nat_movement_range` | 0,2 đến 0,6 | `war_support_factor +0.05`, `conscription_factor +0.05`, `stability_factor −0.02`, `trade_opinion_factor −0.10`, `receiving_investment_cost_modifier 0.10` | Phong trào dâng cao, vốn ngoại e ngại |
| `VIE_nat_fervor_range` | 0,6 đến 1 | `war_support_factor +0.10`, `conscription_factor +0.10`, `political_power_factor +0.10`, `stability_factor −0.05`, `trade_opinion_factor −0.25`, `receiving_investment_cost_modifier 0.25`, `country_productivity_growth_modifier −0.02` | Cuồng nhiệt: mạnh cho chiến tranh, đắt cho kinh tế |

**Giá trị khởi đầu theo đường vào:**

| Đường | Slot | BoP ban đầu | `mil` ban đầu |
|---|---|---|---|
| A (Hội nghị bất thường) | 22 | −0,1 | 70 |
| B (Ủy ban Cứu quốc) | 22 | −0,3 | 65 |
| B, trao cho đường phố | 20 | +0,2 | 45 |
| C (thắng cử; giai đoạn 2) | 20 | +0,1 | 50 |
| D (thắng nội chiến) | 20 | +0,3 | 45 |
| Không rõ (phát hiện) | 20/21/22 | 0 | giữ nguyên nếu đã có `the_military` |

**Trôi hàng tháng** (trong `VIE_nat_monthly`; cộng dồn, BoP tự kẹp trong [−1, 1]):

| Điều kiện | Thay đổi |
|---|---|
| `has_war_support > 0.6` | +0,02 |
| `has_war_support < 0.3` | −0,02 |
| Slot 21 | +0,01 |
| Có idea `VIE_nat_sovereignty_secured` | −0,01 |
| Đang có chiến tranh với CHI | +0,01 |

**Helper** (theo mẫu `VIE_bop_*` của mod, có guard `VIE_bop_nat_active`): `VIE_nat_bop_order_small/medium/large` = −0,05/−0,10/−0,20; `VIE_nat_bop_movement_small/medium/large` = +0,05/+0,10/+0,20. Mọi thay đổi BoP trong bảng dưới đây ghi theo ký hiệu `BoP ±n`.

### 7.4 Idea và modifier

#### 7.4.1 Idea mới (14)

Mọi idea có `allowed = { always = no }`, `allowed_civil_war = { always = no }`, `cancel_if_invalid = no` như các idea khác của mod. Mô tả phải giải thích cách gỡ (✅ `MD:.claude/docs/content-guidelines.md`, Visual).

| Idea | Loại | Modifier | Nguồn → gỡ |
|---|---|---|---|
| `VIE_nat_emergency_rule` | timed 365 ngày | `stability_factor 0.05`, `political_power_factor 0.10`, `receiving_investment_cost_modifier 0.10` | N1 → hết hạn hoặc bị thay bằng charter ở N8 |
| `VIE_nat_charter_populist` | charter | `stability_factor 0.03`, `political_power_factor 0.05`, `war_support_factor 0.03` | N8 khi slot 20 |
| `VIE_nat_charter_guardian` | charter | `stability_factor 0.05`, `army_org_factor 0.02`, `political_power_factor −0.03` | N8 khi slot 22 |
| `VIE_nat_charter_totalist` | charter | `political_power_factor 0.10`, `war_support_factor 0.05`, `stability_factor −0.03` | N8 khi slot 21 |
| `VIE_nat_self_reliance` | vĩnh viễn trong chế độ | `production_speed_arms_factory_factor 0.05`, `receiving_investment_cost_modifier 0.10`, `trade_opinion_factor −0.05` | N7 |
| `VIE_nat_peoples_nationalism` | capstone V1 | `stability_factor 0.05`, `political_power_factor 0.05`, `war_support_factor 0.05` | V1-6 |
| `VIE_nat_fortress_state` | capstone V2 | `army_org_factor 0.05`, `production_speed_arms_factory_factor 0.05`, `stability_factor 0.03` | V2-6 |
| `VIE_nat_totalist_state` | capstone V3 | `war_support_factor 0.15`, `conscription_factor 0.10`, `stability_factor −0.05`, `receiving_investment_cost_modifier 0.20` | V3-6 |
| `VIE_nat_armed_neutrality` | ngoại giao | `foreign_influence_defense_modifier 0.15`, `army_org_factor 0.03` | D4 |
| `VIE_nat_sovereignty_secured` | kìm hãm | `stability_factor 0.05`, BoP trôi −0,01/tháng (mục 7.3) | T1 |
| `VIE_nat_conventional_deterrent` | quân sự | `war_support_factor 0.05`, `army_org_factor 0.03` | M4 |
| `VIE_nat_militia_mobilized` | timed 180 ngày | `conscription_factor 0.05`, `production_speed_buildings_factor −0.05` | decision `VIE_nat_mobilize_militia` |
| `VIE_nat_capital_controls` | timed 365 ngày | `tax_gain_multiplier_modifier −0.02`, `receiving_investment_cost_modifier 0.05` | `vie_nat.11.a` |
| `VIE_nat_sanctions_evasion` | timed 365 ngày | `trade_opinion_factor 0.15` (bù một phần), `stability_factor −0.01` | decision `VIE_nat_sanctions_evasion` |

**Danh sách "idea chế độ"** bị `VIE_nat_regime_exit` gỡ: `VIE_nat_emergency_rule`, ba charter, ba capstone, `VIE_nat_self_reliance`, `VIE_nat_armed_neutrality`, `VIE_nat_militia_mobilized`. Giữ lại: `VIE_nat_sovereignty_secured`, `VIE_nat_conventional_deterrent`.

#### 7.4.2 Idea và hệ thống tái sử dụng (không định nghĩa lại)

| Idea hoặc hệ thống | Dùng khi | Nguồn |
|---|---|---|
| `Reduced_Western_Sanctions` → `Western_Sanctions` → `international_sanctions` → `Massive_International_Sanctions` | Mọi bước "cô lập" | ✅ `MD:common/ideas/Burmese.txt:117,131,145`; `MD:common/ideas/Various.txt:412`; `increase_sanctions`/`decrease_sanctions` |
| `ASEAN_Member` | D6 | ✅ `MD:common/ideas/asean.txt:3` |
| `VIE_fdi_confidence_shock` | Tháo chạy vốn, bạo lực bài ngoại | ✅ `mod:common/ideas/VIE_md_ideas.txt` |
| `VIE_public_anger`, `VIE_civil_unrest_idea` | Bạo lực, đàn áp | ✅ mod |
| `the_military` | Cả chế độ | ✅ `MD:common/ideas/AA_law_internal_factions.txt:313` |
| `VIE_armed_forces_modifier` (biến `VIE_af_*`) | Focus quân sự của dải | ✅ `mod:common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt:3` |
| `VIE_state_modifier` (trục `VIE_ax_*`) | Focus chính trị ghi trục | ✅ mod |

#### 7.4.3 Opinion modifier mới (H9): 5

| Modifier | Giá trị | Dùng ở |
|---|---|---|
| `VIE_nat_common_threat` | +25, không decay | D2, hai chiều với USA, JAP, RAJ, PHI, AST |
| `VIE_nat_hegemony_rhetoric` | −25 | D2 (từ CHI) |
| `VIE_nat_citizens_attacked` | −50, decay 1/tháng | `vie_nat.31.a` |
| `VIE_nat_old_wounds` | −30, decay 0,5/tháng | `vie_nat.55.b` khi CBD từ chối (ký ức 1979–1989) **[LS]** |
| `VIE_nat_irredentist_rhetoric` | −50, decay 1/tháng | `vie_nat.25.b` (từ CHI) |

Khi rời ASEAN (D6) dùng opinion có sẵn của MD nếu có, nếu không thì thêm `VIE_nat_left_asean` −40 (❗N-09).

### 7.5 Scripted trigger (8)

| Trigger | Logic | Ghi chú |
|---|---|---|
| `VIE_nat_regime_active` | `original_tag = VIE` và `ruling_party` là 20, 21 hoặc 22 | Dùng trong mọi `available` của dải. Không dùng flag (I-16) |
| `VIE_nat_is_populist` / `VIE_nat_is_radical` / `VIE_nat_is_junta` | `check_variable = { ruling_party = 20 / 21 / 22 }` | Gate các cột V. Đổi biến thể là focus cột cũ hết khả dụng ngay; focus đang làm dở bị hủy vì `cancel_if_invalid` mặc định là `yes` |
| `VIE_nat_route_a_gate` | Xem 7.7, đường A | Có hai mức: `plausible` và `free` |
| `VIE_nat_radical_turn_allowed` | `VIE_ax_mob_norm > 8` **và** `VIE_ax_checks_norm < −4` **và** `count_triggers` ≥ 2 trong 3 điều kiện cấu trúc (≥ 1 nếu `VIE_ai_free`) | Theo ngưỡng Lạc Hồng (21) ở `VIE_transition_graph_step8.md:117`. Ba điều kiện: (1) **khủng hoảng chính danh**: `has_stability < 0.35` hoặc `VIE_crisis_count_ge_2`; (2) **tinh hoa ly khai**: `VIE_nat_elite_split` hoặc `the_military_opinion < 50`; (3) **rạn độc quyền bạo lực**: đã làm `VIE_nat_militia_self_defense` (lực lượng vũ trang ngoài quân đội) hoặc đang có `VIE_public_anger` (bạo lực đường phố được dung thứ: `vie_nat.15.b`, `vie_alt.1.c`). Việc này lấp đúng khoảng trống "chưa có cách đo" mà `VIE_transition_graph_step8.md` mục 8 ghi lại |
| `VIE_nat_has_sanctions` | Có một trong 4 idea trừng phạt | Dùng cho decision giảm cô lập |
| `VIE_nat_leader_is_ai_safe` | `is_ai = no` hoặc `strength_ratio = { tag = CHI ratio > 0.4 }` | Chặn AI tự sát trong T. Cú pháp ✅ `MD:common/national_focus/05_belarus.txt:4769` |

### 7.6 Scripted effect

Hợp đồng (contract) của từng effect: đầu vào, các bước, và bất biến. Đây không phải code.

**`VIE_nat_regime_init`** (đầu vào: temp `VIE_nat_route`)
1. Nếu `VIE_nat_route = 0` thì suy ra: có `VIE_post_collapse` và slot 20 → 4; có `VIE_democracy_elected` và slot 20 → 3; còn lại → 0.
2. `set_country_flag = VIE_nat_regime_init`.
3. `set_power_balance = { id = VIE_nat_balance … set_value = <bảng 7.3> }`; đặt `VIE_bop_nat_active`.
4. Bảo đảm có `the_military`: nếu chưa có thì đổi `communist_cadres` → `the_military`; nếu không có `communist_cadres` thì đổi `farmers`; nếu không có cả hai thì không thêm (mọi chỗ đọc `mil` đều có guard `has_idea = the_military`). Sau đó `set_variable = { the_military_opinion = <bảng 7.3> }` và gọi `apply_the_military_dynamic_effect_DYNMOD` (✅ `MD:…/00_internal_faction_effects.txt:894`). Lý do đổi `communist_cadres`: dưới chế độ mới, bộ máy cán bộ Đảng mất vai trò thể chế.
5. Cosmetic tag: slot 20 hoặc 22 → `VIE_NAT`; slot 21 → `VIE_NATR` (mục 7.13).
6. `activate_mission = VIE_nat_consolidation_deadline`.
7. Nếu `VIE_nat_leader_id` bằng 0: `country_event = { id = vie_nat.9 days = 1 }`. (Lúc này `set_leader_VIE` đã chạy trong `change_ruling_party_effect` và dựng lãnh đạo mặc định, xem `VIE_nat_create_leader`.)
8. `country_event = { id = vie_nat.10 days = 7 }`; `country_event = { id = vie_nat.11 days = 30 }`.
9. `news_event = { id = vie_nat_news.1 days = 1 }`.

**`VIE_nat_regime_exit`**
1. Nếu có `VIE_bop_nat_active`: `remove_power_balance = { id = VIE_nat_balance }`, xóa flag.
2. Gỡ các "idea chế độ" (7.4.1), mỗi idea có guard `has_idea`.
3. `set_cosmetic_tag = VIE_AUTH_S`, cosmetic mặc định của MD (✅ `MD:history/countries/VIE - Vietnam.txt:4`).
4. Xóa `VIE_nat_regime_init`. Không xóa `VIE_nat_leader_id`.
5. Không trả lại `communist_cadres`: nếu Đảng trở lại, `vie_nat.41` tự xử lý.

**`VIE_nat_on_variant_change`** (đổi trong nhóm 20/21/22)
1. Nếu đã làm N8: swap charter cũ sang charter tương ứng với slot mới (`swap_ideas`).
2. Sang 21: `set_cosmetic_tag = VIE_NATR`; `VIE_nat_sanction_up`; `news_event vie_nat_news.2`.
3. Từ 21 sang 20 hoặc 22: `set_cosmetic_tag = VIE_NAT`.

**`VIE_nat_sanction_up`**: nếu không có bậc nào thì `add_ideas = Reduced_Western_Sanctions`, còn không thì `increase_sanctions`. Lý do: `increase_sanctions` chỉ nâng bậc đang có (✅ `MD:common/scripted_effects/00_sanctions_scripted_effects.txt:2`).

**`VIE_nat_sanction_down`**: `decrease_sanctions` (✅ cùng file, dòng 30).

**`VIE_nat_create_leader`** (gọi từ nhánh 20, 21, 22 của `set_leader_VIE`, H6). Nếu `VIE_nat_leader_id` bằng 0 thì dùng mặc định theo slot: 22 → 1, 20 và 21 → 2.

| `VIE_nat_leader_id` | Tên (hư cấu, ASCII) | Trait nguyên mẫu | Ghi chú |
|---|---|---|---|
| 1 | Gen. Trinh Van Hieu | `army_general`, `military_career` | Tên đã có trong mod |
| 2 | Luu Quang Vinh | slot 20: `populist`; slot 21: `fascist_demagogue` | Nhà hùng biện |
| 3 | Doan Minh Triet | `technocrat`, `economist` | Kỹ trị |
| 4 | Gen. Ha Duc Thang | `army_general`, `ruthless` | Sau đảo chính |
| 5 | Kieu Van Lam | `populist`, `stubborn` | Thế hệ sau |
| 6 | Vu Thanh Son | `technocrat`, `cautious` | Thế hệ sau |

Trait ideology thêm theo slot: `nationalist_Nat_Populism`, `nationalist_Nat_Fascism`, `nationalist_Nat_Autocracy` (✅ `MD:common/country_leader/00_traits.txt:138,144,150`). Mọi trait nguyên mẫu đã có trong `00_traits.txt`. Trước khi merge phải đối chiếu tên với danh sách người nổi tiếng còn sống (giới hạn nội dung 5).

**`VIE_nat_monthly`** (chỉ chạy khi `VIE_nat_regime_active`)
1. Trôi BoP (bảng 7.3).
2. Slot 20: `temp_opinion = −0.5` → `change_the_military_opinion`.
3. **Bước ngoặt**: BoP ≥ 0,6, không phải slot 21, chưa có `VIE_nat_turning_point_done`, không có `VIE_popup_cd` → `vie_nat.20`.
4. **Bạo lực**: nếu BoP ≥ 0,2 và không có `VIE_nat_violence_cd` thì tính `VIE_nat_roll` = 2; ×2 nếu BoP ≥ 0,6; ×0,5 nếu đã làm S4; ×0,5 nếu `WS < 0.4`. Roll `random = { chance = VIE_nat_roll }` → `vie_nat.30`. Kỳ vọng: BoP 0,3 cho khoảng 22%/năm; BoP 0,7 khoảng 40%/năm.
5. **[FR]**: slot 21, BoP ≥ 0,8, chưa có `VIE_nat_fringe_done` → `random = { chance = 5 }` → `vie_nat.25`.
6. **Trừng phạt**: slot 21 và BoP ≥ 0,6 → `random = { chance = 3 }` → `vie_nat.35`.
7. **Kế vị**: slot 21, `VIE_nat_leader_id` không đổi trong 10 năm (❗N-11: dùng `set_country_flag` với `days = 3650` làm đồng hồ) → `vie_nat.42`.
8. **Chiến tranh với CHI**: nếu `has_war_with = CHI` và chưa có flag thì đặt `VIE_nat_war_with_chi` và gửi `vie_nat.51` (chỉ lần đầu). Nếu có flag mà hết chiến tranh: xóa flag; nếu sở hữu 813 → `vie_nat.52`, ngược lại → `vie_nat.53`.
9. **Chiếm Hoàng Sa trong hòa bình**: sở hữu 813, không có `VIE_nat_paracels_held` → đặt flag, gửi `vie_nat.52`.

Mọi `random` trong effect chạy mỗi tháng. Các event pop-up tôn trọng `VIE_popup_cd`, trừ khi được ghi là "Class A".

**`VIE_event_scheduler_nat`** (gọi hàng tháng, H7; bỏ qua khi `VIE_catch_up = 1`)
1. **Phát hiện vào**: `VIE_nat_regime_active` và không có `VIE_nat_regime_init` → `VIE_nat_regime_init` (route 0).
2. **Phát hiện ra**: có `VIE_nat_regime_init` mà không `VIE_nat_regime_active` → `VIE_nat_regime_exit`.
3. **Đường A**: `VIE_nat_route_a_gate`, không có `VIE_nat_plenum_cd`, không có `VIE_popup_cd` → `random = { chance = 10 }` → `vie_nat.1`.
4. **Đường C** (giai đoạn 2): xem 7.7.
5. Nếu `VIE_nat_regime_active` → `VIE_nat_monthly`.

### 7.7 Bốn đường vào

**Đường A: Hội nghị bất thường → slot 22 [AH]**

| Mục | Nội dung |
|---|---|
| Gate `plausible` | `VIE_party_rule_active`; `VIE_d4_hard_line`; `VIE_scs_escalated_trigger`; `VIE_ax_mob_norm > 6`; `VIE_ax_checks_norm < 1`; nếu đã có `the_military` thì `the_military_opinion > 59` (faction này chỉ tự xuất hiện khi `VIE_ax_mob_norm > 7`, nên không bắt buộc phải có); **một cú sốc ngoài**: `has_war_with = CHI` hoặc `has_idea = VIE_china_pressure_idea` hoặc `VIE_crisis_count_ge_2` hoặc `has_stability < 0.4`; không có `VIE_regime_changed_recently` |
| Gate `free` | Như trên nhưng `VIE_ax_mob_norm > 5`, ngưỡng opinion 49, không cần cú sốc |
| Kích hoạt | Scheduler, 10%/tháng khi gate đúng |
| Event | `vie_nat.1` (mục 7.9) |
| Vì sao 22 mà không qua 20 | `VIE_transition_graph_step8.md` chỉ cho vào 22 từ 20. Đường A là ngoại lệ có chủ đích: phe chủ quyền trong Đảng dựa vào quân đội, không cần phong trào đường phố. Gate trục vì vậy dùng ngưỡng của Dân túy (`mob ≥ 7`, `checks ≤ 0`) cộng thêm điều kiện quân đội |

**Đường B: Ủy ban Cứu quốc → slot 22 (hoặc 20) [AH]**

| Mục | Nội dung |
|---|---|
| Hook | H4: option c mới trong `vie_col.1` (mùa đông, cơ hội cuối trước sụp đổ) |
| Trigger option | (`VIE_d4_hard_line` hoặc `VIE_ax_mob_norm > 4`) và (không có `the_military` hoặc `the_military_opinion > 49`) |
| Hiệu ứng | `VIE_nat_route = 2`; `rul_party_temp = 22`; `VIE_transition_regime`; `add_stability = 0.05`; `VIE_collapse_immunity` 730 ngày; `country_event = vie_nat.2` sau 5 ngày |
| AI | base 3; ×0 khi `VIE_ai_historical`; +150 khi `VIE_AI_PATH_NATIONALIST` |

**Đường C: thắng cử → slot 20 [AH]** — *giai đoạn 2, phụ thuộc con đường dân chủ*

| Mục | Nội dung |
|---|---|
| Tiền đề | `VIE_democracy_elected` và `has_elections = yes` (❗N-12: chuỗi `vie_alt.12–14` phải được nối dây trước) |
| Đảng ra đời | Scheduler: chưa có flag `VIE_nat_party_founded`, và (`VIE_scs_escalated_trigger` hoặc có idea `recession` hoặc `VIE_crisis_count_ge_2`) → `vie_nat.4`: `unban_party_scripted_call` với `party_index = 20`, popularity +0,04 |
| Lớn lên | Khi đảng 20 hợp pháp: nếu `VIE_scs_escalated_trigger` thì +0,005/tháng (trần 0,35). Theo quy tắc MD, đảng lập sau năm 2000 phải ẩn đến lúc được tạo (✅ `MD:.claude/docs/content-guidelines.md:16`); điều này đã đúng vì đảng 20 bị cấm và có popularity 0 |
| Vào chế độ | Bầu cử MD (✅ `MD:events/MD_Elections.txt:96`) đưa 20 lên → phát hiện → init, route 3, giữ bầu cử |

**Đường D: nội chiến → slot 20 [AH]**

| Mục | Nội dung |
|---|---|
| Hook 1 (H2) | Option c mới của `vie_alt.1`, "Để đường phố dẫn dắt". Trigger: `check_variable = { VIE_hd981_response = 2 }`, `VIE_scs_escalated_trigger`, `VIE_ax_mob_norm > 4`. Hiệu ứng: `set_country_flag = VIE_d4_street`; trục `mob +2`, `checks −1`; `add_stability = −0.03`; idea `VIE_public_anger` 180 ngày |
| Hook 2 (H3) | `VIE_col_pick_rebel`: `VIE_d4_street` và `VIE_ax_mob_norm > 6` → phe nổi dậy 20 (state 521, 520 như code hiện có) |
| Vào chế độ | Phe nổi dậy thắng → `VIE_collapse_aftermath` (✅ `mod:…/VIE_md_effects_p3.txt:125`) → phát hiện → init, route 4 |

**Lối thoát ở mọi đường.** `vie_nat.1` có option A (từ chối). `vie_col.1` giữ option a và b. `vie_alt.1` giữ option a lịch sử ở vị trí đầu. AI của mọi option lịch sử có `base = 100`.

### 7.8 Dải focus (49 focus)

#### 7.8.0 Quy ước chung

- **Vị trí.** Gốc `VIE_nat_salvation_government` đặt `relative_position_id = VIE_doi_moi_continues`, ở vùng trống bên phải dải An ninh (dải An ninh dùng x 216–232, y 28–29, ✅ `mod:…/VIE_md_focus.txt:3436`). Tọa độ tuyệt đối do `tools/layout_applier.py` chốt (❗N-14). Mọi focus khác dùng `relative_position_id` theo tọa độ tương đối trong bảng 7.8.8.
- **Một gốc duy nhất.** Mọi focus của dải đều nối về N1, để một dòng `shared_focus` là đủ kéo cả dải vào cây (N-01).
- **`available`.** Mọi focus có `VIE_nat_regime_active = yes`. Focus cột V dùng thêm `VIE_nat_is_populist/radical/junta`.
- **Cost.** MD tính 1 đơn vị = 7 ngày; mặc định 10 và không ghi. Dải này dùng 3–7 cho focus thường, 10 cho capstone, vì chế độ khủng hoảng cần nhịp nhanh.
- **Chuẩn MD** (✅ `MD:.claude/docs/focus-tree-reference.md`): thứ tự thuộc tính cố định, `log` trong `completion_reward`, `ai_will_do` đặt cuối, `search_filters` hai lớp, tối đa 5 hiệu ứng vĩnh viễn, bankruptcy guard cho focus tiêu tiền.
- **Nhãn.** Mô tả của mọi focus kết thúc bằng `$VIE_nat_ah_note$` (dòng "Lịch sử giả định"). Focus có tham chiếu lịch sử thật thêm `$VIE_nat_ls_note_<id>$`.
- **Ký hiệu hiệu ứng.** `BoP ±n` = helper 7.3. `mil ±n` = `temp_opinion` + `change_the_military_opinion`; lưu ý MD **nhân đôi** giá trị dương khi slot là 21 hoặc 22 (✅ `MD:…/00_internal_faction_effects.txt:1001`), nên cột "mil" ghi giá trị trước khi nhân. `ax.<trục> ±n` = `add_to_variable` trên `VIE_ax_*` với tooltip `VIE_ax_<trục>_tt` (mẫu có sẵn trong cây). `af.<khóa> +n` = biến `VIE_af_*` của `VIE_armed_forces_modifier` với tooltip `modifies_dynamic_modifier_tt`. `TREAS ±n` = `treasury_change` + `modify_treasury_effect`.
- **AI.** Cột AI ghi `base`, sau dấu chấm phẩy là modifier (`slot 21 → 90` nghĩa là `base` thành 90 khi ở slot 21; `+50` nghĩa là `add = 50`). Mọi focus tiêu tiền có `factor = 0` khi `has_active_mission = bankruptcy_incoming_collapse`.

#### 7.8.1 Trunk N: Nắm quyền và củng cố (9)

| # | ID | Tên EN / VI | Cost | Prereq · ME | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|
| N1 | `VIE_nat_salvation_government` | The National Salvation Government / Chính phủ Cứu quốc | 3 | — | `add_timed_idea VIE_nat_emergency_rule` 365 ngày *(timed idea)*; `PP +50`; `unlock_decision_category_tooltip = VIE_nat_cat_regime` *(mở category)*. Mô tả có dòng miễn trừ lịch sử (mục 7.13) | 100 |
| N2 | `VIE_nat_dissolve_old_institutions` | Dissolve the Old Institutions / Giải thể thiết chế cũ | 5 | N1 | Cấm đảng 19 (`party_index = 19`, `ban_party_scripted_call`) *(chính trị)*; `ax.checks −2`; `STAB −0.03`; `PP +75`; `country_event vie_nat.12` sau 60 ngày *(event)* | 90 |
| N3 | `VIE_nat_secure_armed_forces` | Secure the Armed Forces / Nắm chắc lực lượng vũ trang | 5 | N1 | `mil +10` *(faction)*; `increase_military_spending` *(luật ngân sách)*; `af.army_org_factor +0.02` | 90 |
| N4 | `VIE_nat_new_national_front` | A New National Front / Mặt trận Dân tộc mới | 5 | N2 | `STAB +0.03`; `WS +0.03`; `ax.mob +1`; mở decision `VIE_nat_mass_rally` (`unlock_decision_tooltip`). Mô tả dùng hình ảnh "Nam quốc sơn hà" **[LS: di sản chung]** | 80 |
| N5 | `VIE_nat_emergency_economy` | Emergency Economic Measures / Biện pháp kinh tế khẩn cấp | 5 | N1 | `TREAS +4` (thu khẩn cấp) *(treasury)*; `STAB −0.02`; mở ngã rẽ N6/N7 | 80 |
| N6 | `VIE_nat_reassure_foreign_capital` | Reassure Foreign Capital / Trấn an vốn ngoại | 5 | N5 · ME N7 | Gỡ `VIE_fdi_confidence_shock` nếu có; `VIE_nat_sanction_down` *(ngoại giao)*; `BoP −0.10`; `small_increase` opinion với JAP, KOR, SIN, TAI. Nếu làm trước ngày 30, `vie_nat.11` không nổ (trigger của event) | 60; slot 22 → 80 |
| N7 | `VIE_nat_economic_self_reliance` | Economic Self-Reliance / Tự lực kinh tế | 5 | N5 · ME N6 | `add_ideas VIE_nat_self_reliance` *(idea)*; `one_random_arms_factory` *(công trình, trừ 7,5)*; `ax.integ −2`; `ax.market −1`; `BoP +0.05` | 40; slot 21 → 90. Bankruptcy guard |
| N8 | `VIE_nat_national_charter` | The National Charter / Hiến chương Quốc gia | 7 | N2 và N4 | Swap `VIE_nat_emergency_rule` sang charter theo slot (nếu idea khẩn cấp đã hết hạn thì add) *(idea swap)*; `ax.checks −1`; `STAB +0.02`. Là gốc của cả ba cột V | 90 |
| N9 | `VIE_nat_regime_consolidated` | The Regime Consolidated / Chế độ được củng cố | 7 | N8, N3, và (N6 hoặc N7) | Hoàn thành mission `VIE_nat_consolidation_deadline` *(mission)*; `STAB +0.05`; `PP +75`; nếu đã làm `VIE_assert_maritime_rights` thì `country_event vie_nat.50` *(event)*. Là gốc của nhánh M4, D và T | 90 |

#### 7.8.2 Cột V1: Dân tộc dân túy, slot 20 (7) [AH]

Cơ chế riêng: **bầu cử**. Đây là biến thể duy nhất có thể tự thua bầu cử và rời chế độ một cách hòa bình. Rủi ro riêng: `mil −0.5` mỗi tháng.

| # | ID | Tên EN / VI | Cost | Prereq · ME | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|
| V1-1 | `VIE_nat_voice_of_the_nation` | The Voice of the Nation / Tiếng nói Dân tộc | 5 | N8 | `PP +50`; popularity đảng 20 +0,05 (`change_relative_party_popularity`) *(chính trị)*; `BoP +0.05` | 90 |
| V1-2 | `VIE_nat_special_tribunals` | Special Anti-Corruption Tribunals / Tòa án đặc biệt chống tham nhũng | 5 | V1-1 | `decrease_corruption` *(hệ tham nhũng MD)*; `TREAS +3` (tịch thu); `mil −5`; `industrial_conglomerates` opinion −10 nếu có faction; `BoP +0.05` | 80 |
| V1-3 | `VIE_nat_sovereignty_referendum` | A Sovereignty Referendum / Trưng cầu dân ý về chủ quyền | 5 | V1-1 | `country_event vie_nat.14` *(event có lựa chọn)* | 70 |
| V1-4 | `VIE_nat_welfare_for_the_people` | Welfare for the People / An sinh cho nhân dân | 5 | V1-2 | `increase_social_spending` *(luật ngân sách)*; `STAB +0.03`; `ax.mob +1`; `farmers` opinion +10 nếu có | 70 |
| V1-5a | `VIE_nat_keep_managed_elections` | Keep Managed Elections / Giữ bầu cử có kiểm soát *(kìm hãm)* | 5 | V1-3 và V1-4 · ME V1-5b | Bật bầu cử bằng `set_elections_with_frequency` với chu kỳ 60 tháng tính từ năm hiện tại (✅ `MD:common/scripted_effects/00_MD_politicsview_scripted_effects.txt:2165`). Không dùng `set_politics` trần: lịch sử VIE có `last_election = 1932.11.8`, nên bật bầu cử mà không đặt lại ngày có thể gây bầu cử ngay lập tức; gỡ cấm đảng 13 (đối lập kỹ trị, có thể thắng) *(chính trị)*; `BoP −0.10`; `VIE_nat_sanction_down`; `ax.checks +2` | 50; +30 khi BoP > 0,4 |
| V1-5b | `VIE_nat_postpone_elections` | Postpone the Elections / Hoãn bầu cử | 5 | V1-3 và V1-4 · ME V1-5a | `set_politics = { elections_allowed = no }`; `PP +75`; `mil +5`; `BoP +0.10`; `ax.checks −2` | 50 |
| V1-6 | `VIE_nat_peoples_nationalism` | People's Nationalism / Chủ nghĩa dân tộc nhân dân | 10 | V1-5a hoặc V1-5b | `add_ideas VIE_nat_peoples_nationalism` *(idea)*; mở decision `VIE_nat_patriotic_bonds` *(decision)*. Nếu đã làm V1-5a: popularity đảng 20 +0,10 | 70 |

#### 7.8.3 Cột V2: Quân quản dân tộc, slot 22 (7) [AH]

Cơ chế riêng: **lộ trình dân sự** (mission). Theo Geddes, chế độ quân sự giải huy động, nên cột này kéo BoP về Kỷ cương.

| # | ID | Tên EN / VI | Cost | Prereq · ME | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|
| V2-1 | `VIE_nat_supreme_defense_council` | The Supreme National Defense Council / Hội đồng Quốc phòng Tối cao | 5 | N8 | `mil +5` (thành +10); `PP +40`; `af.planning_speed +0.05`; `ax.checks −1` | 90 |
| V2-2 | `VIE_nat_technocratic_cabinet` | A Technocratic Cabinet / Nội các kỹ trị | 5 | V2-1 | `add_tech_bonus` `CAT_industry` 50% 1 lần *(tech)*; `ax.merit +2`; `VIE_nat_sanction_down`; `BoP −0.05` | 80 |
| V2-3 | `VIE_nat_order_and_discipline` | Order and Discipline / Trật tự và kỷ luật | 5 | V2-1 | `increase_policing_budget` *(luật ngân sách)*; `STAB +0.04`; `WS −0.03`; `ax.civil −2`; `BoP −0.10` | 80 |
| V2-4 | `VIE_nat_defense_conglomerates` | Defense-Industrial Conglomerates / Tập đoàn công nghiệp quốc phòng | 7 | V2-2 | `one_random_arms_factory` ×2 *(công trình, trừ 15)*; `industrial_conglomerates` opinion +10 nếu có | 70. Bankruptcy guard |
| V2-5a | `VIE_nat_promise_civilian_rule` | Promise a Return to Civilian Rule / Hứa trao quyền dân sự *(kìm hãm)* | 5 | V2-3 và V2-4 · ME V2-5b | `activate_mission VIE_nat_civilian_roadmap` *(mission)*; `VIE_nat_sanction_down`; `BoP −0.10`; `mil −5`; `small_increase` opinion với USA, JAP | 50 |
| V2-5b | `VIE_nat_indefinite_guardianship` | Indefinite Guardianship / Giám hộ vô thời hạn | 5 | V2-3 và V2-4 · ME V2-5a | `mil +10` (thành +20); `PP +50`; `ax.checks −2`; `BoP +0.05` | 50 |
| V2-6 | `VIE_nat_fortress_state` | The Fortress State / Nhà nước pháo đài | 10 | V2-5a hoặc V2-5b | `add_ideas VIE_nat_fortress_state` *(idea)*; `522 = { one_state_anti_air }` và `519 = { one_state_anti_air }` *(công trình, trừ 6,5)* | 70. Bankruptcy guard |

#### 7.8.4 Cột V3: Cực đoan, slot 21 (6) [AH]

**Cổng.** Chỉ mở khi `vie_nat.20` chọn "Embrace" (slot đổi sang 21). Mô tả cả cột có dòng: *"Alternate history. No such movement has existed in modern Vietnam."* Cơ chế riêng: **tự ăn mòn** — mọi focus đều trả bằng quân đội, ổn định hoặc ngoại giao.

| # | ID | Tên EN / VI | Cost | Prereq · ME | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|
| V3-1 | `VIE_nat_the_supreme_leader` | The Supreme Leader / Lãnh tụ tối cao | 5 | N8 | `PP +100`; `ax.checks −3`; `BoP +0.05`; `country_event vie_nat.21` sau 30 ngày *(event)* | 90 |
| V3-2 | `VIE_nat_one_national_movement` | One National Movement / Một phong trào dân tộc | 5 | V3-1 | `set_country_flag = free_ban_parties` rồi `set_partyall_banned` (✅ `MD:…/00_MD_politicsview_scripted_effects.txt:2118`) *(chính trị)*; `STAB −0.03`; `WS +0.05`; `ax.civil −3` | 80 |
| V3-3 | `VIE_nat_youth_vanguard` | The Youth Vanguard / Đội tiên phong thanh niên | 5 | V3-1 | `af.training_time_factor −0.10`; `WS +0.03`; `mil −5` (quân đội ghét lực lượng song song) *(faction)* | 70 |
| V3-4 | `VIE_nat_purge_the_moderates` | Purge the Moderates / Thanh trừng phe ôn hòa | 5 | V3-2 | `mil −15`; `PP +75`; `STAB −0.03`; `BoP +0.10`; `country_event vie_nat.22` sau 90 ngày *(event)* | 60 |
| V3-5 | `VIE_nat_war_economy` | The War Economy / Kinh tế thời chiến | 7 | V3-3 và V3-4 | `increase_military_spending`; `decrease_social_spending` (✅ `MD:common/scripted_effects/00_budget_effects.txt:323`) *(luật ngân sách)*; `one_random_arms_factory` *(trừ 7,5)*; `ax.market −2` | 60. Bankruptcy guard |
| V3-6 | `VIE_nat_totalist_state` | The Totalist State / Nhà nước toàn trị | 10 | V3-4 và V3-5 | `add_ideas VIE_nat_totalist_state` *(idea)*; `VIE_nat_sanction_up` *(ngoại giao)*. Là điều kiện của T3 và D6 | 50 |

*Không dùng tên học thuyết "Dân tộc Sinh tồn" của Đại Việt Quốc dân Đảng cho focus nào.* Báo cáo gắn nó với biến thể cực đoan và tự đánh dấu mức ảnh hưởng là [D] (còn tranh cãi). Gắn học thuyết của một đảng có thật vào capstone toàn trị là quy kết mà nguồn chưa đủ chắc.

#### 7.8.5 Nhánh S: Thiết chế chung, gồm các lựa chọn kìm hãm (6)

| # | ID | Tên EN / VI | Cost | Prereq | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|
| S1 | `VIE_nat_patriotic_education` | Patriotic Education / Giáo dục yêu nước | 5 | N4 | `increase_education_budget` *(luật ngân sách)*; `ax.mob +1`; `WS +0.02` | 70 |
| S2 | `VIE_nat_call_the_diaspora` | A New Dong Du: Call on the Diaspora / Đông Du mới: Kêu gọi kiều bào | 5 | S1 | `country_event vie_nat.13` *(event có lựa chọn)*. Tên gợi phong trào Đông Du 1905–1908 **[LS]** | 50 |
| S3 | `VIE_nat_veterans_associations` | Mobilize the Veterans' Associations / Huy động Hội Cựu chiến binh | 5 | N3 | `mil +5`; `WS +0.02`; `ax.mob +1`; `STAB +0.02` | 70 |
| S4 | `VIE_nat_protect_every_citizen` | Protect Every Citizen / Bảo vệ mọi công dân *(kìm hãm)* | 5 | N4 | `BoP −0.20`; `WS −0.03`; `ax.civil +1`; giảm một nửa xác suất `vie_nat.30` và làm option A của nó mạnh hơn *(cơ chế)* | 60; slot 21 → 10 |
| S5 | `VIE_nat_unity_of_54_peoples` | Unity of the 54 Peoples / Đoàn kết 54 dân tộc *(kìm hãm)* | 5 | S4 | `BoP −0.10`; `STAB +0.03`; `ax.decent +1` | 60; slot 21 → 10 |
| S6 | `VIE_nat_reconciliation_commission` | A National Reconciliation Commission / Ủy ban Hòa giải Dân tộc *(kìm hãm)* | 7 | S5 | Gỡ cấm đảng 19 (đối lập hợp pháp) *(chính trị)*; `clr_country_flag = VIE_nat_elite_split` *(cơ chế: gỡ một điều kiện cấu trúc của slot 21)*; `BoP −0.05`; `STAB +0.02`; `mil −5` | 40; slot 21 → 0 |

Bỏ focus "New National Symbols" của báo cáo: cosmetic tag được đặt tự động khi vào chế độ (7.6), nên focus đó không còn việc gì để làm.

#### 7.8.6 Nhánh M: Quân sự riêng của chế độ (4)

Nhánh này **không** nhân đôi nhánh quân sự hiện có. Capstone M4 thưởng cho việc đã đi nhánh đó.

| # | ID | Tên EN / VI | Cost | Prereq | `available` thêm | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|---|
| M1 | `VIE_nat_modern_peoples_war` | A Modernized People's War / Chiến tranh nhân dân hiện đại | 7 | N3 | — | `army_experience = 25`; `af.army_defence_factor +0.03`; `af.dig_in_speed_factor +0.10`; `mil +3` | 90 |
| M2 | `VIE_nat_militia_self_defense` | Militia and Self-Defense Forces / Dân quân tự vệ | 5 | M1 | — | Mở decision `VIE_nat_mobilize_militia` *(decision)*; `ax.mob +1`; `WS +0.03`; tính là điều kiện cấu trúc (3) | 70 |
| M3 | `VIE_nat_northern_border_fortification` | Fortify the Northern Border / Công sự hóa biên giới phía Bắc | 5 | M1 | — | `add_building_construction` loại `bunker` (✅ `MD:common/buildings/00_buildings.txt:285`) cấp 2 tại các province giáp CHI của 523 và 524 (❗N-13: danh sách province) *(công trình)*; `TREAS −2` ghi rõ, vì `add_building_construction` thô không tự trừ tiền | 60. Bankruptcy guard |
| M4 | `VIE_nat_conventional_deterrent` | A Conventional Deterrent / Răn đe quy ước | 10 | N9 và M1 | `count_triggers` ≥ 3 trong: `VIE_kilo_submarines`, `VIE_bastion_p_coastal_defence`, `VIE_integrated_air_defense`, `VIE_uav_program`, `VIE_su30mk2_fleet`, `VIE_z_factories` (`has_completed_focus`), bọc trong `custom_trigger_tooltip` | `add_ideas VIE_nat_conventional_deterrent` *(idea)*; `mil +5` | 50 |

**Không có focus vũ khí hạt nhân.** Mod đã có chuỗi `VIE_nuc_*` trong cây chính. Dải này không đụng tới và không thêm gì vào đó.

#### 7.8.7 Nhánh D: Ngoại giao (6) và nhánh T: Lãnh thổ (4)

| # | ID | Tên EN / VI | Cost | Prereq · ME | `available` thêm | Phần thưởng (loại) | AI |
|---|---|---|---|---|---|---|---|
| D1 | `VIE_nat_foreign_policy_review` | A Foreign Policy Review / Rà soát chính sách đối ngoại | 3 | N9 | — | `PP +25`; `ax.integ −1`. Mô tả đối chiếu chính sách "Bốn không" có thật trong Sách trắng Quốc phòng 2019 **[LS]** | 90 |
| D2 | `VIE_nat_front_against_hegemony` | A Front against Hegemony / Mặt trận chống bá quyền | 5 | D1 · ME D3, D4 | `power_balance_value < 0.4`; không phải slot 21 | Opinion `VIE_nat_common_threat` hai chiều với USA, JAP, RAJ, PHI, AST; `VIE_nat_hegemony_rhetoric` từ CHI; `VIE_nat_sanction_down`; `USA = { country_event vie_nat.60 }` với `TT_IF_THEY_ACCEPT` *(event chéo nước)*; `ax.west +2` | 50; slot 22 → 70 |
| D3 | `VIE_nat_eurasian_partnership` | A Eurasian Partnership / Đối tác Á–Âu | 5 | D1 · ME D2, D4 | `country_exists = SOV` | `SOV = { country_event vie_nat.61 }` với `TT_IF_THEY_ACCEPT` *(event chéo nước)*; `small_increase` opinion với SOV, RAJ; `ax.west −2` | 40; slot 20 → 60 |
| D4 | `VIE_nat_armed_neutrality` | Armed Neutrality / Trung lập vũ trang | 5 | D1 · ME D2, D3 | — | `add_ideas VIE_nat_armed_neutrality` *(idea)*; `WS +0.05`; `BoP +0.05` | 20; slot 21 → 90 |
| D5 | `VIE_nat_lead_the_mainland_bloc` | Lead the Mainland Bloc / Dẫn dắt khối lục địa | 5 | D1 | `country_exists = LAO` | `change_influence_percentage` +10 lên LAO và CBD, gọi **bên trong** scope của từng nước (✅ `MD:.claude/docs/scripting-edge-cases.md:41`) *(influence)*; nếu chưa trong faction: `create_faction_from_template = faction_template_generic_regional_security` *(faction)*; `LAO = { country_event vie_nat.56 }`. Mô tả nhắc Hiệp ước Hữu nghị và Hợp tác Việt–Lào 1977 **[LS]** | 70 |
| D6 | `VIE_nat_leave_asean` | Leave ASEAN / Rời ASEAN | 5 | D4 và V3-6 | Slot 21; `has_idea = ASEAN_Member` | `remove_ideas = ASEAN_Member` (tiền lệ `BRM_leave_asean`) *(ngoại giao)*; mọi nước trong `global.ASEAN_Member` −40 opinion (N-09); `WS +0.05`; `BoP +0.05`; `news_event vie_nat_news.6` | 30; `VIE_AI_PATH_NAT_RADICAL` → +50 |
| T1 | `VIE_nat_stop_at_sovereignty` | Stop at Sovereignty / Dừng ở chủ quyền *(kìm hãm)* | 5 | N9 · ME T3 | — | `add_ideas VIE_nat_sovereignty_secured` *(idea)*; `BoP −0.20`; `VIE_nat_sanction_down`; `WS −0.05` | 70; slot 21 → 20 |
| T2 | `VIE_nat_victors_peace` | The Victor's Peace / Hòa bình của kẻ thắng | 5 | N9 | Sở hữu 813 | Mở decision core 813 và các state Trường Sa *(decision)*; `STAB +0.05`; `WS +0.05` | 80 |
| T3 | `VIE_nat_consolidate_the_spratlys` | Consolidate the Spratlys / Thống nhất Trường Sa | 7 | N9 và (V3-6 hoặc D4) · ME T1 | `has_war = no` | Mở decision nhắm mục tiêu `VIE_nat_press_spratly_claim` *(decision)*; `BoP +0.10`; `VIE_nat_sanction_up` | 10; `VIE_AI_PATH_NAT_RADICAL` → +40 |
| T4 | `VIE_nat_indochinese_sphere` | An Indochinese Sphere / Vùng ảnh hưởng Đông Dương | 7 | D5 | — | Mở decision nhắm mục tiêu `VIE_nat_offer_protectorate` *(decision)*; `ax.integ −1`. Nhãn: "tiền lệ ảnh hưởng thập niên 1980 **[LS]**; bảo hộ là **[AH]**" | 30 |

**Hoàng Sa.** Chiến dịch Hoàng Sa của báo cáo (T02) chính là focus có sẵn `VIE_paracel_ultimatum` (claim 813, wargoal `take_state_focus`, ✅ `mod:…/VIE_md_focus.txt:1021`). Dải không lặp lại nó. T2 xử lý phần hậu chiến.

**Tầng 3 [FR].** Không có focus. Xem event `vie_nat.25`.

#### 7.8.8 Tọa độ tương đối (gợi ý cho layout)

Tất cả tương đối với N1 (x, y). Chỉ là bố cục khởi điểm; công cụ layout của mod chốt cuối.

| Khối | Focus và tọa độ |
|---|---|
| N | N1 (0,0) · N2 (−1,1) · N3 (2,1) · N5 (1,1) · N4 (−1,2) · N6 (0,2) · N7 (2,2) · N8 (−1,3) · N9 (0,4) |
| V1 | V1-1 (−7,4) · V1-2 (−8,5) · V1-3 (−6,5) · V1-4 (−8,6) · V1-5a (−8,7) · V1-5b (−6,7) · V1-6 (−7,8) |
| V2 | V2-1 (−3,4) · V2-2 (−4,5) · V2-3 (−2,5) · V2-4 (−4,6) · V2-5a (−4,7) · V2-5b (−2,7) · V2-6 (−3,8) |
| V3 | V3-1 (1,5) · V3-2 (0,6) · V3-3 (2,6) · V3-4 (0,7) · V3-5 (2,7) · V3-6 (1,8) |
| S | S1 (−11,3) · S2 (−11,4) · S3 (−12,2) · S4 (−10,3) · S5 (−10,4) · S6 (−10,5) |
| M | M1 (5,2) · M2 (4,3) · M3 (6,3) · M4 (5,5) |
| D | D1 (8,5) · D2 (7,6) · D3 (8,6) · D4 (9,6) · D5 (10,6) · D6 (9,9) |
| T | T1 (4,6) · T2 (5,6) · T3 (6,9) · T4 (10,7) |

S3 nối về N3 bằng đường chéo dài. Nếu layout rối, chuyển S3 sang khối M.

### 7.9 Event (36: 29 trong `vie_nat`, 7 trong `vie_nat_news`)

**Quy ước.**
- Mọi event có `is_triggered_only = yes`. Không có MTTH.
- **Option A luôn là lựa chọn lịch sử hoặc kìm hãm**, và được đặt đầu tiên.
- "Class A" = luôn nổ và đặt `VIE_popup_cd` 45 ngày. "Class B" = chỉ nổ khi không có `VIE_popup_cd`; scheduler thử lại tháng sau. Event do focus hoặc decision gọi thì không cần cooldown.
- Event gửi sang nước khác có `TT_IF_THEY_ACCEPT` / `TT_IF_THEY_REJECT` ở phía gửi, `TT_IF_WE_ACCEPT` / `TT_IF_WE_DECLINE` ở phía nhận (✅ `MD:.claude/docs/event-reference.md:236`), và AI phía nhận có trọng số theo opinion hoặc influence.
- Event mô tả bạo lực viết giọng tin tức trung tính, không mô tả chi tiết, và không có option tán thành bạo lực.
- Tranh: tái sử dụng `GFX_report_event_generic_*` như các event khác của mod. News dùng tranh khổ rộng (❗N-08).
- Mọi option có `log` với đúng ID của option đó.

#### 7.9.1 Đường vào và khởi tạo

| ID | Tên EN / VI | Gọi bởi | Option |
|---|---|---|---|
| `vie_nat.1` | An Extraordinary Plenum / Hội nghị bất thường | Scheduler, đường A (Class B) | **A.** "The Central Committee closes ranks": `VIE_nat_plenum_cd` 730 ngày; `STAB +0.03`; `VIE_bop_conservative_small`. AI 100<br>**B.** "The sovereignty faction takes charge": `VIE_nat_route = 1`; popularity 22 +0,20; `rul_party_temp = 22`; `VIE_transition_regime`. AI 5; ×0 khi `VIE_ai_historical`; ×3 khi `VIE_ai_free`; +150 khi `VIE_AI_PATH_NATIONALIST` |
| `vie_nat.2` | The National Salvation Committee / Ủy ban Cứu quốc | `vie_col.1.c` (đường B), sau 5 ngày | **A.** "The army holds power": `mil +5`. AI 80<br>**B.** "Hand power to the street movement" (trigger: `VIE_d4_street` hoặc `VIE_ax_mob_norm > 8`): popularity 20 +0,20; `rul_party_temp = 20`; `VIE_transition_regime`; `BoP +0.20` ×2. AI 20 |
| `vie_nat.4` | A Sovereignty Party Is Founded / Một đảng chủ quyền ra đời | Scheduler, đường C *(giai đoạn 2)* | Immediate: gỡ cấm đảng 20; popularity 20 +0,04; `set_country_flag = VIE_nat_party_founded`<br>**A.** "It is their right": không thêm gì. AI 70<br>**B.** "Ban it": cấm lại đảng 20; `STAB −0.02`; `ax.civil −1`. AI 30 |
| `vie_nat.9` | Who Leads the Nation? / Ai dẫn dắt dân tộc? | `VIE_nat_regime_init`, sau 1 ngày | Mỗi option đặt `VIE_nat_leader_id` rồi gọi `set_leader_VIE`<br>**A.** Tướng lĩnh (id 1): `mil +5`. AI 70 nếu slot 22, còn lại 20<br>**B.** Nhà hùng biện (id 2): `WS +0.05`. AI 60 nếu slot 20 hoặc 21, còn lại 10<br>**C.** Kỹ trị (id 3): `VIE_nat_sanction_down`. AI 30 |

#### 7.9.2 Những tháng đầu

| ID | Tên EN / VI | Gọi bởi | Option |
|---|---|---|---|
| `vie_nat.10` | The World Reacts / Thế giới phản ứng | Init, sau 7 ngày | Immediate: nếu `has_elections = no` (vào không qua bầu cử) → `VIE_nat_sanction_up`. Nếu có bầu cử (đường C) → chỉ `small_decrease` opinion với USA<br>**A.** "Accept the cost": `WS +0.03`; `BoP +0.05`. AI 50<br>**B.** "A charm offensive": `PP −50`; `VIE_nat_sanction_down`. AI 50 |
| `vie_nat.11` | Capital Flight / Vốn tháo chạy | Init, sau 30 ngày. `trigger`: chưa làm N6 | Immediate: `add_timed_idea VIE_fdi_confidence_shock` 365 ngày; `TREAS −3`<br>**A.** "Impose capital controls": `add_timed_idea VIE_nat_capital_controls` 365 ngày; `BoP +0.05`. AI 50<br>**B.** "Pledge to investors": `PP −50`; thay `VIE_fdi_confidence_shock` bằng bản 180 ngày. AI 50 |
| `vie_nat.12` | The Old Party Goes Underground / Đảng cũ rút vào bí mật | N2, sau 60 ngày | **A.** "Conditional amnesty" *(kìm hãm)*: `BoP −0.05`; `STAB −0.02`. AI 60; slot 21 → 20<br>**B.** "Crackdown": `BoP +0.05`; `STAB +0.02`; `set_country_flag = VIE_nat_elite_split`; `add_timed_idea VIE_civil_unrest_idea` 180 ngày; nếu `mil < 50` thì `mil −5`. AI 40 |
| `vie_nat.13` | The Diaspora Answers / Kiều bào đáp lời | S2 | Một phần cộng đồng hưởng ứng, một phần phản đối<br>**A.** "Open a dialogue with every community" *(kìm hãm)*: `TREAS +2`; `BoP −0.05`. AI 60<br>**B.** "Welcome only our supporters": `WS +0.03`; `BoP +0.05`; `small_decrease` opinion với USA. AI 40 |
| `vie_nat.14` | The Sovereignty Referendum / Trưng cầu dân ý về chủ quyền | V1-3 | **A.** "Call off the vote" *(kìm hãm)*: `PP −25`; `BoP −0.05`. AI 20<br>**B.** (trigger `has_war_support > 0.5`) "A resounding yes": `STAB +0.05`; `PP +50`; `BoP +0.05`. AI 80<br>**C.** (trigger `NOT = { has_war_support > 0.5 }`) "A narrow yes, a divided country": `STAB −0.02`; `PP +25`. AI 80 |

#### 7.9.3 Cực đoan hóa

| ID | Tên EN / VI | Gọi bởi | Option |
|---|---|---|---|
| `vie_nat.15` | The Rally Turns Violent / Cuộc mít tinh thành bạo lực | Decision `VIE_nat_mass_rally`, 15% khi BoP ≥ 0,4 | Immediate: `STAB −0.03`; `add_timed_idea VIE_public_anger` 180 ngày<br>**A.** "Prosecute the instigators" *(kìm hãm)*: `BoP −0.05`; `WS −0.02`. AI 70<br>**B.** "Look the other way": `BoP +0.05`. AI 30 |
| `vie_nat.20` | The Turning Point / Bước ngoặt | `VIE_nat_monthly`, lần đầu BoP ≥ 0,6 và không phải slot 21 (Class A) | Immediate: `set_country_flag = VIE_nat_turning_point_done`<br>**A.** "Restrain the movement" *(kìm hãm)*: `BoP −0.20` rồi `−0.10`; `WS −0.05`; `mil +5`. AI 100<br>**B.** "Embrace it" (trigger `VIE_nat_radical_turn_allowed`): popularity 21 +0,20; `rul_party_temp = 21`; `VIE_transition_regime` (tự gọi `VIE_nat_on_variant_change`: cosmetic, trừng phạt, news). AI 5; ×0 khi `VIE_ai_historical`; ×6 khi `VIE_ai_free`; +150 khi `VIE_AI_PATH_NAT_RADICAL` |
| `vie_nat.21` | The Moderates Object / Phe ôn hòa phản đối | V3-1, sau 30 ngày | Immediate: `mil −10`<br>**A.** "Concede to the army" *(kìm hãm)*: `mil +10`; `BoP −0.10`. AI 50<br>**B.** "Sideline them": `BoP +0.05`; `set_country_flag = VIE_nat_elite_split`. AI 50 |
| `vie_nat.22` | The Purge Runs Its Course / Cuộc thanh trừng đi đến cùng | V3-4, sau 90 ngày | **A.** "Stop the purge" *(kìm hãm)*: `STAB +0.03`; `mil +5`. AI 60<br>**B.** "Widen the purge": `PP +50`; `mil −10`; `BoP +0.05`. AI 40 |
| `vie_nat.25` | "Bach Viet" Talk on the Fringe / Diễn ngôn "Bách Việt" bên lề **[FR]** | `VIE_nat_monthly`: slot 21, BoP ≥ 0,8, 5%/tháng, một lần | Mô tả: một trào lưu trên mạng đòi các vùng đất phía nam Trung Quốc, dựa trên cách hiểu "Bách Việt"; **chưa từng là chính sách của bất kỳ nhà nước Việt Nam nào**. Immediate: `VIE_nat_fringe_done`<br>**A.** "Disown it" *(kìm hãm)*: `BoP −0.10`; `WS −0.03`. AI 70<br>**B.** "Let the movement keep its slogans": **không có claim, core hay wargoal**; opinion `VIE_nat_irredentist_rhetoric` −50 từ CHI; `VIE_nat_sanction_up`; `BoP +0.10`; `WS +0.05`; `CHI = { country_event vie_nat.32 }`. AI 30; +50 khi `VIE_AI_PATH_NAT_RADICAL` |

#### 7.9.4 Event bạo lực bài ngoại: `vie_nat.30` và phản ứng

Đây là event nhạy cảm nhất. Nó thể hiện **hậu quả** của cực đoan hóa, không phải phần thưởng. Mô hình tham chiếu là bạo loạn tháng 5/2014, khi các nhà máy của doanh nghiệp Đài Loan, Trung Quốc và các nước khác ở Bình Dương và Hà Tĩnh bị tấn công **[LS]**.

| Mục | Nội dung |
|---|---|
| Gọi bởi | `VIE_nat_monthly`, xác suất ở 7.6 bước 4 (Class A) |
| Tiêu đề | "Riots at Foreign-Owned Factories" / "Bạo loạn tại các nhà máy vốn nước ngoài". **Không** định danh nạn nhân theo sắc tộc |
| Mô tả | Giọng tin tức. Có một câu trung tính nhắc rằng những vụ việc tương tự đã xảy ra năm 2014 |
| Immediate | `STAB −0.05`; `TREAS −3`; `add_timed_idea VIE_fdi_confidence_shock` 730 ngày (thay bản cũ nếu có); `VIE_nat_violence_cd` 730 ngày; `news_event vie_nat_news.3`; `CHI = { country_event vie_nat.31 }` |
| **A** | "Deploy security forces and prosecute the perpetrators" *(kìm hãm)*: `BoP −0.10`; `WS −0.05`. Nếu đã làm S4: thay `VIE_fdi_confidence_shock` bằng bản 365 ngày. AI 70; slot 21 → 30 |
| **B** | "Blame foreign agitators": `WS +0.05`; `BoP +0.05`; `VIE_nat_sanction_up`. AI 30 |
| Giới hạn cứng | Không có event tiếp theo nào leo thang thành trục xuất, tịch thu theo sắc tộc hay thanh lọc. Không có option nào tán thành bạo lực |

| ID | Tên EN / VI | Nước nhận | Option |
|---|---|---|---|
| `vie_nat.31` | Our Citizens Were Attacked in Vietnam / Công dân của ta bị tấn công ở Việt Nam | CHI (từ `vie_nat.30`) | **A.** "Lodge a formal protest": `FROM` nhận opinion `VIE_nat_citizens_attacked`. AI 70<br>**B.** "Prepare a response": `create_wargoal = { type = take_state_focus target = FROM generator = { 801 } }` với `add_threat_from_wargoal_effect` (❗N-06). AI 30; ×2 nếu `FROM` đã làm `VIE_paracel_ultimatum`; ×1,5 nếu opinion của CHI với FROM < −50; ×0 nếu CHI đang có chiến tranh |
| `vie_nat.32` | Irredentist Rhetoric in Hanoi / Lời lẽ đòi đất ở Hà Nội | CHI (từ `vie_nat.25.b`) | Như `vie_nat.31`; AI B 40 |

#### 7.9.5 Cô lập, quân đội và kế vị

| ID | Tên EN / VI | Gọi bởi | Option |
|---|---|---|---|
| `vie_nat.35` | Sanctions Tighten / Trừng phạt siết chặt | `VIE_nat_monthly` (slot 21, BoP ≥ 0,6, 3%/tháng) (Class B) | Immediate: `VIE_nat_sanction_up`<br>**A.** "A diplomatic concession" *(kìm hãm)*: `PP −75`; `VIE_nat_sanction_down`; `BoP −0.05`. AI 40<br>**B.** "Endure": `WS +0.03`. AI 60 |
| `vie_nat.40` | The Army Acts / Quân đội hành động | Mission `VIE_nat_coup_looming` hết hạn; `vie_nat.53.a` | Một option. Slot 20 hoặc 21: `VIE_nat_leader_id = 4`; popularity 22 +0,20; `rul_party_temp = 22`; `VIE_transition_regime`; đặt BoP về −0,3 (❗N-15); `STAB −0.05`; `mil +10`. Slot 22: `VIE_nat_leader_id` đổi (khác 4 → 4; là 4 → 1); `set_leader_VIE`; `STAB −0.10` |
| `vie_nat.41` | A Return to Civilian Rule? / Trở lại chính quyền dân sự? | Mission `VIE_nat_civilian_roadmap` thành công | **A.** "Hand power back to a reformed Party": `rul_party_temp = 19`; `VIE_transition_regime` (tự dựng lại BoP của Đảng và lãnh đạo hư cấu `VIE_create_leader_restored_party`); `news_event vie_nat_news.5`. AI 50<br>**B.** "Round-table and elections" (trigger: đã làm S6): `rul_party_temp = 13`; `VIE_transition_regime`; `set_country_flag = VIE_democracy_path_open` (như `vie_col.6.a`); `news_event vie_nat_news.5`. AI 30<br>**C.** "Not yet": `mil +5`; `VIE_nat_sanction_up`. AI 20 |
| `vie_nat.42` | The Succession Question / Vấn đề kế vị | `VIE_nat_monthly`: slot 21, sau 10 năm | Immediate: `STAB −0.08`; `mil −10`<br>**A.** "A collective leadership" *(kìm hãm)*: `BoP −0.15`; `VIE_nat_leader_id = 6`; `set_leader_VIE`. AI 50<br>**B.** "The heir apparent": `PP +50`; `BoP +0.05`; `VIE_nat_leader_id = 5`; `set_leader_VIE`. AI 50 |

#### 7.9.6 Lãnh thổ và ngoại giao

| ID | Tên EN / VI | Gọi bởi / nước nhận | Option |
|---|---|---|---|
| `vie_nat.50` | Beijing Issues a Warning / Bắc Kinh cảnh cáo | N9 nếu đã làm `VIE_assert_maritime_rights` | **A.** "Lower our voice" *(kìm hãm)*: `BoP −0.05`; `WS −0.03`. AI 60<br>**B.** "Answer in kind": `WS +0.05`; `BoP +0.05`; `add_timed_idea VIE_china_pressure_idea` 365 ngày. AI 40 |
| `vie_nat.51` | Shots in the Paracels / Tiếng súng ở Hoàng Sa | `VIE_nat_monthly`, lần đầu có chiến tranh với CHI (Class A) | Một option: `WS +0.05` |
| `vie_nat.52` | The Paracels Are Ours / Hoàng Sa về ta | `VIE_nat_monthly`: sở hữu 813 | Một option: `WS +0.10`; `STAB +0.05`; `BoP +0.10`; `news_event vie_nat_news.4` |
| `vie_nat.53` | Defeat at Sea / Thất bại trên biển | `VIE_nat_monthly`: chiến tranh với CHI kết thúc, không sở hữu 813 | Immediate: `WS −0.15`; `STAB −0.10`; `mil −15`; `BoP −0.20`<br>**A.** "The leadership resigns": slot 20/21 → `country_event vie_nat.40`; slot 22 → đổi lãnh đạo như `vie_nat.40`. AI 60<br>**B.** "Cling to power": `mil −10`; `VIE_nat_sanction_up`. AI 40 |
| `vie_nat.55` | A Protectorate Offer from Hanoi / Lời đề nghị bảo hộ từ Hà Nội | LAO hoặc CBD (decision `VIE_nat_offer_protectorate`) | **A.** Chấp nhận: `FROM = { puppet = ROOT }`. AI: LAO 60, CBD 20; ×0,5 nếu opinion với FROM < 50; ×1,5 nếu ảnh hưởng của FROM ≥ 60%<br>**B.** Từ chối: nếu ROOT là CBD thì FROM nhận opinion `VIE_nat_old_wounds`. Mô tả của CBD nhắc giai đoạn 1979–1989 **[LS]** |
| `vie_nat.56` | The Mainland Security Pact / Hiệp ước an ninh lục địa | LAO (D5) | **A.** Gia nhập faction của FROM. AI 50 + 20 nếu `influence_higher_40`; ×0,5 nếu opinion với FROM < 25<br>**B.** Từ chối |
| `vie_nat.60` | Access to Cam Ranh / Quyền tiếp cận Cam Ranh | USA (D2) | **A.** Chấp nhận: `FROM = { give_military_access = ROOT }`; opinion hai chiều `small_increase`. AI 70; ×0 nếu FROM là slot 21 hoặc có `international_sanctions` trở lên<br>**B.** Từ chối |
| `vie_nat.61` | An Arms Pact with Hanoi / Hiệp ước vũ khí với Hà Nội | SOV (D3) | **A.** Chấp nhận: trong scope FROM, `add_tech_bonus` 25% cho `CAT_submarines` và `CAT_medium_aircraft` (✅ category có trong `MD:common/technology_tags/`), `TREAS −3`; ROOT `TREAS +2`. AI 70<br>**B.** Từ chối |

#### 7.9.7 News event (`vie_nat_news`)

Mỗi news có ba option theo trigger loại trừ lẫn nhau: VIE; nước ở châu Á; phần còn lại (✅ `MD:.claude/docs/event-reference.md:158`).

| ID | Nội dung |
|---|---|
| `vie_nat_news.1` | Việt Nam thành lập Chính phủ Cứu quốc (thay đổi chế độ) |
| `vie_nat_news.2` | Chế độ Hà Nội chuyển sang cực đoan |
| `vie_nat_news.3` | Bạo loạn tại các nhà máy vốn nước ngoài ở Việt Nam; giới đầu tư rút lui |
| `vie_nat_news.4` | Việt Nam giành lại Hoàng Sa |
| `vie_nat_news.5` | Việt Nam trở lại chính quyền dân sự |
| `vie_nat_news.6` | Việt Nam rút khỏi ASEAN |
| `vie_nat_news.7` | Việt Nam đòi các đảo Trường Sa bằng vũ lực |

**So với báo cáo:** bảng ánh xạ ID đầy đủ ở Phụ lục A.2. Ba event bị bỏ hẳn: `.3` "The Streets Rise" (thay bằng option c của `vie_alt.1` và hệ sụp đổ), `.32` "Arms Embargo" (I-12), `.54` "ASEAN Responds" (thành hiệu ứng trực tiếp và news `.7`).

### 7.10 Decision và mission (14 decision, 3 mission)

**Category** (file `VIE_md_categories_nat.txt`; `allowed = { original_tag = VIE }` chỉ đặt ở category, không lặp ở decision):

| Category | `visible` | Mở bởi |
|---|---|---|
| `VIE_nat_cat_regime` "Chính quyền Cứu quốc" | `VIE_nat_regime_active` | N1 (`unlock_decision_category_tooltip`) |
| `VIE_nat_cat_sphere` "Chủ quyền và vùng ảnh hưởng" | `VIE_nat_regime_active` và đã làm T2, T3 hoặc T4 | T2, T3, T4 |

**Decision** (mọi decision lặp lại có ngẫu nhiên đặt `fixed_random_seed = no`; mọi khối hiệu ứng mở đầu bằng `log`):

| # | ID | Category | `visible` / `available` | Chi phí | Hiệu ứng | Lặp lại | AI |
|---|---|---|---|---|---|---|---|
| 1 | `VIE_nat_mass_rally` | regime | Đã làm N4 | 50 PP | `WS +0.04`; `BoP +0.05`; nếu BoP ≥ 0,4 thì `random = { chance = 15 }` → `vie_nat.15` | 90 ngày | 50 khi `WS < 0.5`; slot 21 → 80 |
| 2 | `VIE_nat_mobilize_militia` | regime | Đã làm M2; `has_war = yes` | `custom_cost_trigger`: `has_war_support > 0.15` | `add_war_support = −0.08`; `add_timed_idea VIE_nat_militia_mobilized` 180 ngày | 180 ngày | 80 khi có chiến tranh |
| 3 | `VIE_nat_patriotic_bonds` | regime | Đã làm V1-6 | `custom_cost_trigger`: `has_war_support > 0.2` | `add_war_support = −0.06`; `TREAS +3` | 365 ngày | 80 khi `treasury < 1` |
| 4 | `VIE_nat_pay_the_generals` | regime | Có `the_military` | `custom_cost_trigger`: `treasury > 2` | `TREAS −2`; `mil +10` | 180 ngày | 90 khi `mil < 45`. Bankruptcy guard |
| 5 | `VIE_nat_rotate_commanders` | regime | Mission đảo chính đang chạy | 75 PP | `mil +8`; `STAB −0.02`; `army_experience = −10` | 365 ngày | 100 khi mission đang chạy |
| 6 | `VIE_nat_restrain_radicals` *(kìm hãm)* | regime | BoP > 0,2 | 75 PP | `BoP −0.10`; `WS −0.03` | 180 ngày | 80 khi BoP ≥ 0,5 và không phải slot 21; slot 21 → 5 |
| 7 | `VIE_nat_purge_disloyal` | regime | Slot 21 | 50 PP | `BoP +0.10`; `mil −8`; `STAB −0.02` | 180 ngày | 20; `VIE_AI_PATH_NAT_RADICAL` → 50 |
| 8 | `VIE_nat_amnesty` *(kìm hãm)* | regime | — | 60 PP | `STAB +0.03`; `BoP −0.05`; gỡ `VIE_civil_unrest_idea` nếu có | 365 ngày | 40 |
| 9 | `VIE_nat_charm_offensive` | regime | `VIE_nat_has_sanctions`; available BoP < 0,6 | 100 PP | `VIE_nat_sanction_down` | 365 ngày | 60 |
| 10 | `VIE_nat_sanctions_evasion` | regime | Có `Western_Sanctions` trở lên | 50 PP, `custom_cost_trigger` `treasury > 1` | `TREAS −1`; `add_timed_idea VIE_nat_sanctions_evasion` 365 ngày; `BoP +0.02` | 365 ngày | 50 |
| 11 | `VIE_nat_core_paracels` | sphere | Đã làm T2; sở hữu và kiểm soát 813; `813 = { compliance > 79 }` (❗N-03) | 100 PP | `813 = { add_core_of = ROOT }` | Một lần | 100 |
| 12 | `VIE_nat_core_spratly_state` | sphere | `state_target = yes`; `target_array = owned_states`; `target_trigger`: FROM là 526, 802 hoặc 816, do ROOT sở hữu, `compliance > 79` | 100 PP | `FROM = { add_core_of = ROOT }` | Một lần mỗi state | 100 |
| 13 | `VIE_nat_press_spratly_claim` | sphere | Đã làm T3; `targets = { CHI PHI MAY TAI }`; `target_trigger`: FROM sở hữu 526, 802 hoặc 816; không đang có chiến tranh với FROM | 50 PP | `set_temp_variable = { wargoal_on = FROM }`; `add_threat_from_wargoal_effect`; `create_wargoal` loại `take_state_focus`, `generator = { 526 802 816 }` (❗N-06); `VIE_nat_sanction_up`. Nếu FROM có `ASEAN_Member`: mọi nước trong `global.ASEAN_Member` −25 opinion với ROOT; `news_event vie_nat_news.7` | 365 ngày mỗi mục tiêu | 0; `VIE_AI_PATH_NAT_RADICAL` → 20 nếu (FROM là PHI hoặc MAY và `strength_ratio` > 1,5) hoặc (FROM là CHI và `strength_ratio` > 0,4) |
| 14 | `VIE_nat_offer_protectorate` | sphere | Đã làm T4; `targets = { LAO CBD }`; `target_trigger`: `FROM = { influence_higher_50 = yes }`, FROM chưa là subject | 150 PP | `FROM = { country_event vie_nat.55 }` với `TT_IF_THEY_ACCEPT` / `TT_IF_THEY_REJECT` | 365 ngày mỗi mục tiêu | 30 |

**Mission:**

| ID | Kích hoạt | Thời hạn | Thành công (`available`, ❗N-04) | Hết hạn (`timeout_effect`) |
|---|---|---|---|---|
| `VIE_nat_consolidation_deadline` | `activate_mission` trong `VIE_nat_regime_init` | 540 ngày | Đã làm N9 → `STAB +0.02` | `STAB −0.08`; `mil −10` |
| `VIE_nat_coup_looming` | `activation`: `VIE_nat_regime_active`, có `the_military`, `mil < 35` | 180 ngày | `mil > 44` | `country_event vie_nat.40` |
| `VIE_nat_civilian_roadmap` | `activate_mission` từ V2-5a | 730 ngày | `has_stability > 0.5` và BoP < −0,19 → `country_event vie_nat.41` | "Các tướng lặng lẽ gác lại lộ trình": `BoP +0.05`; `VIE_nat_sanction_up` |

Cả ba mission có `visible = { VIE_nat_regime_active = yes }` và `cancel_if_not_visible = yes`, để tự hủy khi rời chế độ. `is_good = no` cho mission đảo chính.

**Bỏ so với báo cáo:** `national_day_parade` (trùng mít tinh), `partner_economic_zone` (gộp vào D2 và D3), `rename_southern_coast` và `military_administration` (tầng 3 bị bỏ, I-09), `puppet_laos` và `puppet_cambodia` (gộp thành decision nhắm mục tiêu số 14, đi qua event để nước nhận có quyền quyết định), `campaign_rally` và `sovereignty_platform` (đường C chuyển giai đoạn 2).

### 7.11 AI

#### 7.11.1 Game rule (H8)

Không tạo rule mới. Thêm hai option vào `VIE_ai_behavior` (✅ `mod:common/game_rules/VIE_md_rules.txt:28`) và đặt cờ trong `on_startup` theo đúng mẫu có sẵn (✅ `mod:common/on_actions/VIE_md_on_actions_startup.txt`):

| Option | Cờ đặt | Hành vi AI |
|---|---|---|
| `VIE_NATIONALIST` | `VIE_AI_PATH_NATIONALIST` | Đi đường A hoặc B vào slot 22. Ưu tiên V2-5a, D2, T1, S4. Từ chối Bước ngoặt |
| `VIE_NATIONALIST_RADICAL` | `VIE_AI_PATH_NATIONALIST` + `VIE_AI_PATH_NAT_RADICAL` | Như trên, nhưng chọn "Embrace" ở `vie_nat.20`, đi V3, D4, D6, T3 |
| `RANDOM` (sửa) | — | Thêm `5 = VIE_AI_PATH_NATIONALIST` và `3 = cả hai cờ`; giảm ô trống từ 45 xuống 37 |

Lưu ý tác dụng phụ: trigger có sẵn `VIE_ai_path_security` đã đọc `VIE_AI_PATH_NATIONALIST` (✅ `mod:common/scripted_triggers/VIE_md_triggers_p4.txt:53`), nên option mới cũng nới cửa D3 (An ninh) cho AI. Chấp nhận được, vì đó cũng là quỹ đạo cứng rắn. Focus `VIE_assert_maritime_rights` đã có `+150` với cờ này; trước đây cờ không bao giờ được đặt.

#### 7.11.2 Quy tắc AI

1. **Cửa vào**: mọi option chuyển chế độ có `factor = 0` khi `VIE_ai_historical`, `×3` (hoặc theo bảng) khi `VIE_ai_free`, `+150` khi có cờ đường tương ứng.
2. **Trong chế độ**: trunk N, S, M1–M3 có trọng số dương **bất kể** game rule, vì chế độ đã xảy ra (ví dụ do sụp đổ) và AI phải chơi được nó.
3. **Leo thang** (option B của `vie_nat.20`, V3, D6, T3, decision 7, decision 13): `base` thấp, chỉ tăng mạnh với `VIE_AI_PATH_NAT_RADICAL`.
4. **Không tự sát**: decision 13 chỉ được AI chọn khi `VIE_nat_leader_is_ai_safe`. `VIE_paracel_ultimatum` trong cây chính đã có `base = 0`; giữ nguyên.
5. **Phanh**: `VIE_nat_restrain_radicals` có trọng số 80 khi BoP ≥ 0,5 và không phải slot 21. `VIE_nat_pay_the_generals` và `VIE_nat_rotate_commanders` ưu tiên cao khi `mil` thấp.
6. **Tiền**: focus và decision tiêu tiền có bankruptcy guard.
7. **Không dùng `add_ai_strategy`** trong effect (✅ `MD:.claude/docs/content-guidelines.md`, AI).
8. **Nước khác**: `vie_nat.31`, `.32` (CHI), `.55`, `.56` (LAO, CBD), `.60` (USA), `.61` (SOV) đều có trọng số theo opinion hoặc influence (7.9).

### 7.12 Hành vi Historical và Non-Historical

Theo quy ước của mod (✅ `mod:common/scripted_triggers/VIE_md_triggers_p4.txt:1–4`): **game rule chỉ ràng buộc AI**. Người chơi luôn có quyền chọn, trừ khi trigger của option không thỏa. Chế độ `free` nới ngưỡng cho cả người chơi và AI. `is_historical_focus_on` được tính như `historical`.

| Tình huống | AI, `historical` | AI, `plausible` (mặc định) | AI, `free` | Người chơi (mọi rule) |
|---|---|---|---|---|
| Đường A (`vie_nat.1.b`) | Không bao giờ | 5 trên 105, chỉ khi gate thỏa | ×3, gate nới | Chọn được khi gate thỏa |
| Đường B (`vie_col.1.c`) | Không bao giờ | 3 trên 103 | ×3 | Chọn được |
| Đường C | Không áp dụng (giai đoạn 2) | — | — | — |
| Đường D (`vie_alt.1.c`, rồi sụp đổ) | Không bao giờ | 3 trên 103 | ×3 | Chọn được |
| Bước ngoặt "Embrace" | Không bao giờ | 5 trên 105 | 30 trên 130 | Chọn được khi `VIE_nat_radical_turn_allowed` |
| Tầng [FR] `vie_nat.25.b` | Không tới được (slot 21 không xảy ra với AI) | 30 | 30 | Chọn được |
| Bạo lực `vie_nat.30` | Có thể xảy ra nếu đã ở chế độ | Có thể | Có thể | Có thể (là hậu quả, không phải lựa chọn) |
| CHI tạo wargoal (`.31.b`) | Có (AI của CHI) | Có | Có | Người chơi CHI tự quyết |
| Kịch bản kiểm thử số 1 (mục 7.16) | VIE không bao giờ vào dải | — | — | — |

**Nhãn nội dung** không phụ thuộc game rule: mọi focus mang `$VIE_nat_ah_note$`; tầng 3 mang nhãn [FR].

### 7.13 Quy tắc nội dung, localisation và cờ

#### 7.13.1 Quy tắc cứng (developer không được vi phạm)

| # | Quy tắc | Cách kiểm tra |
|---|---|---|
| R1 | Không focus, decision hay option nào thưởng cho việc đàn áp một nhóm sắc tộc hay tôn giáo | Review mọi `completion_reward` và option có từ khóa đàn áp hoặc thanh trừng; thanh trừng chỉ nhắm "phe ôn hòa" (chính trị) và luôn trả bằng quân đội và ổn định |
| R2 | Bạo lực bài ngoại chỉ là hậu quả ngoài ý muốn (`vie_nat.30`). Không có chuỗi leo thang tới trục xuất, tịch thu theo sắc tộc hay thanh lọc | Không event nào được gọi từ option của `vie_nat.30`, trừ news và event gửi CHI |
| R3 | Mọi tầng có lựa chọn kìm hãm | Trunk: N6. V1: V1-5a. V2: V2-5a. V3: không có focus kìm hãm (có chủ đích), nhưng có `vie_nat.21.a`, `.22.a`, `.25.a`, `.42.a` và decision 6, 8. S: S4, S5, S6. T: T1 |
| R4 | Tầng 3 không có claim, core, wargoal hay đổi tên | Grep `534`, `574` trong file mới: phải bằng 0 |
| R5 | Không dùng tên người thật còn sống làm lãnh đạo | Đối chiếu 6 tên ở 7.6 trước khi merge |
| R6 | Không dùng cờ của tổ chức lịch sử có thật | Cosmetic tag riêng (7.13.3) |
| R7 | Nhãn **[AH]** trên mọi focus; **[FR]** trên tầng 3; **[LS]** cho tham chiếu có thật | Grep: mọi khóa `VIE_nat_*_desc` của focus phải chứa `$VIE_nat_ah_note$`. Nên thêm kiểm tra này vào `tools/verify_all_loc.py` |
| R8 | Tích sử (Diên Hồng, Nam quốc sơn hà, Đông Du) là di sản chung; dùng không hàm ý nhân vật lịch sử ủng hộ chế độ giả tưởng | Dòng miễn trừ trong mô tả N1 |

#### 7.13.2 Localisation

- Tiếng Anh ở `localisation/english/VIE_md_nat_l_english.yml` (UTF-8 có BOM, khoảng trắng đầu dòng, theo `MD:.claude/docs/localisation-rules.md`). Tiếng Việt ở `localisation/english/replace/VIE_md_vi_nat_l_english.yml`, như cách mod đang làm.
- Tiêu đề focus không có mã màu `§`. Mô tả chỉ dùng `§Y`, `§G`, `§R`.
- Khóa dùng chung: `VIE_nat_ah_note` = "§YLịch sử giả định:§! chế độ này không tồn tại trong lịch sử Việt Nam." (bản tiếng Anh: "§YAlternate history:§! no such regime has existed in Vietnam."). `VIE_nat_fr_note` cho tầng 3. `VIE_nat_disclaimer` cho N1.
- **Tên đảng.** Slot 22: ghi đè `VIE.Nat_Autocracy` trong `replace/` (MD đã có hook). Tên đề xuất: "Hội đồng Cứu quốc" (EN: "National Salvation Council"). Slot 20 và 21: MD chưa có hook VIE (❗N-02). Nếu không thêm được hook, chấp nhận tên generic "Right Wing Populists" / "Fascists" trong giao diện chính trị ở bản đầu, và dùng tên riêng trong mô tả focus và event.
- **Tên nước theo cosmetic tag** (❗N-07 định dạng khóa): `VIE_NAT_nationalist` = "Vietnam"; `VIE_NATR_nationalist` = "Vietnamese National State" / "Nhà nước Quốc gia Việt" **[AH]**.

#### 7.13.3 Cờ

| Cosmetic tag | Dùng cho | Cờ |
|---|---|---|
| `VIE_NAT` | Slot 20, 22 | **Giữ quốc kỳ hiện hành** (sao vàng nền đỏ). Chính quyền cứu quốc xuất phát từ bên trong nhà nước nên giữ quốc kỳ; không cần vẽ mới. Tạo `VIE_NAT_nationalist.tga` (+ `medium/`, `small/`) bằng cách sao chép `VIE_AUTH_S.tga` của MD |
| `VIE_NATR` | Slot 21 | **Thiết kế nguyên bản** (việc của họa sĩ). Không lấy cảm hứng từ cờ của tổ chức có thật, gồm cả cờ Đại Việt, VNQDĐ, VNCH. Khi chưa có tranh, tạm dùng bản sao quốc kỳ |

`VIE_nat_regime_exit` trả về `VIE_AUTH_S` (quy tắc MD: bỏ cosmetic tag khi không còn phù hợp).

### 7.14 Dependency cần kiểm tra trong MD (NEED_VERIFY)

| Mã | Điểm cần kiểm tra | Cách kiểm tra | Phương án dự phòng |
|---|---|---|---|
| N-01 | `shared_focus = X` trong `focus_tree` có kéo theo **toàn bộ chuỗi** shared focus có prerequisite trỏ về X không; `relative_position_id` giữa các shared focus có hoạt động không | Tạo 3 shared focus thử, mở cây trong game | Viết dải trực tiếp trong `VIE_md_focus.txt` |
| N-02 | Có thể thêm dòng VIE vào `defined_text` `Nat_Populism_L`, `Nat_Fascism_L` (+ `_desc`, `_icon`) của MD mà không chép lại cả file không. Hai `defined_text` cùng tên sẽ ra sao | Đọc `error.log` sau khi thêm một file scripted_localisation trùng tên | Tên generic (7.13.2) |
| N-03 | `compliance` trên state `state_inhospitable` không dân (813) có tăng tới 80 không | Chiếm 813 bằng console, chờ | Thay bằng "sở hữu liên tục 365 ngày" (flag có `days`) |
| N-04 | Mission hoàn thành khi `available` đúng (ngữ nghĩa vanilla) | Thử với mission đảo chính | Dùng `cancel_trigger` + `cancel_effect` |
| N-05 | `start_civil_war` với ideology trùng ideology chính phủ | Chỉ cần nếu H3 thất bại | H3 buộc phe nổi dậy là 13 khi đang ở dải |
| N-06 | `take_state_focus` có sẵn cho CHI→VIE và VIE→PHI/MAY/TAI; `generator` có lọc theo state mà mục tiêu sở hữu không | Console: `create_wargoal` thử | Tách decision theo từng state |
| N-07 | Định dạng khóa tên nước theo cosmetic tag; có cần dòng màu trong `common/countries/cosmetic.txt` không (file này của MD là một file duy nhất) | Đặt cosmetic tag bằng console | Không đặt màu riêng |
| N-08 | Tên sprite cho icon hai phía BoP, icon category, và tranh event/news có kích thước đúng | Grep `interface/*.gfx` của MD | Dùng icon generic đã dùng trong `VIE_md_bop.txt` |
| N-09 | MD có opinion modifier dùng khi rời ASEAN không | Grep `BRM_leave_asean` hậu quả | Tạo `VIE_nat_left_asean` |
| N-11 | Đồng hồ kế vị 10 năm bằng flag có `days = 3650` | Kiểm tra flag còn sau save/load | Biến lưu ngày bắt đầu |
| N-12 | Chuỗi `vie_alt.12–14` được gọi từ đâu | Grep: hiện **không có nơi gọi** | Đường C chờ tới khi con đường dân chủ được nối dây |
| N-13 | Danh sách province giáp CHI trong 523 và 524 | Đọc `map/definition.csv` và `adjacencies` | Xây ở mọi province của hai state |
| N-14 | Vùng canvas trống bên phải dải An ninh | `tools/layout_applier.py` | Đặt dải dưới cùng cây |
| N-15 | `set_power_balance` trên BoP đang tồn tại có đặt lại giá trị không | Console | `add_power_balance_value` với phần chênh lệch tính trước |
| N-16 | Ba idea trừng phạt trong `MD:common/ideas/Burmese.txt` không bị giới hạn tag ở cấp category | Đọc đầu file | Chỉ dùng `international_sanctions` (trong `Various.txt`) |
| N-17 | `has_power_balance = { id = … }` có thay được flag `VIE_bop_nat_active` không (MD dùng ở `05_iran.txt:5057`) | Đọc `05_iran.txt` | Giữ flag theo mẫu của mod |

**Đã xác minh (không cần kiểm tra thêm):** party slot 20/21/22; VIE ruling party 19; `change_ruling_party_effect`; `ban_party_scripted_call`; `set_partyall_banned` (+ `free_ban_parties`); `set_elections_with_frequency`; `influence_higher_*`; `change_influence_percentage`; `ASEAN_Member`; thang trừng phạt; `the_military` và opinion effect; trait lãnh đạo; category công nghệ; `bunker`; `decrease_social_spending`, `increase_education_budget`, `increase_policing_budget`, `increase_military_spending`; `faction_template_generic_regional_security`; `strength_ratio`; `custom_cost_trigger`; `power_balance_weekly`; state 526, 801, 802, 813, 816, 534, 574; cờ VIE trong MD.

### 7.15 Thứ tự triển khai

Mỗi giai đoạn kết thúc bằng `tools/check_static.py`, `tools/verify_all_loc.py`, `tools/audit_mod.py`, rồi chạy game và đọc `error.log` như `tools/TESTING.md` hướng dẫn (tìm `VIE`, `vie_`, `power_balance`).

| Giai đoạn | Nội dung | Kiểm tra |
|---|---|---|
| P0 Hạ tầng | Trigger 7.5; effect skeleton (init, exit, sanction up/down, BoP helper); BoP; H1, H6, H7; biến `VIE_nat_leader_id` | Console: `set_temp_variable rul_party_temp = 22` + `VIE_transition_regime` → thấy BoP, lãnh đạo hư cấu, cosmetic tag; đổi về 19 → mọi thứ gỡ sạch |
| P1 Vào chế độ và trunk | Đường A (`vie_nat.1`, scheduler, H2 option b), đường B (H4, `vie_nat.2`); trunk N; nhánh S; event `.9–.13`; mission củng cố | Ép gate bằng console; mission hết hạn đúng |
| P2 Biến thể | V2 + mission đảo chính + `.40`, `.41`, mission lộ trình; V1 + `.14`; | Kịch bản 2, 3 |
| P3 Đối ngoại, quân sự | M, D, T1, T2, T4; event chéo nước `.55`, `.56`, `.60`, `.61` | Người chơi LAO nhận được event, AI trả lời theo trọng số |
| P4 Cực đoan | Trôi BoP; `.20`, V3, `.21`, `.22`, `.30`, `.31`, `.25`, `.32`, `.35`, `.42`; T3; D6; H5 | Kịch bản 4, 5, 6 |
| P5 Decision, AI, nội dung | 14 decision; game rule H8; localisation; cờ | Kịch bản 1 (observe) |
| P6 Đường D | `vie_alt.1.c` (H2), H3 | Kịch bản 8 |
| P7 Đường C | Chờ N-12 | — |

### 7.16 Kịch bản kiểm thử

| # | Kịch bản | Kết quả mong đợi |
|---|---|---|
| 1 | Rule `historical`, observe 2000–2035 | VIE không bao giờ vào dải; không có `vie_nat.*` trong log ngoài scheduler |
| 2 | Ép đường A (console), chơi V2, chọn V2-5a, giữ ổn định > 50% và BoP < −0,2 | Mission lộ trình thành công → `vie_nat.41`; chọn A → slot 19, BoP của Đảng xuất hiện, lãnh đạo "Đảng phục hồi", cosmetic `VIE_AUTH_S`, idea chế độ bị gỡ |
| 3 | Ép slot 20 (console), để `mil` xuống dưới 35 | Mission đảo chính kích hoạt; hết hạn → slot 22, BoP −0,3, focus V1 đang làm dở bị hủy, charter đổi sang `guardian` |
| 4 | Đẩy BoP ≥ 0,6 với trục thỏa `VIE_nat_radical_turn_allowed` | `vie_nat.20` nổ một lần; B → slot 21, cosmetic `VIE_NATR`, trừng phạt tăng một bậc, news `.2`; V1/V2 hết khả dụng |
| 5 | `vie_nat.30` có và không có S4, ở BoP 0,3 và 0,7 | Tần suất khớp 7.6; CHI nhận `.31`; không có event leo thang nào khác; `VIE_fdi_confidence_shock` được tính trong `VIE_crisis_count_ge_2` |
| 6 | Làm T1 rồi thử T3 | T3 bị khóa (ME) |
| 7 | Đổi biến thể khi đang làm dở một focus V | Focus bị hủy (`cancel_if_invalid`); không có focus nào của biến thể cũ còn chọn được |
| 8 | Đường D: `vie_alt.1.c`, rồi ép sụp đổ (stability −0,9 + 2 idea khủng hoảng) | Phe nổi dậy là 20; nếu phe này thắng: init route 4, BoP +0,3, scheduler chạy cho tag mới |
| 9 | Ở dải, đẩy BoP > 0,85 và ổn định < 20% với 2 idea khủng hoảng | `VIE_collapse_check` nổ; phe nổi dậy là 13 (H3) |
| 10 | Thua chiến tranh với CHI | `vie_nat.53`; A → đảo chính |
| 11 | Rời dải bằng bất kỳ cách nào | BoP bị gỡ, idea chế độ bị gỡ, cosmetic trả về, mission tự hủy |
| 12 | Save/load giữa chế độ | `VIE_nat_leader_id` giữ nguyên; lãnh đạo không bị thay bằng lãnh đạo ngẫu nhiên |

---

## Phụ lục A: Ánh xạ từ báo cáo sang đặc tả

### A.1 Focus (88 → 49)

| Báo cáo | Kết quả | Lý do |
|---|---|---|
| N01–N08, N10 | N1–N9 | Giữ; N09 "Nam quốc sơn hà" gộp vào mô tả N4 |
| V1-01, 02, 03, 04, 07, 08, 10 | V1-1, 2, 3, 4, 5a, 5b, 6 | Giữ |
| V1-05 Media under One Voice | Bỏ | Chỉ cộng `drift_defence` |
| V1-06 Rally the Streets | Bỏ | Thành decision `VIE_nat_mass_rally` |
| V1-09 Patriotic Business Pact | Bỏ | Chỉ cộng opinion và modifier |
| V2-01–04, 07, 08, 10 | V2-1–4, 5a, 5b, 6 | Giữ |
| V2-05 Developmental Nationalism | Gộp vào V2-2 | Trùng hướng |
| V2-06 Universal National Service | Bỏ | `conscription_factor` đã nằm trong range BoP |
| V2-09 Strategic Industries | Gộp vào V2-4 | Trùng loại phần thưởng |
| V3-01, 02, 04, 07, 09, 10 | V3-1, 2, 3, 4, 5, 6 | Giữ |
| V3-03 Propaganda Directorate | Bỏ | Chỉ cộng biến |
| V3-05 Total Mobilization | Gộp vào V3-5 | Trùng |
| V3-06 Autarky | Bỏ | Trùng N7 và thang trừng phạt |
| V3-08 Doctrine of National Survival | Bỏ | Mở T05 (đã bỏ); vấn đề quy kết (7.8.4) |
| S1, S5, S6, S7 | S1, S4, S5, S2 | Giữ |
| S2 New Dong Du | Gộp vào tên S2 | — |
| S3 Reform State Security, S4 Information Sovereignty | Bỏ | Trùng V2-3 và chỉ cộng biến |
| S8 New National Symbols | Bỏ | Cosmetic tự động |
| (mới) | S3 Hội Cựu chiến binh, S6 Ủy ban Hòa giải | Thêm một lựa chọn kìm hãm có giá chính trị thật và một nguồn `mil` ngoài chi tiền |
| M01, M03, M06, M18 | M1, M3, M2, M4 | Giữ |
| M02 Expand Conscription | Bỏ | Range BoP |
| M04, M05, M07–M17 | Bỏ | Trùng focus có sẵn: `VIE_mechanization`, `VIE_maritime_denial_idea`, `VIE_kilo_submarines`, `VIE_bastion_p_coastal_defence`, `VIE_maritime_militia`, `VIE_spratly_fortification`, `VIE_integrated_air_defense`, `VIE_fighter_replacement`, `VIE_su30mk2_fleet`, `VIE_uav_program`, `VIE_z_factories`, `VIE_viettel_military_tech`, `VIE_msl_cruise_missiles`. M4 thưởng khi đã làm chúng |
| D01, D03, D04, D05, D11, D12 | D1, D2, D3, D4, D5, D6 | Giữ |
| D02 Abandon the "Four Nos" | Tự động (H1) | Vào chế độ là gỡ idea |
| D06 Open Cam Ranh | Gộp vào D2 (`vie_nat.60`) | Cây chính đã có `VIE_cam_ranh_base` |
| D07 Maritime Security Coalition | Bỏ | Phức tạp faction; D5 đã có faction |
| D08 Arms Pact with Russia | Gộp vào D3 (`vie_nat.61`) | Cây chính có `VIE_russian_arms_deals` |
| D09 India Axis | Bỏ | Cây chính có `VIE_india_partnership`; D2/D3 có opinion với RAJ |
| D10 Armed Neutrality | Thành idea của D4 | — |
| D13 Special Relationship | Bỏ | Cây chính có `VIE_special_relations_laos` |
| D14 Indochina Security Pact | Gộp vào D5 | — |
| T01 Assert Sovereignty | Bỏ | Claim đã có |
| T02 Operation for the Paracels | Dùng `VIE_paracel_ultimatum` | Trùng |
| T03, T04, T07, T08 | T3, T4, T2, T1 | Giữ |
| T05, T06 (tầng 3) | Bỏ; thay bằng event `vie_nat.25` [FR] | I-09 |

### A.2 Event

| Báo cáo | Đặc tả | Báo cáo | Đặc tả |
|---|---|---|---|
| vietnam_nat.1 | `vie_nat.1` | vietnam_nat.31 | `vie_nat.35` |
| vietnam_nat.2 | `vie_col.1.c` + `vie_nat.2` | vietnam_nat.32 | Bỏ (I-12) |
| vietnam_nat.3 | Bỏ; `vie_alt.1.c` + hệ sụp đổ | vietnam_nat.40, .41, .42 | `vie_nat.40`, `.41`, `.42` |
| vietnam_nat.4 | Phát hiện qua bầu cử MD; `vie_nat.4` là đảng ra đời | vietnam_nat.45 | `vie_nat.13` |
| vietnam_nat.5, .6, .7 | `vie_nat.10`, `.11`, `.12` | vietnam_nat.50 | `vie_nat.50` |
| vietnam_nat.8 | Gộp vào `vie_nat.13` | vietnam_nat.50b | `vie_nat.31` |
| vietnam_nat.9 | `vie_nat.9` | vietnam_nat.51, .52, .53 | `vie_nat.51`, `.52`, `.53` |
| vietnam_nat.10 | Bỏ (hiệu ứng nằm trong decision) | vietnam_nat.54 | Hiệu ứng trực tiếp + news `.7` |
| vietnam_nat.11 | `vie_nat.15` | vietnam_nat.55 | `vie_nat.56` |
| vietnam_nat.20, .21, .22 | `vie_nat.20`, `.21`, `.22` | vietnam_nat.56 | `vie_nat.55` |
| vietnam_nat.30 | `vie_nat.30` | vietnam_nat.60, .61 | `vie_nat.60`, `.61` |
| (mới) | `vie_nat.14` (trưng cầu), `.25` [FR], `.32` (CHI) | vietnam_nat_news.1–6 | `vie_nat_news.1–6`, thêm `.7` |

### A.3 Hệ thống

| Báo cáo | Đặc tả |
|---|---|
| `VIE_nat_fervor` | War support |
| `VIE_nat_radicalization` | BoP `VIE_nat_balance` |
| `VIE_nat_isolation` | Thang trừng phạt MD + ASEAN + opinion + range BoP |
| `VIE_nat_army_loyalty` | `the_military_opinion` |
| 6 idea phân tầng | 5 range BoP; `VIE_nat_restless_army` bỏ (MD đã phạt `mil` thấp) |
| `VIE_nat_regime_modifier` | Bỏ; dùng idea và `VIE_af_*` |
| `VIE_nat_enter_regime` | `VIE_transition_regime` + `VIE_nat_regime_init` |
| `VIE_nat_update_tiers` | Bỏ (BoP tự áp range) |
| `VIE_nat_swap_charter` | `VIE_nat_on_variant_change` |
| Game rule `VIE_nat_ai_behavior` | Option mới trong `VIE_ai_behavior` |
| 4 biến, 6 idea, 1 dynamic modifier, 1 game rule | 1 biến, 1 BoP, 14 idea (không idea nào là "tầng thước đo") |

---

## Phụ lục B: Quan sát ngoài phạm vi

Không thuộc thiết kế này, nhưng developer sẽ gặp khi code:

1. `tools/TESTING.md` nhắc script `tools\check_vie.ps1` không có trong repo, và các ID không còn tồn tại: `vie_alt.15`, `VIE_np_unlocked`, `VIE_junta_unlocked`, `VIE_lac_hong_active`, và effect `VIE_enter_regime` (hiện chỉ còn dòng chú thích ở `mod:common/scripted_effects/VIE_md_effects_p3.txt:6`).
2. Chuỗi dân chủ `vie_alt.12–14` chưa có nơi gọi (N-12).
3. `VIE_col_pick_rebel` có nhánh nội chiến cho phe 20 trong `VIE_col_start_civil_war`, nhưng không bao giờ chọn 20 (H3 sửa).
4. Cờ `VIE_AI_PATH_NATIONALIST` được focus đọc nhưng chưa bao giờ được đặt (H8 sửa).
