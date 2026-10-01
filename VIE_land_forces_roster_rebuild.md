# Roster tướng lĩnh Lục quân VIE: bản dựng lại theo 2 giai đoạn (2000-2015 và 2015-nay)

**Ngày:** 01/10/2026
**Thay thế:** `VIE_land_forces_2000_2005_2010_research_report.md` (khung 12/6/7), và các bảng mốc đã lỗi thời trong `VIE_commander_timeline_research_report.md`, `VIE_generals_and_commander_system_research_report.md`.
**Phạm vi:** Lục quân QĐND. Hải quân và Không quân chỉ nhắc ở mục 7.

## 1. Nguyên tắc

1. **Chỉ có hai roster:** Giai đoạn 1 (bookmark 2000, đến hết 2014) và Giai đoạn 2 (01/01/2015 trở đi). Chỉ có **một lần đổi roster** ở 01/01/2015. Không retire/recruit giữa chừng trong mỗi giai đoạn.
2. **Mỗi người thuộc đúng một giai đoạn**, chọn theo thời điểm họ bắt đầu giữ chức vụ cao có nguồn:
   - bắt đầu trước 2015 vào Giai đoạn 1;
   - từ 2015 trở đi vào Giai đoạn 2.
3. **Chấp nhận lệch thời điểm trong cùng giai đoạn.** Một người nhận chức năm 2011 sẽ có mặt từ 2000. Bảng mục 3 ghi rõ độ lệch để bạn biết mình đang đánh đổi gì. Không có cohort trùng người.
4. **Không dùng chức vụ cao nhất để suy ngược.** Ví dụ Hoàng Xuân Chiến (sinh 1961) không được xếp vào Giai đoạn 1.
5. **Chức vụ MD khác thực tế thì giữ vai trò MD, ghi chú lệch** (mục 6).
6. Mức tin cậy: **A** nguồn rõ ngày, **B** nguồn có năm, **C** không đủ dữ kiện.

Nguồn: Wikipedia EN/VI, mod.gov.vn, báo Quân khu 7, QĐND, VietnamNet, Báo Biên phòng. Đây là nguồn thứ cấp, chưa phải quyết định bổ nhiệm gốc.

## 2. Nhân vật theo nguồn gốc

| Nhóm | Số | Ghi chú |
|---|---:|---|
| Upstream MD đã định nghĩa và history tuyển (VIE.txt) | 19 | Hiện bị retire lúc khởi động (trừ Nguyễn Chí Vịnh) |
| Upstream MD có định nghĩa nhưng không tuyển | 1 | `VIE_Hyunh_Chien_Thang` |
| Submod `VIE_army_*` | 7 | Hiện tuyển 01/2023 |
| **Chưa có character, nên tạo mới (`VIE_army_*`)** | 6 | Lê Văn Dũng, Phạm Văn Trà, Phùng Quang Thanh, Nguyễn Khắc Nghiên, Đỗ Bá Tỵ, Lê Mạnh |

Portrait đã có trong `gfx/leaders/VIE/` cho Phạm Văn Trà, Phùng Quang Thanh, Đỗ Bá Tỵ. Lê Văn Dũng, Nguyễn Khắc Nghiên, Lê Mạnh chưa có.

## 3. Giai đoạn 1: roster bookmark 2000 (có mặt từ 01/01/2000 đến 31/12/2014)

