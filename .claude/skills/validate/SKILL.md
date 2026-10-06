---
name: validate
description: 'Chạy bộ kiểm tra tĩnh của mod VIE (focus, tham chiếu chéo, event, state/province, loc, gfx) và tóm tắt lỗi theo file:dòng. Dùng khi người dùng gọi /validate hoặc yêu cầu chạy kiểm tra.'
disable-model-invocation: true
---

Chạy bộ kiểm tra của mod và báo kết quả thật. Tham số (tuỳ chọn): $ARGUMENTS
(`focus`, `refs`, `event`, `prov`, `loc`, `gfx`, hoặc để trống để chạy tất cả).

Chạy từ gốc repo, đặt `PYTHONIOENCODING=utf-8`:

| Nhóm | Lệnh |
|---|---|
| focus | `python tools/audit/audit.py` |
| refs | `python tools/audit/live.py` |
| event | `python tools/audit/ev.py` |
| prov | `python tools/audit/prov.py` |
| loc | `python tools/audit_loc_errors.py` và `python tools/verify_all_loc.py` |
| gfx | `python tools/audit_dds_and_gfx.py` |

Khi diễn giải kết quả, đọc `.claude/docs/validation.md` và `.claude/docs/known-issues.md`:
- Nếu `live.py` in `DEFS:` với `effect: 0`, bộ định nghĩa rỗng (đường dẫn hỏng). Báo "kết quả không dùng được", đừng liệt kê
  hàng trăm MISSING như lỗi mod.
- Loại các báo nhầm đã biết (event ẩn thiếu loc, `GFX_report_event_generic_*`).
- Mỗi lỗi thật ghi `file:dòng — mô tả`. Kết thúc bằng một dòng tổng: số lỗi thật theo nhóm, hoặc "Sạch" cho nhóm đã chạy.
- Nói rõ nhóm nào không chạy được và vì sao. Đây là kiểm tra tĩnh, không thay thế chạy trong game.
