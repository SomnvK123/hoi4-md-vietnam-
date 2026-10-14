# Sửa error.log VIE — v55, 13/10/2026

## Kết luận

**Cập nhật v56 — 14/10/2026:** đã sửa tiếp BoP, thứ tự retire nhân vật và khai báo font theo log của lượt khởi động 23:50 ngày 13/10. Chưa khởi động lại HOI4 sau v56; không kết luận sạch runtime. Các mục v55 phía dưới là lịch sử đợt sửa trước.

## Cập nhật v56 — sửa lỗi còn lại

| Lỗi và nguyên nhân | Thay đổi | Kiểm tra |
|---|---|---|
| `VIE_bop_add_central` bị đợt sửa v55 thay nhầm trường khởi tạo vào effect cộng | Sửa đúng block thành `add_power_balance_value = { id = VIE_leadership_balance value = 0.05 }`; giữ khởi tạo 0 và hai side | Kiểm schema mọi block cộng BoP, delta của bốn helper -0,05/+0,05/-0,30/+0,30; guard khởi tạo còn nguyên |
| Hai nhân vật bị retire trước các lời gọi recruit của MD trong cùng history | Chuyển retire sau recruit; giữ ngày `< 2002.2.7`; guard `has_character` riêng cho từng nhân vật | Kiểm thứ tự, có/vắng nhân vật, bookmark 2000/2017, ngày 06/07/08-02-2002 và gọi lại không retire lặp |
| Override load-screen chứa trường màu/offset không thuộc schema override | Bỏ hai override dư trong `fonts.gfx`; giữ nguyên file `load_screen_font.gfx` có font, màu và offset hiện tại | Không còn override load-screen dư; hash file load-screen không đổi |
| `hoi_33w` có override nhưng thiếu font nền | Thêm `bitmapfont` dùng `path = "gfx/fonts/hoi_33"`; giữ override tiếng Việt | Font nền tồn tại trước override, provider FNT/DDS và kích thước atlas khớp |
| Override `tahoma_60` cũng có trường màu ngoài schema | Bỏ `color`/`textcolors` trong override; giữ fontfiles và ngôn ngữ, dùng màu từ font nền | Mọi override local chỉ còn `name/fontfiles/languages` |

### Kết quả v56

- `error_log_regressions.py --md … --game …`: **1.136 kiểm tra PASS**, gồm 222 ca biên ngân khố/số tàu; đủ 74 node chính trị live và kiểm font được GUI local gọi.
- Audit focus: 291 node toàn cây; không prerequisite thiếu, trùng tọa độ, forward anchor hoặc vòng lặp. Audit tham chiếu: 0 MISSING. Audit event: 0 ID trùng và 0 event không caller.
- Hai audit localisation: 0 lỗi cú pháp và 0 focus thiếu tên/mô tả. DDS/GFX: 0 lỗi DDS, texture thiếu hoặc sprite focus thiếu. Cảnh báo picture bên ngoài submod và loc của event ẩn được giữ như ghi chú v55.
- Audit I1–I10 chạy **trên bản sao trong thư mục tạm**: tất cả PASS trong mô hình tài liệu; 1.296 dòng, 648 hợp lệ. Hash toàn bộ file `VIETNAM_POLITICAL_*`, file event và cấu hình load-screen trong repo không đổi.
- Không sửa giá, timer, deadline, bonus, glyph, metadata `.fnt`, lịch roster, AI hoặc layout. Không sửa MD/game gốc và không thêm migration save cũ.
- Ghi chú kiểm atlas: HOI4 dùng cặp đường dẫn khai báo `prefix.fnt`/`prefix.dds`. File vanilla `hoi_33.fnt` ghi page `hoi_33_0.dds` nhưng tài nguyên thật là `hoi_33.dds`; audit đối chiếu consumer thực, header DDS và kích thước `scaleW/scaleH`, không sửa tên page hoặc glyph để làm kiểm tra PASS.

### Runtime và lỗi còn mở sau v56

Chưa kiểm chữ tiếng Việt, màn hình tải, tooltip, bookmark 2000/2017 hoặc save/load trong engine sau bản sửa mới. Log hiện có là bằng chứng lỗi trước v56; cần lượt khởi động mới để xác nhận hết lỗi.

Giữ riêng 18 cảnh báo `recruit_character` giữa chiến dịch theo lựa chọn người dùng. Cảnh báo lệch `base`/`lineHeight` của font vẫn cần kiểm runtime; không tự chỉnh metadata. Lỗi ngoài VIE và hạn chế audit không quân/tên lửa không được sửa hoặc hạ tiêu chí.

Nghiệm thu: sau khi người dùng lưu và đóng phiên hiện tại, khởi động lại playset MD + VIE; kiểm BoP cộng đúng +0,05, hai nhân vật không còn gây lỗi retire, chữ tiếng Việt ở load-screen/tooltip và log không còn lỗi schema font. Kiểm thêm bookmark 2017 và save/load. Chỉ kết luận sạch ba nhóm lỗi này khi log mới xác nhận.

## Lịch sử v55

