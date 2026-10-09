# Cơ cấu lực lượng lục quân v28 — 09/10/2026

Sơ đồ người dùng gửi được dùng làm tham khảo nội dung. Thiết kế áp dụng cách hiểu độc lập là mỗi hướng có chuỗi tổ chức, phát triển và hoàn thiện riêng; vẫn chọn một ưu tiên trong ba hướng, như chú thích ở ảnh. Nếu chuyển sang phát triển đồng thời cả ba, cần thiết kế lại các cờ sở trường, bonus và gate phía dưới, vì hiện chúng đọc một ưu tiên cơ cấu.

## Nội dung hiện hành

| Bước | Cơ giới hóa | Cơ động nhẹ | Địa phương và dự bị |
|---|---|---|---|
| 1 | Ưu tiên lực lượng cơ giới hóa | Ưu tiên lực lượng cơ động nhẹ | Ưu tiên lực lượng địa phương và dự bị |
| 2 | Tổ chức đơn vị hợp thành cơ giới | Tổ chức đơn vị cơ động linh hoạt | Kiện toàn bộ đội địa phương |
| 3 | Đồng bộ trang bị cơ giới | Hỏa lực cơ động bộ binh | Chuẩn hóa lực lượng dự bị động viên |
| 4 | Bảo đảm tác chiến cơ giới | Bảo đảm cơ động trên địa hình phức tạp | Liên kết lực lượng và bảo đảm tại chỗ |
| 5 | Hoàn thiện lực lượng chủ lực cơ giới | Hoàn thiện lực lượng cơ động nhẹ | Hoàn thiện lực lượng phòng thủ địa bàn |

Mỗi focus sau ưu tiên chỉ cần cha trực tiếp trong chuỗi của nó. Ba focus ưu tiên loại trừ từng cặp; ba đích hoàn thiện không có mutex riêng. Cải cách chỉ huy II có một khối prerequisite OR chứa ba đích hoàn thiện. Hàng Cơ động chiến lược / Phòng thủ khu vực và dự bị cũ được thay bằng hai đích tương ứng; ID `VIE_lf_dev_strategic` và `VIE_lf_dev_territorial` được giữ để các caller hiện có tiếp tục hoạt động.

## Bố cục và gate

- Ba hướng xòe thành hình quạt: hàng lựa chọn ở x=168 / 180 / 192, thu dần qua các hàng 9–12 đến x=176 / 180 / 184. Cải cách II vẫn ở trục giữa (180,13).
- Kiện toàn Công binh ở (186,4) mở focus huấn luyện Công binh tại (186,5). Hiệp đồng binh chủng xuống (180,6), sau toàn bộ hàng huấn luyện y=5; Cải cách I ở (180,7). Mọi focus Lục quân được neo vào một prerequisite trực tiếp đã khai báo trước.
- Gate ba trong bốn binh chủng, gate hai trong ba lĩnh vực và mốc mở N1 được giữ. Nhánh có 38 focus; Công binh có focus tổ chức riêng và focus huấn luyện riêng. Mọi vị trí focus ngoài Lục quân được giữ.
- `structure_v28.json` ghi đủ tọa độ tuyệt đối, hàng hiển thị, anchor trực tiếp, nhóm prerequisite AND/OR, mutex và `available` của cả 38 focus; audit so từng trường với code hiện tại.
- Chương trình Phản ứng nhanh mở sau đích cơ giới hoặc đích cơ động nhẹ; Động viên toàn dân mở sau đích phòng thủ địa bàn. Các cờ `regular/mobile/depth` vẫn là cờ ưu tiên duy nhất cho phần năng lực phía dưới.

## Effect theo chức năng

Reward được chia từ các tổ hợp cơ cấu cũ tương thích: FR1+FR2+PS, FM1+FM2+PS và FD1+FD2+PT. Tổng modifier động của mỗi hướng không tăng; XP/mastery lần lượt là 65 / 65 / 50. Đây là hợp đồng của riêng ba chuỗi cơ cấu, không phải tuyên bố rằng toàn bộ modifier của quân đội đã được kiểm chứng trong game.

Các bước tổ chức mở mẫu đơn vị có guard chống định nghĩa lặp, để người chơi tuyển và trang bị. Nhánh cơ giới có mẫu hợp thành dùng bộ binh cơ giới, thiết giáp và pháo tự hành; nhánh nhẹ có mẫu bộ binh nhẹ và công binh; nhánh địa bàn có mẫu bộ binh bảo vệ khu vực. Các chuỗi cơ cấu không còn thưởng ngay sư đoàn đầy trang bị, tiền, kho vũ khí, quân số hoặc công trình phòng thủ. Phần nền tảng binh chủng và năng lực phía dưới vẫn dùng effect hiện có.

Đồng bộ trang bị cơ giới cấp bonus nghiên cứu 25% một lần cho `CAT_main_battle_tanks`, có định nghĩa trong dữ liệu MD tham chiếu. Các bước bảo đảm giảm tiêu hao; dự bị tăng hệ số tuyển quân; hoàn thiện cấp modifier hợp đồng theo vai trò. Mô tả national spirit đã được đổi cho phù hợp các hướng mới.

## Save và kiểm tra

Giữ cả 30 ID cũ, thêm tám focus. Save đã hoàn thành focus giữ reward đã nhận; không tự hồi tố hoặc thu hồi reward cũ. Người chơi đang giữa chuỗi có thể phải hoàn thành thêm các bước mới. Save từng hoàn tất một đích cũ vẫn có prerequisite mở Cải cách II theo ID được giữ.

`python tools/audit/land_structure.py` đọc script thực, kiểm ba chuỗi, mutex, thiếu cha, cấm mở C2 sớm, tổng biến, XP/mastery và template guard. `lf_balance.py` chứa bảng tính lịch sử 30 focus; nó không đọc modifier/national spirit hiện hành và không thay thế kiểm tra mới. Xuất PNG bằng `python tools/focus_layout/land_diagram.py`.

Cần kiểm tra HOI4: hover/đường nối, khai thác template với trang bị có thật, XP/mastery, hiệu ứng priority spirit và save giữa chuỗi. Kiểm tra tĩnh không chứng minh các phần này đã chạy đúng trong game.

Static validation: land_structure.py PASS (38 focus; tapered pyramid layout, 32 reachable 3-of-4 training states, 12 reachable 2-of-3 capability states, direct anchors, minimum gap 2, zero connector crossings); audit.py: 432 focus, no dangling prerequisites, duplicate coordinates, forward anchors or cycles; live.py: 0 missing references (one unused legacy air-force idea remains); localization audit: 0 errors and all focus titles/descriptions present. PNG 1894×3109 exported and visually inspected. In-game validation not run.
