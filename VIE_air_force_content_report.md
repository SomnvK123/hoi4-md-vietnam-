# BÁO CÁO NỘI DUNG NHÁNH KHÔNG QUÂN (QUÂN CHỦNG PHÒNG KHÔNG – KHÔNG QUÂN) · VIE · MILLENNIUM DAWN

> Bản 1.4 · 2026-10-02 · **Chỉ có nội dung thiết kế, chưa có dòng code nào.**
> Bản 1.4 viết lại Trục 2 (Phần 6, chi tiết `VIE_air_truc2_review_and_plan.md`). Bản 1.3 sửa Trục 1 (Phần 5) và các chỗ liên quan (4.2, 4.3, 12.1) sau khi đối chiếu với MD v2.0.0 cài trên máy và repo; chi tiết lỗi, ánh xạ trang bị và plan code ở `VIE_air_truc1_review_and_plan.md`. Các Phần 7–11 chưa đối chiếu lại bằng cách này.
> Bản 1.2 chốt thêm Q15 (hỗ trợ cả BBA và non-BBA) và Q16 (Trục 2 giữ bằng Decision; bản 1.4 sửa: nuôi MIO Viettel có sẵn bằng `add_mio_size`, xem 6.5). Bản 1.1 so với 1.0: đã chốt Q1, Q2, Q4 (Phần 13); đã đối chiếu một phần với repo Millennium Dawn chính thức (Phần 12.2) và sửa các điểm bị ảnh hưởng ở Phần 5.1, 7.5, 8.2, 9.
> Khuôn tham khảo: `VIE_naval_truc3_review_and_plan.md` (nhánh hải quân: 3 trục + Program Engine 1B, đã qua review). Bản này áp sẵn các bài học của review đó (Phần 3.2) để không lặp lại các lỗi chặn.
> Dữ kiện lịch sử: tra nguồn công khai ngày 2026-10-02 (danh sách cuối tài liệu). **Tôi không đọc được repo hay bản clone MD**, nên mọi tên token, ID, khóa loc trong game đều là *đề xuất* và được đánh dấu `[?]`, gom lại ở Phần 12 để kiểm trước khi code.
>
> Ký hiệu độ tin cậy của dữ kiện: **[✓]** có nguồn công khai khớp nhau · **[~]** báo chí/phân tích đưa tin, chưa có xác nhận chính thức hoặc các nguồn lệch nhau · **[?]** chưa kiểm, là giá trị khởi điểm do tôi đặt.
>
> **KẾT LUẬN: Nhánh không quân nên dựng đúng khuôn của hải quân (3 trục + 1B), vì dữ liệu lịch sử đủ dày cho cả bốn phần.**
> - **Trục 1:** 16 sự kiện mua sắm lịch sử có cửa sổ thời gian (4 đợt Su-30MK2, S-300PMU1, Pechora-2TM, C-295M, SPYDER, VERA-NG, Yak-130, L-39NG, T-6C…); sự kiện thứ 17 (khủng hoảng hỗ trợ Su-27/30) chuyển sang 1B.
> - **Trục 2:** 5 trụ công nghiệp quốc phòng (Nhà máy A32, Nhà máy A31, radar Viettel, tích hợp hệ thống, UAV), mỗi trụ 3 bậc; 7 focus + 5 Decision lặp lại (mỗi trụ một Decision, bậc kế đọc biến bậc); nuôi MIO Viettel có sẵn.
> - **Trục 3:** 22 focus lực lượng (8 chung + 3 nhánh học thuyết) và 5 Decision.
> - **1B:** 10 chương trình giả định bám các tin 2025–2026 (F-16V, Rafale, Su-57E, AEW&C, tiếp dầu…).
>
> Khác hải quân ở bốn điểm: (1) quân chủng PK-KQ gồm cả tên lửa phòng không và radar, nên nhánh "lịch sử" là phòng không tích hợp chứ không phải "chỉ có máy bay"; (2) máy bay không có "hull" mà có khung máy bay và module, rủi ro tech còn lớn hơn tàu; (3) lịch sử mua sắm dày hơn hải quân nhiều, và đang có loạt tin chưa xác nhận (2025–2026) rất hợp để làm 1B; (4) nút thắt thật của không quân Việt Nam là đào tạo phi công và phụ thuộc hỗ trợ kỹ thuật của Nga, cả hai cần có chỗ đứng trong thiết kế.

---

# PHẦN 1 — PHẠM VI VÀ RANH GIỚI

## 1.1 Nhánh này gồm gì

| Thuộc nhánh không quân | Ghi chú |
|---|---|
| Tiêm kích, tiêm kích-bom, đa nhiệm (Su-22, Su-27, Su-30MK2 và hậu duệ) | Lõi của nhánh |
| Huấn luyện bay (Yak-52, L-39, Yak-130, T-6C, L-39NG) và trường sĩ quan không quân | Nút thắt thật, nằm ở Trục 1 và T1 của Trục 3 |
| Vận tải, trực thăng của quân chủng (An-26, C-295M, Mi-8/17) | Nhẹ, chủ yếu ở 1B |
| Tên lửa phòng không tầm trung/xa (S-125, S-75, S-300PMU1, SPYDER) và radar cảnh giới | Có trong nhánh vì quân chủng là "Phòng không – Không quân" (hợp nhất 1999–2000) |
| UAV, cảnh báo sớm, tiếp dầu (chủ yếu giả định) | 1B và nhánh C của Trục 3 |
| Công nghiệp sửa chữa/nâng cấp (A32, A31, Viettel) | Trục 2 |

## 1.2 Ranh giới với các nhánh khác (một chiều, không ghi ngược)

| Nhánh | Quy ước |
|---|---|
| Hải quân, `VIE_nf_naval_aviation` (B4) | **Tuần tra biển, chống ngầm trên không, trực thăng hạm thuộc hải quân.** Không quân không làm P-8, Ka-28, DHC-6. Hai bên chỉ chia sẻ khung máy bay nếu MD bắt buộc (xem Q10) |
| Lục quân (phòng không tầm ngắn, MANPADS, pháo phòng không) | Ở lại lục quân. Không quân chỉ có SAM tầm trung/xa và radar thuộc quân chủng |
| Vietnam Special Force (chưa thiết kế) | Nhảy dù, đổ bộ đường không thuộc nhánh đó. Không quân chỉ cung cấp "vận tải" ở 1B (P6), không tạo focus riêng |
| Nhánh Biển Đông | Chiều phụ thuộc duy nhất: **năng lực không quân → mở focus Biển Đông** (như hải quân đã làm với `VIE_assert_maritime_rights`). Đề xuất một cổng: T8 hoàn tất mở sớm một focus "tuần tra và kiểm soát vùng trời Trường Sa". Biển Đông không đọc cờ nào khác của không quân |
| Không gian/vệ tinh | **Ngoài phạm vi** (có tin Việt Nam mua vệ tinh quan sát, chưa xác nhận [~]). Nếu muốn, làm một nhánh nhỏ riêng sau; xem Q12 |

---

# PHẦN 2 — BỐI CẢNH LỊCH SỬ 2000–2026

## 2.1 Quân chủng và tình trạng ban đầu

- Quân chủng PK-KQ hình thành dạng hiện nay từ 1999–2000, khi Không quân và Phòng không hợp nhất [✓]. Nó vừa là không quân vừa là phòng không quốc gia.
- Đầu những năm 2000: đội bay chủ lực là MiG-21 (hàng trăm chiếc, nhiều bản) và Su-22 (Liên Xô chuyển giao 70 chiếc 1981–1984); chỉ có 12 Su-27SK/UBK mua 1995 và 1997 [✓]. Phòng không dựa vào S-75, S-125 từ thời Liên Xô, đã xuống cấp sau 1991 [✓].
- Hợp tác quốc phòng Ấn Độ – Việt Nam (3/2000) gồm đại tu MiG-21 và đào tạo phi công/kỹ thuật viên [✓]; 10/2006 Ấn Độ cấp phụ tùng MiG-21 [✓].
- Chuỗi cung ứng phụ thuộc Nga áp đảo (hơn 80% nhập khẩu vũ khí) [✓]. Sau 2022 có tin Rosoboronexport/Sukhoi chỉ hỗ trợ tiếp nếu trả trước lớn [~]. Đây là động lực chính của đa dạng hóa nguồn mua.

## 2.2 Dòng thời gian (nền cho Trục 1, 2, 3)

| Thời điểm | Sự kiện | Tin cậy | Gắn vào |
|---|---|---|---|
| 3/2000 | Hiệp định hợp tác quốc phòng Ấn Độ: đại tu MiG-21, đào tạo | [✓] | Trục 1 E1 |
| 8/2003 | Nga đồng ý cấp 2 tiểu đoàn S-300PMU1; tiểu đoàn đầu (12 bệ phóng, 62 tên lửa) giao 8/2005 | [✓] | Trục 1 E2 |
| 12/2003 | Hợp đồng 4 Su-30MK2 (khoảng 120 triệu USD), giao 11/2004 | [✓] | Trục 1 E3 |
| 2008 | Đặt 10 Yak-52 (Romania) | [✓] | Trục 1 E4 |
| Đầu 2009 | Hợp đồng 8 Su-30MK2 không kèm vũ khí (khoảng 400 triệu USD), giao 2010–2011 | [✓] | Trục 1 E5 |
| 2/2010 | Hợp đồng 12 Su-30MK2V kèm vũ khí, phụ tùng (nguồn nêu khoảng 1 tỷ USD cả gói), giao xong cuối 2012 | [✓] (giá lệch giữa các nguồn) | Trục 1 E6 |
| 2009–2011 | Nâng cấp S-125 lên Pechora-2TM (hãng Tetraedr, Belarus), thử nghiệm tại Nhà máy A31 tháng 3/2011 | [✓] | Trục 1 E7, Trục 2 A31 |
| 6/2011 | Trung đoàn 923 bắt đầu thay Su-22 bằng Su-30MK2V; toàn bộ Su-27 chuyển sang Trung đoàn huấn luyện 940 | [✓] | Trục 3 T5 |
| 2011 | Nhà máy A32 (Đà Nẵng) đề xuất tự đại tu Su-27 | [✓] | Trục 2 A32 |
| 2013 | Hợp đồng 3 C-295M (khoảng 100 triệu USD gồm phụ tùng, đào tạo), vào biên chế từ 2015 | [✓] | Trục 1 E8 |
| 8/2013 | Hợp đồng 12 Su-30MK2 cuối (khoảng 600 triệu USD), giao 2014 đến đầu 2016, tổng 36 chiếc | [✓] | Trục 1 E9 |
| 2014–2018 | Chương trình nâng cấp ZSU-23-4M với hệ điều khiển hỏa lực số của Viettel | [✓] | Trục 2 Radar |
| 2013–2016 | VERA-NG thụ động (Séc), giao 2014–2016; SPYDER (Israel) 5 hệ thống nhận 2016–2018 kèm tên lửa Python-5/Derby | [✓] (ngày đặt hàng SPYDER chưa rõ) | Trục 1 E10, E11 |
| 5/2016 | Mỹ dỡ bỏ lệnh cấm bán vũ khí sát thương cho Việt Nam | [✓] | Mở cổng đối tác Mỹ |
| 2016 | Mất 1 Su-30MK2 do tai nạn; hoàn tất 3 trung đoàn Su-30MK2 (927 Kép, 923 Sao Vàng, 935 Biên Hòa) | [✓] | Trục 3 T7 |
| 2016 | Nhà máy A32 đại tu Su-27 đầu tiên bằng tài liệu mua ngoài | [✓] | Trục 2 A32 bậc 1 |
| 2016–2017 | MiG-21 chính thức nghỉ hưu | [✓] (năm chính xác chưa rõ) | Trục 1 E12 |
| 12/2016 | Thỏa thuận quốc phòng Ấn Độ: đào tạo phi công Su-30 tại Ấn Độ | [✓] | Trục 1 E13 |
| 2017 | Quân chủng công bố lập sư đoàn huấn luyện tiêm kích siêu âm, chương trình đào tạo phi công 5 năm; cân nhắc Yak-130 và L-39NG | [✓] | Trục 1 E14, Trục 3 T1 |
| 2017–2019 | A32 kéo dài niên hạn: Su-22 trên 30 năm, Su-27 trên 20 năm, Su-30MK2 15 năm | [✓] | Trục 2 A32 bậc 2 |
| 2019–2021 | Yak-130 (12 chiếc, khoảng 350 triệu USD) | [✓] đã mua 12 chiếc (xác nhận của chủ dự án 2026-10-02); năm hợp đồng 2019–2020 tùy nguồn, chưa rõ năm giao | Trục 1 E14 |
| 6/2021 | Mỹ chấp thuận bán T-6C Texan II (12 chiếc, giao 2024–2027) | [✓] | Trục 1 E15 |
| 2021 | Đặt 12 L-39NG (Aero Vodochody/Omnipol) | [✓] | Trục 1 E16 |
| 2019–2024 | A32 đại tu 20 Su-22, 5 Su-27, 4 Su-30MK2 (theo báo quân chủng) | [✓] | Trục 2 A32 bậc 3 |
| 8/2024 – 3/2025 | Giao đủ 12 L-39NG (2 đợt, mỗi đợt 6) | [✓] | Trục 1 E16 |
| 11/2024 | 5 T-6C đầu tiên tới Việt Nam (căn cứ Phan Thiết) | [✓] (một nguồn thứ cấp ghi 2023, không khớp) | Trục 1 E15 |
| 12/2024 | Triển lãm VIDEX: Viettel giới thiệu radar 3D VRS-MSSS, radar chống tàng hình RV-02 | [✓] | Trục 2 Radar bậc 3 |
| 2023–2026 | Tin Nga ngần ngại hỗ trợ Su-27/30; Nhà máy A32 đạt đại tu Su-30MK2, tự sửa C-295M | [~] / [✓] | Trục 1 E17, Trục 2 |

