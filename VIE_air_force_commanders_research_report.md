# Báo cáo nghiên cứu chỉ huy Không quân VIE (Quân chủng Phòng không - Không quân)

**Ngày:** 01/10/2026
**Phạm vi:** chỉ huy cấp quân chủng của Quân chủng Phòng không - Không quân (PK-KQ), 2000 đến nay. Chưa gồm cấp sư đoàn (xem mục 7).
**Trạng thái:** đã chốt hướng chuỗi 8 mốc cho slot `air_chief` và mở rộng 12 chỉ huy bổ sung (mục 8). Plan code: [VIE_air_force_implementation_plan.md](VIE_air_force_implementation_plan.md).

## 1. Kết luận ngắn

1. **Roster Không quân hiện có của MD sai về nhân thân.** Trong 4 character VIE mà MD gán cho Không quân, **không ai là chỉ huy Không quân**:
   - `VIE_Tran_Quang_Phuong` (slot `air_chief`): thực tế là tướng chính trị, Chính ủy Quân khu 5, Phó Chủ tịch Quốc hội.
   - `VIE_Tran_Viet_Khoa` (slot `air_chief`): thực tế là tướng Lục quân, Giám đốc Học viện Quốc phòng; hồ sơ không có dòng nào ở Phòng không-Không quân.
   - `VIE_Vo_Minh_Luong` (slot `high_command`, ledger air): thực tế là Tư lệnh Quân khu 7.
   - `VIE_Vo_Trong_Viet` (slot `high_command`, ledger air): thực tế là Tư lệnh Bộ đội Biên phòng.
2. **Chuỗi tư lệnh PK-KQ có nguồn rõ**, 8 người từ 1999: Soát, Thân, Đức, Hòa, Vịnh, Kha (quyền), Hiền, Sơn. Chuỗi này đủ để dựng slot `air_chief` đúng lịch sử, không cần dùng người của Lục quân.
3. **Không quân khác Lục quân về cơ chế:** HOI4/MD không có commander cho Không quân; chỉ có advisor. Vì vậy "chỉ huy Không quân" trong mod chính là các advisor ở slot `air_chief` và `high_command` ledger air. Số lượng bị giới hạn bởi slot, không phải bởi công thức số tướng.
4. **Ước tính cần tạo mới khoảng 10 character** (mục 5). Phần lớn dữ liệu có nguồn đáng tin; điểm yếu nằm ở vài ngày chính xác và cấp sư đoàn.

## 2. Không quân được mô hình hóa thế nào trong MD

| Điểm | Thực tế (nguồn: `VIE.txt` của MD, `01_air_chief_traits.txt`, `01_high_command_traits.txt`) |
|---|---|
| Vai trò có thể có | Chỉ `advisor`. Không có khối `field_marshal`/`corps_commander` cho Không quân |
| Slot | `air_chief` (1 người) và `high_command` với `ledger = air` |
| Pool trait `air_chief` | `air_chief_reform_*`, `_safety_*`, `_night_operations_*`, `_ground_support_*`, `_all_weather_*`; `air_air_superiority_*`, `air_bomber_interception_*`, `air_close_air_support_*`, `air_pilot_training_*`, `air_force_multiplier_*`, `air_strategic/tactical_bombing_*`, `air_naval_strike_*`, `air_airborne_*`, `air_air_combat_training_*` (mỗi loại cấp 1-3) |
| Pool trait `high_command` air | `air_high_command_interception_*`, `_air_superiority_*`, `_multirole_support_*`, `_ground_support_*`, `_all_weather_*`, `_night_operations_*`, `_flight_safety_*`, `_heavy_aircraft_*`, `_aircraft_design_*`, `_combat_training_*`, `_air_reform_*` (cấp 1-3) |
| Validator MD | Trait `air_chief_*` chỉ hợp lệ ở slot `air_chief`; trait `air_high_command_*` chỉ hợp lệ ở `high_command`; trait lẫn pool bị báo lỗi |