| Nhân vật | ID | Vai trò MD đề xuất | Thời gian giữ chức thật | Lệch so với 2000 | Tin cậy |
|---|---|---|---|---|:-:|
| Nguyễn Chí Vịnh | `VIE_Nguyen_Chi_Vinh` (upstream, giữ nguyên) | `field_marshal` | Phó Tổng cục trưởng Tổng cục II 1998; Tổng cục trưởng 2002-2009; Thứ trưởng 2009-2021 | 2 năm | B |
| Lê Văn Dũng | `VIE_army_le_van_dung` (mới) | `field_marshal` + advisor `army_chief` | Tổng Tham mưu trưởng 22/05/1998 - 05/2001; Tư lệnh QK7 1995-1998 | 0 | A |
| Phạm Văn Trà | `VIE_army_pham_van_tra` (mới, có portrait) | advisor `high_command` | Bộ trưởng Quốc phòng 12/1997 - 06/2006 | 0 | A |
| Phùng Quang Thanh | `VIE_army_phung_quang_thanh` (mới, có portrait) | `corps_commander` + advisor `army_chief` | **Tư lệnh Quân khu 1 02/1998 - 05/2001** (Trung tướng 1999), Tổng Tham mưu trưởng 05/2001 - 08/2006, Bộ trưởng 2006-2016. Đã là tư lệnh quân khu ở bookmark 2000, nên lệch 0 | 0 | A |
| Lê Mạnh (**bỏ khỏi mặc định**, xem mục 10) | `VIE_army_le_manh` (mới, tùy chọn) | `corps_commander` | Tham mưu trưởng QK7 2000-2004, Tư lệnh QK7 2005-2009 | 0 đến 5 năm | A |
| Nguyễn Khắc Nghiên | `VIE_army_nguyen_khac_nghien` (mới) | advisor `army_chief` | Tham mưu trưởng QK2 1998-2001, Tư lệnh QK1 2001-2002, Tư lệnh QK5 2002-2005, Phó Tổng Tham mưu trưởng 2004-2006, Tổng Tham mưu trưởng 31/08/2006 - 13/11/2010 | 6,7 năm | A |
| Phí Quốc Tuấn | `VIE_Phi_Quoc_Tuan` (upstream) | `corps_commander` | Tư lệnh Bộ Tư lệnh Thủ đô Hà Nội 2009-2015 | 9 năm | B |
| Đỗ Bá Tỵ | `VIE_army_do_ba_ty` (mới, có portrait) | advisor `army_chief` | Tham mưu trưởng QK2 04/2001 - 02/2007, Tư lệnh QK2 02/2007 - 10/2010, Tổng Tham mưu trưởng 13/11/2010 - 17/05/2016 | 10,9 năm | A |
| Trần Đơn | `VIE_Tran_Don` (upstream) | `high_command` (army) | Tham mưu trưởng QK7 2009-2011, Tư lệnh QK7 2011 - 10/2015 | 11 năm | A |
| Ngô Xuân Lịch | `VIE_Ngo_Xuan_Lich` (upstream) | `corps_commander` | Phó Chủ nhiệm TCCT 2008, Chủ nhiệm TCCT 2011-2016 | 11 năm | A |
| Võ Trọng Việt | `VIE_Vo_Trong_Viet` (upstream) | `high_command` (ledger air) | Tư lệnh Biên phòng 2012-2015, Thứ trưởng 2015-2016 | 12 năm | A |

Chia phạm vi lệch như sau:
- **Gần đúng (≤ 2 năm):** Dũng, Trà, Vịnh, Thanh. Đây là lõi nên có.
- **Lệch vừa (5-7 năm):** Nghiên, Mạnh.
- **Lệch lớn (9-12 năm):** Tuấn, Tỵ, Đơn, Lịch, Việt. Năm 2000 những người này mới chỉ là sĩ quan cấp thấp hoặc trung. Nếu muốn giảm anachronism, có thể đưa năm người này sang Giai đoạn 2 thay vì giữ ở Giai đoạn 1, nhưng khi đó họ lệch tương tự theo hướng ngược lại (xuất hiện muộn 3-6 năm). **Đề xuất: giữ ở Giai đoạn 1** vì ít nhất họ đã có vai trò trước ranh giới 2015.

## 4. Giai đoạn 2: roster 01/01/2015 trở đi

**Sự kiện đổi roster 01/01/2015** vừa tuyển nhóm mới vừa rút nhóm cũ.