## 2.3 Tin chưa xác nhận, dùng làm nền cho 1B

| Tin | Mức | Dùng ở |
|---|---|---|
| 4/2025: Việt Nam thỏa thuận mua ít nhất 24 F-16 (nhiều khả năng F-16V) | [~] (nguồn: 19FortyFive qua RFA; chưa có xác nhận chính thức) | 1B P2 (đối tác USA) |
| 4/2026: phi công Việt Nam bay thử Rafale; nói về khoảng 24–40 chiếc, 4–6 tỷ USD, giao sớm nhất 2028–2030, thay khoảng 30 Su-22 | [~] | 1B P2 (đối tác FRA) |
| 4/2026: Bộ Quốc phòng quan tâm Su-57, dự kiến đầu thập niên 2030 | [~] | 1B P3 |
| 8/2026: Việt Nam có thể là khách hàng đầu của Yak-130M, 18 chiếc | [~] (bản thân Yak-130M mới bay thử 6/2026) | 1B P1 |
| Quan tâm Barak-8 | [~] | 1B P8 |

## 2.4 Bốn áp lực lịch sử và cách thiết kế đáp ứng

| Áp lực | Biểu hiện | Đáp ứng trong thiết kế |
|---|---|---|
| Đội bay già, MiG-21 đã mất | Su-22 (khoảng 30 chiếc) và Su-27 gần hết niên hạn | Trục 2 A32 (kéo dài niên hạn); 1B P2 thay thế |
| Phụ thuộc hỗ trợ của Nga | Phụ tùng, tài liệu, động cơ AL-31F | Sự kiện E17 + Trục 2 (A32 bậc 3 giảm phạt) |
| Đa dạng hóa nguồn | CZE (L-39NG), USA (T-6C), ISR (SPYDER), FRA (Rafale?) | Cổng đối tác ở Trục 1, bảng đối tác ở 1B |
| Đào tạo phi công là nút cổ chai | Chương trình 5 năm: Yak-52/T-6C → L-39NG → Yak-130 → Su-30 | T1 + D-A + E4/E13/E14/E15/E16 |

---

# PHẦN 3 — QUY TẮC THIẾT KẾ

## 3.1 Mười bốn quy tắc cho nhánh không quân

| # | Quy tắc |
|---|---|
| R1 | **Hai nguồn sự thật:** việc đã xảy ra → Trục 1 (cửa sổ thời gian, có thử lại; cổng chỉ gồm đối tác còn tồn tại và không có chiến tranh; quan hệ ngoại giao chỉ ảnh hưởng AI). Tin/giả định → 1B (Decision, người chơi chủ động; AI chỉ khi `VIE_ai_free`) |
| R2 | Focus chỉ mở Decision, đặt mốc, cấp XP và modifier nhỏ. Việc đào tạo/xây dựng là Decision |
| R3 | Không giữ cờ phản chiếu trạng thái có sẵn (`has_completed_focus`, scripted trigger thay cho cờ). Chỉ giữ cờ "đã xong" khi HOI4 không hỏi được. Mọi biến/cờ phải có người đọc thật |
| R4 | Mọi lựa chọn có đánh đổi bằng số (tiền, thời gian, trần modifier, phụ thuộc đối tác) |
| R5 | Trục 3 chỉ cấp modifier vận hành và XP. Không đụng giá, sản xuất, độ tin cậy của Trục 2; không ghi `VIE_cap_*` hay bậc của Trục 2 |
| R6 | Trục 2 sở hữu: bậc năng lực, giá, tuổi thọ/độ tin cậy, `VIE_cap_*` |
| R7 | Ngày cổng chương trình mua sắm đặt ở Decision hoặc cửa sổ sự kiện, không ở focus. Riêng chuỗi focus chung của Trục 3 có `date >` theo mốc lịch sử (tiền lệ hải quân) |
| R8 | Ngân sách pop-up: tuân `VIE_popup_cd` và luật không quá 7 pop-up mỗi năm; chuỗi chọn do người chơi bấm Decision thì miễn cd; event ẩn không tính |
| R9 | Bộ đếm slot (Trục 3: tối đa 2; 1B: tối đa 2; Trục 2: tối đa 2) phải được đếm lại theo timed idea sau nội chiến |
| R10 | Mọi hiệu ứng vận hành ghi vào `VIE_armed_forces_modifier` qua biến `VIE_af_*` kèm tooltip; có trần cho đường đầy đủ, kiểm bằng script cân bằng |
| R11 | Phụ thuộc không vòng: Trục 1 → Trục 2 → {Trục 3, 1B}. Hai cạnh ngược (Trục 1 và 1B cộng exp vào Trục 2; Trục 3 cộng thưởng vào Trục 1) chỉ **cộng thưởng**, không gate |
| R12 | Nhánh Biển Đông, hải quân, Special Force chỉ đọc năng lực không quân, không viết ngược |
| R13 | ID tiếng Anh theo tiền tố nhóm; loc tiếng Việt (BOM, `:0`); mọi tên đơn vị/máy bay trong loc ghi `TODO(names)` nếu chưa kiểm |
| R14 | Mọi con số là giá trị khởi điểm cho tới khi script cân bằng đo xong |

## 3.2 Bài học của review hải quân, đã áp sẵn

| Lỗi hải quân | Ở không quân đã xử lý thế nào |
|---|---|
| A1: focus nền không còn trong cây live | T1 treo trực tiếp dưới `VIE_modernize_vpa`; không phụ thuộc focus hải quân hay lục quân. Phải kiểm cây live, xem 12.1 |
| A2: ID đụng khóa loc chết | Tiền tố mới (4.3); kiểm khóa loc cũ của các focus không quân đã xóa trước khi đặt tên |
| A3: cờ/biến phản chiếu hoặc không ai đọc | Chỉ giữ 4 bộ đếm có người đọc (4.2); không có biến "readiness" 0–100 |
| A4: tên biến đếm tàu sai | Dùng đúng một bộ đếm tích lũy `VIE_var_air_delivered` (đếm giao hàng, gồm cả máy bay sau này bị mất) |
| A5: Funding Gate phải dùng cổng đã code | Dùng trigger kiểu `VIE_naval_can_fund` và nhánh thiếu vốn kiểu `vie_naval.43` (cắt/vay ×1,1/hoãn/hủy). Q9 hỏi có nên gộp thành trigger chung không |
| A6: "dữ liệu thay event" không thực hiện được trong script | Kiến trúc hai tầng: phần dùng chung viết tay, phần theo chương trình sinh bằng script từ bảng dữ liệu |
| A7: thiếu hull tech và module tech | Rủi ro lớn nhất, nằm đầu checklist (Phần 9, 12) |
| B1: không có trạng thái "chờ" | Cổng ở lúc bấm Decision; đã bắt đầu thì chạy hết |
| B2: Decision chạy chuỗi nhiều tháng | Decision là nút khởi động → chuỗi event chọn → timed idea hiển thị → event ẩn hoàn tất |
| B3: bộ đếm slot sau nội chiến | Hook `VIE_collapse_aftermath` đã bỏ (không dùng nữa); bộ đếm tự chữa theo timed idea (6.6) |
| B5: variant của đối tác không có sẵn | Mọi máy bay 1B dùng variant do VIE tự tạo (`creator = VIE`) |
| L1: readiness chỉ template đọc | Bỏ hẳn; hiệu ứng "sẵn sàng" là modifier thật |
| L6/L8: phạt lệch nhánh | Giữ cặp đối xứng phạt/thưởng nhỏ ở focus mở nhánh |
| L7: thưởng ngược Trục 1 | Chỉ có một cạnh ngược duy nhất (xem 5.4, E15) |

---

# PHẦN 4 — KIẾN TRÚC VÀ HỢP ĐỒNG GIỮA CÁC TRỤC

## 4.1 Sơ đồ phụ thuộc

```
                       VIE_modernize_vpa  (root quân sự, cổng chung)
                              |
        +---------------------+-----------------------+
        |                     |                       |
   TRỤC 1 (sự kiện       TRỤC 2 (công nghiệp)     TRỤC 3 (focus lực lượng)
   lịch sử, cửa sổ)      5 trụ x 3 bậc            8 chung + 3 nhánh
        |  exp, đếm máy bay      |  bậc, VIE_cap_*      |  mở khóa
        +----------> Trục 2 ----+--------------------> 1B (Program Engine)
                                                       10 chương trình giả định
   cạnh ngược (chỉ cộng thưởng): 1B -> exp Trục 2 ;  Trục 3 -> thưởng nhỏ ở E15 (huấn luyện)
```

## 4.2 Biến và cờ cuối cùng (đề xuất, mọi tên là `[?]`)

| Tên | Loại | Đặt bởi | Đọc bởi |
|---|---|---|---|
| `VIE_var_air_delivered` | biến ≥ 0 | Trục 1 và 1B, +1 mỗi tiêm kích giao (Trục 1 chỉ Su-30; huấn luyện và vận tải không tính; kể cả sau này mất) | T5 (`> 11`), Trục 2 |
| `VIE_var_air_multirole4` | biến ≥ 0 | 1B P2 | D-E (nhánh B) |
| `VIE_var_sam_lr` | biến ≥ 0 | Trục 1 E2, 1B P8 | D-E (nhánh A) |
| `VIE_var_uav_delivered` | biến ≥ 0 | 1B P9 | D-E (nhánh C) |
| `VIE_var_airf_program_active`, `VIE_var_a1b_active`, `VIE_var_apm_active` | biến 0–2 | các hàm start/end, recount | `available` của Decision |
| `VIE_airf_fighter_level`, `VIE_airf_fighter_specialty`, `VIE_airf_sam_level`, `VIE_airf_sam_orientation`, `VIE_airf_force_priority` (1–3) | biến | event chọn của Trục 3 (7.3) | event hoàn tất, focus mở nhánh |
| `VIE_airf_d1_done` … `VIE_airf_d5_done` | cờ | event ẩn hoàn tất | D-C, P4 |
| `VIE_ap_su35_talks` (E9 lựa chọn B), `VIE_ap_barak_research` (E10 lựa chọn B), `VIE_ap_yak130_declined` (E14 lựa chọn B, đọc bởi E16), `VIE_ap_pechora_scope` (E7: 1 hoặc 2), `VIE_ap_radar_viettel_fast` (E11 lựa chọn C) | cờ/biến | event Trục 1 | `available` của 1B; Trục 2 A31 bậc 1 và Radar (cờ đặt trước, chưa ai đọc tới khi dựng Trục 2) |
| Bậc Trục 2: `VIE_apm_a32_tier`, `VIE_apm_a31_tier`, `VIE_apm_radar_tier`, `VIE_apm_integ_tier`, `VIE_apm_uav_tier` (mỗi biến 0–3); `VIE_cap_mature_air_industry` | biến/cờ | Trục 2 | 1B (điều kiện nội địa/hybrid), T-chain |
| `VIE_a1b_<p>_contracted/_cancelled`; `…_qty_ordered/_qty_delivered/_localization` | cờ/biến | engine 1B | giao hàng, hiển thị |

Không giữ: `_active/_done/_waiting` cho Decision, `_progress`, "readiness". Các cờ `VIE_ap_*` ở trên là những kết quả mà HOI4 không hỏi lại được nên được phép giữ theo R3. `VIE_air_e15_done` bị bỏ vì không ai đọc; `e17_west` chuyển theo E17 sang 1B.

## 4.3 Tiền tố và namespace (đề xuất)

| Phần | Tiền tố | Namespace event |
|---|---|---|
| Trục 1 | `VIE_ap_` (cờ/biến); biến đếm `VIE_var_air_delivered` | `vie_air_proc` |
| Trục 2 | `VIE_apm_` (đề xuất; **không dùng** `VIE_air_`, xem dưới) | `vie_air_ind` (đề xuất) |
| Trục 3 | `VIE_airf_` | `vie_air_force` |
| 1B | `VIE_a1b_` | `vie_a1b` |
| Biến modifier dùng chung | `VIE_af_*` (giữ đúng quy ước hiện có, chỉ thêm họ `VIE_af_air_*`) | — |