**Hệ quả cho thiết kế:** không có chuyện "giới hạn 6 commander" như Lục quân. Câu hỏi thật là bao nhiêu người cần có mặt cùng lúc trong pool để người chơi chọn, và ai nên chiếm slot `air_chief` duy nhất ở mỗi thời điểm.

## 3. Rà soát 4 character Không quân upstream

| ID | Slot, trait, cost trong MD | Thực tế (nguồn) | Đánh giá |
|---|---|---|---|
| `VIE_Tran_Quang_Phuong` | `air_chief`, `air_chief_reform_2`, 150 | Sinh 1961. Chính ủy Quân khu 5 từ 06/2011 đến 2019; Phó Chủ nhiệm Tổng cục Chính trị; Phó Chủ tịch Quốc hội khóa XV. **Không có chức vụ ở PK-KQ** | Sai nhân thân |
| `VIE_Tran_Viet_Khoa` | `air_chief`, `air_bomber_interception_2`, 100 | Sinh 1965. Sư đoàn 301, Phó Tư lệnh Thủ đô; Phó Tư lệnh Quân khu 1 từ 2011; Giám đốc Học viện Quốc phòng từ 2016; Thượng tướng 09/2021. **Không có chức vụ ở PK-KQ** | Sai nhân thân |
| `VIE_Vo_Minh_Luong` | `high_command` ledger air, `air_high_command_interception_3`, 125 | Tư lệnh Quân khu 7 10/2015 - 11/2020 (Lục quân) | Sai quân chủng |
| `VIE_Vo_Trong_Viet` | `high_command` ledger air, `air_high_command_multirole_support_1`, 100 | Tư lệnh Bộ đội Biên phòng 2012-2015, Thứ trưởng 2015-2016 | Sai quân chủng |

**Ghi chú:** tôi không rõ vì sao MD xếp họ vào Không quân (có thể là cách MD "lấp slot" cho các lãnh đạo quốc phòng đương thời). Không có nguồn nào cho thấy họ từng gắn với Không quân.

**Hệ quả với code hiện tại của submod:** sau khi khối retire ở startup bị xóa (nhánh N của plan Lục quân), Phương và Khoa đang có mặt từ 2000 và là hai lựa chọn duy nhất cho slot `air_chief`. Hai người này sẽ chiếm slot `air_chief` bằng chức vụ không có thật. Xem mục 6.

**Phát hiện phụ cho Lục quân:** Trần Việt Khoa có hồ sơ Lục quân đáng kể (Phó Tư lệnh Quân khu 1 từ 2011; Giám đốc Học viện Quốc phòng từ 2016; Thượng tướng 2021). Một nguồn ghi ông là Tư lệnh Quân khu 1 2013-2015, nhưng danh sách tư lệnh Quân khu 1 trên Wikipedia VI ghi Bế Xuân Trường (2010-2014) và Phan Văn Giang (2014-2016). Hai nguồn mâu thuẫn, chưa xác minh.

## 4. Chuỗi chỉ huy PK-KQ đã xác minh

### 4.1. Tư lệnh Quân chủng (slot `air_chief`)

