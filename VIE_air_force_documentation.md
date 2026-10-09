# Tài liệu Toàn diện Nhánh Không quân (Quân chủng PK-KQ) — Millennium Dawn

> **Tài liệu tổng hợp nghiên cứu, kiến trúc & triển khai (08/10/2026)**  
> Hợp nhất toàn bộ 8 tài liệu phân mảnh của Quân chủng Phòng không – Không quân Việt Nam.

## Hoàn thiện reward chuẩn bị lực lượng v25 (09/10/2026)

Bốn focus sau Cải tổ I từng chỉ thưởng tổng cộng 25 Air XP. Nay reward được tách theo nhiệm vụ; giữ tổng 25 XP, chuyển sang mastery nếu đã chọn học thuyết không quân, giống các reward PK-KQ hiện có.

| Focus | Reward |
|---|---|
| Diễn tập Bắn đạn thật | 10 XP/mastery không quân; 10 command power |
| Huấn luyện GCI và radar | 5 XP/mastery; +0,25% phát hiện máy bay |
| Tổ chức trung đoàn | 5 XP/mastery; 5 command power; −0,5% hệ số chi phí nhân sự không quân |
| Căn cứ không quân dự bị | 5 XP/mastery; +1% phòng thủ không quân trên lãnh thổ |

Bonus lâu dài dùng dynamic modifier `VIE_armed_forces_modifier` và được đưa vào audit cân bằng. Căn cứ dự bị ở đây là chuẩn bị, phân tán và diễn tập chuyển sân tại sân bay hiện có; không xây thêm cấp sân bay. Không cấp máy bay, biên chế mới hay cờ hoàn tất chương trình D1–D4. Bốn prerequisite AND trước Củng cố lực lượng nòng cốt và layout được giữ nguyên. Focus được hoàn tất một lần theo cơ chế cây; không thêm replay reward khi tải save cũ đã hoàn tất focus.

Kiểm tra tĩnh bổ sung đối chiếu từng reward, cả nhánh XP/mastery và 24 thứ tự hoàn thành cho mỗi nhánh. Cần kiểm tra tooltip, mastery và modifier thực tế trong HOI4.