**Đã có trong repo, không được dùng lại cho Trục 1/2:** `VIE_air_<tên>` (20 character chỉ huy, `VIE_md_air_commanders.txt`), cờ `VIE_air_phase0_done`/`VIE_air_step_N`, scheduler `VIE_event_scheduler_air` + file `VIE_md_effects_air.txt` (roster chỉ huy), idea `VIE_air_dominance_idea`, namespace `vie_air_commanders` (giữ chỗ). Scripted effect trùng tên ghi đè chứ không gộp.

**Tránh:** `VIE_af_` cho nhánh (đã là họ biến modifier), `VIE_ai_` (cờ AI), `VIE_lf_`, `VIE_nf_`, `VIE_nav_`, `VIE_naval_`, `VIE_p1b_`, `VIE_air_`. Với `VIE_ap_`, `vie_air_proc`, `VIE_var_air_delivered` đã grep 0 kết quả trong repo (2026-10-02); `VIE_apm_`, `vie_air_ind`, `VIE_airf_`, `VIE_a1b_` còn phải grep trước khi dùng (xem 12.1).

## 4.4 Vị trí cây focus (đề xuất, chốt bằng `layout.py`)

Hải quân chiếm x ≈ 216–262; lục quân x ≈ 272–284. Đề xuất cột không quân đặt **x ≥ 290** (bên phải lục quân) hoặc **x ≤ 200** (bên trái hải quân), chia theo trục: Trục 2 ở cột gần root, Trục 3 ở cột riêng, giữ khoảng cách cùng hàng ≥ 4 ô và con luôn `y >` cha. `[?]` chưa đo.

---

# PHẦN 5 — TRỤC 1: MUA SẮM LỊCH SỬ (SỰ KIỆN CÓ CỬA SỔ)

> **Bản 1.3 viết lại sau khi đối chiếu MD và repo.** Chi tiết từng lỗi của bản 1.2, bảng ánh xạ trang bị BBA / non-BBA / GOT, lịch giao hàng, bảng pop-up theo năm và plan 7 bước: `VIE_air_truc1_review_and_plan.md`.

## 5.1 Quy ước chung của Trục 1

- **Kiến trúc** (theo p13/p14 lục quân và hải quân): scheduler riêng `VIE_event_scheduler_air_proc`, gọi từ `on_monthly` (khối có `original_tag = VIE`) và `VIE_catch_up_schedule`; không dùng `on_monthly_VIE`, không dùng `trigger_year_*`. Namespace `vie_air_proc`.
- **Cửa sổ và thử lại:** tick tháng chính là vòng thử lại. Cổng đạt + `VIE_popup_cd` trống ⇒ bắn event; cổng đạt + popup_cd bận ⇒ thử lại tháng sau; **hết cửa sổ mà cổng đã từng đạt ⇒ áp dụng kết quả lịch sử im lặng** (`VIE_fb_ap_*`, không phạt người chơi vì lịch sự kiện dày); **chỉ khi cổng không bao giờ đạt** (đối tác không tồn tại hoặc chiến tranh suốt cửa sổ) mới đặt `_missed` (tin nhắn nhỏ, 1B đọc cờ).
- **Catch-up** (nội chiến xong): người thắng chỉ nhận cờ "đã xảy ra", không popup, không máy bay.
- **Cổng** chỉ gồm `country_exists` và `NOT has_war_with`; độ thiện cảm chỉ ảnh hưởng `ai_chance`. **Tag MD:** Ấn Độ `RAJ` (không phải `IND` = Indonesia), Tây Ban Nha `SPR` (không có `ESP`); còn lại `SOV ROM BLR CZE ISR USA FRA SWE`.
- **Tiền** (tỷ USD, `modify_treasury_effect`; từ 0,4 tỷ trở lên chia ngân khố/nợ như T-90). Giá có nguồn **[✓]** giữ nguyên, còn lại **[?]**. **Không có Funding Gate cho lựa chọn lịch sử** (R1; MD tự phát hành nợ; ngân khố VIE đầu game là 5 tỷ). Chỉ lựa chọn "mở rộng" ngoài lịch sử mới có `trigger` ngân khố, tooltip nêu rõ.
- **Cấp trang bị** theo tiền lệ MD (`05_algeria.txt`): `has_dlc = "By Blood Alone"` ⇒ loại BBA + `variant_name` + `producer`; `else` ⇒ loại non-BBA. Tên lửa phòng không (E2, E7, E10) cần DLC **Götterdämmerung** (nhánh tech `SAM` có `allow_branch`); không có GOT chỉ còn timed idea + modifier. Không có thiết bị cho Yak-52, kho đạn máy bay, hay việc loại MiG-21 (xem plan, 3.2).
- **Giao hàng** là Class C trong scheduler (một cờ `VIE_ap_<chương trình>_dN` mỗi đợt), không popup. **Pop-up:** Class B (có lựa chọn) tuân `VIE_popup_cd`; E4, E12, E16 là Class C (kết quả lịch sử im lặng).
- Trục 1 chỉ cộng `VIE_var_air_delivered` (Su-30) và `VIE_var_sam_lr`; **không ghi exp hay bậc Trục 2** (R11). Kết quả cần cho Trục 2 là *cờ* (`VIE_ap_pechora_scope`, `VIE_ap_radar_viettel_fast`) để Trục 2 đọc sau.
- Mọi option phải chọn được; option lịch sử là mặc định của AI.

## 5.2 Mười sáu sự kiện (E1–E16, ID `vie_air_proc.1` – `.16`)

| ID | Cửa sổ | Lớp | Cổng | Nội dung | Lựa chọn và đánh đổi | Hệ quả chính |
|---|---|---|---|---|---|---|
| `.1` Hợp tác Ấn Độ: MiG-21 và đào tạo | 2000.3 – 2002.12 | B | RAJ | DCA tháng 3/2000: đại tu MiG-21, đào tạo | **A (lịch sử)** 0,05; **B** chỉ đào tạo 0,02; **C** từ chối | A: idea "MiG-21 kéo dài niên hạn" (tới `.12`), +10 XP; B: +5 XP |
| `.2` S-300PMU1 | 2004.3 – 2006.12 | B | SOV | Thỏa thuận 8/2003, tiểu đoàn đầu giao 8/2005 (12 bệ, 62 tên lửa) | **A (lịch sử)** 2 tiểu đoàn 0,30 [?]; **B** 1 tiểu đoàn 0,16; **C** hoãn (thử lại; hết cửa sổ thì `_missed`) | `VIE_var_sam_lr` +2/+1; có GOT ⇒ tech SAM1+SAM2 và `sam_missile_equipment_3` |
| `.3` Su-30MK2 đợt 1 | 2004.1 – 2005.12 | B | SOV | 4 chiếc, hợp đồng 12/2003, giao 11/2004, khoảng 120 triệu [✓] | **A (lịch sử)** 4 chiếc 0,12; **B** 6 chiếc + chuyển loại 0,20 (giao +6 tháng, +10 XP); **C** hoãn | `VIE_var_air_delivered` +4/+6 |
| `.4` Yak-52 | 2007 – 2009 | **C** | ROM | Đặt 10 chiếc năm 2008 [✓] | Kết quả lịch sử, 0,02 | XP + idea đào tạo cơ bản (không có thiết bị) |
| `.5` Su-30MK2 đợt 2 | 2008.6 – 2010.6 | B | SOV | 8 chiếc không kèm vũ khí, khoảng 400 triệu [✓]; giao 2010–2011 | **A (lịch sử)** 0,40, đặt idea thiếu đạn (hiệu suất nhiệm vụ giảm) tới `.6`; **B** kèm vũ khí 0,52, không idea; **C** 6 chiếc 0,30 | +8/+6 |
| `.6` Su-30MK2V đợt 3 | 2009.9 – 2011.6 | B | SOV | 12 chiếc kèm vũ khí, phụ tùng; giao xong cuối 2012 | **A (lịch sử)** 1,00; **B** chỉ thân máy 0,62 (idea −3% nhiệm vụ 24 tháng); **C** 8 chiếc 0,70 | +12/+8; gỡ idea thiếu đạn. Mở T5 (cần > 11) |
| `.7` Pechora-2TM | 2009 – 2012 | B | BLR | Nâng cấp S-125, hãng Tetraedr, thử tại A31 tháng 3/2011 [✓] | **A (lịch sử)** trên 30 bệ 0,15 [?]; **B** 15 bệ 0,08. **Bỏ lựa chọn "A31 tự làm"**: A31 bậc 1 của Trục 2 chính là sự kiện này (vòng R11) | Đặt `VIE_ap_pechora_scope` (2/1) cho Trục 2 đọc; có GOT ⇒ tech SAM1 và `sam_missile_equipment_2` |
| `.8` C-295M | 2013.1 – 2014.12 | B | SPR | 3 chiếc cùng phụ tùng, đào tạo, khoảng 100 triệu [✓]; biên chế từ 2015 | **A (lịch sử)** 3 chiếc 0,10; **B** 2 chiếc 0,07; **C** 4 chiếc 0,14 | Máy bay vận tải |
| `.9` Su-30MK2 đợt 4 | 2013.6 – 2014.12 | B | SOV | 12 chiếc, hợp đồng 8/2013, khoảng 600 triệu [✓], giao 2014 đến đầu 2016; đủ 3 trung đoàn | **A (lịch sử)** 0,60; **B** 6 chiếc 0,30, mở đàm phán Su-35S (`VIE_ap_su35_talks`, 1B P2 giảm 10%); **C** hoãn | +12/+6 |
| `.10` SPYDER và Python-5/Derby | 2015.1 – 2016.12 | B | ISR | 5 hệ thống nhận 2016–2018 [✓]; ngày đặt chưa rõ | **A (lịch sử)** 0,25 [?]; **B** 3 hệ thống + nghiên cứu Barak-8 (`VIE_ap_barak_research`, mở P8 sớm) 0,18 | Có GOT ⇒ `sam_missile_equipment_2`; không cộng `VIE_var_sam_lr` (chỉ S-300 là tầm xa). SPAA lục quân `SP_Anti_Air_2` không cấp (thuộc lục quân) |
| `.11` Radar cảnh giới | 2013.1 – 2015.12 | B | CZE (A), ISR (B) | VERA-NG thụ động ×4, giao 2014–2016 [✓] | **A (lịch sử)** 0,06; **B** thêm ELM-2288 0,10; **C** đẩy radar Viettel 0,04 (`VIE_ap_radar_viettel_fast`, phát hiện thấp hơn 24 tháng) | Chỉ modifier `air_detection` (không xây radar: helper tự trừ 1,75 tỷ mỗi trạm) |
| `.12` MiG-21 nghỉ hưu | 2016.1 – 2017.12 | **C** | không | Quân chủng chính thức loại biên MiG-21 [✓, năm chưa rõ] | Kết quả lịch sử: tiết kiệm 0,03; −3% XP không quân 24 tháng | Gỡ idea `.1`. Không loại thiết bị (script không xác minh được `destroy_equipment`) |
| `.13` Đào tạo Su-30 tại Ấn Độ | 2016.12 – 2018.12 | B | RAJ | Thỏa thuận 12/2016 | **A (lịch sử)** 0,05, +10 XP; **B** vẫn gửi sang Nga 0,08, +15 XP (phụ thuộc SOV); **C** tự đào tạo (cần T1 Trục 3; chưa có thì ẩn) | Idea tăng tốc huấn luyện 36 tháng (A) |
| `.14` Yak-130 | 2017 – 2021 | B | SOV | Cân nhắc Yak-130; khoảng 350 triệu, đã mua 12 chiếc (xác nhận; năm giao chưa rõ) | **A** 12 chiếc 0,35; **B** từ chối (`VIE_ap_yak130_declined`); **C** hoãn. **Không còn L-39NG ở đây** (trùng `.16`) | Máy bay huấn luyện nâng cao |
| `.15` T-6C Texan II | 2022.1 – 2024.12 | B | USA | Mỹ chấp thuận 6/2021; 12 chiếc, giao 2024–2027; 5 chiếc đầu 11/2024 [✓] | **A (lịch sử)** 12 chiếc 0,15; **B** 6 chiếc 0,08 | **Cạnh ngược duy nhất:** gói đào tạo 0,12 thay 0,15 nếu `VIE_ap_training_standardized` (chưa có Trục 3 ⇒ `always = no`). Đặt `VIE_ap_t6c_contracted` |
| `.16` L-39NG | 2022 – 2024 | **C** | CZE | 12 chiếc, giao 8/2024 và 3/2025 [✓]; dưới 10 triệu USD mỗi chiếc | Kết quả lịch sử, 0,12; nếu `yak130_declined` có thêm tùy chọn mở rộng +6 chiếc 0,06 (trigger ngân khố) | Máy bay huấn luyện nâng cao |

**Chuyển sang 1B:** sự kiện cũ E17 "Khủng hoảng hỗ trợ kỹ thuật Su-27/30" (2023–2027): nguồn [~] và đọc `VIE_apm_a32_tier` của Trục 2 (ngược chiều R11). Làm thành Decision ở 1B.