| # | Nhân vật | Chức vụ và thời gian | Thông tin bổ sung | Tin cậy |
|--:|---|---|---|:-:|
| 0 | Nguyễn Văn Cốc | Tư lệnh Quân chủng Không quân 1996-1997 | Trung tướng 1999; sau đó Thanh tra Bộ Quốc phòng 1998-2002. Trước khi hợp nhất, ngoài bookmark | B |
| 1 | **Nguyễn Đức Soát** | Tư lệnh Không quân 1997-1999; Tư lệnh PK-KQ 1999-2002; Phó Tổng Tham mưu trưởng 2002-2008 | Trung tướng 1999; phi công tiêm kích huyền thoại | A |
| 2 | **Nguyễn Văn Thân** | Tư lệnh PK-KQ 07/02/2002 - 02/2007 | Sinh 1945; Trung tướng 2003; nghỉ hưu 02/2007 | A |
| 3 | **Lê Hữu Đức** | Tư lệnh PK-KQ 02/2007 - 2010; Thứ trưởng Bộ Quốc phòng 2010-2016 | Sinh 1955; Sư đoàn trưởng PK 363 (1999); Phó Tư lệnh 2003; Thượng tướng 2015. Hai nguồn lệch năm bắt đầu (2006 và 2007); dùng 02/2007 vì khớp ngày Thân nghỉ | A/B |
| 4 | **Phương Minh Hòa** | Chính ủy PK-KQ 10/2005 - 2010; Tư lệnh PK-KQ 2010 - 21/05/2015; Phó Chủ nhiệm Tổng cục Chính trị 2015-2016 | Sinh 1955; Thượng tướng 07/2015; bị Ban Bí thư cảnh cáo 07/2018. Trình tự Chính ủy rồi Tư lệnh khác thường, nhưng nhất quán giữa Wikipedia và báo | B |
| 5 | **Lê Huy Vịnh** | Phó Tư lệnh 2011-2015; Tư lệnh PK-KQ 21/05/2015 - 31/12/2019; Phó Tổng Tham mưu trưởng, Thứ trưởng 12/2019 - 10/2020 | Sinh 1961; con trai Thiếu tướng Lê Huy Vinh (Phó Tư lệnh Phòng không); Thượng tướng 2020; từng là Ủy viên Bộ Chính trị | A |
| 6 | **Vũ Văn Kha** | Phó Tư lệnh kiêm Tham mưu trưởng 08/2017 - 2019; quyền Tư lệnh từ 31/12/2019 đến 05/2023 | Sinh 1963; phi công Su-22; Sư đoàn trưởng Không quân 370; Trung tướng 08/2021; nghỉ hưu sau đó | A |
| 7 | **Nguyễn Văn Hiền** | Sư đoàn trưởng PK 365 (2016); Phó Tư lệnh 2018; Tham mưu trưởng 06/2020; Tư lệnh 19/05/2023 - 28/06/2025; Thứ trưởng Bộ Quốc phòng từ 27-28/06/2025 | Sinh 22/02/1967; Trung tướng 05/2023; Thượng tướng 14/07/2025 | A |
| 8 | **Vũ Hồng Sơn** | Phó Tư lệnh kiêm Tham mưu trưởng 05/2023 - 06/2025; Tư lệnh PK-KQ từ 28/06/2025 | Rank báo chí ghi không thống nhất (Thiếu tướng/Trung tướng 2025); Ủy viên Trung ương Đảng khóa XIV | A/B |

### 4.2. Tham mưu trưởng và phó tổng tham mưu trưởng (ứng viên `high_command` ledger air)

| Nhân vật | Chức vụ và thời gian | Ghi chú | Tin cậy |
|---|---|---|:-:|
| **Võ Văn Tuấn** | Phó Tư lệnh kiêm Tham mưu trưởng PK-KQ 2008-2011; **Phó Tổng Tham mưu trưởng 2011-2017** | Sinh 1955; phi công Su-27; Thượng tướng 2015; con trai nhà ngoại giao Võ Văn Sung. Loại khỏi roster Lục quân vì gốc Không quân | A |
| Nguyễn Văn Thọ | Tham mưu trưởng PK-KQ 2011-2017 (Thiếu tướng) | Từng là Sư đoàn trưởng Không quân 372. Chỉ có nguồn Wikipedia VI | B |
| Bùi Đức Hiền | Tham mưu trưởng PK-KQ từ 06/2025 (Thiếu tướng) | Đương nhiệm, ít thông tin | B |

### 4.3. Chính ủy (ứng viên chính trị, thấp ưu tiên)

