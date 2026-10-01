# Báo cáo nghiên cứu mốc xuất hiện commander VIE

> **Đã lỗi thời một phần.** Mốc 2005 trong báo cáo này đã bị thay bằng hai giai đoạn (2000-2014 và 2015-nay) trong `VIE_land_forces_roster_rebuild.md` và `VIE_land_forces_implementation_plan_v2.md`. Đoạn nói Nguyễn Chí Vịnh có "căn cứ đủ mạnh" ở 2000 cũng không còn đúng: năm 1998 ông mới là Phó Tổng cục trưởng Tổng cục II, Tổng cục trưởng từ 2002. Giữ file này để tham khảo bảng bằng chứng ở mục 3.

**Ngày:** 01/10/2026  
**Phạm vi:** Millennium Dawn VIE, bookmark 2000 và các mốc 2005, 2010, 2015, 2021, 2023-2025.  
**Mục đích:** xác định character nào có thể xuất hiện đầu game và character nào phải tuyển theo mốc lịch sử.

## 1. Kết luận điều hành

Không nên dùng thẳng phân bổ `12 người năm 2000 / 6 người năm 2005 / 7 người năm 2010` như một kết luận lịch sử. Có ba vấn đề:

1. Millennium Dawn upstream hiện tuyển **19 character VIE** trong history 2000.
2. Submod có thêm **7 character `VIE_army_*`**, tổng cộng **26 ID**.
3. Phân bổ 12 + 6 + 7 chỉ có 25 người và không khớp tổng roster 26; hơn nữa 7 commander mở rộng của submod gắn với Quân đoàn 12/34, chỉ xuất hiện từ 2023-2025, không thể hợp lý hóa thành roster năm 2010.

Kết luận bảo thủ:

- **Có thể giữ đầu game 2000:** chỉ những người có vai trò cấp cao đã tồn tại trước hoặc quanh năm 2000, hoặc được xác nhận là sĩ quan cao cấp nhưng chưa có ngày bổ nhiệm chính xác.
- **Mốc 2005/2010:** chỉ dùng cho người có bằng chứng họ đã giữ chức vụ chỉ huy trước hoặc trong giai đoạn đó. Không dùng năm giữ chức hiện đại để suy ngược.
- **Mốc 2015/2016/2021:** phù hợp hơn cho nhiều advisor/high command upstream hiện đang bị history MD tuyển từ 2000.
- **Mốc 2023-2025:** bắt buộc cho 7 commander submod vì họ gắn với Quân đoàn 12, Quân đoàn 34 và Quân khu 7 hiện đại.

## 2. Nguồn và giới hạn dữ liệu

### Nguồn trong repository

- `tools/audit/md_ref/VIE_country.txt`: history MD tuyển 19 character ngay trong block `2000.1.1`.
- `VIE_generals_and_commander_system_research_report.md`: chuỗi Tổng Tham mưu trưởng, Bộ trưởng Quốc phòng, roster upstream và các mốc Quân đoàn 12/34.
- `VIE_md_character_schema_and_roster.md`: schema character MD, danh sách vai trò upstream và xác nhận history upstream tuyển 19 ID.

### Nguồn công khai đã đối chiếu

