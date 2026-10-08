# MD Vietnam (dev)

Submod của **Millennium Dawn** (MD), nước chơi `VIE`, mốc 2000 → 2026, HOI4 `1.19.*`.
`descriptor.mod` khai báo phụ thuộc vào MD, nên mọi effect/trigger/idea của MD đều dùng được.
MD không nằm trong repo này. Bản MD trên máy tác giả ở `D:\ide\Millennium-Dawn` (đọc để xác minh token, đừng sửa).
Đừng bịa tên scripted effect của MD: grep ở đó, hoặc trong `tools/audit/md_ref/`.

Repo KHÔNG phải repo upstream MD. Không có `Changelog.txt`, `.github/`, `tools/validation/`,
`validation_config.json`, `pre-commit`, `pytest`. Đừng gọi hay tham chiếu chúng.

## Đọc trước khi làm

| Việc | Đọc |
|---|---|
| Cấu trúc thư mục, prefix, namespace | [docs/mod-overview.md](docs/mod-overview.md) |
| Viết/sửa focus, effect, decision, event, idea | [docs/conventions.md](docs/conventions.md) và [skill md-focus](skills/md-focus/SKILL.md) (chuẩn tạo & lập trình focus toàn diện) |
| Viết/sửa localisation | [docs/localisation.md](docs/localisation.md) |
| Chạy kiểm tra, đọc kết quả | [docs/validation.md](docs/validation.md) và [skill validate](skills/validate/SKILL.md) (kiểm tra tĩnh, loc và review diff) |
| Tìm bug theo pattern, review diff | [docs/bug-patterns.md](docs/bug-patterns.md) |
| Bẫy engine (scope, guard, FROM...) | [docs/engine-pitfalls.md](docs/engine-pitfalls.md) |
| Lỗi đã biết còn tồn đọng | [docs/known-issues.md](docs/known-issues.md) |
| Thiết kế mỹ thuật & Icon toàn bộ submod | [docs/art-style-guide/README.md](docs/art-style-guide/README.md) |
| Tạo/sửa/xuất/tích hợp ảnh: focus, idea, decision, event, portrait, UI | [skill md-art](skills/md-art/SKILL.md) (cẩm nang mỹ thuật toàn diện 6 consumer) |

Mỹ thuật: đọc profile thực tế trước khi gen. Focus VIE 93×91, idea 60×68,
decision TGA 33×32, event 210×176, portrait 156×210/38×51 là các profile đã đo,
không là chuẩn duy nhất của MD. Nguồn và quy tắc hiện hành ở art-style-guide tập 4/6/7.
Không áp HUD neon hoặc badge vàng lên mọi loại ảnh. Hai mẫu ngoại giao đã chọn
vẫn là mốc của nhóm ngoại giao; giữ source và báo kiểm file/in-game riêng.

Tài liệu thiết kế nằm ở gốc repo (`VIE_*.md`, `Con_duong_Kien_dinh_*.md`). Trước khi đổi một hệ thống
(trục quân sự, không quân, hải quân, lực lượng đặc biệt, chế độ, state-building) hãy đọc file thiết kế
tương ứng; file kế hoạch `*_plan*.md` / `*_review_and_plan.md` ghi các quyết định đã chốt.

## Quy tắc cứng

1. **Không bịa định danh.** Mọi effect, trigger, modifier, sprite, idea, event id phải kiểm chứng bằng
   định nghĩa thật (grep trong mod, `tools/audit/md_ref/`, hoặc tài liệu engine). Dùng thấy ở chỗ khác
   chưa phải bằng chứng.
2. **Tiền thật phải trừ qua scripted effect của MD** (`one_state_*`, `one_random_*`, hoặc
   `set_temp_variable = { treasury_change = -N }` + `modify_treasury_effect = yes`). Không dùng thô
   `add_building_construction` cho nhà máy/hạ tầng; công trình theo province (bunker, coastal_bunker,
   naval_base) bắt buộc có `province =`.
3. **Scope vào state phải là state VIE sở hữu** (518-524, 526, 801, 802, 813, 816). Xác minh state lạ
   bằng `python tools/audit/prov.py`.
4. **Mọi tham chiếu chéo phải khép kín**: effect gọi phải có định nghĩa, event fire phải tồn tại,
   loc key dùng trong tooltip phải có, focus/decision/idea mới phải có loc và icon.
5. **Sửa cây focus phải giữ**: không trùng toạ độ, không forward-ref của `relative_position_id`,
   không prerequisite thiếu hoặc vòng lặp. Chạy `tools/audit/audit.py` sau mỗi thay đổi.
6. Ghi chú trong code viết **tiếng Việt không dấu** (khớp file hiện có). Loc hiển thị cho người chơi
   viết tiếng Việt có dấu.
7. Sau khi sửa, **chạy kiểm tra liên quan** rồi báo kết quả thật, kể cả khi còn lỗi. Chưa chạy trong
   game thì nói rõ là chưa chạy trong game.
8. Mỗi thay đổi nội dung lớn cập nhật dòng `## vN (dd/mm/yyyy)` ở đầu `VIE_md_focus.txt`
   (nhật ký thay đổi của cây focus) và file kế hoạch tương ứng nếu có.

## Lệnh thường dùng (chạy từ gốc repo)

```bash
python tools/audit/audit.py      # cây focus
python tools/audit/live.py       # tham chiếu chéo
python tools/audit/ev.py         # event
python tools/audit/prov.py       # state / province
python tools/audit_loc_errors.py # loc
python tools/audit_dds_and_gfx.py
python tools/verify_all_loc.py
```

`settings.json` đặt `PYTHONIOENCODING=utf-8` để các script in tiếng Việt không crash trên Windows.

## AI design

Before designing or editing Vietnam AI paths, plans, strategies, research, templates, equipment, theaters, or naval behavior, read [docs/ai-strategy-design.md](docs/ai-strategy-design.md) and [docs/ai-subsystems-reference.md](docs/ai-subsystems-reference.md).

## Commit

Dạng `feat: ...`, `fix: ...`, `docs: ...`, mô tả ngắn bằng tiếng Anh hoặc Việt không dấu như lịch sử git.
Làm việc trên nhánh riêng cho hệ thống lớn, merge vào `main` khi xong (đã làm với `special-forces-v1`,
`air-effects-v2`).