### 4.1. Tuyển vào

| Nhân vật | ID | Vai trò MD | Thời gian giữ chức thật | Lệch so với 2015 | Tin cậy |
|---|---|---|---|---|:-:|
| Bế Xuân Trường | `VIE_Be_Xuan_Truong` | `high_command` (army) | Tư lệnh QK1; Phó Tổng Tham mưu trưởng; Thứ trưởng và Thượng tướng 10/2015 | 0,8 năm | A |
| Võ Minh Lương | `VIE_Vo_Minh_Luong` | `high_command` (ledger air) | Tham mưu trưởng QK7 từ 2011; Tư lệnh QK7 10/2015 - 11/2020 | 0,8 năm | A |
| Phan Văn Giang | `VIE_Phan_Van_Giang` | `high_command` (army) | Tư lệnh QK1 2014-2016; Tổng Tham mưu trưởng 05/2016 - 06/2021; Bộ trưởng từ 2021 | 1,4 năm | A |
| Nguyễn Trọng Nghĩa | `VIE_Nguyen_Trong_Nghia` | `high_command` (army) | Phó Chủ nhiệm TCCT từ 09/2012; Thượng tướng khoảng 2017 | 2 năm | B |
| Hoàng Xuân Chiến | `VIE_Hoang_Xuan_Chien` | `army_chief` | Tư lệnh Biên phòng 11/2015 - 2020; Thứ trưởng 07/2020 | 0,8 đến 5,5 năm | A |
| Nguyễn Tân Cương | `VIE_Nguyen_Tan_Cuong` | `army_chief` | Tư lệnh QK4 11/2014 - 11/2018; Tổng Tham mưu trưởng từ 06/2021 | 6,5 năm | A |
| Huỳnh Chiến Thắng | `VIE_Hyunh_Chien_Thang` (tùy chọn) | `corps_commander` | Phó Tổng Tham mưu trưởng từ 11/2020, Thượng tướng 11/2022 | 5,8 năm | A |
| Lê Xuân Duy | `VIE_Le_Xuan_Duy` | `high_command` (army) | Thiếu tướng 2013 (Chỉ huy trưởng Bộ CHQS Yên Bái), Phó Tư lệnh QK2, **Tư lệnh QK2 05/2016 - 08/2016** (thời gian ngắn, theo Wikipedia VI) | 1 năm | B |
| Phạm Văn Hùng | `VIE_Pham_Van_Hung` | `high_command` (army) | Không tìm được nguồn | không xác định | C |

Hai người nhãn C vẫn để ở Giai đoạn 2 vì tuyển muộn đỡ sai hơn tuyển sớm.

### 4.2. Rút khỏi roster

Rút ở 01/01/2015 những người đã nghỉ hoặc sắp rời vị trí chỉ huy:

| Nhân vật | Vì sao rút |
|---|---|
| Lê Văn Dũng | Rời vị trí 2001 |
| Phạm Văn Trà | Rời vị trí 2006 |
| Nguyễn Khắc Nghiên | Rời vị trí 2010 |
| Lê Mạnh | Rời vị trí 2009 |
| Phí Quốc Tuấn | Rời Bộ Tư lệnh Thủ đô 2015 |
| Phùng Quang Thanh | Rời Bộ trưởng 2016 (sớm hơn khoảng 1 năm; chấp nhận) |
| Đỗ Bá Tỵ | Rời Tổng Tham mưu trưởng 05/2016 (sớm hơn khoảng 1 năm; chấp nhận) |

**Ở lại qua 2015 (không rút):** Nguyễn Chí Vịnh (Thứ trưởng đến 2021), Trần Đơn (Thứ trưởng từ 10/2015), Ngô Xuân Lịch (Bộ trưởng 2016-2021), Võ Trọng Việt (Thứ trưởng 2015-2016).