## 5.3 Sự kiện và thành phần dùng chung

| Thành phần | Việc |
|---|---|
| `VIE_event_scheduler_air_proc` | Scheduler, catch-up, `VIE_fb_ap_*`, `_missed` (mẫu p13/naval) |
| `VIE_ap_deliver_<chương trình>` | Giao hàng Class C, cờ `_dN` mỗi đợt; lịch ở plan 3.3 |
| `vie_air_proc.60` | Thông báo nhỏ khi `_missed` (`minor_flavor = yes`, thử trong game) |
| `VIE_md_triggers_air_proc.txt` | Cổng đối tác, `VIE_ap_training_standardized` (tùy chọn "mở rộng" dùng `treasury` trực tiếp, không có trigger riêng) |

Bỏ so với 1.2: `vie_air.40–.43` (Funding Gate) và `vie_air.50` (sự kiện ẩn giao hàng).

## 5.4 Ngân sách và tác động

- Tổng chi Trục 1 ở mức "lịch sử" khoảng **3,7 tỷ** USD trong 26 năm, phần lớn là Su-30MK2 (2,1 tỷ).
- **Pop-up (đã đo lại):** repo đã vượt 5 mỗi năm ở 2003=6, 2008=6, 2012=8, 2014=8, 2018=6, 2020=6, 2021=12, 2022=6, 2023=6, 2024=7; mục tiêu hiện hành ≤ 7 (không có code ép). Trục 1 không quân thêm tối đa 13 Class B; cửa sổ đã dời để không vào 2003, 2012, 2014, 2021. Bảng theo năm và các đòn bẩy hạ Class: plan 3.4. **Phải đo bằng `ev.py` và chơi quan sát** (2009 và 2013 chưa đo).
- Cạnh ngược duy nhất vào Trục 1 là `.15` (gói T-6C rẻ hơn nếu Trục 3 xong T1). Chỉ là thưởng, không phải điều kiện.

---

# PHẦN 6 — TRỤC 2: CÔNG NGHIỆP QUỐC PHÒNG HÀNG KHÔNG – PHÒNG KHÔNG

> **Bản 1.4 viết lại sau khi đối chiếu MD và repo** (trước đó Phần 6 chưa được đối chiếu). Lỗi của bản 1.3 và plan code 9 bước: `VIE_air_truc2_review_and_plan.md`.

## 6.1 Ý tưởng

Việt Nam **không sản xuất máy bay chiến đấu**. Câu chuyện thật của công nghiệp không quân là: tự sửa chữa, kéo dài niên hạn, tự làm linh kiện điện tử, và tích hợp vũ khí từ nhiều nguồn. Vì vậy Trục 2 là **năm trụ năng lực** thay vì "xưởng đóng", mỗi trụ có bậc 0–3. Trục 2 là phần *người chơi chủ động xây* (Decision), nên khác Trục 1: các bậc dựa tin chưa xác nhận [~] vẫn được phép có, nhưng AI chỉ đi khi `VIE_ai_free`.

Tiền tố: cờ/biến **`VIE_apm_`**, namespace event **`vie_air_ind`**, category **`VIE_apm_category`**, focus **`VIE_apm_*`**. Không dùng `VIE_air_` (roster chỉ huy) và không dùng tên trần như `VIE_apm_a32_tier`.

## 6.2 Cây focus Trục 2 (7 focus)

Cột **x ≥ 288** (chưa có focus nào ở khu vực này; hải quân x 228–262, lục quân 266–284). Toạ độ tuyệt đối dự kiến, chốt bằng `tools/audit/audit.py`; `relative_position_id` neo vào focus đã khai báo ở trên (tránh forward-ref).

| Mã | ID | Tên | Treo từ / tiền đề | (x, y) | Điều kiện | Khi hoàn thành |
|---|---|---|---|---|---|---|
| F1 | `VIE_apm_law` | Cơ chế công nghiệp quốc phòng – hàng không | `VIE_modernize_vpa` | (292, 3) | `date > 2008.12.31`, không `bankruptcy_incoming_collapse` | `unlock_decision_category_tooltip = VIE_apm_category`, 10 XP không quân |
| F2 | `VIE_apm_a32` | Nhà máy A32: đại tu và kéo dài niên hạn | F1 | (290, 4) | `date > 2010.12.31` | `unlock_decision_tooltip = VIE_apm_d_a32` |
| F3 | `VIE_apm_a31` | Nhà máy A31: tên lửa phòng không | F1 | (292, 4) | — | `unlock_decision_tooltip = VIE_apm_d_a31` |
| F4 | `VIE_apm_radar` | Radar và chỉ huy – điều khiển (Viettel) | F1 | (294, 4) | `date > 2010.12.31` | `unlock_decision_tooltip = VIE_apm_d_radar` |
| F5 | `VIE_apm_integration` | Tích hợp vũ khí và hệ thống đa nguồn | F2, F3, F4 (OR) + trigger "ít nhất hai trong ba" | (292, 6) | `date > 2014.12.31` | `unlock_decision_tooltip = VIE_apm_d_integ` |
| F6 | `VIE_apm_uav` | Chương trình UAV nội địa | F4 | (296, 6) | `date > 2017.12.31` | `unlock_decision_tooltip = VIE_apm_d_uav` |
| F7 | `VIE_apm_mature` | Công nghiệp hàng không – phòng không trưởng thành | F5 và F6 (hai khối riêng = AND) | (294, 8) | `date > 2026.12.31`; trigger `VIE_apm_mature_ok` | đặt `VIE_cap_mature_air_industry` |

`VIE_apm_mature_ok` = `a32_tier = 3`, `a31_tier ≥ 2`, `radar_tier = 3`, `integ_tier ≥ 2`, `uav_tier ≥ 2` (một chỗ để đổi). Focus chỉ cấp XP, tooltip mở Decision và (F7) cờ; không đụng bậc (R5, R6). Focus phải theo thứ tự trường của MD: id → icon → x,y → relative_position_id → cost → prerequisite → search_filters → available → completion_reward → `ai_will_do` (cuối).

## 6.3 Năm trụ, mỗi trụ ba bậc

**Mỗi trụ có một Decision lặp lại** (không `fire_only_once`; MD: "dùng `fire_only_once` tiết kiệm"), như hải quân giữ Decision là *nút khởi động* (50 PP): bấm ⇒ `VIE_apm_program_start` (+1 slot) ⇒ event chọn **của bậc kế** (đọc `VIE_apm_<p>_tier`) ⇒ timed idea hiển thị đang chạy ⇒ event ẩn hoàn tất (`days = biến`) tăng bậc, trao hiệu ứng, `VIE_apm_program_end`. Decision `available`: slot < 2, không còn timed idea của chính trụ, và scripted trigger `VIE_apm_<p>_ok` (cổng của bậc kế, bên dưới). Tối đa 2 chương trình chạy cùng lúc (`VIE_var_apm_active`). Cổng đọc từ Trục 1 nằm trong cột "Cổng".

### Trụ 1 · Nhà máy A32 (đại tu khung máy bay, Đà Nẵng) → `VIE_apm_a32_tier`

| Bậc | Mốc thật | Cổng | Chi phí / thời gian | Lựa chọn (đánh đổi) | Hiệu ứng |
|---|---|---|---|---|---|
| 1 | Tự đại tu Su-27 (đề xuất 2011, thành công 2016) | F2; `date > 2010.12.31` | 0,12 / 18 tháng | **Mua tài liệu nước ngoài**: 0,15, 12 tháng; **tự biên soạn**: 0,08, 24 tháng | `air_accidents_factor` −3%; +5 XP không quân |
| 2 | Kéo dài niên hạn Su-22 (>30 năm), Su-27 (>20 năm), kiểm Su-30MK2 (15 năm), 2017–2019 | bậc 1; `date > 2016.12.31` | 0,20 / 24 tháng | **Chỉ Su-22 và Su-27**: 0,15; **thêm Su-30MK2 cục bộ**: 0,20, +6 tháng | tai nạn thêm −3% |
| 3 | Đại tu Su-30MK2, tự sửa C-295M (2025–2026) | bậc 2; `date > 2023.12.31`; `VIE_var_air_delivered ≥ 12` | 0,30 / 30 tháng | **Ưu tiên Su-30MK2**; hoặc **C-295M và trực thăng** (rẻ hơn 0,05; cần `VIE_ap_c295_qty > 0`) | tai nạn thêm −2% (tổng −8%); đọc bởi 1B (P3, Decision hỗ trợ Su-27/30) |

### Trụ 2 · Nhà máy A31 (tên lửa phòng không) → `VIE_apm_a31_tier`

| Bậc | Mốc thật | Cổng | Chi phí / thời gian | Lựa chọn | Hiệu ứng |
|---|---|---|---|---|---|
| 1 | S-75M3 hiện đại hóa; Pechora-2TM (2009–2011) | F3; `VIE_ap_pechora_scope > 0` (Trục 1 `.7`) | 0,10 / 18 tháng; scope 2 ⇒ ×0,8 chi phí, −3 tháng | **Với BLR** (cần BLR tồn tại): nhanh; **tự làm**: 0,04, +12 tháng | `VIE_af_air_defence_factor` +1% |
| 2 | S-125VT với linh kiện điện tử trong nước (Viettel) | bậc 1; `date > 2012.12.31` | 0,15 / 24 tháng | Chỉ S-125; hoặc cả S-75 | phòng không +1%; `VIE_af_equipment_cost_multiplier_modifier` −1%; MIO Viettel +1 |
| 3 | Bảo dưỡng S-300PMU1; sản xuất tên lửa mới `[~]` | bậc 2; `VIE_var_sam_lr ≥ 1`; `date > 2020.12.31` | 0,35 / 36 tháng | **Bảo dưỡng**; hoặc **sản xuất** (+0,10, cần `radar_tier ≥ 2`) | phòng không +2%; MIO Viettel +1; chọn sản xuất đặt `VIE_apm_sam_production` (điều kiện hybrid P8) |

### Trụ 3 · Radar và chỉ huy – điều khiển (Viettel) → `VIE_apm_radar_tier`

| Bậc | Mốc thật | Cổng | Chi phí / thời gian | Lựa chọn | Hiệu ứng |
|---|---|---|---|---|---|
| 1 | Radar tầm thấp VRS-2DM; hệ hỏa lực số cho ZSU-23-4M (2014–2018) | F4; `date > 2013.12.31` | 0,10 / 18 tháng; `VIE_ap_radar_viettel_fast` ⇒ ×0,8, −3 tháng | Chỉ radar; hoặc cả hỏa lực số | `VIE_af_air_detection` +2% |
| 2 | VRS-M2D (VHF), VRS-MRS (3D băng S) | bậc 1; `date > 2018.12.31` | 0,18 / 24 tháng | Đẩy nhanh (0,22, 18 tháng) hoặc theo lịch | phát hiện +2%; MIO Viettel +1 |
| 3 | VRS-MSSS (3D), RV-02 chống tàng hình (VIDEX 12/2024) | bậc 2; `date > 2023.12.31` | 0,30 / 30 tháng | Một chiều: **chống tàng hình** hoặc **ưu tiên 3D** (`VIE_apm_radar_orient` 1/2) | phát hiện +2% (tổng +6%); điều kiện nội địa của P10 |

### Trụ 4 · Tích hợp hệ thống và vũ khí → `VIE_apm_integ_tier`

| Bậc | Mốc thật | Cổng | Chi phí / thời gian | Lựa chọn | Hiệu ứng |
|---|---|---|---|---|---|
| 1 | Lắp Python-5/Derby lên máy bay Nga `[~]` | F5; `VIE_ap_spyder_qty > 0` | 0,12 / 18 tháng | Tên lửa không đối không; hoặc không đối đất | cờ định hướng (đọc bởi 1B) |
| 2 | Liên kết dữ liệu, chỉ huy đa nguồn (S-300, SPYDER, radar Viettel) | bậc 1; `VIE_var_sam_lr ≥ 1`; `radar_tier ≥ 1` | 0,25 / 24 tháng | Chuẩn Nga (rẻ); hoặc chuẩn mở (+0,07) | điều kiện hybrid P2, P3, P8 |
| 3 | Tích hợp chuẩn phương Tây (huấn luyện T-6C/L-39NG, tương thích F-16V/Rafale) | bậc 2; `VIE_ap_t6c_qty > 0` hoặc `VIE_ap_l39ng_qty > 0`; `date > 2024.12.31` | 0,40 / 36 tháng | Ưu tiên huấn luyện hoặc ưu tiên tác chiến | điều kiện P3 |

### Trụ 5 · UAV → `VIE_apm_uav_tier`