| Nhân vật | Thời gian | Tin cậy |
|---|---|:-:|
| Nguyễn Văn Phiệt | 1999-2001 (Trung tướng) | B |
| Hán Vĩnh Tưởng | 2001 - 12/2004 (Trung tướng) | B |
| Nguyễn Mạnh Hải | 12/2004 - 10/2005 (Thiếu tướng) | B |
| Phương Minh Hòa | 10/2005 - 2010 (sau đó Tư lệnh) | B |
| Nguyễn Văn Thanh | 2011 - 2016 (Thiếu tướng/Trung tướng); bị kỷ luật cùng Phương Minh Hòa 2018 | B |
| Lâm Quang Đại | 2016 - 2022 | B |
| Trần Ngọc Quyến | 2022 - nay (Trung tướng) | B |

Các trait `air_high_command_*` của MD thiên về chuyên môn (đánh chặn, ưu thế trên không...), không có trait chính trị. Vì vậy chính ủy ít có chỗ trong roster, trừ Phương Minh Hòa vì ông giữ cả hai chức.

## 5. Ứng viên đề xuất cho roster (chưa phải quyết định)

Dùng cùng khung hai giai đoạn của Lục quân: **2000-2014** và **2015-nay**. Mỗi người xuất hiện đúng một lần.

### 5.1. Giai đoạn 1 (bookmark 2000 đến hết 2014)

| Nhân vật | Slot đề xuất | Cơ sở | Lệch so với 2000 |
|---|---|---|---|
| Nguyễn Đức Soát | `air_chief` | Tư lệnh Không quân rồi PK-KQ; đang tại chức năm 2000 | 0 |
| Nguyễn Văn Thân | `air_chief` | Tư lệnh 2002-2007 | 2 năm |
| Lê Hữu Đức | `air_chief` | Tư lệnh 2007-2010; Sư đoàn trưởng PK 363 từ 1999 | 7 năm |
| Phương Minh Hòa | `air_chief` | Tư lệnh 2010-2015; Chính ủy 2005-2010 | 10 năm |
| Võ Văn Tuấn | `high_command` ledger air | Tham mưu trưởng PK-KQ 2008-2011, Phó Tổng Tham mưu trưởng 2011-2017 | 8 năm |

Bốn người đầu cùng chiếm slot `air_chief`, nên người chơi chỉ chọn được một người ở mỗi thời điểm, như chuỗi Tổng Tham mưu trưởng của Lục quân.

### 5.2. Giai đoạn 2 (từ 01/01/2015)

| Nhân vật | Slot đề xuất | Cơ sở | Lệch so với 2015 |
|---|---|---|---|
| Lê Huy Vịnh | `air_chief` | Tư lệnh 05/2015 - 12/2019 | 0 |
| Vũ Văn Kha | `air_chief` | Quyền Tư lệnh 12/2019 - 05/2023 | 5 năm |
| Nguyễn Văn Hiền | `air_chief` | Tư lệnh 05/2023 - 06/2025 | 8 năm |
| Vũ Hồng Sơn | `air_chief` | Tư lệnh từ 06/2025 | 10 năm |
| Nguyễn Văn Thọ | `high_command` ledger air | Tham mưu trưởng PK-KQ 2011-2017 | 0 |

Hai người cuối chuỗi (Hiền, Sơn) lệch lớn (8-10 năm). Phương án thay thế: chuyển họ sang mốc phụ 2026 như nhóm Quân đoàn 12/34 để giảm lệch, hoặc dùng `visible` có điều kiện ngày nếu thí nghiệm E2 cho thấy dùng được.

### 5.3. Số lượng

| | Giai đoạn 1 | Giai đoạn 2 |
|---|---:|---:|
| `air_chief` | 4 (một slot) | 4 (một slot) |
| `high_command` ledger air | 1 (+ Lương, Việt nếu giữ upstream) | 1 |

**Tổng cần tạo mới: 10 character** (4 + 1 + 4 + 1). Bùi Đức Hiền, các chính ủy và Nguyễn Văn Cốc là dự phòng.

## 6. Quyết định (đã chốt, xem plan)