Nguồn đối chiếu: tài liệu `documentation/effects_documentation.md` và `triggers_documentation.md` của HOI4 đang cài tại `D:/SteamLibrary/steamapps/common/Hearts of Iron IV`; MD Workshop tại `D:/SteamLibrary/steamapps/workshop/content/394360/2777392649`. Không sửa game gốc hoặc MD.

## Lỗi → nguyên nhân → cách sửa → kết quả

| Lỗi | Nguyên nhân | Cách sửa | Kết quả kiểm tĩnh |
|---|---|---|---|
| BOM được đọc thành token | BOM giữa file effects và trước `spriteTypes` | Bỏ BOM của script/GFX; giữ BOM localisation | Không còn BOM trong file script/GFX đang nạp |
| Hàng loạt `Invalid effect` | File effects không đọc được, thêm một ngoặc thiếu gây lồng effect | Sửa BOM và đóng `if` trước `else` trong `VIE_transition_regime` | Cả 206 ID từng bị log báo lỗi đều có định nghĩa ở cấp cao nhất |
| `==`, `>=` bị parser từ chối | Cú pháp ngắn không được engine hỗ trợ cho các toán tử này | Chuyển 72 phép so sánh sang `var/value/compare` | Giữ ngưỡng; kiểm 222 ca ngay dưới/đúng/ngay trên ngưỡng ngân khố và số tàu |
| `visible`, `cost`, decision tiếp theo bị đọc thành trigger | Lỗi so sánh ở guard dự án phụ làm lệch parser | Dùng `compare = equals` giữa hai biến epoch | Kiểm 9 cặp epoch và guard sau khi ghi nhận lựa chọn |
| `value` trong `set_power_balance` | Sai tên trường khởi tạo | `set_value = 0.0`, khai báo đúng hai side hiện có | Guard khởi tạo một lần và ID/side khớp định nghĩa |
| Event đọc sai block | Hai phép `date <=`, ngoặc dư ở `vie_alt.1` và `vie_disaster.1` | `NOT = { date > D }`; bỏ đúng ngoặc dư | Ngoặc cân bằng; kiểm ngày trước/đúng/sau các mốc 2013 và 2023 |
| AI gọi trigger thiếu | `VIE_hl_in_power` đã bị xóa | Khôi phục wrapper `original_tag = VIE` + trigger MD đảng Communist-State cầm quyền | Không còn callable thiếu; giữ luật enable/abort AI |
| Sáu alias BoP định nghĩa hai lần | Stub rỗng còn cạnh alias thật trong file politics | Xóa sáu stub rỗng, giữ alias thật | Không còn định nghĩa scripted effect/trigger trùng |
| Modifier/technology category không hợp lệ | Token trang bị cũ không có provider phù hợp | Thay theo bảng bonus dưới đây | Category có định nghĩa trong MD; các modifier sản xuất có provider MD |
| `cancelable` trong idea | Sai tên trường | `cancel_if_invalid = no` | Bốn idea giữ điều kiện tồn tại đã chốt |
| `interest_rate_multiplier` | Sai tên modifier MD | `interest_rate_multiplier_modifier = 0.05` | Theo công thức tiền MD, cộng 0,05 điểm phần trăm trước khi clamp lãi suất |
| Cảnh báo tuyển nhân vật lúc startup | `recruit_character` đặt trong on_action | Chuyển 12 nhân vật, guard và hai retire effect sang country history | Không còn `recruit_character` trong startup; phần history MD ngoài đoạn chèn được giữ nguyên |

## Bonus thay thế đã được duyệt

| Idea | Nghiên cứu | Trần hiệu suất sản xuất | Sản lượng |
|---|---|---:|---:|
| XTC | `CAT_armored_fighting_vehicles` +10% | +5% | 0 |
| T-1 | `CAT_light_tanks` +10% | +5% | +5% |
| Pháo tự hành | `CAT_artillery` +10%; `CAT_self_propelled_artillery` +10% | 0 | +5% |
| T-2 | `CAT_main_battle_tanks` +15% | +5% | +10% |

**Các modifier sản xuất áp dụng cho toàn bộ nhà máy quân sự.** Tổng số học khi cả bốn idea cùng tồn tại: trần hiệu suất +15%, sản lượng +20%. Đây là tổng đóng góp modifier, chưa xác nhận sản lượng thực tế hoặc trần engine trong game. Công nghệ đồng thời thuộc hai category pháo có đóng góp nghiên cứu +20%; cần kiểm tooltip engine.

Ba thưởng nghiên cứu dùng `CAT_motorized_mechanized` được chuyển sang `CAT_armored_fighting_vehicles`, giữ nguyên số lần dùng và hệ số thưởng. Cập nhật mô tả đang có hiệu lực trong localisation `replace/` để hiển thị phạm vi bonus mới. Bonus nghiên cứu thay thế là bonus công nghệ; chưa được chứng minh tương đương với tốc độ thiết kế cũ.

## Kiểm tra đã chạy