### 4.3. Commander Quân đoàn 12/34 và Quân khu 7 (7 ID submod): đề xuất giữ riêng

Quân đoàn 12 thành lập 02/12/2023 và Quân đoàn 34 thành lập 15/12/2024. Nếu tuyển cùng lúc 2015, commander xuất hiện trước khi quân đoàn tồn tại tới 8-11 năm, đây là lệch lớn nhất trong cả roster. Có hai lựa chọn:

| Lựa chọn | Mô tả | Đánh đổi |
|---|---|---|
| **A (đề xuất)** | Giữ riêng một sự kiện có sẵn cho 7 người này, dời từ 01/2023 sang 01/01/2026 (mốc có nguồn cho cả 7 người) | Thêm một mốc thứ ba, nhưng đã có sẵn trong code nên không thêm cơ chế |
| B | Gộp vào event 2015 | Đúng yêu cầu hai giai đoạn, nhưng sai lịch sử rõ rệt |

| Người (submod) | ID | Giữ chức từ |
|---|---|---|
| Trần Đại Thắng | `VIE_army_tran_dai_thang` | Chính ủy Quân đoàn 12, từ 12/2023 |
| Nguyễn Bá Lực | `VIE_army_nguyen_ba_luc` | Tư lệnh Quân đoàn 34, 12/2024 - 04/2025 |
| Lê Xuân Thuân | `VIE_army_le_xuan_thuan` | Tư lệnh Quân đoàn 12, 24/04/2025 |
| Đào Tuấn Anh | `VIE_army_dao_tuan_anh` | Tư lệnh Quân đoàn 34, 24/04/2025 |
| Lê Xuân Thế | `VIE_army_le_xuan_the` | Tư lệnh QK7, 28/06/2025 |
| Nguyễn Thành Phố | `VIE_army_nguyen_thanh_pho` | Phó Tư lệnh kiêm Tham mưu trưởng Quân đoàn 12, nguồn 2026 |
| Trần Công Đức | `VIE_army_tran_cong_duc` | Phó Tư lệnh kiêm Tham mưu trưởng Quân đoàn 34, nguồn 2026 |

## 5. Thay đổi code cần làm (đề xuất, chưa thực hiện)

1. **Startup ([VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt)):** chỉ retire các nhân vật của Giai đoạn 2. Bỏ khỏi danh sách retire: `VIE_Ngo_Xuan_Lich`, `VIE_Phi_Quoc_Tuan`, `VIE_Tran_Don`, `VIE_Vo_Trong_Viet`. Giữ retire cho các người còn lại ở Giai đoạn 2. Hải quân và Không quân xem mục 7.
2. **Tuyển Giai đoạn 1 lúc khởi động:** thêm `recruit_character` cho 5 character mới (Dũng, Trà, Thanh, Nghiên, Tỵ) và Mạnh nếu dùng.
3. **Gộp event 2015, 2016 và 2021 thành một event 01/01/2015** ([VIE_md_effects_p16.txt](common/scripted_effects/VIE_md_effects_p16.txt), [VIE_army_commanders.txt](events/VIE_army_commanders.txt)): tuyển nhóm 4.1 và rút nhóm 4.2.
4. **Bỏ điều kiện `NOT has_character = ...` làm cổng** trong scheduler. Sau `retire_character` ở startup chưa rõ trigger này có trả false hay không; nếu true, event sẽ không bao giờ chạy. Cờ `VIE_md_roster_recruited_2015` đã đủ làm cổng.
5. **Event 7 commander submod:** đổi ngưỡng ngày từ `date > 2022.12.31` sang `date > 2025.12.31` nếu chọn lựa chọn A ở mục 4.3.
6. **Localisation:** thêm tên cho 6 character mới; sửa hiển thị "Phi Quốc Tuấn" thành "Phí Quốc Tuấn".
7. **Chạy game và đọc `error.log`.** Tôi chưa test hành vi trong game.
8. **Sửa tài liệu cũ:** [VIE_generals_and_commander_system_research_report.md](VIE_generals_and_commander_system_research_report.md) còn ghi "tuyển khi khởi động", "8 portrait", "chưa có portrait riêng" (thực tế 14 file `.dds`); [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) còn mốc 2005 và mâu thuẫn về Nguyễn Chí Vịnh.

