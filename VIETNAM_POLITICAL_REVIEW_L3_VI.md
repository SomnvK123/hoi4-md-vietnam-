# Kiểm thiết kế chính trị — kết quả hiện hành

Đây là kiểm mô hình giấy; [adapter game v57](VIE_political_v57_implementation.md) đã có trong repo nhưng chưa nghiệm thu HOI4/AI/playtest. Giá là giả định gameplay. Báo cáo chỉ giữ kết quả hiện hành; lịch sử xem git, dữ liệu đầy đủ xem CSV hoặc --audit-json.

E103 tự động, bỏ trục A/B/C. CSV ngân sách: **324 hàng hợp lệ**; 324 tổ hợp khóa BoP được kiểm nhưng không xuất hàng rỗng. I5: 18 ca ngoại lệ có kết quả dự báo thật. CSV node: 1095 hàng giá/quyền/Pareto.

## I1–I10

| Mã | Kết quả | Phép tính / phạm vi |
| --- | --- | --- |
| I1 | PASS | Cán bộ: 660/645 > 600 >= 555; Công vụ: 660/645 > 600 >= 555; Kiểm tra: 750/735 > 690 >= 645; Dân vận: 660/645 > 600 >= 555 |
| I2 | PASS | 55+0.5×40−70=5.0 PP quy đổi; bốn programme trong ±10 PP tại k=40; dự án phụ 270 ngày/30 PP là khoản mua thêm |
| I3 | REVIEW | Không báo PASS cân bằng từ chiều chưa có giá. 42 nhánh×k có tác dụng kiểm được; tám node đổi cấu trúc. Giá tiền vẫn báo riêng; ngày/gate không quy PP; xác suất và sở thích cần playtest. |
| I4 | PASS | Năm vùng cohesion có hệ số khác nhau; cổng sau trừ40; BoP qua0.25 làm đổi công cụ. Đây là kiểm vùng/biên, không chứng minh mỗi điểm trong cùng vùng đều đổi giá. |
| I5 | PASS | Cùng trigger: chốt khi còn đường≤270; start≤800/choice≤840. 1440probe0–39/cooldown0/90/180: cổng chung luôn còn công vụ/dân vận trước hạn, kiểm tra không kịp bị khóa riêng. 3ca phản thực full dưới sàn bị khóa; không có nhánh rủi ro E103. Biên19/20 và270/271 có bảng; không cứu hồi tố kỳ đã hết hạn. |
| I6 | PASS | 74=2+6×12; cost/ID/mutex giữ; 40đặc tả+22gate/caller/guard/reader+12lát cắt; thiếu=[]. |
| I7 | PASS | 6 tên VIE và mọi nhãn node/E101–E104 được đăng ký8.1; ID kỹ thuật chưa định nghĩa và chưa xác minh provider. |
| I8 | PASS | Mốc lịch sử có link nguồn hoặc giả định gameplay; event XI08/XIII05 đã chặn phát sớm. Neo quýIV/2022 là gameplay, không giả ngày khởi đầu khủng hoảng. |
| I9 | PASS | Kiểm mô hình và script; không chạy engine/console/playtest. Adapter game v57 có báo cáo nghiệm thu riêng. |
| I10 | REVIEW | Bỏ cờ cơ hội khỏi Pareto programme: 0 ứng viên thắng mọi đối thủ; 34 cặp thống trị. Consumer có hoàn trả PP/ngân khố thật; không dùng quyền mô tả để che thống trị. Chưa chứng minh utility/cân bằng engine. |

Phép so tiền thuần (không định giá gate/ngày hoặc tự cộng thưởng task chưa làm):

| Event | Đảo thứ hạng chi phí | Rẻ nhất mọi k |
| --- | --- | --- |
| E101 | PASS | không có lựa chọn rẻ nhất mọi k |
| E102 | PASS | không có lựa chọn rẻ nhất mọi k |
| E104 | FAIL | C |

## Cấp tốc so chuẩn

Thưởng sớm70PP; gói55PP+0.50ngân khố. Cùng central/r=1/full/cohesion66, chọn phương án rẻ nhất mỗi mode; E103 tự động cùng quy tắc (ghi E102/E103). Dự án phụ30PP là khoản mua thêm.

| Programme | k | Chuẩn E102/E103 | Cấp tốc E102/E103 | Chi chuẩn | Chi cấp tốc | Cấp tốc − chuẩn |
| --- | --- | --- | --- | --- | --- | --- |
| cadre | 20 | NA/NA | NA/NA | 137.0 | 132.0 | -5.0 |
| administration | 20 | NA/NA | NA/NA | 147.0 | 142.0 | -5.0 |
| inspection | 20 | C/AUTO | B/AUTO | 162.0 | 167.0 | 5.0 |
| social | 20 | NA/NA | NA/NA | 127.0 | 122.0 | -5.0 |
| cadre | 40 | NA/NA | NA/NA | 147.0 | 152.0 | 5.0 |
| administration | 40 | NA/NA | NA/NA | 167.0 | 172.0 | 5.0 |
| inspection | 40 | B/AUTO | B/AUTO | 192.0 | 197.0 | 5.0 |
| social | 40 | NA/NA | NA/NA | 147.0 | 152.0 | 5.0 |
| cadre | 60 | NA/NA | NA/NA | 157.0 | 172.0 | 15.0 |
| administration | 60 | NA/NA | NA/NA | 187.0 | 202.0 | 15.0 |
| inspection | 60 | B/AUTO | B/AUTO | 212.0 | 227.0 | 15.0 |
| social | 60 | NA/NA | NA/NA | 167.0 | 182.0 | 15.0 |

## Kiểm file và cổng

50/50 kiểm PASS. Không có lỗi file.

- Cổng chốt: 1440 probe cohesion0–39/cooldown0/90/180; 0 lỗi. Biên270/271 kiểm riêng; không cứu hồi tố cửa sổ đã hết.
- I5: 0 lỗi cổng trễ tất định; không có nhánh thẩm định/rủi ro E103 bỏ qua cổng840.
- Pareto XII12/XIII12: 63 cặp, 0 lỗi; 55 probe ledger XIII12. Hủy luôn mở, không thu hồi hỗ trợ đã nhận/tier/thưởng.
- Chẩn đoán: 34 cặp thống trị; 0 universal winner theo programme/tuyến, 18 theo toàn4programme. Không suy ra cân bằng theo sở thích từ snapshot.
- Biên giá nhỏ: checkpoint k40 chênh1PP; XII10 k20 chênh1PP. Không tự điều chỉnh.

## Tái tạo và gói chia sẻ

[Thiết kế](VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md), [tham số](VIETNAM_POLITICAL_PARAMETERS_VI.json), [balance](VIETNAM_POLITICAL_BALANCE_VI.py), [crosscheck](VIETNAM_POLITICAL_CROSSCHECK_VI.py), [ngân sách](VIETNAM_POLITICAL_BALANCE_VI.csv), [ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv), [node](VIETNAM_POLITICAL_NODE_CHOICES_VI.csv) đi cùng trong gói ZIP. Không cần REVIEW_L1/L2.

Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3`; thêm `--sync-approved` để đồng bộ bảng thiết kế, `--audit-json` khi cần toàn bộ probe/chẩn đoán. Dùng `python tools/package_political_design.py` trong repo để đóng gói đủ nguồn. Exit2 là FAIL kiểm mô hình.
