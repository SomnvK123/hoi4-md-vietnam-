# Kiểm tra (validation)

Repo không có CI, pre-commit hay pytest. Kiểm tra là các script Python thư viện chuẩn trong `tools/`,
chạy tay từ gốc repo. Không có công cụ nào chạy được HOI4, nên "đã qua script" chưa có nghĩa là
"chạy được trong game". Chi tiết từng script: `tools/audit/README.md`. Kịch bản test trong game:
`tools/TESTING.md` (phần đầu là hướng dẫn hiện hành, phần sau là nhật ký lịch sử).

`live.py` và `prov.py` tự đặt stdout UTF-8, chạy được trên Windows lẫn Linux. Các script khác nếu in tiếng Việt
mà crash `UnicodeEncodeError` thì đặt `PYTHONIOENCODING=utf-8` (đã có trong `.claude/settings.json`).

## Bộ kiểm tra theo loại thay đổi

| Bạn vừa sửa | Chạy | Kết quả mong đợi |
|---|---|---|
| Cây focus (thêm/xoá/dời) | `python tools/audit/audit.py` | 0 prerequisite treo, 0 trùng toạ độ, 0 forward-ref, 0 vòng lặp, 0 thiếu x/y |
| Effect / idea / decision / focus ref | `python tools/audit/live.py` | 0 MISSING ở mọi mục (kể cả dynamic modifier) |
| Event | `python tools/audit/ev.py` | Không id trùng, không event mồ côi; event "thiếu loc" của event ẩn là báo nhầm |
| `add_building_construction`, `province =`, scope vào state | `python tools/audit/prov.py` | `TỔNG HỢP LỖI: 0`. Chạy mỗi khi thêm công trình |
| Loc | `python tools/audit_loc_errors.py` và `python tools/verify_all_loc.py` | 0 lỗi cú pháp, 0 focus thiếu title/desc |
| Icon, sprite, DDS | `python tools/audit_dds_and_gfx.py` | 0 lỗi DDS, 0 texturefile thiếu. Danh sách "MISSING EVENT PIC" `GFX_report_event_generic_*` là sprite vanilla/MD, báo nhầm |
| Cân bằng trục quân sự | `tools/audit/lf_balance.py`, `nf_balance.py`, `air_*_balance.py`, `naval_balance.py` | In `PASS` |
| Layout cây | `tools/focus_layout/` (xem README trong đó) | Không tăng span, không gap < 2 |

Luôn đọc kết quả thật trước khi báo "sạch". Nếu script không chạy được, nói rõ thay vì suy đoán.

## Lỗi và hạn chế đã biết của chính các tool

- Sửa 06/10/2026: `live.py` từng báo 500+ "MISSING" sai trên Windows (đường dẫn `\`) và 17 dynamic modifier "thiếu" sai
  (khớp nhầm opinion modifier). Đã sửa; nếu dòng `DEFS:` đầu ra lại có `effect: 0` thì đường dẫn đang hỏng lại, đừng tin kết quả.
- `live.py` mục "IDEAS defined but never granted" là danh sách rác thật, không phải báo nhầm
  (xem known-issues).
- `tools/check_static.py` và `tools/audit_mod.py` hardcode đường dẫn máy (`D:/SteamLibrary/...`,
  `d:/HOI4Mods/md_vietnam`). Muốn chạy phải sửa hằng số hoặc dùng bộ `tools/audit/` portable thay thế.
- `tools/audit/md_ref/` chỉ chứa dữ liệu MD của Việt Nam (12 state, vài file effect). Không đủ để xác nhận
  token MD khác. Muốn chắc, grep bản MD cài trên máy.
- Không script nào kiểm: dùng đúng scope, thứ tự `FROM`/`PREV`, logic gate, balance số liệu ngoài trục quân sự,
  getter loc sai chính tả, tooltip hiển thị đúng hay không. Cần đọc code (xem [bug-patterns.md](bug-patterns.md))
  và chơi thử.

## Kiểm tra trong game (tối thiểu)

1. Thêm "Millennium Dawn - Vietnam" vào playset **sau** MD, khởi động một lần.
2. Mở `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`, tìm `VIE`, `vie_`, `power_balance`,
   `on_action`, `game_rule`, `md_vietnam`, sửa hết trước khi chơi.
3. Chơi VIE 2000, bật `debug`, dùng `focus.autocomplete` kiểm focus mới; event chạy bằng
   `event vie_xxx.N`. Chi tiết và checklist theo hệ thống ở `tools/TESTING.md`.

## Quy tắc khi sửa tool

- Tool dùng thư viện chuẩn, đường dẫn tính từ vị trí script (`os.path.dirname(os.path.abspath(__file__))`),
  không hardcode ổ đĩa. Chạy được từ thư mục bất kỳ trên Windows và Linux.
- Chuẩn hoá `\` thành `/` trước khi so sánh đường dẫn.
- Sửa tool thì chạy lại trên cây hiện tại và so kết quả với trước đó. Không làm yếu một kiểm tra để cho nó "xanh".
- File `.json` do `audit.py` sinh ra nằm trong `.gitignore`, đừng commit.
