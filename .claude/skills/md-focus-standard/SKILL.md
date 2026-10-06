---
name: md-focus-standard
description: 'Chuẩn viết focus theo Millennium Dawn, rút từ cây Đức, Trung Quốc, Thái Lan và tài liệu MD: kiến trúc cây, thứ tự trường, reward, tiền, AI path, tooltip, kiểm tra. Dùng khi viết, mở rộng, review hoặc làm lại bất kỳ focus/nhánh nào của VIE.'
---

# Chuẩn viết focus kiểu Millennium Dawn

Dùng khi viết hoặc review focus trong `common/national_focus/VIE_md_focus.txt`. Nguồn: ba cây tham chiếu của MD
(`D:\ide\Millennium-Dawn\common\national_focus\05_germany.txt` 588 focus, `05_china.txt` 558, `05_thailand.txt` 384)
và tài liệu `D:\ide\Millennium-Dawn\docs\src\content\resources\` (`focus-tree-design-principles.md`,
`code-stylization-guide.md`, `content-review-guide.md`, `focus-tree-modernization-guide.md`, `search-filters.md`,
`dynamic-modifiers.md`). Số liệu dưới đây đo trực tiếp trên ba cây đó. Bản MD ở `D:\ide\Millennium-Dawn` là nơi
**xác minh token**: effect, trigger, modifier, tooltip key phải grep được ở đó (hoặc trong mod VIE) trước khi dùng.

Quy ước riêng của VIE (cost 5/7, bố cục hàng ngang, trigger đảng) vẫn theo `.claude/docs/conventions.md` và
`VIE_focus_coding_standards.md`. Skill này nói MD đòi gì và ba cây mẫu làm thế nào, rồi chỉ ra chỗ VIE lệch.

## 1. Kiến trúc cây (ba cây giống nhau ở điểm nào)

| Điểm | Đức | Trung | Thái | Quy tắc |
|---|---|---|---|---|
| Khối `country` | `factor = 0`, `modifier = { add = 25 tag = GER }` | `add = 20 tag = CHI` | `add = 25 tag = SIA` | `factor = 0` + một `modifier` cộng cho đúng tag |
| `shortcut` | 5 | 5 | 5 | Mỗi nhánh lớn một nút nhảy, 4 đến 6 cái, `scroll_wheel_factor = 0.80` (chuẩn MD) |
| `continuous_focus_position` | có | có | có | Đặt xa các làn nhánh |
| `initial_show_position` | có | không | có | Chỉ về focus đầu tiên người chơi thấy |
| Neo vị trí | 583/588 focus có `relative_position_id` | 553/558 | 383/384 | Chỉ vài root dùng toạ độ tuyệt đối |
| `y` tương đối | 61% `y = 1` | 40% `y = 1` | 84% `y = 1` | `y = 1` ngay dưới cha là mặc định; `y >= 3` hiếm |
| `x` tương đối | `0, ±1, ±2` chiếm đa số | tương tự | tương tự | Anh em lệch ±1 đến ±2 |
| `prerequisite` | 580/588 | 550/558 | 371/384 | Hầu hết focus có cha trực tiếp; root không có |
| `mutually_exclusive` | 58 | 78 | 79 | Dùng cho ngã rẽ thật, không cho cả nhánh khổng lồ |

Nguyên tắc kiến trúc (MD `focus-tree-design-principles.md`):
- **Bố cục**: cây xếp **ngang** thành các làn (lane) theo nhánh; mỗi làn một root, con neo vào cha, dịch cả nhánh
  chỉ cần dời một focus. Cây MD tham chiếu là Pháp và Trung Quốc.
- **Đan xen nhánh**: kinh tế, chính trị, ngoại giao phải ảnh hưởng lẫn nhau, không để nhánh cô lập.
- **Không chuỗi dọc dài không rẽ**: cứ vài focus phải có lựa chọn.
- **Không `mutually_exclusive` cỡ lớn** chứa mutex lồng nhau: dùng `available` để khoá theo điều kiện thay vì khoá vĩnh viễn.
- **Mọi lựa chọn có đánh đổi**: không đường nào hơn hẳn đường kia (người chơi min-max).
- **Thời lượng khớp phần thưởng**: focus dài thì thưởng lớn; thưởng nhỏ thì cost thấp.
- **Không miễn phí**: công trình, nhà máy, bonus kinh tế đều có chi phí tiền.
- **Chất lượng hơn số lượng**: tránh chuỗi chỉ cộng PP, stability, war support, số nhà máy.
- **Có path chính trị/alt-history hợp lý**, kèm một modifier "lịch sử" cho AI (xem mục 5).
- **Hiệu ứng lên nước khác phải qua event** để người kia có quyền chọn (mục 6).
- **Làm lại cây theo từng mảng** (quân sự, rồi công nghiệp...), mỗi mảng draft, code, test, merge rồi mới sang mảng sau.
- Quy mô MD: cây generic là 114 focus, cây quốc gia tối thiểu phải bằng cỡ đó.

## 2. Thứ tự trường trong một focus

Đo thực tế: dạng phổ biến nhất của cả ba cây là
`id, icon, x, y, relative_position_id, cost, prerequisite, search_filters, [available], [bypass], completion_reward, ai_will_do`.

```
id  icon  x  y  relative_position_id  cost  allow_branch  prerequisite/mutually_exclusive
will_lead_to_war_with  search_filters  available/bypass/cancel  completion_reward/select_effect/bypass_effect  ai_will_do (CUỐI)
```

- `id` dòng đầu, `icon` dòng hai. Tag viết hoa: `SIA_xxx`. Id mới viết thường sau tiền tố tag.
- Bỏ giá trị mặc định: `cancel_if_invalid = yes`, `continue_if_invalid = no`, `available_if_capitulated = no`.
  (Đức vẫn còn 7 focus ghi `continue_if_invalid` và 2 ghi `cancel_if_invalid`, đó là ngoại lệ có chủ đích, đừng sao chép.)
- Không để block rỗng (`available`, `bypass`, `cancel`, `mutually_exclusive`) hay dòng marker `# bypass = { }`.
- Tab thụt lề, `{` cùng dòng, điều kiện đơn giản viết một dòng. File `.txt` UTF-8 **không BOM**.
- Mỗi focus tối đa 5 hiệu ứng vĩnh viễn; thêm nữa thì dùng `add_timed_idea`.
- Chỉ viết thuộc tính focus thật sự dùng; không comment code chết.