## 6. Điểm lệch giữa MD và lịch sử (không tự sửa upstream)

| Nhân vật | MD | Lịch sử | Đề xuất |
|---|---|---|---|
| Ngô Xuân Lịch | `corps_commander` | Cán bộ chính trị, Chủ nhiệm TCCT rồi Bộ trưởng | Giữ vai trò MD; ở Giai đoạn 1 |
| Võ Trọng Việt, Võ Minh Lương | `high_command` ledger **air** | Tướng Biên phòng và tư lệnh quân khu (Lục quân) | Giữ ledger air của MD; xếp giai đoạn theo sự nghiệp Lục quân |
| Bế Xuân Trường | Nhóm chính trị-quân đội | Tướng chỉ huy: Tư lệnh QK1, Phó Tổng Tham mưu trưởng | Vai trò MD là `high_command` army nên không đổi |
| Nguyễn Chí Vịnh | `field_marshal`, skill 4, logistics 5 | Tình báo quốc phòng, không phải chỉ huy dã chiến | Giữ làm field marshal bookmark 2000 |
| Phí Quốc Tuấn | Tên "Phi" | Tên đúng "Phí" | Sửa localisation hiển thị |

## 7. Ngoài phạm vi, giữ nguyên, chưa kiểm tra lại

Không Lục quân, nhưng đang nằm chung các event tuyển nên cần xem lại riêng khi gộp event:
- Hải quân: Phạm Hoài Nam, Phạm Kim Hậu, Đinh Gia Thất.
- Không quân: Trần Quang Phương, Trần Việt Khoa.
- Nguyễn Quang Đạm (`army_chief` upstream, nhưng repo xếp Hải quân): chưa xác minh được.

Khi gộp event 2015/2016/2021, các nhân vật này nên được giữ nguyên ngày hiện có hoặc đưa vào Giai đoạn 2 mà không đổi thêm gì khác.

## 8. So sánh với khung cũ

| | Báo cáo cũ | Bản này |
|---|---|---|
| Số mốc | 3 cohort 12/6/7, trùng người | 2 giai đoạn (+1 mốc phụ cho 7 người Quân đoàn 12/34) |
| Trùng người | Có (6/6 ở 2005 đã có ở 2000) | Không |
| Đỗ Bá Tỵ, Thanh, Nghiên | Có trong cohort, không có character | Tạo mới, Giai đoạn 1 |
| Hoàng Xuân Chiến | Cohort 2010 | Giai đoạn 2 |
| Phí Quốc Tuấn, Võ Trọng Việt | Cohort 2000/2005 | Giai đoạn 1, kèm ghi chú độ lệch |
| Võ Minh Lương | Cohort 2010, "Thứ trưởng sau 2015" | Giai đoạn 2, Tư lệnh QK7 10/2015 |
| Cơ chế game | 3 event cohort | 1 event đổi roster + 1 event Quân đoàn 12/34 |

## 10. Mở rộng: 10 tướng Lục quân bổ sung (nghiên cứu 01/10/2026)

Mục tiêu: thêm khoảng 10 tướng Lục quân có nguồn, chủ yếu là tư lệnh quân khu và Phó Tổng Tham mưu trưởng, mà không phá giới hạn commander (tối đa 6 mỗi giai đoạn). Nguồn chính là danh sách tư lệnh trên Wikipedia VI cho từng Quân khu và bảng Phó Tổng Tham mưu trưởng, đối chiếu thêm báo chính thống. Các ngày lấy từ nguồn thứ cấp.

