# Chính trị v57 — adapter game, 14/10/2026

**Cập nhật v61 (14/10/2026):** đã sửa 260 trigger kiểm PP sang
`has_political_power`, sửa nguồn sinh và fixture từ chối token cũ. Generator
giữ layout/thứ tự live v58/v59/v60; kiểm bản sao tạm với input cũ và sinh hai lần không tích
lũy gate. Hiện `politics_runtime.py` có 747 kiểm PASS. Chưa nghiệm thu engine
sau restart; focus hot reload lúc 20:02 không lỗi parser.
[Báo cáo v61](VIE_error_log_fix_v61.md) ghi provider đã xác minh và
checklist runtime. Các số kiểm và giới hạn provider bên dưới là lịch sử v57.

Đã triển khai các thay đổi đã chốt vào script game của checkout. Đây là bản kiểm
script, **chưa nghiệm thu một lượt HOI4**. I3/I10 của mô hình vẫn REVIEW, không
đổi thành PASS cân bằng chỉ vì đã có code.

## Hành vi đã triển khai

- E103 là thông báo tiến độ ngày450, chỉ có nút tiếp tục. Chương trình tự chấm khi
  đủ bốn nhóm chứng cứ sau thực thi/kiểm chứng; trượt690 không ép partial. Thưởng
  sớm70PP, mốc600/690 inclusive; deadline900, một kết quả/tier/reward mỗi epoch.
- Chương trình có các task trả PP/ngân khố theo B1, timer chuẩn/cấp tốc đã ký.
  Cán bộ cần gắn kết≥55 liên tục90ngày; công vụ cần `treasury_rate≥0` liên tục90ngày;
  kiểm tra cần giảm corruption so baseline hoặc giữ bậc đáy; dân vận cần nghiệm
  thu hai dự án tại518/526 và GDP/người≥104% baseline. Mất kiểm soát địa bàn dừng task.
- E102-C thêm đủ90ngày vào chuỗi, không chạy song song để mất tác dụng. Cổng chọn
  C đọc dự báo từ phần việc còn lại và thời gian đã chờ, khóa tổng>840. Start≤800,
  khởi động≤270. Nếu chưa có mode khởi động hợp lệ, phục hồi trước khi chốt kiểm tra;
  có thể đổi trọng tâm chưa khởi động, không hoàn tiền hoặc mở lại chương trình đã chạy.
- Cấp tốc trả giá chuẩn theo tier/gắn kết cộng55PP+0.50ngân khố hoặc25PP/−16gắn kết
  khi vượt phản đối. Trả đủ hai khoản thương lượng được gộp tại launch; không thu lại
  trên từng task. Snapshot trước dịch chuyển BoP giữ nguyên timer cho lần chạy hiện tại.
- E104 ký21/25/30ngày, không phát hỗ trợ ngay. Mỗi đợt kiểm chứng90/180ngày cần
  cấp10PP trước khi đợt kết thúc. Qua cả hai mới trả hỗ trợ chưa nhận; bỏ một đợt
  mất hỗ trợ/quyền chưa dùng và gắn kết−6 một lần. Đào tạo90ngày chỉ trả25PP khi
  đã hoàn tất và đủ hai đợt kiểm chứng. Hủy không thu hồi tiền/thưởng đã nhận.
- Điều khoản sửa E104 được đối tác chấp nhận trước trong chính đề nghị ký; không
  tạo xác suất chấp thuận mới chưa có trong B1. XIII12 sửa chỉ khi còn lợi ích,
  đặt lại hai đợt kiểm chứng và mở XIV11 cho đúng contract epoch; hủy khóa reader đó.
- IX11 có hai kết quả65/35; XI10 có70/30 sau90ngày tái cơ cấu. Kết quả ghi một lần,
  không reroll hoặc nhận lại tài sản khi load/callback lặp. XI09 cần90ngày thực thi
  trước thu hồi tài sản, không trả tiền ngay khi mở focus.
- X01/XII02 có phương án trả cohesion và gate XI05/XIII09; XII12 quyết định gate
  XII09. Bàn giao tuần tự khóa XII09 trong kỳ XII, có thể mở lại sau sang kỳ XIII.
  Prerequisite nguồn được thêm vào reader; XII09 được đặt sau XII12 trên cây.
- Consumer gọi tại completion của reader thật: hồ sơ A hoàn trả8PP, B hoàn trả0.20
  ngân khố một lần. Hồ sơ chưa chốt trước reader không được trả hồi tố. Archive XIV→XV
  chỉ lưu, không có gameplay/rebate. Đối tượng adapter là hồ sơ quốc gia VIE gắn với
  node nguồn; không giả lập nhiều đối tượng doanh nghiệp bằng một cờ chung.
- Popup E102/E104 có ID gắn kỳ nguồn; popup XIII12 có ID gắn contract epoch.
  Callback cũ không dùng ledger mới. Chỉ một programme được khởi động mỗi nhiệm kỳ.
