# Sửa error.log VIE — v61, 14/10/2026

## Kết quả

Đã sửa script, generator, font và bộ kiểm tra trong checkout. Giữ nguyên các
thay đổi layout v58/v59/v60 của người dùng, 291 focus toàn cây và 74 node chính
trị. **Focus hot reload lúc 20:02 báo `no errors`; chưa nghiệm thu toàn bộ
mod sau khởi động mới hoặc so sánh hai playset.** Phiên HOI4 mở từ
18:56 được giữ nguyên, không đóng game hoặc thay playset/save của người dùng.

Log trước sửa: phiên mở từ 18:56, bản sao đến 19:44:33 ngày 14/10/2026, HOI4
`Operation Postern v1.19.3.0.c01a (dbf6)`; 612 dòng, 96.440 byte. Phần khởi
động ban đầu có 590 dòng; hai lần hot reload cũ bổ sung 22 dòng.
[Bản sao nguyên log](.claude/docs/error-log/v61/error_before_fix.log) và
[manifest bảo toàn](.claude/docs/error-log/v61/manifest.json) lưu hash SHA-256.
Log này không phải bằng chứng nghiệm thu bản sửa. [Log sau focus hot reload
20:02](.claude/docs/error-log/v61/error_after_focus_reload.log) giữ cả lỗi cũ;
chỉ block reload cuối báo focus/bookmark `no errors`. Không có bằng chứng các
scripted trigger, event, font hoặc gameplay đã được nghiệm thu sau restart.

## Thay đổi

| Nhóm | Sửa | Bảo toàn |
|---|---|---|
| PP | 260 trigger đổi `political_power` thành `has_political_power` trong focus, trigger, decision và event; generator chuẩn hóa input cũ trước khi thêm gate | Toán tử, ngưỡng, lớp NOT, các effect `add_political_power`, giá/timer/RNG |
| Generator | Không tự đổi anchor/x/y hoặc di chuyển XII09; giữ thứ tự live; helper chuẩn hóa bỏ qua chuỗi/comment | Toàn bộ layout/prerequisite/mutex/cost live; sinh lại không tích lũy gate |
| XTC | `CAT_armored_fighting_vehicles`, giữ 50%/một lượt; tooltip và tên bonus khớp phạm vi; hai key trùng trong replace được gộp | ID focus/bonus và decision chương trình |
| Font | Thêm nền `garamond_12`, `cw_3d_debug` trước override, cùng path `gfx/fonts/garamond_12`, màu `0xffffffff` như vanilla | Override tiếng Việt, `hoi_33w`, load-screen, atlas và metadata FNT/DDS |
| Fixture | Chỉ nhận `has_political_power`; từ chối trigger cũ; kiểm cost PP native của decision trước khi trừ | Không sửa script gameplay để chiều theo fixture |

Đối chiếu AST với bản chụp file focus v58 trước sửa: mọi nội dung được giữ, ngoài
token PP và category XTC; changelog là comment. Sau kiểm này, người dùng tiếp
tục chỉnh layout v59/v60; kiểm generator trên bản sao của layout mới vẫn PASS.
Changelog sửa lỗi dùng v61 để giữ các dòng lịch sử mới của người dùng.
Không sửa game/Workshop, roster,
AI weight, cờ/biến save hoặc thêm migration.

## Kiểm tra đã chạy

| Kiểm | Kết quả |
|---|---|
| `python tools/audit/politics_runtime.py` | 747 kiểm PASS; 260 tham chiếu PP live, 50 phép so sánh khác nhau; biên dưới/đúng/trên với phần lẻ 0,01, NOT, focus/task/option/payment guard, AI E104 và native cost |
| `python tools/audit/error_log_regressions.py --md <MD> --game <HOI4>` | 1.086 kiểm, 0 FAIL; 222 ca biên ngân khố/số tàu; 85 category reference của tech bonus được đối chiếu provider hiệu lực |
| `python tools/audit/political_generator_regressions.py` | PASS trên bản sao tạm: tái hiện 260 input PP cũ, giữ semantics/layout/thứ tự live, lần sinh thứ hai không đổi byte; không ghi vào checkout |
| `python tools/audit/audit.py` | 291 focus; 0 prerequisite/anchor treo, tọa độ trùng, thiếu x/y, forward anchor hoặc vòng lặp |
| `python tools/audit/live.py` | Mọi mục MISSING=0, 0 event mồ côi; còn 3 idea chưa được dùng |
| `python tools/audit/ev.py` | 201 event; 0 ID trùng, mồ côi hoặc loc thiếu; 4 event ẩn được loại khỏi kiểm loc |
| `python tools/audit_loc_errors.py`, `python tools/verify_all_loc.py` | 0 lỗi cú pháp, title/desc/tooltip thiếu; 3.908 key hiệu lực |
| `python tools/audit/compare_error_logs.py --self-test` | PASS: bỏ giờ/ngày/số dòng script, giữ số lần lặp, lỗi mới và lỗi mất đi |
| `git diff --check` | PASS |

Nguồn provider đọc trực tiếp: MD Workshop
`D:/SteamLibrary/steamapps/workshop/content/394360/2777392649`, game tại
`D:/SteamLibrary/steamapps/common/Hearts of Iron IV`.