## Mục lục
1. [Phần 1: Kiến trúc theo tầng và Chuẩn hóa Layout PK-KQ v19](#phần-1-kiến-trúc-theo-tầng-và-chuẩn-hóa-layout-pk-kq-v19)
2. [Phần 2: Báo cáo Tổng thể Nội dung nhánh Không quân](#phần-2-báo-cáo-tổng-thể-nội-dung-nhánh-không-quân)
3. [Phần 3: Review & Kế hoạch code Trục 1 (Mua sắm Lịch sử)](#phần-3-review--kế-hoạch-code-trục-1-mua-sắm-lịch-sử)
4. [Phần 4: Review & Kế hoạch code Trục 2 (Công nghiệp Hàng không APM)](#phần-4-review--kế-hoạch-code-trục-2-công-nghiệp-hàng-không-apm)
5. [Phần 5: Review & Kế hoạch code Trục 3 (Xây dựng Lực lượng PK-KQ)](#phần-5-review--kế-hoạch-code-trục-3-xây-dựng-lực-lượng-pk-kq)
6. [Phần 6: Chi tiết Scripted Effects & Kế hoạch Triển khai](#phần-6-chi-tiết-scripted-effects--kế-hoạch-triển-khai)
7. [Phần 7: Nghiên cứu Chỉ huy Quân chủng PK-KQ](#phần-7-nghiên-cứu-chỉ-huy-quân-chủng-pk-kq)
8. [Phần 8: Kế hoạch Triển khai Roster Chỉ huy PK-KQ](#phần-8-kế-hoạch-triển-khai-roster-chỉ-huy-pk-kq)

---
## Phần 1: Kiến trúc theo tầng và Chuẩn hóa Layout PK-KQ v24

# PK-KQ air branch v24 - tiered Y1-Y12 layout

09/10/2026, triển khai trực tiếp trên `main`. Đây là thiết kế hiện hành; các phần nghiên cứu và kế hoạch phía sau giữ làm lịch sử.

**37 PK-KQ focuses**: retain 29 original IDs, three force-structure choices, add three readiness focuses at Y4, and one integrated capstone. The full tree now has 424 focuses; 387 outside the PK-KQ scope retain their AST and coordinates. All four readiness focuses unlock after Command Reform I; First Force requires all four.

## Kiến trúc và bố cục

Shared root at (220,2), Command Reform I at (220,4), four readiness focuses on y=5, and First Force at (220,6). Three mutually exclusive structures sit at (212/220/228,7); Command Reform II and Medium Force at (218/222,8). The three specialty roots are at y=9; specialty components plus Datalink at y=10; tanker at y=11; capstones at y=12; Integrated Force at (220,13). Display Y1 maps to absolute file y=2 because the branch starts below `VIE_modernize_vpa`. Datalink belongs to the UAV column and is a visible prerequisite of Teaming. Multirole requires Command Reform II AND Medium Force. Integrated Force retains the 2/3 capstone gate in `available`.

| Display row | Absolute y | Focuses / gate summary |
|---|---:|---|
| Y1 | 2 | Shared standardization root |
| Y2-Y3 | 3-4 | Fighter + SAM; Command Reform I requires both |
| Y4-Y5 | 5-6 | Four readiness focuses; First Force requires all four |
| Y6-Y7 | 7-8 | Three pairwise mutex structures; Command Reform II + Medium Force |
| Y8-Y10 | 9-11 | SAM, multirole and UAV columns; tanker and Datalink on support row |
| Y11-Y12 | 12-13 | Three specialty capstones; Integrated Force retains the 2/3 gate |

## Quan hệ chuyên ngành

- A1 → **A2 và A3 song song** → A4 cần A2 AND A3. Radar–tên lửa nhiều tầng và tác chiến điện tử là hai chức năng bổ sung; giữ ngưỡng công nghiệp riêng.
- B1 `VIE_airf_multirole` requires Command Reform II AND Medium Force. B2 (fleet), B3 (sustainment), and T8 (operating range) open directly from B1; B5 requires all three. Tanker depends on T8 but is not required for B5.
- C1 opens C2 (ISR), C4 (UCAV), and C3 (Datalink) in the UAV column. C5 `VIE_airf_teaming` requires C2 AND C4 AND C3 as visible prerequisites; `available` still requires B1 `VIE_airf_multirole` and MUM-T readiness. Integrated Force retains its 2/3 capstone, mature-industry, and completed-D4 gates.
- Diễn tập hiệp đồng mở từ Cải cách I; T5 mở sau diễn tập, cần D1/D2 đã hoàn tất và một trụ công nghiệp đã mở. Ba lựa chọn tác chiến chỉ mở sau T5; không có lựa chọn ngân sách trước củng cố.
- T6 và T7 mở từ một trong ba cơ cấu; T6 cần D3 hoàn tất, T7 cần D4 hoàn tất. Riêng B1 cần cả T6 và T7; do đó các năng lực tiêm kích phía sau không thể bỏ qua chỉ huy hoặc biên chế. T8 là con của B1. C3 mở từ T6 và tích hợp công nghiệp.

Quan hệ nội bộ hiện bằng prerequisite. Điều kiện công nghiệp của lực lượng có tooltip tên focus và bậc; không vẽ đường ngang xuyên cụm công nghiệp. Con thấp hơn mọi cha; gap cùng hàng ≥2; anchor thật khai báo trước con.

## Một hàng lựa chọn và ngân sách theo chương trình

Ba cơ cấu loại trừ từng cặp hai chiều, cùng cost 5. Khi chọn, giữ D4 **50 PP + 0,60 tỷ, 360 ngày**; reward và giảm thời gian focus chỉ áp tại event hoàn tất. Phòng không, đa nhiệm và UAV vẫn cùng phát triển. `vie_air_force.30` giữ ID cho save cũ nhưng không đảo lựa chọn khi D4 đã bắt đầu.

Bỏ hệ số ngân sách toàn nhánh 0,8/1,1; không thay bằng một hàng mutex khác hoặc ép tầm xa tương ứng UAV. Người chơi chi tiền theo các option/decision của từng chương trình. Giữ giá cơ sở, giảm giá lịch sử, PP và thời lượng; chỉ trừ treasury một lần, không hoàn tiền các chương trình đã thanh toán.

Bonus 25%, một lần, chuyển từ ba focus ngân sách sang lối vào chuyên ngành tương ứng: A1 nhận SAM, B1 nhận máy bay trung bình, C1 nhận UAV. Mỗi bonus có cờ chống lặp; nếu save v18 đã nhận bonus ngân sách tương ứng thì không cấp lại. Không suy diễn các bonus research cũ khác từ ngày hoặc scheduler.

## D5 chọn rõ một mục tiêu

Ba decision hỗ trợ phòng không / đa nhiệm / UAV dùng chung cờ started/done, nên **toàn lực lượng chỉ thực hiện một D5**. Giữ ID `VIE_airf_d5_capstone` cho mục tiêu phòng không; thêm `VIE_airf_d5_multirole` và `VIE_airf_d5_uav`.

Mỗi decision cần đúng đích chuyên ngành và bậc công nghiệp. Khi bắt đầu, lưu target 1/2/3; mọi lựa chọn khác bị chặn, kể cả đã đạt nhiều đích. Guard complete_effect chống đổi mục tiêu và charge lặp. Giá **60 PP + 1 tỷ**, thời lượng **548 ngày**; thưởng MIS và một chỉ số chuyên ngành **0,5 hoặc 1 điểm phần trăm**, giữ mức cũ. Mức cao cần tích hợp bậc 3 cùng radar/A32/UAV bậc 3 theo mục tiêu.

AI lịch sử giữ cơ cấu phòng thủ, các ngày lịch sử và hạn chế UAV giả định. D5 ưu tiên phòng không cho cơ cấu phòng thủ, đa nhiệm cho cân bằng/tầm xa nhưng vẫn có phương án đủ điều kiện khác; không khóa người chơi bằng trọng số AI. Không sửa AI chính trị hoặc `VIE_ai_historical`.

## Reward, điều kiện và save

Giữ các modifier, XP/mastery, PP, CP và bonus cũ của v18 ngoài ba bonus chuyển vị trí. Toàn bộ ba cụm cùng phát triển vẫn trong trần: mission 16/16, detection 19,5/20, interception 7,75/8, ace 9,5/10. Đích hiệp đồng cost 7 vẫn thưởng 20 XP/mastery, 50 PP, 3% war support, không thêm buff chiến đấu thường trực.

D1–D4, stages D3 và các bậc công nghiệp vẫn đọc kết quả hoàn tất thật, có guard chống lặp và slot/pending/running. Giữ đường A32 C-295 độc lập số Su-30, fallback A31 tự phát triển, radar/tích hợp/UAV nối bậc theo năng lực. Không dùng ngày hoặc scheduler làm bằng chứng hoàn tất.

Save mới là chuẩn. Giữ 29 ID gốc, ba cơ cấu và các event cũ; ba ID ngân sách mới của v18 bị bỏ theo thiết kế này. Không hoàn nguyên buff/chi phí đã nhận. Programme đang chạy từ phiên bản cũ không tự được xác nhận bằng focus hoặc ngày; bonus legacy chỉ được nhận diện từ lựa chọn đã lưu. Tên focus mới và đích được đặt trong file localisation PK-KQ hiện hữu, mỗi key một định nghĩa, UTF-8 BOM; cần khởi động lại HOI4 để kiểm bản đang nạp.

## Bàn giao và nghiệm thu

- [Sơ đồ v18 trước sửa](.claude/docs/air/air_v18_before.png), [sơ đồ v19](.claude/docs/air/air_after.png), [Diagram.net XML không nén](.claude/docs/air/air_redesign.drawio).
- [Quan hệ/reward trước–sau](.claude/docs/air/air_changes.md), [kiểm định và cảnh báo](.claude/docs/air/validation.md).
- Xuất lại: `python tools/focus_layout/air_diagram.py`; fixture: `python tools/audit/air_scenarios.py`.

**Chưa nghiệm thu trong HOI4.** Diagram và fixture Python không chứng minh routing, hover, designer/DLC, thời lượng engine hoặc AI. Checklist ở `tools/TESTING.md`; chỉ xác nhận runtime sau khi mở cây, chạy chương trình và đọc `error.log` của phiên mới.

---
## Phần 2: Báo cáo Tổng thể Nội dung nhánh Không quân

# BÁO CÁO NỘI DUNG NHÁNH KHÔNG QUÂN (QUÂN CHỦNG PHÒNG KHÔNG – KHÔNG QUÂN) · VIE · MILLENNIUM DAWN

> **Ghi chú lịch sử PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản v18 có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


> Bản 1.5 · 2026-10-03 · **Trục 1 và 2 đã code; Trục 3 và 1B chỉ có thiết kế.**
> Bản 1.5 sửa Trục 3 (Phần 7, 3.1 R9, 4.3; chi tiết, tọa độ, ngân sách modifier và plan code ở `VIE_air_truc3_review_and_plan.md`): T5 đòi một trong ba focus Trục 2 và có dự phòng theo ngày; D-E mức 1 chỉ đọc Trục 1–2; "phòng không" = `air_home_defence_factor`, "phòng thủ" = `air_intercept_efficiency`, Trục 3 không dùng `air_defence_factor`; phát hiện hạ về 4,5–8,5%; category `VIE_airf_category` (priority 86); bỏ phần thưởng mở 1B; cột focus x 290–322.
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
| R9 | Bộ đếm slot (Trục 3: tối đa 2; 1B: tối đa 2; Trục 2: tối đa 2) tự chữa hàng tháng theo timed idea và cờ chờ (không còn hook nội chiến) |
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
| `VIE_airf_d1_done`, `VIE_airf_d2_done` | cờ | event ẩn hoàn tất D-A, D-B | D-C |
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

Hải quân chiếm x ≈ 216–262; lục quân x ≈ 272–284. Đề xuất cột không quân đặt **x ≥ 290** (bản 1.5: Trục 2 ở x 290–296, Trục 3 ở x 290–322, y 2–12, đã kiểm trống; xem `VIE_air_truc3_review_and_plan.md` 4.1) (bên phải lục quân) hoặc **x ≤ 200** (bên trái hải quân), chia theo trục: Trục 2 ở cột gần root, Trục 3 ở cột riêng, giữ khoảng cách cùng hàng ≥ 4 ô và con luôn `y >` cha. `[?]` chưa đo.

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
| T5 | `VIE_airf_first_force` | Cơ cấu lực lượng ban đầu | T4 **và** một trong `VIE_apm_a32`, `VIE_apm_a31`, `VIE_apm_radar` | `date > 2011.12.31`; `OR = { VIE_var_air_delivered > 11, date > 2014.12.31 }` (đường lịch sử: 4 + 8 = 12 vào 2011; dự phòng khi Su-30 không giao) |
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

## 7.2 Phần thưởng focus (chỉ XP, modifier; sửa ở bản 1.5, không còn `unlock_decision_tooltip` tới 1B vì 1B chưa tồn tại)

Ký hiệu token: EXP `experience_gain_air_factor`, ATK `air_attack_factor`, SUP `air_superiority_efficiency`, CAS `air_cas_efficiency`, MIS `air_mission_efficiency`, RNG `air_range_factor`, DET `air_detection`, HOME `air_home_defence_factor` ("phòng không"), INT `air_intercept_efficiency` ("phòng thủ"), PERS `airforce_personnel_cost_multiplier_modifier`.

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP +15; EXP +4% | category Trục 3 |
| T2 | ATK +1% | D-A |
| T3 | HOME +2% | D-B |
| T4 | MIS +2% | D-C |
| T5 | XP +10 | D-D |
| T6 | MIS +2%, DET +1% | — |
| T7 | RNG +3% | — (1B đọc `has_completed_focus` khi dựng) |
| T8 | RNG +4%, DET +1% | ba nhánh |
| A1–A4 | A1 HOME +2%; A2 DET +2%, HOME +2%; A3 INT +3%, DET +2%; A4 MIS +2%, HOME +2% (thưởng gốc; D-E cộng thêm 25% / 50%) | A4: D-E |
| B1–B5 | B1 RNG +4%; B2 ATK +3%, SUP +2%, CAS +2%; B3 MIS +2%; B4 RNG +3%; B5 MIS +2%, ATK +2% (thưởng gốc; D-E cộng thêm 25% / 50%) | B5: D-E |
| C1–C5 | C1 DET +1%; C2 DET +3%; C3 MIS +2%; C4 ATK +3%; C5 MIS +2%, INT +2% (thưởng gốc; D-E cộng thêm 25% / 50%) | C5: D-E |

(Mức lệch nhánh và đúng nhánh: xem 7.4.)

## 7.3 Năm Decision lực lượng (category `VIE_airf_category`, priority 86, `allowed = original_tag = VIE`)

Mỗi Decision: `fire_only_once`, chi phí 50 PP (D-E 60 PP), cổng ở lúc bấm (không có trạng thái "chờ"), chuỗi chọn là event nối tiếp (miễn `VIE_popup_cd`), hoàn tất bằng event ẩn; slot `VIE_var_airf_program_active < 2`.

| Decision | Mở từ | Chuỗi chọn | Hoàn tất |
|---|---|---|---|
| D-A `VIE_airf_d1_fighters` | T2 | Mức: **Cơ bản** 0,40 tỷ / 12 tháng; **Chuyên sâu** 0,60 / 18 tháng. Chuyên môn: **Không chiến** hoặc **Tấn công mặt đất/mặt biển** | Đặt mức, chuyên môn, modifier theo 7.5, `VIE_airf_d1_done` |
| D-B `VIE_airf_d2_sam` | T3 | Định hướng: **Lịch sử** 0,30 (nâng cấp S-125, S-75 tại A31) hoặc **Sớm** 0,50 (đưa hệ thống mới vào biên chế ngay, thưởng đầu cao hơn). Mức Cơ bản/Chuyên sâu (×1,0/×1,5). | `VIE_airf_d2_done`, modifier |
| D-C `VIE_airf_d3_coordination` | T4 | Không có lựa chọn: 0,50 tỷ / 18 tháng, **đòi `d1_done` và `d2_done`**. Ba giai đoạn ẩn: (1) XP và hiệu suất nhiệm vụ; (2) phối hợp tiêm kích – tên lửa; (3) bức tranh trên không tích hợp | `VIE_airf_d3_done` |
| D-D `VIE_airf_d4_first_force` | T5 | Ba cơ cấu: **1 Phòng thủ lãnh thổ**, **2 Cân bằng**, **3 Tầm xa**. 0,60 tỷ / 12 tháng. Đặt `VIE_airf_force_priority` | modifier |
| D-E `VIE_airf_d5_capstone` | A4, B5 hoặc C5 | 1,0 tỷ / 18 tháng. Cổng **mức 1** (chỉ Trục 1–2): **A** (`VIE_var_sam_lr ≥ 1` hoặc `VIE_apm_a31_tier ≥ 2`) và `VIE_apm_radar_tier ≥ 2`; **B** `VIE_var_air_delivered ≥ 24` và `VIE_apm_a32_tier ≥ 2`; **C** `VIE_apm_uav_tier ≥ 2`. **Mức 2** (đọc 1B, chỉ để cộng thưởng): A `VIE_var_sam_lr ≥ 3` (S-300 của Trục 1 đã cho 2), B `VIE_var_air_multirole4 ≥ 12`, C `VIE_var_uav_delivered ≥ 4` | Cộng thêm +25% (mức 1) hoặc +50% (mức 2) thưởng gốc của focus capstone, như hải quân |

Chi phí D-A đến D-D khoảng 1,8 tỷ (mọi mức Cơ bản, D-B Lịch sử) đến 2,45 tỷ (mọi mức Chuyên sâu, D-B Sớm), cộng D-E 1,0 tỷ. Tổng đối xứng với hải quân.

## 7.4 Lệch nhánh và đúng nhánh (đối xứng, nhỏ)

- Cơ cấu D-D ở mức 1 (Phòng thủ lãnh thổ) hợp với nhánh A; mức 2 (Cân bằng) hợp mọi nhánh; mức 3 (Tầm xa) hợp nhánh B và C.
- **Lệch nhánh** khi mở A1/B1/C1: timed idea 365 ngày, hiệu suất nhiệm vụ −3%, phát hiện −3%. **Đúng nhánh**: +1% hiệu suất nhiệm vụ.
- Mức chuyên môn (D-A) là lựa chọn một lần. Hướng còn lại được bù một phần bởi giai đoạn 2 của D-C (phối hợp tiêm kích – tên lửa).

## 7.5 Bảng modifier (giá trị khởi điểm, sửa ở bản 1.5)

| Nguồn | Hiệu ứng (+ là bonus) |
|---|---|
| D-A mức 1/2 × Không chiến | SUP +3% / +4,5% |
| D-A mức 1/2 × Tấn công đất/biển | CAS +3% / +4,5%; ATK +1% / +1,5% |
| D-B mức 1/2 | HOME +3% / +4,5%; DET +1% / +1,5% (Sớm: HOME +1% thêm) |
| D-C (ba giai đoạn) | MIS +2%; HOME +2%, SUP +2%; DET +1%, MIS +2% |
| D-D Phòng thủ | INT +3%, HOME +2%, RNG −3% |
| D-D Cân bằng | ATK +1%, INT +1%, RNG +1% |
| D-D Tầm xa | RNG +5%, MIS +2%; PERS +3% (token `airforce_personnel_cost_multiplier_modifier`, đã xác nhận) |

**Token đã đối chiếu** (`modifiers_documentation.md`, `money_modifier_definitions.txt`, 2026-10-03): `experience_gain_air_factor`, `air_attack_factor`, `air_superiority_efficiency`, `air_cas_efficiency`, `air_mission_efficiency`, `air_range_factor`, `air_detection`, `air_home_defence_factor`, `air_intercept_efficiency`, `airforce_personnel_cost_multiplier_modifier`. `air_attack_factor` và PERS cần thêm vào `VIE_armed_forces_modifier`. **Trục 3 không dùng `air_defence_factor`** (đã có 0,18 từ Trục 1, Trục 2, lục quân). Không dùng `air_agility_factor` vì MD đã đổi "Agility" thành "Radar Advantage".

**Trần là tổng cả ba trục vì biến dùng chung** (script cân bằng cộng chéo): EXP ≤ 10%, ATK ≤ 10%, SUP ≤ 10%, CAS ≤ 10%, MIS ≤ 16%, RNG ≤ 20%, **DET ≤ 20% (Trục 1 + 2 đã chiếm 11%, Trục 3 còn 9%)**, HOME ≤ 20%, INT ≤ 8%, `air_defence_factor` ≤ 20%. Tổng lớn nhất của Trục 3 (nhánh A / B / C, mức hai, D-E +50%): DET 8,5 / 4,5 / 8,5; HOME 18,5 / 11,5 / 11,5; RNG 12 / 19 / 12; MIS 13 / 15 / 16; ATK 3,5 / 9,5 / 6,5. Mọi tổ hợp dưới trần. Nếu script báo vượt thì hạ giá trị chứ không nâng trần (như hải quân đã làm).

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
| Focus Trục 3 | `ai_will_do` base 60 cho chuỗi chung; A1 = 40; B1 và C1 `factor = 0 VIE_ai_historical = yes` (bản 1.5: `VIE_ai_free` chưa định nghĩa, dùng mẫu Trục 2/hải quân; AI chỉ đi nhánh A); `factor = 0` khi `bankruptcy_incoming_collapse` |
| Decision lực lượng | base 100, `factor = 0` khi `bankruptcy_incoming_collapse`; option lịch sử `base 90` + `add 100` nếu `VIE_ai_historical`; option khác `factor 0 VIE_ai_historical = yes`, có guard tài chính (`bankruptcy_incoming_collapse`, `ai_has_high_deficit`) |
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

---

## Phần 3: Review & Kế hoạch code Trục 1 (Mua sắm Lịch sử)

# REVIEW TRỤC 1 KHÔNG QUÂN (MUA SẮM LỊCH SỬ) + PLAN CODE

> Đầu vào: `VIE_air_force_content_report.md` bản 1.2, Phần 5 (Trục 1) và các chỗ Trục 1 chạm tới (4.2, 4.3, 8.2, 9, 12, 13).
> Đối chiếu với: repo @ `e4f3215`; MD v2.0.0 cài trên máy (`workshop/content/394360/2777392649`: `history/countries`, `history/units`, `common/technologies/missile_defense.txt`, `common/units/equipment/MD_sam_missile.txt`, `common/national_focus/05_algeria.txt`, `Changelog.txt`); mẫu code Trục 1 lục quân (`VIE_md_effects_p14.txt`) và hải quân (`VIE_md_effects_naval.txt`, `VIE_naval_truc1_review_and_plan.md`).
> Phạm vi: chỉ Trục 1. Trục 2, Trục 3, 1B chỉ nhắc khi Trục 1 phải nối vào.
>
> **KẾT LUẬN: logic cốt lõi (cửa sổ + thử lại hằng tháng, lựa chọn lịch sử là mặc định, dữ kiện lịch sử, tổng chi ≈ 3,9 tỷ) ĐÚNG và giữ nguyên.
> Nhưng bản 1.2 chưa code được: 5 lỗi chặn (Phần 1), 7 chỗ không khớp game/mod (Phần 2).**
> Báo cáo gốc đã được sửa theo Phần 3 (bản 1.3, Phần 5 viết lại). Phần 4 là plan code, Phần 6 là các quyết định cần bạn chốt (mỗi dòng có mặc định).

---

# PHẦN 1 — 5 LỖI CHẶN

## A1 · Mã quốc gia sai: `IND` là Indonesia, `ESP` không tồn tại

Đếm từ `history/countries` của MD:

| Báo cáo dùng | Thực tế trong MD | Hệ quả |
|---|---|---|
| `IND` cho Ấn Độ (E1, E13) | `IND - Indonesia.txt`; Ấn Độ là **`RAJ`** | Cổng `country_exists = IND` luôn đúng nhưng **trỏ nhầm nước**; `producer`/opinion cũng nhầm |
| `ESP` cho Tây Ban Nha (E8, P6) | **`SPR`** | `country_exists = ESP` sai tag, engine bỏ im lặng hoặc báo lỗi |

Các tag còn lại đúng: `SOV`, `ROM`, `BLR`, `CZE`, `ISR`, `USA`, `FRA`, `SWE`. Mod đã dùng `RAJ` đúng cho Ấn Độ (`events/VIE_def_ind.txt:43`).

## A2 · Tiền tố và tên đã bị roster chỉ huy không quân (đã code 01/10) chiếm

Mục 4.3 báo cáo nói "phải grep 0 kết quả"; thực tế **không phải 0**:

| Thứ báo cáo định dùng | Đã có trong repo |
|---|---|
| tiền tố `VIE_air_` | 20 character `VIE_air_<tên>` (`VIE_md_air_commanders.txt`), cờ `VIE_air_phase0_done`, `VIE_air_step_1…7`, idea `VIE_air_dominance_idea` |
| scheduler `VIE_event_scheduler_air` (suy ra từ nhóm tên) | **đã có**, là scheduler *chỉ huy* (`VIE_md_effects_air.txt`), đã gọi trong `on_monthly` |
| file `VIE_md_effects_air.txt` | đã có (chỉ huy) |
| namespace `vie_air` | trống, nhưng `vie_air_commanders` đã được kế hoạch roster giữ chỗ làm phương án dự phòng |

Nếu code Trục 1 vào đúng tên cũ, scripted effect trùng tên **ghi đè** chứ không gộp (cùng lý do mod không dùng `trigger_year_*`), làm mất scheduler chỉ huy.
**Sửa:** namespace **`vie_air_proc`** (khớp `vie_proc_army`), scheduler `VIE_event_scheduler_air_proc`, tiền tố cờ/biến **`VIE_ap_`** (grep 0 kết quả, đã kiểm), file `VIE_md_effects_air_proc.txt` / `VIE_md_triggers_air_proc.txt` / `events/VIE_air_proc.txt` / `VIE_md_ideas_air_proc.txt`. Biến đếm dùng chung giữ `VIE_var_air_delivered` (grep 0, T5 của Trục 3 đọc). Trục 2 và 1B giữ `VIE_air_`… **không dùng**; cần chọn tiền tố khác khi tới lượt (đề xuất `VIE_apm_` và `VIE_a1b_`); ghi vào 4.3.

## A3 · Nhánh tên lửa phòng không (SAM) của MD chỉ tồn tại khi có DLC Götterdämmerung

Đọc `missile_defense.txt`: tech `SAM` có `allow_branch = { has_dlc = "Gotterdammerung" }`. `VIE - Vietnam.txt` chỉ cấp `SAM`, `SAM0` và kho `sam_missile_equipment_1` ×280 (S-125/S-75) **trong nhánh `has_dlc = "Gotterdammerung"`**. Báo cáo 12.2 mục 4 nói "Việt Nam được cấp sẵn tech SAM/SAM0" mà không nêu điều kiện DLC, và Q15 chỉ chốt BBA/non-BBA, không có GOT.

Hệ quả cho E2, E7, E10 (cả ba là SAM):
- Có GOT: `set_technology` chuỗi tới bậc cần (tech `SAM1` → `SAM2`…, mỗi bậc đòi bậc trước) rồi `add_equipment_to_stockpile` loại `sam_missile_equipment_N`. Tiền lệ MD: **S-300P/PMU = `sam_missile_equipment_3`** (Slovakia, Ukraine); S-125 = `_1`. Bậc tech theo năm: SAM0 1965→`_1`, SAM1 1975→`_2`, SAM2 1985→`_3`, SAM3 1995→`_4`, SAM4 2005→`_5`.
- Không có GOT: không có thiết bị SAM nào để cấp. Chỉ còn timed idea + `VIE_af_air_defence_factor` (đúng quy ước mod: MANPADS Igla cũng "tác dụng nằm ở modifier").

Mục 5.1 báo cáo ("làm trên hệ tên lửa của MD") đúng về hướng nhưng thiếu nhánh không-GOT. Thêm vào Q15: **ba nhánh DLC**: BBA (máy bay), GOT (SAM), và NSB không liên quan Trục 1 không quân.

## A4 · Chưa có ánh xạ từ mỗi sự kiện sang trang bị thật của MD

Báo cáo Phần 9 bàn variant cho 1B nhưng Trục 1 chỉ ghi "cấp máy bay…". Đối chiếu MD cho từng thứ (xem bảng đầy đủ ở 3.2):

- **Cách cấp đã có tiền lệ MD, không cần chép module:** `add_equipment_to_stockpile = { type variant_name amount producer }` với `has_dlc = "By Blood Alone"` / `else` dùng loại non-BBA. MD tự dùng đúng mẫu này (focus `ALG_purchase_russian_su30`: `medium_plane_airframe_2` + `variant_name = "Su-30MKI"`, `else` `MR_Fighter2`; trừ tiền `treasury_change` + `modify_treasury_effect`). Hệ quả: Phần 9 ("chép module từ MD") **chỉ cần cho 1B**, Trục 1 không phải tạo variant, trừ T-6C và L-39NG.
- **Variant có sẵn trong MD:** SOV `"Su-30"` (`medium_plane_airframe_2`), SOV `"Yak-130"` (`small_plane_strike_airframe_2`), SPR `"Airbus C-295"` (`large_plane_air_transport_airframe_2`), CZE `"Aero L-39"` (`small_plane_strike_airframe_1`).
- **Không có:** T-6C (USA), L-39NG (CZE), Yak-52 (ROM); MD không có loại thiết bị cho tiêu kích huấn luyện cơ bản piston.
- Loại non-BBA tương ứng: Su-30 → `AS_Fighter2` (đã chốt, khớp CHI và `vie_dip.16`; ALG/RAJ dùng `MR_Fighter2` nhưng không theo); trainer → `L_Strike_fighter2` (L-39, T-6 của CAN); C-295 → `transport_plane3`.
- **Không có "vũ khí cấp kèm" cho máy bay:** vũ khí là module trong variant, không phải kho đạn. E5 "8 chiếc không kèm vũ khí" / "kèm vũ khí" không có hiệu ứng nào nếu chỉ cấp thiết bị (xem B3).

## A5 · Cách chạy sự kiện không theo kiến trúc đã dùng trong mod

Mục 5.1 mô tả "thử lại hằng tháng, hết cửa sổ thì lỡ hẹn" và 5.3 có sự kiện ẩn giao hàng và 4 sự kiện Funding Gate. Mod đã có hai tiền lệ (p13/p14 lục quân, naval) và review hải quân đã sửa đúng các lỗi này:

| Báo cáo 1.2 | Mod / review hải quân | Sửa |
|---|---|---|
| Hết cửa sổ ⇒ "lỡ hẹn" | Class B: popup chỉ bị `VIE_popup_cd` chặn tới hết cửa sổ ⇒ **áp dụng kết quả lịch sử im lặng** (`VIE_fb_*`); `_missed` chỉ khi **cổng không bao giờ đạt** | Theo mod (naval B5) |
| Không nhắc `VIE_catch_up` | Mọi scheduler có nhánh catch-up (nội chiến xong, người thắng chỉ nhận cờ "đã xảy ra", không popup, không máy bay); `VIE_catch_up_schedule` (`VIE_md_effects_p3.txt:15`) phải gọi scheduler mới | Thêm |
| Không nhắc `on_monthly_VIE` | Dùng `on_monthly` chung với `original_tag = VIE`, vì người thắng nội chiến có thể là tag nổi loạn; MD đã có `on_monthly_VIE` riêng (bắn `vietnam.1`) | Theo mod |
| `vie_air.50` sự kiện ẩn giao hàng, `vie_air.51` lỡ hẹn | Giao hàng là **Class C** trong scheduler, một cờ cho mỗi đợt (`VIE_ap_<p>_dN`), không event | Bỏ `.50`; `.51` thành thông báo nhỏ |
| Funding Gate cho cả 17 sự kiện (`.40–.43`) | Lựa chọn lịch sử **luôn có** (R1); MD tự phát hành nợ khi thiếu tiền; Funding Gate chỉ ở lựa chọn *ngoài lịch sử* (Sigma). Ngân khố VIE lúc đầu là 5 tỷ, nên chi 1,0 tỷ cho E6 là hợp lệ | Bỏ `.40–.43`; chỉ lựa chọn "mở rộng" mới có `trigger` ngân khố, tooltip rõ (xem 3.3) |

---

# PHẦN 2 — 7 CHỖ KHÔNG KHỚP GAME/MOD

## B1 · Bước ngoặt vòng phụ thuộc: E7 và E17 đọc ngược chiều R11

R11 của báo cáo: Trục 1 → Trục 2 → {Trục 3, 1B}; cạnh ngược chỉ được **cộng thưởng**, không gate. Nhưng:
- **E7 lựa chọn C** ("để A31 tự làm") đòi `VIE_var_a31_tier ≥ 1`, trong khi A31 bậc 1 của Trục 2 *chính là* "Pechora-2TM (2009–2011)" (6.3). Vừa vòng, vừa trả hai lần cho một sự kiện lịch sử.
- **E17** đọc `VIE_var_a32_tier = 3` để *không kích hoạt*: Trục 1 gate bằng trạng thái Trục 2 (ngược chiều), và nguồn là [~] (tin Nga ngần ngại), trái R1 ("Trục 1 chỉ chứa việc đã xảy ra").
**Sửa:** E7 bỏ lựa chọn C; Trục 2 A31 bậc 1 sau này *đọc* cờ kết quả `VIE_ap_pechora_scope` để giảm giá/thời gian (cạnh thưởng hợp lệ). **E17 chuyển sang 1B** (Decision, cạnh tranh nguồn hỗ trợ Nga/phương Tây), không còn thuộc Trục 1 (Phần 6, Q-A2). Trục 1 còn **16 sự kiện**.

## B2 · Exp cộng vào Trục 2 chưa có người đọc

E7 (exp A31 +25/+40), E11-C (exp radar +30), E17-B (exp A32 +40) ghi vào một biến "exp" mà Trục 2 chưa có; đó đúng là loại biến phản chiếu mà R3 cấm. Mục 5.1 gợi ý "helper kiểu `VIE_nav_add_*_exp`": các helper này có thật (`VIE_md_effects_nav_ind.txt:34-51`) nhưng là của Trục 2 *hải quân*; Trục 2 không quân chưa tồn tại nên không có nơi nhận.
**Sửa:** Trục 1 **không ghi exp**. Nó ghi *cờ kết quả* (`VIE_ap_pechora_scope` 1/2, `VIE_ap_radar_viettel_fast`), Trục 2 đọc khi dựng. Trong khi chờ, các cờ này nằm trong danh sách "đặt trước, chưa ai đọc" trong `VIE_v9_flag_mapping.md` (mẫu của `VIE_cap_ba_son_yard` ở hải quân).

## B3 · Bốn sự kiện có nội dung game không thể hiện được

| Sự kiện | Vấn đề | Cách làm trong game |
|---|---|---|
| E5 "không kèm vũ khí / kèm vũ khí" | Không có kho đạn máy bay | A (lịch sử): cờ `VIE_ap_su30_no_munitions` + timed idea −X% hiệu suất nhiệm vụ tới khi E6 chốt; B: +0,12 tỷ, không idea |
| E12 MiG-21 nghỉ hưu | `destroy_equipment` chưa được xác minh ở MD (0 lần dùng), mod cũng từ chối dùng (`VIE_md_effects_p14.txt:95-103`); MiG-21 của VIE nằm trong air wing | Không loại thiết bị. Chỉ gỡ timed idea của E1, thêm hiệu ứng XP/chi phí; cấp quyền Trục 3 đọc cờ |
| E4 Yak-52 | Không có thiết bị tiêm kích huấn luyện cơ bản trong MD | Chỉ XP + timed idea đào tạo cơ bản; bỏ "cấp trang bị huấn luyện" |
| E11 VERA-NG ×4 | Helper `one_state_radar_station` tự trừ **1,75 tỷ mỗi trạm** (đặt `skip_payment = 1` để bỏ), gấp ~30 lần giá 0,06 của báo cáo | Chỉ cộng `VIE_af_air_detection` (modifier); không xây công trình radar trong Trục 1 |

## B4 · E14 và E16 cùng mua L-39NG

E14-B "L-39NG ×12, 0,12" và E16-A "L-39NG ×12, 0,12" là cùng một đơn hàng; chọn B rồi A ra 24 chiếc; chọn C (cả hai) cũng vậy. Lịch sử: L-39NG chỉ đặt một lần (2021, 12 chiếc), còn Yak-130 là [~] (chưa xác nhận hợp đồng/giao).
**Sửa:** E14 chỉ còn **Yak-130** (A mua 12 / B từ chối / C hoãn); L-39NG chỉ ở E16. Lựa chọn E14-B đặt `VIE_ap_yak130_declined`; E16 khi có cờ này có thêm tùy chọn mở rộng 18 chiếc (Funding Gate nhỏ). Tổng chi bỏ 0,12 trùng.

## B5 · Ngân sách pop-up viết sai

Mục 5.4: "17 sự kiện, dưới 1 pop-up mỗi năm… cao điểm 2009–2013 đúng ngân sách". Số đo của repo (`tools/TESTING.md`, "Balance sanity"): **các năm đã vượt 5 trước khi thêm không quân: 2003=6, 2008=6, 2012=8, 2014=8, 2018=6, 2020=6, 2021=12, 2022=6, 2023=6, 2024=7**, hải quân thêm vào 2003, 2006, 2009, 2011. Mục tiêu hiện hành: **≤ 7 mỗi năm**, không có code ép. Báo cáo không đọc số này.
**Sửa:** xếp lại cửa sổ (E2/E3 đầu 2004 thay 2003, E8/E9 sang 2013 thay 2012, E15 sang 2022.1 thay 2021.6), hạ E1/E4/E12/E16 xuống **Class C** (không popup). Bảng đếm theo năm ở 3.4.

## B6 · Tồn dư `vie_dip.16` chồng lên 1B P2

`events/VIE_md_p7.txt` còn event `vie_dip.16` "Ai cấp tiêm kích mới?" (Su-30SM của SOV hoặc Gripen), được mở bởi focus `VIE_fighter_replacement` đã xóa ở v9. Không ai kích hoạt nó (đã grep). Nó dùng `AS_Fighter2` cho Su-30, khác tiền lệ `MR_Fighter2` của MD (ALG, RAJ). Không chặn Trục 1; ghi chú để **1B P2 thay hẳn event này** (xóa khi làm 1B), và Q-A3 chốt loại non-BBA cho Su-30.

## B7 · Cạnh ngược E15 tham chiếu focus chưa có

E15 giảm giá nếu `has_completed_focus = VIE_airf_training_standardization`. Focus này thuộc Trục 3 (chưa tồn tại); `live.py` sẽ báo tham chiếu focus treo. Làm đúng mẫu naval 3.8: một scripted trigger `VIE_ap_training_standardized = { always = no }` trong file gate, đổi một dòng khi Trục 3 có focus thật.

---

# PHẦN 3 — TRỤC 1 SAU KHI SỬA

## 3.1 Quy ước (thay cho 5.1 cũ; bản 1.3 của báo cáo đã cập nhật)

- Scheduler `VIE_event_scheduler_air_proc`, gọi từ `on_monthly` (khối có `original_tag = VIE`) **và** `VIE_catch_up_schedule`. Mẫu p13/naval:

```
catch-up                         -> chỉ đặt cờ "đã xảy ra", không popup, không máy bay
cổng đạt + popup_cd trống        -> đặt _offered + popup_cd 45 ngày + fire event
cổng đạt + popup_cd bận          -> đặt _gate_seen, thử lại tháng sau
hết cửa sổ + _gate_seen          -> VIE_fb_ap_<p> (kết quả lịch sử, im lặng)
hết cửa sổ, cổng chưa từng đạt   -> _missed (tin nhắn nhỏ, 1B đọc cờ)
Class C (E4, E12, E16)           -> áp dụng thẳng kết quả lịch sử khi vào cửa sổ, không popup
giao hàng                        -> Class C, cờ VIE_ap_<p>_dN mỗi đợt
```

- Cổng đối tác chỉ gồm `country_exists` và `NOT = { has_war_with }` (R1), gom vào file triggers: `VIE_ap_gate_sov`, `_raj`, `_rom`, `_blr`, `_spr`, `_isr`, `_cze`, `_usa`.
- Tiền: `set_temp_variable = { treasury_change = -X } modify_treasury_effect = yes` (tỷ USD, như MD và Trục 1 lục quân). Từ 0,4 tỷ trở lên chia ngân khố/nợ như T-90 (`modify_debt_effect`); đề xuất: E5 0,40 / E6 1,00 / E9 0,60 trả 60% ngân khố + 40% nợ. Giá có nguồn [✓] giữ nguyên báo cáo; giá [?] ghi `TODO(giá)`.
- AI: option lịch sử là mặc định (`ai_chance`), mọi option phải chọn được (bài học zero-weight).
- Trục 1 chỉ cộng `VIE_var_air_delivered` (máy bay chiến đấu Su-30 giao) và `VIE_var_sam_lr`; không ghi bậc/exp Trục 2 (R11, B2).

## 3.2 Ánh xạ trang bị (BBA / non-BBA / GOT)

Cách viết chung: `has_dlc = "By Blood Alone"` ⇒ loại BBA + `variant_name` + `producer`; `else` ⇒ loại non-BBA (mẫu `05_algeria.txt`). Số lượng giữ 1:1 giữa hai nhánh ở bản đầu (`TODO(balance)`: MD tự lệch, ví dụ ALG Su-30 72 so với 40).

| Sự kiện | BBA (loại / variant / producer) | non-BBA | GOT | Ghi chú |
|---|---|---|---|---|
| E1 hợp tác Ấn Độ (RAJ) | — | — | — | Timed idea `VIE_ap_mig21_extension_idea` + XP; không thiết bị |
| E2 S-300PMU1 (SOV) | — | — | **có**: `set_technology` SAM1+SAM2; `sam_missile_equipment_3` ×~60/tiểu đoàn, `producer = SOV`; **không**: chỉ idea | `VIE_var_sam_lr` +2 (A) / +1 (B) luôn tăng (đếm, không phụ thuộc kho); `VIE_af_air_defence_factor` +0,02 / +0,01 |
| E3, E5, E6, E9 Su-30MK2 (SOV) | `medium_plane_airframe_2`, `"Su-30"`, SOV | `AS_Fighter2` (Q-A3 đã chốt), SOV | — | `VIE_var_air_delivered` mỗi đợt; E5/E6 có idea (B3) |
| E4 Yak-52 (ROM) | — | — | — | Chỉ XP + idea |
| E7 Pechora-2TM (BLR) | — | — | **có**: tech SAM1; `sam_missile_equipment_2` ×N, `producer = BLR` | Bỏ lựa chọn C (B1); đặt `VIE_ap_pechora_scope` |
| E8 C-295M (SPR) | `large_plane_air_transport_airframe_2`, `"Airbus C-295"`, SPR | `transport_plane3`, SPR | — | |
| E10 SPYDER (ISR) | — | — | **có**: `sam_missile_equipment_2` (TODO bậc), `producer = ISR`; SPAA lục quân `SP_Anti_Air_2` **không** cấp (thuộc lục quân) | Không cộng `VIE_var_sam_lr` (chỉ S-300 tầm xa) |
| E11 radar (CZE/ISR) | — | — | — | Chỉ `VIE_af_air_detection` (B3) |
| E12 MiG-21 nghỉ hưu | — | — | — | Không loại thiết bị (B3) |
| E13 đào tạo (RAJ) | — | — | — | XP + timed idea 36 tháng |
| E14 Yak-130 (SOV) | `small_plane_strike_airframe_2`, `"Yak-130"`, SOV | `L_Strike_fighter2`, SOV | — | Đã xác nhận mua 12 chiếc (bạn xác nhận); năm hợp đồng/giao chưa rõ |
| E15 T-6C (USA) | `small_plane_strike_airframe_1`, **không có variant USA**: thử không `variant_name`; dự phòng `"Aero L-39"` CZE (T4) | `L_Strike_fighter2`, USA | — | Rủi ro T4 (dưới) |
| E16 L-39NG (CZE) | `small_plane_strike_airframe_1`, `"Aero L-39"`, CZE | `L_Strike_fighter2`, CZE | — | NG chưa có variant; dùng L-39 gần nhất, ghi `TODO(names)` |

Đối chiếu cấp thiết bị trước khi tin (T1–T4, Phần 5): variant `"Su-30"` của SOV nằm trong khối BBA của `SOV - Russia.txt`, nên `producer = SOV` chỉ chạy được khi SOV còn tồn tại; nếu SOV mất tag thì rơi về `MR_Fighter2` không variant (cổng E3/E5/E6/E9 đã đòi `country_exists = SOV`, nên không phát sinh).

## 3.3 Bảng 16 sự kiện sau khi sửa

Số tiền là tỷ USD [✓] nếu có nguồn ở báo cáo, còn lại `[?]`. Không đổi giá so với báo cáo 1.2 trừ các dòng ghi chú.

| ID | Cửa sổ (đổi so với 1.2) | Lớp | Cổng | Lựa chọn (đã sửa) | Kết quả |
|---|---|---|---|---|---|
| `.1` DCA Ấn Độ | 2000.3 – 2002.12 | B | RAJ | A đại tu + đào tạo 0,05 (lịch sử); B chỉ đào tạo 0,02; C từ chối | A: idea `VIE_ap_mig21_extension_idea` + 10 XP; B: 5 XP |
| `.2` S-300PMU1 | **2004.3** – 2006.12 | B | SOV | A 2 tiểu đoàn 0,30 (lịch sử); B 1 tiểu đoàn 0,16; C hoãn | A: `sam_lr`+2; B +1; GOT ⇒ thiết bị (3.2) |
| `.3` Su-30MK2 đợt 1 | **2004.1** – 2005.12 | B | SOV | A 4 chiếc 0,12; B 6 chiếc + chuyển loại 0,20 (giao +6 tháng, +10 XP); C hoãn | `air_delivered` +4/+6 |
| `.4` Yak-52 | 2007 – 2009 | **C** | ROM | Kết quả lịch sử: 10 chiếc, 0,02 | XP + idea đào tạo cơ bản |
| `.5` Su-30MK2 đợt 2 | 2008.6 – 2010.6 | B | SOV | A 8 chiếc không vũ khí 0,40 (lịch sử); B 8 chiếc + vũ khí 0,52; C 6 chiếc 0,30 | A đặt idea thiếu đạn tới `.6`; +8/+6 |
| `.6` Su-30MK2V đợt 3 | 2009.9 – 2011.6 | B | SOV | A 12 chiếc + vũ khí 1,00 (lịch sử, 60% ngân khố/40% nợ); B 12 chiếc chỉ thân 0,62 (idea −3% nhiệm vụ 24 tháng); C 8 chiếc 0,70 | +12/+8; gỡ idea thiếu đạn của `.5`; `T5` cần > 11 |
| `.7` Pechora-2TM | 2009 – 2012 | B | BLR | A trên 30 bệ 0,15 (lịch sử); B 15 bệ 0,08 | `VIE_ap_pechora_scope` 2/1; GOT ⇒ thiết bị (3.2). **Bỏ C** (B1) |
| `.8` C-295M | **2013.1** – 2014.12 | B | SPR | A 3 chiếc 0,10 (lịch sử); B 2 chiếc 0,07; C 4 chiếc 0,14 | Vận tải (3.2) |
| `.9` Su-30MK2 đợt 4 | **2013.6** – 2014.12 | B | SOV | A 12 chiếc 0,60 (lịch sử); B 6 chiếc 0,30 + `VIE_ap_su35_talks`; C hoãn | +12/+6 |
| `.10` SPYDER | **2015.1** – 2016.12 | B | ISR | A 5 hệ thống 0,25 (lịch sử); B 3 hệ thống + nghiên cứu Barak-8 0,18 (cờ `VIE_ap_barak_research`) | GOT ⇒ thiết bị; không cộng `sam_lr` |
| `.11` Radar cảnh giới | 2013.1 – 2015.12 | B | CZE (A), ISR (B) | A VERA-NG ×4 0,06 (lịch sử); B thêm ELM-2288 0,10; C đẩy radar Viettel 0,04 (cờ `VIE_ap_radar_viettel_fast`, phát hiện thấp hơn 24 tháng) | Chỉ `air_detection` (3.2) |
| `.12` MiG-21 nghỉ hưu | 2016.1 – 2017.12 | **C** | — | Kết quả lịch sử: giải ngũ, tiết kiệm 0,03; −3% XP không quân 24 tháng (idea) | Gỡ idea `.1` |
| `.13` Đào tạo Su-30 tại Ấn Độ | 2016.12 – 2018.12 | B | RAJ | A Ấn Độ 0,05, 10 XP (lịch sử); B Nga 0,08, 15 XP; C tự đào tạo (cần T1 Trục 3: không có thì ẩn) | Idea tăng tốc huấn luyện 36 tháng (A) |
| `.14` Yak-130 | 2017 – 2021 | B | SOV | A 12 chiếc 0,35 (đã mua 12 chiếc, lịch sử); B từ chối (`VIE_ap_yak130_declined`); C hoãn | Huấn luyện nâng cao (3.2). **Bỏ L-39NG** (B4) |
| `.15` T-6C | **2022.1** – 2024.12 | B | USA | A 12 chiếc 0,15 (lịch sử); B 6 chiếc 0,08 | Gói đào tạo 0,12 nếu `VIE_ap_training_standardized` (B7) |
| `.16` L-39NG | 2022 – 2024 | **C** | CZE | Kết quả lịch sử: 12 chiếc 0,12 (+6 chiếc 0,06 nếu `yak130_declined` và ngân khố đủ, tooltip rõ) | Huấn luyện nâng cao |

Chuyển đi: `.17` Khủng hoảng hỗ trợ Su-27/30 ⇒ 1B (B1). Tổng chi lịch sử ≈ **3,7 tỷ** (3,96 trừ E17 0,12 cộng chênh lệch E14): kiểm bằng script cân bằng (bước 7).

Lịch giao (nội suy là `TODO(nguồn)`, mẫu naval 3.2/3.3: đợt N giao tại `max(mốc lịch sử, ngày ký + lead_min)`, đợt vượt số lịch sử giao cách 6 tháng):

| Chương trình | Đợt | Ngày |
|---|---|---|
| Su-30 đợt 1 (4) | 1 | 2004.11 |
| Su-30 đợt 2 (8) | 2 đợt × 4 | 2010.12, 2011.6 (nội suy) |
| Su-30 đợt 3 (12) | 3 đợt × 4 | 2011.12, 2012.6, 2012.12 (nội suy; "xong cuối 2012") |
| Su-30 đợt 4 (12) | 3 đợt × 4 | 2014.12, 2015.8, 2016.2 (có mốc 2015.8 và đầu 2016) |
| S-300 | 2 tiểu đoàn | 2005.8 (có nguồn), 2006.12 (nội suy) |
| C-295M | 3 | 2015.3, 2015.9, 2016.3 (nội suy; "biên chế từ 2015") |
| T-6C | 2 đợt | 2024.11 (5 chiếc, có nguồn), 2026.6 (nội suy; "giao tới 2027") |
| L-39NG | 2 đợt × 6 | 2024.8, 2025.3 (có nguồn) |
| Yak-130 (12) | 2 đợt × 6 | `TODO(nguồn)`: năm giao chưa rõ; tạm 2021.6 và 2022.6 (nội suy, tìm nguồn trước bước 5) |

Hệ quả cho T5 của Trục 3: 4 + 8 = 12 sau 2011.6 ⇒ `VIE_var_air_delivered > 11` đạt trước `date > 2011.12.31` (đúng ý đồ).

## 3.4 Pop-up theo năm (ước tính, chỉ đếm Class B có title)

| Năm | Đã có (đo 30/9) | + naval | + air B | Tổng | Ghi chú |
|---|---|---|---|---|---|
| 2000 | chưa đo | — | `.1` | ? | |
| 2003 | 6 | `.1` | 0 | **7** | E2/E3 dời sang 2004 |
| 2004 | ≤ 5? | — | `.2`, `.3` | ≤ 7 | |
| 2008 | 6 | — | `.5` | **7** | |
| 2009 | ? | `.3`, `.20` | `.6`, `.7` | ? | **phải đo** |
| 2013 | ≤ 5? | — | `.8`, `.9`, `.11` | ≤ 8 | **phải đo**; hạ `.8` xuống Class C nếu vượt |
| 2015–2017 | ? | — | `.10`, `.13`, `.14` | ? | |
| 2022 | 6 | — | `.15` | **7** | |

Đòn bẩy nếu một năm vượt 7: hạ lần lượt `.8`, `.13`, `.10`, `.11` xuống Class C (áp dụng lựa chọn lịch sử im lặng). `.12`, `.4`, `.16` đã là Class C.

---

# PHẦN 4 — PLAN CODE (7 bước, mỗi bước 1 commit, nhánh `claude/air-truc1`)

Kiến trúc: scheduler riêng, gọi từ `on_monthly` và `VIE_catch_up_schedule`, không dùng `on_monthly_VIE`, không dùng `trigger_year_*`. Không đụng `VIE_event_scheduler_air` (chỉ huy).

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | báo cáo + `VIE_v9_flag_mapping.md` | Báo cáo đã sửa (bản 1.3). Thêm mục "Truc 1 khong quan" vào bảng cờ, với danh sách cờ đặt trước chưa ai đọc (`VIE_ap_pechora_scope`, `_radar_viettel_fast`, `_su35_talks`, `_barak_research`, `_yak130_declined`) | Đọc lại; grep `VIE_ap_` 0 kết quả trước khi code |
| **1** | `common/scripted_triggers/VIE_md_triggers_air_proc.txt` (mới) | Gom cổng: `VIE_ap_gate_sov/_raj/_rom/_blr/_spr/_isr/_cze/_usa`; `VIE_ap_training_standardized = { always = no }` (đã bỏ `has_bba`, `has_got`, `can_fund`: không ai gọi); comment trạng thái Q-list như p14 | `python tools/audit/live.py` sạch |
| **2** | `common/scripted_effects/VIE_md_effects_air_proc.txt` (mới) | (a) Phần thưởng dùng chung (mỗi chuỗi một effect `VIE_ap_reward_<p>_a/b/c`, dùng cho cả fallback và option, giống p14); (b) helper cấp thiết bị dự kiến nhưng không được gọi; delivery giữ logic inline trong `VIE_ap_deliver_*`; (c) `VIE_event_scheduler_air_proc` (catch-up → cờ; popup_cd; fallback; `_missed`); (d) `VIE_ap_deliver_<p>` (Class C, cờ `_dN`); nối vào `on_monthly` **và** `VIE_catch_up_schedule` | console `effect VIE_event_scheduler_air_proc = yes` không lỗi; `effect set_variable = { VIE_catch_up = 1 }` rồi chạy: không popup, không máy bay |
| **3** | `events/VIE_air_proc.txt` (mới, `add_namespace = vie_air_proc`), `common/ideas/VIE_md_ideas_air_proc.txt` | **Lát cắt Su-30 trước** (`.3 .5 .6 .9` + giao hàng + `VIE_var_air_delivered` + idea thiếu đạn / chỉ thân máy). Đây là rủi ro lớn nhất (T1, T2) | chơi tới 2004.1: một popup `.3`; 2004.11 +4 chiếc trong kho; BBA có `"Su-30"`, non-BBA có `MR_Fighter2`; `error.log` sạch |
| **4** | cùng file | **Lát cắt SAM** (`.2 .7 .10`) với hai nhánh: có GOT (tech chuỗi + `sam_missile_equipment_N`) và không GOT (chỉ idea + modifier) | chạy hai lượt (có và không GOT): kho SAM tăng/không; tech `SAM2` có; không có "equipment does not exist" |
| **5** | cùng file | **Huấn luyện, vận tải, radar** (`.1 .4 .8 .11 .12 .13 .14 .15 .16`), hai nhánh BBA/non-BBA, các idea; E15/E16 theo T4 | chơi tới 2025: không lỗi; `.4 .12 .16` không popup |
| **6** | `localisation/english/VIE_md_events_air_proc_l_english.yml` (+ `replace/` theo mẫu repo), `tools/TESTING.md` mục "Air procurement", `tools/audit/air_proc_balance.py` | Loc có BOM; checklist mục Phần 5; script cộng chi theo năm, đếm popup/năm từ `ev.py`, in PASS khi tổng chi và popup nằm trong dải | `python tools/verify_all_loc.py` PASS; `python tools/audit/ev.py` không orphan; script PASS |
| **7** | `VIE_v9_flag_mapping.md`, báo cáo | Ghi cờ thực tế, ghi trạng thái vào cuối tài liệu này (mẫu naval) | — |

Ước lượng: 13 event Class B + 3 Class C (chỉ ở scheduler), ~700 dòng script, ~110 khóa loc, 7–8 timed idea. Không có Decision (cửa sổ lỡ hẹn chỉ đặt `_missed`, 1B tự đọc).

---

# PHẦN 5 — CHECKLIST THỬ TRONG GAME

- [ ] `error.log`: grep `vie_air_proc`, `VIE_ap_`, `equipment`, `variant`, `sam_missile`, `stockpile`, `technology`.
- [ ] **T1 (rủi ro cao nhất):** BBA — `add_equipment_to_stockpile = { type = medium_plane_airframe_2 variant_name = "Su-30" producer = SOV }` cho VIE: kho có máy bay tên "Su-30" không, có dùng được trong air wing không (VIE chưa nghiên cứu khung này).
- [ ] **T2:** non-BBA — `AS_Fighter2` có hiện trong kho (Su-27 đầu game của VIE cũng là loại này: cộng dồn đúng).
- [ ] **T3:** GOT — sau `set_technology` SAM1+SAM2 và cấp `sam_missile_equipment_3`, thiết bị có hiện ra, triển khai được không; không GOT: không có lỗi, chỉ có idea.
- [ ] **T4:** BBA — cấp `small_plane_strike_airframe_1` **không** có `variant_name` (T-6C): có tạo thiết bị mặc định không; nếu không, dùng `"Aero L-39"` producer CZE.
- [ ] Đặt `VIE_popup_cd` thủ công (`effect set_country_flag = { flag = VIE_popup_cd days = 45 }`) vào 2004.1 rồi chờ: `.3` dời sang tháng sau, không mất; giữ tới hết cửa sổ: fallback im lặng, không `_missed`.
- [ ] Cho Nga biến mất trước 2008 (console): `.5 .6 .9` đặt `_missed`, không popup; không máy bay; không lỗi.
- [ ] Chiến tranh với SOV giữa cửa sổ rồi hòa: cửa sổ còn thì offer vẫn bắn.
- [ ] Nội chiến: người thắng có cờ lịch sử, không nhận máy bay, không popup.
- [ ] Đếm popup/năm 2000–2024 (`ev.py`, rồi chơi quan sát); mục tiêu ≤ 7, ghi các năm vượt.
- [ ] `treasury` thực tế của VIE tại 2009-09 và 2013-06: chi 1,0 tỷ (E6) và 0,6 tỷ (E9) trừ đúng, nợ tăng đúng phần 40%.
- [ ] Chơi AI tới 2020: AI chọn lịch sử mọi sự kiện, tổng `VIE_var_air_delivered` = 36 vào đầu 2016.
- [ ] Chạy **hai lượt**: có BBA / không BBA; có GOT / không GOT.

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đề xuất)

| # | Câu hỏi | Mặc định |
|---|---|---|
| Q-A1 | Tiền tố/namespace Trục 1: `VIE_ap_`, `vie_air_proc`, scheduler `VIE_event_scheduler_air_proc` (A2) | **Theo đề xuất** |
| Q-A2 | E17 (khủng hoảng hỗ trợ Su-27/30) chuyển sang 1B (B1) | **ĐÃ CHỐT: chuyển** |
| Q-A3 | Loại non-BBA cho Su-30MK2: `MR_Fighter2` (RAJ/ALG) hay `AS_Fighter2` (CHI, `vie_dip.16`) | **ĐÃ CHỐT: `AS_Fighter2`** |
| Q-A4 | Funding Gate chỉ cho lựa chọn "mở rộng", không cho lịch sử (A5) | **Có** |
| Q-A5 | Hạ E4, E12, E16 xuống Class C (im lặng) để giữ ngân sách pop-up (B5) | **Có** |
| Q-A6 | E14 (Yak-130, [~]) vẫn nằm ở Trục 1 hay chuyển hẳn sang 1B P1 | **ĐÃ CHỐT: giữ ở Trục 1, Yak-130 đã mua 12 chiếc** (bỏ nhãn [~]; 1B P1 chỉ còn Yak-130M/L-39/FA-50/M-346 bổ sung) |
| Q-A7 | Q15 mở rộng: nhánh không-GOT chỉ còn timed idea + modifier cho E2/E7/E10 (A3) | **Có** |
| Q-A8 | E5 mô tả "vũ khí" bằng idea thiếu đạn (B3) thay vì bỏ lựa chọn này | Giữ lựa chọn bằng idea |

---

# TRẠNG THÁI

Phân tích và sửa báo cáo xong (2026-10-02). **Chưa có dòng code nào.** Bước 0 trong Phần 4 đã làm (báo cáo bản 1.3); bước 1–7 chờ bạn chốt Phần 6.

---

# TIẾN ĐỘ CODE (2026-10-02)

Bước 1–7 đã code/ghi tài liệu, chưa chạy game, chưa commit: trigger cổng, scheduler + template, Su-30 (`.3 .5 .6 .9`), SAM (`.2 .7 .10`), huấn luyện/vận tải/radar (`.1 .8 .11 .13 .14 .15` + Class C `yak52`, `mig21_retire`, `l39ng`).
Thay đổi so với plan khi code:
- L-39NG (Class C, không popup) không có "tùy chọn mở rộng": nếu `VIE_ap_yak130_declined` và `treasury > 0,3` thì tự động đặt 18 chiếc 0,18, ngược lại 12 chiếc 0,12.
- E11 A đòi `VIE_ap_gate_cze`; khi Séc không tồn tại, AI chọn được C (không bị zero-weight).
- `VIE_var_sam_lr` chỉ cộng theo tiểu đoàn S-300.
Bước 6: `tools/audit/air_proc_balance.py` (ALL PASS; tổng chi lịch sử 3,69 tỷ) và mục "Air procurement" trong `tools/TESTING.md`. Bước 7: bảng cờ trong `VIE_v9_flag_mapping.md` (mục "Truc 1 khong quan"). Còn lại: thử trong game theo TESTING.md (T0–T4), rồi commit. Cờ đặt trước chưa ai đọc: `VIE_ap_pechora_scope`, `VIE_ap_radar_viettel_fast`, `VIE_ap_su35_talks`, `VIE_ap_barak_research`, `VIE_ap_yak130_declined` (E16 đọc).

## Đợt sửa sau review (2026-10-02)
1. Idea thiếu đạn (E5): chỉ thêm khi E6 chưa ký; gỡ khi E6 `_missed`.
2. Lead time: cờ `VIE_ap_<p>_lead` đặt lúc ký (150–480 ngày), mọi đợt giao đòi hết cờ.
3. Su-30 khi SOV đã mất tag: cấp loại mặc định không `producer` (không variant).
4. Helper `VIE_ap_ensure_af_modifier`: gắn `VIE_armed_forces_modifier` nếu chưa có (trước đó chỉ focus `VIE_modernize_vpa` gắn).
5. Ảnh hưởng bên bán: tăng 1% mỗi hợp đồng bằng logic inline trong reward (mẫu focus Algeria của MD).
6. Dọn convention MD: bỏ cờ `_contracted` (dùng `qty > 0`), bỏ 3 trigger không dùng, idea theo kiểu MD (không `allowed`, `allowed_civil_war = yes`), bỏ log ở option không hiệu ứng.

---

## Phần 4: Review & Kế hoạch code Trục 2 (Công nghiệp Hàng không APM)

# REVIEW TRỤC 2 KHÔNG QUÂN (CÔNG NGHIỆP QUỐC PHÒNG) + PLAN CODE

> **Ghi chú lịch sử PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản v18 có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


> Đầu vào: `VIE_air_force_content_report.md` bản 1.3, Phần 6 (Trục 2) và các chỗ Trục 2 chạm tới (4.2, 4.3, 6.5, 7, 8.2, 11, 12.2 mục 10, 13 Q16).
> Đối chiếu với: repo @ `e4f3215` + đợt Trục 1 không quân đã code (chưa commit); MD v2.0.0 trên máy; code Trục 2 hải quân (`VIE_md_nav_ind_decisions.txt`, `VIE_md_effects_nav_ind.txt`, `VIE_naval_truc2_review_and_plan.md`) và lục quân (`VIE_md_def_industry.txt`); Code Style Guide của MD (GitHub `docs/.../code-stylization-guide.md`) và `code-resource.md`.
>
> **KẾT LUẬN: cấu trúc ý tưởng (5 trụ × 3 bậc, bậc là biến, Decision là nút khởi động, Trục 3 và 1B chỉ đọc) ĐÚNG và giữ nguyên.
> Nhưng bản 1.3 chưa code được: 4 lỗi chặn (Phần 1), 7 chỗ lệch game/mod (Phần 2).**
> Báo cáo đã được sửa (bản 1.4, Phần 6 viết lại). Phần 3 là thiết kế chốt, Phần 4 plan code 9 bước, Phần 6 các quyết định cần bạn chốt.

---

# PHẦN 1 — 4 LỖI CHẶN

## A1 · Báo cáo nói "Việt Nam chưa có MIO", nhưng repo đã có 4 MIO và Trục 2 khác đã nuôi chúng

6.5 và 12.2 mục 10 của bản 1.3: MD chưa có MIO cho Việt Nam, nên MIO "làm sau", chỉ là lớp phủ tùy chọn, và đòi AAT làm Trục 2 hỏng. Thực tế `VIE_md_organizations.txt` định nghĩa:

| MIO | Phạm vi | Liên quan Trục 2 không quân |
|---|---|---|
| `VIE_viettel_manufacturer` | `cnc`, `mio_cat_eq_only_uav`, `guided_missile_equipment`, `sam_missile_equipment`; `CAT_drones CAT_a_uav CAT_naval_radar CAT_missile CAT_electrical_tech`; trait radar, EW, UAV, drone trinh sát / tấn công, loitering, tên lửa phòng không | đúng 4 trụ (A31, Radar, Tích hợp, UAV) |
| `VIE_vaeco_manufacturer` | máy bay nhẹ, trực thăng, vận tải | chỉ gần A32 bậc 3 (C-295M, trực thăng) |
| `VIE_gdt_manufacturer`, `VIE_ba_son_manufacturer` | lục quân, hải quân | không |

Trục 2 hải quân và lục quân đã dùng `add_mio_size` bọc `has_dlc = "Arms Against Tyranny"` (`VIE_ba_son_mio_size_N`; ghi chú Q8 = a: không dùng `add_mio_funds` cùng lúc, vì nó tự lên size). Lý do "Q16 chỉ-Decision vì AAT" đã được giải bởi cái bọc `has_dlc`: người không có AAT chỉ không thấy MIO.
**Sửa:** Trục 2 giữ bậc bằng biến + Decision (không đổi), và nuôi `VIE_viettel_manufacturer` bằng `VIE_apm_viettel_mio_size` (+1 ở A31 bậc 2 và 3, Radar bậc 2, UAV bậc 2). A32 không có MIO. Trait sẵn có của Viettel đã cho bonus SAM và UAV, nên modifier Trục 2 không cộng cùng loại (tránh đếm đôi).

## A2 · Hai hiệu ứng trong 6.4 không có token trong MD

Đối chiếu `code-resource.md` của MD và `common/modifier_definitions`:
- "**Giá thay thế tên lửa phòng không** (A31)": MD chỉ có `olv_/gnss_/comsat_/spysat_/killsat_production_*` (vệ tinh, phóng) và `equipment_cost_multiplier_modifier` (= **chi phí duy trì** trang bị, tên hiển thị "Equipment upkeep"). Không có modifier giá/tốc độ sản xuất SAM. Mod đã có `VIE_af_equipment_cost_multiplier_modifier` trong `VIE_armed_forces_modifier`.
- R6 báo cáo cho Trục 2 sở hữu "tuổi thọ / độ tin cậy": **độ tin cậy** chỉ chỉnh được qua `equipment_bonus` của MIO (`reliability`), không có modifier quốc gia; **tuổi thọ** không có cơ chế nào trong MD.
Token thật dùng được: `air_accidents_factor` (A32), `air_detection` (Radar), `air_defence_factor` (A31, mod đã dùng cho SAM/Igla), `equipment_cost_multiplier_modifier` (chi phí duy trì), `air_experience`, `add_mio_size`.
**Sửa:** bảng hiệu ứng 6.4 viết lại bằng các token trên; bỏ "nửa mức phạt phụ tùng nếu SOV không còn hỗ trợ" và "kéo dài tuổi thọ" (không có cơ chế; phần Nga ngần ngại nằm ở Decision 1B, E17 đã chuyển).

## A3 · Bộ đếm slot: bỏ hook `VIE_collapse_aftermath`, dùng bộ đếm tự chữa

R9 (3.1) và 6.6 của bản 1.3 dựa vào `VIE_collapse_aftermath` để đếm lại. **Đã chốt (2026-10-02): bỏ hook này, không dùng nữa.** Mod đã gỡ collapse/civil war (`tools/TESTING.md`: "Removed 2026-10-02"); grep repo cho `VIE_collapse_aftermath`, `VIE_civil_war_end`, `recount` ra **0 kết quả trong code** (dòng "Kept: `VIE_civil_war_end`" trong TESTING là chú thích cũ, đã sửa). Hệ quả: mất event hoàn tất thì slot kẹt ở 2 nếu không có cơ chế khác.

Ghi chú: các tài liệu hải quân (`VIE_naval_truc2/3_review_and_plan.md`) còn ghi recount "gọi trong `VIE_collapse_aftermath`", nhưng code tương ứng không có trong repo; coi các dòng đó là tài liệu cũ, hải quân chưa có đếm lại (nợ riêng, Q-B4).
**Sửa cho Trục 2 không quân (và ghi nợ cho hải quân):** bộ đếm **tự chữa**. Hàm tháng `VIE_apm_slot_heal` (gọi từ cùng scheduler): nếu không còn timed idea `VIE_apm_prog_*` nào thì đặt `VIE_var_apm_active = 0`. Không gắn vào bất kỳ hook nội chiến nào, và không cần `VIE_catch_up`.

## A4 · Tiền tố và tên: focus còn `VIE_air_*`, biến còn tên trần

Bản 1.3 chốt (4.3) Trục 2 dùng `VIE_apm_`/`vie_air_ind`, nhưng 6.2 vẫn ghi focus `VIE_air_industry_law`, `VIE_air_mro_a32`…, 6.3 ghi `VIE_var_a32_tier`, `VIE_var_air_industry_active`… Tiền tố `VIE_air_` đã bị roster chỉ huy chiếm (Trục 1 đã phải né, xem `VIE_air_truc1_review_and_plan.md` A2); `VIE_var_a32_tier` là tên chung chung dễ đụng nhánh khác.
**Sửa:** đổi hết sang `VIE_apm_*` (focus `VIE_apm_law/_a32/_a31/_radar/_integration/_uav/_mature`; bậc `VIE_apm_a32_tier`, `VIE_apm_a31_tier`, `VIE_apm_radar_tier`, `VIE_apm_integ_tier`, `VIE_apm_uav_tier`; slot `VIE_var_apm_active`; category `VIE_apm_category`; Decision `VIE_apm_d_*`; idea `VIE_apm_prog_*`). Đã grep: 0 kết quả trong repo.

---

# PHẦN 2 — 7 CHỖ LỆCH GAME / MOD

## B1 · 15 Decision `fire_only_once` thay vì 5 Decision lặp lại

MD Code Style Guide: "Use `fire_only_once` sparingly". Hải quân dùng 5 Decision cho 5 chương trình; lục quân 9. 15 Decision (mỗi bậc một cái) làm category dài, 30 khóa loc chỉ để mở bậc kế của cùng một trụ.
**Sửa:** **5 Decision lặp lại** (một mỗi trụ), `visible` = focus xong và bậc < 3, `available` = slot < 2, không còn timed idea của trụ, và trigger cổng của bậc kế `VIE_apm_<p>_ok`. Bấm ⇒ `VIE_apm_program_start` ⇒ event chọn của bậc kế (đọc `VIE_apm_<p>_tier`) ⇒ timed idea ⇒ event ẩn hoàn tất tăng bậc. Số event ≈ 20 (15 chọn + 5 ẩn), không đổi nội dung.

## B2 · Cổng đọc từ Trục 1 chưa được viết ra

Bản 1.3 mô tả bằng lời ("điều kiện cho E17", "Pechora-2TM") và vẫn nói "Trục 1 cộng exp vào Trục 2". Trục 1 đã code **không ghi exp**, chỉ ghi cờ/biến (`VIE_ap_pechora_scope`, `VIE_ap_radar_viettel_fast`, `VIE_var_air_delivered`, `VIE_var_sam_lr`, `VIE_ap_spyder_qty`, `VIE_ap_c295_qty`, `VIE_ap_t6c_qty`, `VIE_ap_l39ng_qty`).
**Sửa:** bảng cổng trong 6.3 (mỗi bậc một cột "Cổng") và ba cờ có người đọc thật ngay trong Trục 2:

| Cờ/biến Trục 1 | Người đọc trong Trục 2 |
|---|---|
| `VIE_ap_pechora_scope` (1/2) | cổng A31 bậc 1; scope 2 ⇒ chi phí ×0,8, −3 tháng |
| `VIE_ap_radar_viettel_fast` | Radar bậc 1: ×0,8 chi phí, −3 tháng |
| `VIE_var_air_delivered ≥ 12` | cổng A32 bậc 3 |
| `VIE_ap_c295_qty > 0` | lựa chọn "C-295M và trực thăng" của A32 bậc 3 |
| `VIE_var_sam_lr ≥ 1` | cổng A31 bậc 3, Tích hợp bậc 2 |
| `VIE_ap_spyder_qty > 0` | cổng Tích hợp bậc 1 (Python-5/Derby đến cùng SPYDER) |
| `VIE_ap_t6c_qty > 0` hoặc `VIE_ap_l39ng_qty > 0` | cổng Tích hợp bậc 3 |

## B3 · Cổng "ít nhất hai trong F2, F3, F4" không biểu diễn được bằng `prerequisite`

`prerequisite` chỉ có OR (một khối nhiều focus) và AND (nhiều khối). "Hai trong ba" cần scripted trigger.
**Sửa:** F5 `prerequisite = { focus = F2 focus = F3 focus = F4 }` (OR) + `available` gọi `VIE_apm_two_of_three` (đếm `has_completed_focus`).

## B4 · F7 không định nghĩa "đủ điều kiện bậc"

6.2 ghi "đặt `VIE_cap_mature_air_industry` khi đủ điều kiện bậc" nhưng không nói điều kiện.
**Sửa:** scripted trigger `VIE_apm_mature_ok` = `a32_tier = 3`, `a31_tier ≥ 2`, `radar_tier = 3`, `integ_tier ≥ 2`, `uav_tier ≥ 2` (một chỗ để đổi). F7 `available` đòi trigger này.

## B5 · Trục 3 T5 còn tham chiếu `VIE_air_mro_a32`

7.1 T5: "T4, hoặc `VIE_air_mro_a32`". Đã đổi sang `VIE_apm_a32` (bản 1.4). Trục 3 chỉ đọc, không viết ngược (R12).

## B6 · Hiệu ứng nặng về Nga hỗ trợ đã chuyển sang 1B

6.3 A32 bậc 3 "nếu SOV không còn hỗ trợ, nửa mức phạt phụ tùng; điều kiện cho E17": E17 đã sang 1B (Trục 1 review B1), và MD không có cơ chế phụ tùng. A32 bậc 3 chỉ còn: tai nạn −2%, XP, và **là dữ kiện mà Decision hỗ trợ Su-27/30 của 1B đọc** (`VIE_apm_a32_tier`).

## B7 · Chi phí: thang giá thật trong khi hai Trục 2 kia dùng thang giá công trình của MD

Hải quân 34,7 tỷ, lục quân 30,25 tỷ, vì Decision xây công trình bằng helper `one_state_*` của MD (mỗi dockyard 7,5 tỷ, airbase 3,0, radar 1,75). Trục 2 không quân không xây công trình nào nên 3,1 tỷ (giá thật, cùng thang Trục 1 = 3,7 tỷ) là nhất quán, nhưng người chơi sẽ thấy hiệu ứng nhỏ so với hai trục kia. Giữ (Q-B2), ghi rõ trong 6.3.

---

# PHẦN 3 — THIẾT KẾ CHỐT

Toàn bộ bảng focus (7), bậc (15), token, MIO nằm ở `VIE_air_force_content_report.md` Phần 6 (bản 1.4). Tóm tắt dữ kiện cần để code:

## 3.1 Ba hợp đồng với phần còn lại

| Cạnh | Qua |
|---|---|
| Trục 1 → Trục 2 | bảng B2 |
| Trục 2 → Trục 3 | T5 đọc `VIE_apm_a32` (hoặc T4); không ghi ngược |
| Trục 2 → 1B | `*_tier`, `VIE_apm_sam_production`, `VIE_apm_radar_orient`, `VIE_cap_mature_air_industry` (điều kiện hybrid/nội địa P2, P3, P8, P9, P10; Decision hỗ trợ Su-27/30) |

## 3.2 Biến và cờ (đề xuất)

| Tên | Đặt bởi | Đọc bởi |
|---|---|---|
| `VIE_apm_a32_tier`, `VIE_apm_a31_tier`, `VIE_apm_radar_tier`, `VIE_apm_integ_tier`, `VIE_apm_uav_tier` (0–3) | event ẩn hoàn tất | cổng bậc kế, `VIE_apm_mature_ok`, 1B |
| `VIE_var_apm_active` (0–2) | `VIE_apm_program_start/_end`, `VIE_apm_slot_heal` | `available` của Decision |
| `VIE_apm_<p>_choice` (lựa chọn của bậc đang chạy, 1–3) | event chọn | event ẩn hoàn tất (đọc xong thì không cần nữa) |
| `VIE_apm_radar_orient` (1 chống tàng hình / 2 ưu tiên 3D), `VIE_apm_sam_production` (cờ) | Radar bậc 3, A31 bậc 3 | 1B (P10, P8) |
| `VIE_cap_mature_air_industry` (cờ) | F7 | 1B |
| timed idea `VIE_apm_prog_a32/_a31/_radar/_integ/_uav` | event chọn | chỉ báo "đang chạy", dùng để tự chữa slot |

Không giữ cờ `_active/_done/_waiting` cho Decision, `_progress`, `VIE_cap_*` thừa (xem naval B5).

## 3.3 Việc tránh (để khỏi lặp lỗi hải quân)

- Không có trạng thái "chờ giữa chừng": cổng ở lúc bấm, `custom_trigger_tooltip` nêu điều kiện thiếu.
- Event chọn do người chơi bấm Decision: miễn `VIE_popup_cd`. Event ẩn hoàn tất không tính vào ngân sách pop-up.
- `days = <biến>` cho `add_timed_idea` và `country_event` đã được xác minh trong mã MD (naval Phần 10).
- Mọi `ai_chance` có tốn tiền có guard `bankruptcy_incoming_collapse`.

---

# PHẦN 4 — PLAN CODE (9 bước, mỗi bước 1 commit, nhánh `claude/air-truc2`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | báo cáo + `VIE_v9_flag_mapping.md` | Báo cáo bản 1.4 (đã làm). Thêm mục "Truc 2 khong quan" vào bảng cờ | grep `VIE_apm_`, `vie_air_ind`, `VIE_apm_category` 0 kết quả |
| **1** | `common/scripted_triggers/VIE_md_triggers_air_ind.txt` (mới) | `VIE_apm_<p>_ok` (5 cổng bậc kế, đọc cờ Trục 1), `VIE_apm_two_of_three`, `VIE_apm_mature_ok`, `VIE_apm_slot_free` | `live.py` sạch |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc + `tools/build_vie_focus_icons.py` (7 mục `FOCI`) + `common/decisions/categories/VIE_md_categories.txt` | 7 focus (6.2), category `VIE_apm_category` (priority **87**; đã dùng 88–95 và 100) | `tools/audit/audit.py` (toạ độ x ≥ 288, gap, forward-ref); `verify_all_loc.py` |
| **3** | `common/scripted_effects/VIE_md_effects_air_ind.txt` (mới), `common/ideas/VIE_md_ideas_air_ind.txt` (mới) | `VIE_apm_pay`, `VIE_apm_program_start/_end`, `VIE_apm_slot_heal`, `VIE_apm_viettel_mio_size`, helper cộng modifier (`VIE_apm_add_accidents/_detection/_air_def/_upkeep`, có `VIE_ap_ensure_af_modifier` và tooltip, kẹp theo trần), 5 timed idea | `live.py` sạch |
| **4** | `events/VIE_air_ind.txt` (`add_namespace = vie_air_ind`) + `common/decisions/VIE_md_air_ind_decisions.txt` | **A32 trọn vẹn**: Decision lặp lại, 3 event chọn (`.11 .12 .13`), event ẩn hoàn tất `.19` | chơi tới 2011 (console mở F2), bấm Decision: event, timed idea, bậc 1 |
| **5** | cùng file | **A31** (`.21–.23`, `.29`) và **Radar** (`.31–.33`, `.39`); đọc cờ Trục 1 | `VIE_ap_pechora_scope` đổi giá; MIO Viettel +1 (có AAT) |
| **6** | cùng file | **Tích hợp** (`.41–.43`, `.49`) và **UAV** (`.51–.53`, `.59`); UAV bậc 2–3 AI chỉ `VIE_ai_free` | cổng đọc Trục 1 đúng |
| **7** | focus F7 + `VIE_cap_mature_air_industry`; nối `VIE_apm_slot_heal` vào `on_monthly` | mở F7 bằng console ngày | slot tự chữa: xóa timed idea bằng console, tháng sau slot = 0 |
| **8** | `localisation/english/VIE_md_events_air_ind_l_english.yml` (BOM), `tools/TESTING.md` (mục "Air industry"), `VIE_v9_flag_mapping.md`, `tools/audit/air_ind_balance.py` | loc ≈ 120 khóa; script cộng chi/bậc, trần modifier, MIO size | `verify_all_loc.py`; script PASS |
| **9** | `tools/build_vie_air_event_pictures.py` | ảnh cho event chọn (13 tệp Commons như Trục 1) hoặc dùng `GFX_report_event_generic_read_write` tạm | không lỗi `texturefile` |

Ước lượng: 7 focus, 5 Decision, ≈ 20 event (5 ẩn), 5 timed idea, ≈ 600 dòng script, ≈ 120 khóa loc.

---

# PHẦN 5 — CHECKLIST THỬ TRONG GAME (dự kiến, đưa vào TESTING.md ở bước 8)

- [ ] `error.log`: grep `vie_air_ind`, `VIE_apm_`, `add_mio_size`, `mio:`, `texturefile`.
- [ ] Chạy hai lượt: có AAT (MIO Viettel nhận +1) và không AAT (không lỗi, không MIO).
- [ ] F1 xong ⇒ category `VIE_apm_category` hiện; F2–F4 xong ⇒ Decision tương ứng hiện, chỉ khi cổng đạt.
- [ ] Decision lặp lại: bấm A32 lần 1 ⇒ bậc 1; ngay sau đó Decision mờ (còn timed idea); xong ⇒ hiện lại cho bậc 2, đòi `date > 2016.12.31`.
- [ ] Slot: chạy A32 + A31 cùng lúc thì Radar mờ (slot = 2); xóa timed idea bằng console ⇒ tháng sau slot về 0.
- [ ] Cổng Trục 1: không ký E7 ⇒ A31 bậc 1 mờ với tooltip "cần hợp đồng Pechora"; `VIE_ap_radar_viettel_fast` ⇒ Radar bậc 1 rẻ hơn.
- [ ] Modifier: `VIE_af_air_accidents_factor`, `air_detection`, `air_defence_factor` tăng đúng, tooltip hiện, không vượt trần.
- [ ] Tổng chi đủ 15 bậc ≈ 3,1 tỷ; AI chỉ đi bậc dựa tin [~] khi `VIE_ai_free`.
- [ ] Size tối đa MIO của MD không bị vượt (tổng +4 từ Trục 2).

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đề xuất)

| # | Câu hỏi | Mặc định |
|---|---|---|
| Q-B1 | 5 Decision lặp lại thay vì 15 Decision `fire_only_once` (B1) | **5 Decision** |
| Q-B2 | Giữ thang giá thật 3,1 tỷ (B7), hay nâng lên thang MD để ngang hải quân/lục quân | **Giữ giá thật** |
| Q-B3 | Nuôi MIO Viettel bằng `add_mio_size` (+4 tổng) (A1) | **Có** |
| Q-B4 | Slot tự chữa bằng hàm tháng (A3); đồng thời vá cho hải quân | **Có**; vá hải quân tách riêng |
| Q-B5 | Bậc dựa tin [~] (UAV 2–3, A31 bậc 3 sản xuất) AI chỉ khi `VIE_ai_free` | **Có** |
| Q-B6 | Trần modifier: phát hiện Trục 1 ≤ 5%, Trục 2 = 6%, Trục 3 theo 7.5 (≈ 16%): tổng ≈ 27%, chấp nhận hay đặt trần chung | **Chấp nhận**, đo bằng script bước 8 |
| Q-B7 | Ảnh event Trục 2 lấy từ Commons như Trục 1 (bước 9) | **Có** |

---

# TRẠNG THÁI

Bước 1 (triggers) và bước 2 (7 focus, category, loc 16 khóa) đã code, chưa chạy game, chưa commit. Focus dùng icon generic của vanilla (`GFX_focus_generic_*`) như hải quân; icon riêng thêm 7 mục vào `FOCI` khi có ảnh. Tooltip `unlock_decision_tooltip = VIE_apm_d_*` trỏ Decision chưa tồn tại tới bước 4–6.

Review và sửa báo cáo xong (2026-10-02). **Chưa có dòng code nào cho Trục 2.** Bước 0 đã làm (báo cáo 1.4); bước 1–9 chờ bạn chốt Phần 6.

## Tiến độ code (2026-10-02)
Bước 1–8 đã code, chưa chạy game, chưa commit: triggers, 7 focus + category, helper + 5 timed idea, 5 Decision lặp lại, 20 event (15 chọn + 5 hoàn tất), `VIE_apm_slot_heal` nối vào `on_monthly` (bước 7; F7 đã nằm trong bước 2), loc 117 khóa, `tools/audit/air_ind_balance.py` (ALL PASS: tổng 3,10 tỷ, đường lịch sử xong khoảng 2030-07 với 2 slot, MIO +4), mục "Air industry" trong `tools/TESTING.md`, bảng cờ trong `VIE_v9_flag_mapping.md`.
Còn: bước 9 (ảnh event) và thử trong game theo TESTING.md. Nợ chung: `VIE_ai_free` được `VIE_md_p1b_decisions.txt` dùng nhưng không được định nghĩa ở đâu; hải quân chưa có đếm lại slot.

---

## Phần 5: Review & Kế hoạch code Trục 3 (Xây dựng Lực lượng PK-KQ)

# REVIEW TRỤC 3 KHÔNG QUÂN (XÂY DỰNG LỰC LƯỢNG) + PLAN CODE

> **Ghi chú lịch sử PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản v18 có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


> Đầu vào: `VIE_air_force_content_report.md` bản 1.4, Phần 7 (Trục 3) và các chỗ Trục 3 chạm tới (3.1 R5/R9/R11, 4.2, 4.3, 4.4, 10, 11, 13).
> Đối chiếu với: repo đang có Trục 1 + Trục 2 không quân (chưa commit, đã qua review 2026-10-03); Trục 3 hải quân (`VIE_naval_truc3_review_and_plan.md`, `VIE_md_effects_nav_force.txt`, `VIE_md_nav_force_decisions.txt`, `events/VIE_nav_force.txt`) và lục quân (`VIE_md_effects_p17.txt`); MD v2.0.0 và HOI4 trên máy (`documentation/modifiers_documentation.md`, `common/modifier_definitions`); cây focus live (323 focus, đo toạ độ tuyệt đối).
> Phạm vi: chỉ Trục 3 (22 focus + 5 Decision). 1B chưa dựng nên mọi chỗ Trục 3 nối sang 1B được tách ra, xem A2, A4.
>
> **KẾT LUẬN: khung (8 focus chung → 3 nhánh loại trừ, 5 Decision, modifier ghi vào `VIE_armed_forces_modifier`) ĐÚNG và giống hải quân, giữ nguyên.
> Nhưng bản 1.4 chưa code được: 4 lỗi chặn (Phần 2), 4 chỗ lệch với Trục 1–2 và mod (Phần 3). Báo cáo đã sửa thành bản 1.5. Phần 4 là thiết kế chốt, Phần 5 plan code 9 bước.**

---

# PHẦN 1 — ĐÚNG, GIỮ NGUYÊN

| Điểm | Lý do |
|---|---|
| 22 focus = 8 chung + A (4) + B (5) + C (5), ba nhánh loại trừ nhau ở A1/B1/C1 | Cùng khuôn `VIE_nf_*` hải quân (D/G/B) |
| T1 treo `VIE_modernize_vpa`, không phụ thuộc cây hải quân hay lục quân | Giống `VIE_nf_training_standardization` |
| Focus chỉ cấp XP, modifier và tooltip mở Decision; việc đào tạo là Decision (R2) | Giống hải quân |
| 5 Decision `fire_only_once`, 50 PP (D-E 60), cổng ở lúc bấm, chuỗi event chọn nối tiếp (miễn `VIE_popup_cd`), hoàn tất bằng event hẹn giờ | Cùng mẫu `VIE_nf_d1…d5` |
| Chuyên môn D-A chọn ngay trong chuỗi, không "event giữa chừng" | Hải quân đã sửa như vậy |
| Cặp lệch nhánh / đúng nhánh nhỏ, đối xứng (7.4) | Giống `VIE_nf_branch_mismatch_idea` |
| Trục 3 không ghi `VIE_cap_*` và bậc Trục 2 (R5), chỉ cộng thưởng ngược cho Trục 1 | Giữ nguyên |
| Token: `experience_gain_air_factor`, `air_range_factor`, `air_cas_efficiency`, `air_mission_efficiency`, `air_superiority_efficiency`, `air_detection`, `air_defence_factor` | Đối chiếu `modifiers_documentation.md` hôm nay: đều có |

---

# PHẦN 2 — 4 LỖI CHẶN

## A1 · T5 và các cổng đọc Trục 1 không có đường dự phòng, và prerequisite viết sai

Bản 1.4: T5 = "T4, hoặc `VIE_apm_a32`", cổng `VIE_var_air_delivered > 11`.
- "T4 **hoặc** A32" cho phép bỏ qua T4 nếu đã xong A32. Hải quân viết ngược lại: T6 = T5 **và** (một trong hai focus Trục 2). Hai cách mở T5 loại trừ ý nghĩa của chuỗi chung.
- `VIE_var_air_delivered > 11` chỉ tăng khi Su-30 được giao (Trục 1). Nếu SOV không còn hoặc đang có chiến tranh với VIE trong cả bốn cửa sổ, biến đứng ở 0 và T5 khóa vĩnh viễn, kéo theo T6, T7, T8 và cả ba nhánh. Đây là đúng lỗi #1 của review Trục 2 (hợp đồng tùy chọn thành cổng cứng).

**Sửa:** T5 = `prerequisite = { focus = VIE_airf_command_reform_1 }` **và** `prerequisite = { focus = VIE_apm_a32 focus = VIE_apm_a31 focus = VIE_apm_radar }` (một trong ba focus Trục 2, đúng mẫu hải quân). `available`: `date > 2011.12.31` và `OR = { VIE_var_air_delivered > 11, date > 2014.12.31 }` (hết cửa sổ Su-30 cuối thì tự phát triển).

## A2 · D-E của nhánh B và C đọc biến của 1B, mà 1B chưa tồn tại

Bản 1.4: B cần `VIE_var_air_multirole4 ≥ 12` (chỉ 1B P2 ghi), C cần `VIE_var_uav_delivered ≥ 4` (chỉ 1B P9 ghi). Không có 1B thì D-E của B và C không bao giờ bấm được, chương trình đỉnh của hai trong ba nhánh bị khóa. Nhánh A: `VIE_var_sam_lr ≥ 1` chỉ tăng khi S-300 giao (lại thiếu dự phòng như A1).

**Sửa:** mức đầu của D-E dùng chỉ dữ liệu Trục 1–2 đã có; mức hai (thưởng cao hơn) mới đọc 1B, nên 1B ra sau chỉ mở thêm thưởng, không mở khóa.

| Nhánh | Mức 1 (bấm được) | Mức 2 (thưởng +50%) |
|---|---|---|
| A | (`VIE_var_sam_lr ≥ 1` hoặc `VIE_apm_a31_tier ≥ 2`) và `VIE_apm_radar_tier ≥ 2` | `VIE_var_sam_lr ≥ 3` (hai tiểu đoàn S-300 của Trục 1 đã cho 2; cần 1B P8) |
| B | `VIE_var_air_delivered ≥ 24` và `VIE_apm_a32_tier ≥ 2` | `VIE_var_air_multirole4 ≥ 12` (1B P2) |
| C | `VIE_apm_uav_tier ≥ 2` | `VIE_var_uav_delivered ≥ 4` (1B P9) |

Tuân R11: Trục 3 chỉ đọc biến của 1B để cộng thưởng, không dùng làm cổng.

## A3 · "Phòng không" và "phòng thủ" của 7.5 không có token riêng, và biến modifier đang dùng chung

- 12.2 báo cáo thừa nhận dòng "phòng không" chưa có token. Hiện `air_defence_factor` (= "Air Defense") đã bị Trục 1 không quân (0,06), Trục 2 (0,04) và lục quân (Igla 0,05 + TL-01 0,03) cộng chung, tổng 0,18 trên trần 0,20. Nếu Trục 3 cũng cộng vào đó (nhánh A ≈ 0,175) thì vượt hẳn.
- `VIE_armed_forces_modifier` thiếu `air_attack_factor` (T2, D-A, B2…) và `airforce_personnel_cost_multiplier_modifier` (D-D), và chưa có khóa tooltip `VIE_tt_*` cho `experience_gain_air_factor`, `air_superiority_efficiency`, `air_home_defence_factor`, `air_intercept_efficiency`. Hai token mới đã xác nhận có trong MD/HOI4 (`air_attack_factor` trong `modifiers_documentation.md`, `airforce_personnel_cost_multiplier_modifier` trong `money_modifier_definitions.txt`).
- Detection là biến dùng chung: Trục 1 (tối đa 0,05) + Trục 2 (0,06) = 0,11 trên trần 0,20, nên Trục 3 chỉ còn **0,09**. Bản 1.4 đặt 0,165 cho nhánh C và nhánh A.

**Sửa:**
1. "Phòng không" của Trục 3 = `air_home_defence_factor` ("Home defence", đã nằm sẵn trong modifier, chưa ai dùng). "Phòng thủ" = `air_intercept_efficiency` (cũng nằm sẵn, chưa ai dùng). **Trục 3 không đụng `air_defence_factor`**, nên khoản #3 còn treo của review Trục 1–2 (trần phòng không) tự hết: 0,18 ≤ 0,20, không cần bạn chọn nữa.
2. Thêm 2 dòng vào `VIE_armed_forces_modifier` (ngoài khối `GEN`) và 6 khóa `VIE_tt_*` (bước 0).
3. Hạ phát hiện của Trục 3 xuống 4,5% ở phần chung và 4% ở nhánh A/C (bảng 4.5). Làm theo quy tắc của báo cáo: **hạ giá trị, không nâng trần**.

## A4 · Phần thưởng "mở 1B" gọi `unlock_decision_tooltip` tới Decision chưa tồn tại

7.2: T7 mở P1, P6, P7; A2 mở P8, P10; A3 mở P4; B2 mở P2, P3; B4 mở P5; C2 mở P9; C3 mở P4, P10. 1B chưa có, tooltip tới Decision không tồn tại sinh lỗi.
**Sửa:** bỏ các dòng này khỏi reward khi code Trục 3. Việc 1B đọc `has_completed_focus` của các focus này (như hải quân: quyền mở ghi ở `available` của Decision 1B, không ở focus) đã đủ; khi dựng 1B thì thêm `unlock_decision_tooltip` một lần.

---

# PHẦN 3 — 4 CHỖ LỆCH VỚI TRỤC 1–2 VÀ MOD

| # | Lệch | Sửa |
|---|---|---|
| B1 | R9 và 3.2 B3 còn nói "đếm lại slot sau nội chiến" và 4.2 nhắc hook. Hook `VIE_collapse_aftermath` đã bỏ. | Bộ đếm `VIE_var_airf_program_active` tự chữa bằng `VIE_airf_slot_heal` (monthly, cùng scheduler với `VIE_apm_slot_heal`): đặt 0 khi không còn timed idea `VIE_airf_prog_*` nào **và** không có cờ `VIE_airf_d?_pending`. Cờ chờ không hết hạn trong 2 ngày: dùng 30 ngày, xóa bởi mọi option (bài học review Trục 2, lỗi #5). |
| B2 | Báo cáo dùng `VIE_air_force_category`, trùng tiền tố `VIE_air_` mà 4.3 cấm (roster chỉ huy). Trục 2 dùng `VIE_apm_category`. | Đổi thành `VIE_airf_category`, `priority = 86` (86 chưa dùng; 87 Trục 2 không quân, 88 hợp tác an ninh biển, 89 1B hải quân). Cổng: `has_completed_focus = VIE_airf_training_standardization`. |
| B3 | `VIE_ap_training_standardized` (Trục 1) đang là `always = no`, chờ T1; E13 option c và E15 giá rẻ đều đọc nó. | Bước 3: đổi thành `has_completed_focus = VIE_airf_training_standardization`. Đây là cạnh ngược duy nhất Trục 3 → Trục 1 (chỉ thưởng, không gate). |
| B4 | `ai_free`: bản 1.4 viết "chỉ khi `VIE_ai_free`" cho nhánh B, C và UAV. `VIE_ai_free` **chưa được định nghĩa** (lỗi có sẵn của 1B). | Dùng mẫu đang chạy của Trục 2 và hải quân: `modifier = { factor = 0 VIE_ai_historical = yes }` (trigger này luôn đúng, nên AI không bao giờ đi B/C). Nhánh A là mặc định của AI. Không thêm `VIE_ai_free` mới. |

Lưu ý nhỏ: báo cáo ghi D-E "nhân thưởng nhánh ×1,0/×1,5". Hải quân thực tế: focus B5 cho thưởng gốc, D-E cộng thêm **25% (mức 1) hoặc 50% (mức 2)** của thưởng gốc. Trục 3 không quân làm y như vậy: focus capstone A4/B5/C5 cho thưởng gốc (+XP), D-E cộng +0,25× / +0,5×. Tổng tối đa = ×1,5, trùng ý bản gốc.

---

# PHẦN 4 — THIẾT KẾ V19 (TÀI LIỆU LỊCH SỬ, KHÔNG PHẢI QUAN HỆ CODE HIỆN HÀNH)

## 4.1 Hai mươi hai Focus (tọa độ tuyệt đối, đã kiểm trống)

Neo: tất cả vào **T1** (`relative_position_id = VIE_airf_training_standardization`, khai báo trước các focus còn lại); T1 neo `VIE_modernize_vpa` (266, 1) với `x = 36, y = 1` → (302, 2). Vùng x ≥ 298 và y 2–13 hoàn toàn trống (cây live: Trục 2 không quân ở x 290–296 y 3–8; lục quân Trục 3 tới x 284; khối `VIE_sec_*` ở y ≥ 24). Đã kiểm: không đè focus nào, cùng hàng cách nhau ≥ 4 (thực tế ≥ 6), con luôn `y >` cha.

| Mã | ID | Tên | (dx,dy) → abs | Prerequisite | `available` |
|---|---|---|---|---|---|
| T1 | `VIE_airf_training_standardization` | Chuẩn hóa đào tạo phi công và kỹ thuật viên | → (302,2) | `VIE_modernize_vpa` | `date > 2004.12.31` |
| T2 | `VIE_airf_fighter_force` | Phát triển lực lượng tiêm kích | (−4,1) → (298,3) | T1 | `date > 2007.12.31` |
| T3 | `VIE_airf_sam_force` | Phát triển lực lượng tên lửa phòng không và radar | (+4,1) → (306,3) | T1 | `date > 2005.12.31` |
| T4 | `VIE_airf_command_reform_1` | Cải cách chỉ huy PK-KQ I | (0,2) → (302,4) | T2 **và** T3 | `date > 2009.12.31` |
| T5 | `VIE_airf_first_force` | Cơ cấu lực lượng ban đầu | (0,3) → (302,5) | T4 **và** (một trong `VIE_apm_a32`, `VIE_apm_a31`, `VIE_apm_radar`) | `date > 2011.12.31`; `OR = { VIE_var_air_delivered > 11, date > 2014.12.31 }` |
| T6 | `VIE_airf_command_reform_2` | Cải cách chỉ huy PK-KQ II | (0,4) → (302,6) | T5 | `date > 2013.12.31` |
| T7 | `VIE_airf_medium_force` | Lực lượng không quân trung bình | (0,5) → (302,7) | T6 | `date > 2015.12.31` |
| T8 | `VIE_airf_operating_range` | Mở rộng bán kính hoạt động và căn cứ tiền phương | (0,6) → (302,8) | T7 | `date > 2017.12.31` |
| A1 | `VIE_airf_iads` | Phòng không tích hợp (loại trừ B1, C1) | (−12,7) → (290,9) | T8 | — |
| A2 | `VIE_airf_layered_defence` | Mạng radar – tên lửa nhiều tầng | (−12,8) → (290,10) | A1 | `date > 2019.12.31` |
| A3 | `VIE_airf_ew_antistealth` | Tác chiến điện tử và chống tàng hình | (−12,9) → (290,11) | A2 | `date > 2021.12.31` |
| A4 | `VIE_airf_iads_command` | Bộ chỉ huy phòng không khu vực | (−12,10) → (290,12) | A3 | `date > 2024.12.31` |
| B1 | `VIE_airf_multirole` | Không quân đa nhiệm (loại trừ A1, C1) | (0,7) → (302,9) | T8 | — |
| B2 | `VIE_airf_multirole_fleet` | Chương trình tiêm kích đa nhiệm 4.5 | (−6,8) → (296,10) | B1 | `date > 2024.12.31` |
| B3 | `VIE_airf_sustainment` | Bảo đảm kỹ thuật đa nguồn | (0,8) → (302,10) | B1 | `date > 2022.12.31` |
| B4 | `VIE_airf_airlift_tanker` | Vận tải và tiếp dầu trên không | (+6,8) → (308,10) | B1 | `date > 2026.12.31` |
| B5 | `VIE_airf_multirole_wing` | Cánh không quân đa nhiệm | (0,9) → (302,11) | B2, B3, B4 (ba khối riêng = AND) | `date > 2028.12.31` |
| C1 | `VIE_airf_unmanned` | Không người lái và mạng hóa (loại trừ A1, B1) | (+16,7) → (318,9) | T8 | — |
| C2 | `VIE_airf_isr_uav` | UAV trinh sát và mục tiêu | (+12,8) → (314,10) | C1 | `date > 2020.12.31` |
| C3 | `VIE_airf_datalink` | Mạng liên kết dữ liệu (C4ISR) | (+20,8) → (322,10) | C1 | `date > 2022.12.31` |
| C4 | `VIE_airf_strike_uav` | UAV tấn công | (+12,9) → (314,11) | C2 | `date > 2025.12.31` |
| C5 | `VIE_airf_teaming` | Phối hợp có người – không người | (+16,10) → (318,12) | C3 **và** C4 (khối riêng) | `date > 2029.12.31` |

`FOCUS_FILTER_AIRCRAFT`, cost 7 cho chuỗi (10 cho capstone), icon generic tạm. `ai_will_do`: 60 cho chuỗi; A1 = 40; B1, C1 `factor = 0 VIE_ai_historical = yes`; `factor = 0` khi `bankruptcy_incoming_collapse`. Cổng một chiều không quân → Biển Đông (Q7) là việc phía Biển Đông đọc `has_completed_focus = VIE_airf_operating_range`; Trục 3 không viết gì thêm.

## 4.2 Phần thưởng focus (đã đổi token theo A3, bỏ mở 1B theo A4)

Ký hiệu: EXP `experience_gain_air_factor`, ATK `air_attack_factor`, SUP `air_superiority_efficiency`, CAS `air_cas_efficiency`, MIS `air_mission_efficiency`, RNG `air_range_factor`, DET `air_detection`, HOME `air_home_defence_factor`, INT `air_intercept_efficiency`, PERS `airforce_personnel_cost_multiplier_modifier`. XP dùng helper `VIE_airf_xp_10/15/20/25` (mastery `folder = air` nếu đã chọn học thuyết, không thì `air_experience`).

| Focus | Thưởng | Mở |
|---|---|---|
| T1 | XP 15; EXP +4% | category `VIE_airf_category` (tooltip) |
| T2 | ATK +1% | D-A |
| T3 | HOME +2% | D-B |
| T4 | MIS +2% | D-C |
| T5 | XP 10 | D-D |
| T6 | MIS +2%, DET +1% | — |
| T7 | RNG +3% | — |
| T8 | RNG +4%, DET +1% | ba nhánh |
| A1 / A2 / A3 / A4 | HOME +2% / DET +2%, HOME +2% / INT +3%, DET +2% / MIS +2%, HOME +2% | A4: D-E |
| B1 / B2 / B3 / B4 / B5 | RNG +4% / ATK +3%, SUP +2%, CAS +2% / MIS +2% / RNG +3% / MIS +2%, ATK +2% | B5: D-E |
| C1 / C2 / C3 / C4 / C5 | DET +1% / DET +3% / MIS +2% / ATK +3% / MIS +2%, INT +2% | C5: D-E |
| A1, B1, C1 thêm | lệch/đúng nhánh theo `VIE_airf_force_priority` (7.4): lệch → timed idea 365 ngày (MIS −3%, DET −3% ⇒ dùng idea, không qua biến); đúng → MIS +1% | — |

## 4.3 Năm Decision (category `VIE_airf_category`, priority 86)

Mỗi Decision: `cost = 50` (D-E 60), `fire_only_once = yes`, `available` có `custom_trigger_tooltip` cho slot và từng điều kiện, `complete_effect` = log + cờ chờ 30 ngày + `VIE_airf_program_start` + bắn chuỗi; `ai_will_do` base 100, `factor = 0` khi `bankruptcy_incoming_collapse`.

| Decision | Mở từ | `available` | Chuỗi chọn | Hoàn tất |
|---|---|---|---|---|
| D-A `VIE_airf_d1_fighters` | T2 | slot | `.1` mức (Cơ bản 0,40 tỷ / 12 tháng; Chuyên sâu 0,60 / 18) → `.2` chuyên môn (Không chiến / Tấn công mặt đất–biển) | `.61` ẩn: modifier theo bảng 4.4, `VIE_airf_d1_done`, −1 slot |
| D-B `VIE_airf_d2_sam` | T3 | slot | `.10` định hướng (Lịch sử 0,30 / Sớm 0,50, đặt `VIE_airf_sam_orientation` ngay) → `.11` mức (×1,0 / ×1,5) | `.62` ẩn, `VIE_airf_d2_done` |
| D-C `VIE_airf_d3_coordination` | T4 | slot; `d1_done`; `d2_done` | không chọn: 0,50 tỷ / 18 tháng | `.50` ẩn (giai đoạn 1), `.51` ẩn (giai đoạn 2), `.63` ẩn (giai đoạn 3) |
| D-D `VIE_airf_d4_first_force` | T5 | slot | `.30` ba cơ cấu (1 Phòng thủ lãnh thổ, 2 Cân bằng, 3 Tầm xa): 0,60 tỷ / 12 tháng, đặt `VIE_airf_force_priority` | `.64` ẩn |
| D-E `VIE_airf_d5_capstone` | A4, B5 hoặc C5 | slot; cổng nhánh mức 1 (A2) | không chọn: 1,0 tỷ / 18 tháng | `.65` ẩn: +0,25× (mức 1) hoặc +0,5× (mức 2) thưởng của focus capstone |

Event hoàn tất là `hidden = yes` hoặc `minor_flavor` như hải quân; hẹn giờ bằng `days = <biến tạm>` (đã được MD xác nhận cho `country_event` và `add_timed_idea`). Chuỗi chọn do người chơi bấm nên miễn `VIE_popup_cd`. Số event chọn: 6 (`.1 .2 .10 .11 .30` và D-E không chọn), cộng 7 event ẩn/nhỏ.

## 4.4 Hiệu ứng Decision (đã đổi token)

| Nguồn | Hiệu ứng |
|---|---|
| D-A × Không chiến, mức 1/2 | SUP +3% / +4,5% |
| D-A × Tấn công đất/biển, mức 1/2 | CAS +3% / +4,5%; ATK +1% / +1,5% |
| D-B mức 1/2 | HOME +3% / +4,5%; DET +1% / +1,5% (Sớm: HOME +1% thêm) |
| D-C ba giai đoạn | MIS +2%; HOME +2%, SUP +2%; DET +1%, MIS +2% |
| D-D Phòng thủ | INT +3%, HOME +2%, RNG −3% |
| D-D Cân bằng | ATK +1%, INT +1%, RNG +1% |
| D-D Tầm xa | RNG +5%, MIS +2%, PERS +3% |

## 4.5 Ngân sách modifier (biến dùng chung, tổng mọi trục)

| Token | Trần | Trục khác đã dùng | Dành cho Trục 3 | Trục 3 tối đa (A / B / C) |
|---|---:|---|---:|---|
| EXP | 10% | (timed idea Trục 1–2 là tạm thời) | 10% | 4 / 4 / 4 |
| ATK | 10% | — | 10% | 3,5 / 9,5 / 6,5 |
| SUP | 10% | — | 10% | 6,5 / 8,5 / 6,5 |
| CAS | 10% | — | 10% | 4,5 / 6,5 / 4,5 |
| MIS | 16% | — | 16% | 13 / 16 / 16 |
| RNG | 20% | — | 20% | 12 / 19 / 12 |
| **DET** | **20%** | **Trục 1 + 2 = 11%** | **9%** | **8,5 / 4,5 / 8,5** |
| HOME | 20% | — | 20% | 18,5 / 11,5 / 11,5 |
| INT | 8% | — | 8% | 6 / 3 / 6 |
| PERS | +3% (chi phí) | — | 3% | 3 (chỉ D-D Tầm xa) |
| `air_defence_factor` | 20% | Trục 1 0,06 + Trục 2 0,04 + lục quân 0,08 = 18% | **0** | không dùng |

Các tổng đã tính bằng script thử (mọi tổ hợp nhánh × chuyên môn × cơ cấu D-D, mức hai, D-E +50%): **tất cả dưới trần**. Bước 0 biến script này thành `tools/audit/air_force_balance.py` và thêm phần cộng chéo Trục 1–2–lục quân để kiểm `air_defence_factor` và DET luôn.

## 4.6 Hợp đồng cờ/biến giữa các trục

| Cạnh | Qua | Ghi chú |
|---|---|---|
| Trục 1 → Trục 3 | `VIE_var_air_delivered` (T5), `VIE_var_sam_lr` (D-E A) | luôn có dự phòng theo ngày hoặc theo bậc Trục 2 (A1, A2) |
| Trục 2 → Trục 3 | `has_completed_focus` của `VIE_apm_a32/_a31/_radar` (T5); `VIE_apm_a32_tier`, `_a31_tier`, `_radar_tier`, `_uav_tier` (D-E) | một chiều |
| Trục 3 → Trục 1 | `VIE_ap_training_standardized` (B3) | chỉ thưởng |
| Trục 3 → Trục 2 | không | R5 |
| 1B → Trục 3 | `VIE_var_air_multirole4`, `_sam_lr ≥ 2`, `_uav_delivered` | chỉ mức 2 của D-E |
| Trục 3 → 1B | `has_completed_focus` của T7, A2, B2… đọc ở `available` của Decision 1B | 1B làm sau |
| Trục 3 → Biển Đông | `has_completed_focus = VIE_airf_operating_range` | Biển Đông đọc |

Biến/cờ mới (tiền tố `VIE_airf_`, mọi cái đều có người đọc): `VIE_var_airf_program_active` (0–2); `VIE_airf_fighter_level`, `VIE_airf_fighter_specialty`, `VIE_airf_sam_level`, `VIE_airf_sam_orientation`, `VIE_airf_force_priority`; cờ `VIE_airf_d1_done`, `VIE_airf_d2_done` (D-C đọc), `VIE_airf_d1_pending`, `_d2_pending`, `_d4_pending`. Idea: `VIE_airf_prog_fighters/_sam/_coord/_first/_capstone` (timed, chỉ báo đang chạy), `VIE_airf_branch_mismatch_idea` (365 ngày). Trigger mới (file `VIE_md_triggers_air_force.txt`): `VIE_airf_slot_free`, `VIE_airf_branch_a/_b/_c` (= `has_completed_focus`), `VIE_airf_capstone_ok_a/_b/_c` (mức 1), `VIE_airf_capstone_lvl2_a/_b/_c`.

## 4.7 AI

Focus: 4.1. Decision: base 100, `factor 0` khi `bankruptcy_incoming_collapse`. Event: option Cơ bản / Lịch sử `base 90` + `add 100 VIE_ai_historical`; option khác `modifier = { factor = 0 VIE_ai_historical = yes }` và guard `bankruptcy_incoming_collapse`, `ai_has_high_deficit`. Mỗi option có ít nhất một đường chọn được (bài học zero-weight).

---

# PHẦN 5 — PLAN CODE (9 bước, nhánh `claude/air-truc3`)

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `common/dynamic_modifiers/VIE_md_dynamic_modifiers.txt` (+`air_attack_factor`, +`airforce_personnel_cost_multiplier_modifier`, ngoài `GEN`); `localisation/english/replace/VIE_md_vi_tt_l_english.yml` (+6 khóa: `VIE_tt_experience_gain_air_factor`, `_air_attack_factor`, `_air_superiority_efficiency`, `_air_home_defence_factor`, `_air_intercept_efficiency`, `_airforce_personnel_cost`); `tools/audit/air_force_balance.py`; `common/scripted_triggers/VIE_md_triggers_air_force.txt` | Hạ tầng modifier, trigger, script cân bằng cộng chéo | `air_force_balance.py` PASS; brace; `verify_all_loc.py` sạch |
| **1** | `common/scripted_effects/VIE_md_effects_air_force.txt` | `VIE_airf_xp_*`, `VIE_airf_dm_tt`, `VIE_airf_add_*` (ghi `VIE_af_*` + `force_update_dynamic_modifier`), `VIE_airf_program_start/end`, `VIE_airf_slot_heal`, `VIE_airf_start_timer`, chi phí/thời gian như `VIE_apm_*` | scan effect chưa định nghĩa |
| **2** | `common/national_focus/VIE_md_focus.txt` + loc | Chuỗi chung T1–T8, reward theo 4.2 | `audit.py`: 0 dangling/forward-ref/cycle/trùng toạ độ; chạy `live.py` bản sed |
| **3** | cùng file; `VIE_md_triggers_air_proc.txt` | 14 focus nhánh (ME A1/B1/C1; phạt/thưởng lệch/đúng nhánh), icon generic; đổi `VIE_ap_training_standardized` | `audit.py` 22/22; `ev.py` |
| **4** | `common/decisions/VIE_md_air_force_decisions.txt`, category `VIE_airf_category` (priority 86), `common/ideas/VIE_md_ideas_air_force.txt`, `events/VIE_air_force.txt` (`add_namespace = vie_air_force`) | D-A (`.1 .2 .61`) và D-B (`.10 .11 .62`) | `ev.py`; tooltip `VIE_airf_slot_tt` |
| **5** | cùng file | D-C (`.50 .51 .63`), D-D (`.30 .64`), D-E (`.65`) với cổng 2 mức (A2) | slot ≤ 2; D-C cần cả `d1_done` và `d2_done` |
| **6** | `common/on_actions/VIE_md_on_actions.txt` (+`VIE_airf_slot_heal = yes`); loc `VIE_md_events_air_force_l_english.yml` (focus + decision + event + tooltip, BOM, `:0`) | Nối scheduler tháng, loc toàn bộ | `verify_all_loc.py` ZERO errors |
| **7** | `tools/build_vie_air_event_pictures.py`, `tools/build_vie_focus_icons.py` | Ảnh cho 6 event chọn (Commons, giấy phép tự do, ghi CREDITS) và icon cho 29 focus (7 Trục 2 + 22 Trục 3) | không lỗi `texturefile` |
| **8** | `tools/TESTING.md`; `VIE_v9_flag_mapping.md` (mục "Truc 3 khong quan"); cập nhật báo cáo | Checklist thử + bảng cờ | `ev.py`, `audit.py`, `air_force_balance.py` sạch |
| **9** | rà soát `ai_chance` / `ai_will_do` | Không option nào mọi trọng số 0; AI đi A, không đi B/C | script quét option |

Ước lượng: 22 focus, 5 Decision, 13 event (6 chọn + 7 ẩn/nhỏ), ~600 dòng script, ~140 khóa loc, ~8 trigger, 6 idea.

Lỗi cần tránh khi code (rút từ review Trục 1–2): cờ chờ 30 ngày thay vì 2 ngày, xóa bởi mọi option; `slot_heal` bỏ qua khi có cờ chờ; mọi `add_to_variable` modifier kèm `force_update_dynamic_modifier`; mọi cổng đọc hợp đồng tùy chọn có đường dự phòng; file mới ghi CRLF.

---

# PHẦN 6 — QUYẾT ĐỊNH CẦN BẠN CHỐT (mặc định đã gắn; chỉ trả lời khi muốn đổi)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q-C1 | "Phòng không" = `air_home_defence_factor`, "phòng thủ" = `air_intercept_efficiency`, Trục 3 không dùng `air_defence_factor` | **Có** (khoản #3 treo của Trục 1–2 tự hết) | Dùng `air_defence_factor`: phải hạ phòng không Trục 3 xuống 2% hoặc nâng trần 0,20 |
| Q-C2 | D-E mức 1 chỉ đọc Trục 1–2, mức 2 đọc 1B (A2) | **Có** | Đòi 1B cho cả mức 1: Trục 3 nhánh B, C bị khóa tới khi dựng 1B |
| Q-C3 | Cột Trục 3 đặt x 290–322, T1 neo `x = 36` so với `VIE_modernize_vpa` | **Có** | Đặt x ≤ 200 (bên trái hải quân): đổi một dòng neo |
| Q-C4 | Category `VIE_airf_category`, priority 86 | **Có** | Đổi một dòng |
| Q-C5 | T5 đòi một trong ba focus Trục 2 (không chỉ A32) | **Có** | Chỉ A32: người không muốn làm A32 bị chặn |
| Q-C6 | Capstone A4/B5/C5 cho thưởng gốc, D-E cộng +25% / +50% (giống hải quân) | **Có** | Đổi hệ số trong `VIE_airf_d5_finish` |

---

# PHẦN 7 — CHECKLIST THỬ TRONG GAME (đưa vào `tools/TESTING.md` ở bước 8)

- [ ] `error.log`: grep `VIE_airf_`, `vie_air_force`, `air_attack_factor`, `airforce_personnel_cost`, `air_home_defence`.
- [ ] Cây focus: cột Trục 3 ở x 298–322, y 2–12, không đè Trục 2 (x 290–296); A1/B1/C1 loại trừ nhau.
- [ ] T5: mở khi T4 xong và một trong ba focus Trục 2; với SOV bị loại khỏi thế giới (`VIE_var_air_delivered` = 0) T5 vẫn mở sau 2014-12-31.
- [ ] D-A…D-D: tiền trừ, timed idea hiện, modifier xuất hiện đúng lúc; bấm hai lần liên tiếp không mở hai chương trình; slot ≤ 2.
- [ ] D-E: mức 1 bấm được với dữ liệu Trục 1–2 thuần (không 1B); thưởng +25%; mức 2 khi có biến 1B (thử bằng console `set_variable`).
- [ ] Detection tổng (Trục 1+2+3) ≤ 20% ở đường A và C đầy đủ; `air_defence_factor` không đổi so với trước Trục 3.
- [ ] `VIE_ap_training_standardized` trở thành đúng sau T1: E15 (T-6C) rẻ hơn, option `.13.c` hiện.
- [ ] Mismatch: D-D cơ cấu 1 rồi chọn B1 → timed idea phạt 365 ngày; cơ cấu 3 rồi chọn B1 → +1% nhiệm vụ.
- [ ] Quan sát AI tới 2030: đi nhánh A, không bao giờ B/C, không kẹt slot.

---

# TIẾN ĐỘ CODE (2026-10-03)

- **Bước 0–3 xong** (chưa chạy trong game): hạ tầng modifier, helper, 22 focus (chuỗi chung + 14 nhánh), loc, `air_force_balance.py` (22/22 focus khớp bảng, ALL PASS).
- Hai chỗ lệch nhỏ so với bảng 4.2, vì trần MIS 16%: C3 `VIE_airf_datalink` MIS +2% (thay vì +3%); thưởng "đúng nhánh" là MIS +1% (A1 khớp cơ cấu 1; B1, C1 khớp cơ cấu 3) bằng `VIE_airf_branch_fit_a/_wide`, còn cơ cấu 2 hoặc chưa chọn là trung tính. Lệch nhánh = timed idea 365 ngày.
- `VIE_ap_training_standardized` (Trục 1) đã đổi sang `has_completed_focus = VIE_airf_training_standardization`.
- **Bước 4–5 xong**: 5 Decision (`VIE_md_air_force_decisions.txt`), 12 event (`events/VIE_air_force.txt`: 5 chọn `.1 .2 .10 .11 .30`, 2 ẩn `.50 .51`, 5 thông báo `.61–.65`), `unlock_decision_tooltip` ở T2–T5 và A4/B5/C5; `air_force_balance.py` có thêm mục 5 đối chiếu Decision (ALL PASS). Cổng B của D-E thêm `OR date > 2030.12.31` (hợp đồng Su-30 tùy chọn). `VIE_airf_slot_heal` chỉ chờ cờ của D-A, D-B, D-D (D-C và D-E không có khoảng giữa bấm và chọn).
- **Bước 6–8 xong**: `VIE_airf_slot_heal` nối vào on_monthly; ảnh cho 5 event chọn (`vie_air_force.1 .2 .10 .11 .30`, plan ghi 6 nhưng chỉ có 5 event chọn) và icon ảnh thật cho 29 focus (7 Trục 2 + 22 Trục 3) bằng `tools/build_vie_air_focus_icons.py` (tái dùng ảnh Commons đã tải, ghi giấy phép vào `assets/focus_icons/CREDITS.json`); mục TESTING "Air force (Truc 3)" và bảng cờ trong `VIE_v9_flag_mapping.md`.
- Còn: bước 9 (rà AI), chạy thử trong game theo TESTING.md, commit.
- **Bước 9 xong**: `tools/audit/air_ai_options.py` quét mọi event có lựa chọn của Trục 1–3: mọi event còn ít nhất một option AI chọn được (option lịch sử `base 90` + `add 100`); các option không lịch sử đều `factor = 0 VIE_ai_historical`, nên AI không đi nhánh B/C, UAV bậc 2–3 hay option phi lịch sử. 3 cặp "conditional zero" (`vie_air_ind.13`, `.21`, `vie_air_proc.11`) bù nhau với `trigger` của option kia nên an toàn.

---

## Phần 6: Chi tiết Scripted Effects & Kế hoạch Triển khai

# EFFECT NHÁNH KHÔNG QUÂN — NỘI DUNG CHI TIẾT + PLAN CODE

> **Ghi chú lịch sử PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản v18 có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


> Mục tiêu: đưa effect của nhánh không quân (Trục 2 CNQP: 7 focus `VIE_apm_*`; Trục 3 lực lượng: 22 focus `VIE_airf_*`) lên mức chi tiết của lục quân (`VIE_lf_*`, 30 node) và hải quân (`VIE_nf_*`, 22 node + 6 node Trục 2, đã code ở commit `f07ac5d`).
> Nguồn đối chiếu: lục quân `VIE_md_effects_p17.txt`, `VIE_md_decisions_lf.txt`; hải quân `VIE_md_effects_nav_force.txt`, `VIE_md_effects_nav_ind.txt` (dòng 436–472), `VIE_md_decisions_nf_drills.txt`, `VIE_naval_effects_content_and_plan.md`; không quân `VIE_md_focus.txt` (dòng 11097–12097), `VIE_md_effects_air_force.txt`, `VIE_md_effects_air_ind.txt`, `VIE_md_air_force_decisions.txt`, `VIE_air_truc2/3_review_and_plan.md`, `VIE_air_force_content_report.md`.
> Ngày: 2026-10-05. **Chưa sửa dòng code mod nào.** Số liệu Phần 2–4 và 6 đã được kiểm bằng script `tools/audit/air_effects_v2_check.py` (file mới, chỉ là công cụ kiểm; bước 0 gộp nó vào `air_force_balance.py`).
> Trục 1 (mua sắm, sự kiện) và Trục 1B (chưa dựng) **ngoài phạm vi**, giống tài liệu hải quân.

---

# PHẦN 0 — HIỆN TRẠNG: KHÔNG QUÂN THIẾU GÌ SO VỚI LỤC QUÂN VÀ HẢI QUÂN

| Hạng mục | Lục quân | Hải quân (đã code) | Không quân (hiện tại) |
|---|---|---|---|
| Nơi đặt effect | `VIE_lf_<mã>_reward` ×30 | `VIE_nf_<mã>_reward` ×22, `VIE_nav_f<n>_reward` ×6 | Viết thẳng trong `completion_reward`, lặp 4 dòng (`ensure` + `dm_tt` + `add_to_variable` + `force_update`) cho **mỗi** modifier |
| XP | Hầu hết node | Mọi node | **5/22** node Trục 3 (T1, T5, A4, B5, C5); Trục 2 chỉ XP 10 và còn gọi thẳng `air_experience = 10`, bỏ qua nhánh `add_mastery` khi đã chọn học thuyết |
| Political power / command power | N1 +25, N2 +15 CP, `def_industry_law` +50 | T1 +25, capstone +50, 4 node CP | **0 node** |
| Cái giá ở node đầu hướng | FM1, FR1, FD1… | D1 range −2%, G1/B1 personnel cost | A1/B1/C1 chỉ có thưởng/phạt `branch_fit`, **không có khoản âm** |
| Hướng đã chọn đổi effect node sau | CR2, L1/L2, A1/A2… | T7 đọc `VIE_nf_force_priority` | Chỉ A1/B1/C1 đọc `VIE_airf_force_priority`; T6, B2 và các node giữa không đọc gì |
| Giảm cost theo hướng | `VIE_lf_fav_discount` | `VIE_nf_fav_discount` (trong `d4_finish`) | Không có |
| Tech bonus | — | 4 node (xem Phần 7, rủi ro R1) | Không có |
| Mốc lịch sử → giảm cost | 5 event | 3 event | 0 event cho Trục 2/3 |
| Decision huấn luyện lặp lại | 6 | 4 | **0** (5 Decision lực lượng đều `fire_only_once`) |
| Số chiều modifier mới | — | thêm 3 (`hit_chance`, `capital_ship_atk/def`) | thêm 3 chưa dùng (Phần 1.2) |
| Công cụ cân bằng | `lf_balance.py` | `nf_balance.py` (PASS) | `air_force_balance.py` **FAIL 28 dòng**, `air_ind_balance.py` **FAIL 16 dòng** (xem dưới) |

## Hai phát hiện ngoài phạm vi "thiếu effect"

1. **Hai script cân bằng không quân đang hỏng, không phải do con số sai.** Commit `f51d488` ("uodate", 2026-10-03) đã bung mọi lời gọi `VIE_airf_add_exp = { V = 0.04 }` thành khối inline; script vẫn tìm dạng cũ nên mục 4 và 5 của `air_force_balance.py` đọc ra `{}` (28 FAIL). `air_ind_balance.py` mục 5 không đọc được chi phí/thời gian trong event (16 FAIL; cần mở ra xem nguyên nhân chính xác ở bước 0). Hậu quả: bảng 4.2 của review Trục 3 hiện **không còn được máy kiểm** so với code. Bước 0 sửa việc này trước khi thêm số mới. Mười helper `VIE_airf_add_*` và bốn `VIE_apm_add_*` hiện có **0 nơi gọi** (chỉ còn định nghĩa), nên header ghi "ghi bằng `VIE_airf_add_<token>`" đang sai.
2. **Hải quân có thể đang dùng tên category tech không tồn tại.** `VIE_nf_d2/d3/g2/b2_reward` gọi `add_tech_bonus` với `CAT_as_missiles`, `CAT_sub`, `CAT_atk_sub`, `CAT_frigate`, `CAT_destroyer`. `VIE_repo_health_report.md` (dòng 218) đã ghi `CAT_as_missiles`, `CAT_frigate`… là token "cần tra" và không có trong `MD_all_CATS.json`; MD có `CAT_frigates`, `CAT_destroyers`, `CAT_submarines`, `CAT_attack_submarines`, `CAT_naval_anti_ship_missiles`. Nếu đúng thì 4 tech bonus hải quân không có tác dụng (engine bỏ qua im lặng). Tôi **không sửa** (ngoài phạm vi), nhưng nên xử lý riêng; kế hoạch không quân dưới đây chỉ dùng category đã thấy trong file tech của MD (Phần 3).

Ba chỗ nhỏ khác: (a) comment đầu khối Trục 3 trong `VIE_md_focus.txt:11101` ghi "T1 neo x+36", thực tế `x = 20`; (b) `VIE_airf_iads_command`, `VIE_airf_multirole_wing`, `VIE_airf_teaming`, `VIE_apm_mature` không có `cost` (mặc định 10), đúng ý capstone, chỉ cần ghi comment; (c) T6 và T8 hiện lặp `ensure` + `dm_tt` hai lần trong một reward.

---

# PHẦN 1 — NGUYÊN TẮC VÀ THANG ĐIỂM

## 1.1 Sáu nguyên tắc (giống hải quân, đã chỉnh cho không quân)

1. **Một node = một effect đặt tên**: `VIE_airf_<mã>_reward` (Trục 3: t1…t8, a1…a4, b1…b5, c1…c5) và `VIE_apm_f<n>_reward` (Trục 2: f1…f7). Focus chỉ còn `log` + `unlock_decision_tooltip` (nếu có) + gọi effect. `VIE_ap_ensure_af_modifier` gọi **một lần** ở đầu effect, `VIE_airf_dm_tt` và `force_update_dynamic_modifier` một lần ở cuối.
2. **Mỗi node có hơn một loại hiệu ứng**: modifier + XP, hoặc PP/command power, hoặc tech bonus.
3. **Node đầu hướng trả giá** (A1, B1, C1): một khoản âm đo bằng cùng thang điểm; điểm ròng ≈ 1,7–2,0.
4. **Hướng đã chọn đổi effect node sau**: T6 đọc `VIE_airf_force_priority` (đặt ngay lúc chọn ở `vie_air_force.30`); B2 đọc `VIE_airf_fighter_specialty`; D-D mở giảm cost 14 ngày cho node đầu nhánh khớp.
5. **Mốc lịch sử không khóa ngày**: chỉ giảm cost focus chưa làm, hoặc thưởng nhỏ nếu đã làm (mẫu `VIE_nf_ms*_apply`).
6. **Trục 3 không ghi `VIE_cap_*`/bậc của Trục 2** (R5) và **không đụng `air_defence_factor`** (đã 18/20 từ Trục 1, 2 và lục quân; A3 review Trục 3).

## 1.2 Ba chiều modifier mới

Cả ba **đã khai báo** trong `VIE_armed_forces_modifier` (khối `GEN:vars`, dòng 55–57) và **đã có tooltip** trong `VIE_md_vi_tt_l_english.yml` (dòng 31–33), 0 chỗ nào dùng trước nay; không cần sửa dynamic modifier hay loc tooltip. Dấu: `night`, `wx` là *penalty*, giá trị âm = tốt hơn, tooltip hiển thị `-=` (cùng quy ước `VIE_full_spectrum_idea`: `air_night_penalty = -0.2`).

| Chiều | Biến | Ý nghĩa dùng cho | Trần (đề xuất) |
|---|---|---|---:|
| `air_ace_generation_chance_factor` (ACE) | `VIE_af_air_ace_generation_chance_factor` | Đào tạo phi công, văn hóa huấn luyện (T1, T2, B5, A1, B1, C1, C5, mốc 2011) | 10 |
| `air_night_penalty` (NIGHT) | `VIE_af_air_night_penalty` | Bay đêm, EW, ISR (T4, A3, A4, B3, C1, C2, C5) | 6 |
| `air_weather_penalty` (WX) | `VIE_af_air_weather_penalty` | Mọi thời tiết, bảo đảm kỹ thuật (T7, A2, A3, B1, B3, C2, C3) | 6 |

Lý do chọn: chúng là chiều **chưa dùng** nên không đụng trần B/C đang chạm 16/16 (MIS) và 20/20 (RNG); chúng khớp nội dung lịch sử (Su-30MK2 bay đêm, T-6C/L-39NG đào tạo) và các trait chỉ huy sẵn có (`air_chief_all_weather_*`, `air_high_command_night_operations_*`). Trần là **đề xuất của tôi** theo thang các chiều khác (5–10%), chưa phải dữ kiện lịch sử.

Đổi một trần cũ: `pers` (chi phí duy trì không quân) từ +3 lên **+6** để ngang hải quân (+6); node mới chỉ dùng thêm +2 (B1) và −1 (B3), D-D cơ cấu 3 vẫn +3 (đỉnh B = +4).

Các trần cũ giữ nguyên: exp 10, atk 10, sup 10, cas 10, mis 16, rng 20, det 20, home 20, int 8.

---

# PHẦN 2 — TRỤC 3: NỘI DUNG EFFECT TỪNG FOCUS (22 NODE)

Ký hiệu: **(giữ)** = đã có trong code, không đổi; **(mới)** = thêm. Số trong ngoặc là % modifier. "Điểm" = tổng trọng số của modifier (chưa tính XP/PP/CP/tech bonus), trọng số trong `air_effects_v2_check.py`. Điểm cột "cũ → mới".

## 2.1 Chuỗi dùng chung (8 node)

| Mã | Focus | Modifier | Ngoài modifier | Điểm |
|---|---|---|---|---|
| T1 | `VIE_airf_training_standardization` | EXP +4 (giữ); ACE +3 (mới) | XP 15 (giữ); **+25 PP (mới)** | 2,0 → 4,4 |
| T2 | `VIE_airf_fighter_force` | ATK +1 (giữ); ACE +2 (mới) | **XP 10, tech bonus 0,25 `CAT_air_to_air_weapons` ×1 (mới)**; mở D-A (giữ) | 1,0 → 2,6 |
| T3 | `VIE_airf_sam_force` | HOME +2 (giữ) | **XP 10, tech bonus 0,25 `CAT_surface_to_air_missiles` ×1 (mới)**; mở D-B (giữ) | 1,6 |
| T4 | `VIE_airf_command_reform_1` | MIS +2 (giữ); NIGHT −1 (mới) | **+15 command power (mới)**; mở D-C (giữ) | 2,0 → 3,0 |
| T5 | `VIE_airf_first_force` | — | XP 10 (giữ); **+10 command power (mới)**; mở D-D (giữ) | 0 |
| T6 | `VIE_airf_command_reform_2` | MIS +2, DET +1 (giữ); **theo D-D (mới)**: cơ cấu 1 INT +1 · cơ cấu 2 INT +0,5, RNG +0,5, NIGHT −0,5 · cơ cấu 3 RNG +1 · chưa chọn: không thêm | **XP 10 (mới)** | 2,8 + 0,6–1,2 |
| T7 | `VIE_airf_medium_force` | RNG +3 (giữ); WX −1 (mới) | **XP 10 (mới)** | 1,8 → 2,6 |
| T8 | `VIE_airf_operating_range` | RNG +4, DET +1 (giữ) | **XP 15, +15 command power (mới)** | 3,2 |

T6 đọc `VIE_airf_force_priority` (đặt ngay ở `vie_air_force.30`, không đợi 12 tháng của D-D) nên đúng cả khi người chơi làm T6 trước khi D-D kết thúc; giá trị 0 = không thưởng, không phạt. Giá trị cơ cấu 3 chỉ +1 RNG (không +1,5 như hải quân) vì nhánh B đã chạm RNG 20/20.

**Giảm cost theo D-D** (`VIE_airf_fav_discount`, gọi cuối `VIE_airf_d4_finish`, mẫu `VIE_nf_fav_discount`): cơ cấu 1 (Phòng thủ lãnh thổ) → `VIE_airf_iads` −14 ngày; cơ cấu 3 (Tầm xa) → `VIE_airf_multirole` và `VIE_airf_unmanned` mỗi cái −14 ngày; cơ cấu 2 không giảm. Chỉ áp khi focus tương ứng chưa xong. Giữ nguyên thưởng MIS +1 khi đúng nhánh và timed idea phạt khi lệch nhánh như hiện tại.

## 2.2 Nhánh A — Phòng không tích hợp (lịch sử, 4 node, 19,9 điểm; cũ 12,4)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| A1 | `VIE_airf_iads` | HOME +2 (giữ); INT +0,5, ACE +1,5 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | RNG −2 (mới) | 2,0 |
| A2 | `VIE_airf_layered_defence` | DET +2, HOME +2 (giữ); WX −1, SUP +1,5 (mới) | **XP 10 (mới)** | — | 5,5 |
| A3 | `VIE_airf_ew_antistealth` | INT +3, DET +2 (giữ); NIGHT −1, WX −1, SUP +1 (mới) | **XP 10, tech bonus 0,25 `CAT_air_countermeasures` ×1 (mới)** | — | 6,8 |
| A4 | `VIE_airf_iads_command` (capstone) | MIS +2, HOME +2 (giữ); NIGHT −1, ATK +1 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,6 |

## 2.3 Nhánh B — Đa nhiệm (5 node, 21,6 điểm; cũ 16,8)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| B1 | `VIE_airf_multirole` | RNG +4 (giữ); WX −1, ACE +1 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | PERS +2 (mới) | 2,0 |
| B2 | `VIE_airf_multirole_fleet` | ATK +3, SUP +2, CAS +2 (giữ); **theo `VIE_airf_fighter_specialty` (mới)**: 1 Không chiến SUP +1 · 2 Tấn công đất/biển CAS +1 | **XP 10, tech bonus 0,25 `CAT_medium_aircraft` ×1 (mới)** | — | 6,6 (+0,8–1) |
| B3 | `VIE_airf_sustainment` | MIS +2 (giữ); WX −2, NIGHT −1, PERS −1 (mới; bảo đảm tốt hơn giảm duy trì) | **XP 10 (mới)** | — | 5,6 |
| B4 | `VIE_airf_airlift_tanker` | RNG +3 (giữ) | **XP 15, +10 command power (mới)** | — | 1,8 |
| B5 | `VIE_airf_multirole_wing` (capstone) | MIS +2, ATK +2 (giữ); ACE +2 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,6 |

## 2.4 Nhánh C — Không người lái và mạng hóa (5 node, 19,2 điểm; cũ 11,8)

| Mã | Focus | Modifier | Ngoài modifier | Giá phải trả | Điểm ròng |
|---|---|---|---|---|---:|
| C1 | `VIE_airf_unmanned` | DET +1 (giữ); ACE +1,5, NIGHT −0,5 (mới) | **XP 15 (mới)**; khớp/lệch nhánh (giữ) | HOME −1 (mới) | 1,7 |
| C2 | `VIE_airf_isr_uav` | DET +3 (giữ); NIGHT −1,5, WX −1 (mới) | **XP 10, tech bonus 0,25 `CAT_air_drones` ×1 (mới)** | — | 4,7 |
| C3 | `VIE_airf_datalink` | MIS +2 (giữ); WX −1, SUP +1 (mới) | **XP 10, +10 command power (mới)** | — | 3,8 |
| C4 | `VIE_airf_strike_uav` | ATK +3 (giữ); RNG +1 (mới) | **XP 15 (mới)** | — | 3,6 |
| C5 | `VIE_airf_teaming` (capstone) | MIS +2, INT +2 (giữ); ACE +1, NIGHT −1 (mới) | XP 20 (giữ); **+50 PP (mới)**; mở D-E (giữ) | — | 5,4 |

Tổng chuỗi chung 20,2 điểm (cũ 14,4). Tổng ba nhánh lệch nhau trong ±8% (A 19,9 · B 21,6 · C 19,2). B cao nhất vì đắt nhất và phụ thuộc 1B nhiều nhất; A là hướng lịch sử nên không bị phạt thêm; không cần cân lại nếu bạn chấp nhận Q2.

---

# PHẦN 3 — TECH BONUS (7 CHỖ, TÙY CHỌN)

Dùng `add_tech_bonus = { name = VIE_airf_tb_<…> bonus = 0.25 uses = 1 category = <CAT> }`; `name` duy nhất và cần loc. **Chỉ dùng category có thật trong file tech của MD** (`tools/audit/md_ref/tech_*.txt`), đã đối chiếu từng cái:

| Chỗ | `name` | Category | Có trong |
|---|---|---|---|
| T2 | `VIE_airf_tb_a2a` | `CAT_air_to_air_weapons` | `tech_BBA_aircraft.txt` |
| T3 | `VIE_airf_tb_sam` | `CAT_surface_to_air_missiles` | `tech_missile_defense.txt` |
| A3 | `VIE_airf_tb_ew` | `CAT_air_countermeasures` | `tech_BBA_aircraft.txt` |
| B2 | `VIE_airf_tb_multirole` | `CAT_medium_aircraft` | `tech_BBA_aircraft.txt`, `tech_fixed_wing.txt` |
| C2 | `VIE_airf_tb_uav` | `CAT_air_drones` | `tech_BBA_aircraft.txt`, `tech_fixed_wing.txt` |
| F4 (Trục 2) | `VIE_apm_tb_radar` | `CAT_airborne_early_warning` | `tech_BBA_aircraft.txt`, `tech_bombers.txt` (gần nhất với radar; MD không có category radar mặt đất riêng) |
| F5, F6 (Trục 2) | `VIE_apm_tb_avionics`, `VIE_apm_tb_drones` | `CAT_avionics`, `CAT_drones` | `tech_BBA_aircraft.txt` |

Tech bonus không tính điểm; bỏ cả Phần 3 không làm đổi bảng nào.

---

# PHẦN 4 — TRỤC 2 KHÔNG QUÂN: EFFECT 7 FOCUS

Trục 2 không có "kinh nghiệm công nghiệp" như hải quân (bậc nằm ở biến `VIE_apm_*_tier`, Decision lo), nên effect focus chỉ gồm PP/CP, XP chuẩn hóa và tech bonus, cộng một khoản `accidents` nhỏ. Bậc, MIO, chi phí giữ nguyên.

| Mã | Focus | Effect mới | Giữ nguyên |
|---|---|---|---|
| F1 | `VIE_apm_law` | **+25 PP** | category tooltip; XP 10 (đổi sang `VIE_airf_xp_10`) |
| F2 | `VIE_apm_a32` | **+15 PP**; `air_accidents_factor` −1 (tổng Trục 2 −8 → −9, trần đề xuất −10) | XP 10; mở `VIE_apm_d_a32` |
| F3 | `VIE_apm_a31` | **+10 PP** | XP 10; mở `VIE_apm_d_a31` |
| F4 | `VIE_apm_radar` | **+10 command power**; tech bonus `CAT_airborne_early_warning` | XP 10; mở `VIE_apm_d_radar` |
| F5 | `VIE_apm_integration` | **+10 command power**; tech bonus `CAT_avionics` | XP 10; mở `VIE_apm_d_integ` |
| F6 | `VIE_apm_uav` | tech bonus `CAT_drones` | XP 10; mở `VIE_apm_d_uav` |
| F7 | `VIE_apm_mature` (capstone) | **+50 PP**, `add_war_support` +3% | cờ `VIE_cap_mature_air_industry`; XP 10 |

Không thêm modifier DET/MIS/RNG vào Trục 2: DET đã 11 từ Trục 1+2, A/C đã 19,5/20. Tổng PP Trục 2 = 100; Trục 3 = 25 + 50 = 75 (một capstone). Hải quân: 100 và 75, lục quân cùng cỡ.

Bug nhỏ sửa kèm: F2–F7 hiện gọi `air_experience = 10` trực tiếp; khi đã chọn học thuyết lớn thì XP phải đi vào `add_mastery` (đúng như F1, mọi node Trục 3 và lục quân/hải quân). Dùng `VIE_airf_xp_10` cho cả bảy.

---

# PHẦN 5 — NĂM DECISION HUẤN LUYỆN KHÔNG QUÂN (LẶP LẠI ĐƯỢC)

Mẫu `VIE_dec_nf_train_*` (không `complete_effect`; thưởng ở `remove_effect` sau `days_remove`; `days_re_enable = 545`; category có sẵn `VIE_military_readiness_category`; `available = { has_war = no }`; `ai_will_do` base 15 với `factor 0` khi `VIE_def_ind_bankrupt = yes` hoặc `bankruptcy_incoming_collapse`). Timed idea là hiệu ứng tạm, **không tính vào trần** (cùng quy ước lục quân và hải quân).

| Decision | Hiện khi | PP | Chạy | Thưởng | Ghi chú |
|---|---|---:|---:|---|---|
| `VIE_dec_airf_train_aa` Huấn luyện không chiến | `VIE_airf_fighter_force` | 35 | 90 | +10 XP; SUP +3% 180 ngày | Chung |
| `VIE_dec_airf_train_night` Huấn luyện bay đêm, mọi thời tiết | `VIE_airf_command_reform_1` | 35 | 120 | +10 XP; NIGHT −3%, WX −2% 180 ngày | Chung; đúng nguồn báo Nghệ An về Su-30MK2 bay đêm |
| `VIE_dec_airf_train_sam` Diễn tập phòng không tích hợp | `VIE_airf_layered_defence` | 35 | 90 | +10 XP; HOME +4% 180 ngày | Chỉ nhánh A |
| `VIE_dec_airf_train_strike` Diễn tập đánh mặt đất, mặt biển | `VIE_airf_multirole_fleet` | 40 | 120 | +10 XP; CAS +3%, ATK +1,5% 180 ngày | Chỉ nhánh B |
| `VIE_dec_airf_train_uav` Diễn tập UAV và liên kết dữ liệu | `VIE_airf_datalink` | 35 | 90 | +10 XP; MIS +3% 180 ngày | Chỉ nhánh C |

Cần 5 idea tạm `VIE_airf_idea_aa_drill`, `_night_drill`, `_sam_drill`, `_strike_drill`, `_uav_drill` trong `VIE_md_ideas_air_force.txt` (khác 5 idea chỉ-báo `VIE_airf_prog_*` đang có). Icon: `GFX_decision_generic_form_nation` (đang dùng ở mọi Decision không quân); nếu muốn icon không quân riêng thì kiểm tên trong vanilla trước.

---

# PHẦN 6 — MỐC LỊCH SỬ (BA EVENT, TÙY CHỌN)

Mẫu `VIE_nf_ms*_apply` + `VIE_event_scheduler_nf`: không khóa ngày; focus mục tiêu **chưa xong** → giảm 24 ngày; **đã xong** → thưởng XP 10. Chung cho mọi người chơi kèm thưởng nhỏ. Namespace `vie_air_force`, id `.70 .71 .72` (đang trống; đã dùng `.1 .2 .10 .11 .30 .50 .51 .61–.65`).

| Event | Ngày kích hoạt | Mốc | Focus mục tiêu | Thưởng chung | Độ tin cậy |
|---|---|---|---|---|---|
| `.70` | `date > 2011.5.31` | Trung đoàn 923 bắt đầu thay Su-22 bằng Su-30MK2V; Su-27 chuyển sang Trung đoàn 940 | `VIE_airf_first_force` (T5) | ACE +1 | Năm 2011 đã xác minh trên web; **tháng 6 chỉ có trong báo cáo nội bộ mục 2.2** |
| `.71` | `date > 2016.2.29` | Hai Su-30MK2 cuối giao đầu tháng 2/2016, đủ 36 chiếc, hoàn tất 3 trung đoàn | `VIE_airf_medium_force` (T7) | +10 XP, +10 command power | Cao (armyrecognition, defence-blog) |
| `.72` | `date > 2022.12.7` | Triển lãm Quốc phòng quốc tế VN lần đầu, 8–10/12/2022, Gia Lâm; Không quân – Phòng không, Viettel trưng bày | `VIE_apm_radar` (F4) | +15 PP | Cao (VietnamPlus) |

Cả ba là pop-up dùng `VIE_popup_cd` (45 ngày) và fallback im lặng sau 6 tháng nếu cờ cooldown còn; catch-up sau nội chiến chỉ đặt cờ. Lưu ý Trục 1 cũng bắn pop-up quanh 2011–2016 (E5–E9 Su-30): cooldown chung giải quyết, mốc nào bị hoãn sẽ rơi vào fallback. Nếu chưa muốn thêm event, bỏ nguyên Phần 6; không phần nào khác phụ thuộc nó.

Ứng viên **không đưa vào** vì chưa đủ nguồn: ngày chính xác T-6C (nguồn lệch 2023/2024), ngày hợp đồng Yak-130, mọi tin 2025–2026 (F-16V, Rafale, Su-57) đang là [~].

---

# PHẦN 7 — KIỂM SỐ LIỆU VÀ RỦI RO

## 7.1 Kết quả script (`tools/audit/air_effects_v2_check.py`)

Duyệt 2 chuyên môn × 3 cơ cấu D-D × 2 mức × có/không D-B sớm = 24 tổ hợp mỗi nhánh (72 tổng); cộng Trục 3 mới, D-A…D-E, mốc `.70`, và DET Trục 1+2 (11). Trường hợp xấu nhất, tất cả PASS:

| Chiều | A (cũ → mới) | B | C | Trần |
|---|---|---|---|---:|
| exp | 4 | 4 | 4 | 10 |
| atk | 3,5 → 4,5 | 9,5 | 6,5 | 10 |
| sup | 6,5 → 9,0 | 8,5 → 9,5 | 6,5 → 7,5 | 10 |
| cas | 4,5 | 6,5 → 7,5 | 4,5 | 10 |
| mis | 13 | **16** | **16** | 16 |
| rng | 12 → 11 | 19 → **20** | 12 → 14 | 20 |
| det | 19,5 | 15,5 | 19,5 | 20 |
| home | 18,5 | 11,5 | 11,5 → 10,5 | 20 |
| int | 6 → 7,5 | 3 → 4 | 6 → 7 | 8 |
| pers | 3 | 3 → 4 | 3 | 6 (nâng từ 3) |
| **ace (mới)** | 7,5 | 9,0 | 8,5 | 10 |
| **night (mới)** | 3,5 | 2,5 | 4,5 | 6 |
| **wx (mới)** | 3,0 | 4,0 | 3,0 | 6 |

Ba chiều chạm trần đúng bằng (B: mis 16/16, rng 20/20; DET A/C 19,5/20) nên **mọi thay đổi sau này phải chạy lại script**; đừng nâng trần để chữa. Accidents Trục 2: −9 so với trần đề xuất −10 (chưa có trong script; thêm ở bước 0). EXP đỉnh với timed idea vẫn 10,00/10 như cũ (không thêm EXP).

## 7.2 Rủi ro

| # | Rủi ro | Giảm |
|---|---|---|
| R1 | Tên category tech sai bị engine bỏ qua im lặng (đang nghi với 4 tech bonus hải quân) | Phần 3 chỉ dùng category thấy trong file tech MD; bước 7 thêm kiểm tra `add_tech_bonus` ↔ `MD_all_CATS.json` + file tech; ghi mục riêng cho hải quân |
| R2 | `air_night_penalty`, `air_weather_penalty`, `air_ace_generation_chance_factor` không hiển thị/áp dụng khi là biến của dynamic modifier | Bước 0 kiểm bằng console `effect add_to_variable = { VIE_af_air_night_penalty = -0.01 }`; nếu lỗi, bỏ chiều đó và chuyển điểm sang chiều còn trần (A: sup, atk; C: rng) |
| R3 | Script cân bằng không bắt được sai lệch vì parse sai | Bước 0 viết lại parser theo dạng `add_to_variable = { VIE_af_<token> = <giá trị> … }` trong từng `VIE_airf_*_reward`; chạy trên code hiện tại phải ra 22/22 khớp bảng cũ trước khi thêm số mới |
| R4 | Đơn vị `reduce_focus_completion_cost` (ngày/tuần) | Dùng chung kết quả kiểm của lục quân/hải quân (TESTING.md), không test riêng |
| R5 | Pop-up mốc đụng pop-up Trục 1 | `VIE_popup_cd` + fallback 6 tháng, như hải quân |
| R6 | `.70` tháng 6/2011 chỉ có một nguồn | Giữ `date > 2011.5.31` (ngày chỉ làm nền cho cooldown, không khóa gì); sửa nếu có nguồn tháng khác |
| R7 | Sửa 29 `completion_reward` cùng lúc | Mỗi bước một commit; diff chỉ được đổi khối `completion_reward` (kiểm bằng `git diff` lọc dòng) |

---

# PHẦN 8 — PLAN CODE (9 BƯỚC, MỖI BƯỚC MỘT COMMIT, NHÁNH `air-effects-v2`)

Bước 0–3 đủ để người chơi thấy khác biệt; 4–6 tùy chọn thêm; 7–8 hoàn thiện.

| Bước | File | Việc | Kiểm chứng |
|---|---|---|---|
| **0** | `tools/audit/air_force_balance.py` (gộp `air_effects_v2_check.py`, parser mới, trần mới, bảng 29 focus); `tools/audit/air_ind_balance.py` (sửa parser mục 5) | Đưa script về trạng thái PASS **trên code hiện tại** trước, rồi mới thêm số mới. Console thử 3 chiều mới (R2) | `air_force_balance.py` ALL PASS (22/22 focus + 5 Decision khớp); `air_ind_balance.py` ALL PASS |
| **1** | `common/scripted_effects/VIE_md_effects_air_force.txt` | `VIE_airf_refresh`; 22 effect `VIE_airf_<mã>_reward`; `VIE_airf_t6_dir` (đọc `force_priority`); `VIE_airf_b2_spec` (đọc `fighter_specialty`); `VIE_airf_fav_discount` | brace; `live.py` không báo effect thiếu |
| **2** | `common/national_focus/VIE_md_focus.txt` (22 focus Trục 3) | Thay `completion_reward` bằng `log` + `unlock_decision_tooltip` + `VIE_airf_<mã>_reward = yes`; giữ nguyên prerequisite, `available`, `ai_will_do`, tọa độ; sửa comment dòng 11101 | `audit.py` 0 dangling/cycle/trùng tọa độ; `git diff` không đổi dòng nào ngoài `completion_reward` |
| **3** | `VIE_md_effects_air_ind.txt` (+7 effect `VIE_apm_f<n>_reward`), `VIE_md_focus.txt` (7 focus Trục 2) | PP/CP, accidents, tech bonus, đổi `air_experience` → `VIE_airf_xp_10` | `air_ind_balance.py` PASS (không đổi tổng chi 3,10 tỷ) |
| **4** | `VIE_airf_d4_finish` | Gọi `VIE_airf_fav_discount`. Kiểm đơn vị giảm cost | chơi: chọn cơ cấu 1 → `VIE_airf_iads` rẻ hơn 14 ngày |
| **5** | `common/decisions/VIE_md_decisions_af_drills.txt` (mới), `VIE_md_ideas_air_force.txt` (+5 idea) | 5 Decision huấn luyện (Phần 5) | `live.py`: 0 decision/idea treo; chơi: cooldown 545, timed idea 180 ngày |
| **6** | `events/VIE_air_force.txt` (+`.70 .71 .72`), `VIE_md_effects_air_force.txt` (`VIE_airf_ms1..3_apply`, `VIE_event_scheduler_airf`), `VIE_md_on_actions.txt` (+1 dòng cạnh `VIE_event_scheduler_nf`), `VIE_md_effects_p3.txt` (catch-up) | Mốc lịch sử | `ev.py` sạch; `debug` đặt ngày 2011-06 thấy event; catch-up không bắn |
| **7** | `localisation/english/VIE_md_events_air_force_l_english.yml` (BOM, `:0`), loc cho 7 tech bonus, 5 Decision, 5 idea, 3 event; mô tả focus nếu đổi | Loc đầy đủ; thêm kiểm tra category tech vào `air_force_balance.py` | `verify_all_loc.py` sạch |
| **8** | `tools/TESTING.md` (mục "Air effects v2"), `VIE_v9_flag_mapping.md`, rà `ai_will_do` (capstone base 60 và guard phá sản giữ như hiện có), xóa 10 + 4 helper `VIE_airf_add_*`/`VIE_apm_add_*` không còn ai gọi (hoặc ghi chú "legacy") | Hoàn thiện | `ev.py`, `audit.py`, `live.py`, hai script cân bằng đều sạch |

Mẫu code bước 1 (theo `VIE_nf_t7_reward` và `VIE_lf_cr2_reward`):

```
VIE_airf_refresh = { force_update_dynamic_modifier = yes }

VIE_airf_t1_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_experience_gain_air_factor = 0.04 tooltip = VIE_tt_experience_gain_air_factor }
	add_to_variable = { VIE_af_air_ace_generation_chance_factor = 0.03 tooltip = VIE_tt_air_ace_generation_chance_factor }
	VIE_airf_xp_15 = yes
	add_political_power = 25
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}

VIE_airf_t6_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_air_mission_efficiency = 0.02 tooltip = VIE_tt_air_mission_efficiency }
	add_to_variable = { VIE_af_air_detection = 0.01 tooltip = VIE_tt_air_detection }
	if = { limit = { check_variable = { VIE_airf_force_priority = 1 } }
		add_to_variable = { VIE_af_air_intercept_efficiency = 0.01 tooltip = VIE_tt_air_intercept_efficiency } }
	else_if = { limit = { check_variable = { VIE_airf_force_priority = 3 } }
		add_to_variable = { VIE_af_air_range_factor = 0.01 tooltip = VIE_tt_air_range_factor } }
	else_if = { limit = { check_variable = { VIE_airf_force_priority = 2 } }
		add_to_variable = { VIE_af_air_intercept_efficiency = 0.005 tooltip = VIE_tt_air_intercept_efficiency }
		add_to_variable = { VIE_af_air_range_factor = 0.005 tooltip = VIE_tt_air_range_factor }
		add_to_variable = { VIE_af_air_night_penalty = -0.005 tooltip = VIE_tt_air_night_penalty } }
	VIE_airf_xp_10 = yes
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}

VIE_airf_b2_reward = {
	VIE_ap_ensure_af_modifier = yes
	add_to_variable = { VIE_af_air_attack_factor = 0.03 tooltip = VIE_tt_air_attack_factor }
	add_to_variable = { VIE_af_air_superiority_efficiency = 0.02 tooltip = VIE_tt_air_superiority_efficiency }
	add_to_variable = { VIE_af_air_cas_efficiency = 0.02 tooltip = VIE_tt_air_cas_efficiency }
	if = { limit = { check_variable = { VIE_airf_fighter_specialty = 1 } }
		add_to_variable = { VIE_af_air_superiority_efficiency = 0.01 tooltip = VIE_tt_air_superiority_efficiency } }
	else_if = { limit = { check_variable = { VIE_airf_fighter_specialty = 2 } }
		add_to_variable = { VIE_af_air_cas_efficiency = 0.01 tooltip = VIE_tt_air_cas_efficiency } }
	VIE_airf_xp_10 = yes
	add_tech_bonus = { name = VIE_airf_tb_multirole bonus = 0.25 uses = 1 category = CAT_medium_aircraft }
	VIE_airf_dm_tt = yes
	VIE_airf_refresh = yes
}
```

Khối lượng ước tính: 29 effect reward (~400 dòng), 29 focus sửa `completion_reward`, 5 Decision (~130 dòng), 5 idea, 3 event + scheduler (~150 dòng), ~100 khóa loc, 1 script cân bằng viết lại. Không đụng: 5 Decision lực lượng D-A…D-E và các effect `*_finish` (giá trị giữ nguyên; có thể rút gọn chúng sau bằng cùng kiểu, không nằm trong plan này).

---

# PHẦN 9 — CÂU HỎI CẦN CHỐT (mặc định đã gắn)

| # | Câu hỏi | Mặc định | Nếu đổi |
|---|---|---|---|
| Q1 | Thêm 3 chiều mới ACE/NIGHT/WX thay vì nâng trần các chiều cũ? | **Có** (đã khai báo, đã có loc) | Nâng trần: lệch với thang lục quân/hải quân |
| Q2 | A 19,9 · B 21,6 · C 19,2 điểm có chấp nhận? | **Chấp nhận** | Muốn ngang: thêm 1–2 điểm vào B1/B4 ngược lại bớt B3, hoặc thêm vào A/C ở chiều còn chỗ (sup, atk, rng) |
| Q3 | Làm 3 event mốc (Phần 6)? | **Có**; `.70` cần tháng chính xác | Bỏ bước 6, không ảnh hưởng bước khác |
| Q4 | Tech bonus 7 chỗ (Phần 3)? | **Có** | Bỏ: bớt 7 dòng, điểm không đổi |
| Q5 | Trục 2 không quân cho PP/CP/tech bonus (Phần 4)? | **Có** | Bỏ: giữ XP + tooltip hiện tại |
| Q6 | Nâng trần `pers` từ +3 lên +6? | **Có** (cho B1 +2) | Giữ +3: bỏ khoản phạt PERS của B1, đổi sang RNG −1,5 |
| Q7 | Xóa 14 helper `VIE_airf_add_*` / `VIE_apm_add_*` không còn ai gọi? | **Xóa ở bước 8** | Giữ và ghi chú legacy |
| Q8 | Xử lý riêng lỗi category tech hải quân (R1)? | **Nên làm**, một task riêng sau bước 8 | Bỏ qua: 4 tech bonus hải quân có thể vô tác dụng |

---

## Phần 7: Nghiên cứu Chỉ huy Quân chủng PK-KQ

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

---

## Phần 8: Kế hoạch Triển khai Roster Chỉ huy PK-KQ

# Plan triển khai: roster chỉ huy Không quân VIE (chuỗi 8 mốc + 12 chỉ huy bổ sung)

> **Ghi chú lịch sử PK-KQ v18 — 08/10/2026:** phần kiến trúc không quân bên dưới là lịch sử. Bản v18 có 36 focus, hai cụm lực lượng/công nghiệp dưới root không quân chung, năm tầng lực lượng, cơ cấu tác chiến trên focus, ba cụm năng lực cùng tồn tại. [Thiết kế hiện hành](VIE_air_force_documentation.md), [sơ đồ và kiểm định](.claude/docs/air/validation.md). Chưa nghiệm thu trong HOI4. Quy tắc nén bỏ mọi hàng trống/giấu phụ thuộc hoặc mutex cả cụm của bản cũ không áp dụng cho PK-KQ v18.


**Ngày:** 01/10/2026
**Dữ liệu và nguồn:** [VIE_air_force_commanders_research_report.md](VIE_air_force_commanders_research_report.md), mục 4 và mục 8.
**Liên quan:** [VIE_land_forces_implementation_plan_v2.md](VIE_land_forces_implementation_plan_v2.md) (cùng cơ chế, cùng quy ước).
**Trạng thái:** chỉ là plan, chưa sửa code nào, chưa chạy game.

## Trạng thái triển khai (01/10/2026)

**Đã code trong working tree (chưa commit, chưa chạy game):**

| Hạng mục | Kết quả |
|---|---|
| Character | 20 ID trong [VIE_md_air_commanders.txt](common/characters/VIE_md_air_commanders.txt): 8 `air_chief` + 12 `high_command` ledger air |
| Trait và cost | Cả 20 trait đã đối chiếu với pool của MD: tồn tại, đúng slot (`air_chief` hay `high_command`), hai pool không chồng lấn; cost theo mục 2 |
| Localisation | [VIE_air_commanders_l_english.yml](localisation/english/VIE_air_commanders_l_english.yml): 40 khóa (ID và `idea_token` cho từng người) |
| Portrait | 20 ảnh placeholder (silhouette trung tính, không phải chân dung thật) bằng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py); thay bằng ảnh thật khi có |
| Bước 0 | Khối trong [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt): tuyển Soát và bốn người đầu, retire Phương và Khoa, có cờ `VIE_air_phase0_done` |
| Bước 1-7 | [VIE_md_effects_air.txt](common/scripted_effects/VIE_md_effects_air.txt) (`VIE_event_scheduler_air`, 7 khối có cờ), gọi hằng tháng từ [VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt) |
| Tài liệu | Checklist trong [tools/TESTING.md](tools/TESTING.md); ghi chú trong [VIE_md_character_schema_and_roster.md](VIE_md_character_schema_and_roster.md) |

**Chọn nhánh E7 mặc định:** scheduler gọi `recruit_character` và `retire_character` **trực tiếp**, không qua event ẩn, vì chưa thể chạy game để thử. Nếu E7 thất bại thì chuyển sang event ẩn như mục 5, bước 4.

**Đã kiểm tra tĩnh:** 20/20 character hợp lệ về trait, slot, ledger, cost, `idea_token` không trùng; mọi `recruit_character` và `retire_character` trỏ tới character tồn tại; mọi portrait và khóa loc có; mỗi ID được tuyển đúng một lần và chỉ bị retire sau khi đã tuyển; 7 mốc ngày tăng dần; không trùng tên cờ; `verify_all_loc.py` đạt cho file mới; `ev.py` sạch; `live.py` không thêm lỗi nào ngoài việc đánh dấu `VIE_event_scheduler_air` giống mọi scheduler có sẵn (công cụ không đọc được định nghĩa scripted effect).

**Chưa làm:** thí nghiệm E5-E7 và mọi kiểm tra trong game; tạo nhánh git và commit; thay ảnh placeholder.

## 0. Quyết định đã chốt

| # | Quyết định | Nguồn quyết định |
|---|---|---|
| D1 | Slot `air_chief` đi theo **chuỗi 8 mốc** đúng nhiệm kỳ: tuyển người kế nhiệm rồi retire người tiền nhiệm; mỗi ID chỉ tuyển một lần | Bạn chọn |
| D2 | Thêm **12 chỉ huy** bổ sung, tất cả là advisor `high_command` ledger air | Bạn yêu cầu |
| D3 | Retire `VIE_Tran_Quang_Phuong` và `VIE_Tran_Viet_Khoa` ở startup (sai nhân thân) | Đề xuất bạn đã đọc, tôi đồng ý |
| D4 | Giữ nguyên `VIE_Vo_Minh_Luong` và `VIE_Vo_Trong_Viet` (ledger air nhưng là Lục quân) | Như trên |
| D5 | 12 người bổ sung **gắn vào đúng 8 mốc của chuỗi**, không có lịch riêng | Quyết định thiết kế của plan này (mục 1) |

## 1. Thiết kế

Slot `air_chief` chỉ có một người nên chuỗi tuyển/retire đi từng bước là tự nhiên. 12 chỉ huy bổ sung đi cùng các bước đó:
- Người nào có chức vụ **tại thời điểm** một mốc thì được tuyển ở mốc ấy (hoặc ở startup nếu đã giữ chức năm 2000).
- Người nào hết chức vụ thì được retire ở **mốc gần nhất sau đó**.
- Hệ quả: chỉ có **8 mốc ngày** trong toàn bộ plan, không cần lịch thứ hai. Đánh đổi: có người rời pool trễ 1-3 năm (cột "trễ" ở mục 3).

Mọi thao tác đều **một chiều** (tuyển ID chưa tuyển, retire ID đã tuyển). Không có vòng "retire rồi tuyển lại".

Ba điều tôi chưa xác minh và là rủi ro chính, xem mục 4: retire ở startup có chạy không; retire advisor đang được thuê có gỡ khỏi slot không; scheduler có tuyển trực tiếp được không (code hiện tại dùng event ẩn).

## 2. Roster

### 2.1. Chuỗi `air_chief` (8 người, slot `air_chief`, ledger air)

| Bước | Nhân vật | ID | Trait (pool `air_chief`) | cost |
|--:|---|---|---|--:|
| 0 | Nguyễn Đức Soát | `VIE_air_nguyen_duc_soat` | `air_air_superiority_2` | 100 |
| 1 | Nguyễn Văn Thân | `VIE_air_nguyen_van_than` | `air_chief_safety_1` | 100 |
| 2 | Lê Hữu Đức | `VIE_air_le_huu_duc` | `air_bomber_interception_2` | 100 |
| 3 | Phương Minh Hòa | `VIE_air_phuong_minh_hoa` | `air_chief_reform_2` | 150 |
| 4 | Lê Huy Vịnh | `VIE_air_le_huy_vinh` | `air_force_multiplier_2` | 100 |
| 5 | Vũ Văn Kha | `VIE_air_vu_van_kha` | `air_close_air_support_2` | 100 |
| 6 | Nguyễn Văn Hiền | `VIE_air_nguyen_van_hien` | `air_chief_all_weather_2` | 100 |
| 7 | Vũ Hồng Sơn | `VIE_air_vu_hong_son` | `air_chief_reform_1` | 100 |

### 2.2. 12 chỉ huy bổ sung (slot `high_command`, ledger air)

| # | Nhân vật | ID | Chức vụ chính (nguồn) | Trait (pool `high_command`) | cost | Tin cậy |
|--:|---|---|---|---|--:|:-:|
| 1 | Phạm Thanh Ngân | `VIE_air_pham_thanh_ngan` | Tư lệnh Không quân 04/1989-1996; Chủ nhiệm Tổng cục Chính trị 01/1998-05/2001; phi công ace, Thượng tướng 11/1999 | `air_high_command_air_superiority_3` | 125 | A |
| 2 | Hán Vĩnh Tưởng | `VIE_air_han_vinh_tuong` | Phó Tư lệnh chính trị Không quân từ 11/1996; Bí thư Đảng ủy PK-KQ 02/2001-01/2005; phi công, Trung tướng 2002 | `air_high_command_combat_training_2` | 100 | A |
| 3 | Phạm Tuân | `VIE_air_pham_tuan` | Phó Tư lệnh chính trị Không quân 1989; Giám đốc Tổng cục Công nghiệp Quốc phòng 1999; phi công vũ trụ, Trung tướng; nghỉ hưu 2008 | `air_high_command_aircraft_design_2` | 100 | B |
| 4 | Nguyễn Văn Phiệt | `VIE_air_nguyen_van_phiet` | Chính ủy Phòng không/PK-KQ 1992-2001, Trung tướng 1999 | `air_high_command_flight_safety_1` | 100 | B |
| 5 | Võ Văn Tuấn | `VIE_air_vo_van_tuan` | Phó Tư lệnh kiêm Tham mưu trưởng PK-KQ 2008-2011; Phó Tổng Tham mưu trưởng 2011-2017; phi công Su-27, Thượng tướng 2015 | `air_high_command_air_superiority_2` | 100 | A |
| 6 | Nguyễn Văn Thọ | `VIE_air_nguyen_van_tho` | Tham mưu trưởng PK-KQ 2011-2017 (Thiếu tướng); trước đó Sư đoàn trưởng Không quân 372 | `air_high_command_multirole_support_2` | 100 | B |
| 7 | Nguyễn Văn Thanh | `VIE_air_nguyen_van_thanh` | Chính ủy PK-KQ 2011-2016, Trung tướng 2012 | `air_high_command_flight_safety_2` | 100 | A |
| 8 | Lâm Quang Đại | `VIE_air_lam_quang_dai` | Phó Chính ủy từ 06/2015; Chính ủy 2016-2022; Trung tướng 2019 | `air_high_command_combat_training_1` | 100 | A |
| 9 | Phạm Văn Tính | `VIE_air_pham_van_tinh` | Sư đoàn trưởng PK 363 2016-01/2019; Phó Tư lệnh từ 06/2020 (Thiếu tướng) | `air_high_command_interception_2` | 100 | B |
| 10 | Trần Ngọc Quyến | `VIE_air_tran_ngoc_quyen` | Chính ủy PK-KQ từ 16/06/2022, Trung tướng | `air_high_command_air_reform_1` | 100 | A |
| 11 | Phạm Tuấn Anh | `VIE_air_pham_tuan_anh` | Phó Tham mưu trưởng, rồi Phó Tư lệnh PK-KQ từ 07/2023 | `air_high_command_all_weather_1` | 100 | B |
| 12 | Bùi Đức Hiền | `VIE_air_bui_duc_hien` | Tham mưu trưởng PK-KQ từ 06/2025 (Thiếu tướng) | `air_high_command_night_operations_1` | 100 | B |

Ghi chú:
- Trait và `cost` là điểm khởi đầu để cân bằng, **không phải dữ kiện lịch sử**. Tôi đã kiểm tra cả 20 trait tồn tại trong đúng pool của MD và hai pool không chồng lấn. Quy ước cost theo upstream: `reform_2` là 150, trait cấp 3 của `high_command` là 125, còn lại 100.
- 6 người trong số 12 là cán bộ chính trị (Ngân sau 1998, Tưởng, Phiệt, Thanh, Đại, Quyến). Pool trait của MD không có trait chính trị nên họ mang trait chuyên môn gần nhất; đây là xấp xỉ.

## 3. Lịch 8 mốc

Scheduler của mod chạy **hằng tháng**, nên ngày thực tế lệch tối đa 1 tháng. Cột "trễ" là thời gian người bị retire đã hết chức vụ thật.

| Bước | Điều kiện | Tuyển | Retire (trễ) |
|--:|---|---|---|
| 0 | Startup, `date < 2002.2.7` | Soát, Ngân, Tưởng, Tuân, Phiệt | Upstream: `VIE_Tran_Quang_Phuong`, `VIE_Tran_Viet_Khoa` |
| 1 | `date > 2002.2.6` | Thân | Soát (tại mốc), Ngân (trễ 0,7 năm), Phiệt (trễ 0,7 năm) |
| 2 | `date > 2007.1.31` | Đức | Thân (0), Tưởng (trễ 2 năm) |
| 3 | `date > 2010.6.30` | Hòa, Võ Văn Tuấn | Đức (0), Tuân (trễ 2 năm) |
| 4 | `date > 2015.5.20` | Vịnh, Thọ, Thanh, Đại | Hòa (0) |
| 5 | `date > 2019.12.30` | Kha, Tính | Vịnh (0), Võ Văn Tuấn (trễ 2 năm), Thọ (trễ 2 năm), Thanh (trễ 3,5 năm) |
| 6 | `date > 2023.5.18` | Hiền, Tuấn Anh, Quyến | Kha (0), Đại (trễ 1 năm) |
| 7 | `date > 2025.6.27` | Sơn, Bùi Đức Hiền | Hiền (0) |

**Ngày chưa chính xác:** mốc 3 (Hòa) dùng 01/07/2010 vì nguồn chỉ ghi năm 2010. Mốc 2 dùng 01/02/2007 theo ngày Thân nghỉ hưu (02/2007); một nguồn khác ghi Đức nhận chức 2006.

**Người ở lại đến cuối** (không bị retire): Tính, Tuấn Anh, Quyến, Bùi Đức Hiền, Sơn.

**Số người có mặt** (ngoài Lương và Việt của upstream):

| Khoảng thời gian | `air_chief` | `high_command` ledger air |
|---|---|---|
| 2000 - 02/2002 | Soát | Ngân, Tưởng, Tuân, Phiệt |
| 02/2002 - 02/2007 | Thân | Tưởng, Tuân |
| 02/2007 - 07/2010 | Đức | Tuân |
| 07/2010 - 05/2015 | Hòa | Võ Văn Tuấn |
| 05/2015 - 12/2019 | Vịnh | Võ Văn Tuấn, Thọ, Thanh, Đại |
| 12/2019 - 05/2023 | Kha | Tính, Đại |
| 05/2023 - 06/2025 | Hiền | Tính, Tuấn Anh, Quyến |
| từ 06/2025 | Sơn | Tính, Tuấn Anh, Quyến, Bùi Đức Hiền |

Giai đoạn 2007-2015 mỏng (1 người bổ sung) vì nguồn cho cấp Phó Tư lệnh thời đó chưa có. Cần nghiên cứu thêm nếu muốn dày hơn (mục 7).

## 4. Thí nghiệm bắt buộc trước khi code (khoảng 20 phút)

Làm trên bản sao save, bật `debug`, chơi VIE. Kết quả quyết định kỹ thuật ở mục 5.

| # | Thí nghiệm | Nếu thành công | Nếu thất bại |
|---|---|---|---|
| **E5** | Mới vào game 2000: `effect retire_character = VIE_Tran_Quang_Phuong`, mở panel advisor Không quân | Phương biến mất khỏi pool: bước 0 dùng đúng thiết kế | Retire ở startup không đủ: giữ họ và ghi nhận anachronism, hoặc tìm cách khác |
| **E6** | Thuê Phương làm `air_chief`, rồi `effect retire_character = VIE_Tran_Quang_Phuong` | Slot trống, có thể thuê người mới | Nếu slot vẫn giữ người đã retire thì mỗi bước chuỗi phải kèm cách gỡ slot (cần nghiên cứu thêm) |
| **E7** | Tạo effect thử gọi `recruit_character` và `retire_character` trực tiếp trong khối `if` của scheduler tháng (không qua event), đặt cờ | Bỏ event, dùng scheduler trực tiếp (mục 5, bước 4) | Quay lại mẫu hiện có: event ẩn `days = 1`, mỗi bước một event |

Nếu E5 và E6 đều đạt, plan chạy như viết. Nếu E7 thất bại thì chỉ thay bước 4 (mục 5), phần còn lại giữ nguyên.

## 5. Các bước code

### Bước 1: Nhánh git

Tạo `claude/air-roster` từ `main`. Mỗi bước dưới đây một commit.

### Bước 2: Character mới (không phụ thuộc thí nghiệm)

**File mới:** `common/characters/VIE_md_air_commanders.txt`, 20 character. Khuôn mẫu theo `VIE_Tran_Quang_Phuong` upstream:

```txt
VIE_air_nguyen_duc_soat = {
	name = "Nguyen Duc Soat"
	portraits = {
		army = {
			small = "gfx/leaders/VIE/small/Portrait_Nguyen_Duc_Soat_small.dds"
			large = "gfx/leaders/VIE/Portrait_Nguyen_Duc_Soat.dds"
		}
	}
	advisor = {
		slot = air_chief
		idea_token = vie_air_nguyen_duc_soat
		ledger = air
		traits = { air_air_superiority_2 }
		cost = 100
		ai_will_do = { factor = 1 }
	}
}
```

- Chuỗi 8 người: `slot = air_chief`. 12 người bổ sung: `slot = high_command`. Tất cả `ledger = air`.
- Mỗi advisor cần `idea_token` chữ thường (`vie_air_...`), xem mục 2.
- Không có khối `field_marshal` hoặc `corps_commander` (Không quân không có commander).
- Định dạng file: CRLF, ASCII (tên không dấu), thụt dòng bằng tab, như các file character khác của mod.

**Lưu ý đặt tên dễ nhầm:** `nguyen_van_than` (Thân, tư lệnh) và `nguyen_van_thanh` (Thanh, chính ủy) chỉ khác một chữ; `nguyen_van_hien` (Hiền, tư lệnh) và `bui_duc_hien` (Hiền, tham mưu trưởng); `pham_tuan` (phi công vũ trụ) và `pham_tuan_anh` (Phó Tư lệnh). Nên ghi chú một dòng trên đầu file.

### Bước 3: Localisation và portrait (không phụ thuộc thí nghiệm)

**Localisation:** file mới `localisation/english/VIE_air_commanders_l_english.yml`. Giữ BOM UTF-8, CRLF, dòng đầu `l_english:`, tên hiển thị có dấu. Mỗi nhân vật cần **hai khóa** (ID và `idea_token` chữ thường), như nhóm Lục quân:

```yaml
 VIE_air_nguyen_duc_soat:0 "Nguyễn Đức Soát"
 vie_air_nguyen_duc_soat:0 "Nguyễn Đức Soát"
```

**Portrait:** mở rộng [tools/build_vie_placeholder_portraits.py](tools/build_vie_placeholder_portraits.py): thêm 20 stem vào `PLACEHOLDERS` với một bảng màu mới cho Không quân (xanh trời). Ảnh là silhouette trung tính, không phải chân dung thật; ghi đè cùng tên khi có ảnh thật.

### Bước 4: Scheduler (phụ thuộc E7)

**File mới:** `common/scripted_effects/VIE_md_effects_air.txt`, chứa một scripted effect `VIE_event_scheduler_air`. Mỗi bước một khối có cờ:

```txt
VIE_event_scheduler_air = {
	if = {
		limit = {
			date > 2002.2.6
			NOT = { has_country_flag = VIE_air_step_1 }
		}
		recruit_character = VIE_air_nguyen_van_than
		retire_character = VIE_air_nguyen_duc_soat
		retire_character = VIE_air_pham_thanh_ngan
		retire_character = VIE_air_nguyen_van_phiet
		set_country_flag = VIE_air_step_1
	}
	# ... step 2..7 theo bảng mục 3, theo thứ tự thời gian
}
```

**Gọi từ tháng:** thêm một dòng `VIE_event_scheduler_air = yes` ngay sau `VIE_event_scheduler_p16 = yes` trong [VIE_md_on_actions.txt](common/on_actions/VIE_md_on_actions.txt) (khối `on_monthly`, đã có điều kiện loại tag nổi dậy).

**Nếu E7 thất bại:** thay các lệnh trong khối bằng `country_event = { id = vie_air_commanders.N days = 1 }` và đặt các lệnh tuyển/retire trong event ẩn như mẫu của [VIE_army_commanders.txt](events/VIE_army_commanders.txt). Khi đó cần thêm `add_namespace`, một event mỗi bước (7 event) và khóa loc `.a` cho từng option.

### Bước 5: Startup (bước 0, không phụ thuộc E7)

Sửa [VIE_md_on_actions_startup.txt](common/on_actions/VIE_md_on_actions_startup.txt), trong scope `VIE = { ... }`, cạnh khối tuyển Lục quân Giai đoạn 1:

```txt
if = {
	limit = {
		date < 2002.2.7
		NOT = { has_country_flag = VIE_air_phase0_done }
	}
	recruit_character = VIE_air_nguyen_duc_soat
	recruit_character = VIE_air_pham_thanh_ngan
	recruit_character = VIE_air_han_vinh_tuong
	recruit_character = VIE_air_pham_tuan
	recruit_character = VIE_air_nguyen_van_phiet
	retire_character = VIE_Tran_Quang_Phuong
	retire_character = VIE_Tran_Viet_Khoa
	set_country_flag = VIE_air_phase0_done
}
```

Cờ bắt buộc vì `on_startup` chạy cả khi load save; không có cờ thì mỗi lần load sẽ tuyển lặp và retire lặp. Điều kiện `date < 2002.2.7` để save sau mốc 1 không tuyển lại người đã hết nhiệm kỳ.

### Bước 6: Cập nhật tài liệu

| File | Việc |
|---|---|
| [VIE_air_force_commanders_research_report.md](VIE_air_force_commanders_research_report.md) | Đã có mục "mở rộng 12 chỉ huy" (mục 8) và quyết định chuỗi 8 mốc |
| [tools/TESTING.md](tools/TESTING.md) | Thêm checklist Không quân như mục 6 dưới đây |
| [VIE_md_character_schema_and_roster.md](VIE_md_character_schema_and_roster.md) | Ghi chú 4 character Không quân upstream sai nhân thân (dẫn sang báo cáo Không quân) |

## 6. Kiểm tra

**Tĩnh** (xem [tools/TESTING.md](tools/TESTING.md)):

```bash
python3 tools/verify_all_loc.py
python3 tools/audit/live.py
python3 tools/audit/ev.py   # chỉ cần nếu E7 thất bại và dùng event
```

**Tự kiểm tra chéo** (như đợt Lục quân): mọi `recruit_character`/`retire_character` trỏ tới character tồn tại; mọi portrait có file; mọi tên và `idea_token` có khóa loc; trait nằm đúng pool của MD (`air_chief` hay `high_command`).

**Trong game (chưa ai chạy):**
- [ ] `error.log` sạch: không báo `VIE_air_`, `trait`, `portrait`, `idea_token`.
- [ ] Bắt đầu 2000, panel Không quân: `air_chief` chỉ có Soát; `high_command` có Ngân, Tưởng, Tuân, Phiệt, cùng Lương và Việt của upstream. Không có Phương, Khoa.
- [ ] Đặt ngày/lấy save ở các mốc 2002, 2007, 2010, 2015, 2019, 2023, 2025: `air_chief` đổi đúng người; không ai bị tuyển hai lần; không có hai `air_chief` cùng lúc.
- [ ] Load save giữa hai mốc (ví dụ 2012): không tuyển lặp, roster vẫn đúng giai đoạn.
- [ ] Mỗi mốc kiểm tra số người có mặt đối chiếu bảng ở mục 3.

## 7. Rủi ro và phần chưa làm

| Rủi ro | Xử lý |
|---|---|
| Retire ở startup không hoạt động (E5) | Chấp nhận anachronism của Phương và Khoa, hoặc tìm cách khác |
| Retire advisor đang được thuê không gỡ khỏi slot (E6) | Cần nghiên cứu thêm cơ chế gỡ slot trước khi triển khai chuỗi |
| Scheduler không tuyển trực tiếp được (E7) | Dùng event ẩn như mẫu Lục quân |
| Retire người trễ 1-3,5 năm | Chấp nhận (mục 3); mỗi mốc là ngày cố định |
| 6/12 người bổ sung là cán bộ chính trị mang trait chuyên môn | Xấp xỉ do pool trait của MD; ghi rõ |
| 6/12 người bổ sung chỉ có một nguồn (nhãn B) | Xem báo cáo, mục 8; xác minh thêm nếu có điều kiện |
| Giai đoạn 2007-2015 mỏng | Chưa có nguồn cho Phó Tư lệnh thời đó; nghiên cứu thêm nếu cần |
| Bookmark khác 2000 | Plan chỉ hỗ trợ bookmark 2000; bắt đầu sau 2002 sẽ không tuyển Soát |

**Ngoài phạm vi:**
- Cấp sư đoàn: Wikipedia VI chỉ ghi sư đoàn trưởng hiện tại (Đại tá), không có danh sách lịch sử; không đưa vào plan.
- Trần Việt Khoa cho Lục quân: vẫn chờ nguồn bổ nhiệm đáng tin cậy.
- **Nguyễn Văn Rinh** (phát hiện trong lúc nghiên cứu): là tướng Lục quân (Tư lệnh Quân đoàn 2 năm 1992, Phó Tổng Tham mưu trưởng 1994-1998, Thứ trưởng 1998-2007, Thượng tướng 2004). Không thuộc Không quân, nhưng là ứng viên `high_command` còn thiếu của roster Lục quân Giai đoạn 1.

## 8. Nguồn

Nguồn từng người nằm ở [báo cáo Không quân](VIE_air_force_commanders_research_report.md), mục 4 và mục 8. Nguồn kỹ thuật:
- [MD VIE.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/characters/VIE.txt), [01_air_chief_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_air_chief_traits.txt), [01_high_command_traits.txt](https://raw.githubusercontent.com/MillenniumDawn/Millennium-Dawn/main/common/country_leader/01_high_command_traits.txt)
- [HOI4 Character modding](https://hoi4.paradoxwikis.com/Character_modding)