Q1 (retire Phương và Khoa) và Q2 (giữ Lương và Việt) đã chốt như khuyến nghị. Q5 (Hiền, Sơn) chốt theo chuỗi 8 mốc: Hiền 19/05/2023, Sơn 28/06/2025. Q3 chốt theo hướng retire khi bàn giao, không tự chuyển sang vai trò khác. Q4 vẫn chờ nguồn.

| # | Câu hỏi | Tùy chọn | Khuyến nghị |
|---|---|---|---|
| Q1 | Xử lý `VIE_Tran_Quang_Phuong` và `VIE_Tran_Viet_Khoa` (sai nhân thân) | (a) retire ở startup, một chiều, đã có tiền lệ; (b) giữ nguyên | **(a)**, vì họ chiếm slot `air_chief` bằng chức vụ không có thật. Retire một chiều không cần tuyển lại |
| Q2 | Xử lý `VIE_Vo_Minh_Luong` và `VIE_Vo_Trong_Viet` (ledger air nhưng là Lục quân) | (a) giữ nguyên; (b) retire | **(a)**, vì họ thuộc nhóm tướng Lục quân đã dùng trong roster Lục quân; chỉ ghi chú lệch |
| Q3 | Lê Hữu Đức, Phương Minh Hòa, Lê Huy Vịnh sau khi hết chức vụ Không quân vẫn là Thứ trưởng/Phó Chủ nhiệm TCCT | Giữ trong slot Không quân hay chuyển | Giữ trong Giai đoạn 1 hoặc 2 theo chức vụ Không quân; không nhân đôi sang Lục quân |
| Q4 | Có đưa Trần Việt Khoa vào roster Lục quân không | Có / Không | Chờ xác minh mâu thuẫn Quân khu 1 (mục 3), nếu đúng thì đáng thêm |
| Q5 | Hiền và Sơn: giai đoạn 2 hay mốc phụ 2026 | Hai lựa chọn ở 5.2 | Mốc phụ 2026 nếu muốn tránh lệch 8-10 năm |

## 7. Khoảng trống và rủi ro nghiên cứu

- **Chưa nghiên cứu cấp sư đoàn.** Báo cáo Lục quân đã gợi ý nhưng chưa có số liệu cho các sư đoàn Phòng không 361, 363, 365, 367 và Không quân 370, 371, 372. Không cần cho slot `air_chief`, nhưng cần nếu muốn nhiều advisor `high_command` ledger air hơn.
- **Một nguồn:** Tham mưu trưởng PK-KQ giai đoạn 2008-2025 và danh sách Chính ủy chỉ có Wikipedia VI. Nguyễn Văn Thọ, Bùi Đức Hiền, các chính ủy đều ở mức B.
- **Mâu thuẫn nhỏ:** năm Lê Hữu Đức nhận chức Tư lệnh (2006 so với 2007); cấp bậc Vũ Hồng Sơn năm 2025; thời gian Trần Việt Khoa ở Quân khu 1.
- **Nguyên tắc ngày tháng:** tôi dùng ngày chính xác khi có, nếu không thì dùng năm. Mọi ngày lấy từ nguồn thứ cấp (Wikipedia VI, báo chí chính thống), chưa phải quyết định bổ nhiệm gốc.
- **Không có nguồn nào gắn Không quân với công thức số tướng** của MD; con số 10 ở mục 5.3 là đề xuất thiết kế, không phải công thức.

## 8. Mở rộng: 12 chỉ huy bổ sung (nghiên cứu 01/10/2026)

Yêu cầu: thêm khoảng 12 chỉ huy ngoài chuỗi tư lệnh 8 người, cho slot `high_command` ledger air. Cấp sư đoàn không dùng được: trang Wikipedia VI của các sư đoàn Phòng không 361, 363 và Không quân 370, 371, 372 chỉ ghi sư đoàn trưởng hiện tại (cấp Đại tá) và không có danh sách lịch sử có năm. Vì vậy 12 người đều lấy từ cấp Phó Tư lệnh, Tham mưu trưởng, Chính ủy và các tướng gốc Không quân giữ chức cao hơn.

