# Thiết kế và tái cấu trúc nhánh focus VIE

Đọc khi thêm một cụm focus, làm lại bố cục/quan hệ hoặc review thiết kế. Đây là
các nguyên tắc tái sử dụng từ công nghiệp v17; số focus, tọa độ, năm và reward
của đợt đó không phải khuôn bắt buộc cho nhánh khác.

## 1. Quan hệ và điều kiện

- Hai khối prerequisite riêng là **AND**; nhiều focus trong một khối là **OR**.
  Kiểm từng khối, không gộp danh sách cha rồi coi tất cả là AND.
- Phụ thuộc nội bộ cụ thể phải hiện bằng prerequisite. Nếu B cần A nhưng đang
  cùng hàng, đưa B xuống dưới; không dùng available để giấu quan hệ hoặc làm phẳng cây.
- Ngành/doanh nghiệp cùng tồn tại có lối vào độc lập khi nội dung cho phép.
  Chỉ nối khi có lý do năng lực hoặc lịch sử thực sự.
- available giữ điều kiện ngoài nhánh, ngày, cờ kết quả và ngưỡng năng lực.
  Tooltip nêu đúng tên focus ngoài nhánh, có thể tham chiếu `$VIE_<id>$`.
- Ít nhất N nhóm là ngưỡng năng lực tổng hợp: dùng trigger đã xác minh và tooltip
  rõ tiêu chí/trạng thái. Không coi đó là một prerequisite cụ thể bị giấu.

Ví dụ trung tâm chế tạo cần phụ trợ AND (Samsung OR China+1):

```pdx
prerequisite = { focus = VIE_supporting_industries }
prerequisite = { focus = VIE_samsung_partnership focus = VIE_china_plus_one }
```

## 2. Chính sách, reward và chi phí

- Dùng cặp mutex nhỏ cho chính sách thay thế nhau, khai báo hai chiều và đặt cạnh
  nhau cùng hàng. Không loại trừ các ngành/doanh nghiệp có thể cùng phát triển.
- Đánh đổi phải có ý nghĩa: tăng trưởng so với nội địa hóa, đầu tư trước so với
  bổ sung sau, lợi ích trước mắt so với rủi ro. Không chỉ thay một con số.
- Ưu tiên hỗ trợ không mặc định cấm năng lực dài hạn. Nếu hai đường cùng đạt một
  dự án, nêu rõ hội tụ, tiền đề và các khoản chi khác nhau.
- Giữ reward cũ khi chỉ tái bố trí, trừ thay đổi nội dung đã được yêu cầu/chốt.
  Bảng trước/sau phải giúp phát hiện mất reward hoặc thưởng lặp.
- cost là thời gian; PP, hỗ trợ ngân sách và giá công trình là các khoản khác nhau.
  Helper công trình MD đã thu tiền; hỗ trợ riêng phải có lý do và thu một lần,
  không lặp lại giá công trình.

## 3. Thời điểm, cờ và save cũ

- Dự án/nghị quyết có tên khớp mốc mô tả: đầu tư, xây dựng, khánh thành hay vận
  hành là những thời điểm khác nhau. Kiểm nguồn trước khi đổi ngày.
- Chính sách năng lực chung có thể mở theo tiền đề/năng lực thay vì khóa năm.
  Khi đường thay thế đã chốt, ưu tiên ngày lịch sử cho AI trong ai_will_do;
  không dùng guard AI để khóa người chơi.
- Đào tạo là chương trình, không lập tức có đủ nhân lực; pilot không thành tự chủ
  toàn ngành. Chỉ số gameplay không gắn nhãn tỷ lệ thống kê thực nếu không đo tỷ lệ đó.
- Cờ scheduler chỉ xác nhận lên lịch. Gate sau khủng hoảng đọc cờ kết quả, được
  set ở các option, fallback và catch-up/bookmark liên quan.
- Chuyển lựa chọn từ event sang focus dùng chung effect có guard kết quả.
  Event đã queue không được cấp thưởng lần nữa hoặc đảo phương án đã chọn.
- Chỉ bypass lựa chọn cũ khi có bằng chứng trạng thái, chặn phía đối lập.
  Không suy diễn kết quả từ cờ lịch hoặc tự đặt cờ chỉ để mở gate.
- Giữ ID được tham chiếu khi làm lại. Báo giới hạn nhận diện save cũ; save mới
  là chuẩn kiểm khi thay quan hệ/reward.

## 4. Bố cục và đích cuối

- Anchor là một prerequisite thật, khai báo trước con. Con thấp hơn **tất cả**
  cha; điểm hội tụ ở dưới hàng lựa chọn/tiền đề.
- Giữ phạm vi ngang đã chốt, gap cùng hàng ≥2; được tăng chiều sâu để quan hệ đúng.
  Không dời nhánh lân cận chỉ để lấp chỗ trống.
- Xếp các nhánh song song và cặp chính sách cạnh nhau khi có thể. Kiểm đường dài,
  giao cắt và chữ ở kích thước hiển thị, không chỉ kiểm trùng ô.
- Capstone công nhận nhiều hướng thành công phù hợp nội dung; tránh ép một ngành
  công nghệ cụ thể khi các ngành khác cũng đáp ứng mục tiêu.
- Với N/M nhóm, mỗi nhóm là một tiêu chí; nhóm nhiều focus cần đủ thành phần.
  Dùng count_triggers đã xác minh, tooltip ngưỡng và trạng thái từng nhóm.
  Thiết kế N/M, ngưỡng điểm và reward theo nhánh; không sao chép cố định 3/6 và 45.

## 5. Sơ đồ và kiểm định

- Diagram.net dùng XML không nén: rectangle là focus, mọi connection FROM/TO
  focus, dashed là OR, một LINK cho mỗi cặp mutex. AND vẫn là cạnh bắt buộc.
  Công cụ sinh skeleton không được ghi đè reward hiện có.
- Bàn giao sơ đồ trước/sau, bảng quan hệ/reward và nguồn mốc lịch sử khi đổi lớn.
  Hình render từ code không chứng minh routing của engine HOI4.
- Chạy lệnh thật trong [.claude/docs/validation.md](../../../../.claude/docs/validation.md);
  đọc cảnh báo dù exit code 0, đối chiếu baseline và provider MD/base game.
- Kiểm đường đạt/không đạt, hai phía OR/mutex, nhóm thiếu thành phần, ngưỡng ngay
  dưới/bằng mức yêu cầu, chi phí từng đường, event đang chờ và save cũ.
- Báo riêng kiểm file/logic tĩnh, tích hợp và runtime. Chỉ xác nhận runtime sau
  khi mở cây VIE, kiểm khóa/đường nối, hover và error.log; AI cần quan sát hành vi.
  Không dùng nochecks/ignoreprerequisites làm bằng chứng gate đúng.

Ví dụ: [thiết kế công nghiệp](../../../../VIE_industry_branch_redesign.md) và
[kiểm định](../../../../.claude/docs/industry/validation.md). Các script industry
chuyên cho fixture đó; nhánh khác phải kiểm theo đồ thị và tiêu chí riêng.

Nguồn: [Focus Tree Tool](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-tool/)
và [Design Principles](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/focus-tree-design-principles/).
Tài liệu tool giải thích ký hiệu/xuất skeleton, không yêu cầu mọi nhánh có mutex.
