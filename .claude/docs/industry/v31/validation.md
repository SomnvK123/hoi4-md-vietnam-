# Công nghiệp v31 — kiểm định ngày 09/10/2026

Triển khai trên main; game mới bắt buộc. Manifest và baseline bất biến trong thư mục này.

## File tĩnh và scenario

- Focus: 24 node công nghiệp, 19 decision kỹ thuật/17 chương trình; anchor trực tiếp khai báo trước, AND/OR, mutex hai chiều và gap >=2 đã kiểm trên tọa độ thật.
- Đủ 64 tổ hợp ngành, 20 bộ ba đều đạt 32 điểm, biên 31,9/32, không tính focus mở như bàn giao. Không bắt fab hay FDI chọn lọc.
- Đủ 8 tổ hợp vốn/ưu tiên: 80,625–84,875 tỷ có fab; 66,5–72 tỷ không fab; tối đa 8 IC/1 dockyard. Bonus nghiên cứu và các idea thay bậc đúng trần.
- Thiếu tiền, tiền đúng bằng giá, bấm/finish lặp, mất sở hữu hoặc kiểm soát/refund/thử lại, state đầy, busy slot, các slot song song được kiểm bằng evaluator đọc script thực. Fixture JSON giữ variables/flags/timer qua serialize; không thay kiểm save/load HOI4.
- Vinashin trước/sau cải cách, phí option/fallback, replay, debt HSR, catch-up; thép nội địa và FDI muộn không kích Formosa; hàng đợi lựa chọn qua cooldown; Petrolimex và thông báo không phát thưởng lại đã kiểm.
- AI bankruptcy và helper nhân lực: không xây mới khi thiếu người; state đầy vẫn có thể nâng cấp trừu tượng. Lịch sử ưu tiên FDI chọn lọc, thiết kế/OSAT.
- Localization Việt BOM, key duy nhất, getter dùng cùng trigger ngành. Không còn consumer tới 17 ID bỏ trong code game nạp.

Lệnh `python tools/audit/industry.py` chạy hợp đồng v31; hợp đồng v17 giữ trong hàm lịch sử. Audit không báo ALL PASS nếu hash focus ngoài ngành đổi. Trong lần triển khai này, các nhóm Lục quân/quốc phòng đang được sửa đồng thời: các scenario chức năng PASS, phần bảo toàn baseline FAIL có chủ đích báo khác biệt thật; không thay baseline và không khôi phục các thay đổi đồng thời. Danh sách chính xác trong `audit_logs/industry.txt` và `concurrent_focus_changes.json`.

Audit repo đã chạy và đọc diagnostic: focus không dangling/trùng/forward/cycle/missing xy; reference 0 MISSING; state/province 0 lỗi; loc 0 lỗi cú pháp/thiếu title/desc; DDS/GFX không lỗi format/texture. Cảnh báo ngoài nhánh được ghi trong log thay vì sửa gameplay khác: idea mồ côi PK-KQ `VIE_airf_branch_mismatch_idea`, loc event quân sự/chính trị cũ, event picture do provider vanilla. Tổng cây hiện tại nằm trong `audit_logs/focus.txt`; không dùng tổng dự kiến 401 khi có thay đổi đồng thời.

`live.py`/`ev.py` loại đúng file archive v31 và bản nháp `scratch/test_focus.txt` ngoài thư mục game nạp; giữ nguyên bản nháp của người dùng. Không bỏ qua file gameplay để đạt kết quả xanh.

## Tích hợp/provider và hình ảnh

`industry_assets.py <MD directory> <HOI4 directory>` tra sprite local + MD, và eventpictures vanilla. Đọc texture thật, kiểm kích thước/frame; xem contact sheet ở kích thước gốc. Đã xác minh tất cả consumer công nghiệp: focus, idea, decision và ảnh event. Provider base game chỉ đọc eventpictures.gfx dùng bởi consumer này; không coi mọi file GFX vanilla tương thích với parser PDX giản lược.

Sửa ba token focus không tồn tại sang naval_industry/industry3/diplomatic_treaty và idea hỗ trợ sang industrial_focus đã xác minh. Không có artwork mới; không sửa sprite/texture/master. Native sizes có thể khác mặc định 93x91/60x68, giữ kích thước provider thật. Sơ đồ before/after lấy baseline39 và cây24 hiện hành, đã xem PNG; drawio hai trang có thể sửa. Sơ đồ thiết kế không chứng minh đường nối engine.

## In-game — chưa thực hiện

Không có kết quả chạy HOI4 cho thay đổi này. Cần game mới, playset MD trước submod, kiểm điều kiện thật; không dùng ignoreprerequisites làm bằng chứng.

1. Xem bốn vùng, hai mutex, hội tụ Y7/Y9, title/icon ở độ zoom chơi thực tế. Kiểm hover các gate quốc tế, bàn giao và 3/6; số điểm 31,9/32.
2. Chạy 8 tổ hợp FDI × ưu tiên chip × vốn thép. Treasury trước start/finish/refund; không bị helper thu tiền lần hai. Thiếu từng nền tảng, nhân lực, thiết kế và OSAT phải chặn đúng; chip được tính khi chưa fab.
3. Kiểm state đầy và mất sở hữu/kiểm soát giữa đợt. Busy slot từng ngành, sáu ngành và nhóm chung chạy song song. Save/load khi đang đầu tư, thời gian còn lại và bàn giao đúng một lần.
4. Vinashin sớm/muộn, risk thấp/cao, popup/fallback/catch-up; giữ debt HSR. Thép nội địa không có Formosa, FDI sau 2016 không phát lại khủng hoảng.
5. Cooldown không làm mất lựa chọn thép, không đổi vốn khi event lặp. Fab và xuất khẩu ô tô chỉ thông báo; EV/Petrolimex thưởng một lần. Nước đối tác biến mất không ghi lỗi ngoại giao.
6. AI có tiền/state/nhân lực và không bankruptcy mới xây; lịch sử giữ các mốc 2013/2024/2026/2030. Kiểm getter, idea thay bậc, tooltip chương trình đang chạy và error.log.

Đây là triển khai code đã qua file/scenario/provider; nghiệm thu runtime vẫn còn mở.

## Kết quả chụp cuối

Audit tại 2026-10-09T16:55:33.522043+00:00: 353 focus toàn cây; 24 focus công nghiệp. 49 block ngoài ngành khác baseline (48 bỏ, 1 sửa), giữ nguyên các thay đổi đồng thời. Industry audit exit 1 chỉ tại guard bảo toàn; sáu nhóm scenario chức năng trước guard đều PASS. Tám audit file/provider còn lại exit 0, diagnostic đã được đọc.

`git diff --check` đã sạch trong các file công nghiệp sở hữu; còn whitespace ngoài phạm vi tại cây focus và on_actions_startup do thay đổi đồng thời. Xem log `audit_logs/diff_check.txt`; không format toàn cây.