### 8.1. Mười hai người được chọn

| # | Nhân vật | Chức vụ và thời gian | Tin cậy |
|--:|---|---|:-:|
| 1 | Phạm Thanh Ngân | Sinh 1939; phi công MiG-21, 8 máy bay Mỹ bị bắn rơi, Anh hùng LLVTND 1969; Tư lệnh Quân chủng Không quân 04/1989 - 1996; Chủ nhiệm Tổng cục Chính trị 01/1998 - 05/2001; Thượng tướng 11/1999; nghỉ hưu 2002 | A |
| 2 | Hán Vĩnh Tưởng | Sinh 1945; phi công, bắn rơi 3 máy bay Mỹ; Phó Tư lệnh chính trị Không quân từ 11/1996; Phó Tư lệnh chính trị kiêm Bí thư Đảng ủy PK-KQ 02/2001 - 01/2005; Trung tướng 2002 | A |
| 3 | Phạm Tuân | Sinh 1947; phi công vũ trụ đầu tiên của Việt Nam (1980); Phó Tư lệnh chính trị Không quân 1989; Giám đốc Tổng cục Công nghiệp Quốc phòng 1999; Trung tướng; nghỉ hưu 2008. Chỉ có báo chí, chưa có nguồn thứ hai về năm chính xác | B |
| 4 | Nguyễn Văn Phiệt | Sinh 1938; Chính ủy Quân chủng Phòng không 1992 - 1999, Chính ủy PK-KQ 1999 - 2001; Trung tướng 1999 | B |
| 5 | Võ Văn Tuấn | Phi công Su-27; Phó Tư lệnh kiêm Tham mưu trưởng PK-KQ 2008 - 2011; Phó Tổng Tham mưu trưởng 2011 - 2017; Thượng tướng 2015 | A |
| 6 | Nguyễn Văn Thọ | Sư đoàn trưởng Không quân 372; Tham mưu trưởng PK-KQ 2011 - 2017 (Thiếu tướng) | B |
| 7 | Nguyễn Văn Thanh | Sinh 1956; Chính ủy PK-KQ 2011 - 2016; Thiếu tướng 2009, Trung tướng 2012; bị kỷ luật cảnh cáo 07/2018 cùng Phương Minh Hòa | A |
| 8 | Lâm Quang Đại | Sinh 1962; Phó Chính ủy từ 06/2015; Chính ủy PK-KQ 2016 - 2022; Thiếu tướng 2015, Trung tướng 2019 | A |
| 9 | Phạm Văn Tính | Sư đoàn trưởng PK 363 2016 - 01/2019; Phó Tư lệnh PK-KQ từ 06/2020; Thiếu tướng 2020 | B |
| 10 | Trần Ngọc Quyến | Sinh 1969; Chính ủy PK-KQ từ 16/06/2022; Trung tướng | A |
| 11 | Phạm Tuấn Anh | Phó Tham mưu trưởng, rồi Phó Tư lệnh PK-KQ từ 07/2023 | B |
| 12 | Bùi Đức Hiền | Tham mưu trưởng PK-KQ từ 06/2025 (Thiếu tướng) | B |

### 8.2. Dự phòng, không chọn

| Nhân vật | Lý do |
|---|---|
| Nguyễn Văn Cốc | Tư lệnh Không quân 1996 - 1997, sau đó Thanh tra Bộ Quốc phòng 1998 - 2002; chỉ có một nguồn |
| Nguyễn Mạnh Hải | Chính ủy 12/2004 - 10/2005 (Thiếu tướng); nhiệm kỳ quá ngắn, ít thông tin |
| Bùi Thiên Thau, Vũ Đại Dương | Đại tá khi được bổ nhiệm Phó Tư lệnh (2023, 2025); cấp bậc và năm thăng tướng chưa xác minh |

### 8.3. Phát hiện cần ghi nhận

