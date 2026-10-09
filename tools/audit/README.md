# `tools/audit/` — script kiểm tra tĩnh cho md_vietnam

Bổ sung cho `tools/verify_all_loc.py` (chỉ kiểm tra loc key + BOM + đếm focus) và
`tools/check_static.py` (sâu hơn nhưng **hardcode đường dẫn Windows** tới bản cài
Millennium Dawn, xem `tools/TESTING.md` mục 1).

Các script ở đây **portable**: đường dẫn được tính từ chính vị trí script
(`os.path.dirname(os.path.abspath(__file__))`), nên chạy được **từ bất kỳ thư mục nào**,
không cần `cd` vào gốc repo, không cần cài thêm gì, không cần HOI4 hay Millennium
Dawn trên máy. Khác với `tools/check_static.py` — file đó hardcode `D:/SteamLibrary/...`.

```bash
# chạy từ đâu cũng được
python3 <repo>/tools/audit/live.py      # đối chiếu tham chiếu chéo — chạy cái này trước
python3 <repo>/tools/audit/prov.py      # state / province so với dữ liệu Millennium Dawn
python3 <repo>/tools/audit/ev.py        # event: namespace, id trùng, loc, orphan
python3 <repo>/tools/audit/audit.py     # focus tree: prerequisite, toạ độ, cycle, forward-ref
python3 <repo>/tools/audit/xref.py      # bản cũ của live.py, quét cả file archive
```

Cả 5 script đã được test chạy từ `/tmp` (ngoài repo) và từ gốc repo — cả hai đều OK.
Ba file `.json` mà `audit.py` / `xref.py` sinh ra khi chạy nằm trong `.gitignore`.

Yêu cầu: Python 3.8+. Không có dependency ngoài thư viện chuẩn.

`industry.py` (Python 3.10+) kiểm riêng 39 focus công nghiệp v17: 64 tổ hợp nhóm
ngành, ngưỡng điểm, hai đường FDI, sự kiện save cũ, hai mức hỗ trợ bán dẫn và cổng
Vinashin. Bộ kiểm tra dùng một phần nhỏ trigger/effect đã khai báo và từ chối token
chưa hỗ trợ; không mô phỏng runtime HOI4. So đồ trước/sau tái xuất bằng
`tools/focus_layout/industry_diagram.py` (Pillow).

---

## `live.py` — đối chiếu tham chiếu chéo (quan trọng nhất)

Quét mọi file `.txt` / `.mod` / `.gfx` **live** (bỏ qua `.bak` và `v1*_removed_*.txt`
ở gốc repo — đó là archive, game không load) rồi đối chiếu:

| Kiểm tra | Nghĩa là |
|---|---|
| SCRIPTED EFFECT / TRIGGER CALLS (`X = yes`) | gọi một effect/trigger không tồn tại → engine bỏ qua im lặng |
| IDEAS (`add_ideas` / `has_idea` / `remove_idea`) | cấp hoặc hỏi một idea không tồn tại |
| DECISIONS · DECISION CATEGORIES | `activate_decision` / `unlock_decision_category` treo |
| FOCUS refs | `has_completed_focus`, `prerequisite`, shortcut `target` trỏ focus đã xoá |
| GAME RULE OPTIONS | `has_game_rule = { rule = … option = … }` sai tên |
| MIO organizations | `add_mio_*` sai tên |
| LOC keys dùng làm `tooltip` / `custom_*_tooltip` | tooltip sẽ hiện nguyên tên key |
| EVENTS fired but undefined | `country_event = { id = … }` trỏ event không tồn tại |
| EVENTS true orphans | event định nghĩa mà không ai fire (loại trừ chain nội bộ) |
| IDEAS defined but never granted | idea mồ côi — rác, dọn được |

In thêm `DEFS:` là số định nghĩa mỗi loại, dùng để đối chiếu nhanh sau khi thêm nội dung.

### Dương tính giả đã biết

