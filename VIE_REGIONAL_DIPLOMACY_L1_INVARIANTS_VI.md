# L1 — Bảng bất biến và kiểm bàn giao

**Phạm vi các kiểm dưới đây: baseline 51 node trước mở rộng C.** Ứng viên C mới có 18 node, toàn nhánh 63; [đặc tả và kiểm riêng](VIE_CHINA_EXPANDED_BRANCH_DESIGN_VI.md). H1 PASS baseline không chứng nhận ứng viên mới hoặc SVG tổng mới; J2/J5 vẫn FAIL.

J1/J4 PASS ở mức hợp đồng thiết kế và phép tính, không chứng minh engine. J2 và J5 giữ FAIL; chưa đóng L1, chưa sang L2.

| Bất biến | PASS/FAIL | Phép tính / bằng chứng |
|---|---|---|
| J1 | PASS | Ba giao diện thiết kế G/P/C có writer, consumer, hiệu ứng và tooltip; root OR nguồn thật=True/True; 9 mục C/E đọc gate. Không có script game ngoại giao mới; T tier/kiêm nhiệm hoãn, không tính active. |
| J2 | FAIL | G có 16 ca đối chứng đường mặc định/bỏ F02; C: 60−8=52<55, phục hồi 30PP mở lại. P chỉ đổi chuẩn bị 15 ngày, chưa chứng minh đổi lựa chọn. Người dùng chọn giữ lịch, J2 FAIL và L1 mở; không đổi định nghĩa. |
| J3 | PASS | Đọc JSON trực tiếp; bảng ký/bands khớp tài liệu=True/True; drift=[]; nguồn đổi=[]. |
| J4 | PASS | 7/7 cụm có đúng kỳ và nhãn giả định gameplay; R0 IX+(F02 OR mặc định)=True. B1=X, S1=XIII với phạm vi tách XIII05–08; không coi là năm hình thành quan hệ. |
| J5 | FAIL | NỢ ĐÃ BIẾT: ownership biển/S-vs-XIII05–08/W-vs-X05–X08/hợp đồng ghi ngay trong plan 19.5. E104 chỉ có kế hoạch chuyển riêng19.6, sau C qua kiểm; chưa chuyển/kiểm thật nên J5 giữ FAIL. |
| D1 | FAIL | Chưa chứng minh mọi chương trình: C sâu có trade opinion cao hơn; quyền sâu E/S chưa có consumer đo được. |
| D2 | FAIL | Chưa có ngưỡng hoàn vốn người dùng chọn; trade opinion/research chưa định giá; gom PP không là hoàn vốn. |
| D3 | FAIL | Đúng một chương trình/cụm: phí tháng nhỏ=0.15, sâu=0.32; không có thu treasury. r là PP/ngày; M/E/W có thể nhiều chương trình. |
| D4 | FAIL | Research: 3×0.01=0.03 chạm trần nếu đủ 3 nguồn. R1 duy nhất 0.05 < trần 0.1; chưa có nguồn thứ hai. |
| D5 | FAIL | Category/điều kiện/consumer riêng JAP/KOR và USA/SOV/RAJ chưa đủ; không so bằng tên lĩnh vực. |
| D6 | FAIL | Đã nhập k và công cụ chính trị; chưa có mô hình đủ phản hồi/hủy/vướng mắc hoặc lợi ích định giá. |
| D7 | PASS | Đơn vị treasury trong tài liệu/JSON chính trị: chưa xác định; k chỉ là sensitivity, không là tỷ giá engine. |
| D8 | FAIL | Chưa định nghĩa đủ chiều có tác dụng; không dùng tên cờ cơ hội để tạo PASS. |
| N1 | FAIL | M/A/B/E/S/W chưa đủ bảy thành phần; dành L3, chưa viết lại. |
| N2 | FAIL | Chưa có event mới để thử lựa chọn rẻ nhất. |
| N3 | FAIL | Quyền hợp tác sâu E/S chưa có consumer chốt; không tính vào so thống trị. |
| N4 | FAIL | Chưa rà nguồn toàn tài liệu; không thêm mốc/nhân vật; các gate ứng viên ghi giả định gameplay. |
| H1 | PASS | catalog/layout/SVG=[51, 51, 51]; 49+2=51; edges=74; errors=[] |
| H2 | FAIL | Mâu thuẫn cũ:14.3 A04 sau A02+A03,17.1 từ C4;14.6 chưa chọn duy trì,20.3 có phí tháng;11/14 còn nói chưa có số trong khi21 có bộ thử. Chờ L4. |
| H3 | PASS | 50 anchor trước node/cha trực tiếp; relative=node-anchor; 74 cạnh con thấp hơn cha; min gap=4>=2; errors=[]. |
| H4 | PASS | Chỉ Python/XML/CSV; chưa chạy HOI4, chưa playtest hay xác nhận cân bằng. |

Catalog/layout/SVG=[51, 51, 51]; 50 anchor; 74 cạnh; gap nhỏ nhất=4.
Hình học SVG so baseline không đổi=True; PNG xuất từ SVG khớp=True.
AI: focus F02 có base=70; số tham chiếu F02 trong hai plan=0. Trọng số không chứng minh AI luôn chọn.
Đường R0 bỏ F02 vẫn mở sau đại hội=True; chỉ đọc điều kiện nền, không kéo hạn programme sang ngoại giao.

## Liên kết local hiện tại

- VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md: 19 lần xuất hiện, 17 đích duy nhất; thiếu=[].
- VIE_REGIONAL_DIPLOMACY_L1_REVIEW_VI.md: 11 lần xuất hiện, 9 đích duy nhất; thiếu=[].