- **Nguyễn Văn Rinh không thuộc Không quân.** Một kết quả tìm kiếm gợi ý ông là tướng Không quân, nhưng hồ sơ ghi Tư lệnh Quân đoàn 2 (1992), Phó Tổng Tham mưu trưởng 1994 - 1998, Thứ trưởng Bộ Quốc phòng 1998 - 2007, Thượng tướng 2004. Đây là tướng Lục quân và là ứng viên `high_command` còn thiếu của roster Lục quân Giai đoạn 1; chưa đưa vào đó.
- **Phạm Thanh Ngân đang tại chức cao nhất năm 2000** (Chủ nhiệm Tổng cục Chính trị 01/1998 - 05/2001), là tướng gốc Không quân có vị trí cao nhất trong quân đội ở bookmark 2000. Báo cáo Lục quân đã ghi Lê Văn Dũng là Chủ nhiệm Tổng cục Chính trị từ 2001, khớp với việc Ngân thôi chức 05/2001.
- **Sáu trong 12 người là cán bộ chính trị** (Tưởng, Phiệt, Thanh, Đại, Quyến, và Ngân từ 1998). Pool trait `high_command` của MD không có trait chính trị, nên họ mang trait chuyên môn gần nhất.
- **Phạm Tuân** gắn với Công nghiệp Quốc phòng (Giám đốc Tổng cục 1999): có thể hợp với trục CNQP của mod nếu về sau muốn.
- **Xung đột nguồn nhỏ:** Hán Vĩnh Tưởng giữ chức Chính ủy 1996 - 1999 theo một nguồn nhưng nguồn khác ghi Phó Tư lệnh chính trị; Lâm Quang Đại có rank khác nhau giữa hai nguồn trước 2019. Không ảnh hưởng đến roster.

## 9. Nguồn