| Kiểm | Kết quả |
|---|---|
| `tools/audit/error_log_regressions.py --md … --game …` | PASS; kiểm encoding, ngoặc, so sánh biên, epoch, BoP, 74 focus live, provider category, tổng bonus, roster |
| `tools/audit/audit.py` | 291 focus toàn cây; 0 prerequisite thiếu, trùng tọa độ, forward anchor hoặc vòng lặp |
| `tools/audit/live.py` | 0 MISSING trên các nhóm được kiểm; 0 event mồ côi |
| `tools/audit/ev.py` | 144 event; 0 ID trùng; 0 event không caller |
| `tools/audit/prov.py` | Tổng lỗi 0 |
| `tools/audit_loc_errors.py` và `tools/verify_all_loc.py` | 0 lỗi cú pháp; 0 focus thiếu tên/mô tả |
| `tools/audit_dds_and_gfx.py` | 0 lỗi DDS, 0 texture thiếu, 0 sprite focus thiếu |
| Provider picture event | Tất cả picture được gọi có định nghĩa trong submod/MD/game gốc |
| `VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3` | I1–I10 PASS trong phạm vi mô hình tài liệu; 1.296 dòng, 648 hợp lệ; không phải kiểm engine |
| `tools/audit/naval_scenarios.py --md … --game …` | 1.375 scenario PASS; fixture đã hỗ trợ schema so sánh của engine và vẫn từ chối operator không biết |
| `tools/audit/lf_balance.py` | PASS; script này kiểm cân bằng lục quân cũ, không thay kiểm bonus mới |
| `git diff --check` | PASS |

Hash của tất cả file `VIETNAM_POLITICAL_*` không đổi sau khi chạy lại generator/audit. Giữ nguyên tài liệu nguồn, BLUF, tham chiếu repo, giá/timer/deadline và các CSV. Các thay đổi người dùng đang có được giữ lại; không reset working tree hoặc commit.

## Điểm còn mở

- **Runtime chưa nghiệm thu.** Log của phiên mở từ 23:15 tiếp tục ghi `Invalid effect` khi reload decision/focus lúc 23:45. Log có reload các consumer nhưng chưa cho thấy engine đã nạp lại toàn bộ scripted effects sau sửa. Các dòng đó không chứng minh bản sửa đã chạy sạch hoặc vẫn lỗi khi khởi động mới.
- Các event tuyển thêm quân nhân giữa chiến dịch vẫn giữ nguyên lịch và `recruit_character`. Cảnh báo từ engine về lời gọi này vẫn cần kiểm các đợt chuyển roster; không chuyển chúng về đầu game, vì làm vậy sẽ thay lịch xuất hiện nhân vật.
- `air_scenarios.py` không chạy được do còn trỏ tới file tách `VIE_md_effects_air_force.txt` đã không tồn tại. Đây là hạn chế của audit hiện tại; không kết luận không quân PASS.
- `missile_scenarios.py` FAIL tại `six programs same row`: kiểm layout hiện tại không khớp hàng cố định mà fixture mong đợi. Không đổi layout tên lửa hoặc hạ tiêu chí để cho qua trong đợt sửa parser.
- `live.py` báo hai idea chưa có caller: `VIE_air8_spirit_master_of_the_skies`, `VIE_military_rescue_idea`. Không xóa nội dung chưa được yêu cầu.
- `ev.py` báo hai event thiếu loc (`vie_msl.20/.30`); cả hai là event ẩn. Audit ảnh báo 139 lượt picture nằm ngoài submod; provider đã được xác minh nên không sửa chúng.
- Country history là bản override dựa trên file MD đang cài. Khi cập nhật MD, cần đối chiếu lại phần upstream. Save cũ chưa có roster/flag không được tự bổ sung bằng startup nữa; nghiệm thu dùng lượt chơi mới. Chưa thêm migration save cũ.
- Font, checksum DLC, state hoặc thiết bị ngoài VIE trong log được giữ riêng; không sửa MD/game gốc.

## Checklist nghiệm thu HOI4

1. Lưu và thoát phiên đang mở, khởi động lại đúng playset MD + VIE, bắt đầu VIE năm 2000. Giữ log cũ để so sánh theo thời gian.
2. Kiểm roster quân đội/không quân, BoP khởi tạo 0 với đúng hai side, cohesion và decision chọn chương trình.
3. Kiểm guard dự án phụ: hoàn tất chương trình, chọn một lần trong epoch, không chọn lại cùng epoch; epoch tiếp theo mở theo điều kiện hiện có.
4. Kiểm biên ngân khố, số tàu, ngày 2013/2023, điều kiện AI trước/sau đổi đảng cầm quyền và các event từng lỗi.
5. Kiểm tooltip bốn idea, bonus công nghệ/phạm vi sản xuất và +0,05 điểm phần trăm lãi suất. Save/load không reset BoP hoặc tuyển lặp roster.
6. Chơi tới các đợt bổ sung/chuyển roster và kiểm nhân vật thực sự xuất hiện; ghi lại cảnh báo liên quan.
7. Đọc `error.log` mới. Chỉ kết luận sạch runtime sau khi không còn lỗi VIE thuộc phạm vi sửa; phân loại riêng các cảnh báo bên ngoài submod.