| Bậc | Mốc thật | Cổng | Chi phí / thời gian | Lựa chọn | Hiệu ứng |
|---|---|---|---|---|---|
| 1 | Mục tiêu bay M-100CT (đã có) | F6; `date > 2017.12.31` | 0,05 / 12 tháng | — | +5 XP không quân |
| 2 | UAV trinh sát nội địa `[~]` | bậc 1; `radar_tier ≥ 1`; `date > 2022.12.31` | 0,15 / 24 tháng | Mua công nghệ ngoài (nhanh, 0,20) hoặc nội địa | MIO Viettel +1; điều kiện nội địa của P9 |
| 3 | UAV tấn công/loitering `[~]` | bậc 2; `date > 2025.12.31` | 0,30 / 36 tháng | Chỉ cánh cố định hoặc cả loitering | điều kiện nhánh C (C4); chọn loitering đặt `VIE_apm_uav_loitering` |

Tổng chi nếu đủ 15 bậc khoảng 3,1 tỷ USD (thang giá thật, như Trục 1), rải từ 2009 đến khoảng 2030. Khác Trục 2 hải quân/lục quân (30–35 tỷ) vì không xây công trình nào của MD (helper `one_state_*` tự trừ 3–7,5 tỷ mỗi công trình).

## 6.4 Hiệu ứng thuộc Trục 2 và token đã kiểm

| Hiệu ứng | Token | Ghi chú |
|---|---|---|
| Tai nạn không quân (A32) | `VIE_af_air_accidents_factor` (→ `air_accidents_factor`) | có sẵn trong `VIE_armed_forces_modifier`; tổng Trục 2 −8% |
| Phát hiện (Radar) | `VIE_af_air_detection` | tổng Trục 2 +6%; cộng Trục 1 (≤ 5%) và Trục 3 phải qua script cân bằng |
| Phòng không (A31) | `VIE_af_air_defence_factor` | +4%; Trục 1 đã dùng ≤ 6% |
| "Giá thay thế tên lửa" của báo cáo 1.2 | **không có token trong MD** (MD chỉ có `olv_/…sat_production_*` và `equipment_cost_multiplier_modifier` = chi phí duy trì) | thay bằng `VIE_af_equipment_cost_multiplier_modifier` −1% mỗi bậc A31 từ bậc 2 |
| Kinh nghiệm không quân | `air_experience` | như Trục 1 |
| Công nghiệp | MIO Viettel (`add_mio_size`) | xem 6.5; bọc `has_dlc = "Arms Against Tyranny"` |
| Điều kiện cho Trục 3 và 1B | bậc `VIE_apm_*_tier`, cờ `VIE_apm_sam_production`, `VIE_apm_radar_orient`, `VIE_cap_mature_air_industry` | đọc, không viết ngược |

Không có modifier sản xuất hay chi phí chế tạo máy bay (R5): MD không có token tương ứng ngoài MIO.

## 6.5 MIO (sửa so với bản 1.2: **repo đã có MIO**, Trục 2 dùng luôn)

Bản 1.2 (Q16) nói Việt Nam chưa có MIO và để MIO "làm sau". Thực tế `common/military_industrial_organization/organizations/VIE_md_organizations.txt` đã có 4 tổ chức (AAT-gated, `allowed = { original_tag = VIE }`): `VIE_viettel_manufacturer` (UAV, tên lửa, SAM, radar, điện tử: đúng 4 trụ), `VIE_vaeco_manufacturer` (máy bay nhẹ, trực thăng, vận tải), `VIE_gdt_manufacturer`, `VIE_ba_son_manufacturer`. Trục 2 hải quân và lục quân đã nuôi MIO của mình bằng `add_mio_size` bọc `has_dlc = "Arms Against Tyranny"` (`VIE_ba_son_mio_size_N`), và `add_mio_funds` tự lên size nên **chỉ dùng `add_mio_size`** (Q8 = a).

**Quyết định (Q16 sửa):** Trục 2 không quân giữ bậc bằng **biến + Decision** (không đổi) *và* nuôi `VIE_viettel_manufacturer` bằng helper `VIE_apm_viettel_mio_size` (+1 ở A31 bậc 2, 3; Radar bậc 2; UAV bậc 2; tổng +4). Không có MIO cho A32 (tiêm kích không thuộc `equipment_type` của MIO nào; VAECO chỉ nhận vận tải/trực thăng/huấn luyện nhẹ). Người không có AAT không mất gì (helper bỏ qua). Trait của Viettel đã cho bonus SAM (`air_attack` +6%) và UAV (`air_range`, `air_ground_attack`, giá −5%): modifier Trục 2 **không** cộng thêm cùng loại để tránh đếm đôi.
Cần kiểm trong game: size tối đa của MIO MD, và `add_mio_size` có áp dụng cho `VIE_viettel_manufacturer` khi chưa chọn trait nào không.

## 6.6 Slot, nội chiến và AI

- `VIE_var_apm_active` 0–2 (+1/−1 bằng `VIE_apm_program_start/_end`, `clamp_variable`). Không có hook nội chiến nào: `VIE_collapse_aftermath` đã bỏ và không dùng nữa (mod đã gỡ collapse/civil war). Bộ đếm **tự chữa**: hàm tháng `VIE_apm_slot_heal` đặt lại 0 khi không còn timed idea `VIE_apm_prog_*` nào, nên không cần gắn vào bất kỳ sự kiện nội chiến nào.
- AI: base 80 / 50 / 30 theo bậc 1 / 2 / 3, `factor 0` khi `bankruptcy_incoming_collapse`; bậc dựa tin [~] (UAV 2–3, A31 bậc 3 sản xuất) chỉ khi `VIE_ai_free`; mỗi lần chỉ một chương trình với AI.

---

# PHẦN 7 — TRỤC 3: XÂY DỰNG LỰC LƯỢNG (22 FOCUS + 5 DECISION)

## 7.1 Cây focus

Cấu trúc: **8 focus chung → 3 nhánh học thuyết loại trừ nhau** (4 + 5 + 5 = 14 focus nhánh). Mỗi lần chơi đi 12 hoặc 13 focus.

### Chuỗi chung (8)

| Mã | ID (đề xuất) | Tên | Prerequisite | Ngày / điều kiện |
|---|---|---|---|---|
| T1 | `VIE_airf_training_standardization` | Chuẩn hóa đào tạo phi công và kỹ thuật viên | `VIE_modernize_vpa` | `date > 2004.12.31` (Su-30MK2 đầu giao 11/2004) |
| T2 | `VIE_airf_fighter_force` | Phát triển lực lượng tiêm kích | T1 | `date > 2007.12.31` |
| T3 | `VIE_airf_sam_force` | Phát triển lực lượng tên lửa phòng không và radar | T1 | `date > 2005.12.31` (S-300PMU1 giao 8/2005) |
| T4 | `VIE_airf_command_reform_1` | Cải cách chỉ huy PK-KQ I | T2 và T3 | `date > 2009.12.31` |
| T5 | `VIE_airf_first_force` | Cơ cấu lực lượng ban đầu | T4, hoặc `VIE_apm_a32` | `date > 2011.12.31`; `VIE_var_air_delivered > 11` (đường lịch sử: 4 + 8 = 12 vào 2011) |
| T6 | `VIE_airf_command_reform_2` | Cải cách chỉ huy PK-KQ II (trung tâm chỉ huy tích hợp, liên kết với lục quân, hải quân) | T5 | `date > 2013.12.31` |
| T7 | `VIE_airf_medium_force` | Lực lượng không quân trung bình | T6 | `date > 2015.12.31` (đủ 3 trung đoàn Su-30MK2 cuối 2016) |
| T8 | `VIE_airf_operating_range` | Mở rộng bán kính hoạt động và căn cứ tiền phương | T7 | `date > 2017.12.31` |

### Nhánh A — Phòng không – Không quân tích hợp (nhánh lịch sử, 4 focus)

| Mã | ID | Tên | Prerequisite | Ngày |
|---|---|---|---|---|
| A1 | `VIE_airf_iads` | Phòng không tích hợp (loại trừ B1, C1) | T8 | — |
| A2 | `VIE_airf_layered_defence` | Mạng radar – tên lửa nhiều tầng | A1 | `date > 2019.12.31` |
| A3 | `VIE_airf_ew_antistealth` | Tác chiến điện tử và chống tàng hình | A2 | `date > 2021.12.31` |
| A4 | `VIE_airf_iads_command` | Bộ chỉ huy phòng không khu vực | A3 | `date > 2024.12.31` |

### Nhánh B — Không quân đa nhiệm khu vực (cải cách / phương Tây, 5 focus)

| Mã | ID | Tên | Prerequisite | Ngày |
|---|---|---|---|---|
| B1 | `VIE_airf_multirole` | Không quân đa nhiệm (loại trừ A1, C1) | T8 | — |
| B2 | `VIE_airf_multirole_fleet` | Chương trình tiêm kích đa nhiệm 4.5 | B1 | `date > 2024.12.31` |
| B3 | `VIE_airf_sustainment` | Bảo đảm kỹ thuật đa nguồn | B1 | `date > 2022.12.31` |
| B4 | `VIE_airf_airlift_tanker` | Vận tải và tiếp dầu trên không | B1 | `date > 2026.12.31` |
| B5 | `VIE_airf_multirole_wing` | Cánh không quân đa nhiệm | B2, B3, B4 (ba khối riêng = AND) | `date > 2028.12.31` |

### Nhánh C — Không quân không người lái và mạng hóa (công nghệ, 5 focus)

| Mã | ID | Tên | Prerequisite | Ngày |
|---|---|---|---|---|
| C1 | `VIE_airf_unmanned` | Không người lái và mạng hóa (loại trừ A1, B1) | T8 | — |
| C2 | `VIE_airf_isr_uav` | UAV trinh sát và mục tiêu | C1 | `date > 2020.12.31` |
| C3 | `VIE_airf_datalink` | Mạng liên kết dữ liệu (C4ISR) | C1 | `date > 2022.12.31` |
| C4 | `VIE_airf_strike_uav` | UAV tấn công | C2 | `date > 2025.12.31` |
| C5 | `VIE_airf_teaming` | Phối hợp có người – không người | C3 và C4 | `date > 2029.12.31` |

`[?]` Các nhánh B và C chỉ mở cho người chơi tự do/`VIE_ai_free`; AI mặc định đi nhánh A (như quy tắc hải quân).

## 7.2 Phần thưởng focus (chỉ XP, modifier và `unlock_decision_tooltip`)

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP +15; kinh nghiệm không quân +4% | category Trục 3 |
| T2 | tấn công không quân +1% | D-A |
| T3 | tấn công phòng không +2% | D-B |
| T4 | hiệu suất nhiệm vụ +2% | D-C |
| T5 | XP +10 | D-D |
| T6 | hiệu suất nhiệm vụ +2%, phát hiện +2% | — |
| T7 | tầm bay +3% | lối vào 1B: P1, P6, P7 |
| T8 | tầm bay +4%, phát hiện +3% | ba nhánh |
| A1–A4 | A1 phòng không +2%; A2 phát hiện +4%, phòng không +2%; A3 phòng thủ không quân +3%, phát hiện +3%; A4 nhiệm vụ +2%, phòng không +2% (nhân 1,0/1,5 theo D-E) | A2: P8, P10; A3: P4; A4: D-E |
| B1–B5 | B1 tầm bay +4%; B2 tấn công +3%, ưu thế trên không +2%, hỗ trợ mặt đất +2%; B3 nhiệm vụ +2%; B4 tầm bay +3%; B5 nhiệm vụ +2%, tấn công +2% (nhân 1,0/1,5) | B2: P2 (và P3 từ 2030); B4: P5; B5: D-E |
| C1–C5 | C1 phát hiện +3%; C2 phát hiện +4%; C3 nhiệm vụ +3%; C4 tấn công +3%; C5 nhiệm vụ +2%, phòng thủ +2% (nhân 1,0/1,5) | C2: P9; C3: P4, P10; C5: D-E |

(Mức lệch nhánh và đúng nhánh: xem 7.4.)

## 7.3 Năm Decision lực lượng (category `VIE_air_force_category`, `allowed = original_tag = VIE`)

Mỗi Decision: `fire_only_once`, chi phí 50 PP (D-E 60 PP), cổng ở lúc bấm (không có trạng thái "chờ"), chuỗi chọn là event nối tiếp (miễn `VIE_popup_cd`), hoàn tất bằng event ẩn; slot `VIE_var_airf_program_active < 2`.