## 3. `cost`, log, search_filters

- `cost`: MD gốc mặc định 10. Thái dùng 5 (38%), 6 (29%), 7 (10%); Trung dùng 7 (44%), 5 (34%), 3 (13%), 10; Đức dùng
  số lẻ (4.3, 6.5, 6, 7.15). VIE giữ thang 5/7 (16 cho `VIE_spratly_fortification`) và bỏ khi bằng 10.
  Cost là thời gian, không phải tiền.
- Log là dòng đầu của `completion_reward`: `log = "[GetDateText]: [Root.GetName]: Focus TAG_ten"`. Cả ba cây đều ghi ở
  100% focus có reward. Bản làm-lại mới của MD ghi `[This.GetName]: focus <ID> executed`; VIE giữ dạng `Focus ...` cho nhất quán.
  Chỉ log khi reward có effect thật.
- `search_filters` bắt buộc, một dòng. Mô hình hai lớp: filter riêng của nước (ví dụ `FOCUS_FILTER_CHI_TECH_DEPENDENCE`)
  cộng 1 đến 2 filter chung. Cây nhỏ có thể dùng filter chung. Ba cây dùng nhiều nhất: `POLITICAL`, `MILITARY_LAWS`,
  `ECONOMY`, `INDUSTRY`, `EXPENDITURE`, `FOREIGN_POLICY`, `STABILITY`. Focus tốn tiền thật (từ ~5 tỷ) gắn
  `FOCUS_FILTER_EXPENDITURE` (Đức 92, Trung 35, Thái 49 focus; VIE mới 2).
- Danh sách filter đầy đủ: `D:\ide\Millennium-Dawn\docs\src\content\resources\search-filters.md`. Dùng `MILITARY_LAWS`
  và `AIRCRAFT`, không dùng alias cũ `MILITARY` và `AIR`.

## 4. Reward: cái gì làm focus "có thật"

Đo thực tế (số focus có reward chỉ gồm log, tooltip, `add_to_variable`, PP, stability, war support):
Đức 8/588, Trung 29/558, Thái 16/384. Tức hầu hết focus có ít nhất một thứ khác. MD đặt ngưỡng: nếu hơn ~20% focus chỉ là
`log` + `custom_effect_tooltip` + `add_to_variable` thì cây "công thức hoá".

