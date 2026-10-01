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