- Side project chỉ mở sau full sớm và còn đủ270+100ngày trước chuẩn bị đại hội sau;
  callback đọc đúng programme epoch. Họp phục hồi vẫn là action riêng, không bị cổng
  trọng tâm khóa.

## Nguồn code và tái tạo

| Thành phần | File trong checkout |
| --- | --- |
| Generator, giữ phần ngoài nhánh chính trị | `tools/build_political_runtime.py` |
| Task/consumer/clock/signature/obligation | `common/scripted_effects/VIE_md_effects_politics_runtime.txt` |
| Trigger giá, thời gian và điều kiện kiểm chứng | `common/scripted_triggers/VIE_md_triggers_politics_runtime.txt` |
| Task/fee/reopen/change trước launch | `common/decisions/VIE_md_politics_runtime_decisions.txt` |
| Choice, callback ID gắn kỳ/hợp đồng, clock | `events/VIE_md_politics_runtime_events.txt` |
| Cây74node, resolver và event cũ được nối lại | `common/national_focus/VIE_md_focus.txt`, `VIE_md_effects_politics.txt`, `VIE_md_politics_events.txt` |
| Loc mới và các key cũ sửa lại | `localisation/english/VIE_md_politics_runtime_l_english.yml`, `VIE_md_politics_l_english.yml` |
| Fixture đọc script game thật, từ chối statement không hỗ trợ | `tools/audit/politics_runtime.py` |

Chạy `python tools/build_political_runtime.py` để tái tạo adapter từ B1. Sinh lại
không làm đổi file. Bộ chọn backdrop/sprite dùng ID hiện có; không tạo artwork mới.

`treasury_rate`, `gdp_per_capita` và các bậc corruption được đối chiếu với nguồn MD
đã lưu ở `tools/audit/md_ref/00_economic_triggers.txt` và `00_budget_effects.txt`.
Không có game/MD tại hai đường dẫn máy cũ ghi trong repo, nên chưa kiểm provider
với một installation sống hoặc engine1.19. Gói ZIP thiết kế là gói review/tái tạo
mô hình, **không phải mod có thể cài độc lập**; code game nằm trong checkout.

## Kiểm đã chạy

- `python tools/audit/politics_runtime.py`: 351 kiểm PASS. Có đường chuẩn/cấp tốc
  cả bốn programme, delay C, biên tiền/690/600/270/840, mất địa bàn, streak bị phá,
  thiếu phí, sign/payout/training, RNG hai nhánh, stale popup và nhận lại thưởng.
- `audit.py`: không prerequisite/anchor treo, không trùng tọa độ, forward anchor
  hoặc vòng lặp; vẫn74node chính trị và291focus toàn cây.
- `live.py`: mọi mục MISSING=0. Ba idea chưa dùng còn lại là nợ cũ ngoài thay đổi này.
- `ev.py`: không ID trùng/mồ côi, không thiếu key loc được tham chiếu. Audit này
  kiểm key thật thay vì giả mỗi event bắt buộc dùng prefix ID riêng.
- `audit_loc_errors.py`, `verify_all_loc.py`: không lỗi loc hoặc thiếu title/desc.
- `git diff --check`: sạch. Không chạy console/engine/AI/playtest để thay kết quả đó.
- DDS/GFX:0lỗi định dạng/nội dung DDS,0texture thiếu,0sprite focus tùy chỉnh thiếu.
  Category `GFX_decision_category_power_struggle` và195lượt tham chiếu picture chung
  nằm ngoài provider local của audit. Chưa có MD/game sống để xác minh các sprite
  ngoài checkout; không đổi sang ID tự đoán hoặc coi file audit là kiểm UI trong game.

## Nghiệm thu trong game còn lại

1. Chạy playset mới VIE2000, MD trước submod; kiểm `error.log`, mở BoP/decision,
   thử chuẩn/cấp tốc và giữ popup E102 qua một mốc đại hội để kiểm nguồn kỳ.
2. Làm đủ task, phá streak ở ngày cuối; GDP chưa tăng phải partial ở900. Kiểm cả
   baseline corruption đáy để không nhận bồi hoàn PP của helper MD.
3. E104: chờ ký, cấp phí hoặc bỏ từng đợt; làm/hủy đào tạo; sửa/hủy XIII12; save/load
   giữa ký,90/180 và payout. Kiểm hỗ trợ/reward không phát hai lần.
4. Kiểm gate X01/XII02/XII12/XIII12 và hai nhánh RNG; kích thước chữ/UI, dây cây,
   reader thiếu hồ sơ, thứ tự source trước reader, party-rule và chuyển tag khi nội chiến.

Chưa cung cấp migration cho programme đang chạy theo script cũ. Nghiệm thu bản này
trên lượt chơi mới trước khi coi save đang chạy theo v56 là tương thích.