Các dạng reward MD dùng, nên trộn ít nhất 4 loại trong cả cây:
1. **Dynamic modifier có biến** (chủ lực): `custom_effect_tooltip = { localization_key = modifies_dynamic_modifier_tt MODIFIER = TAG_x_modifier }`
   rồi `add_to_variable = { TAG_x_<stat> = 0.05 tooltip = <stat>_tt }`. Lần đầu thêm modifier dùng
   `adds_dynamic_modifier_tt` kèm `add_dynamic_modifier`. Thái add modifier ở `history/countries` (khởi đầu), nên focus chỉ
   `add_to_variable`. Không bao giờ `force_update_dynamic_modifier`. Cả hai nhánh mutex cùng thêm modifier lần đầu đều dùng `adds_...`.
2. **Idea và swap**: `add_ideas`, `swap_ideas`, `add_timed_idea` (Đức 70/51, Trung 68/19 + 49 timed, Thái 67/14 + 29).
   Thang cải cách = timed idea + `swap_ideas`, không chồng idea vĩnh viễn.
3. **Chi phí tiền**: `set_temp_variable = { treasury_change = -N }` + `modify_treasury_effect = yes`; công trình dùng
   `one_state_*` / `one_random_*` / `two_office_construction` (đã tự trừ tiền, đừng trừ hai lần). Tham chiếu giá: MD `code-resource.md`.
4. **Công trình / tài nguyên** qua scripted effect có giá + chỗ slot đi kèm.
5. **Opinion nhóm lợi ích** (`set_temp_variable = { temp_opinion = 5 } change_<group>_opinion = yes`), **influence**, **tham nhũng**
   (`decrease_corruption = yes`), **tăng trưởng** (`increase_economic_growth = yes`).
6. **Event có lựa chọn thật** (`country_event = { id = ... days = N }`), cờ, mở decision category, unlock MIO
   (`mio:TAG_x = { add_mio_funds = N }` bọc `has_dlc = "Arms Against Tyranny"`), `add_tech_bonus`, wargoal.
7. Chính trị: mỗi nhánh chính trị phải đi vào idea/cơ chế/event **riêng**, không chỉ `add_popularity` + bonus kinh tế.

Kèm theo:
- Capstone/điểm cuối nhánh phải mở thứ mới (decision category, giải phóng chư hầu, event định nghĩa, idea riêng), không chỉ số lớn hơn.
- Một nhánh mutex phải khác nhau về **loại** thưởng, không chỉ khác số (0.02 so với 0.01 là lựa chọn giả).
- Không dán nguyên khối reward/ai_will_do lặp lại; cùng một dòng `biến = số` lặp ≥10 lần chỉ đổi tên là copy-paste.
- Mỗi cây cần ít nhất một cơ chế riêng (họ modifier, thang idea, hệ scripted) mà không cây khác có.
- Đừng thêm cờ trùng với trạng thái truy vấn được (focus đã xong, idea đang có). Cờ chỉ cho chuyển trạng thái lịch sử.
- Không `add_ai_strategy` trong effect (hại hiệu năng AI).

## 5. `ai_will_do` và đường AI

- `ai_will_do` luôn cuối focus. Đo: không flat ở Đức 527/588, Trung 551/558, Thái 317/384.
- **Bankruptcy guard** (AI-only, đặt trong `ai_will_do`, không đặt trong `available`):
  `modifier = { factor = 0 has_active_mission = bankruptcy_incoming_collapse }`. Bắt buộc cho focus `cost ≥ 8`, hoặc `cost ≥ 5`
  mang filter quân sự/kinh tế/nghiên cứu, hoặc reward tốn tiền thật (Đức 140, Trung 176, Thái 134 focus có guard).
- Focus xây nhà máy/văn phòng thêm `modifier = { factor = 0 can_staff_an_industrial_complex = no }` (hoặc `can_staff_an_offices`,
  `can_staff_an_arms_industry`).
- **Đường chính trị**: game rule `TAG_ai_behavior` (nhóm `MD_FOCUS_TREE_RULES`) → `on_action` đặt cờ global
  `TAG_<PATH>_FOCUS_PATH` (MD đặt ở `999_game_rules_on_actions.txt`) → scripted trigger `TAG_ai_<path>_path`,
  `TAG_ai_not_<path>_path` → focus gate bằng cặp:
  `modifier = { factor = 25 has_global_flag = TAG_X_FOCUS_PATH }` và `modifier = { factor = 0 TAG_ai_not_x_path = yes }`.
  Thái tách: nhánh Greater Thailand nhận `factor 25` khi đúng path, `factor 0` khi path khác.