- [Tư lệnh Quân chủng Phòng không - Không quân Việt Nam (VI Wikipedia)](https://vi.wikipedia.org/wiki/T%C6%B0_l%E1%BB%87nh_Qu%C3%A2n_ch%E1%BB%A7ng_Ph%C3%B2ng_kh%C3%B4ng_-_Kh%C3%B4ng_qu%C3%A2n_Vi%E1%BB%87t_Nam)
- [Tham mưu trưởng Quân chủng Phòng không - Không quân (VI Wikipedia)](https://vi.wikipedia.org/wiki/Tham_m%C6%B0u_tr%C6%B0%E1%BB%9Fng_Qu%C3%A2n_ch%E1%BB%A7ng_Ph%C3%B2ng_kh%C3%B4ng_%E2%80%93_Kh%C3%B4ng_qu%C3%A2n_Vi%E1%BB%87t_Nam)
- [Quân chủng Phòng không - Không quân (VI Wikipedia)](https://vi.wikipedia.org/wiki/Qu%C3%A2n_ch%E1%BB%A7ng_Ph%C3%B2ng_kh%C3%B4ng_%E2%80%93_Kh%C3%B4ng_qu%C3%A2n,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam)
- [Lê Huy Vịnh (VI Wikipedia)](https://vi.wikipedia.org/wiki/L%C3%AA_Huy_V%E1%BB%8Bnh)
- [Phương Minh Hòa (VI Wikipedia)](https://vi.wikipedia.org/wiki/Ph%C6%B0%C6%A1ng_Minh_H%C3%B2a) và [báo VnExpress về kỷ luật 2018](https://vnexpress.net/nguyen-tu-lenh-quan-chung-phong-khong-khong-quan-bi-canh-cao-3784366.html)
- [Lê Hữu Đức (VI Wikipedia)](https://vi.wikipedia.org/wiki/L%C3%AA_H%E1%BB%AFu_%C4%90%E1%BB%A9c_(th%C6%B0%E1%BB%A3ng_t%C6%B0%E1%BB%9Bng))
- [Nguyễn Văn Thân (trung tướng, VI Wikipedia)](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_V%C4%83n_Th%C3%A2n_(trung_t%C6%B0%E1%BB%9Bng))
- [Nguyễn Văn Hiền (thượng tướng, VI Wikipedia)](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_V%C4%83n_Hi%E1%BB%81n_(th%C6%B0%E1%BB%A3ng_t%C6%B0%E1%BB%9Bng))
- [Tân Tư lệnh PK-KQ được thăng Trung tướng (Chính phủ, 06/2023)](https://xaydungchinhsach.chinhphu.vn/tan-tu-lenh-quan-chung-phong-khong-khong-quan-duoc-chu-tich-nuoc-thang-ham-trung-tuong-119230601133532399.htm)
- [Thiếu tướng Vũ Hồng Sơn nhận nhiệm vụ Tư lệnh PK-KQ (Tuổi Trẻ, 07/2025)](https://tuoitre.vn/thieu-tuong-vu-hong-son-nhan-nhiem-vu-tu-lenh-quan-chung-phong-khong-khong-quan-20250704192745086.htm)
- [Bàn giao Tư lệnh PK-KQ (Bộ Quốc phòng)](http://mod.gov.vn/bo-truong/chi-tiet?current=true&urile=wcm:path:/mod/sa-mod-site/minister-site/hoat-dong/dai-tuong-phan-van-giang-chu-tri-hoi-nghi-ban-giao-chuc-vu-tu-lenh-quan-chung-phong-khong-khong-quan)
- [Vũ Văn Kha được giao quyền Tư lệnh (VOV)](https://vov.gov.vn/thieu-tuong-vu-van-kha-duoc-giao-quyen-tu-lenh-quan-chung-pk-kq-dtnew-167847)
- [Võ Văn Tuấn (VI Wikipedia)](https://vi.wikipedia.org/wiki/V%C3%B5_V%C4%83n_Tu%E1%BA%A5n)
- [Trần Quang Phương (VI Wikipedia)](https://vi.wikipedia.org/wiki/Tr%E1%BA%A7n_Quang_Ph%C6%B0%C6%A1ng) và [Trần Việt Khoa (VI Wikipedia)](https://vi.wikipedia.org/wiki/Tr%E1%BA%A7n_Vi%E1%BB%87t_Khoa)
- Mục 8 (mở rộng): [Phạm Thanh Ngân](https://vi.wikipedia.org/wiki/Ph%E1%BA%A1m_Thanh_Ng%C3%A2n), [Nguyễn Văn Rinh](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_V%C4%83n_Rinh), [Lâm Quang Đại](https://vi.wikipedia.org/wiki/L%C3%A2m_Quang_%C4%90%E1%BA%A1i), [Hán Vĩnh Tưởng](https://vi.wikipedia.org/wiki/H%C3%A1n_V%C4%A9nh_T%C6%B0%E1%BB%9Fng), [Nguyễn Văn Thanh (trung tướng)](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_V%C4%83n_Thanh_(trung_t%C6%B0%E1%BB%9Bng)), [Trần Ngọc Quyến](https://vi.wikipedia.org/wiki/Tr%E1%BA%A7n_Ng%E1%BB%8Dc_Quy%E1%BA%BFn), [Phạm Tuân (Báo Bắc Ninh)](https://baobacninhtv.vn/trung-tuong-anh-hung-phi-cong-pham-tuan-que-huong-dat-nuoc-chap-canh-toi-bay-postid363871.bbg), [bổ nhiệm Phó Tư lệnh PK-KQ (Hà Nội Mới)](https://hanoimoi.vn/bo-nhiem-pho-tu-lenh-quan-chung-phong-khong-khong-quan-636038.html), [Vũ Đại Dương (Báo Chính phủ)](https://baochinhphu.vn/dai-ta-vu-dai-duong-giu-chuc-pho-tu-lenh-quan-chung-phong-khong-khong-quan-10225072310001599.htm)
- [MD VIE.txt (upstream)](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt), [01_air_chief_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_air_chief_traits.txt), [01_high_command_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_high_command_traits.txt)
- Trong repo: [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md), [VIE_md_character_schema_and_roster.md](VIE_md_character_schema_and_roster.md)
