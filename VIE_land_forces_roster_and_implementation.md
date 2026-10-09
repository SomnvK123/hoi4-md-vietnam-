# Hệ thống Tướng lĩnh & Roster Lục quân Việt Nam — Millennium Dawn

> **Tài liệu tổng hợp danh sách tướng lĩnh & kế hoạch triển khai (08/10/2026)**  
> Hợp nhất 4 tài liệu phân mảnh về tướng lĩnh Lục quân.

## Mục lục
1. [Phần 1: Roster tướng lĩnh Lục quân VIE dựng lại](#phần-1-roster-tướng-lĩnh-lục-quân-vie-dựng-lại-theo-2-giai-đoạn-2000-2015-và-2015-nay)
2. [Phần 2: Plan triển khai v2 — Chuẩn Millennium Dawn](#phần-2-plan-triển-khai-v2--roster-tướng-lục-quân-vie-theo-chuẩn-millennium-dawn)
3. [Phụ lục I: Plan triển khai v1 (Lịch sử)](#phụ-lục-i-plan-triển-khai-v1-lịch-sử-tham-khảo)
4. [Phụ lục II: Báo cáo nghiên cứu cohort (Lịch sử)](#phụ-lục-ii-báo-cáo-nghiên-cứu-cohort-2000--2005--2010-lịch-sử-tham-khảo)

---
## Phần 1: Roster tướng lĩnh Lục quân VIE dựng lại theo 2 giai đoạn (2000-2015 và 2015-nay)

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

---

## Phần 2: Plan triển khai v2 — Roster tướng Lục quân VIE theo chuẩn Millennium Dawn

# Plan triển khai v2: roster tướng Lục quân VIE theo kiểu Millennium Dawn

**Ngày:** 01/10/2026 (cập nhật lần 2: thêm 10 tướng mở rộng)
**Thay thế:** [VIE_land_forces_implementation_plan.md](VIE_land_forces_implementation_plan.md) (v1).
**Dữ liệu, nguồn và lý do chọn người:** [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md), đặc biệt mục 10 (10 tướng mở rộng).
**Khác v1 ở đâu:** v1 mặc định nhóm upstream sẽ được "retire lúc khởi động rồi tuyển lại 2015". Chưa ai chứng minh được vòng này chạy. v2 làm thí nghiệm trước, rồi chọn một trong hai nhánh, và chỉ dựa vào thao tác một chiều cho phần chắc chắn.

## 0. Trạng thái triển khai (01/10/2026)

**Đã làm trong working tree (chưa commit, chưa chạy game):**

| Hạng mục | Kết quả |
|---|---|
| Character mới | 15 ID trong [VIE_md_army_legacy.txt](common/characters/VIE_md_army_legacy.txt) (14 mới + Lê Mạnh tùy chọn) và Trương Mạnh Dũng trong [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt) |
| Trait và cost | 45 trait đã đối chiếu với `common/unit_leader` và `common/country_leader` của MD: tồn tại, đúng loại vai trò, advisor đúng slot. Cost theo mẫu upstream |
| Sửa 6 commander submod cũ | Trait `engineer` không tồn tại thành `trait_engineer`; `offensive_doctrine`/`defensive_doctrine` chỉ dành cho field marshal nên đổi sang `adaptable`/`desperate_defender` cho corps commander; điểm kỹ năng đưa về tổng 10 |
| Portrait | 13 ảnh placeholder (silhouette, không phải chân dung thật) bằng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py); header DDS trùng byte với ảnh đang chạy |
| Localisation | Tên và `idea_token` cho mọi nhân vật mới |
| Startup, scheduler, event | Tuyển Giai đoạn 1 lúc khởi động; event .2 đổi roster 2015; event .1 thêm Trương Mạnh Dũng; ngưỡng Quân đoàn 12/34 là 2025.12.31 |
| Tài liệu | Cập nhật 3 báo cáo cũ và [tools/TESTING.md](tools/TESTING.md) |

**Quyết định đã áp dụng (nhánh N của mục 4, bước 5):** khối retire ở startup đã bị xóa **toàn bộ**, event .3 và .4 đã bị xóa, nên cả nhóm upstream Giai đoạn 2 (Giang, Cương, Chiến...) **và** nhóm Hải quân/Không quân (Hậu, Thất, Khoa, Đạm, Nam, Phương) đều có mặt từ 2000 theo history MD, thay vì bị giữ đến 2015 hoặc 2021 như code cũ. Event .2 tuyển 5 character mới của Giai đoạn 2 và rút 10 người của Giai đoạn 1.

**Chưa làm:** thí nghiệm E1-E4 (cần chạy game), thay portrait placeholder bằng ảnh thật, tạo nhánh git và commit, và sửa lỗi thiếu BOM có sẵn ở `VIE_md_mil_l_english.yml`.

**Nếu E1 đạt và muốn đưa nhóm upstream về đúng 2015:** khôi phục khối retire ở startup (chỉ nhóm Giai đoạn 2, bỏ Lịch, Tuấn, Đơn, Việt), thêm lại `recruit_character` cho nhóm đó ở event .2 theo mục 4, bước 6 (nhánh R).

## 1. Nguyên tắc thiết kế (rút từ cách MD làm Trung Quốc)

1. **Roster là ảnh chụp của thời kỳ, không phải đường thời gian.** MD tuyển cả nhóm vào khối `2000.1.1` và không xoay theo năm. Vì vậy submod chỉ có đúng một lần đổi (2015), cộng một mốc phụ 2026 cho nhóm Quân đoàn 12/34.
2. **Chỉ dùng thao tác một chiều đã có tiền lệ:** `recruit_character` (chưa tuyển → đã tuyển) và `retire_character` (đã tuyển → nghỉ, không quay lại). Vòng "retire rồi tuyển lại đúng người đó" chỉ dùng khi thí nghiệm E1 chứng minh được.
3. **Số commander theo công thức MD.** VIE 2000 có 34 sư đoàn, công thức ra khoảng 3-4 tướng; upstream có 1 field marshal + 3 corps commander. v2 giữ **tối đa 6 commander** mỗi giai đoạn, phần còn lại là advisor.
4. **Dùng vai trò kép như MD.** Người đứng đầu tham mưu là `field_marshal` + advisor `army_chief`; tư lệnh quân khu có chức tham mưu cấp cao là `corps_commander` + advisor. Người không chỉ huy quân thì chỉ là advisor.
5. **Điểm kỹ năng theo công thức MD:** `skill` là cấp, và `attack + defense + planning + logistics = (skill - 1) × 3 + 4`. Đã đối chiếu: Vịnh (skill 4) tổng 13; Phí Quốc Tuấn, Ngô Xuân Lịch, Huỳnh Chiến Thắng (skill 3) tổng 10. Công thức khớp, nên dùng cho mọi character mới.
6. **Không chép đè ID upstream.** Chỉ thêm ID `VIE_army_*`.
7. **Chỉ Lục quân.** Trong lúc nghiên cứu mở rộng tôi loại Võ Văn Tuấn (gốc Phòng không-Không quân) và Phạm Ngọc Minh (gốc Hải quân/Cảnh sát biển) dù cả hai là Phó Tổng Tham mưu trưởng.

## 2. Roster v2

Nguồn, ngày giữ chức và độ tin cậy của từng người: xem [roster report](VIE_land_forces_roster_rebuild.md) mục 3, 4 và 10.

### 2.1. Giai đoạn 1 (bookmark 2000, đến hết 2014)

| Nhân vật | ID | Vai trò | Nguồn |
|---|---|---|---|
| Nguyễn Chí Vịnh | `VIE_Nguyen_Chi_Vinh` | `field_marshal` (có sẵn) | Upstream |
| Lê Văn Dũng | `VIE_army_le_van_dung` | `field_marshal` + advisor `army_chief` | **Mới** |
| Phùng Quang Thanh | `VIE_army_phung_quang_thanh` | `corps_commander` + advisor `army_chief` | **Mới** |
| Huỳnh Tiền Phong | `VIE_army_huynh_tien_phong` | `corps_commander` | **Mới (mở rộng)** |
| Phí Quốc Tuấn | `VIE_Phi_Quoc_Tuan` | `corps_commander` (có sẵn) | Upstream |
| Ngô Xuân Lịch | `VIE_Ngo_Xuan_Lich` | `corps_commander` (có sẵn) | Upstream |
| Phạm Văn Trà | `VIE_army_pham_van_tra` | advisor `high_command` | **Mới** |
| Nguyễn Khắc Nghiên | `VIE_army_nguyen_khac_nghien` | advisor `army_chief` | **Mới** |
| Đỗ Bá Tỵ | `VIE_army_do_ba_ty` | advisor `army_chief` | **Mới** |
| Nguyễn Văn Được | `VIE_army_nguyen_van_duoc` | advisor `high_command` | **Mới (mở rộng)** |
| Hoàng Kỳ | `VIE_army_hoang_ky` | advisor `high_command` | **Mới (mở rộng)** |
| Phạm Xuân Hùng | `VIE_army_pham_xuan_hung` | advisor `high_command` | **Mới (mở rộng)** |
| Trần Đơn | `VIE_Tran_Don` | advisor `high_command` (có sẵn) | Upstream |
| Võ Trọng Việt | `VIE_Vo_Trong_Viet` | advisor `high_command`, ledger air (có sẵn) | Upstream |

**Commander: 6** (Vịnh, Dũng, Thanh, Phong, Tuấn, Lịch), đúng giới hạn. **Advisor: 10.** Lê Mạnh bị bỏ khỏi mặc định vì Phong thay vai corps commander của quân khu và vì đã đủ 6. Nếu muốn thêm Mạnh, phải loại một người khác hoặc chấp nhận 7 commander.

Dũng, Thanh, Nghiên, Tỵ cùng chiếm slot `army_chief`, mỗi lần người chơi chỉ chọn được một người, nên game tự giữ đúng chuỗi Tổng Tham mưu trưởng.

### 2.2. Giai đoạn 2 (từ 01/01/2015)

| Nhân vật | ID | Vai trò | Nguồn |
|---|---|---|---|
| Phùng Sĩ Tấn | `VIE_army_phung_si_tan` | `corps_commander` | **Mới (mở rộng)** |
| Nguyễn Doãn Anh | `VIE_army_nguyen_doan_anh` | `corps_commander` | **Mới (mở rộng)** |
| Nguyễn Hồng Thái | `VIE_army_nguyen_hong_thai` | `corps_commander` | **Mới (mở rộng)** |
| Huỳnh Chiến Thắng (tùy chọn) | `VIE_Hyunh_Chien_Thang` | `corps_commander` | Upstream |
| Nguyễn Phương Nam | `VIE_army_nguyen_phuong_nam` | advisor `high_command` | **Mới (mở rộng)** |
| Vũ Hải Sản | `VIE_army_vu_hai_san` | advisor `high_command` | **Mới (mở rộng)** |
| Bế Xuân Trường | `VIE_Be_Xuan_Truong` | advisor `high_command` army | Upstream |
| Võ Minh Lương | `VIE_Vo_Minh_Luong` | advisor `high_command` ledger air | Upstream |
| Phan Văn Giang | `VIE_Phan_Van_Giang` | advisor `high_command` army | Upstream |
| Nguyễn Trọng Nghĩa | `VIE_Nguyen_Trong_Nghia` | advisor `high_command` army | Upstream |
| Hoàng Xuân Chiến | `VIE_Hoang_Xuan_Chien` | advisor `army_chief` | Upstream |
| Nguyễn Tân Cương | `VIE_Nguyen_Tan_Cuong` | advisor `army_chief` | Upstream |
| Lê Xuân Duy | `VIE_Le_Xuan_Duy` | advisor `high_command` army (nhãn B) | Upstream |
| Phạm Văn Hùng | `VIE_Pham_Van_Hung` | advisor `high_command` army (nhãn C) | Upstream |

Ở lại từ Giai đoạn 1: Vịnh, Lịch (commander), Đơn, Việt (advisor). Tổng commander Giai đoạn 2: 5 (6 nếu dùng Thắng).

### 2.3. Mốc phụ: Quân đoàn 12/34 và Quân khu 7

Giữ 7 ID `VIE_army_*` hiện có và event hiện có, dời ngưỡng sang `date > 2025.12.31`. **Thêm 1 người:** Trương Mạnh Dũng (`VIE_army_truong_manh_dung`, `corps_commander`): Tư lệnh Quân đoàn 12 từ 12/2023 đến 24/04/2025, Tư lệnh Quân khu 1 từ 26/04/2025, Phó Tổng Tham mưu trưởng từ 22/06/2026. Tổng nhóm này 8 người.

### 2.4. Tổng kết số lượng

| | Trước (v2 bản đầu) | Bản này |
|---|---|---|
| Character mới cần tạo | 5-6 | **15** |
| Commander Giai đoạn 1 | 4-5 | 6 |
| Commander Giai đoạn 2 | 4-5 | 5-6 |

Cách đếm 15 ID mới: 5 từ báo cáo gốc (Dũng, Trà, Thanh, Nghiên, Tỵ; Mạnh đã bị bỏ) + 9 mở rộng cho hai giai đoạn (Phong, Được, Kỳ, Xuân Hùng, Tấn, Doãn Anh, Thái, Nam, Sản) + 1 cho nhóm submod (Trương Mạnh Dũng). Cộng 9 và 1 cho đúng 10 người mở rộng. Mục 4, bước 2 liệt kê đủ 15 ID.

## 3. Thí nghiệm bắt buộc trước khi code (khoảng 15 phút)

Làm trên bản sao save, bật `debug`, chơi VIE.

| # | Thí nghiệm | Kết quả | Hệ quả |
|---|---|---|---|
| **E1** | `effect retire_character = VIE_Phan_Van_Giang` rồi `effect recruit_character = VIE_Phan_Van_Giang`, mở panel advisor | Giang xuất hiện lại | **Nhánh R** |
| | | Không xuất hiện | **Nhánh N** |
| **E2** | Tạo character thử có `visible = { has_global_flag = TEST }`; kiểm tra bị ẩn, rồi `effect set_global_flag = TEST`; kiểm tra hiện ra | Hiện ra | Có thể dùng `visible` cho phần mở rộng (mục 6) |
| **E3** | Character thử không có khối `portraits` | `error.log` không báo lỗi | Bỏ qua ảnh cho 15 character mới (chỉ Trà, Thanh, Tỵ có ảnh) |
| **E4** | Character advisor thử thiếu khóa localisation `idea_token` | Hiển thị khóa trần hay tên | Xác nhận cần khóa chữ thường như trường hợp Trần Đại Thắng |

E3 giờ quan trọng hơn trước: 12 trong 15 character mới chưa có portrait.

## 4. Các bước code

### Bước 1: Nhánh git

Tạo `claude/land-roster-v2` từ `main`. Mỗi bước dưới đây một commit.

### Bước 2: Character mới (không phụ thuộc E1)

**File mới:** `common/characters/VIE_md_army_legacy.txt`, theo khuôn [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt). Có thể tách thành hai file (`..._phase1.txt`, `..._phase2.txt`) nếu muốn dễ quản lý.

**Commander (10 người).** Mọi dòng: `skill = 3`, tổng bốn chỉ số = 10 theo công thức.

| ID | Khối | attack / defense / planning / logistics | Trait (đề xuất, đã có trong repo hoặc upstream) |
|---|---|---|---|
| `VIE_army_le_van_dung` | `field_marshal` | 2 / 3 / 3 / 2 | `defensive_doctrine organizer` |
| `VIE_army_phung_quang_thanh` | `corps_commander` | 2 / 3 / 3 / 2 | `organizer infantry_leader` |
| `VIE_army_huynh_tien_phong` | `corps_commander` | 4 / 2 / 2 / 2 | `jungle_rat infantry_leader` |
| `VIE_army_phung_si_tan` | `corps_commander` | 2 / 3 / 3 / 2 | `hill_fighter infantry_leader` |
| `VIE_army_nguyen_doan_anh` | `corps_commander` | 3 / 2 / 3 / 2 | `organizer infantry_leader` |
| `VIE_army_nguyen_hong_thai` | `corps_commander` | 2 / 3 / 2 / 3 | `hill_fighter organizer` |
| `VIE_army_truong_manh_dung` | `corps_commander` | 3 / 2 / 3 / 2 | `offensive_doctrine organizer` |

Phong: Anh hùng lực lượng vũ trang, hồ sơ chiến đấu nên thiên về tấn công. Thanh và Thái thuộc Quân khu 1 (núi phía Bắc) nên một người có `hill_fighter`. Đây là điểm khởi đầu để cân bằng, không phải dữ kiện lịch sử.

**Advisor (tất cả có `ai_will_do = { factor = 1 }`, `ledger = army`):**

| ID | Slot | `idea_token` | Trait | cost |
|---|---|---|---|---|
| `VIE_army_le_van_dung` (khối advisor thêm vào cùng nhân vật) | `army_chief` | `vie_army_le_van_dung` | `army_chief_reform_2` | 150 |
| `VIE_army_phung_quang_thanh` (khối advisor thêm vào cùng nhân vật) | `army_chief` | `vie_army_phung_quang_thanh` | `army_chief_logistics_1` | 100 |
| `VIE_army_nguyen_khac_nghien` | `army_chief` | `vie_army_nguyen_khac_nghien` | `army_chief_drill_2` | 100 |
| `VIE_army_do_ba_ty` | `army_chief` | `vie_army_do_ba_ty` | `army_chief_logistics_2` | 100 |
| `VIE_army_pham_van_tra` | `high_command` | `vie_army_pham_van_tra` | `army_entrenchment_2` | 100 |
| `VIE_army_nguyen_van_duoc` | `high_command` | `vie_army_nguyen_van_duoc` | `army_entrenchment_1` | 100 |
| `VIE_army_hoang_ky` | `high_command` | `vie_army_hoang_ky` | `army_militia_2` | 100 |
| `VIE_army_pham_xuan_hung` | `high_command` | `vie_army_pham_xuan_hung` | `army_artillery_2` | 100 |
| `VIE_army_nguyen_phuong_nam` | `high_command` | `vie_army_nguyen_phuong_nam` | `army_regrouping_2` | 100 |
| `VIE_army_vu_hai_san` | `high_command` | `vie_army_vu_hai_san` | `army_infantry_3` | 125 |

Các trait trên đều đã có trong upstream VIE hoặc CHI. Mức `cost` theo mẫu upstream (cấp trait 3 thì 125, cấp 2 trở xuống thì 100, `reform_2` thì 150).

**Portrait:** Trà, Thanh, Tỵ dùng file có sẵn (`gfx/leaders/VIE/Portrait_*.dds` và bản `small`). 12 người còn lại chưa có ảnh: bỏ khối `portraits` nếu E3 đạt, nếu không thì dùng ảnh tạm. Kích thước ảnh theo MD: 156×210 (lớn), 38×51 (nhỏ).

**Skill của nhóm submod hiện có lệch công thức:** `VIE_army_le_xuan_thuan` tổng 11, `VIE_army_nguyen_thanh_pho` tổng 11, `VIE_army_le_xuan_the` (`field_marshal` skill 3) tổng 12, trong khi công thức cho 10. Sửa tùy ý, không chặn plan.

### Bước 3: Localisation (không phụ thuộc E1)

Sửa [VIE_army_commanders_l_english.yml](localisation/english/VIE_army_commanders_l_english.yml), theo khuôn của 7 dòng hiện có. Mỗi nhân vật có advisor cần **cả hai khóa** (ID và `idea_token` chữ thường):

```yaml
 VIE_army_le_van_dung:0 "Lê Văn Dũng"
 vie_army_le_van_dung:0 "Lê Văn Dũng"
 VIE_army_pham_van_tra:0 "Phạm Văn Trà"
 vie_army_pham_van_tra:0 "Phạm Văn Trà"
 VIE_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 vie_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 VIE_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 vie_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 VIE_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 vie_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 VIE_army_huynh_tien_phong:0 "Huỳnh Tiền Phong"
 VIE_army_nguyen_van_duoc:0 "Nguyễn Văn Được"
 vie_army_nguyen_van_duoc:0 "Nguyễn Văn Được"
 VIE_army_hoang_ky:0 "Hoàng Kỳ"
 vie_army_hoang_ky:0 "Hoàng Kỳ"
 VIE_army_pham_xuan_hung:0 "Phạm Xuân Hùng"
 vie_army_pham_xuan_hung:0 "Phạm Xuân Hùng"
 VIE_army_nguyen_phuong_nam:0 "Nguyễn Phương Nam"
 vie_army_nguyen_phuong_nam:0 "Nguyễn Phương Nam"
 VIE_army_vu_hai_san:0 "Vũ Hải Sản"
 vie_army_vu_hai_san:0 "Vũ Hải Sản"
 VIE_army_phung_si_tan:0 "Phùng Sĩ Tấn"
 VIE_army_nguyen_doan_anh:0 "Nguyễn Doãn Anh"
 VIE_army_nguyen_hong_thai:0 "Nguyễn Hồng Thái"
 VIE_army_truong_manh_dung:0 "Trương Mạnh Dũng"
```

Giữ BOM UTF-8. Lưu ý tên "Phạm Xuân Hùng" (`VIE_army_pham_xuan_hung`) khác "Phạm Văn Hùng" (`VIE_Pham_Van_Hung`, upstream): hai người khác nhau, dễ nhầm khi tìm kiếm. Sửa "Phi" thành "Phí" cho Phí Quốc Tuấn là việc tùy chọn, làm sau cùng.

### Bước 4: Tuyển Giai đoạn 1 (không phụ thuộc E1)

Sửa [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), trong scope `VIE = { ... }`:

```txt
if = {
	limit = {
		date < 2015.1.1
		NOT = { has_country_flag = VIE_army_phase1_recruited }
	}
	recruit_character = VIE_army_le_van_dung
	recruit_character = VIE_army_phung_quang_thanh
	recruit_character = VIE_army_huynh_tien_phong
	recruit_character = VIE_army_pham_van_tra
	recruit_character = VIE_army_nguyen_khac_nghien
	recruit_character = VIE_army_do_ba_ty
	recruit_character = VIE_army_nguyen_van_duoc
	recruit_character = VIE_army_hoang_ky
	recruit_character = VIE_army_pham_xuan_hung
	set_country_flag = VIE_army_phase1_recruited
}
```

Cờ bắt buộc vì `on_startup` chạy cả khi load save. Chỉ dùng thao tác một chiều nên bước này chắc chắn.

### Bước 5: Khối retire ở startup (phụ thuộc E1)

Khối `if date < 2015.1.1 { retire_character ... }` hiện có.

| | Nhánh R (E1 đạt) | Nhánh N (E1 không đạt) |
|---|---|---|
| Khối retire | Giữ, nhưng **xóa 4 dòng**: Lịch, Tuấn, Đơn, Việt | **Xóa cả khối.** Upstream giữ nguyên như history MD đã tuyển |
| Giai đoạn 2 upstream | Vắng đến 2015, tuyển lại ở event | Có mặt từ 2000 như MD thiết kế |
| Giai đoạn 2 mới (Tấn, Doãn Anh, Thái, Nam, Sản) | Tuyển ở event 2015 (không phụ thuộc E1: đây là ID chưa từng tuyển) | Như nhánh R |
| Tính chính xác lịch sử | Cao hơn | Giảm cho nhóm upstream: Giang, Cương, Chiến... có mặt sớm |

**Hải quân/Không quân** (Hậu, Thất, Khoa, Đạm, Nam, Phương): ở nhánh R vẫn nằm trong khối retire như hiện tại. Ở nhánh N chúng cũng có mặt từ đầu như MD. Cân nhắc kỹ trước khi xóa, vì ngoài phạm vi báo cáo này. (Lưu ý "Nam" ở đây là Phạm Hoài Nam, Hải quân, khác Nguyễn Phương Nam.)

### Bước 6: Event và scheduler

**Scheduler** [VIE_md_effects_p16.txt](common/scripted_effects/VIE_md_effects_p16.txt) (chạy hằng tháng từ `on_monthly`):

| Khối | Thay đổi |
|---|---|
| 2015 (`.2`) | Bỏ dòng `NOT = { has_character = VIE_Ngo_Xuan_Lich }` |
| 2016 (`.3`) | Xóa cả khối |
| 2021 (`.4`) | Bỏ dòng `NOT = { has_character = VIE_Nguyen_Tan_Cuong }`. Nhánh N: cũng xóa khối này nếu không còn ai để tuyển |
| 7+1 commander | `date > 2022.12.31` thành `date > 2025.12.31` |

**Event** [VIE_army_commanders.txt](events/VIE_army_commanders.txt), `vie_army_commanders.2`:

*Nhánh R:*

```txt
immediate = {
	# Giai đoạn 2, character mới (không phụ thuộc E1)
	recruit_character = VIE_army_phung_si_tan
	recruit_character = VIE_army_nguyen_doan_anh
	recruit_character = VIE_army_nguyen_hong_thai
	recruit_character = VIE_army_nguyen_phuong_nam
	recruit_character = VIE_army_vu_hai_san
	# Giai đoạn 2, upstream (chỉ nhánh R)
	recruit_character = VIE_Be_Xuan_Truong
	recruit_character = VIE_Vo_Minh_Luong
	recruit_character = VIE_Phan_Van_Giang
	recruit_character = VIE_Nguyen_Trong_Nghia
	recruit_character = VIE_Hoang_Xuan_Chien
	recruit_character = VIE_Nguyen_Tan_Cuong
	recruit_character = VIE_Le_Xuan_Duy
	recruit_character = VIE_Pham_Van_Hung
	recruit_character = VIE_Hyunh_Chien_Thang   # tùy chọn
	# Giữ nguyên ngày hiện có, ngoài phạm vi Lục quân
	recruit_character = VIE_Nguyen_Quang_Dam
	recruit_character = VIE_Pham_Kim_Hau
	recruit_character = VIE_Tran_Viet_Khoa
	recruit_character = VIE_Dinh_Gia_That
	# Rút nhóm Giai đoạn 1 hết vai trò
	retire_character = VIE_army_le_van_dung
	retire_character = VIE_army_pham_van_tra
	retire_character = VIE_army_phung_quang_thanh
	retire_character = VIE_army_nguyen_khac_nghien
	retire_character = VIE_army_do_ba_ty
	retire_character = VIE_army_huynh_tien_phong
	retire_character = VIE_army_nguyen_van_duoc
	retire_character = VIE_army_hoang_ky
	retire_character = VIE_army_pham_xuan_hung
	retire_character = VIE_Phi_Quoc_Tuan
	set_country_flag = VIE_md_roster_recruited_2015
	clr_country_flag = VIE_md_roster_event_pending
}
```

*Nhánh N:* bỏ khối "Giai đoạn 2, upstream" và khối "Giữ nguyên ngày hiện có"; giữ 5 dòng tuyển character mới và toàn bộ `retire_character`.

Cả hai nhánh: xóa event `.3` (kèm khóa `vie_army_commanders.3.a`); `.4` chỉ còn `VIE_Pham_Hoai_Nam` và `VIE_Tran_Quang_Phuong` ở nhánh R (nhánh N: xóa luôn); `.1` thêm `recruit_character = VIE_army_truong_manh_dung`.

## 5. Kiểm tra

**Kiểm tra tĩnh** (xem [tools/TESTING.md](tools/TESTING.md), [tools/audit/README.md](tools/audit/README.md)):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py
python3 tools/audit/ev.py
```

**Trong game** (chưa ai từng chạy): đọc `error.log` (tìm `VIE`, `character`, `portrait`), rồi đối chiếu số mong đợi.

| Thời điểm | Commander Lục quân | Advisor |
|---|---|---|
| 01/2000 | Vịnh, Dũng, Thanh, Phong, Tuấn, Lịch = **6** | Dũng, Thanh, Nghiên, Tỵ (army_chief); Trà, Được, Kỳ, Xuân Hùng, Đơn, Việt (high_command) |
| Sau 01/2015, nhánh R | Vịnh, Lịch, Tấn, Doãn Anh, Thái (+ Thắng) = **5-6** | Đơn, Việt, Nam, Sản, Bế, Lương, Giang, Nghĩa, Chiến, Cương, Duy, Hùng |
| Sau 01/2015, nhánh N | Như nhánh R | Như nhánh R (nhóm upstream đã có từ đầu) |
| Sau 01/2026 | Thêm 8 commander submod | |

Không còn Dũng, Thanh, Phong, Tuấn, Trà, Nghiên, Tỵ, Được, Kỳ, Xuân Hùng sau 2015.

Test console: `tag VIE`, `event vie_army_commanders.2` để kiểm tra đổi roster ngay. Load save giữa giai đoạn (2007, 2016) để chắc chắn không tuyển lặp và roster đúng giai đoạn.

## 6. Mở rộng tùy chọn (chỉ khi E2 đạt)

Gắn `visible` vào character của mình để chia nhỏ thời điểm mà không cần event:

```txt
visible = { date > 2001.5.1 }
```

Có thể áp cho chuỗi Tổng Tham mưu trưởng (Thanh từ 05/2001, Nghiên từ 08/2006, Tỵ từ 11/2010) và nhóm quân khu (Tấn từ 12/2016, Doãn Anh từ 11/2018, Thái từ 10/2019). Cần thí nghiệm thêm: khi `visible` chuyển từ đúng sang sai lúc advisor đã được thuê, người đó có bị gỡ khỏi slot không. Chưa kiểm chứng nên **không nằm trong phạm vi v2**.

## 7. Rủi ro

| Rủi ro | Xử lý |
|---|---|
| Nhánh N làm mất chính xác lịch sử ở Giai đoạn 2 | Chấp nhận như MD, ghi rõ vào changelog |
| 12 character không có portrait gây lỗi | E3; dùng ảnh tạm |
| Tuyển lặp khi load save | Cờ `VIE_army_phase1_recruited` |
| Save cũ đã chạy event 2015 theo bản cũ | Không retire nhóm cũ cho save đó; ghi changelog |
| Thanh, Tỵ, Xuân Hùng bị rút sớm 1-2 năm | Chấp nhận |
| Nhóm mới Tấn, Doãn Anh, Thái xuất hiện sớm 1-4 năm so với chức vụ | Chấp nhận theo yêu cầu hai giai đoạn |
| Tên trùng gần: Phạm Xuân Hùng / Phạm Văn Hùng, Nguyễn Phương Nam / Phạm Hoài Nam | Dùng ID đầy đủ khi tìm kiếm, ghi chú trong file character |
| Dữ liệu 4 người mở rộng chỉ có một nguồn (Được, Kỳ, Xuân Hùng, Thái) | Nhãn B trong roster report; xác minh thêm nếu có điều kiện |

## 8. Ngoài phạm vi

- Hải quân và Không quân (chỉ giữ nguyên).
- Nguyễn Quang Đạm.
- Làm ảnh portrait mới cho 12 người.
- Cân bằng chi tiết ngoài công thức điểm kỹ năng.
- Commander cho các quân khu khác ngoài những người ở mục 2.

## 9. Việc dọn tài liệu

| File | Sửa |
|---|---|
| [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md) | Đã thêm mục 10 (10 tướng mở rộng); đồng bộ vai trò Dũng, Thanh, Nghiên, Tỵ; bỏ Mạnh khỏi mặc định |
| [VIE_generals_and_commander_system_research_report.md](VIE_generals_and_commander_system_research_report.md) | Bỏ "tuyển khi khởi động", "8 portrait", "chưa có portrait riêng" |
| [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) | Bỏ mốc 2005 và đoạn "Chí Vịnh căn cứ mạnh ở 2000" |
| [tools/TESTING.md](tools/TESTING.md) | Thêm mục kiểm tra roster như mục 5 |

## 10. Nguồn

- [MD New General Guidelines](https://millenniumdawn.github.io/Millennium-Dawn/dev-resources/new-general-guidelines/) (công thức số tướng và điểm kỹ năng; tôi chỉ đọc qua bản tóm tắt tự động, nên đối chiếu lại với trang gốc)
- [HOI4 Character modding](https://hoi4.paradoxwikis.com/Character_modding)
- [MD VIE.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt) và [CHI.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/CHI.txt)
- [tools/audit/md_ref/CHI.txt](tools/audit/md_ref/CHI.txt), [VIE_2000_nsb.txt](tools/audit/md_ref/VIE_2000_nsb.txt) (34 sư đoàn)
- Nguồn từng người trong mục 10 của [roster report](VIE_land_forces_roster_rebuild.md).

---

## Phụ lục I: Plan triển khai v1 (Lịch sử tham khảo)

# Plan triển khai: roster tướng lĩnh Lục quân VIE theo 2 giai đoạn

> **Đã được thay bằng [VIE_land_forces_implementation_plan_v2.md](VIE_land_forces_implementation_plan_v2.md).** v1 giả định vòng "retire rồi tuyển lại" chạy được và để 8 commander ở bookmark 2000; v2 kiểm tra giả định đó trước và theo công thức số tướng của MD. Giữ file này chỉ để tham khảo.

**Ngày:** 01/10/2026
**Cơ sở:** [VIE_land_forces_roster_rebuild.md](VIE_land_forces_roster_rebuild.md) (dữ liệu và lý do; plan này chỉ nói *làm gì, ở file nào, theo thứ tự nào*).
**Mục tiêu:** bookmark 2000 có roster Giai đoạn 1; ngày 01/01/2015 đổi sang roster Giai đoạn 2; 7 commander Quân đoàn 12/34 tuyển riêng từ 2026.

## 0. Quyết định cần chốt trước khi code

| # | Quyết định | Mặc định trong plan |
|---|---|---|
| D1 | 7 commander Quân đoàn 12/34/QK7 | Phương án A: giữ event riêng, dời ngưỡng sang `date > 2025.12.31` |
| D2 | Lê Mạnh (tùy chọn) và Huỳnh Chiến Thắng (tùy chọn) | Tạo Mạnh (Giai đoạn 1), tuyển Thắng (Giai đoạn 2) |
| D3 | Hải quân/Không quân (Hậu, Thất, Khoa, Đạm, Nam, Phương) | **Không đổi ngày hiện có** (mục 3.4) |
| D4 | Vai trò của Thanh, Nghiên, Tỵ | `corps_commander`, không phải `field_marshal`, để bookmark 2000 không có 5 field marshal cùng lúc. Chỉ Dũng và Vịnh là `field_marshal` |
| D5 | Character mới thiếu portrait (Dũng, Nghiên, Mạnh) | Bỏ khối `portraits` ban đầu, test `error.log`, bổ sung ảnh sau |

## 1. Thứ tự làm

1. Tạo nhánh `claude/land-roster-2-phase` từ `main` (repo đang sạch).
2. Bước 2: character mới.
3. Bước 3: localisation.
4. Bước 4: startup.
5. Bước 5: event và scheduler.
6. Bước 6: kiểm tra tĩnh, rồi trong game.
7. Bước 7: dọn tài liệu cũ.

Mỗi bước commit riêng để rollback từng phần. Bước 4 và 5 phải đi cùng nhau trước khi test, vì làm một mình sẽ cho roster lệch.

## 2. Bước 2: Character mới

**File mới:** `common/characters/VIE_md_army_legacy.txt`. Giữ prefix `VIE_army_` để không đụng ID upstream. Copy đúng khuôn của [VIE_md_army_expansion.txt](common/characters/VIE_md_army_expansion.txt).

| ID | Tên hiển thị | Vai trò | Ghi chú |
|---|---|---|---|
| `VIE_army_le_van_dung` | Lê Văn Dũng | `field_marshal` | Chưa có portrait |
| `VIE_army_pham_van_tra` | Phạm Văn Trà | `advisor` slot `high_command`, ledger `army` | Có `Portrait_Pham_Van_Tra.dds` |
| `VIE_army_phung_quang_thanh` | Phùng Quang Thanh | `corps_commander` | Có `Portrait_Phung_Quang_Thanh.dds` |
| `VIE_army_nguyen_khac_nghien` | Nguyễn Khắc Nghiên | `corps_commander` | Chưa có portrait |
| `VIE_army_do_ba_ty` | Đỗ Bá Tỵ | `corps_commander` | Có `Portrait_Do_Ba_Ty.dds` |
| `VIE_army_le_manh` | Lê Mạnh | `corps_commander` | Chưa có portrait |

**Skill/trait đề xuất** (số là điểm khởi đầu để cân bằng, không phải dữ kiện lịch sử). Chỉ dùng trait đã có trong repo hoặc upstream:

| ID | Trait | skill / attack / defense / planning / logistics |
|---|---|---|
| Dũng | `defensive_doctrine organizer` | 3 / 2 / 3 / 3 / 3 |
| Thanh | `organizer infantry_leader` | 3 / 2 / 3 / 3 / 2 |
| Nghiên | `offensive_doctrine organizer` | 3 / 3 / 2 / 3 / 2 |
| Tỵ | `infantry_leader organizer` | 3 / 2 / 3 / 3 / 2 |
| Mạnh | `defensive_doctrine infantry_leader` | 2 / 2 / 3 / 2 / 2 |
| Trà (advisor) | `army_entrenchment_2`, `cost = 100`, `ai_will_do = { factor = 1 }` | không áp dụng |

**Lưu ý schema:** advisor cần `idea_token = vie_army_pham_van_tra` (chữ thường). Đường dẫn portrait: `gfx/leaders/VIE/Portrait_X.dds` và `gfx/leaders/VIE/small/Portrait_X_small.dds` (ba người có ảnh đều đã có bản `small`).

**Việc cần xác nhận khi test:** chưa chắc HOI4 chấp nhận character không có `portraits`. Nếu `error.log` báo lỗi, dùng tạm một portrait có sẵn hoặc làm ảnh mới.

## 3. Bước 3: Localisation

**Sửa:** [VIE_army_commanders_l_english.yml](localisation/english/VIE_army_commanders_l_english.yml). File này giữ BOM UTF-8, dùng cú pháp `key:0 "text"` có một dấu cách đầu dòng.

Thêm các khóa, theo đúng khuôn của 7 dòng hiện có (khóa trùng ID):

```yaml
 VIE_army_le_van_dung:0 "Lê Văn Dũng"
 VIE_army_pham_van_tra:0 "Phạm Văn Trà"
 vie_army_pham_van_tra:0 "Phạm Văn Trà"
 VIE_army_phung_quang_thanh:0 "Phùng Quang Thanh"
 VIE_army_nguyen_khac_nghien:0 "Nguyễn Khắc Nghiên"
 VIE_army_do_ba_ty:0 "Đỗ Bá Tỵ"
 VIE_army_le_manh:0 "Lê Mạnh"
```

**Phí Quốc Tuấn** (upstream ghi "Phi"): làm sau cùng và là việc tùy chọn. Cần thử đặt khóa `VIE_Phi_Quoc_Tuan` trong `localisation/english/replace/` và xem game có lấy bản đó không. Không chắc cách MD lấy tên character, nên đừng làm việc này trước khi mọi thứ khác chạy.

## 4. Bước 4: Startup

**Sửa:** [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), khối `if date < 2015.1.1` (dòng 9-29).

1. **Xóa 4 dòng retire** của Giai đoạn 1 upstream: `VIE_Ngo_Xuan_Lich`, `VIE_Phi_Quoc_Tuan`, `VIE_Tran_Don`, `VIE_Vo_Trong_Viet`.
2. **Giữ nguyên** các dòng retire còn lại, kể cả Hải quân/Không quân (D3).
3. **Thêm khối tuyển Giai đoạn 1 (lần đầu)** trong cùng scope `VIE = { ... }`:

```txt
if = {
	limit = {
		date < 2015.1.1
		NOT = { has_country_flag = VIE_army_phase1_recruited }
	}
	recruit_character = VIE_army_le_van_dung
	recruit_character = VIE_army_pham_van_tra
	recruit_character = VIE_army_phung_quang_thanh
	recruit_character = VIE_army_nguyen_khac_nghien
	recruit_character = VIE_army_do_ba_ty
	recruit_character = VIE_army_le_manh
	set_country_flag = VIE_army_phase1_recruited
}
```

**Vì sao cần cờ:** `on_startup` chạy cả khi load save, không chỉ khi bắt đầu game. Không có cờ thì mỗi lần load save 2005 sẽ tuyển lại. Điều kiện `date < 2015.1.1` giữ cho save sau 2015 không tuyển lại nhóm đã bị rút.

## 5. Bước 5: Event và scheduler

### 5.1. Scheduler

**Sửa:** [VIE_md_effects_p16.txt](common/scripted_effects/VIE_md_effects_p16.txt). Hàm này được gọi hằng tháng từ `on_monthly`, nên mốc ngày sẽ bắn trong tháng đầu tiên sau mốc.

| Khối | Thay đổi |
|---|---|
| 2015 (`vie_army_commanders.2`) | Bỏ dòng `NOT = { has_character = VIE_Ngo_Xuan_Lich }`. Cờ `VIE_md_roster_recruited_2015` đã đủ |
| 2016 (`vie_army_commanders.3`) | **Xóa cả khối** (Giang, Trường chuyển vào event .2) |
| 2021 (`vie_army_commanders.4`) | Bỏ dòng `NOT = { has_character = VIE_Nguyen_Tan_Cuong }`. Giữ ngưỡng `date > 2020.12.31` và cờ `VIE_md_roster_recruited_2021` |
| 7 commander submod | Đổi `date > 2022.12.31` thành `date > 2025.12.31` |

### 5.2. Event

**Sửa:** [VIE_army_commanders.txt](events/VIE_army_commanders.txt).

**`vie_army_commanders.2` (đổi roster 2015).** Thay danh sách `immediate`:

```txt
immediate = {
	# Giai đoạn 2, Lục quân
	recruit_character = VIE_Be_Xuan_Truong
	recruit_character = VIE_Vo_Minh_Luong
	recruit_character = VIE_Phan_Van_Giang
	recruit_character = VIE_Nguyen_Trong_Nghia
	recruit_character = VIE_Hoang_Xuan_Chien
	recruit_character = VIE_Nguyen_Tan_Cuong
	recruit_character = VIE_Le_Xuan_Duy
	recruit_character = VIE_Pham_Van_Hung
	recruit_character = VIE_Hyunh_Chien_Thang   # tùy chọn (D2)

	# Giữ nguyên, ngoài phạm vi Lục quân (D3)
	recruit_character = VIE_Nguyen_Quang_Dam
	recruit_character = VIE_Pham_Kim_Hau
	recruit_character = VIE_Tran_Viet_Khoa
	recruit_character = VIE_Dinh_Gia_That

	# Rút nhóm Giai đoạn 1 đã hết vai trò
	retire_character = VIE_army_le_van_dung
	retire_character = VIE_army_pham_van_tra
	retire_character = VIE_army_phung_quang_thanh
	retire_character = VIE_army_nguyen_khac_nghien
	retire_character = VIE_army_do_ba_ty
	retire_character = VIE_army_le_manh
	retire_character = VIE_Phi_Quoc_Tuan

	set_country_flag = VIE_md_roster_recruited_2015
	clr_country_flag = VIE_md_roster_event_pending
}
```

Ở lại qua 2015, không rút: Nguyễn Chí Vịnh, Trần Đơn, Ngô Xuân Lịch, Võ Trọng Việt.

**`vie_army_commanders.3`:** xóa cả event, kèm khóa `vie_army_commanders.3.a` trong localisation.

**`vie_army_commanders.4` (2021):** chỉ còn hai người ngoài phạm vi: `VIE_Pham_Hoai_Nam` và `VIE_Tran_Quang_Phuong`. Bỏ Cương, Nghĩa, Võ Minh Lương, Hoàng Xuân Chiến (đã chuyển sang event .2).

**`vie_army_commanders.1`:** không đổi nội dung.

## 6. Bước 6: Kiểm tra

### 6.1. Kiểm tra tĩnh

Chạy theo [tools/TESTING.md](tools/TESTING.md) và [tools/audit/README.md](tools/audit/README.md):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py     # tham chiếu chéo
python3 tools/audit/ev.py       # namespace, id trùng, loc, orphan (sẽ bắt event .3 bị xóa sót loc)
```

`tools/check_static.py` hardcode đường dẫn Windows tới Millennium Dawn nên chưa chạy được nếu chưa sửa hằng số.

### 6.2. Trong game (chưa ai chạy)

1. Thêm mod sau Millennium Dawn, mở game, đọc `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`, tìm `VIE`, `vie_`, `character`, `portrait`.
2. Bắt đầu bookmark 2000, chơi VIE.

| Thời điểm | Lục quân có mặt (số lượng mong đợi) |
|---|---|
| 01/2000 | Vịnh, Dũng, Trà, Thanh, Nghiên, Tỵ, Mạnh, Phí Quốc Tuấn, Đơn, Lịch, Việt = **11** |
| Sau 01/2015 (tháng đầu) | Vịnh, Đơn, Lịch, Việt + Bế, Lương, Giang, Nghĩa, Chiến, Cương, Duy, Hùng, (Thắng) = **12-13**. Dũng, Trà, Thanh, Nghiên, Tỵ, Mạnh, Tuấn không còn |
| Sau 01/2021 | Như trên, thêm Phạm Hoài Nam và Trần Quang Phương (ngoài Lục quân) |
| Sau 01/2026 | Thêm 7 commander submod |

3. **Test nhanh bằng console** (dùng bản sao save, bật `debug`): `tag VIE`, `event vie_army_commanders.2` để kiểm tra đổi roster ngay mà không cần chờ đến 2015, và `event vie_army_commanders.1` cho nhóm 7 người.
4. **Load save giữa giai đoạn** (ví dụ 2007): xác nhận không có người bị tuyển lặp và roster vẫn là Giai đoạn 1.
5. **Load save sau mốc 2015:** xác nhận roster Giai đoạn 2 vẫn còn, Giai đoạn 1 không quay lại.
6. **Câu hỏi còn mở cần chốt bằng thử nghiệm:** `retire_character` có thực sự gỡ người khỏi recruit panel không, và có tuyển lại được bằng `recruit_character` ở 2015 không (hiện startup đang dựa vào điều này cho 14 người, nhưng chưa ai xác nhận trong game).

## 7. Bước 7: Dọn tài liệu

| File | Sửa |
|---|---|
| [VIE_generals_and_commander_system_research_report.md](VIE_generals_and_commander_system_research_report.md) | Bỏ "tuyển khi khởi động"; sửa "8 portrait" thành 14 file `.dds`; bỏ "chưa có portrait riêng" cho 7 commander |
| [VIE_commander_timeline_research_report.md](VIE_commander_timeline_research_report.md) | Bỏ mốc 2005 và đoạn "Chí Vịnh căn cứ mạnh ở 2000" |
| `VIE_land_forces_2000_2005_2010_research_report.md` | Xóa hoặc thêm dòng đầu "đã thay bằng `VIE_land_forces_roster_rebuild.md`" (file chưa commit nên xóa là mất hẳn) |
| [tools/TESTING.md](tools/TESTING.md) | Thêm mục kiểm tra roster như 6.2 |

## 8. Rủi ro và cách xử lý

| Rủi ro | Xử lý |
|---|---|
| Character không có portrait gây lỗi | Dùng portrait tạm; làm ảnh sau |
| `on_startup` tuyển lặp khi load save | Cờ `VIE_army_phase1_recruited` (mục 4) |
| Save cũ đã chạy event 2015 theo bản cũ | Phase 1 không bị rút cho save đó; chấp nhận, cần ghi vào changelog |
| Bắt đầu bookmark sau 2015 (nếu MD có) | Event .2 vẫn chạy sau 1 tháng; thử trước khi hứa là hỗ trợ |
| Thanh và Tỵ bị rút sớm ~1 năm | Chấp nhận, đã ghi trong báo cáo |
| 11 người xuất hiện cùng lúc ở 2000, lệch 9-12 năm | Chấp nhận theo yêu cầu 2 giai đoạn |

## 9. Ngoài phạm vi (không đụng trong đợt này)

- Hải quân: Phạm Hoài Nam, Phạm Kim Hậu, Đinh Gia Thất.
- Không quân: Trần Quang Phương, Trần Việt Khoa.
- Nguyễn Quang Đạm.
- Cân bằng skill/trait chi tiết.
- Tạo portrait mới cho Dũng, Nghiên, Mạnh.
- Thêm commander cho các quân khu khác ngoài chuỗi QK7.

---

## Phụ lục II: Báo cáo nghiên cứu cohort 2000 / 2005 / 2010 (Lịch sử tham khảo)

# Báo cáo nghiên cứu Lục quân VIE: cohort 2000 / 2005 / 2010

> **Đã được thay bằng `VIE_land_forces_roster_rebuild.md`** (dữ liệu) và `VIE_land_forces_implementation_plan_v2.md` (code). Khung 12/6/7 trong file này có cohort trùng người và nhiều chức vụ sai niên đại; không dùng để code. Giữ lại để đối chiếu.

**Ngày:** 01/10/2026  
**Phạm vi:** chỉ Lục quân QĐND Việt Nam; không gồm Hải quân, Không quân thuần túy, advisor chính trị thuần túy, hoặc 7 commander Quân đoàn 12/34 của submod đã nghiên cứu riêng.  
**Mục tiêu thiết kế:** tìm ứng viên cho ba cohort: 12 người đầu game 2000, thêm 6 người năm 2005, thêm 7 người năm 2010.

## 1. Kết luận ngắn

Yêu cầu 12/6/7 có thể dùng như **khung gameplay**, nhưng hiện chưa thể coi là ba danh sách lịch sử đã được chứng minh đầy đủ. Nguồn công khai xác nhận chắc chuỗi Tổng Tham mưu trưởng, Bộ trưởng Quốc phòng và một số tư lệnh quân khu; không có hồ sơ công khai thống nhất cho mọi sĩ quan cấp quân đoàn/sư đoàn vào đúng các ngày 01/01/2000, 01/01/2005 và 01/01/2010.

Vì vậy báo cáo dùng ba nhãn:

- **A - xác minh cao:** chức vụ hoặc chuỗi chỉ huy có mốc công khai rõ.
- **B - ứng viên hợp lý:** là tướng cấp cao/lục quân và có thể đã hoạt động trong giai đoạn, nhưng chưa có ngày chức vụ đủ chắc.
- **C - không đủ dữ kiện:** không đưa vào cohort lịch sử nếu không có nguồn bổ sung.

Không nên code tuyển dụng từ báo cáo này cho tới khi các ứng viên nhãn B được xác minh riêng.

## 2. Mốc lịch sử nền

Nguồn tổng hợp về Tổng Tham mưu trưởng ghi nhận:

| Giai đoạn | Nhân vật | Ý nghĩa cho cohort |
|---|---|---|
| 22/05/1998 - 05/2001 | Lê Văn Dũng | Có thể xuất hiện đầu game 2000 |
| 05/2001 - 31/08/2006 | Phùng Quang Thanh | Xuất hiện từ 2001, không phải đầu ngày 01/01/2000 nếu mô phỏng chặt |
| 31/08/2006 - 13/11/2010 | Nguyễn Khắc Nghiên | Xuất hiện từ cuối 2006 |
| 13/11/2010 - 17/05/2016 | Đỗ Bá Tỵ | Xuất hiện từ cuối 2010 |
| 17/05/2016 - 03/06/2021 | Phan Văn Giang | Xuất hiện từ 2016 |
| 03/06/2021 - nay | Nguyễn Tân Cương | Xuất hiện từ 2021 |

Phạm Văn Trà là Bộ trưởng Quốc phòng trong giai đoạn đầu bookmark và là nhân vật lục quân cấp cao phù hợp với cohort 2000, dù chức Tổng Tham mưu trưởng của ông kết thúc trước 2000.

## 3. Danh sách 12 ứng viên đầu game 2000

Đây là danh sách gameplay đề xuất, không phải khẳng định rằng cả 12 người cùng giữ chức vụ tương ứng vào ngày 01/01/2000.

| # | Nhân vật | Vai trò đại diện | Mức | Nhận xét |
|---:|---|---|---|---|
| 1 | Lê Văn Dũng | Tổng Tham mưu trưởng | A | Đang giữ chức từ 1998 |
| 2 | Phạm Văn Trà | Bộ trưởng / tướng lục quân | A | Nhân vật cấp cao đương nhiệm đầu giai đoạn |
| 3 | Nguyễn Chí Vịnh | Tình báo quốc phòng / chỉ huy chiến lược | B | Có thể đại diện lớp tướng chiến lược trước 2010; cần hồ sơ chức vụ 2000 |
| 4 | Ngô Xuân Lịch | Chính trị-quân đội / lục quân | B | Sĩ quan cấp cao, nhưng cần xác minh chức vụ đúng năm 2000 |
| 5 | Phùng Quang Thanh | Chỉ huy chiến lược | B | Có mặt từ 05/2001; nếu giữ tính ngày tháng chặt nên chuyển sang cohort 2005 |
| 6 | Nguyễn Khắc Nghiên | Chỉ huy chiến lược | B | Có mặt từ 2006; không nên coi là tướng active 2000 nếu mô phỏng theo chức vụ |
| 7 | Đỗ Bá Tỵ | Tham mưu chiến lược | B | Chức Tổng Tham mưu trưởng bắt đầu cuối 2010; cần hồ sơ chức vụ trước đó |
| 8 | Phi Quốc Tuấn | Corps commander | B | MD có role lục quân, nhưng repo chưa có timeline chức vụ |
| 9 | Lê Mạnh | Quân khu / lục quân | B | Report ghi tư lệnh Quân khu 7 giai đoạn 2004-2009, nên không chắc cho 2000 |
| 10 | Trần Đơn | Quân khu / lục quân | B | Report ghi rõ vai trò Quân khu 7 2011-2015, không nên gắn chắc vào 2000 |
| 11 | Võ Trọng Việt | Biên phòng / lục quân | B | Có thể là lớp sĩ quan cao cấp trước 2010; cần ngày chức vụ cụ thể |
| 12 | Phạm Văn Hùng | High command lục quân | C | Chưa có hồ sơ thời điểm đủ để xác nhận cohort 2000 |

**Kết luận cohort 2000:** chỉ các mục 1-2 là xác minh mạnh theo mốc chức vụ. Các mục còn lại là pool ứng viên để đạt quy mô gameplay, không được mô tả là “12 tướng chắc chắn đang giữ chức năm 2000”.

## 4. Sáu ứng viên bổ sung năm 2005

Đây là cohort bổ sung dùng khi người chơi tiếp tục qua giai đoạn giữa thập niên 2000. Mốc 2005 phù hợp với các sĩ quan đã trưởng thành trong hệ thống chỉ huy nhưng chưa có ngày bổ nhiệm công khai trong repo.

| # | Nhân vật | Vai trò đại diện | Mức | Lý do đưa vào 2005 |
|---:|---|---|---|---|
| 1 | Phùng Quang Thanh | Tổng Tham mưu trưởng | A | Bắt đầu 05/2001, chắc chắn active năm 2005 |
| 2 | Nguyễn Khắc Nghiên | Chỉ huy chiến lược | A/B | Được bổ nhiệm Tổng Tham mưu trưởng 08/2006, đã là sĩ quan cấp cao trước đó |
| 3 | Lê Mạnh | Quân khu 7 | B | Report ghi vai trò chỉ huy Quân khu 7 giai đoạn 2004-2009 |
| 4 | Ngô Xuân Lịch | Chính trị-quân đội | B | Phù hợp lớp cán bộ chính trị quân đội giữa thập niên 2000 |
| 5 | Phi Quốc Tuấn | Corps commander | B | Có role corps commander trong MD; cần nguồn chức vụ trước khi gọi là historical |
| 6 | Võ Trọng Việt | Biên phòng / lục quân | B | Có thể đại diện lớp chỉ huy biên phòng-lục quân trước 2010; cần xác minh ngày |

**Lưu ý:** nếu đã đưa một trong các nhân vật này vào cohort 2000, không tuyển lại năm 2005. Cohort 2005 là danh sách bổ sung, không phải danh sách thay thế.

## 5. Bảy ứng viên bổ sung năm 2010

Mốc 2010 nên được hiểu là “lớp sĩ quan bước vào vai trò chỉ huy cấp cao từ 2010 trở đi”, không phải tất cả đã là tư lệnh đúng ngày 01/01/2010.

| # | Nhân vật | Vai trò đại diện | Mức | Mốc lịch sử liên quan |
|---:|---|---|---|---|
| 1 | Đỗ Bá Tỵ | Tổng Tham mưu trưởng | A | Bắt đầu 13/11/2010 |
| 2 | Trần Đơn | Quân khu 7 / high command | A/B | Report ghi Tư lệnh Quân khu 7 2011-2015 |
| 3 | Võ Minh Lương | Quân khu / high command | B | Report ghi Tham mưu trưởng Quân khu 7 2011-2015, sau đó là Thứ trưởng |
| 4 | Nguyễn Trọng Nghĩa | Chính trị-quân đội | B | Phù hợp nhóm lãnh đạo chính trị quân đội giai đoạn sau 2010 |
| 5 | Hoàng Xuân Chiến | Army chief / quản trị quốc phòng | B | Phù hợp lớp lãnh đạo quốc phòng hiện đại, cần xác minh ngày đầu |
| 6 | Trần Quang Phương | Chính trị-quân đội / phòng không | C | MD đặt ở air chief; chỉ đưa vào báo cáo lục quân nếu xác minh vai trò lục quân |
| 7 | Trần Việt Khoa | Chỉ huy quân chủng/lục quân | C | Cần nguồn bổ nhiệm rõ trước khi xếp vào cohort 2010 |

**Độ chắc cohort 2010:** Đỗ Bá Tỵ, Trần Đơn và Võ Minh Lương có cơ sở tốt nhất. Bốn người còn lại là ứng viên thiết kế, chưa phải kết luận lịch sử.

## 6. Những người không đưa vào ba cohort Lục quân này

Các nhân vật sau không nên dùng để lấp danh sách Lục quân 2000/2005/2010 nếu không có nguồn mới:

- Phạm Hoài Nam, Phạm Kim Hậu, Đinh Gia Thật: nhóm Hải quân.
- Nguyễn Quang Đạm: upstream dùng `army_chief`, nhưng hồ sơ thiết kế trong repo xếp vào nhóm Hải quân; cần xác minh trước.
- VIE_Tran_Quang_Phuong, VIE_Tran_Viet_Khoa: upstream dùng `air_chief`, không tự chuyển thành Lục quân.
- VIE_Vo_Minh_Luong: upstream ledger `air`, cần tách khỏi danh sách Lục quân thuần túy.
- Lê Xuân Thuân, Đào Tuấn Anh, Trần Đại Thắng, Nguyễn Thành Phố, Trần Công Đức, Nguyễn Bá Lực, Lê Xuân Thế: nhóm commander hiện đại 2023-2025 của submod, không thuộc cohort 2010.

## 7. Kết luận về con số 12 / 6 / 7

Có thể dùng 12/6/7 như **khung roster gameplay**, nhưng chưa thể gọi đó là ba cohort lịch sử đã xác minh. Danh sách hiện tại có:

- **12 ứng viên đầu game:** 2 mức A, 9 mức B, 1 mức C.
- **6 ứng viên năm 2005:** 1 mức A, 5 mức B.
- **7 ứng viên năm 2010:** 1 mức A, 2 mức A/B, 2 mức B, 2 mức C.

Muốn đạt chất lượng lịch sử cao hơn, bước nghiên cứu tiếp theo phải là truy từng hồ sơ bổ nhiệm của các nhãn B/C qua QĐND, Bộ Quốc phòng, TTXVN hoặc lịch sử đơn vị. Không nên code tuyển dụng tự động từ bảng này cho đến khi các nhãn C được xác nhận.

## 8. Nguồn tham khảo

- [Chief of the General Staff of Vietnam](https://en.wikipedia.org/wiki/Chief_of_the_General_Staff_(Vietnam))
- [Minister of Defence of Vietnam](https://en.wikipedia.org/wiki/Minister_of_Defence_(Vietnam))
- [Báo cáo nghiên cứu tướng lĩnh trong repo](VIE_generals_and_commander_system_research_report.md)
- [Báo cáo Lục quân VIE](Báo cáo%20Lục%20quân%20VIE%20—%20Trục%201,%202,%203.md)
- [MD history reference VIE](tools/audit/md_ref/VIE_country.txt)
- [MD character roster reference](VIE_md_character_schema_and_roster.md)