- **Lịch sử**: Trung dùng `is_historical_focus_on = yes` cộng điểm (`add = 1..5`) và `factor = 0 date < 20XX.1.1` để
  AI không nhảy sớm. Đức và Thái dùng `TAG_ai_historical_path = yes` / `TAG_ai_not_historical_path`.
  Focus cuối game thêm `modifier = { factor = 0 date < ... }`.
- Tình huống: `has_war = yes` (Đức 209 lần, chủ yếu focus quân sự), `ai_is_threatened = yes` (Trung 120, Thái 92).
- **Focus chiến tranh** giữ guard faction/sức mạnh; không gỡ khi chỉnh trọng số.
- `ai_will_do` base: Đức 1, Trung 8, Thái 10 đến 60. Giá trị base tuỳ cây, quan trọng là tương quan giữa các focus cùng cấp.
- **Strategy plan**: mỗi nước một file `common/ai_strategy_plans/TAG_strategy_plans.txt` (Thái, Trung có; VIE chưa):
  mỗi plan có `allowed = { original_tag = TAG }`, `enable` theo cờ path, `abort = { is_subject = yes }`, `focus_factors`
  (đặt 0 cho focus của path đối lập, 30 đến 100 cho focus của path), và `ai_strategy`. Mọi focus id trong plan phải còn tồn tại.

## 6. Tooltip, available, event, chiến tranh

- Điều kiện cờ/biến trong `available` bọc `custom_trigger_tooltip = { tooltip = KEY ... }` bằng câu dễ đọc (Trung 84, Thái 26).
  Trong `NOT` cần key `<KEY>_NOT`.
- Điều kiện đảng cầm quyền dùng trigger MD (`<slug>_are_in_power`, `_are_in_coalition`), không `check_variable = { ruling_party = N }`.
- `bypass` phải đạt được: ví dụ `bypass = { date > 2001.1.6 }` hay `NOT = { country_exists = X }`. Không bao giờ ghép
  với `available = { always = no }`.
- **Focus bắn event sang nước khác** (mẫu Trung `CHI_The_Duterte_Pivot`):
  ```
  PHI = { country_event = { id = china_scs.32 days = 1 } }
  newline = yes
  custom_effect_tooltip = TT_IF_THEY_ACCEPT
  effect_tooltip = { add_ideas = ... add_to_variable = { ... tooltip = ... } }
  ```
  `effect_tooltip` cho người chơi thấy hệ quả nếu họ đồng ý. Event sang nước khác gọi qua `hidden_effect` nếu chỉ báo tin
  (mẫu Đức). Có `country_exists = TAG` trong `available`. Event gửi nước khác có `ai_chance` dựa trên quan hệ/opinion, không ngẫu nhiên.
- `newline = yes` ngăn cách các cụm effect trong tooltip.
- **Chiến tranh**: `will_lead_to_war_with = TAG` ngay dưới prerequisite; `available` có `country_exists`, `NOT has_war_with`,
  `NOT has_subject`, `has_army_size`, `has_war_support`; `bypass` khi mục tiêu đã chết hoặc thành chư hầu; reward bọc wargoal trong
  `if = { limit = { country_exists = TAG NOT = { has_subject = TAG } } ... create_wargoal ... }`, kèm tăng threat bằng
  scripted effect của MD khi có (Thái dùng `TAG_add_threat_from_wargoal_effect`).
- Không thêm core miễn phí: cần cơ chế đạt ≥ 80% compliance hoặc hệ hội nhập.
- Cờ đặt trong reward bọc `hidden_effect`; thông tin hiện cho người chơi bằng `custom_effect_tooltip`.
- Không bọc cả reward trong `if/limit` (tooltip sẽ báo "no effect"); dọn trạng thái cũ để trong `hidden_effect`.

## 7. Nội dung đi kèm một nhánh (vòng đời MD)