Dòng `[DYNAMIC MODIFIERS] … MISSING=15` **không phải lỗi**. Pattern `modifier = X`
bắt cả `add_opinion_modifier = { … modifier = X }` lẫn `add_dynamic_modifier`. 15 tên đó
(`VIE_arms_deal`, `VIE_asean_cooperation`, `VIE_hd981_*`, `VIE_border_treaty`, …) đều
nằm trong `common/opinion_modifiers/VIE_md_opinion_modifiers.txt`, cộng
`VIE_ax_market_mod` là **biến** dùng bên trong `VIE_state_modifier`. Tất cả hợp lệ.

---

## `prov.py` — state & province so với Millennium Dawn

Đọc dữ liệu MD thật trong `md_ref/` (12 file `history/states/` của Việt Nam), dựng bản đồ
`province → state` và `state → owner năm 2000`, rồi kiểm tra code của mod:

1. mọi `province = N` có thuộc state mà khối bao quanh nó khai báo không
2. mọi khối `<state_id> = { … }` có rơi vào state mà **VIE không sở hữu** không
3. mọi `naval_base` / `dockyard` có đặt ở province nội địa không

Đây là script đã bắt ra 6 lỗi state/province (D-1 → D-6) sửa ở commit `2d95460`.
**Chạy script này mỗi lần thêm `add_building_construction` có `province =`.**

Kết quả mong đợi: `TỔNG HỢP LỖI: 0`.

---

## `ev.py` — event

- `add_namespace` có trong mỗi file `events/*.txt` không
- event `id` trùng lặp giữa các file
- event fired mà không có `id`
- event định nghĩa mà không ai fire
- event **không** `hidden = yes` mà thiếu loc `.t` / `.d` / `.a`

Đã loại trừ hai loại dương tính giả: `id = X` bên trong `set_power_balance` /
`create_faction` (không phải event), và event `hidden = yes` (không cần title/desc).

---

## `audit.py` — focus tree

Parse `common/national_focus/VIE_md_focus.txt` thành cây rồi kiểm tra:

| Kiểm tra | Vì sao quan trọng |
|---|---|
| dangling `prerequisite` / `relative_position_id` / `mutually_exclusive` | trỏ focus đã xoá → engine báo lỗi |
| **forward anchor ref** | `relative_position_id` trỏ focus khai báo **sau** trong file → engine đọc top-down nên báo ERROR |
| prerequisite cycle | focus không bao giờ mở được |
| duplicate toạ độ tuyệt đối | hai focus chồng lên nhau trên UI |
| missing absolute x/y | focus không vẽ được |
| child nằm ngang/trên parent | dây nối vẽ ngược |
| roots · cost distribution · no completion_reward · no icon | tổng quan cây |

Ghi ra `focus.json` để script khác dùng lại.

⚠️ Dòng `duplicate (x,y)` trong output là toạ độ **tương đối** (chưa resolve
`relative_position_id`) nên sẽ báo vài chục ca — **không phải lỗi**. Bản tuyệt đối nằm
ở khối `ABSOLUTE coordinate collisions`, phải bằng 0.

---

## `xref.py` — bản quét rộng (kèm archive)

Giống `live.py` nhưng **không** loại `v1*_removed_*.txt` và `.bak`. Dùng khi muốn biết
một id từng tồn tại ở đâu. Vì quét cả archive nên sẽ ra nhiều "missing" — đó là nội dung
đã xoá có chủ đích, không phải lỗi của code live. **Để kiểm tra code thì dùng `live.py`.**

Ghi ra `defined.json` và `missing.json`.

---

## `md_ref/` — dữ liệu Millennium Dawn (chỉ đọc)

Tải từ repo `MillenniumDawn/Millennium-Dawn` nhánh `main` qua GitHub API,
ngày **2026-09-30**. Không sửa tay; tải lại khi MD cập nhật.