| Decision | Mở từ | Chuỗi chọn | Hoàn tất |
|---|---|---|---|
| D-A `VIE_airf_d1_fighters` | T2 | Mức: **Cơ bản** 0,40 tỷ / 12 tháng; **Chuyên sâu** 0,60 / 18 tháng. Chuyên môn: **Không chiến** hoặc **Tấn công mặt đất/mặt biển** | Đặt mức, chuyên môn, modifier theo 7.5, `VIE_airf_d1_done` |
| D-B `VIE_airf_d2_sam` | T3 | Định hướng: **Lịch sử** 0,30 (nâng cấp S-125, S-75 tại A31) hoặc **Sớm** 0,50 (đưa hệ thống mới vào biên chế ngay, thưởng đầu cao hơn). Mức Cơ bản/Chuyên sâu (×1,0/×1,5). | `VIE_airf_d2_done`, modifier |
| D-C `VIE_airf_d3_coordination` | T4 | Không có lựa chọn: 0,50 tỷ / 18 tháng, **đòi `d1_done` và `d2_done`**. Ba giai đoạn ẩn: (1) XP và hiệu suất nhiệm vụ; (2) phối hợp tiêm kích – tên lửa; (3) bức tranh trên không tích hợp | `VIE_airf_d3_done` |
| D-D `VIE_airf_d4_first_force` | T5 | Ba cơ cấu: **1 Phòng thủ lãnh thổ**, **2 Cân bằng**, **3 Tầm xa**. 0,60 tỷ / 12 tháng. Đặt `VIE_airf_force_priority` | `VIE_airf_d4_done`, modifier |
| D-E `VIE_airf_d5_capstone` | A4, B5 hoặc C5 | 1,0 tỷ / 18 tháng. Cổng theo nhánh: **A** `VIE_var_sam_lr ≥ 1` và radar bậc ≥ 2; **B** `VIE_var_air_multirole4 ≥ 12`; **C** `VIE_var_uav_delivered ≥ 4` và `VIE_apm_uav_tier ≥ 2` | Nhân thưởng nhánh ×1,0 (đạt mức đầu) hoặc ×1,5 (đạt mức hai: ≥ 2 hệ thống / ≥ 24 chiếc / ≥ 8 UAV) |

Chi phí D-A đến D-D khoảng 1,8 tỷ (mọi mức Cơ bản, D-B Lịch sử) đến 2,45 tỷ (mọi mức Chuyên sâu, D-B Sớm), cộng D-E 1,0 tỷ. Tổng đối xứng với hải quân.

## 7.4 Lệch nhánh và đúng nhánh (đối xứng, nhỏ)

- Cơ cấu D-D ở mức 1 (Phòng thủ lãnh thổ) hợp với nhánh A; mức 2 (Cân bằng) hợp mọi nhánh; mức 3 (Tầm xa) hợp nhánh B và C.
- **Lệch nhánh** khi mở A1/B1/C1: timed idea 365 ngày, hiệu suất nhiệm vụ −3%, phát hiện −3%. **Đúng nhánh**: +1% hiệu suất nhiệm vụ.
- Mức chuyên môn (D-A) là lựa chọn một lần. Hướng còn lại được bù một phần bởi giai đoạn 2 của D-C (phối hợp tiêm kích – tên lửa).

## 7.5 Bảng modifier (giá trị khởi điểm; token `[?]`, cần tra MD)

| Nguồn | Hiệu ứng (+ là bonus) |
|---|---|
| D-A mức 1/2 × Không chiến | ưu thế trên không +3% / +4,5% |
| D-A mức 1/2 × Tấn công đất/biển | hỗ trợ mặt đất +3% / +4,5%; tấn công +1% / +1,5% |
| D-B mức 1/2 | phòng không +3% / +4,5%; phát hiện +1% / +1,5% (Sớm: +1% thêm) |
| D-C (ba giai đoạn) | nhiệm vụ +2%; phòng không +2%, ưu thế +2%; phát hiện +2%, nhiệm vụ +2% |
| D-D Phòng thủ | phòng thủ +3%, phòng không +2%, tầm bay −3% |
| D-D Cân bằng | tấn công +1%, phòng thủ +1%, tầm bay +1% |
| D-D Tầm xa | tầm bay +5%, nhiệm vụ +2%; chi phí nhân sự không quân +3% (token `airforce_personnel_cost_multiplier_modifier`, **đã xác nhận** trong tài liệu MD) |

**Token đã đối chiếu với MD/HOI4 gốc (12.2 mục 1–3):** `experience_gain_air_factor`, `air_attack_factor`, `air_defence_factor`, `air_mission_efficiency`, `air_superiority_efficiency`, `air_cas_efficiency`, `air_range_factor`, `air_detection`, `air_accidents_factor`. Dòng "phòng không" (tấn công phòng không mặt đất) vẫn `[?]`, chưa tìm thấy token. Không dùng `air_agility_factor` vì MD đã đổi "Agility" thành "Radar Advantage" trong tính toán không chiến.

**Trần cho đường đầy đủ** (script cân bằng cộng cả ba nhánh): kinh nghiệm không quân ≤ +10%, tấn công ≤ +10%, phòng thủ ≤ +8%, hiệu suất nhiệm vụ ≤ +16%, ưu thế trên không ≤ +10%, hỗ trợ mặt đất ≤ +10%, tầm bay ≤ +20%, phòng không ≤ +20%, phát hiện ≤ +18%. Tính tay sơ bộ: nhánh A phòng không ≈ 17,5%, nhánh B tầm bay ≈ 19%, hiệu suất nhiệm vụ ≈ 16% (sát trần), nhánh C phát hiện ≈ 16,5%. Nếu script báo vượt thì hạ giá trị chứ không nâng trần (như hải quân đã làm).

Không có modifier sản xuất, chi phí chế tạo hay tai nạn (R5; thuộc Trục 2).

---

# PHẦN 8 — TRỤC 1B: PROGRAM ENGINE (MUA SẮM GIẢ ĐỊNH, BẰNG DECISION)

## 8.1 Vai trò

Trục 1 chỉ chứa **việc đã xảy ra**. Mọi thứ còn là tin hoặc giả định (F-16V, Rafale, Su-57E, Yak-130M, Barak-8, AEW&C, tiếp dầu, UAV tấn công…) nằm ở **1B**: người chơi chủ động bấm Decision; không có cửa sổ lịch sử, không event tự kích, không "lỡ hẹn" (khác Trục 1). AI chỉ bấm khi `VIE_ai_free`.

## 8.2 Mười chương trình

Giá là tỷ USD mỗi chiếc/hệ thống ở mức **nhập khẩu**. Mức nội địa hóa: **nhập khẩu** (×1,0 giá, ×1,0 thời gian) / **hybrid** (×1,10, ×1,15; bảo dưỡng và một phần linh kiện trong nước, điều kiện Trục 2) / **nội địa** (×1,25, ×1,30; chỉ áp dụng cho P9, P10; máy bay chiến đấu tối đa là hybrid). `[?]` các hệ số này là giá trị khởi điểm.

| Mã | Chương trình | Lối vào (focus + ngày) | Đối tác và giá/đơn vị | Số lượng | Tới đơn vị đầu (tháng) | Điều kiện hybrid/nội địa (Trục 2) |
|---|---|---|---|---|---:|---|
| P1 | Huấn luyện – tiêm kích hạng nhẹ | T7, ≥ 2024 | SOV Yak-130M 0,035 [~]; CZE L-39NG 0,012 [✓]; KOR FA-50 0,06 [?]; ITA M-346 0,05 [?] | 6–18 | 18 | Hybrid: `a32_tier ≥ 2` |
| P2 | Tiêm kích đa nhiệm 4.5 (thay Su-22) | T7 và (B2 hoặc `VIE_ap_su35_talks` hoặc `VIE_ap_a32_west` (đặt bởi Decision E17 ở 1B)), ≥ 2025 | FRA Rafale 0,16 [~]; USA F-16V 0,12 [?]; SWE Gripen E 0,10 [?]; SOV Su-35S 0,09 [?] (−10% nếu `su35_talks`) | 12–36 (bước 6) | 36 | Hybrid: `a32_tier ≥ 2` và `integration_tier ≥ 2` |
| P3 | Tiêm kích thế hệ 5 | B2, ≥ 2030 | SOV Su-57E 0,14 [?] | 6–12 | 60 | `a32_tier = 3` và `integration_tier ≥ 2` |
| P4 | Máy bay cảnh báo sớm (AEW&C) | T7 và (A3 hoặc C3), ≥ 2022 | ISR G550 0,45 [?]; SWE GlobalEye 0,35 [?]; SOV A-50EI 0,40 [?] | 1–3 | 48 | Hybrid: `radar_tier = 3` |
| P5 | Máy bay tiếp dầu | B4, ≥ 2026 | FRA/EU A330 MRTT 0,25 [?]; BRA KC-390 0,10 [?]; SOV Il-78 0,15 [?] | 1–2 | 36 | Nhập khẩu |
| P6 | Vận tải chiến thuật bổ sung | T7, ≥ 2020 | SPR C-295M 0,035 [✓]; BRA C-390 0,085 [?] | 2–6 | 24 | Hybrid: `a32_tier = 3` (A32 đã tự sửa C-295M) |
| P7 | Trực thăng đa dụng | T7, ≥ 2020 | SOV Mi-171Sh 0,02 [?]; FRA H225M 0,03 [?]; USA UH-60M 0,03 [?] | 6–18 | 18 | Hybrid: `a32_tier ≥ 2` |
| P8 | Tên lửa phòng không tầm trung/xa | A2 hoặc lựa chọn B của E10, ≥ 2018 | SOV S-400 0,60 [?]; ISR Barak-8 0,25 [~]; USA/NOR NASAMS 0,20 [?]; KOR KM-SAM 0,30 [?] | 1–4 tổ hợp | 30 | Hybrid: `a31_tier ≥ 2` và `radar_tier ≥ 2`; cộng `VIE_var_sam_lr` |
| P9 | UAV | C2, ≥ 2022 | ISR Heron 0,04 [?]; TUR 0,02 [?]; nội địa | 2–6 hệ thống | 18 | Nội địa: `uav_tier ≥ 2` (tối đa bậc 3 cho UAV tấn công) |
| P10 | Mạng radar tầm xa (hệ thống mặt đất, không phải máy bay) | A2 hoặc C3, ≥ 2020 | ISR ELM-2288 0,06; FRA GM400 0,05; nội địa VRS-MSSS 0,03 | 2–8 trạm | 18 | Nội địa: `radar_tier = 3` |

- **Lối vào khác nhau theo nhánh** là cố ý: nhánh A thấy P4, P8, P10; nhánh B thấy P2, P3, P5; nhánh C thấy P4, P9, P10. P1, P6, P7 mở chung từ T7.
- Tổng nếu mua hết ở số lượng tối đa, mức nhập khẩu: khoảng 14,1 tỷ USD (P2 chiếm 5,8 tỷ), tối đa khoảng 16–17 tỷ nếu toàn bộ ở hybrid. Chương trình lớn nhất (P2 ×36) cao hơn trung vị chi phí event của MD (khoảng 4,0 tỷ theo báo cáo hải quân) nhưng thấp xa p90 (26,45 tỷ). Kiểm bằng script cân bằng.
- Đánh đổi theo đối tác (R4): **USA** giá thấp nhất nhưng timed idea 24 tháng "điều kiện vũ khí và tiếp cận cơ sở" (tấn công không quân −3%), thưởng huấn luyện; **FRA** đắt, không điều kiện chính trị, GPS-dependent không mô hình hóa; **SWE** trung bình, hybrid rẻ hơn 5%; **SOV** rẻ nhất nhưng nếu `a32_tier < 3` và E17 chưa xử lý thì chịu phạt hỗ trợ.
- **P8 là hệ tên lửa, không phải máy bay:** cấp thiết bị SAM theo bậc và triển khai theo cơ chế tên lửa của MD, không dùng chuỗi variant (12.2 mục 4).
- **P9 (UAV)** khả thi như một variant máy bay có module "drone avionics" (12.2 mục 6), không cần loại thiết bị mới.
- **Hoãn có điều kiện:** P4 (AEW) và P5 (tiếp dầu) chỉ dựng nếu MD có loại thiết bị tương ứng (AEW: có nhóm tech AWACS nhưng chưa xác minh thiết bị; tiếp dầu: chưa tìm thấy). Nếu không, đưa thành modifier thuần ở focus (như hải quân từng hoãn P5, P9).

## 8.3 Chuỗi chương trình (dùng chung)

Decision (`available`: focus, ngày, `VIE_var_a1b_active < 2`, đối tác tồn tại và không chiến tranh nếu nhập khẩu, chưa `contracted`) → `vie_a1b.1` chọn số lượng → `vie_a1b.2` chọn nhập khẩu / hybrid / nội địa (mức sau đòi bậc Trục 2) → **Funding Gate** (dùng trigger kiểu `VIE_naval_can_fund`; thiếu vốn → `vie_a1b.3`: cắt quy mô / vay ×1,1 / hoãn / hủy) → hợp đồng (trừ tiền, cấp tech, tạo variant, hẹn giao, timed idea hiển thị) → event ẩn giao từng đợt (mỗi đợt tối đa 6 chiếc, cách nhau 6 tháng) → đợt cuối: cộng exp Trục 2 theo mức nội địa hóa (0% / 50% / 100% của phần thưởng), cộng bộ đếm (`VIE_var_air_delivered`, `_multirole4`, `_sam_lr`, `_uav_delivered`), −1 slot.

Mã dữ liệu mỗi chương trình (tiền tố `VIE_a1b_<p>_`): cờ `contracted`, `cancelled`; biến `qty_ordered`, `qty_delivered`, `localization` (0–2). `<p>` ∈ {`trainer`, `multirole`, `gen5`, `aew`, `tanker`, `airlift`, `helo`, `sam`, `uav`, `radar_net`}. Không có `_complete/_offered/_missed` (R3).