### 10.1. Mười người được chọn

| # | Nhân vật | Giai đoạn | Vai trò MD đề xuất | Chức vụ chính (nguồn) | Tin cậy |
|--:|---|---|---|---|:-:|
| 1 | Huỳnh Tiền Phong | 1 | `corps_commander` | Tư lệnh Quân khu 9 2000-2007, Trung tướng, Anh hùng LLVTND (phong 26/12/2025) | A |
| 2 | Nguyễn Văn Được | 1 | advisor `high_command` | Tư lệnh Quân khu 5 1997-2002 (Trung tướng), sau đó Thứ trưởng Bộ Quốc phòng. Ngày chính xác chỉ có một nguồn | B |
| 3 | Hoàng Kỳ | 1 | advisor `high_command` | Tư lệnh Quân khu 3 1996-2005, Phó Tổng Tham mưu trưởng 2005-2008 (Trung tướng) | A |
| 4 | Phạm Xuân Hùng | 1 | advisor `high_command` | Tư lệnh Quân khu 3 khoảng 2004/2005-2006, Phó Tổng Tham mưu trưởng 2008-2016, Thượng tướng 2014. Hai nguồn lệch 1 năm về thời điểm nhận Quân khu 3 | A |
| 5 | Nguyễn Phương Nam | 2 | advisor `high_command` | Tư lệnh Quân khu 9 04/2011 - 09/2015, Phó Tổng Tham mưu trưởng từ 09/2015, Thượng tướng 12/2016 | A |
| 6 | Vũ Hải Sản | 2 | advisor `high_command` | Phó Tham mưu trưởng QK3 2013-2015, Tư lệnh QK3 đến 07/2020, Thứ trưởng 14/07/2020. Wikipedia ghi tư lệnh từ 2015, báo ghi từ 2018: dùng 07/2020 làm mốc chắc | B |
| 7 | Phùng Sĩ Tấn | 2 | `corps_commander` | Tư lệnh Quân khu 2 12/2016 - 09/2019, Phó Tổng Tham mưu trưởng từ 15/09/2019 | A |
| 8 | Nguyễn Doãn Anh | 2 | `corps_commander` | Tư lệnh Bộ Tư lệnh Thủ đô, Tư lệnh Quân khu 4 11/2018 - 11/2022, Phó Tổng Tham mưu trưởng từ 11/2022 | A |
| 9 | Nguyễn Hồng Thái | 2 | `corps_commander` | Tư lệnh Quân khu 1 từ 10/2019 (Wikipedia: đến 2025; một nguồn báo ghi 03/2024), Thứ trưởng 04/2025, Thượng tướng 07/2025 | B |
| 10 | Trương Mạnh Dũng | Mốc phụ 2026 | `corps_commander` | Tư lệnh Quân đoàn 12 từ 12/2023 đến 24/04/2025, Tư lệnh Quân khu 1 từ 26/04/2025, Phó Tổng Tham mưu trưởng từ 22/06/2026 | A |

Trương Mạnh Dũng khớp mục 3.1 của báo cáo tướng lĩnh ("Giai đoạn đầu thành lập: Thiếu tướng Trương Mạnh Dũng") và bổ sung ID còn thiếu cho Quân đoàn 12.

### 10.2. Bị loại sau khi kiểm tra nguồn

