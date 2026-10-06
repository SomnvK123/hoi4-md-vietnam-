# Tổng quan mod

Submod của Millennium Dawn, chơi Việt Nam (`VIE`) từ 2000 đến 2026. `descriptor.mod` v0.4.x,
`supported_version = 1.19.*`.

## Xương sống gameplay

- **Lịch sử chạy bằng event có ngày cố định** (Đại hội Đảng IX → XIV). Focus là lựa chọn của người chơi,
  decision là lớp thực thi nghị quyết.
- **Hệ trục** `VIE_ax_*` (9 chiều), chuẩn hoá hằng tháng bằng `VIE_ax_normalize`, hiển thị qua
  `common/scripted_localisation/VIE_md_axis_bars.txt`, đổ vào dynamic modifier `VIE_state_modifier`
  (biến `VIE_sb_*_mod`). Thiết kế: `VIE_statebuilding_*.md`.
- **Balance of Power** `VIE_party_balance` (`common/bop/VIE_md_bop.txt`). Band oligarch đã xoá.
- **Biến nhiệm kỳ** `VIE_congress_term` (8 → 14), suy lại mỗi `on_startup`.
- **Scheduler**: một hook `on_monthly` duy nhất ở `common/on_actions/VIE_md_on_actions.txt`, guard
  `original_tag = VIE` để vẫn chạy sau nội chiến. Thêm scheduler mới thì thêm vào đúng khối này.
- **Game rule** `VIE_alt_history` (Plausible / Historical / Free) và `VIE_ai_behavior`
  (cờ global `VIE_AI_PATH_*`, đọc bởi `ai_will_do` / `ai_chance`).
- **Hệ thống quân sự**: trục Lục quân (`VIE_lf_*`), Hải quân (`VIE_nf_*`, `VIE_naval_*`, `VIE_nav_*`),
  Không quân (`VIE_airf_*`, `VIE_apm_*`, `VIE_ap_*`), Lực lượng đặc biệt (`VIE_sf_*`), chế độ cứng rắn
  (`VIE_hl_*`), an ninh / Biển Đông (`VIE_sec_*`, `VIE_scs_*`). Modifier quân sự gộp ở dynamic modifier
  `VIE_armed_forces_modifier`, giá trị nằm ở các biến `VIE_af_*`.

## Bản đồ thư mục

| Đường dẫn | Nội dung |
|---|---|
| `common/national_focus/VIE_md_focus.txt` | Toàn bộ cây focus (1 file, ~13k dòng, ~412 focus). Đầu file có nhật ký `## vN` |
| `common/scripted_effects/VIE_md_effects_<chủ đề>.txt` | Reward và helper. Hậu tố `_pN` là đợt (phase) viết, không phải chủ đề |
| `common/scripted_triggers/` | Trigger dùng chung (`VIE_md_triggers_*.txt`) |
| `common/decisions/` + `categories/` | Decision, nhóm theo hệ thống (`air_force`, `naval`, `hardline`, ...) |
| `common/ideas/VIE_md_ideas_*.txt` | Idea / national spirit. Một số idea không còn ai cấp (xem known-issues) |
| `common/dynamic_modifiers/` | `VIE_armed_forces_modifier`, `VIE_state_modifier` |
| `common/opinion_modifiers/` | Opinion modifier (ASEAN, HD-981, hiệp định biên giới, ...). Không phải dynamic modifier |
| `common/characters/`, `gfx/leaders/VIE/` | Nhân vật và chân dung |
| `events/VIE_*.txt` | Event, mỗi file khai báo `add_namespace` của nó |
| `localisation/english/` | Loc (toàn tiếng Việt, tên thư mục chỉ để HOI4 nạp) |
| `localisation/english/replace/` | Loc **ghi đè** cùng key ở thư mục cha. Bản trong `replace/` thắng |
| `interface/*.gfx`, `gfx/` | Sprite, icon focus, ảnh event, font |
| `assets/focus_icons/png`, `assets/event_pictures` | Nguồn PNG để build ra DDS/TGA (script `tools/build_*`) |
| `tools/` | Script kiểm tra, sinh nội dung, layout. Xem [validation.md](validation.md) |
| `scratch/` | Thử nghiệm tạm, không phải nội dung mod |
| `*.md` ở gốc | Tài liệu thiết kế và kế hoạch. `v1*_removed_*.txt` là kho lưu focus đã xoá, game không nạp |

## Prefix và namespace

Biến, cờ, effect, idea đều bắt đầu bằng `VIE_`. Prefix con (suy ra từ tên file và biến):

| Prefix | Hệ thống |
|---|---|
| `ax`, `axbar`, `sb` | Hệ trục, thanh trục, state-building |
| `lf`, `af` | Lục quân (land force), biến modifier lực lượng vũ trang |
| `nf`, `naval`, `nav` | Hải quân |
| `airf`, `apm`, `ap` | Không quân: lực lượng, công nghiệp, mua sắm |
| `sf` | Lực lượng đặc biệt (sapper, marine) |
| `hl` | Chế độ cứng rắn (hardline), `VIE_md_hardline_*` |
| `sec`, `scs` | An ninh, Biển Đông |
| `tt` | Key loc dùng cho tooltip (`VIE_tt_*`) |
| `sched` | Hàm scheduler hằng tháng |

Namespace event (ví dụ): `vie_pol`, `vie_eco`, `vie_scs`, `vie_dip`, `vie_soc`, `vie_alt`, `vie_hl`,
`vie_lf`, `vie_air_force`, `vie_nav_force`, `vie_naval`, `vie_sec`, `vie_p1b`. Id event dạng `vie_xxx.N`.
Một namespace có thể trải qua nhiều file (ví dụ `vie_scs`, `vie_pol`), mỗi file phải tự khai báo
`add_namespace`.

## Phụ thuộc MD

- Mọi token MD (scripted effect, modifier, idea, trigger) phải có thật trong MD. Kiểm bằng bản MD trên máy
  `D:\ide\Millennium-Dawn` (cây tham chiếu `common/national_focus/05_germany.txt`, `05_china.txt`, `05_thailand.txt`;
  tài liệu `docs/src/content/resources/`), hoặc `tools/audit/md_ref/` (12 file state, vài file effect/trigger),
  hoặc Steam Workshop id `2777392649`.
- File MD bị ghi đè hoặc chèn vào: `common/bookmarks/blitzkrieg.txt` (bản sao file MD, chèn khối VIE).
  Đụng vào là đụng file của MD, cần cẩn thận khi MD đổi phiên bản.
- Hook của MD đã dùng sẵn: `on_monthly_VIE` (MD, bắn `vietnam.1`). Mod dùng `on_monthly` chung để không đụng.