**Số event 1B thực tế:** 3 dùng chung (viết tay) + khoảng 10 event ẩn giao hàng (sinh bằng script từ một bảng dữ liệu). Thêm chương trình = thêm một dòng bảng + chạy lại script; tên cờ, `create_equipment_variant`, tên máy bay vẫn là literal trong mã sinh ra (bài học A6 của hải quân).

---

# PHẦN 9 — TEMPLATE THIẾT KẾ MÁY BAY (VARIANT) VÀ TECH

Nguyên tắc (bài học B5, A7, **sửa ở bản 1.1 theo đối chiếu MD**): **ưu tiên cấp variant đã có sẵn trong MD** khi MD đã định nghĩa máy bay thật tương ứng (MD có các variant đặt tên theo máy bay thật như "Su-30", "Typhoon Tranche 1"; đội MD từng phải sửa focus Algeria vì gọi sai tên variant). **Chỉ tự tạo variant VIE** (`creator = VIE`, cờ chặn trùng) khi MD chưa có. Tech khung máy bay và module cấp **khi ký hợp đồng** bằng `set_technology`, **kèm đủ prerequisites** (cách MD đã dùng để sửa thiết kế sai của 70 nước); nếu không đủ thì lùi về `add_tech_bonus` và đòi nghiên cứu. **Q15 đã chốt hỗ trợ cả có và không có By Blood Alone:** mỗi lần cấp máy bay có hai nhánh `has_dlc`; nhánh non-BBA dùng thiết bị cùng bậc của chuỗi tech non-BBA (`MR_Fighter`…), nhánh BBA dùng variant theo trình thiết kế. Checklist Phần 12 phải chạy hai lượt (có và không có BBA).

| Chương trình | Loại máy bay (dự kiến) | Variant mẫu cần chép module từ MD | Ghi chú rủi ro |
|---|---|---|---|
| P1 | huấn luyện/tiêm kích nhẹ | variant có sẵn của nước có L-39/Yak-130 | Dễ nhất |
| P2 | đa nhiệm 4.5 (khung và radar AESA, động cơ, vũ khí) | variant của FRA (Rafale), USA (F-16V), SWE (Gripen), SOV (Su-35S) trong `history/countries` | Rủi ro lớn nhất: module bị bỏ im lặng nếu thiếu tech |
| P3 | thế hệ 5 | variant SOV (Su-57) | Phụ thuộc tech 5 |
| P4, P5 | AEW&C, tiếp dầu | variant ISR/SWE/FRA (nếu MD có loại thiết bị) | Có thể không có trong MD |
| P6, P7 | vận tải, trực thăng | variant SPR, FRA, SOV | Dễ |
| P8 | SAM | thiết bị tên lửa SAM theo bậc (`sam_missile`, 8 bậc) và triển khai | Khác cơ chế, xem 12.2 mục 4 |
| P9 | UAV | khung máy bay + module drone avionics | Cần kiểm tech mở module (12.2 mục 6) |
| P10 | radar mặt đất | building/equipment radar | Không có variant |

Tên máy bay trong loc: placeholder `TODO(names)`; tên biên đội Việt Nam (trung đoàn 923, 927, 935…) chỉ dùng khi đã kiểm chứng đơn vị.

---

# PHẦN 10 — AI

| Phần | Quy tắc |
|---|---|
| Focus Trục 3 | `ai_will_do` base 60 cho chuỗi chung; 40 cho A1/B1/C1 với `factor` theo đường (Historical: nhánh A ×1,5, nhánh B ×0,5, nhánh C ×0,25; Reform/Western: B ×1,5; chỉ `VIE_ai_free` cho B và C); `factor = 0` khi `bankruptcy_incoming_collapse` |
| Decision lực lượng | base 100, `factor = 0` khi `bankruptcy_incoming_collapse`; option lịch sử `base 90` + `add 100` nếu `VIE_ai_historical`; option khác `factor 0` nếu không `VIE_ai_free`, có guard tài chính (`bankruptcy_incoming_collapse`, `ai_has_high_deficit`) |
| Trục 1 | option lịch sử là mặc định của AI; quan hệ ngoại giao chỉ cộng `ai_chance`; mọi option phải có ít nhất một đường chọn được (bài học zero-weight) |
| Trục 2 | base 80 cho bậc 1 của từng trụ, 50 cho bậc 2, 30 cho bậc 3; guard tài chính; chỉ một chương trình chạy mỗi lần với AI |
| 1B | base 20 và chỉ khi `VIE_ai_free` (AI không đi alt-history ngoài chế độ free); cùng guard tài chính; tránh giữ slot vô ích |

---

# PHẦN 11 — KHỐI LƯỢNG ƯỚC TÍNH

| Hạng mục | Số lượng |
|---|---|
| Focus | 22 (Trục 3) + 7 (Trục 2) = **29** |
| Decision | 5 (Trục 3) + 5 (Trục 2, lặp lại theo bậc) + 10 (1B) = **20** |
| Event | Trục 1: 16 event + scheduler (đã code); Trục 2: ≈ 20 (15 event chọn theo bậc + 5 event ẩn hoàn tất); Trục 3: ≈ 13; 1B: ≈ 13 → **≈ 80** (khoảng một nửa là ẩn, không tính vào ngân sách pop-up) |
| Script | khoảng 4 500 dòng, trong đó khoảng 2 000 do script sinh |
| Loc | khoảng 700 khóa |
| Chi phí in-game | Trục 1 ≈ 3,7 tỷ; Trục 2 ≈ 3,1 tỷ; Trục 3 ≈ 2,8–3,5 tỷ; 1B tối đa ≈ 14–17 tỷ |

Con số 1B ở trên chưa tính Q15 (hỗ trợ cả BBA và non-BBA): cộng khoảng 30% khối lượng 1B (mỗi variant hai bản hoặc guard `has_dlc`).

Khối lượng lớn hơn hải quân vì bản này gộp cả Trục 1 và 2 (ở hải quân hai trục đó đã làm xong trước).

**Nếu cần cắt phạm vi, theo thứ tự ít đau nhất:**
1. Bỏ các sự kiện flavor Trục 1: E1, E4, E12, E13 (−4 event).
2. Gộp trụ Tích hợp và UAV của Trục 2 (−3 Decision, −6 event).
3. Rút nhánh C còn 3 focus (C1, C2/C3 gộp, C5) và hoãn P9.
4. Giữ 1B ở 7 chương trình (bỏ P5, P7, P9).

---

# PHẦN 12 — ĐIỂM CẦN ĐỐI CHIẾU TRƯỚC KHI CODE (BƯỚC 0)

## 12.1 Với repo (đã đối chiếu một phần ngày 2026-10-02 cho Trục 1; mục chưa tích là chưa kiểm)

- [ ] `VIE_modernize_vpa` vẫn là root quân sự duy nhất trong cây live (A1 hải quân).
- [ ] Focus không quân cũ nằm ở `v11_removed_military_all_subbranches.txt` hoặc `.bak`; khóa loc chết nào còn nằm trong `VIE_md_p2_l_english.yml` (tránh trùng khóa với loc mới).
- [x] `VIE_air_` và `vie_air` **không** sạch (roster chỉ huy, xem 4.3): Trục 1 đổi sang `VIE_ap_` / `vie_air_proc` (grep 0). Còn phải grep `VIE_airf_`, `VIE_a1b_`, `VIE_apm_`, `vie_air_force`, `vie_a1b`, `vie_air_ind`.
- [ ] Vùng trống trên lưới cây focus (`layout.py`) cho khoảng 29 focus.
- [ ] Ngân sách `VIE_armed_forces_modifier`: lục quân, hải quân, Biển Đông đã dùng token không quân (nếu có) bao nhiêu.
- [x] Số pop-up/năm hiện tại: đã vượt 5 ở 10 năm (5.4); mục tiêu ≤ 7.
- [ ] Trigger funding của hải quân (`VIE_naval_can_fund`) có dùng lại được không (Q9).
- [ ] Biển Đông đã có cổng nào đọc năng lực không quân chưa.

## 12.2 Với MD: KẾT QUẢ ĐỐI CHIẾU (2026-10-02)

**Đã đọc:** repo chính thức `MillenniumDawn/Millennium-Dawn` nhánh `main` (release mới nhất v2.0.0-beta.3 ngày 3/7/2026; bản dự kiến v2.0.0), gồm README, tài liệu `code-resource.md`, các trang docs, changelog v1.9 "Top Gun" và v2.0 "The Millennium Renaissance". **Chưa đọc được:** mã nguồn các file `common/…`, `history/…`, vì GitHub chặn công cụ của tôi vào trang duyệt thư mục. Những gì cần soi tận file được gom thành lệnh grep ở cuối mục này để chạy trên clone của bạn.

| # | Mục cần kiểm | Kết quả | Tác động tới thiết kế |
|---|---|---|---|
| 1 | Token chi phí nhân sự không quân | **Có:** `airforce_personnel_cost_multiplier_modifier` (ghi trong `code-resource.md`, cạnh `army_…` và `navy_…`) | Sửa tên token ở D-D Tầm xa (7.5). Tôi đã đoán sai thành `air_personnel_…` |
| 2 | Token modifier không quân | **Có**, là token của HOI4 gốc: `experience_gain_air_factor`, `air_attack_factor`, `air_defence_factor`, `air_mission_efficiency`, `air_superiority_efficiency`, `air_cas_efficiency`, `air_range_factor`, `air_detection`, `air_accidents_factor` (nguồn thứ cấp: danh sách static modifier của cộng đồng). **Không tìm thấy** token cho tấn công phòng không mặt đất và cho "radar advantage" | 7.5 dùng tên đã kiểm; dòng "phòng không" giữ `[?]`; phải tra `modifier_definitions` của HOI4 gốc để xác nhận chính thức |
| 3 | Cơ chế không chiến | MD v1.9 đổi **"Agility" thành "Radar Advantage"** và nói Radar Advantage quan trọng hơn hầu hết chỉ số khác; tai nạn không quân tăng với máy bay độ tin cậy thấp | Bỏ `air_agility_factor`. **Trụ Radar của Trục 2 và modifier phát hiện quan trọng hơn tôi dự tính**; A32 (giảm tai nạn) cũng có giá trị thật. Cân nhắc tăng trần phát hiện sau khi có số đo |
| 4 | SAM trong MD | v2.0: SAM là **thiết bị tên lửa** (`sam_missile`, 8 bậc), tách khỏi sản xuất dân sự, trả tiền hàng tuần; "Foreign SAM Missiles Can Now Be Deployed"; **Việt Nam được cấp sẵn tech SAM/SAM0** (nhóm 34 nước có SAM đời ≤ 1965); v1.9 thêm 15 modifier tốc độ sản xuất tên lửa (tên chưa đọc được) | E2, E7, E10, P8 và trụ A31 phải làm trên **hệ tên lửa**, không dùng chuỗi `create_equipment_variant`. S-125 và S-75 coi như đã có từ đầu; S-300PMU1 và SPYDER là bậc cao hơn. `VIE_var_sam_lr` có thể thay bằng số tổ hợp triển khai |
| 5 | Máy bay và variant | Có **trình thiết kế máy bay** (v1.9), khung tới bậc 6; MD có sẵn variant đặt tên theo máy bay thật ("Su-30", "Typhoon Tranche 1", F-35A…). v2.0 sửa lỗi Algeria vì focus gọi variant "Su-30MKA" (không tồn tại) thay vì "Su-30" | Phần 9 đã sửa: **ưu tiên dùng variant có sẵn**. Cần xem `history/countries/` của VIE đã có "Su-30", "Su-27", "Su-22" chưa |
| 6 | UAV | Không thấy loại thiết bị UAV riêng. Các bản sửa v2.0 cho thấy **"drone avionics" là module nằm trong slot avionics** của khung máy bay (F-35A, Tempest); có mô-đun tên lửa chống hạm cho drone, "Kamikaze drone", raid bằng drone | P9 khả thi như variant máy bay có module drone avionics. Không cần loại thiết bị mới |
| 7 | AEW và tiếp dầu | Có nhóm tech **AWACS** (v2.0 sửa ngày `start_year` của tech này), nhưng chưa xác minh loại thiết bị. **Không thấy** tiếp dầu trong tài liệu | P4 giữ "hoãn có điều kiện"; P5 có khả năng phải thành modifier thuần |
| 8 | Rủi ro A7 (tech khung và module) | **Được xác nhận bởi chính lịch sử sửa lỗi của MD:** v2.0 sửa thiết kế của **70 nước** đang trang bị module chưa nghiên cứu, nên variant không dùng được; cách MD xử lý là cấp tech kèm prerequisites trong history. Spain từng gặp focus trực thăng cấp license nhưng không hiện vì thiếu tech trực thăng | `set_technology` phải kèm đủ prerequisites và kiểm điều kiện tech trước khi cấp. Đưa vào checklist: sau khi cấp, variant phải **hiện trong kho** |
| 9 | Phụ thuộc DLC | Trình thiết kế máy bay và khung gắn với **By Blood Alone (BBA)**; MD giữ nhánh tech "non-BBA" (chuỗi `MR_Fighter`) và sửa nhiều lỗi cho người chơi thiếu BBA (v2.0: module cảm biến/avionics/AAM của trực thăng trước chỉ mở qua BBA) | **Quyết định mới (Q15):** hỗ trợ cả BBA và non-BBA hay chỉ BBA. Nếu cả hai, mỗi variant 1B cần hai bản hoặc guard `has_dlc` |
| 10 | MIO (tổ chức công nghiệp quân sự) | v2.0 có MIO riêng cho USA, ITA, FRA…; chưa có Việt Nam **trong MD**. **Nhưng repo mod đã định nghĩa 4 MIO của VIE** (Viettel, VAECO, GDT, Ba Son), Trục 2 hải quân/lục quân đã nuôi chúng bằng `add_mio_size` | **Bản 1.4:** Trục 2 không quân nuôi `VIE_viettel_manufacturer` (6.5); không cộng đôi với trait sẵn có |
| 11 | Mastery và học thuyết | v1.9 thêm học thuyết không quân JSEAD, Light Aircraft, Strategic Destruction; v2.0 nâng "air mastery" ở focus chung từ 10 lên 25 | `add_mastery { folder = air }` rất có khả năng tồn tại (chưa thấy trực tiếp); trigger chọn grand doctrine không quân chưa xác minh |
| 12 | Mô hình mua sắm | v1.9 **gỡ** hệ "MD Equipment Purchasing", thay bằng Thị trường quốc tế; v2.0 (SMA) có 30 event mua trang bị có chấp nhận/từ chối, AI chỉ mua khi `treasury > 30`; từng sửa lỗi bán trang bị mà không trừ kho người bán | Funding Gate và guard tài chính của ta khớp quy ước MD. Trục 1/1B tách hẳn khỏi Thị trường quốc tế (tránh giá chồng chéo) |
| 13 | Chi phí focus | v2.0 gỡ chi phí PP khỏi phần thưởng focus ở 39 cây ("thời gian focus là chi phí") và HOL chỉ tính tiền cho focus tài trợ dự án thật | Khớp: focus của ta không tiêu PP hay tiền, Decision mới tiêu. Chỉ cần so mức 50 PP/Decision với mặt bằng hải quân và lục quân |
| 14 | Không gian/vệ tinh | v2.0 có hệ thống vệ tinh và phóng đầy đủ, kể cả tự động hóa chương trình | Q12 giữ "ngoài phạm vi"; không cần nhánh riêng |
| 15 | Phiên bản | Repo ở v2.0.0-beta.3 (3/7/2026), wiki ghi phiên bản dự kiến v2.0.0, checksum `442a` | Xác nhận clone của bạn cùng phiên bản trước khi code |

