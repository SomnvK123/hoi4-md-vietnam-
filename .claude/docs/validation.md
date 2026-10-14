# Kiểm tra (validation)

## Sửa error.log v55 — 13/10/2026

Cập nhật v56 (14/10/2026): kiểm thêm schema cộng BoP, bốn delta helper,
thứ tự/guard retire, biên ngày roster, font nền cho override, schema font,
provider FNT/DDS và kích thước atlas. Bộ hồi quy hiện có 1.136 kiểm tra;
I1–I10 được chạy trên bản sao tạm để không ghi lại tài liệu/CSV gốc.
Chưa nghiệm thu lượt khởi động HOI4 sau v56.

Chạy `python tools/audit/error_log_regressions.py --md <MD root> --game <HOI4 root>`
để kiểm BOM/ngoặc, schema so sánh, biên ngân khố/số tàu/ngày, epoch dự án phụ,
khởi tạo BoP, 74 node chính trị, provider category, tổng bonus và roster history.
`naval_scenarios.py` hỗ trợ cả cú pháp ngắn và `var/value/compare` của engine.
[Báo cáo, lỗi audit còn mở và checklist runtime](../../VIE_error_log_fix_v55.md).
Đây là kiểm tĩnh; chưa nghiệm thu lượt chơi mới sau sửa.

Repo không có CI, pre-commit hay pytest. Kiểm tra là các script Python trong `tools/`
(audit dữ liệu chủ yếu dùng thư viện chuẩn; audit ảnh cần Pillow),
chạy tay từ gốc repo. Không có công cụ nào chạy được HOI4, nên "đã qua script" chưa có nghĩa là
"chạy được trong game". Chi tiết từng script: `tools/audit/README.md`. Kịch bản test trong game:
`tools/TESTING.md` (phần đầu là hướng dẫn hiện hành, phần sau là nhật ký lịch sử).

`live.py` và `prov.py` tự đặt stdout UTF-8, chạy được trên Windows lẫn Linux. Các script khác nếu in tiếng Việt
mà crash `UnicodeEncodeError` thì đặt `PYTHONIOENCODING=utf-8` (đã có trong `.claude/settings.json`).

## Bộ kiểm tra theo loại thay đổi

Tên lửa V5/v50 (12/10/2026): kiểm `python tools/audit/missile_scenarios.py --md <MD root>`,
xuất sơ đồ `python tools/focus_layout/missile_diagram_v5.py`.
[Kết quả, cảnh báo hidden-event và checklist runtime](missile/validation.md).
Mốc A gồm 10 focus và chuỗi nghiệm thu; mapping VCS/batch production chưa bật.

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

PK-KQ v19: chạy thêm `python tools/audit/air_scenarios.py` và
`python tools/audit/air_ai_options.py`; xuất sơ đồ bằng
`python tools/focus_layout/air_diagram.py`. Kiểm định/cảnh báo hiện hành:
[air/validation.md](air/validation.md). Fixture đọc script thực nhưng không thay
kiểm đường nối, hover, chương trình và AI trong game.

Luôn đọc kết quả thật trước khi báo "sạch". Nếu script không chạy được, nói rõ thay vì suy đoán.

Với tài nguyên hình ảnh, đọc [quy trình và profile mỹ thuật](art-style-guide/04_giai_phap_cong_nghe_va_quy_trinh_san_xuat.md)
và [skill md-art](../skills/md-art/SKILL.md). Audit DDS/GFX hiện không kiểm đầy đủ
TGA, idea picture token, decision/category icon field, đường dẫn portrait hay GUI
frame/state. Kiểm thêm consumer cụ thể và xem bản xuất ở kích thước 1:1.
Không gọi mọi reference nằm ngoài submod là lỗi; phải tra provider MD/base game.

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

## Hải quân V35.4 — cập nhật V48 — 12/10/2026

`python tools/audit/naval_scenarios.py --md <MD checkout>` kiểm 47 focus, root
chọn hướng G00/B00 loại trừ nhau, hai cột mỗi hướng và capstone hội tụ AND,
gate tàu/căn cứ, XP/mastery/CP và reward một lần,
event nghiên cứu, carrier enable, hỗ trợ 8 tỷ/365 ngày và trạng thái chờ.
Audit cân bằng cộng idea và dynamic modifier, tách organization points/factor.
`python tools/audit/naval_balance.py` là entry point cùng bộ scenario.

`python tools/focus_layout/naval_diagram_v35_4.py` xuất PNG và manifest từ live
focus, dùng Pillow và DDS đăng ký sẵn. Layout v47 đặt root G00/B00 dưới H02,
tỏa ra hai cột rồi hội tụ G03/B03; F01 cần P06 AND (G03 OR B03), F02 chỉ cần F01;
S03/L04 là nhánh tùy chọn. Cần kiểm UI/mutex/dây
nối trong game;
ảnh không phải screenshot engine. Runtime: gate mất khi focus đang chạy, carrier
bật/tắt, timer, save/load và error.log. Không migration save cũ.

Đợt 12/10/2026 sau V49: 1.292 scenario với provider MD PASS; focus tree, references,
event, province, localisation, DDS/texture/focus sprite và diff whitespace qua.
Audit ảnh local vẫn báo các event picture bên ngoài checkout; xác minh provider
riêng thay vì invent ID. Runtime chưa chạy.

## Hải quân V35.3 — 12/10/2026

Chạy `python tools/audit/naval_scenarios.py --md <đường dẫn MD>` để kiểm I08,
Special Project `sp_stealth_frigate`, unlock `stealth_frigate_hull_1`, module/slot
provider, hợp đồng 0,8 tỷ/1.460 ngày, điều kiện chờ/khôi phục và bàn giao một lần.
Fixture không xác nhận Ship Designer hoặc save HOI4 thật; cần nghiệm thu runtime.

## Hải quân V35.2 — 12/10/2026

Chạy `python tools/audit/naval_scenarios.py --md <đường dẫn MD>` để kiểm R&D 8 tỷ,
trợ cấp đúng state/province, blueprint trước hợp đồng, công nghệ/module/slot,
giới hạn một hợp đồng chạy, thời gian và giao dịch một lần; thử mất và khôi phục
căn cứ/xưởng. `--md` chạy độc lập; thêm `--game` để kiểm modifier/sprite provider.
TT400 dùng corvette, fuel tank auxiliary và CIWS front. Fixture đọc live code,
không xác nhận Ship Designer hoặc save HOI4 thật.

## Hải quân V35.1 — 11/10/2026 (ghi nhận trước bổ sung)

Hải quân V35.1: chạy `python tools/audit/naval_scenarios.py` (hoặc entry point
`naval_balance.py`). Thêm `--md <MD root> --game <HOI4 root>` để kiểm provider
modifier/category/sprite/staffing trigger. Fixture dùng live script, không
thay kiểm runtime. Kết quả và ca chơi thử ở
[VIE_naval_V35_implementation.md](../../VIE_naval_V35_implementation.md).

## Effect chính sách v32 — 10/10/2026

Chạy thêm `python tools/audit/policy_rewards.py`: reward trực tiếp, bậc idea, bảo toàn giao dịch và baseline mới. Provider: `python tools/audit/policy_assets.py <MD directory>`. [Kết quả và giới hạn runtime](policy_rewards/v32/validation.md). Fixture đọc mã thật không thay nghiệm thu HOI4.