| File | Nguồn trong MD |
|---|---|
| `518-Mekong Delta.txt` … `816-Southern Spratlys.txt` | `history/states/` — 12 state Việt Nam |
| `VIE_country.txt` | `history/countries/VIE - Vietnam.txt` |
| `state_names.yml` | `localisation/english/state_names_l_english.yml` |
| `vp.yml` | `localisation/english/victory_points_l_english.yml` |
| `SOV_Russia.txt` `POL.txt` `KOR.txt` `CHI.txt` `VIE_Vietnam.txt` | `history/countries/` — variant |
| `VIE_2000_nsb.txt` `VIE_2000_nonnsb.txt` | `history/units/` |
| `MD_tank_chassis.txt` `MD_x_tank_chassis.txt` `MD_artillery.txt` `MD_infantry_equipment.txt` | `common/units/equipment/` |
| `MD_tank_modules.txt` | `common/units/equipment/modules/` (295 module) |
| `MD_land_upgrades.txt` | `common/units/equipment/upgrades/` |
| `equipment_archetypes.md` | `common/units/equipment/` (bảng ID ↔ tên hiển thị) |
| `00_budget_effects.txt` | `common/scripted_effects/` — `modify_treasury_effect`, `modify_debt_effect` |
| `00_economic_triggers.txt` | `common/scripted_triggers/` — họ `can_staff_an_*` |
| `00_yearly_effects.txt` | `common/scripted_effects/` — 70 effect `trigger_year_*` |
| `MD_on_actions.txt` | `common/on_actions/` — dòng 904 gọi `trigger_year_[year]_events` |
| `MD_event_on_actions.txt` | `common/on_actions/` — `random_events` của MD |
| `00_scripted_effects.txt` | `common/scripted_effects/` — **`one_state_arms_factory` ở dòng 20**: tự trừ 7,5 tỷ, tự cộng `add_extra_state_shared_building_slots`, có fallback khi hết slot, có cờ `skip_payment` |
| `00_mio_scripted_effects.txt` | `common/scripted_effects/` — cú pháp `mio:<org> = { add_mio_size = N }` (dòng 218) |
| `00_startup_effects.txt` | `common/scripted_effects/` |
| `00_game_rules.txt` | `common/game_rules/` — nhóm `MD_FOCUS_TREE_RULES`, mẫu `rule_salafist_branch` |
| `MD_arty_modules.txt` | `common/units/equipment/modules/` — **170 module pháo**, gồm `art_med_gun_gen2`, `art_med_rocket_gen1`, `artillery_medium_ammo_2`. ⚠️ Các module pháo **không** nằm trong `MD_tank_modules.txt` |
| `tech_*.txt` (23 file) + `MD_technologies_artillery.txt` | `common/technologies/` — **đủ 24 file**, nguồn của `MD_all_CATS.json` (194 token) |
| `MD_all_CATS.json` | **194 token `CAT_*` hợp lệ**. ⚠️ Đối chiếu trước khi viết `add_tech_bonus` / `research_bonus` — xem `VIE_repo_health_report.md` mục 6.13 |
| `05_china.txt` | `events/` — mẫu event có 4+ option: `sino_indian.39` dùng `.d_opt` để tránh đụng `desc` |
| `oa_*.txt` | `common/on_actions/` |

Tải lại bằng GitHub API (không cần auth cho repo công khai):

```
https://api.github.com/repos/MillenniumDawn/Millennium-Dawn/git/trees/main?recursive=1
https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/<path>
```

---

## Tài liệu đọc kèm (ở gốc repo)

| File | Nội dung |
|---|---|
| `VIE_repo_health_report.md` | báo cáo sức khoẻ toàn repo: cấu trúc, kiến trúc gameplay, phần sạch, 12 khoản nợ |
| `VIE_md_states_reference.md` | 12 state Việt Nam trong MD + bảng tra 81 province → state → thành phố |
| `VIE_truc1_review_and_plan.md` | review Trục 1 (mua sắm) + plan code 8 bước |
| `VIE_variant_research.md` | bảng tier equipment MD, variant có sẵn, checklist khi cấp xe |
| `VIE_v9_flag_mapping.md` | hợp đồng cờ `VIE_ev_*` và cờ Trục 1 |
| `tools/TESTING.md` | cách test trong game + build log |

Land V30.2: `python tools/audit/land_structure_v30_2.py` checks the live 44-focus graph, direct/earlier anchors, global coordinate collisions, strategy AND/OR gates, 3-of-6 terminal gate, shared reward order independence, and no free unit spawning from training focuses.