Một nhánh/tree hoàn chỉnh cần (theo `focus-tree-lifecycle-checklist.md`): draft được duyệt trước khi code; reward;
idea; decision; cơ chế riêng; `history` của nước; OOB; lãnh đạo/tướng; loc đảng, focus, idea, decision; namelist;
AI đầu tư/ảnh hưởng; game rule AI; GFX (khoảng 15% icon custom là đủ, chỉ cho focus quan trọng); scripted loc; log lỗi sạch;
ít nhất một lần chơi thử, hai lần review; ghi changelog. Với VIE: đủ loc `VIE_<id>` và `_desc`, icon tồn tại,
đã chạy `tools/audit/*`, và ghi dòng `## vN` đầu file focus.

## 8. Quy trình viết một focus hoặc nhánh

1. Đọc nhánh liên quan trong file thiết kế `VIE_*.md` và các focus lân cận. Giữ id, toạ độ, anchor, prerequisite đã có
   (events/decisions tham chiếu qua `has_completed_focus`); chỉ đổi khi người dùng yêu cầu.
2. Quyết định **danh tính cơ chế** của nhánh: 3 đến 4 họ modifier, idea, hoặc scripted effect riêng, dựa trên thứ VIE đã có
   (`VIE_armed_forces_modifier`, `VIE_state_modifier`, `VIE_ax_*`...). Viết bảng reward cho từng focus trước khi đụng script.
3. Viết theo từng khối 60 đến 80 focus nếu làm lại lớn; tìm vị trí bằng `grep -n "id = VIE_xxx"`, không theo số dòng.
4. Với mỗi focus: thứ tự trường (mục 2), reward đa dạng (mục 4), `ai_will_do` đủ guard (mục 5), tooltip và available (mục 6).
5. Thêm loc, icon; chạy `/validate focus`, `/validate refs`, `/validate loc`; so với baseline trước khi làm.
6. Báo: focus thêm/sửa, loại reward trong nhánh (đủ ≥ 4 loại chưa), focus còn thiếu guard, và việc chưa thử trong game.

## 9. Checklist review nhanh

- [ ] Thứ tự trường đúng, `ai_will_do` cuối, `log` dòng đầu reward, không giá trị mặc định, không block rỗng
- [ ] `search_filters` một dòng, 1 đến 2 filter, `EXPENDITURE` nếu tốn tiền thật
- [ ] Bankruptcy guard cho focus `cost ≥ 8` hoặc tốn tiền; `can_staff_*` cho focus xây
- [ ] Công trình qua scripted effect có giá; công trình province có `province =`; không trừ tiền hai lần
- [ ] Reward không chỉ là PP/stability/war support; nhánh mutex khác nhau về loại thưởng
- [ ] Có ≥ 4 loại reward trong cả nhánh; capstone mở thứ mới; không dán nguyên khối lặp
- [ ] Event sang nước khác có `effect_tooltip` + `TT_IF_THEY_ACCEPT`, `country_exists`, `ai_chance`
- [ ] Focus chiến tranh có `will_lead_to_war_with`, guard `country_exists`/`has_subject`, `bypass` khả thi
- [ ] Dynamic modifier: đúng `adds_/modifies_dynamic_modifier_tt`, mỗi `add_to_variable` có `tooltip = <stat>_tt`
- [ ] Đường AI: cờ path, cặp `factor 25` / `factor 0`, strategy plan khớp id (VIE chưa có plan)
- [ ] Không forward-ref anchor, không trùng toạ độ, không vòng prerequisite (`tools/audit/audit.py`)
- [ ] Loc đủ `VIE_<id>` và `_desc`, có dấu, token động nguyên vẹn (`/loc-check`)

## 10. Chỗ VIE đang lệch so với ba cây mẫu (đo ngày 06/10/2026)

- `FOCUS_FILTER_EXPENDITURE` mới có 2 focus, trong khi nhiều focus VIE tốn tiền thật.
- Chưa có `common/ai_strategy_plans/VIE_strategy_plans.txt`; trigger `VIE_ai_historical` hiện luôn đúng
  (`common/scripted_triggers/VIE_md_triggers_p4.txt`), nên các nhánh path-AI chưa tách được.
- Còn một vài filter alias cũ (`FOCUS_FILTER_MILITARY`, `FOCUS_FILTER_AIR`).
- Cây hơn 400 focus nhưng nhiều nhánh quân sự mới dùng cùng một dạng reward biến + modifier; kiểm tỷ lệ reward "công thức"
  trước khi thêm nhánh nữa (ngưỡng ~20%).
- Công trình bunker trong `VIE_md_effects_p17.txt` thiếu `province` và không trừ tiền (xem `known-issues.md`).