- [Chief of the General Staff of Vietnam](https://en.wikipedia.org/wiki/Chief_of_the_General_Staff_(Vietnam)): Lê Văn Dũng 1998-2001, Phùng Quang Thanh 2001-2006, Nguyễn Khắc Nghiên 2006-2010, Đỗ Bá Tỵ 2010-2016, Phan Văn Giang 2016-2021, Nguyễn Tân Cương từ 2021.
- [Minister of Defence of Vietnam](https://en.wikipedia.org/wiki/Minister_of_Defence_(Vietnam)): xác nhận Phan Văn Giang là Bộ trưởng từ 2021 và chuỗi Bộ trưởng được dùng để đối chiếu vai trò chính trị-quân sự.
- [QĐND: Bàn giao chức vụ Tư lệnh Quân đoàn 12](https://www.qdnd.vn/quoc-phong-an-ninh/tin-tuc/ban-giao-chuc-vu-tu-lenh-quan-doan-12-827158): Lê Xuân Thuân nhận chức Tư lệnh Quân đoàn 12 năm 2025.
- [Chính phủ: bổ nhiệm Lê Xuân Thế làm Tư lệnh Quân khu 7](https://xaydungchinhsach.chinhphu.vn/thu-tuong-bo-nhiem-tan-thu-truong-bo-quoc-phong-tu-lenh-quan-khu-7-11925070922253096.htm): Lê Xuân Thế nhận chức Tư lệnh Quân khu 7 năm 2025.
- [VietNamNet: Nguyễn Bá Lực](https://vietnamnet.vn/tu-lenh-quan-doan-34-giu-chuc-pho-tong-tham-muu-truong-qdnd-viet-nam-2394744.html): Nguyễn Bá Lực là Tư lệnh Quân đoàn 34 trước khi chuyển làm Phó Tổng Tham mưu trưởng năm 2025.
- [TTXVN: hồ sơ Đào Tuấn Anh](https://nvsk.vnanet.vn/ho-so/dao-tuan-anh-3-181955.vna): Đào Tuấn Anh là Tư lệnh Quân đoàn 34 trong giai đoạn hiện đại.
- [QĐND: Trần Công Đức](https://www.qdnd.vn/quoc-phong-an-ninh/tin-tuc/quan-doan-34-hoan-thanh-toan-dien-nhiem-vu-quy-i-nam-2026-1034371): Trần Công Đức là Phó tư lệnh kiêm Tham mưu trưởng Quân đoàn 34 năm 2026.

Các nguồn trên xác nhận chắc các mốc hiện đại. Với nhiều tên upstream khác, repo chỉ có role gameplay mà không có hồ sơ ngày bổ nhiệm; các kết luận bên dưới vì vậy được đánh dấu mức tin cậy.

## 3. Timeline đã xác minh

| Nhân vật / ID | Bằng chứng lịch sử | Mốc gameplay đề xuất | Độ tin cậy |
|---|---|---:|---|
| Nguyễn Chí Vịnh / `VIE_Nguyen_Chi_Vinh` | Tướng cấp cao, gắn với Tổng cục Tình báo Quốc phòng trong giai đoạn trước 2010; có thể đại diện lớp chỉ huy chiến lược đầu thế kỷ | 2000 | Trung bình-khá |
| Phùng Quang Thanh | Tổng Tham mưu trưởng 05/2001-08/2006; không phải ID commander mở rộng của submod nhưng là chuẩn đối chiếu lịch sử | 2001 | Cao |
| Nguyễn Khắc Nghiên | Tổng Tham mưu trưởng 08/2006-11/2010; không phải ID recruit hiện tại | 2006 | Cao |
| Đỗ Bá Tỵ | Tổng Tham mưu trưởng 11/2010-05/2016; portrait đã có trong repo, nhưng chưa được thêm thành character mới trong submod | 2010 | Cao |
| Phan Văn Giang / `VIE_Phan_Van_Giang` | Tổng Tham mưu trưởng 05/2016-06/2021, Bộ trưởng từ 2021 | 2016 | Cao |
| Nguyễn Tân Cương / `VIE_Nguyen_Tan_Cuong` | Tổng Tham mưu trưởng từ 2021 | 2021 | Cao |
| Bế Xuân Trường / `VIE_Be_Xuan_Truong` | Thuộc lớp lãnh đạo quốc phòng hiện đại; report đặt trong nhóm chính trị-quân đội, không có bằng chứng đủ để đưa về 2000 | 2015-2016 | Trung bình |
| Lê Xuân Thuân / `VIE_army_le_xuan_thuan` | Tư lệnh Quân đoàn 12 từ 24/04/2025 | 2023-2025; không trước 2023 | Cao |
| Trần Đại Thắng / `VIE_army_tran_dai_thang` | Chính ủy Quân đoàn 12 trong giai đoạn Quân đoàn 12 hiện đại | 2023-2025; không trước 2023 | Cao |
| Nguyễn Thành Phố / `VIE_army_nguyen_thanh_pho` | Phó tư lệnh kiêm Tham mưu trưởng Quân đoàn 12 trong nguồn QĐND năm 2026 | 2023-2025; không trước 2023 | Cao |
| Đào Tuấn Anh / `VIE_army_dao_tuan_anh` | Tư lệnh Quân đoàn 34 trong giai đoạn hiện đại | 2024-2025; không trước 2023 | Cao |
| Nguyễn Bá Lực / `VIE_army_nguyen_ba_luc` | Tư lệnh Quân đoàn 34 tại giai đoạn thành lập, chuyển công tác năm 2025 | 2024-2025; không trước 2023 | Cao |
| Trần Công Đức / `VIE_army_tran_cong_duc` | Phó tư lệnh kiêm Tham mưu trưởng Quân đoàn 34 năm 2026 | 2024-2025; không trước 2023 | Cao |
| Lê Xuân Thế / `VIE_army_le_xuan_the` | Tư lệnh Quân khu 7 từ 2025 | 2025; không trước 2023 | Cao |

## 4. Phân nhóm upstream 19 ID để phục vụ code

Đây là phân nhóm thiết kế bảo thủ, không phải khẳng định ngày bổ nhiệm chính thức cho mọi người.

### 4.1. Có thể xuất hiện ở bookmark 2000

Chỉ nên giữ một nhóm nhỏ có vai trò cấp cao hoặc có khả năng đã là sĩ quan cao cấp trước 2000:

- `VIE_Nguyen_Chi_Vinh`
- `VIE_Ngo_Xuan_Lich`
- `VIE_Phi_Quoc_Tuan`
- `VIE_Nguyen_Quang_Dam`
- `VIE_Pham_Kim_Hau`

Nhóm này vẫn cần kiểm tra thêm hồ sơ chức vụ cụ thể. Nếu yêu cầu lịch sử nghiêm ngặt, chỉ Nguyễn Chí Vịnh hiện có căn cứ đủ mạnh để giữ chắc ở 2000; bốn người còn lại nên dùng mốc 2005 fallback.

### 4.2. Có thể mở từ 2005, dùng fallback nếu thiếu ngày chính thức

- `VIE_Pham_Van_Hung`
- `VIE_Tran_Don`
- `VIE_Vo_Trong_Viet`
- `VIE_Le_Xuan_Duy`
- `VIE_Tran_Viet_Khoa`
- `VIE_Dinh_Gia_That`

Các ID này có role high command, quân khu, binh chủng hoặc hải quân trong MD nhưng report chưa có ngày bắt đầu đủ chắc. Mốc 2005 là fallback gameplay, không nên ghi là ngày lịch sử chính thức.

### 4.3. Nên trì hoãn đến 2015-2016

- `VIE_Phan_Van_Giang`: 2016 là mốc có căn cứ, không nên tuyển từ 2000.
- `VIE_Be_Xuan_Truong`: dùng 2015-2016 theo lớp lãnh đạo quốc phòng hiện đại.

### 4.4. Nên trì hoãn đến 2021

- `VIE_Nguyen_Tan_Cuong`: Tổng Tham mưu trưởng từ 2021.
- `VIE_Nguyen_Trong_Nghia`: vai trò chính trị-quân đội cấp cao thuộc giai đoạn hiện đại.
- `VIE_Pham_Hoai_Nam`: advisor/navy chief gắn với lớp lãnh đạo hải quân hiện đại.
- `VIE_Tran_Quang_Phuong`: advisor không quân/chính trị-quân đội, chưa có căn cứ đưa về 2000.
- `VIE_Vo_Minh_Luong`: vai trò cấp cao hiện đại; report gắn với giai đoạn sau 2020.
- `VIE_Hoang_Xuan_Chien`: advisor quân đội cấp cao hiện đại.

## 5. Đối chiếu với yêu cầu 12 / 6 / 7

Yêu cầu số lượng 12 + 6 + 7 chưa khớp roster hiện tại:

- upstream recruit history: 19 người;
- submod mở rộng: 7 người;
- tổng đang dùng: 26 người;
- 12 + 6 + 7 = 25 người.

Ngoài ra, 7 người mở rộng của submod có nguồn lịch sử gắn với Quân đoàn 12/34 và Quân khu 7 từ 2023-2025, nên không thể đặt họ vào năm 2010 nếu giữ tính lịch sử.

Phân bổ hợp lý hơn cho roster hiện tại là:

- 2000: 1 người chắc chắn, tối đa 5 người nếu chấp nhận suy luận bảo thủ;
- 2005: 6 người fallback;
- 2015-2016: 2 người;
- 2021: 6 người;
- 2023-2025: 7 người mở rộng.

Nếu bắt buộc phải có đúng 12 người đầu game, đó phải là **một quyết định balance/gameplay**, không nên ghi là kết luận lịch sử. Có thể tuyển 12 người đầu game nhưng cần gắn nhãn “roster đại diện sĩ quan đương nhiệm”, không phải “12 người đang giữ chức vụ tương ứng năm 2000”.

## 6. Khuyến nghị triển khai sau báo cáo

1. Giữ character definitions và portrait độc lập với recruitment timing.
2. Không retire/recruit cả roster upstream thành một nhóm duy nhất.
3. Tách event theo cohort 2005, 2016, 2021 và 2023.
4. Giữ Nguyễn Chí Vịnh ở history 2000 nếu muốn có một chỉ huy chiến lược đầu game.
5. Đưa Phan Văn Giang và Bế Xuân Trường vào event 2016.
6. Đưa Nguyễn Tân Cương, Nguyễn Trọng Nghĩa, Phạm Hoài Nam, Trần Quang Phương, Võ Minh Lương và Hoàng Xuân Chiến vào event 2021.
7. Giữ 7 commander submod ở event 2023 hoặc các event chi tiết 2024-2025.
8. Chỉ nâng bốn người hiện đang ở nhóm 2000 lên mức chắc chắn sau khi có hồ sơ chức vụ trước 2005 từ QĐND, Bộ Quốc phòng hoặc TTXVN.

## 7. Trạng thái code tại thời điểm lập báo cáo

Các event cohort tạm thời (2015/2016/2021/2023) đã được thay: còn một event đổi roster ngày 2015.1.1 (`vie_army_commanders.2`) và một event Quân đoàn 12/34 từ 2026 (`vie_army_commanders.1`). Chưa coi số 12/6/7 là dữ kiện lịch sử.