Audit font áp ưu tiên đường dẫn VIE > MD > vanilla, không lấy font nền từ file
vanilla cùng đường dẫn đã bị che. Fixture chứng minh phát hiện thiếu nền, nền
đặt sau override, thiếu FNT/DDS, hỏng header và lệch atlas. Garamond vanilla dùng
`common ... pages=1` và `char ... page=0`, không có dòng `page ... file=...`;
audit nhận đúng định dạng này và vẫn yêu cầu cặp prefix FNT/DDS, header và kích
thước atlas khớp. Không chỉnh metadata hoặc glyph.

Số kiểm hồi quy thay đổi so với v56 vì các kiểm provider font được nhóm thành
một kết quả mỗi consumer; vẫn kiểm FNT, DDS, single atlas, glyph page và kích
thước. Không so sánh số lượng kiểm như thước đo chất lượng.

## Lỗi còn theo dõi và chẩn đoán nguồn

| Diagnostic trước sửa | Số dòng | Bằng chứng và trạng thái |
|---|---:|---|
| Invalid/Unknown trigger PP | 528 | 520 dòng startup ở 260 vị trí, cộng 8 dòng trong hai reload cũ; script đã sửa, focus reload mới không lỗi, còn chờ khởi động mới |
| Category XTC không biết | 3 | Một dòng startup và hai reload cũ; provider mới đã xác minh, focus reload mới không lỗi, chờ tooltip/tech bonus trong game |
| Thiếu hai font | 2 | VIE ghi đè `interface/fonts.gfx`; đã bổ sung nền, chờ runtime |
| Lệch font base/lineHeight | 5 | Chờ so sánh MD riêng và kiểm chữ; không chỉnh FNT trong đợt này |
| `recruit_character` trong event | 18 | Lịch roster giữa chiến dịch đã biết; giữ nguyên, chờ kiểm xuất hiện nhân vật |
| `supply_state_category` | 8 | Có token này trong history state MD, ví dụ `39_Schleswig_Holstein.txt:29`; chưa có log baseline MD riêng |
| Support unit thiếu type support | 9 | Định nghĩa trong MD `common/units/MD_regimental_support.txt`; chưa sửa upstream |
| Unknown ship equipment đồ họa | 21 | Không có consumer tương ứng trong thay đổi này; nguồn graphics hiệu lực và baseline còn cần đối chiếu |
| GUI `context_type` | 2 | Nguồn MD `02_conditional_peace_deals_scripted_gui.txt` chú thích đây là cảnh báo đã biết; không đổi sang `player_context` vì phá entry point |
| Checksum DLC | 1 | Chưa quy nguyên nhân; đối chiếu cùng DLC/version/playset |
| `Failed allocate data buffer` | 3 | Exception lobby tại 18:59:04, ngày game 2000.01.01; cần tái hiện, chưa chứng minh VIE hoặc thiếu RAM gây ra |

Ba idea chưa dùng mà audit ghi nhận:
`VIE_air8_spirit_master_of_the_skies`, `VIE_leadership_transition_penalty`,
`VIE_military_rescue_idea`. Không xóa nội dung ngoài phạm vi.

Log trước sửa không báo Invalid effect, lỗi BoP, retire hoặc schema font của
v55/v56. Không suy từ đó rằng hành vi runtime của các hệ thống đã đúng.

## Nghiệm thu runtime còn chờ

1. Người dùng lưu và thoát phiên đang mở. Giữ phiên bản HOI4 1.19.3, MD, DLC,
   cấu hình và bookmark 2000 cố định. Mỗi phiên khởi động mới phải lưu log ngay
   sau phép thử, trước khi khởi động phiên kế tiếp.
2. Chạy MD riêng, lưu log thành `error_md_baseline.log`; chạy MD + VIE (VIE sau
   MD), lưu `error_md_vie_after_v61.log`. Đây là bước chưa được thực hiện.
3. Chơi VIE mới; kiểm PP dưới/bằng/trên ngưỡng cho focus IX11/IX12, task cán bộ,
   option X01 và launch; phí thu một lần. E104: thiếu/đủ 10 PP, hai đợt 90/180,
   đào tạo, AI hủy hợp đồng và save/load.
4. Hoàn thành `VIE_lf_ind_xtc_program`; xem bonus 50%, một lượt, áp dụng nhóm
   AFV. Kiểm chữ tiếng Việt trên focus, tooltip, decision và load-screen; kiểm
   hai font thiếu và năm cảnh báo metric riêng. Kiểm thêm bookmark 2017/roster.
5. Log mới phải hết trigger PP sai, category XTC và hai font thiếu; không tái
   xuất hiện lỗi BoP/retire/schema font. Giữ cảnh báo roster và lỗi ngoài VIE
   trong bảng riêng; không yêu cầu toàn bộ error.log rỗng.

So sánh log (chỉ đọc, không đổi playset/game):

```powershell
python tools/audit/compare_error_logs.py error_md_baseline.log error_md_vie_after_v61.log
# JSON ra stdout, có thể lưu làm bằng chứng:
python tools/audit/compare_error_logs.py error_md_baseline.log error_md_vie_after_v61.log --json
```

`shared` là diagnostic thấy ở cả hai phiên; `candidate_only` chưa tự chứng
minh VIE là nguyên nhân. Với exception lobby, thử lại cùng thao tác và lưu
error/system/game log cùng thời điểm trước khi phân loại nguyên nhân.