**Lệnh grep để chạy trên clone của bạn** (đường dẫn thư mục là suy đoán theo cấu trúc HOI4, điều chỉnh nếu khác):

```
grep -rn "airforce_personnel_cost_multiplier_modifier" common/modifier_definitions
grep -rln "sam_missile" common/units/equipment
grep -rn "Su-30\|Su-27\|Su-22" history/countries/VIE*
grep -rln "drone_avionics\|awacs\|tanker\|refuel" common/
grep -rn "add_mastery" common/ | grep -i air
grep -rn "has_dlc = \"By Blood Alone\"" history/countries/VIE*
ls common/military_industrial_organization | grep -i vie
grep -rn "anti_air_attack_factor\|air_detection" common/modifier_definitions
```

Các mục còn lại của 12.2 cũ (variant mẫu của FRA, USA, SWE, SOV, ISR, KOR, ITA trong `history/countries/`) cũng phải kiểm trên clone. Với variant Rafale, F-16V, Gripen: chưa biết MD đã có chưa.

## 12.3 Dữ kiện lịch sử còn lệch hoặc chưa kiểm

| Điểm | Tình trạng |
|---|---|
| Giá gói Su-30MK2 2010 | Nguồn lệch: khoảng 1 tỷ USD (cả gói vũ khí, phụ tùng) so với các số thấp hơn; dùng 1,00 cho gói đầy đủ |
| Hợp đồng và giao hàng Yak-130 | Năm hợp đồng 2019–2020 tùy nguồn; chưa thấy xác nhận đã giao; đánh dấu [~] |
| Năm T-6C đến Việt Nam | Janes/RFA: 11/2024; một nguồn thứ cấp ghi 2023; dùng 2024 |
| Ngày đặt hàng SPYDER | Chưa rõ; chỉ biết 5 hệ thống nhận 2016–2018 |
| Ngày MiG-21 nghỉ hưu | Khoảng 2016–2017 |
| Giá S-300PMU1, SPYDER, Pechora-2TM, và toàn bộ giá 1B ngoài mục [✓] | **Không có nguồn**, là ước tính [?] |
| Đóng quân của các trung đoàn (923 Sao Vàng, 927 Kép, 935 Biên Hòa, 940 Phù Cát) | Có nguồn báo chí quân sự; kiểm lại trước khi dùng tên trong loc |
| Mọi tin 2025–2026 (F-16V, Rafale, Su-57, Yak-130M) | **Chưa xác nhận chính thức**; 1B được thiết kế để không phụ thuộc chúng là sự thật |

---

# PHẦN 13 — CÂU HỎI CẦN CHỐT (mặc định đã gắn; chỉ trả lời khi bạn muốn đổi)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | **ĐÃ CHỐT (có).** Nhánh gồm cả tên lửa phòng không tầm trung/xa và radar (đúng quân chủng PK-KQ) | **Có** | Bỏ T3, D-B, trụ A31, nhánh A; viết lại cấu trúc |
| Q2 | **ĐÃ CHỐT (có).** Ba nhánh học thuyết loại trừ nhau như hải quân | **Có**; AI chỉ đi nhánh A | Cho đi nhiều nhánh: phải hạ giá trị, nâng/giữ trần |
| Q3 | Giữ nhánh C (không người lái, mạng hóa)? | **Có** | Bỏ C: −5 focus, −P9, đơn giản hóa D-E |
| Q4 | **ĐÃ CHỐT (có).** 1B bám tin 2025–2026 (F-16V, Rafale, Su-57E, Yak-130M) | **Có**, ghi rõ là giả định | Đổi bảng dữ liệu của script |
| Q5 | F1 Trục 2 dựng riêng hay treo sau focus luật quốc phòng của hải quân? | **Riêng** | Đổi prerequisite, 1 dòng |
| Q6 | Tiền tố `VIE_air_`, `VIE_airf_`, `VIE_a1b_`; namespace `vie_air_proc` (Trục 1), `vie_air_force`, `vie_a1b`; Trục 2 `VIE_apm_` | **Như 4.3** (Trục 1 đã đổi từ `VIE_air_`/`vie_air` vì trùng roster chỉ huy) | Đổi hàng loạt trước khi code |
| Q7 | Cổng một chiều không quân → Biển Đông ở T8? | **Có** (1 cổng) | Bỏ, hoặc thêm cổng khác |
| Q8 | Trục 2 giữ 5 trụ × 3 bậc? | **Có** | Gộp Tích hợp + UAV (mục 3 của Phần 11) |
| Q9 | Funding Gate: sao chép trigger của hải quân hay gộp thành trigger chung? | **Không sao chép**: Trục 1 không có Funding Gate (xem 5.1); không sửa code hải quân | Gộp: sửa cả hai nhánh, rủi ro hồi quy |
| Q10 | Máy bay thuộc hải quân (tuần tra biển, chống ngầm) có chia sẻ khung máy bay với không quân? | **Không** | Cần thống nhất tech/variant giữa hai nhánh |
| Q11 | Dùng giá ước tính [?] làm mặc định chờ script cân bằng? | **Có** | Đổi một cột bảng |
| Q12 | Không gian/vệ tinh nằm ngoài phạm vi? | **Ngoài** | Thêm nhánh nhỏ riêng |
| Q13 | Phạt thiếu phụ tùng cho đội bay Nga khi SOV không còn tồn tại (alt-history) chỉ qua E17? | **Có** (không có event riêng) | Thêm timed idea tự động theo trạng thái SOV |
| Q14 | Thang modifier và trần ở 7.5 | **Giá trị khởi điểm**, cân bằng bằng script | Đổi số |
| Q15 | **ĐÃ CHỐT (hỗ trợ cả BBA và non-BBA).** Mỗi variant 1B cần hai bản hoặc guard `has_dlc` | **Cả hai** | Khối lượng 1B tăng khoảng 30%; kiểm kỹ chuỗi tech non-BBA (`MR_Fighter`) ở bước 0 |
| Q16 | **ĐÃ CHỐT (Decision), SỬA ở bản 1.4.** Trục 2 giữ bậc bằng biến + Decision như hải quân, và nuôi MIO Viettel có sẵn bằng `add_mio_size` (6.5) | **Decision + `add_mio_size`** | Chuyển hẳn sang MIO: chỉ người có AAT dùng được Trục 2 |

---

# NGUỒN (tra ngày 2026-10-02)

**Mua sắm và đội bay**
- Su-30MK2, Su-27: https://www.airrecognition.com/index.php/news/defense-aviation-news/global-news-2015/august/1931-vietnam-takes-delivery-of-two-more-su-30mk2-multi-role-fighter-jets.html · https://armyrecognition.com/news/aerospace-news/2016/vietnam-took-delivery-of-its-two-final-su-30mk2-multirole-fighter-jets · https://www.globalsecurity.org/military/world/vietnam/su-30mk.htm · https://amti.csis.org/tracking-vietnams-force-build-south-china-sea/
- Hiện đại hóa không quân (Ấn Độ 2000, Yak-52, S-300PMU1, Pechora-2TM, C-295): https://www.globalsecurity.org/military/world/vietnam/airforce-modernization.htm
- Huấn luyện: https://ainonline.com/aviation-news/defense/2017-04-04/vietnams-air-force-shops-new-trainer-jet · https://www.scramble.nl/military-news/vietnam-orders-the-aero-vodochody-l-39ng-jet-trainer · https://scramble.nl/military-news/texan-ii-trainers-for-vietnam-part-2 · https://janes.com/osint-insights/defence-news/industry/update-vietnam-receives-five-t-6c-trainer-aircraft · https://www.globalsecurity.org/military/library/news/2025/03/mil-250307-rfa01.htm
- Trang bị tổng hợp: https://en.wikipedia.org/wiki/List_of_equipment_of_the_Vietnam_People%27s_Air_Force · https://en.wikipedia.org/wiki/Vietnam_Air_Defence_-_Air_Force
- Phòng không, radar: https://news.tuoitre.vn/vietnam-buys-israeli-made-air-defense-missile-system-radar-10326490.htm · https://militarnyi.com/en/news/vietnam-mastered-production-of-key-components-for-soviet-era-air-defense-systems/ · https://raksha-anirveda.com/upgraded-cold-war-era-air-defence-systems-showcased-at-vietnams-first-defence-expo/ · https://baobacninhtv.vn/international-defense-expo-in-hanoi-showcases-world-s-weaponries-postid409722.bbg
- Nhà máy A32: https://baophapluat.vn/nha-may-a32-sang-tao-tang-nien-han-cua-may-bay-phan-luc-chien-dau-post327494.html · https://news.tuoitre.vn/vietnams-factory-a32-achieves-2-breakthroughs-in-fighter-jet-overhaul-capability-103260408171453229.htm · https://baohatinh.vn/viet-nam-tu-sua-chua-may-bay-c-295m-post139172.html
- Đơn vị, MiG-21: https://baonghean.vn/en/su-30mk2-viet-nam-bay-dem-tai-diem-trong-yeu-10129889.html · https://baonghean.vn/en/top-3-chien-dau-co-canh-troi-viet-nam-dip-tet-2017-10126673.html

**Tin chưa xác nhận (1B)**
- F-16: https://www.rfa.org/english/vietnam/2025/04/21/us-f16-fighter-jet-sale/ · https://thediplomat.com/2025/04/vietnam-has-reached-deal-with-us-on-f-16-fighter-purchase-report-claims/
- Rafale, Su-57: https://aviationnews.eu/news/2026/04/vietnam-tests-rafale-fighter-jets-as-france-pushes-major-defense-deal/ · https://meta-defense.fr/en/2026/08/31/vietnam-rafale-fighter-modernization/ · https://defencesecurityasia.com/en/vietnam-rafale-pivot-china-russia-defence-dominance/ · https://nationalinterest.org/blog/buzz/could-this-asian-country-be-next-buyer-dassault-rafale-ps-091926
- Yak-130M: https://www1.ru/en/news/2026/08/05/426639-iak-130m-vyxodit-na-eksport-vetnam-mozet-polucit-18-noveisix-boevyx-samoletov.html

Mọi mục giá ngoài các số có nguồn ở Phần 5 là ước tính của tôi `[?]`.