| Nhân vật | Lý do |
|---|---|
| Võ Văn Tuấn | Gốc Phòng không-Không quân (Phó Tư lệnh kiêm Tham mưu trưởng Quân chủng PK-KQ 2008), phi công. Phó Tổng Tham mưu trưởng 2011-2017 nhưng không phải Lục quân |
| Phạm Ngọc Minh | Gốc Hải quân (Phó Tư lệnh kiêm Tham mưu trưởng Hải quân 2005), sau là Tư lệnh Cảnh sát biển. Phó Tổng Tham mưu trưởng 2014-2019 nhưng không phải Lục quân |
| Lê Mạnh | Hợp lệ (Tư lệnh QK7 2005-2009), nhưng Giai đoạn 1 đã đủ 6 commander; để làm tùy chọn |
| Phạm Xuân Thệ, Nguyễn Văn Lân, Trần Phi Hổ, Nguyễn Văn Đạo, Ma Thanh Toàn, Nguyễn Khắc Dương | Tư lệnh quân khu hợp lệ (Wikipedia VI), nhưng chỉ có một nguồn và vượt giới hạn; dự phòng nếu cần thêm |
| Trương Đình Thanh | Tư lệnh Quân khu 4 02/2002 - 01/2005, mất trong tai nạn máy bay 26/01/2005; thích hợp cho một sự kiện riêng, không phải roster |

### 10.3. Điều chỉnh đi kèm với mục 3 và 4

- **Phùng Quang Thanh** là Tư lệnh Quân khu 1 từ 02/1998 đến 05/2001 (Trung tướng 1999), nên đã là tư lệnh quân khu ở bookmark 2000, không phải chỉ xuất hiện từ 2001. Vai trò: `corps_commander` + advisor `army_chief`.
- **Nguyễn Khắc Nghiên** và **Đỗ Bá Tỵ** trước khi làm Tổng Tham mưu trưởng đều là tư lệnh quân khu (Nghiên QK1, QK5; Tỵ QK2). Vẫn đặt ở advisor `army_chief` để giữ giới hạn commander.
- **Lê Xuân Duy** có chức vụ nguồn: Tư lệnh QK2 05/2016 - 08/2016 (ngắn). Nâng từ nhãn C lên B.
- **Phạm Xuân Hùng** (mới, Phó Tổng Tham mưu trưởng 2008-2016) khác **Phạm Văn Hùng** (upstream `VIE_Pham_Van_Hung`, chưa tìm được nguồn). Hai người khác nhau.

### 10.4. Cân đối số lượng

| | Giai đoạn 1 | Giai đoạn 2 |
|---|---:|---:|
| Commander | 6 (Vịnh, Dũng, Thanh, Phong, Tuấn, Lịch) | 5-6 (Vịnh, Lịch, Tấn, Doãn Anh, Thái, + Thắng tùy chọn) |
| Advisor | 10 | 12 |

Mục 3 và 4 liệt kê roster gốc; mục 10 này là phần bổ sung và thay thế các vai trò đã nêu ở 10.3. Danh sách rút khỏi roster ở 01/01/2015 (mục 4.2) cần thêm Huỳnh Tiền Phong, Nguyễn Văn Được, Hoàng Kỳ và Phạm Xuân Hùng, và Phùng Quang Thanh đã được tính; mục 4.1 cần thêm Nguyễn Phương Nam, Vũ Hải Sản, Phùng Sĩ Tấn, Nguyễn Doãn Anh, Nguyễn Hồng Thái.

## 11. Nguồn

