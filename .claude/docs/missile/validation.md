# Tên lửa V5: triển khai và kiểm định

Ngày: 12/10/2026. Nhánh: `missile-v5`. Header cây: v50.
Kế hoạch: [VIE_missile_V5_implementation_plan.md](../../../VIE_missile_V5_implementation_plan.md).

Mốc A đã được code: 10 focus với 15 cạnh AND, sáu chương trình cùng Y=4,
ba Decision bảo dưỡng lặp, ba chương trình 180 ngày với callback ẩn,
ba tinh thần vĩnh viễn và ba chu kỳ bảo dưỡng có hạn. Cây 408 → 418 focus.
M09 thay các tinh thần cũ; không cộng chồng, không cấp trang bị hoặc nhà máy.

VCM-01 → nghiệm thu VSM-01A → tích hợp VCS-01 chạy tuần tự trong Decision.
M06/M07 vẫn có thể chuẩn bị song song qua focus. M08 cần đủ ba focus và
chứng nhận VCS; M09 cần cả hai capstone. Tổng vốn focus 9,5 tỷ USD;
ba chương trình thêm 2,25 tỷ USD và 175 PP. Chu kỳ bảo dưỡng tùy chọn,
mỗi lần 0,1 tỷ USD; không phải gate capstone.

## Kết quả kiểm file

| Kiểm tra | Kết quả thực tế |
|---|---|
| `audit.py` | 418 focus; 0 tọa độ trùng, 0 forward-ref, 0 prerequisite treo/vòng lặp |
| `live.py` | 0 MISSING ở mọi nhóm; 0 event/idea mồ côi |
| `ev.py` | 0 event ID trùng/mồ côi; hai cảnh báo thiếu loc sai cho callback ẩn |
| `prov.py` | Tổng hợp lỗi 0; nhánh mới không tạo công trình |
| `audit_loc_errors.py`, `verify_all_loc.py` | 0 lỗi; 76 key mới, đủ title/desc/tooltip |
| `audit_dds_and_gfx.py` | 0 lỗi DDS, 0 content warning, 0 thiếu texture/focus sprite; cảnh báo ảnh event cũ ngoài checkout còn hiện |
| `missile_scenarios.py --md ... --baseline ...` | **2.888 assertions PASS**, gồm kiểm bảo toàn dữ liệu cũ |
| `naval_scenarios.py --md ...` | **1.292 static scenarios PASS** |
| `git diff --check` và kiểm whitespace file mới | Không lỗi whitespace; Git có thông báo LF/CRLF cho các file hiện hữu |

`ev.py` tìm hidden event bằng regex lấy 400 ký tự sau ID. Matcher có thể
nuốt đầu event tiếp theo khi callback ngắn, làm bỏ sót `vie_msl.20` và
`vie_msl.30`. Cả ba callback có `hidden = yes`, `is_triggered_only = yes`
và effect trong `immediate`; fixture đọc block thật xác nhận điều này.
Không thêm title/option giả hoặc sửa tool cũ để che cảnh báo.

Log ở [audit_logs](audit_logs/); đây là evidence kiểm file, không là log HOI4.
Snapshot baseline tạm dùng so hash và AST trước/sau đã được kiểm;
snapshot chỉ phục vụ đợt triển khai, không là bộ dữ liệu game cần commit.

## Kiểm tích hợp provider và hình ảnh

Đã đọc MD tại `D:/ide/Millennium-Dawn`, commit
`60accbc19a19369d8c4095b40b5144d5bb6c0fd2`.
Fixture `--md` xác nhận định nghĩa category nghiên cứu, treasury effect,
sprite và texture focus/Decision/idea được sử dụng. Icon dùng lại tài nguyên
thật; không tạo sprite hoặc ảnh giả cho tên lửa.

- [Sơ đồ từ code live](missile_v5.png) và [manifest](missile_v5.json):
  đúng 1–6–2–1, 15 cạnh, tọa độ/anchor/cost/icon từ script.
- [Board icon kích thước gốc](reused_icons_native.png): đã xem icon 93×91;
  giữ nguyên DDS gốc. PNG sơ đồ là preview, không là screenshot engine.
- Sáu lớp AI đã rà: bổ sung focus weights trong Historical/Hardline và
  AI Decision; chưa thêm equipment/template/theater/navy mới vì không có
  consumer trang bị mới ở mốc A.

Mapping VCS chưa được xác minh; hai Decision batch/công suất chỉ hiện debug,
available false, không thu PP/vốn và không giao equipment. Không có designer
tên lửa ráp module trong các định nghĩa MD đã khảo sát. Không dùng
`guided_missile_equipment_2` giả danh Trường Sơn. Mốc B chưa bật.

## Runtime chưa kiểm

**Chưa chạy HOI4**, chưa kiểm timer/save-load/civil-war/AI thực hoặc connector
dài từ root quân sự đến M00. Fixture mô phỏng điều kiện và giao dịch,
không thực thi engine và không chứng minh tương thích DLC qua chơi thật.
Khuyến nghị game mới, không có migration save cũ.

Checklist nghiệm thu trong game:

1. VIE 2000, submod sau MD, kiểm Gotterdammerung bật/tắt và error.log.
2. Kiểm sáu node cùng hàng, AND và gate M08; kiểm cạnh dài từ X=202 đến X=284.
3. Start từng chương trình bằng PP/vốn thật, chặn sai thứ tự hoặc chọn lặp.
4. Save/load giữa timer 180 ngày và sát ngày hoàn tất; callback chạy một lần,
   clear in-progress, không thu tiền lần hai hoặc mất tiến độ khi visible đổi.
5. Bảo dưỡng tồn tại/cooldown 365 ngày, hết hạn chọn lại, không farm XP/đạn.
6. M09 gỡ hai spirit cũ, giữ timed maintenance và trần tổng 2,5% XP gain
   mỗi quân chủng; kiểm doctrine-aware reward trước/sau chọn doctrine.
7. Historical/Hardline tích lũy PP/vốn, chọn ba Decision và đạt capstone.
   Người chơi thường không thấy hai integration stub.

Nếu phát hiện timer/callback không vận hành đúng, sửa lifecycle trước khi
nghiệm thu runtime; không bỏ cờ VCS để mở M08 bằng đường tắt.