- [Chief of the General Staff (Vietnam)](https://en.wikipedia.org/wiki/Chief_of_the_General_Staff_(Vietnam))
- [Minister of Defence (Vietnam)](https://en.wikipedia.org/wiki/Minister_of_Defence_(Vietnam))
- [Bộ trưởng Phạm Văn Trà (1997-2006), mod.gov.vn](http://mod.gov.vn/bo-truong/bai-viet?current=true&urile=wcm:path:/mod/sa-mod-site/minister-site/tien-nhiem/06511a76-1324-4a67-b1ff-d8cfa49f138b)
- [Ngô Xuân Lịch (EN Wikipedia)](https://en.wikipedia.org/wiki/Ng%C3%B4_Xu%C3%A2n_L%E1%BB%8Bch)
- [Quân khu 7 (VI Wikipedia)](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_7,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam)
- [Võ Minh Lương](https://vi.wikipedia.org/wiki/V%C3%B5_Minh_L%C6%B0%C6%A1ng)
- [Nguyễn Chí Vịnh](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Ch%C3%AD_V%E1%BB%8Bnh)
- [Võ Trọng Việt](https://vi.wikipedia.org/wiki/V%C3%B5_Tr%E1%BB%8Dng_Vi%E1%BB%87t)
- [Hoàng Xuân Chiến](https://vi.wikipedia.org/wiki/Ho%C3%A0ng_Xu%C3%A2n_Chi%E1%BA%BFn)
- [Bế Xuân Trường](https://vi.wikipedia.org/wiki/B%E1%BA%BF_Xu%C3%A2n_Tr%C6%B0%E1%BB%9Dng)
- [Huỳnh Chiến Thắng](https://vi.wikipedia.org/wiki/Hu%E1%BB%B3nh_Chi%E1%BA%BFn_Th%E1%BA%AFng)
- [Nguyễn Tân Cương](https://vietnamnet.vn/ho-so/ong-nguyen-tan-cuong-C001108.html)
- [Phan Văn Giang](https://baochinhphu.vn/tieu-su-dong-chi-phan-van-giang-102290457.htm)
- [Nguyễn Trọng Nghĩa](https://vietnamnet.vn/ho-so/ong-nguyen-trong-nghia-C000615.html)
- [MD VIE.txt (upstream)](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt)
- Mục 10 (mở rộng): [Quân khu 1](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_1,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Quân khu 2](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_2,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Quân khu 3](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_3,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Quân khu 4](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_4,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Quân khu 5](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_5,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Quân khu 9](https://vi.wikipedia.org/wiki/Qu%C3%A2n_khu_9,_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam), [Phó Tổng Tham mưu trưởng QĐND](https://vi.wikipedia.org/wiki/Ph%C3%B3_T%E1%BB%95ng_tham_m%C6%B0u_tr%C6%B0%E1%BB%9Fng_Qu%C3%A2n_%C4%91%E1%BB%99i_nh%C3%A2n_d%C3%A2n_Vi%E1%BB%87t_Nam)
- Mục 10, từng người: [Huỳnh Tiền Phong](https://vi.wikipedia.org/wiki/Hu%E1%BB%B3nh_Ti%E1%BB%81n_Phong), [Nguyễn Phương Nam](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Ph%C6%B0%C6%A1ng_Nam), [Vũ Hải Sản](https://vi.wikipedia.org/wiki/V%C5%A9_H%E1%BA%A3i_S%E1%BA%A3n), [Phùng Sĩ Tấn](https://vi.wikipedia.org/wiki/Ph%C3%B9ng_S%C4%A9_T%E1%BA%A5n), [Nguyễn Doãn Anh](https://vi.wikipedia.org/wiki/Nguy%E1%BB%85n_Do%C3%A3n_Anh), [Phạm Xuân Hùng](https://vi.wikipedia.org/wiki/Ph%E1%BA%A1m_Xu%C3%A2n_H%C3%B9ng), [Trương Mạnh Dũng](https://vi.wikipedia.org/wiki/Tr%C6%B0%C6%A1ng_M%E1%BA%A1nh_D%C5%A9ng), [Võ Văn Tuấn](https://vi.wikipedia.org/wiki/V%C3%B5_V%C4%83n_Tu%E1%BA%A5n) và [Phạm Ngọc Minh](https://vi.wikipedia.org/wiki/Ph%E1%BA%A1m_Ng%E1%BB%8Dc_Minh) (hai người bị loại), [Nguyễn Hồng Thái](https://xaydungchinhsach.chinhphu.vn/tieu-su-dong-chi-nguyen-hong-thai-bi-thu-tinh-uy-bac-ninh-119250930132050503.htm)
- Mốc Quân đoàn 12/34 và các commander 2023-2026: xem [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) mục 2.
