# Báo cáo hải quân Việt Nam – 3 trục: Mua sắm, CNQP, Lực lượng (bản 2.4)

Sep 29, 2026 · @dfd

## 1. Kết luận kiến trúc

Bản 2 giữ hai trục nhưng đổi cách nối chúng: Trục 1 chạy theo cửa sổ thời gian lịch sử, Trục 2 chạy theo Focus → Decision → Event, và nội địa hóa Molniya chỉ cần xưởng Ba Son, không cần Small Combatant.

- **Trục 1 – Mua sắm** trả lời "Việt Nam mua hoặc đặt đóng trang bị nào?". Event lịch sử tự kích trong cửa sổ thời gian (có retry). Decision chỉ là lối vào thủ công cho đường alt-history hoặc khi đã lỡ cửa sổ.
- **Trục 2 – CNQP** trả lời "Việt Nam tự bảo dưỡng, đóng và tích hợp được những gì?". Focus mở năng lực, Decision khởi động chương trình, Event quyết định chương trình diễn ra thế nào.
- **Focus của Trục 1** (`VIE_navy_modernization`, `VIE_russian_arms_deals`) chỉ thưởng: giảm giá, rút ngắn giao hàng, mở quy mô lớn hơn. Chúng không còn khóa các deal lịch sử.

### Sáu vấn đề đã xử lý

| # | Vấn đề ở bản 1 | Cách sửa ở bản 2 | Xem mục |
| --- | --- | --- | --- |
| 1 | ToT Molniya (2009–2010) đòi Small Combatant (mở từ 2010+), nên đi đúng lịch sử không bao giờ kịp | ToT Molniya chỉ cần `VIE_cap_ba_son_yard` (đạt khoảng 2006–2008). Small Combatant trở thành hệ quả của kinh nghiệm đóng tàu, không phải tiền đề | 4, 5, 6 |
| 2 | Decision Small Combatant có lựa chọn "tàu tốc độ cao", trùng bản chất Molniya, vi phạm Quy tắc 1 | Decision 3 chỉ cấp capability và giảm chi phí, không cấp tàu. Mọi tàu chỉ đến từ Event của Trục 1 | 5 |
| 3 | Lựa chọn định hướng ở Decision Ba Son vô nghĩa vì cả hai nhánh đều bắt buộc | Mỗi lựa chọn có đánh đổi bằng số: kinh nghiệm khởi điểm, thời lượng nhánh còn lại, chi phí | 3, 5 |
| 4 | Procurement phụ thuộc Focus và ngoại giao, mâu thuẫn quy ước cửa sổ + retry đã chọn cho lục quân | Cổng chung: đối tác tồn tại và không chiến tranh, trong cửa sổ thời gian, retry mỗi tháng; hai ngoại lệ có tên (pha nội địa cần capability, chương trình nối tiếp cần chương trình trước). Ngoại giao chỉ ảnh hưởng AI | 3, 4 |
| 5 | Sigma: "không RNG" nhưng vẫn có nhánh Collapse; người chơi đi đường lịch sử dễ vượt Funding Gate | Cổng tài chính có ngưỡng xác định. Lựa chọn mặc định "lịch sử" là tiếp tục đàm phán nhưng chưa cam kết mua vì chưa chốt tài chính, dẫn tới không có Sigma operational; muốn có Sigma phải chuyển sang nhánh mua sắm | 4 |
| 6 | Chuỗi Focus → Decision → Focus tạo thời gian chết, slot focus bỏ trống | Focus chỉ dùng Focus tiền đề, ngày, trạng thái thế giới và năng lực do nhánh khác sở hữu; không đọc kết quả Decision. Các Decision chạy song song, tối đa 2 cùng lúc; Decision đang chờ không chiếm slot | 3, 5 |

Bảng flag và variable cho toàn bộ capability nằm ở mục 7.

### Bản 2.1: bảy sửa sau rà soát

Bảy sửa dưới đây đã được áp dụng vào mục 1–9:

- Quy tắc 6 viết lại thành bốn loại điều kiện của Focus. Focus 4 chỉ còn Focus 2 và ngày; Focus 6 chỉ còn Focus 3, 4, 5 và ngày, ngưỡng kinh nghiệm chuyển sang Decision 5.
- Cổng của Trục 1 nêu rõ hai ngoại lệ có tên: pha nội địa (Molniya pha 2) và chương trình nối tiếp (Gepard II).
- Sigma tách hai nhánh: Historical (chưa cam kết, dừng ở `suspended`) và mua sắm. Bỏ lời giải thích "ưu tiên chương trình Nga", vì nguồn nêu vướng mắc tài chính.
- Gepard II gate bằng `VIE_gepard1_complete`, cửa sổ từ 2011-12 (đơn đặt hàng công bố tháng 12/2011), vì Batch II được đặt sau khi Batch I giao xong.
- Molniya pha 1 có cửa sổ 2003-06 → 2005-12; đóng tại Ba Son khởi đóng 2010 và giao 2014–2017.
- Molniya late là một Decision định tuyến theo pha, với hai cờ lỡ hạn theo pha.
- Trạng thái chờ capability là trạng thái riêng và không chiếm slot.

Bản 2.2 bổ sung: các mốc còn ghi "cần xác minh" của Gepard II, Molniya, Kilo và Sigma đã được chọn theo bậc tin cậy của nguồn (mục 8.3), và ngày bắt đầu cửa sổ của Trục 1 nay bằng mốc ký lịch sử đã chọn.

Bản 2.3 bổ sung: các mục còn ghi "cần xác minh" và các nguồn ghi "(đoạn trích)" đã được mở đối chiếu; kết quả ở mục 8.3. Thay đổi về mốc: Molniya pha 1 quay về cửa sổ 2003-06 → 2005-12, Bastion-P giao 2011, tàu Kilo cuối đến Cam Ranh 20/1/2017. Hai ghi chú mới: MRO tàu ngầm Kilo đặt ở Cam Ranh với hỗ trợ của Nga, và Ba Son dời khỏi TP.HCM sang Phú Mỹ khoảng 2015.

Bản 2.4 bổ sung: mục 16–18 đối chiếu thiết kế với quy ước và mã hỗ trợ của Millennium Dawn, cung cấp script mẫu cho lát cắt Molniya và Decision 1, và ghi kết quả rà nhất quán. Bốn mục còn mở nằm ở bảng 18.1.

Bản 2.5 bổ sung: gỡ Hải quân đánh bộ khỏi Trục 3 (chuyển sang nhánh Vietnam Special Force), không thêm Trục 4 vì phần Biển Đông là một focus tree riêng, và ghi ranh giới ở mục 10.3. Trục 3 còn 22 node Focus và 4 Decision lực lượng.

## 2. Nguyên tắc thiết kế và quy tắc chống xung đột

Một chương trình chỉ được tạo ra bởi đúng một loại nút, và mọi phụ thuộc chỉ đi một chiều. Chín quy tắc dưới đây giữ điều đó. Quy tắc 6 được viết lại ở bản 2.1; quy tắc 9 là mới; quy tắc 3, 5 và 7 được viết lại.

| # | Quy tắc | Nội dung |
| --- | --- | --- |
| 1 | Không nhận thiết bị hai lần | Molniya chỉ được tạo bởi Event của Molniya. Không Focus hay Decision CNQP nào cấp tàu |
| 2 | Procurement không tự tạo CNQP | Mua Kilo không có nghĩa Ba Son biết bảo dưỡng Kilo. Phải hoàn thành chương trình MRO |
| 3 | CNQP không tự tạo procurement | Hoàn thành Ba Son hoặc Small Combatant không tặng tàu. Decision 3 chỉ cấp capability, kinh nghiệm và giảm chi phí, không cấp tàu |
| 4 | Trang bị lịch sử tạo cơ hội, không tự tạo ToT | Kilo mở cơ hội MRO. ToT Molniya chỉ xảy ra khi người chơi chọn nhánh nội địa hoặc hybrid |
| 5 | Lịch sử là baseline có cửa sổ và retry | Deal lịch sử tự kích trong cửa sổ thời gian; cổng chung là đối tác tồn tại và không chiến tranh, với hai ngoại lệ có tên (mục 3.1). Alt-history đi qua Decision |
| 6 | Focus chỉ dùng bốn loại điều kiện (bản sửa) | (a) Focus tiền đề, kể cả "hoặc" và "ít nhất 2 trong 3"; (b) ngày; (c) trạng thái thế giới như số thân tàu operational; (d) năng lực do nhánh khác sở hữu (VIE\_ext\_\*). Không dùng kết quả chương trình hay Decision (VIE\_cap\_\*, \_started, biến kinh nghiệm, biến readiness). Kết quả Decision chỉ gate hiệu ứng và Decision khác |
| 7 | Không có prerequisite vòng | Vòng phát triển chạy qua biến kinh nghiệm cộng dồn, không qua prerequisite. Thứ tự lớp: Thể chế → Xưởng → MRO / Small Combatant → Integration → Trưởng thành |
| 8 | Doctrine tách khỏi CNQP | `VIE_navy_blue_water` và `VIE_path_maritime_denial` có thể tăng nhu cầu hoặc mở chương trình, nhưng không nằm trong chuỗi Ba Son |
| 9 | Mọi lựa chọn có đánh đổi định lượng (mới) | Không có lựa chọn nào chỉ khác tên. Mỗi lựa chọn phải đổi ít nhất một trong: chi phí, thời lượng, kinh nghiệm, phụ thuộc bên ngoài |

Ba điều được khóa để tránh mâu thuẫn với các nhánh khác:

- Focus mở hoặc hoàn thành không đồng nghĩa capability tồn tại. Capability chỉ tồn tại khi flag `VIE_cap_*` tương ứng được đặt.
- Không có Focus CNQP nào cấp Kilo, Gepard, Bastion-P, Molniya hoặc Sigma.
- Doctrine hải quân và trục CNQP chỉ giao nhau qua flag, không qua prerequisite.

## 3. Cơ chế chung

Bốn cơ chế dùng lại cho mọi chương trình: cửa sổ + retry cho Trục 1, Focus và Decision chạy song song cho Trục 2, một thang chi phí thống nhất, và đường đi riêng cho AI. Mọi con số trong tài liệu này là giá trị khởi điểm, cần cân bằng khi playtest.

### 3.1 Cửa sổ thời gian và retry (Trục 1)

Mỗi chương trình có một cửa sổ `[start, end]`. Một event ẩn kiểm tra mỗi tháng. Cổng chung gồm hai điều kiện: đối tác tồn tại và không đang có chiến tranh với đối tác. Có hai ngoại lệ có tên, đều ghi trong bảng 4.1: pha nội địa cần capability công nghiệp (Molniya pha 2 cần `VIE_cap_ba_son_yard`), và chương trình nối tiếp cần chương trình trước (Gepard II cần `VIE_gepard1_complete`). Quan hệ ngoại giao không gate người chơi, chỉ ảnh hưởng AI (giống quyết định đã chọn cho deal K9 của lục quân).

Ngày bắt đầu cửa sổ của mỗi chương trình đặt bằng mốc ký lịch sử đã chọn, vì event kích ngay khi cổng mở. Các mốc đã chọn, nguồn và lý do nằm ở mục 8.3.

```text
on_monthly (VIE):
  if date in window(P)
     and not flag(P_contracted) and not flag(P_missed) and not flag(P_cancelled)
     and country_exists(partner) and not at_war_with(partner):
        fire event P.1            # bàn đàm phán, có lựa chọn Historical
  else if date > window_end(P) and not flag(P_contracted):
        set flag P_missed
        enable decision P_late    # lối vào thủ công, chi phí +25%, giao hàng chậm hơn
```

Điều này thay ghi chú "availability phải tuân theo dependency của Focus Tree" ở bản 1. Focus hoàn thành chỉ thêm thưởng vào cùng event: giảm giá, rút ngắn giao hàng, hoặc mở lựa chọn quy mô lớn hơn mức lịch sử.

Giao hàng có sàn thời gian: ngày giao không sớm hơn mốc lịch sử trừ 12 tháng, để đầu tư tối đa không cho ra Kilo vào 2011.

Mỗi chương trình có đúng một Decision `P_late` (Kilo, Gepard I, Gepard II, Bastion-P, Molniya, Sigma), mở bằng cờ `_missed` khi hết cửa sổ mà chưa ký. Hai chương trình có quy tắc riêng. Molniya có hai cờ theo pha (`VIE_molniya_p1_missed`, `VIE_molniya_p2_missed`) và một Decision `molniya_late` kiểm tra từng pha còn khả thi rồi đưa người chơi vào pha đó. Sigma có `sigma_late`, mở được từ cả `VIE_sigma_missed` lẫn `VIE_sigma_suspended`.

### 3.2 Focus và Decision chạy song song (Trục 2)

- Focus kế tiếp chỉ đòi Focus trước đã hoàn thành, cộng ngày và điều kiện thế giới. Nó không chờ Decision trước kết thúc, nên slot focus không bị bỏ trống.
- Decision đọc capability flag khi bắt đầu từng Event. Thiếu flag, Decision chuyển sang trạng thái chờ (Waiting for capability), không chiếm slot, hiển thị "chưa đủ năng lực" và tự tiếp tục khi flag xuất hiện.
- Kinh nghiệm được cộng ngay từ Event đầu của Decision, không đợi Event cuối. Vì vậy các điều kiện dựa trên biến kinh nghiệm không biến thành chờ Decision kết thúc.
- Tối đa 2 Decision CNQP chạy cùng lúc (`VIE_var_naval_program_active`), để ngân sách hải quân không bị rút quá mức. Decision đang chờ capability không tính vào giới hạn này.

### 3.3 Thang chi phí và thời lượng

Ba mức đầu tư dùng cho Decision 1, 2, 3, 4. Chi phí tính theo tỷ lệ so với mức Cơ bản.

| Mức | Chi phí | Thời lượng | Trần tier | Ghi chú |
| --- | --- | --- | --- | --- |
| Cơ bản | ×1,0 | 12 tháng | 1 | Rẻ, đủ để mở các bước sau |
| Mở rộng | ×1,6 | 18 tháng | 2 | Cân bằng |
| Trọng điểm | ×2,4 | 24 tháng | 3 | Cần cho mức tự chủ cao ở Decision 5 |

Mốc quan trọng: capability tối thiểu (tier 1) được đặt khi Decision đạt khoảng 40% tiến độ, không phải khi kết thúc. Đầu tư Trọng điểm vì thế không làm trễ các chương trình đang chờ capability đó.

### 3.4 AI

- **Trục 1:** cùng cửa sổ và cùng event, nhưng AI tự chọn lựa chọn mang nhãn Historical (`ai_chance` 100% cho lựa chọn đó). Quan hệ ngoại giao ảnh hưởng `ai_will_do` của các lựa chọn alt-history.
- **Trục 2:** Focus có trọng số AI cao trong đúng khoảng ngày của chúng; Decision tự chạy với lựa chọn Cơ bản hoặc Cân bằng. AI không cần tương tác để có Kilo, Gepard và Ba Son.

## 4. Trục 1 – Mua sắm

Sáu chương trình chạy theo cửa sổ thời gian, cổng chung là đối tác tồn tại và không chiến tranh (hai ngoại lệ có tên ở bảng 4.1), và mỗi chương trình luôn có một lựa chọn mang nhãn Historical. Molniya được tách thành hai pha để khớp lịch sử và bỏ phụ thuộc vào Small Combatant.

### 4.1 Cửa sổ, cổng và kết quả lịch sử

| Chương trình | Cửa sổ | Cổng (ngoài đối tác tồn tại, không chiến tranh) | Kết quả lịch sử | Giao hàng lịch sử |
| --- | --- | --- | --- | --- |
| Kilo 636 | 2009-12 → 2011-12 (ký 12/2009) | không có | 6 tàu ngầm | 2014–2017 (tàu đầu biên chế 15/1/2014; tàu thứ sáu đến Cam Ranh 20/1/2017) |
| Gepard I | 2006-01 → 2008-12 | không có | 2 tàu | 2011 (biên chế 3/2011 và 8/2011) |
| Gepard II | 2011-12 → 2014-12 | `VIE_gepard1_complete` (ngoại lệ chương trình nối tiếp: Batch I đã giao xong) | 2 tàu ASW | 2017–2018 |
| Bastion-P | 2006-07 → 2009-12 | không có | 2 hệ thống | 2011 |
| Molniya pha 1 (mua) | 2003-06 → 2005-12 (thỏa thuận 2003 theo nguồn đã chọn, xem 8.3) | không có | 2 tàu từ Nga | 2007–2008 |
| Molniya pha 2 (nội địa) | 2009-06 → 2012-12 | `VIE_cap_ba_son_yard` (ngoại lệ pha nội địa) | 6 tàu đóng tại Ba Son | khởi đóng 2010; giao giữa 2014, 6/2015, 10/2017 |
| Sigma 9814 | 2011-10 → 2014-12 | không có (đối tác là Hà Lan) | không có hạm đội Sigma operational | không có |

Focus `VIE_navy_modernization` mở quy mô lớn hơn mức lịch sử ở Gepard, Bastion-P, Sigma. Focus `VIE_russian_arms_deals` giảm giá và mở quy mô lớn hơn ở Kilo và Molniya. Cả hai chỉ thưởng, không gate.

### 4.2 Kilo 636

1. **Quy mô:** 6 (Historical), 4, 2, hoặc 8 (alt-history, cần `VIE_russian_arms_deals`, chi phí cao hơn), hoặc hoãn.
2. **Huấn luyện và cơ sở hỗ trợ:** đầy đủ (chi phí cao, readiness cao, tiến độ ổn định) hoặc cắt giảm (rẻ, readiness thấp, chậm hơn).
3. **Bàn giao từng chiếc**, cộng `VIE_kilo_qty_delivered`, đặt sàn thời gian như mục 3.1.
4. **Hoàn tất** khi `delivered = ordered`: đặt `VIE_kilo_complete`, cộng kinh nghiệm hải quân, đặt `VIE_opp_sub_mro` (cơ hội, chưa phải capability).

### 4.3 Gepard 3.9 – Batch I và II

- **Batch I:** cấu hình (Standard, ASW, phòng không), rồi quy mô (2 Historical; 4 alt cần `VIE_navy_modernization`). Batch I được đặt hàng năm 2006 và bàn giao năm 2011.
- **Batch II:** cổng là `VIE_gepard1_complete` (Batch I đã bàn giao xong). Lịch sử đi theo thứ tự giao Batch I, đánh giá, rồi đặt Batch II: hai tàu đầu giao tháng 3 và tháng 8/2011, và đơn đặt Batch II được công bố tháng 12/2011 theo nguồn đương thời (mục 8.3). Cửa sổ mở từ 2011-12. Chọn 2 ASW (Historical), 4 ASW (alt), hoặc không mua. Không tự động xảy ra sau Batch I.

### 4.4 Bastion-P

Quy mô: 2 (Historical), 1, 4 (alt), hoặc hoãn. Sau đó chọn triển khai: Bắc, Trung, Nam hoặc phân tán, đặt `VIE_bastion_deploy`. Đây là chuỗi ngắn nhất và không có tầng công nghiệp riêng. Bastion có thể đặt `VIE_ext_naval_missile` cho Trục 2 (xem mục 6).

### 4.5 Molniya – hai pha, ba đường

- **Pha 1 (cửa sổ 2003-06 → 2005-12):** mua 2 tàu từ Nga (Historical), hoặc 4 tàu (alt, đắt), hoặc bỏ qua pha 1. Đặt `VIE_molniya_contracted`. Tàu giao 2007–2008. Mốc 2003 được chọn theo nguồn ở mục 8.3 (thỏa thuận 2003 cho 2 tàu hoàn chỉnh); giấy phép chế tạo được mua khoảng 2005–2006 và thỏa thuận chuyển giao công nghệ ký năm 2009.
- **Pha 2 (từ 2009-06):** cổng là `VIE_cap_ba_son_yard`, không phải Small Combatant. Chọn tổng số tàu: dừng ở số đã mua, 2 + 6 (Historical), 2 + 8, hoặc 2 + 10. Hai mức sau cần `VIE_var_ba_son_tier ≥ 2`. Lịch sử khởi đóng năm 2010; cặp đầu giao giữa 2014, cặp hai ngày 2/6/2015, cặp ba ngày 9/10/2017.

Ba đường của bản 1 vẫn còn, nhưng gọn hơn:

| Đường | Cách đi | Đặc điểm |
| --- | --- | --- |
| A – Mua hoàn chỉnh | Pha 1 rồi dừng | Nhanh, không cần xưởng, kinh nghiệm đóng tàu thấp |
| B – Nội địa thuần | Bỏ pha 1, vào thẳng pha 2 khi có xưởng | Chậm hơn, kinh nghiệm cao, không có 2 tàu đầu |
| C – Hybrid | Pha 1 rồi pha 2 (đường lịch sử) | Cân bằng, cầu nối chính sang Trục 2 |

Pha 2 cộng `VIE_var_shipbuilding_exp` theo từng tàu bàn giao và đặt `VIE_molniya_domestic_started` khi chiếc đầu vào đóng. Mỗi pha có cờ lỡ hạn riêng (`VIE_molniya_p1_missed`, `VIE_molniya_p2_missed`). Decision `molniya_late` là một Decision duy nhất, kiểm tra từng pha còn khả thi và đưa người chơi vào pha đó.

### 4.6 Sigma 9814

Sigma là chương trình duy nhất mà kết quả lịch sử là "không có hạm đội". Cách làm: kết quả này là một lựa chọn có nhãn, không phải RNG.

1. **Mở đàm phán**, ba lựa chọn. (a) **Historical:** tiếp tục đàm phán nhưng chưa cam kết mua; báo chí năm 2011 mô tả đàm phán chỉ còn vướng chi tiết tài chính. Nhánh này đi qua bước xem xét rồi đặt `VIE_sigma_suspended` và kết thúc, không có Sigma operational. (b) **Chuyển sang mua sắm:** đi tiếp các bước 2 đến 5. (c) **Từ bỏ:** đặt `VIE_sigma_cancelled`.
2. **Quy mô** (chỉ nhánh mua sắm): 2, 4, 6 hoặc hoãn.
3. **Cấu hình:** Full Western (tích hợp cao, logistics mới), Hybrid, Domestic adaptation (đắt, chậm, cộng `VIE_var_integration_exp`).
4. **Funding Gate:** `cost = quantity × unit_cost × config_multiplier`. Qua cổng nếu `VIE_var_naval_budget_room ≥ cost`; ngược lại người chơi chọn cắt quy mô, hoãn, hủy, hoặc tìm nguồn tài chính.
5. **Thực hiện:** hợp đồng → đóng → thử nghiệm → bàn giao → operational.

| Kết quả | Điều kiện xác định | Số lượng |
| --- | --- | --- |
| Collapse | Chọn nhánh Historical (chưa cam kết) ở bước 1, hoặc hủy ở Funding Gate | 0 |
| Limited | Quy mô 2 qua Funding Gate | 2 |
| Full | Quy mô 4 qua Funding Gate | 4 |
| Expanded | Quy mô 6 qua Funding Gate, cần `VIE_navy_modernization` | 6 |

Người chơi đi đường lịch sử mà không chủ động cam kết sẽ không có Sigma. Người muốn Sigma phải chọn nó và chịu chi phí. Sigma không phải tiền đề của Systems Integration.

Sau khi hết cửa sổ, Decision `sigma_late` mở được từ cả `VIE_sigma_missed` và `VIE_sigma_suspended`, để người chơi chuyển sang nhánh mua sắm muộn với chi phí +25%. Tài liệu không giả định nguyên nhân địa chính trị cho việc đàm phán không đi tới hợp đồng; nhãn Historical chỉ dựa trên việc đàm phán chưa chốt được tài chính.

## 5. Trục 2 – Công nghiệp quốc phòng hải quân

Sáu Focus mở năng lực, năm Decision biến năng lực thành hiện thực. Focus 3 và 4 chạy song song, Focus 5 chờ cả hai, Focus 6 là capstone. Không Decision nào cấp tàu; phần thưởng luôn là capability, kinh nghiệm hoặc giảm chi phí.

### 5.1 Sáu Focus

| # | Focus | Điều kiện mở (Quy tắc 6 bản sửa) | Ngày | Khi hoàn thành |
| --- | --- | --- | --- | --- |
| 1 | `VIE_naval_defence_law` | `VIE_defence_industry_modernization`; không trong khủng hoảng tài khóa nghiêm trọng | ≥ 2005 | Đặt `VIE_cap_naval_institution` |
| 2 | `VIE_ba_son_shipyards` | Focus 1 | ≥ 2005 | Kích hoạt Decision 1 |
| 3 | `VIE_naval_mro` | Focus 2; `VIE_var_hulls_operational ≥ 4` (trạng thái thế giới) | ≥ 2012 | Kích hoạt Decision 2 |
| 4 | `VIE_small_combatant_construction` | Focus 2 | ≥ 2010 | Kích hoạt Decision 3 |
| 5 | `VIE_naval_systems_integration` | Focus 3 và 4; `VIE_var_ext_support ≥ 1` (năng lực do nhánh khác sở hữu) | ≥ 2018 | Kích hoạt Decision 4 |
| 6 | `VIE_naval_defence_2030` | Focus 3, 4, 5 | ≥ 2028 | Kích hoạt Decision 5 |

Ba điều khác bản 1. Focus 3 không còn neo vào 2014: điều kiện là có ít nhất 4 thân tàu chủ lực đang hoạt động (theo lịch sử đạt khoảng 2011, sau khi hai Gepard đầu giao), và nhánh tàu ngầm của Decision 2 mới đòi Kilo đã giao. Focus 4 chỉ còn Focus 2 và ngày; `VIE_molniya_domestic_started` và kinh nghiệm đóng tàu không còn gate Focus mà chỉ mở tier 3 của Decision 3. Focus 6 chỉ còn Focus tiền đề và ngày; ngưỡng kinh nghiệm chuyển thành điều kiện bắt đầu của Decision 5 (mục 5.6).

### 5.2 Decision 1 – Phát triển năng lực Ba Son

Event 1 chọn định hướng. Vì cả hai nhánh MRO và Small Combatant đều bắt buộc, lựa chọn phải đổi lấy thứ khác ngoài thứ tự:

| Định hướng | Kinh nghiệm khởi điểm | Thời lượng nhánh sau | Chi phí |
| --- | --- | --- | --- |
| Shipbuilding trước | `shipbuilding_exp` +12 | Decision 3 giảm 25%, Decision 2 tăng 25% | ×1,0 |
| MRO trước | `mro_exp` +12 | Decision 2 giảm 25%, Decision 3 tăng 25% | ×1,0 |
| Cân bằng | mỗi loại +6 | không đổi | ×1,15 |

Event 2 chọn mức đầu tư (Cơ bản, Mở rộng, Trọng điểm, xem mục 3.3). Event 3 hoàn thiện: đặt `VIE_cap_ba_son_yard` ở mốc 40% tiến độ để không chặn ToT Molniya, đặt `VIE_cap_ba_son_complete` và `VIE_var_ba_son_tier` khi kết thúc.

### 5.3 Decision 2 – Nội địa hóa MRO hải quân

| Event | Lựa chọn | Điều kiện | Đánh đổi |
| --- | --- | --- | --- |
| 1 Trọng tâm | Tàu ngầm | `VIE_kilo_qty_delivered ≥ 1` | Chỉ mở MRO Kilo |
| 1 Trọng tâm | Tàu mặt nước | Đã giao ít nhất 1 Gepard hoặc Molniya | Chỉ mở MRO mặt nước |
| 1 Trọng tâm | Toàn hạm đội | Cả hai điều kiện trên | Chi phí ×1,3 |
| 2 Nguồn hỗ trợ | Hợp tác Nga (**Historical**) | Nga tồn tại | Chi phí ×0,8, nhanh hơn 25%, trần `mro_exp` 50, đặt `VIE_mro_russia_dependent` |
| 2 Nguồn hỗ trợ | Tự chủ | không | Chi phí ×1,4, chậm hơn 25%, trần `mro_exp` 100, không phụ thuộc Nga |
| 3 Mức nội địa hóa | Cơ bản, Chuyên sâu, Tự chủ cao | mức sau cần `mro_exp` đủ ngưỡng | Đặt `VIE_cap_naval_mro` tier 1–3, giảm chi phí duy trì hạm đội |

MRO tàu ngầm Kilo trong lịch sử đặt ở Cam Ranh với hỗ trợ của Nga, không đặt ở Ba Son (mục 8.3). Lựa chọn Historical vì vậy là hợp tác Nga; tự chủ là đường alt-history. Focus 3 vẫn đi sau Ba Son để giữ chuỗi Trục 2, nhưng khi viết localisation, địa điểm MRO tàu ngầm là Cam Ranh.

### 5.4 Decision 3 – Chương trình đóng tàu chiến đấu cỡ nhỏ

Decision này không cấp tàu. Nó cấp capability, kinh nghiệm và một hệ số giảm chi phí áp dụng cho các chương trình đóng tàu nhỏ về sau, kể cả pha 2 của Molniya nếu còn mở, hoặc khi mở lại qua Decision molniya\_late.

| Event | Lựa chọn | Kết quả |
| --- | --- | --- |
| 1 Chuyên hóa | Tuần tra | `shipbuilding_exp` +6, hệ số chi phí tàu nhỏ −20% |
| 1 Chuyên hóa | Tốc độ cao | `shipbuilding_exp` +8, hệ số chi phí −15% |
| 1 Chuyên hóa | Đa dụng | `shipbuilding_exp` +5, hệ số chi phí −10% |
| 2 Mức sản xuất | Lô thử nghiệm / Sản xuất hàng loạt / Chuyển giao công nghệ | Tier 1 / 2 / 3; tier 3 cần `VIE_molniya_domestic_started` |
| 3 Hoàn thiện | (tự động) | Đặt `VIE_cap_small_combatant`, tăng MIO Ba Son |

### 5.5 Decision 4 – Naval Systems Integration

Mỗi lĩnh vực ưu tiên đòi đúng nguồn hỗ trợ từ nhánh khác, nên lựa chọn phụ thuộc vào việc người chơi đã đầu tư ở đâu.

| Lĩnh vực | Điều kiện | Kết quả |
| --- | --- | --- |
| Electronics | `VIE_ext_viettel_mil_tech` hoặc `VIE_ext_c4isr` | Mở tích hợp cảm biến, liên lạc, hỏa lực; cộng `integration_exp` |
| Weapons | `VIE_ext_naval_missile` | Mở tích hợp vũ khí và điều khiển hỏa lực |
| Full System Integration | Một trong hai nguồn điện tử và `VIE_ext_naval_missile`; chi phí ×1,5 | Cảm biến + C4ISR + vũ khí + combat management |

Event 2 chọn mức nội địa hóa (Cơ bản, Cân bằng, Tự chủ cao) và Event 3 đặt `VIE_cap_integration` tier 1–3. Sigma không phải điều kiện; nếu có Sigma, mức Cân bằng cho thêm `integration_exp`.

### 5.6 Decision 5 – Naval Industrial Development 2030

Decision 5 mở khi Focus 6 hoàn thành. Event 1 chỉ bắt đầu khi `VIE_var_shipbuilding_exp ≥ 50` và `VIE_var_mro_exp ≥ 30`; thiếu thì Decision ở trạng thái chờ và tiếp tục khi đủ, không chiếm slot. Event 1 chọn ưu tiên: Shipbuilding, MRO, Systems Integration hoặc Comprehensive. Event 2 chọn mức tự chủ, có ngưỡng cụ thể:

| Mức tự chủ | Nội dung | Điều kiện |
| --- | --- | --- |
| Limited Autonomy | Tự chủ thân tàu, nhập phần lớn hệ thống | Không thêm |
| Integrated Industry | Thân tàu + MRO + một phần integration | `VIE_var_ba_son_tier ≥ 2` |
| High Autonomy | Toàn bộ, nhiều hệ thống nội địa | `VIE_var_ba_son_tier = 3` và `VIE_cap_integration` (tier ≥ 2 trong VIE\_var\_integration\_tier) |

Event 3 đặt `VIE_cap_mature_naval_industry`. Không cấp hạm đội miễn phí; phần thưởng là năng lực công nghiệp.

## 6. Liên kết giữa hai trục

Hai trục nối nhau qua sáu cạnh, và chỉ Molniya nối theo cả hai chiều. Vòng phát triển tích cực vẫn còn, nhưng chạy qua biến kinh nghiệm cộng dồn, không qua prerequisite, nên không tạo vòng phụ thuộc.

&#91;embedded content: hai trục nối nhau · 5 cạnh\]

Chuỗi giữa là Trục 2 theo lớp; các khung màu là Trục 1. Molniya pha 2 là cạnh hai chiều duy nhất: đọc cờ xưởng từ lớp 1 và ghi kinh nghiệm cho lớp 2.

| # | Chiều | Cạnh | Qua | Ghi chú |
| --- | --- | --- | --- | --- |
| 1 | Trục 2 → Trục 1 | Ba Son yard → Molniya pha 2 | `VIE_cap_ba_son_yard` | Đạt ở mốc 40% Decision 1, khoảng 2006–2008, trước cửa sổ pha 2 (2009-06) |
| 2 | Trục 1 → Trục 2 | Molniya pha 2 → Small Combatant | `VIE_molniya_domestic_started`, `VIE_var_shipbuilding_exp` | Mở tier 3 của Decision 3; không gate Focus 4 |
| 3 | Trục 1 → Trục 2 | Kilo → MRO tàu ngầm | `VIE_kilo_qty_delivered`, `VIE_opp_sub_mro` | Cơ hội, không tự tạo capability |
| 4 | Trục 1 → Trục 2 | Gepard, Molniya → MRO mặt nước, Focus 3 | `VIE_var_hulls_operational` | Focus 3 cần ít nhất 4 thân tàu |
| 5 | Trục 1 → Trục 2 | Bastion-P → Weapons integration | `VIE_ext_naval_missile` | Ngành tên lửa là nguồn thay thế cùng đặt flag này |
| 6 | Trục 1 → Trục 2 | Sigma → Integration (tùy chọn) | `VIE_var_integration_exp` | Chỉ là phần thưởng thêm, không phải tiền đề |

### Vì sao không có vòng

Mọi prerequisite đi theo một chiều qua năm lớp:

1. Lớp 0 – Thể chế: Focus 1.
2. Lớp 1 – Xưởng: Focus 2, Decision 1, `VIE_cap_ba_son_yard`.
3. Lớp 2 – Năng lực nền: Focus 3 (MRO) và Focus 4 (Small Combatant), song song.
4. Lớp 3 – Tích hợp: Focus 5 cùng Decision 4.
5. Lớp 4 – Trưởng thành: Focus 6 cùng Decision 5.

Trục 1 chỉ đọc lớp 1 (Molniya pha 2) và chỉ ghi biến đầu ra cho lớp 2 trở lên. Lớp 2 trở đi không ghi vào bất kỳ điều kiện cổng nào của Trục 1; chúng chỉ đổi hệ số chi phí. Nhờ vậy "Molniya cần Small Combatant" và "Small Combatant cần Molniya" không thể cùng đúng.

## 7. Bảng flag và variable

Toàn bộ trạng thái được lưu trong sáu nhóm: capability, kinh nghiệm và tier, trạng thái chương trình Trục 1, trạng thái Decision, biến điều khiển, và điều kiện đọc từ nhánh khác. Mọi thứ Trục 2 cần đọc đều nằm trong các bảng này; nếu một điều kiện không có ở đây thì nó không được dùng làm cổng.

Bản 2.4: các bảng dưới là tập tối đa. Theo quy ước MD (mục 16.3), khi code hãy bỏ các flag phản chiếu trạng thái có sẵn và các biến `_progress`, chỉ giữ flag cho chuyển tiếp lịch sử. Mỗi chương trình có event hỏi cần thêm hai flag chuyển tiếp `_offered` và `_skipped`.

### 7.1 Quy ước đặt tên

| Tiền tố | Loại | Ai được ghi |
| --- | --- | --- |
| `VIE_cap_*` | Country flag, vĩnh viễn | Chỉ Decision CNQP tương ứng |
| `VIE_var_*` | Biến số | Decision, Event Trục 1 (theo bảng 7.3) |
| `VIE_<mã>_*` | Trạng thái chương trình Trục 1 (`kilo`, `gepard1`, `gepard2`, `bastion`, `molniya`, `sigma`) | Event của chương trình đó |
| `VIE_dec_*` | Trạng thái Decision | Chính Decision đó |
| `VIE_ext_*` | Điều kiện do nhánh khác đặt | Chỉ nhánh sở hữu; Trục 2 chỉ đọc |

### 7.2 Capability flag (Trục 2)

| Flag | Đặt bởi | Khi nào | Được đọc bởi |
| --- | --- | --- | --- |
| `VIE_cap_naval_institution` | Focus 1 | Hoàn thành Focus | Điều kiện hiển thị của mọi Decision CNQP |
| `VIE_cap_ba_son_yard` | Decision 1 | Mốc 40% tiến độ | Molniya pha 2, Decision 3 |
| `VIE_cap_ba_son_complete` | Decision 1 | Kết thúc | Decision 5 |
| `VIE_cap_naval_mro` | Decision 2 | Kết thúc; kèm `VIE_cap_naval_mro_sub` và/hoặc `VIE_cap_naval_mro_surface` theo trọng tâm | Decision 5, hiệu ứng chi phí duy trì |
| `VIE_cap_small_combatant` | Decision 3 | Kết thúc | Decision 5, hệ số chi phí tàu nhỏ |
| `VIE_cap_integration` | Decision 4 | Kết thúc; kèm `VIE_cap_integration_electronics`, `_weapons`, hoặc `_full` theo lĩnh vực | Decision 5 |
| `VIE_cap_mature_naval_industry` | Decision 5 | Kết thúc | Hiệu ứng cuối, các chương trình tương lai |

### 7.3 Biến kinh nghiệm, tier và điều khiển

| Biến | Khoảng | Cộng bởi (giá trị khởi điểm) | Đọc bởi |
| --- | --- | --- | --- |
| `VIE_var_shipbuilding_exp` | 0–100 | Decision 1: +12 hoặc +6 theo định hướng, +5/+10/+15 theo mức đầu tư. Decision 3: +5 đến +8 theo chuyên hóa, +5/+10/+15 theo mức sản xuất. Molniya pha 2: +3 mỗi tàu bàn giao | Decision 5 (ngưỡng bắt đầu) |
| `VIE_var_mro_exp` | 0–100, trần 50 nếu `VIE_mro_russia_dependent` | Decision 1: +12 hoặc +6. Decision 2: +10/+20/+30 theo mức nội địa hóa | Decision 5 (ngưỡng bắt đầu), mức của Decision 2 |
| `VIE_var_integration_exp` | 0–100 | Decision 4: +10/+20/+30 theo mức nội địa hóa. Sigma cấu hình Domestic: +8, Hybrid: +4 | Decision 5 |
| `VIE_var_ba_son_tier` | 0–3 | Decision 1 theo mức đầu tư | Molniya pha 2 (mức 2 + 8, 2 + 10), Decision 5 |
| `VIE_var_mro_tier` | 0–3 | Decision 2 | Hiệu ứng chi phí duy trì |
| `VIE_var_small_combatant_tier` | 0–3 | Decision 3 | Hệ số chi phí |
| `VIE_var_integration_tier` | 0–3 | Decision 4 | Decision 5 |
| `VIE_var_hulls_operational` | ≥ 0 | +1 mỗi thân tàu chủ lực bàn giao (Kilo, Gepard, Molniya, Sigma) | Focus 3 |
| `VIE_var_ext_support` | 0–3 | Số flag `VIE_ext_*` đang được đặt (chỉ ba flag hải quân, không tính VIE\_ext\_nuclear\_tech), tính lại mỗi tháng | Focus 5 |
| `VIE_var_naval_program_active` | 0–2 | +1 khi Decision bắt đầu, −1 khi kết thúc; Decision đang chờ không tính | Điều kiện bắt đầu mọi Decision |
| `VIE_var_naval_budget_room` | tính mỗi tháng | Lấy từ ngân sách quốc gia của MD; cần nối vào hệ thống tài chính hiện có | Funding Gate của Sigma, chi phí Decision |
| `VIE_small_combatant_cost_mult` | 0,8–1,0 | Đặt bởi chuyên hóa của Decision 3 | Chi phí các chương trình tàu nhỏ về sau |

### 7.4 Trạng thái chương trình Trục 1

| Chương trình | Flag trạng thái | Biến số lượng và cấu hình |
| --- | --- | --- |
| Kilo | `VIE_kilo_contracted`, `_complete`, `_missed`, `_cancelled`, `VIE_opp_sub_mro` | `VIE_kilo_qty_ordered`, `VIE_kilo_qty_delivered`, `VIE_kilo_training` (0 cắt giảm, 1 đầy đủ) |
| Gepard I | `VIE_gepard1_contracted`, `_complete`, `_missed` | `VIE_gepard1_qty_ordered`, `_qty_delivered`, `VIE_gepard1_config` (1 Standard, 2 ASW, 3 phòng không) |
| Gepard II | `VIE_gepard2_contracted`, `_complete`, `_missed`, `_cancelled` (cổng mở: `VIE_gepard1_complete`) | `VIE_gepard2_qty_ordered`, `_qty_delivered` |
| Bastion-P | `VIE_bastion_contracted`, `_complete`, `_missed` | `VIE_bastion_qty_ordered`, `_qty_delivered`, `VIE_bastion_deploy` (1 Bắc, 2 Trung, 3 Nam, 4 phân tán) |
| Molniya | Pha 1: `VIE_molniya_contracted`, `VIE_molniya_ru_complete`, `VIE_molniya_p1_missed`. Pha 2: `VIE_molniya_domestic_started`, `VIE_molniya_complete`, `VIE_molniya_p2_missed` | `VIE_molniya_ru_qty`, `VIE_molniya_vn_qty_ordered`, `VIE_molniya_vn_qty_delivered`, `VIE_molniya_path` (1 A, 2 B, 3 C) |
| Sigma | `VIE_sigma_contracted`, `VIE_sigma_suspended`, `VIE_sigma_missed`, `VIE_sigma_cancelled`, `VIE_sigma_complete` | `VIE_sigma_qty_ordered`, `_qty_delivered`, `VIE_sigma_config` (1 Full Western, 2 Hybrid, 3 Domestic) |

Mỗi chương trình có flag `_missed` khi hết cửa sổ mà chưa ký, dùng để mở đúng một Decision `P_late` cho chương trình đó (mục 3.1). Molniya có hai flag theo pha và một Decision `molniya_late`; Sigma còn mở `sigma_late` từ trạng thái `VIE_sigma_suspended`.

### 7.5 Trạng thái Decision (Trục 2)

| Decision | Flag | Biến | Lựa chọn được lưu |
| --- | --- | --- | --- |
| 1 Ba Son | `VIE_dec_ba_son_active`, `_done`, `_waiting` | `VIE_dec_ba_son_progress` (0–100) | `VIE_ba_son_orientation` (1 shipbuilding, 2 MRO, 3 cân bằng), `VIE_ba_son_invest` (1–3) |
| 2 MRO | `VIE_dec_mro_active`, `_done`, `_waiting`, `VIE_mro_russia_dependent` | `VIE_dec_mro_progress` | `VIE_mro_scope` (1 tàu ngầm, 2 mặt nước, 3 toàn hạm đội), `VIE_mro_level` (1–3) |
| 3 Small Combatant | `VIE_dec_smallcomb_active`, `_done`, `_waiting` | `VIE_dec_smallcomb_progress` | `VIE_smallcomb_spec` (1 tuần tra, 2 tốc độ cao, 3 đa dụng), `VIE_smallcomb_level` (1–3) |
| 4 Integration | `VIE_dec_integration_active`, `_done`, `_waiting` | `VIE_dec_integration_progress` | `VIE_integration_field` (1 electronics, 2 weapons, 3 full), `VIE_integration_level` (1–3) |
| 5 Naval 2030 | `VIE_dec_naval2030_active`, `_done`, `_waiting` | `VIE_dec_naval2030_progress` | `VIE_naval2030_priority` (1–4), `VIE_naval2030_autonomy` (1–3) |

Flag `_waiting` được đặt khi Event kế tiếp thiếu capability hoặc ngưỡng, và xóa khi đủ. Decision đang chờ không tính vào `VIE_var_naval_program_active`.

### 7.6 Điều kiện đọc từ nhánh khác

Ba flag này do nhánh sở hữu đặt. Trục 2 chỉ đọc. Nếu nhánh sở hữu chưa được xây, Focus 5 không thể mở, nên cần thống nhất chủ sở hữu trước khi code.

| Flag | Ý nghĩa | Chủ sở hữu đề xuất |
| --- | --- | --- |
| `VIE_ext_viettel_mil_tech` | Công nghệ quân sự Viettel đủ dùng cho điện tử hải quân | Nhánh điện tử / Viettel |
| `VIE_ext_c4isr` | Có năng lực C4ISR | Nhánh điện tử / C4ISR |
| `VIE_ext_naval_missile` | Có năng lực tên lửa hải quân | Nhánh công nghiệp tên lửa, hoặc Bastion-P hoàn tất (`VIE_bastion_complete`) |

### 7.7 Mẫu dùng trong script

```text
# Focus 5: chỉ đọc Focus, ngày, điều kiện thế giới
available = has_completed_focus(VIE_naval_mro)
        and has_completed_focus(VIE_small_combatant_construction)
        and VIE_var_ext_support >= 1 and date > 2018.1.1

# Decision 4, Event 1, lựa chọn Weapons
trigger = has_country_flag(VIE_ext_naval_missile)

# Kết thúc Decision 1: capability không phụ thuộc Focus kế tiếp
when progress >= 40 and not has_country_flag(VIE_cap_ba_son_yard):
    set_country_flag(VIE_cap_ba_son_yard)
```

Các lệnh cụ thể (đặt flag, cộng biến, MIO của Ba Son) cần đối chiếu với phiên bản Millennium Dawn đang dùng; bảng trên chỉ cố định tên và ngữ nghĩa.

## 8. Kiểm tra timeline và dữ kiện lịch sử

Đi đúng lịch sử, mọi cổng đều mở đúng lúc và không có chương trình nào bị chặn bởi chương trình khác. Điểm then chốt là xưởng Ba Son sẵn sàng trước cửa sổ ToT Molniya (2009-06) với biên độ lớn.

### 8.1 Đường lịch sử qua các cổng

| Mốc | Trục 1 | Trục 2 | Kiểm tra |
| --- | --- | --- | --- |
| 2003–2005 | Molniya pha 1 mở (cửa sổ 2003-06 → 2005-12); thỏa thuận 2003 cho 2 tàu, giấy phép mua khoảng 2005–2006 | – | Mốc chọn theo mục 8.3 |
| 2005 | Molniya pha 1 hết cửa sổ | Focus 1, 2 mở | Người chơi bắt đầu Trục 2 |
| 2006 | Gepard I mở (2006-01); Bastion-P mở từ 2006-07 | Decision 1 chạy | Mốc 40% của Decision 1 đến sau khoảng 5–10 tháng tùy mức đầu tư |
| 2006–2008 | 2 Molniya từ Nga về (2007–2008) | `VIE_cap_ba_son_yard` được đặt | Xưởng sẵn sàng trước 2009-06 nếu Focus 1 và 2 xong trước cuối 2007 |
| 2009 | Molniya pha 2 mở từ 2009-06; Kilo mở từ 2009-12 (ký 12/2009) | Decision 1 hoàn tất | Pha 2 chỉ đòi `cap_ba_son_yard`, đã có |
| 2010 | Chiếc Molniya đầu khởi đóng tại Ba Son | Focus 4 mở (≥ 2010) | Focus 4 chỉ cần Focus 2 và ngày; `VIE_molniya_domestic_started` chỉ mở tier 3 của Decision 3 |
| 2011 | Gepard I giao (tháng 3 và 8); Bastion-P đưa vào; Sigma mở từ 2011-10; Gepard II mở từ 2011-12 | Decision 3 có thể bắt đầu | Batch II cần `gepard1_complete`, thỏa từ tháng 8/2011 |
| 2012 | – | Focus 3 mở (≥ 2012) | `hulls_operational` ≥ 4 (2 Molniya Nga, 2 Gepard) đã thỏa từ 2011 |
| 2014–2017 | Kilo giao (tàu đầu 15/1/2014, tàu thứ sáu 20/1/2017); Molniya VN giao (cặp đầu giữa 2014, cặp hai 6/2015, cặp ba 10/2017) | Decision 2 (nhánh tàu ngầm cần Kilo đã giao) | `kilo_qty_delivered ≥ 1` từ tháng 1/2014 |
| 2015 | Ba Son dời khỏi trung tâm TP.HCM sang Phú Mỹ (mục 8.3) | – | Chỉ đổi mô tả địa điểm, không đổi cơ chế |
| 2017–2018 | Gepard II giao | Focus 5 mở (≥ 2018) | Cần Focus 3, 4 và một nguồn `VIE_ext_*` |
| 2028+ | – | Focus 6 mở | Chỉ cần Focus 3, 4, 5 và ngày; Decision 5 chờ `shipbuilding_exp ≥ 50` và `mro_exp ≥ 30` |

Rủi ro duy nhất của đường lịch sử là người chơi hoàn thành Focus 1 và 2 quá muộn (sau 2008). Khi đó pha 2 của Molniya chờ trong cửa sổ đến 2012-12, và nếu vẫn thiếu xưởng thì chuyển sang Decision `molniya_late` (mục 3.1).

### 8.2 Dữ kiện lịch sử cần xác minh

Bảng này chỉ còn các mục chưa xác minh được hoặc còn mâu thuẫn. Các mốc đã đối chiếu (Gepard I và II, Molniya, Kilo, MRO Kilo, Bastion-P, Sigma, TT-400TP, Ba Son) nằm ở mục 8.3. Nên đối chiếu các mục dưới đây trước khi viết localisation hoặc ghi nhãn Historical.

| Mục | Trong tài liệu | Vấn đề còn lại | Nên đối chiếu |
| --- | --- | --- | --- |
| Bastion-P | Hợp đồng khoảng 2006 (cửa sổ 2006-07) | Năm ký ghi 2005, 2006 hoặc 2007 tùy nguồn thứ cấp. Việc giao năm 2011 đã xác minh | Cơ sở dữ liệu SIPRI Arms Transfers (trang động, chưa truy cập được) |
| Sigma | Lịch sử = không có hạm đội operational | Chưa xác minh thời điểm và lý do chương trình dừng; nguồn thứ cấp ghi khoảng 2016 | Nguồn của Damen, Jane's |
| Molniya | 2 + 6 giao xong; quyền chọn thêm 4 tàu | bmpd ghi quyền chọn 4 tàu đã chuyển thành hợp đồng chắc tháng 4/2015; chưa thấy nguồn xác nhận việc giao | bmpd, Vympel |
| TT-400TP | Chiếc thứ tư giao 2014 | Chưa xác minh | Nguồn Chính phủ Việt Nam |
| Nguồn ngoài Nga và Hà Lan | Trục 1 chỉ có Nga và Hà Lan | Danh sách trang bị Hải quân trên Wikipedia (đoạn trích) ghi Hàn Quốc chuyển 2 tàu Pohang Flight III (2017, 2018) và 1 Flight IV (2025), Ấn Độ chuyển 1 tàu Khukri; chưa mở nguồn | Nguồn Chính phủ Việt Nam, báo quốc phòng |

Hai điểm kỹ thuật mod cũng cần xác nhận: tag của Nga trong Millennium Dawn dùng cho điều kiện "đối tác tồn tại", và cách nối `VIE_var_naval_budget_room` vào hệ thống ngân sách của MD.

### 8.3 Nguồn đã chọn cho các mốc có mâu thuẫn

Các mốc dưới đây có nguồn mâu thuẫn hoặc trước đây ghi "cần xác minh". Mỗi mốc được chọn theo bậc tin cậy của nguồn. Ngày bắt đầu cửa sổ của Trục 1 nay bằng mốc ký lịch sử đã chọn, vì event kích ngay khi cổng mở.

Bậc tin cậy, từ cao xuống thấp:

1. Phát biểu đương thời của bên trực tiếp (nhà máy, nhà xuất khẩu, chính phủ) do hãng tin như Interfax, TASS hoặc báo Chính phủ Việt Nam đưa lại.
2. Bài hồi cứu của hãng tin nhà nước hoặc trang chính thức: đáng tin nhưng có thể nhầm bên ký hợp đồng (nhà xuất khẩu hay nhà máy).
3. Trang chuyên ngành thứ cấp (Naval Today, Naval Technology, GlobalSecurity): dùng khi dẫn lại bậc 1 và 2.
4. Blog, wiki, diễn đàn: chỉ tham khảo.

Khi cùng bậc mâu thuẫn, chọn mốc có nhiều báo cáo độc lập và khớp chuỗi đóng và giao, ghi lại mốc còn lại, và nếu chênh lệch không đổi cơ chế thì không cần quyết. Mục ghi "(đã mở)" là trang tôi đã mở đọc trực tiếp; mục ghi "(đoạn trích)" chỉ đọc qua kết quả tìm kiếm.

| Chương trình | Mốc chọn | Nguồn chọn | Mốc khác và cách xử lý | Độ tin cậy |
| --- | --- | --- | --- | --- |
| Gepard II | Đơn đặt hàng 12/2011; cửa sổ 2011-12 → 2014-12; giao 2017–2018 | Naval Technology (đã mở): đặt lô hai 12/2011, keel 9/2013, giao dự kiến 2017–2018. Interfax dẫn phó giám đốc nhà máy Zelenodolsk, đăng lại trên Naval Today 8/12/2011 (đã mở). SIPRI Yearbook 2012 (đã mở): hai Gepard ASW đang đặt | TASS 2016 (đã mở) ghi hợp đồng ký năm 2012 với nhà máy; defensa.com 4/2014 (đoạn trích) ghi 10/2012. Xử lý: coi 2012 là hợp đồng cấp nhà máy (suy luận, chưa kiểm chứng), không đổi cơ chế | Cao |
| Molniya pha 1 | Thỏa thuận 2003 cho 2 tàu hoàn chỉnh; cửa sổ 2003-06 → 2005-12; giao 2007–2008 | TASS 3/2015 dẫn Tổng giám đốc Vympel (đã mở qua GlobalSecurity); bmpd (đoạn trích) ghi "thỏa thuận năm 2003" cho 2 tàu hoàn chỉnh | Interfax 12/2011 (đã mở) và Lenta.ru dẫn lại: mua giấy phép 12 tàu năm 2005; bmpd: hợp đồng lắp ráp 2006; Naval Technology: 3–4/2004. Xử lý: các mốc là các bước khác nhau của cùng gói (2003 thỏa thuận 2 tàu, 2005–2006 giấy phép, 2009 chuyển giao công nghệ), pha 1 khớp bước đầu | Trung bình |
| Molniya pha 2 | Chuyển giao công nghệ 2009; khởi đóng 2010; cặp đầu giao giữa 2014, cặp hai 2/6/2015, cặp ba 9/10/2017 | Sputnik 3/6/2015 (đã mở qua GlobalSecurity): thỏa thuận 2009, cặp đầu tháng 7 năm trước, cặp hai giao 2/6/2015. TASS 3/2015 (đã mở): khởi đóng 2010, giấy phép đến 2016 | bmpd và TopWar (đoạn trích): cặp ba đưa vào biên chế 9/10/2017, chậm gần một năm so với kế hoạch. Một nguồn trước đó ghi cặp đầu 24/6/2014; chênh lệch nhỏ | Cao |
| Kilo | Hợp đồng 12/2009; cửa sổ 2009-12 → 2011-12; tàu đầu biên chế 15/1/2014; tàu thứ sáu đến Cam Ranh 20/1/2017 | GlobalSecurity (đã mở): hợp đồng 12/2009, tàu đầu biên chế 15/1/2014, tàu thứ tư giao 30/6/2015. Xinhua 20/1/2017 (đã mở): tàu thứ sáu đến Cam Ranh, tàu thứ năm đến 2/2016 | Giá trị 1,8 hay 3,2 tỷ USD tùy nguồn, không ảnh hưởng mốc. Lễ thượng cờ hai tàu cuối 28/2/2017 (Wikipedia, đoạn trích) | Cao |
| MRO Kilo | Sửa chữa ở Cam Ranh với hỗ trợ của Nga, không ở Ba Son | GlobalSecurity, mục căn cứ (đã mở): đại diện Zvezdochka nói năm 2013 về cơ sở sửa chữa tại Cam Ranh, hạn 2015, phục vụ toàn bộ tàu Nga và Liên Xô, chuyên gia Nga tham gia thiết kế. USNI News 8/2012 (đoạn trích): hợp đồng gồm cơ sở bảo dưỡng trên bờ | Xưởng X52 của Hải quân tại Cam Ranh khánh thành 2012 và hỗ trợ Kilo (phân tích thứ cấp trên Medium, đoạn trích) | Trung bình đến cao |
| Bastion-P | Đưa vào 2011, hai hệ thống; đàm phán thêm cuối 2011 | SIPRI Yearbook 2012 (đã mở): nhập 2 hệ thống trong 2007–2011, đàm phán thêm cuối 2011. AMTI/CSIS 3/2015 (đoạn trích): hai tổ hợp vào 2011 | Năm ký 2005 (blog), 2006 (phân tích Nga qua blog), 2007 (C3S dẫn SIPRI). Cửa sổ 2006-07 bao 2006–2007 nên không đổi | Giao: cao. Ký: thấp |
| Sigma | Đàm phán 4 tàu 10/2011; cửa sổ 2011-10 → 2014-12; lịch sử không có tàu biên chế | GlobalSecurity (đã mở): 10/2011 đàm phán 4 tàu, thiết kế 9814 công bố ở Vietship 2014. SIPRI Yearbook 2014 (đoạn trích): đồng ý đặt 2 tàu tháng 8/2013 | DSNS xác nhận với Jane's 22/8/2013 (đoạn trích). Proceedings 3/2015 (đoạn trích) vẫn ghi 4 tàu đang đặt. Wikipedia ghi chương trình có vẻ đã hủy khoảng 2016; danh sách trang bị Hải quân không có Sigma. Xử lý: giữ Historical = không có Sigma | Trung bình |
| Gepard I | Ký 2006; biên chế 3/2011 và 8/2011 | Naval Technology (đã mở): ký 2006, HQ-011 biên chế 3/2011, HQ-012 biên chế 8/2011. Naval Today 12/2011 (đã mở) | Ngày ký 12/5/2006 (Wikipedia) hoặc 12/2006 (nguồn khác); cửa sổ 2006-01 bao cả hai | Cao |
| TT-400TP | Hồng Hà (Hải Phòng) đóng; khởi đóng 2009, chạy thử 2011, chiếc đầu đến 1/2012 | GlobalSecurity (đã mở) | Mốc chiếc thứ tư (2014) chưa xác minh | Trung bình |
| Ba Son | Dời khỏi trung tâm TP.HCM sang Phú Mỹ (Bà Rịa–Vũng Tàu) khoảng 2015 | Wikipedia (Ba Son Shipyard và Bạch Đằng Quay, đoạn trích): xưởng đóng cửa 2015 sau di dời, cảng hải quân đóng cùng năm; vietnam.vn 8/2025 (đoạn trích): di dời về cảng Phú Mỹ | defencerussia 29/6/2015 (đoạn trích): lễ giao cặp hai Molniya vẫn diễn ra tại xưởng Ba Son ở TP.HCM ngày 2/6/2015. Địa điểm giao cặp ba (2017) chưa xác minh | Trung bình |

Ghi chú ảnh hưởng thiết kế:

- **Molniya pha 1 đổi mốc ba lần.** Bản 2.1 chọn 2003, bản 2.2 đổi sang 2005, bản 2.3 quay lại 2003. Nguồn Nga (bmpd, TASS) tách gói thành các bước: thỏa thuận 2003 cho 2 tàu hoàn chỉnh, giấy phép 2005–2006, chuyển giao công nghệ 2009. Pha 1 khớp bước đầu.
- **Quyền chọn 4 tàu Molniya.** bmpd ghi quyền chọn đã chuyển thành hợp đồng chắc tháng 4/2015, nên các mức 2 + 8 và 2 + 10 của pha 2 có cơ sở lịch sử. Số tàu giao xong đã xác minh chỉ là 2 + 6.
- **MRO Kilo ở Cam Ranh.** Năng lực bảo dưỡng tàu ngầm không nằm ở Ba Son. Decision 2 giữ nhánh "hợp tác Nga" làm Historical, nhưng localisation cần ghi địa điểm là Cam Ranh.
- **Sigma.** Nhánh Historical nên có thêm một event ngắn tháng 8/2013: đàm phán đạt thỏa thuận cho 2 tàu nhưng chưa ký hợp đồng, rồi chuyển sang `suspended`.
- **Nhiều xưởng đóng tàu.** Ngoài Ba Son còn có Z189 (Hải Phòng), Hồng Hà, Song Thu (Đà Nẵng), X50, X51, X52 theo danh sách trang bị trên Wikipedia (đoạn trích). Năng lực đóng tàu nhỏ của Việt Nam vì vậy không chỉ nằm ở Ba Son; template dự trữ `VIE_std_patrol_tt400` (mục 13.3) cần ghi xưởng Hồng Hà.
- **Nguồn ngoài Nga và Hà Lan.** Pohang (Hàn Quốc) và Khukri (Ấn Độ) là ứng viên bổ sung cho Trục 1 hoặc 1B, chưa quyết định.

## 9. Di chuyển từ v7, khối lượng và triển khai

Khối lượng nội dung vừa phải cho một người làm: khoảng 39 event, 11 Decision và 6 Focus, và có thể nhân bản từ một chương trình mẫu (Molniya). Việc cần làm trước là gỡ phần cũ của v7 và chốt chủ sở hữu ba flag `VIE_ext_*`.

### 9.1 Di chuyển từ v7

- Gỡ `VIE_domestic_corvettes` cùng mọi tham chiếu `has_completed_focus` tới nó, và mọi hiệu ứng cấp Molniya từ Focus.
- Giữ Ba Son / Hồng Hà, dockyard và MIO Ba Son của v7, nhưng chuyển hiệu ứng vào Decision 1. Focus 2 chỉ kích hoạt Decision.
- Tìm các chỗ dùng `VIE_navy_modernization` và `VIE_russian_arms_deals` làm điều kiện của procurement; đổi thành thưởng (mục 4.1).
- Giữ nguyên node Doctrine (`VIE_navy_blue_water`, `VIE_path_maritime_denial`); chúng không thuộc chuỗi Ba Son.

### 9.2 Khối lượng nội dung

| Hạng mục | Số lượng ước tính | Ghi chú |
| --- | --- | --- |
| Event Trục 1 | 24 | Kilo 4, Gepard I 3, Gepard II 2, Bastion 2, Molniya 6, Sigma 7 |
| Event Trục 2 | 15 | 5 Decision × 3 Event |
| Decision | 11 | 5 chương trình CNQP + 6 Decision `P_late` cho Trục 1 (mỗi chương trình một Decision; Molniya late định tuyến theo pha) |
| Focus | 6 | Chuỗi Trục 2 |
| Event ẩn | 1 | Xung kiểm tra hàng tháng cho cả sáu chương trình |

Bàn giao từng chiếc dùng vòng lặp trên biến `_qty_delivered`, không viết một event cho mỗi tàu.

### 9.3 Rủi ro và cách giảm

| Rủi ro | Cách giảm |
| --- | --- |
| Con số cân bằng (chi phí, kinh nghiệm, ngưỡng) đều là giá trị khởi điểm | Playtest ba kịch bản: lịch sử, Ba Son muộn, đầu tư tối đa; chỉnh ngưỡng exp của Decision 3 và 5 trước |
| Ba flag `VIE_ext_*` chưa có chủ sở hữu | Chốt chủ sở hữu và tên flag trước khi làm Focus 5 |
| Nối `VIE_var_naval_budget_room` vào ngân sách MD | Làm phiên bản đơn giản trước (ngưỡng cố định theo GDP), nối hệ thống thật sau |
| AI không tự chạy Decision | Chạy thử AI-only đến 2020 và kiểm tra có Kilo, Gepard, Ba Son |
| Submod dân tộc chủ nghĩa hoặc Nga thay đổi quan hệ | Không sửa cổng lõi; thêm điều kiện riêng của submod vào từng chương trình khi cần |

### 9.4 Thứ tự triển khai

1. Khai báo các biến và flag chuyển tiếp ở mục 7 (bỏ flag phản chiếu, theo mục 16.3), cùng xung on\_monthly\_VIE.
2. Làm mẫu Molniya (hai pha) và Decision 1; kiểm tra `VIE_cap_ba_son_yard` được đặt trước 2009-06.
3. Nhân bản sang Kilo, Gepard I, Gepard II, Bastion-P.
4. Làm Focus 3, 4 và Decision 2, 3.
5. Làm Sigma, gồm Funding Gate và ba kết cục xác định.
6. Làm Focus 5, 6 và Decision 4, 5 sau khi ba flag `VIE_ext_*` có chủ.
7. Playtest bốn kịch bản: đường lịch sử; Ba Son sau 2008; AI-only; chiến tranh với Nga trong cửa sổ Kilo (chương trình phải bị bỏ lỡ và mở lại qua Decision `P_late`).

## 10. Trục 3 – Xây dựng lực lượng hải quân (bản sửa)

Trục 3 giữ triết lý gốc (con người → tổ chức → lực lượng nhỏ → lực lượng trung gian → hướng chiến lược) nhưng gọn hơn: khoảng 12–13 Focus mỗi lần chơi (22 node tổng), phần đào tạo chuyển sang Decision, và tàu mới đến từ Trục 1B chứ không từ Focus.

| Trục | Câu hỏi | Ghi gì |
| --- | --- | --- |
| 1 – Mua sắm (và 1B) | Việt Nam mua hoặc đặt đóng tàu nào? | Tàu, số lượng, `VIE_var_hulls_*` |
| 2 – CNQP | Việt Nam tự bảo dưỡng, đóng và tích hợp được đến đâu? | `VIE_cap_*`, tier, kinh nghiệm công nghiệp |
| 3 – Lực lượng | Ai vận hành, tổ chức ra sao, đi theo hướng nào? | `VIE_org_*`, readiness, tổ chức hạm đội, chọn nhánh |

Trục 3 đọc kết quả của Trục 1 và 2 để mở lựa chọn, và chỉ ghi biến vận hành. Nó không ghi gì làm tàu rẻ hơn, nhanh hơn hoặc mạnh hơn về công nghiệp.

### 10.1 Thiết kế cốt lõi

1. **Focus là cột mốc, Decision là việc.** Đào tạo sĩ quan, kíp, vũ khí, chỉ huy là Decision chạy song song cho hai lực lượng (mặt nước, tàu ngầm), có biến readiness. Focus chỉ mở Decision và đánh dấu tổ chức.
2. **Chuỗi mốc một chiều:** chuẩn hóa đào tạo → hai lực lượng song song → Command Reform I → cơ cấu lực lượng ban đầu → Command Reform II → lực lượng trung gian → điểm rẽ chiến lược.
3. **Đường lịch sử có đích.** Điểm rẽ có ba nhánh, gồm Maritime Denial (ngăn chặn ven bờ) là nhánh lịch sử. Bản gốc chỉ có Greenwater và Bluewater, nên người chơi đúng lịch sử không có chỗ đi.

&#91;embedded content: Trục 3 · 8 Focus dùng chung, 3 nhánh\]

Đọc từ trên xuống. Các khung tô màu ở hai bên là đầu vào hoặc đầu ra từ Trục 1, 1B và 2; nhánh Maritime Denial là nhánh lịch sử.

### 10.2 Quy tắc bổ sung

Hai quy tắc dưới đây bổ sung cho chín quy tắc ở mục 2, còn Quy tắc 6 được nhắc lại từ mục 2, nơi nó đã được cập nhật ở bản 2.1.

| # | Quy tắc | Nội dung |
| --- | --- | --- |
| 6 (nhắc lại từ mục 2) | Focus chỉ dùng bốn loại điều kiện | (a) Focus tiền đề, kể cả "hoặc" và "ít nhất 2 trong 3"; (b) ngày; (c) trạng thái thế giới như số thân tàu operational theo lớp; (d) năng lực do nhánh khác sở hữu (`VIE_ext_*`). Không dùng kết quả chương trình hay Decision: `VIE_cap_*`, `_started`, biến kinh nghiệm, biến readiness |
| 10 (mới) | Trục 3 chỉ cấp modifier vận hành | XP, thời gian huấn luyện, readiness, tổ chức, chỉ huy, hậu cần, hiệp đồng. Không cấp modifier sản xuất, chi phí đóng tàu hoặc trang bị |
| 11 (mới) | Namespace riêng | Trục 3 dùng `VIE_org_*` cho flag và `VIE_var_*_readiness` cho biến. Không ghi `VIE_cap_*` (của Trục 2) |

Hai điều chỉnh nhỏ:

- **Quy tắc 8 (Doctrine):** `VIE_path_maritime_denial` và `VIE_navy_blue_water` trở thành lối vào của hai nhánh chiến lược ở Trục 3. Chúng vẫn không nằm trong chuỗi Ba Son. Cần đối chiếu với các node và tham chiếu đang có ở v7 trước khi đổi.
- **Quy tắc 5 (cửa sổ lịch sử):** giữ nguyên. Lối vào alt-history của Trục 1B là Decision, và được phép đòi Focus của Trục 3. Deal lịch sử của Trục 1 thì không.

### 10.3 Phạm vi và ranh giới

Trục 3 chỉ xây hạm đội chính quy (tàu mặt nước, tàu ngầm) và tổ chức của nó. Hai mảng nằm ngoài báo cáo này:

- **Nhánh Biển Đông (một focus tree riêng):** cảnh sát biển, kiểm ngư, lực lượng bán quân sự trên biển, xung đột với Trung Quốc, tập trận, thăm cảng, huấn luyện với Ấn Độ và Nga. Vì vậy báo cáo không có Trục 4. Trường Sa và phòng thủ bờ chưa được phân về nhánh nào.
- **Nhánh Vietnam Special Force (chưa thiết kế):** Hải quân đánh bộ đã gỡ khỏi Trục 3 cùng các phần liên quan (Decision Marine, readiness, bộ chỉ huy Marine), và sẽ chuyển sang nhánh này.

Quy tắc ranh giới: hai nhánh trên không phải điều kiện Focus của Trục 1 đến 3. Khi cần thông tin về hạm đội, chúng đọc trạng thái thế giới (ví dụ `VIE_var_hulls_amphib`) theo Quy tắc 6(c). Hiện Trục 3 không đọc gì từ chúng; nếu sau này cần thì qua `VIE_ext_*` theo Quy tắc 6(d).

## 11. Focus và Decision của Trục 3

Trục 3 có 22 node Focus, gồm 8 node dùng chung và 14 node chia trong ba nhánh, nhưng mỗi lần chơi chỉ đi 12 hoặc 13 Focus. Mã T2 đã bị gỡ (Hải quân đánh bộ) và các mã còn lại giữ nguyên để khỏi đánh số lại. Đào tạo và tổ chức là Decision chạy song song. Mọi ngày trong mục này là giá trị khởi điểm, cần cân bằng.

### 11.1 Chuỗi dùng chung (8 Focus)

| # | Focus | Điều kiện mở (theo Quy tắc 6) | Ngày | Khi hoàn thành |
| --- | --- | --- | --- | --- |
| T1 | `VIE_naval_training_standardization` | `VIE_navy_modernization` | ≥ 2005 | Đặt `VIE_org_naval_training`, cộng Navy XP, giảm thời gian huấn luyện |
| T3 | `VIE_surface_force_development` | T1 | ≥ 2005 | Mở Decision Lực lượng mặt nước |
| T4 | `VIE_submarine_force_development` | T1 | ≥ 2008 | Mở Decision Lực lượng tàu ngầm |
| T5 | `VIE_naval_command_reform_1` | T3 và T4 | ≥ 2010 (cần xác minh) | Dựng Naval HQ với Surface, Submarine, Support; mở Decision Hiệp đồng hạm đội |
| T6 | `VIE_first_force_structure` | T5; `VIE_naval_mro` hoặc `VIE_small_combatant_construction` (Trục 2); `VIE_var_hulls_operational ≥ 4` | ≥ 2012 | Mở Decision cơ cấu lực lượng ban đầu |
| T7 | `VIE_naval_command_reform_2` | T6 | ≥ 2014 | Tổ chức lại thành biên đội và hải đoàn, hợp nhất chỉ huy tác chiến |
| T8 | `VIE_medium_naval_force` | T7 | ≥ 2016 | Mở lối vào alt-history của Trục 1B: hộ vệ hạm nhẹ, khinh hạm cỡ trung, chống ngầm cơ động, tàu ngầm tấn công khu vực |
| T9 | `VIE_expand_naval_operating_range` | T7 và T8 | ≥ 2018 | Mở ba nhánh chiến lược (mục 11.5) |

T6 gate bằng Focus của Trục 2, không đọc `VIE_cap_*`. Điều này bỏ lỗi ở bản gốc: Focus 25 đòi capability của Decision, nên phải chờ Decision kết thúc.

### 11.2 Hai Decision lực lượng (chạy song song)

| Decision | Kích hoạt | Event 1 | Event 2 | Event 3 | Kết quả |
| --- | --- | --- | --- | --- | --- |
| Lực lượng mặt nước | T3 | Khung sĩ quan và chuẩn hóa kíp tàu | Chuyên môn: hỏa lực (radar, pháo, tên lửa, phòng không) hoặc chống ngầm (sonar, hiệp đồng trực thăng) | Bộ chỉ huy lực lượng mặt nước | `VIE_var_surface_readiness`, `VIE_var_asw_skill`, `VIE_org_surface_command` |
| Lực lượng tàu ngầm | T4 | Sĩ quan tàu ngầm: chuẩn bị nhân lực trước khi nhận tàu (**Historical**) hoặc chuẩn bị sớm hơn (alt, đắt, readiness khởi điểm cao hơn) | Kíp tàu ngầm và tác chiến dưới mặt biển | Bộ chỉ huy tàu ngầm; tùy chọn chương trình tàu ngầm mini (alt) | `VIE_var_sub_readiness`, `VIE_org_submarine_command` |

Đánh đổi để mỗi lựa chọn có nghĩa (Quy tắc 9):

- **Mức đầu tư:** Cơ bản (chi phí ×1,0, 12 tháng, readiness +15) hoặc Chuyên sâu (×1,5, 18 tháng, readiness +25). Mức chuyên môn chỉ tăng trần hướng đã chọn; hướng còn lại mở lại được bằng Event trễ với chi phí cao hơn.
- **Slot:** hai Decision này có bộ đếm riêng `VIE_var_force_program_active` với trần 2, tách khỏi giới hạn 2 của CNQP để không tranh nhau. Decision đang chờ không chiếm slot.
- **Readiness chỉ là modifier vận hành**: thời gian huấn luyện, tổ chức, độ sẵn sàng. Nó không gate Focus hay chương trình nào.

### 11.3 Decision Hiệp đồng hạm đội

Mở từ T5, gồm ba Event: huấn luyện hiệp đồng hạm đội (task force, XP); phối hợp tàu ngầm và tàu mặt nước; mạng lưới chống ngầm ven bờ. Kết quả là `VIE_var_fleet_organization`. Phần "tàu tấn công nhanh" và "đóng loạt lớn" của Focus 21–22 gốc bị bỏ khỏi Trục 3: mặt tổ chức nằm ở Decision này, mặt sản xuất thuộc Decision 3 của Trục 2 và Molniya mở rộng của Trục 1.

### 11.4 Cơ cấu lực lượng ban đầu (từ T6)

T6 mở một Decision ba lựa chọn, đặt `VIE_force_priority`. Ba lựa chọn chỉ cấp modifier vận hành (Quy tắc 10):

| Lựa chọn | Ưu tiên | Bonus vận hành | Đánh đổi | Khớp nhánh |
| --- | --- | --- | --- | --- |
| Coastal Defence | Tàu tấn công nhanh, tên lửa bờ, tàu ngầm | Chiến đấu ven bờ, hiệu quả nhiên liệu | Tầm hoạt động thấp hơn | Maritime Denial |
| Balanced | Tàu tấn công nhanh, hộ vệ hạm, ASW, tàu ngầm, khinh hạm nhẹ | Bonus nhỏ đều mọi mặt | Không có điểm mạnh nổi bật | Cả ba |
| Extended Range | Khinh hạm, đổ bộ, tàu ngầm, hậu cần | Tầm hoạt động, tổ chức hạm đội | Chi phí duy trì cao | Greenwater, Bluewater |

"Regional" ở bản gốc đổi tên thành Extended Range để không trùng với Greenwater. Lựa chọn nhánh ở T9 không bị khóa bởi `force_priority`, nhưng nếu lệch thì `VIE_var_fleet_organization` giảm tạm thời trong 12 tháng (chi phí chuyển đổi).

### 11.5 Điểm rẽ chiến lược (14 Focus)

T9 mở ba nhánh có Focus mở đầu loại trừ nhau. Nhánh Maritime Denial là nhánh lịch sử.

| Nhánh | # | Focus | Điều kiện chính | Hiệu ứng |
| --- | --- | --- | --- | --- |
| Maritime Denial (lịch sử) | D1 | `VIE_path_maritime_denial` | T9 | Ngăn chặn biển; tổ chức phòng thủ ven bờ |
|  | D2 | `VIE_denial_integrated_defence` | D1 | Phòng thủ ven bờ tích hợp; mở Bastion mở rộng và tàu ngầm mini (1B) |
|  | D3 | `VIE_denial_submarine_fleet` | D2 | Lực lượng tàu ngầm ngăn chặn; mở tàu ngầm tấn công khu vực (1B) |
|  | D4 | `VIE_denial_command` | D3 | Bộ chỉ huy phòng thủ ven bờ (capstone) |
| Greenwater (alt) | G1 | `VIE_greenwater_navy` | T9 | Hải quân khu vực |
|  | G2 | `VIE_regional_frigates` | G1 | Mở khinh hạm viễn hành (1B) |
|  | G3 | `VIE_amphibious_fleet` | G1 | Hạm đội đổ bộ (tàu và biên đội đổ bộ) |
|  | G4 | `VIE_lhd_program` | G2, G3 | Mở tàu đổ bộ trực thăng và LHD (1B) |
|  | G5 | `VIE_regional_fleet_command` | G4 | Bộ chỉ huy hạm đội khu vực (capstone) |
| Bluewater (alt) | B1 | `VIE_navy_blue_water` | T9 | Hải quân viễn dương |
|  | B2 | `VIE_ocean_escort_program` | B1 | Mở khinh hạm viễn dương và khu trục (1B) |
|  | B3 | `VIE_fleet_replenishment` | B1 | Bảo đảm hậu cần hạm đội (bắt buộc về logic) |
|  | B4 | `VIE_naval_aviation` | B1 | Không quân hải quân; mở tàu sân bay hạng nhẹ (1B) |
|  | B5 | `VIE_carrier_strike_group` | B2, B3, B4 | Capstone. Không đòi tàu, nhưng hiệu ứng tổ chức nhân theo số tàu sân bay thực tế; Decision thành lập nhóm tác chiến cần tàu sân bay và khu trục |

Hải quân đánh bộ đã tách khỏi Trục 3 và sẽ chuyển sang nhánh Vietnam Special Force; G3 chỉ còn đòi G1. Tàu sân bay và SSN là chương trình của Trục 1B, không phải Focus.

## 12. Trục 1B – Program Engine và chương trình alt-history

Mọi tàu mới của Trục 3 đến từ một Program Engine dùng chung: một chuỗi trạng thái cố định, còn dữ liệu mỗi chương trình là một dòng bảng. Trục 1B là alt-history nên lối vào là Decision, không có cửa sổ lịch sử, và dùng lại Funding Gate xác định của Sigma.

### 12.1 Chuỗi trạng thái dùng chung

1. **Mở:** Decision hiện khi đủ điều kiện (Focus của Trục 3, ngày, đối tác nếu nhập khẩu).
2. **Quy mô:** chọn số tàu.
3. **Template và mức nội địa hóa:** chọn template (mục 13) và một trong ba đường: nhập khẩu, hybrid, nội địa.
4. **Funding Gate:** `cost = quantity × unit_cost × template_multiplier × localization_multiplier`. Qua cổng nếu `VIE_var_naval_budget_room ≥ cost`; ngược lại người chơi chọn cắt quy mô, hoãn, hủy hoặc tìm nguồn tài chính.
5. **Hợp đồng và đóng:** thời gian đóng có sàn `lead_min` (tháng) theo từng chương trình, để đầu tư nhiều không cho ra tàu quá sớm.
6. **Bàn giao từng chiếc:** cộng `VIE_<p>_qty_delivered`, `VIE_var_hulls_operational` và bộ đếm theo lớp `VIE_var_hulls_<lớp>`.
7. **Hoàn tất:** đặt `VIE_<p>_complete` và cộng kinh nghiệm cho Trục 2 theo mức nội địa hóa (`shipbuilding_exp`, `integration_exp`).

Một engine thay cho mười một chuỗi event riêng: nội dung chỉ còn khoảng 7 event chung cộng dữ liệu, dùng cùng quy ước đặt tên ở mục 7.4.

### 12.2 Bảng chương trình

Lối vào của Trục 1B là alt-history, nên được phép đòi Focus của Trục 3 (Quy tắc 5). Điều kiện năng lực của Trục 2 là điều kiện của Decision chương trình, không phải của Focus, nên không vi phạm Quy tắc 6.

| Mã | Chương trình | Lối vào (Focus Trục 3, ngày) | Template chính | Điều kiện đường nội địa (Trục 2) |
| --- | --- | --- | --- | --- |
| P1 | Hộ vệ hạm nhẹ | T8, ≥ 2016 | `std_corvette_domestic` | `VIE_var_small_combatant_tier ≥ 2` và `VIE_var_ba_son_tier ≥ 2` |
| P2 | Khinh hạm cỡ trung | T8, ≥ 2018 | `std_frigate_medium` | `VIE_var_integration_tier ≥ 1` và `VIE_var_ba_son_tier ≥ 2` |
| P3 | Chống ngầm cơ động | T8, ≥ 2018 | `std_frigate_asw` | `VIE_var_integration_tier ≥ 1` |
| P4 | Tàu ngầm tấn công khu vực | T8 và (D3 hoặc G2), ≥ 2020 | `std_ssk_regional` | `VIE_var_ba_son_tier = 3`, `VIE_var_integration_tier ≥ 2`, `VIE_cap_naval_mro_sub` |
| P5 | Tàu ngầm mini | Event tùy chọn của Decision Tàu ngầm, hoặc D2 | `std_minisub` | `VIE_var_ba_son_tier ≥ 1` |
| P6 | Bastion-P mở rộng | D2 | Hệ thống bờ, không phải template tàu | Không có; chỉ nhập khẩu |
| P7 | Tàu đổ bộ trực thăng và LHD | G4, ≥ 2022 | `std_lpd`, `std_lhd` | `VIE_var_ba_son_tier = 3` |
| P8 | Khu trục | B2, ≥ 2024 | `std_destroyer` | `VIE_var_integration_tier ≥ 2` và `VIE_var_ba_son_tier = 3` |
| P9 | Tàu tiếp tế hạm đội | B3, ≥ 2022 | `std_aor` | `VIE_var_ba_son_tier ≥ 2` |
| P10 | Tàu sân bay hạng nhẹ | B4, ≥ 2028 | `std_carrier_light` | `VIE_cap_mature_naval_industry` |
| P11 | Tàu ngầm hạt nhân (SSN) | B5, ≥ 2030, `VIE_ext_nuclear_tech` | `std_ssn` | `VIE_cap_mature_naval_industry` |

Mỗi chương trình luôn có đường nhập khẩu và hybrid, dùng cổng chung (đối tác tồn tại, không chiến tranh) cộng Funding Gate. Đối tác cụ thể cần được định nghĩa theo hướng chính trị của từng nhánh, bản này chưa chọn.

### 12.3 Quy tắc riêng của Trục 1B

- Không có cửa sổ lịch sử và không có event tự kích. Mọi chương trình là Decision thủ công.
- Focus chỉ mở lối vào, không cấp tàu (Quy tắc 1).
- Tối đa 2 chương trình 1B chạy cùng lúc (`VIE_var_procurement_1b_active`), tách khỏi hai bộ đếm CNQP và lực lượng.
- Đường nội địa cộng kinh nghiệm cho Trục 2, nhập khẩu thì ít hơn. Nhờ đó vòng phát triển tích cực có cả ở phần alt-history: chương trình nội địa → tier cao hơn → mở chương trình nội địa lớn hơn.
- Mốc 2028–2030 của tàu sân bay và SSN là giá trị khởi điểm, cần cân bằng theo ngân sách hải quân.

## 13. Template thiết kế tàu

Template thiết kế tàu là một bản ghi thiết kế dùng lại: mỗi template cố định hull, nhóm module và hệ số, còn chương trình chỉ chọn template thay vì tự mô tả tàu. Nhờ đó cùng một tàu (ví dụ Molniya) nhất quán ở Trục 1, 1B và 2, và thêm tàu mới chỉ cần thêm một dòng bảng.

Hull và module cụ thể của Millennium Dawn chưa được đối chiếu. Các bảng dưới đây dùng nhóm slot trừu tượng; tên thật được điền khi code.

### 13.1 Cấu trúc một bản ghi template

| Trường | Ý nghĩa | Ví dụ |
| --- | --- | --- |
| `id` | Mã template | `VIE_std_fac_molniya` |
| `role` | Vai trò: FAC, corvette, khinh hạm, khu trục, tàu đổ bộ, SSK, tàu ngầm mini, tàu tiếp tế, tàu sân bay, SSN | FAC |
| `hull` | Hull trong MD (xem bảng 16.2) | điền khi code |
| `modules` | Theo nhóm slot: pháo, tên lửa chống hạm, phòng không, ASW, radar và CMS, động lực, hàng không, đặc biệt | 1 pháo chính, 16 tên lửa chống hạm |
| `parent` | Template gốc nếu là biến thể | Gepard ASW kế thừa Gepard tiêu chuẩn |
| `origin` | Historical hoặc Alt | Historical |
| `localization` | Các mức nội địa hóa được phép: 0 nhập khẩu, 1 hybrid, 2 nội địa | 0 và 2 |
| `unlock` | Ngày, đối tác, và tier Trục 2 (chỉ cho đường nội địa) | `VIE_var_ba_son_tier ≥ 2` |
| `cost_mult`, `build_mult`, `lead_min` | Hệ số chi phí, hệ số thời gian đóng, sàn thời gian (tháng) | ×1,0; ×1,0; 24 |
| `exp_reward` | Kinh nghiệm cộng cho Trục 2 mỗi tàu bàn giao | `shipbuilding_exp` +3 |
| `readiness_link` | Biến readiness của Trục 3 ảnh hưởng hiệu quả lớp tàu | `VIE_var_surface_readiness` |
| `class_counter` | Bộ đếm lớp | `VIE_var_hulls_fac` |

### 13.2 Ba quy tắc template

1. **Chương trình chọn template, không tự mô tả tàu.** Event chỉ đọc `VIE_<p>_template` (số nguyên).
2. **Biến thể là template con.** Chỉ đổi module, giữ hull, hệ số nhân từ cha. Các dòng cấu hình của Trục 1 (`VIE_gepard1_config`, `VIE_sigma_config`) ánh xạ sang template biến thể.
3. **Template không gate Focus (Quy tắc 6).** Template mở bằng ngày, đối tác và tier Trục 2 ở mức Decision chương trình.

Mức nội địa hóa dùng chung cho mọi template (giá trị khởi điểm):

| `localization` | Đường | Chi phí | Thời gian đóng | Kinh nghiệm cho Trục 2 |
| --- | --- | --- | --- | --- |
| 0 | Nhập khẩu | ×1,0 | ×1,0 | 0% |
| 1 | Hybrid | ×1,15 | ×1,2 | 50% của `exp_reward` |
| 2 | Nội địa | ×1,3 | ×1,4 | 100% của `exp_reward` |

### 13.3 Template lịch sử (tham chiếu)

Cấu hình tham chiếu của Molniya (Sputnik 6/2015, đã mở) và Gepard (Naval Technology, đã mở) đã đối chiếu: Molniya mang 16 tên lửa Uran-E, hai hệ pháo AK-630 và một pháo AK-176M; Gepard 3.9 có pháo AK-176M hoặc A-190, hai AK-630M hoặc tổ hợp Palma với Sosna-R, tên lửa Kh-35E (Club-N tùy chọn), ngư lôi và tên lửa chống ngầm, và sàn trực thăng Ka-28 hoặc Ka-31. Cấu hình Sigma và Kilo chưa mở nguồn.

| Template | Vai trò | Chương trình | Biến thể và cấu hình | Cấu hình tham chiếu |
| --- | --- | --- | --- | --- |
| `VIE_std_fac_molniya` | FAC tên lửa (Project 12418) | Molniya pha 1 và pha 2 | Pha 1: `localization` 0. Pha 2: `localization` 2 | 16 tên lửa chống hạm Uran-E, 1 pháo AK-176M, 2 pháo tầm gần AK-630M |
| `VIE_std_frigate_gepard_std` | Khinh hạm Gepard 3.9 tiêu chuẩn | Gepard I | `VIE_gepard1_config` = 1 (Standard); biến thể phòng không = 3 | Pháo AK-176, tổ hợp Palma, tên lửa chống hạm |
| `VIE_std_frigate_gepard_asw` | Khinh hạm Gepard 3.9 chống ngầm, con của bản tiêu chuẩn | Gepard II; Gepard I với config = 2 | Thêm module ASW | Ngư lôi, thiết bị phát hiện tàu ngầm |
| `VIE_std_ssk_kilo636` | Tàu ngầm diesel-điện | Kilo | Mức huấn luyện (`VIE_kilo_training`) là tham số vận hành, không phải biến thể | Cần xác minh |
| `VIE_std_corvette_sigma` | Corvette SIGMA 9814 | Sigma | `VIE_sigma_config` = 1 Full Western; 2 Hybrid và 3 Domestic là template con | Dài khoảng 98 m, khoảng 1.950 t, radar Smart-S, hệ TACTICOS; Exocet và VL MICA được báo cáo là lựa chọn |
| `VIE_std_patrol_tt400` (dự trữ) | Tàu tuần tra nội địa | Chưa có chương trình | – | Hồng Hà (Hải Phòng) đóng, khởi đóng 2009, chạy thử 2011 (mục 8.3) |

Bastion-P là hệ thống bờ, không có template tàu.

### 13.4 Template alt-history

| Template | Vai trò và nhóm module chính | Chương trình | `localization` | Readiness liên kết | Bộ đếm lớp |
| --- | --- | --- | --- | --- | --- |
| `VIE_std_corvette_domestic` | Corvette: pháo, chống hạm, phòng không điểm, sonar cơ bản | P1 | 0–2 | `surface_readiness` | `VIE_var_hulls_corvette` |
| `VIE_std_frigate_medium` | Khinh hạm: pháo, chống hạm, phòng không tầm trung, sàn trực thăng | P2 | 0–2 | `surface_readiness` | `VIE_var_hulls_frigate` |
| `VIE_std_frigate_asw` | Con của khinh hạm cỡ trung: sonar kéo, ngư lôi, trực thăng ASW | P3 | 0–2 | `asw_skill` | `VIE_var_hulls_frigate` |
| `VIE_std_ssk_regional` | Tàu ngầm tấn công khu vực: ngư lôi, tên lửa phóng qua ống, AIP | P4 | 0–1 | `sub_readiness` | `VIE_var_hulls_sub` |
| `VIE_std_minisub` | Tàu ngầm mini: ngư lôi nhẹ, đặc nhiệm ven bờ | P5 | 2 | `sub_readiness` | `VIE_var_hulls_minisub` |
| `VIE_std_lpd`, `VIE_std_lhd` | Tàu đổ bộ: ụ đổ bộ, sàn bay, chở lực lượng đổ bộ | P7 | 0–2 | `fleet_organization` | `VIE_var_hulls_amphib` |
| `VIE_std_destroyer` | Khu trục: phòng không tầm xa, chống hạm tầm xa, chống ngầm | P8 | 0–2 | `surface_readiness` | `VIE_var_hulls_destroyer` |
| `VIE_std_aor` | Tàu tiếp tế: tiếp tế trên biển | P9 | 0–2 | `fleet_organization` | `VIE_var_hulls_support` |
| `VIE_std_carrier_light` | Tàu sân bay hạng nhẹ: sàn bay, hàng không hải quân | P10 | 0–1 | `fleet_organization` | `VIE_var_hulls_carrier` |
| `VIE_std_ssn` | Tàu ngầm hạt nhân: lò phản ứng, ngư lôi, tên lửa | P11 | 0–1 | `sub_readiness` | `VIE_var_hulls_sub` |

Tàu ngầm mini và tàu tiếp tế không tính vào `VIE_var_hulls_operational` (chỉ tính thân tàu chủ lực), để Focus T6 và Trục 2 không mở sớm nhờ các loại này.

### 13.5 Cách template nối ba trục

- **Trục 1 và 1B:** chọn template và số lượng; `cost_mult` đi vào Funding Gate.
- **Trục 2:** đường nội địa đòi tier từ `unlock`; mỗi tàu bàn giao trả `exp_reward` theo `localization`.
- **Trục 3:** readiness của lực lượng liên quan chỉ đổi hiệu quả vận hành của lớp tàu (`readiness_link`), không đổi hull, module hay giá (Quy tắc 10).
- **Thêm tàu mới** là thêm một dòng vào bảng template và ánh xạ cấu hình, không thêm event.

## 14. Flag và variable của Trục 3 và hệ template

Các bảng này bổ sung cho mục 7 và dùng cùng quy ước đặt tên. Trục 3 chỉ ghi `VIE_org_*`, `VIE_path_*` và các biến readiness; nó không ghi `VIE_cap_*` hay các biến kinh nghiệm công nghiệp của Trục 2.

### 14.1 Flag tổ chức và nhánh (Trục 3)

| Flag | Đặt bởi | Khi nào | Được đọc bởi |
| --- | --- | --- | --- |
| `VIE_org_naval_training` | Focus T1 | Hoàn thành Focus | Decision của T3, T4 |
| `VIE_org_surface_command` | Decision Lực lượng mặt nước | Kết thúc | Decision Hiệp đồng hạm đội |
| `VIE_org_submarine_command` | Decision Lực lượng tàu ngầm | Kết thúc | Decision Hiệp đồng hạm đội, chương trình P4 |
| `VIE_org_first_force` | Decision cơ cấu ban đầu | Kết thúc | Hiệu ứng tổ chức |
| `VIE_path_denial`, `VIE_path_greenwater`, `VIE_path_bluewater` | Focus D1, G1, B1 | Hoàn thành Focus | Chương trình 1B, trọng số AI |

### 14.2 Biến Trục 3

| Biến | Khoảng | Cộng bởi (giá trị khởi điểm) | Đọc bởi |
| --- | --- | --- | --- |
| `VIE_var_surface_readiness` | 0–100 | Decision Lực lượng mặt nước | Template tàu mặt nước |
| `VIE_var_asw_skill` | 0–100 | Decision Mặt nước (hướng chống ngầm), Decision Hiệp đồng | Template chống ngầm |
| `VIE_var_sub_readiness` | 0–100 | Decision Lực lượng tàu ngầm | Template tàu ngầm; Kilo Event 2 (chỉ thưởng, không gate) |
| `VIE_var_fleet_organization` | 0–100 | Hiệu ứng T5 và T7, Decision Hiệp đồng, capstone; giảm tạm khi `force_priority` lệch nhánh | Template tàu tiếp tế, tàu sân bay |
| `VIE_force_priority` | 1–3 | Decision cơ cấu ban đầu (1 Coastal, 2 Balanced, 3 Extended Range) | So khớp ở T9 |
| `VIE_var_force_program_active` | 0–2 | +1 khi Decision lực lượng bắt đầu, −1 khi kết thúc; trạng thái chờ không tính | Điều kiện bắt đầu Decision lực lượng |
| `VIE_var_procurement_1b_active` | 0–2 | Program Engine của Trục 1B | Điều kiện mở chương trình 1B |
| `VIE_var_hulls_<lớp>` | ≥ 0 | +1 mỗi tàu bàn giao. Lớp: `fac`, `corvette`, `frigate`, `destroyer`, `sub`, `minisub`, `amphib`, `support`, `carrier` | Decision chương trình sau (nhóm tác chiến tàu sân bay cần carrier và khu trục) |

`VIE_var_hulls_operational` (mục 7.3) chỉ đếm thân tàu chủ lực: FAC, corvette, khinh hạm, khu trục, tàu ngầm, tàu đổ bộ và tàu sân bay. Tàu ngầm mini và tàu tiếp tế không được tính.

### 14.3 Trạng thái Decision Trục 3

Mỗi Decision có ba flag `_active`, `_done` và `_waiting`, cùng một biến `_progress` (0–100), theo mẫu ở mục 7.5.

| Decision | Tiền tố | Lựa chọn được lưu |
| --- | --- | --- |
| Lực lượng mặt nước | `VIE_dec_surface_*` | `VIE_surface_specialty` (1 hỏa lực, 2 chống ngầm), `VIE_surface_level` (1–2) |
| Lực lượng tàu ngầm | `VIE_dec_submarine_*` | `VIE_sub_orientation` (1 lịch sử, 2 sớm), `VIE_sub_level` (1–2), `VIE_sub_minisub_opt` |
| Hiệp đồng hạm đội | `VIE_dec_fleet_coord_*` | Không có (chuỗi cố định) |
| Cơ cấu lực lượng ban đầu | `VIE_dec_first_force_*` | `VIE_force_priority` |

### 14.4 Trạng thái chương trình 1B và template

Mỗi chương trình 1B có tiền tố riêng và cùng bộ flag, biến của mục 7.4.

| Mã | Tiền tố | Ghi chú |
| --- | --- | --- |
| P1 | `VIE_corvette_*` | Hộ vệ hạm nhẹ |
| P2 | `VIE_frigate_med_*` | Khinh hạm cỡ trung |
| P3 | `VIE_asw_frigate_*` | Chống ngầm cơ động |
| P4 | `VIE_ssk_reg_*` | Tàu ngầm tấn công khu vực |
| P5 | `VIE_minisub_*` | Tàu ngầm mini |
| P6 | `VIE_bastion2_*` | Bastion-P mở rộng |
| P7 | `VIE_amphib_*` | Tàu đổ bộ trực thăng và LHD |
| P8 | `VIE_destroyer_*` | Khu trục |
| P9 | `VIE_aor_*` | Tàu tiếp tế |
| P10 | `VIE_carrier_*` | Tàu sân bay hạng nhẹ |
| P11 | `VIE_ssn_*` | Tàu ngầm hạt nhân |

Mỗi tiền tố có: flag `_contracted`, `_complete`, `_cancelled`, `_suspended`; biến `_qty_ordered`, `_qty_delivered`, `_template` (mã template), `_localization` (0–2). Flag ẩn `VIE_std_<id>_unlocked` đánh dấu template đã mở.

### 14.5 Điều kiện ngoại lai bổ sung

Thêm vào bảng ở mục 7.6:

| Flag | Ý nghĩa | Chủ sở hữu đề xuất |
| --- | --- | --- |
| `VIE_ext_nuclear_tech` | Có nền công nghệ hạt nhân dân sự và năng lượng đủ cho chương trình SSN | Nhánh năng lượng hoặc công nghệ (chưa có, cần chốt) |

Kilo Event 2 đọc `VIE_var_sub_readiness` chỉ để thưởng (chi phí huấn luyện thấp hơn hoặc readiness cao hơn), không đòi Focus 13–14 kiểu bản gốc. Vì vậy vẫn giữ Quy tắc 5: deal Kilo không phụ thuộc Trục 3.

## 15. Xung đột đã xử lý, khối lượng và dữ kiện cần xác minh

Bản sửa xử lý 11 lỗi của Trục 3 gốc, giảm từ 48 Focus xuống 22 node, và để lại một nhóm dữ kiện lịch sử chưa kiểm tra. Các sửa cho mục 1–9 đã được áp dụng ở bản 2.1, và mục 10–15 theo cùng Quy tắc 6 bản sửa.

### 15.1 Lỗi ở bản gốc và cách sửa

| # | Lỗi ở bản gốc | Cách sửa | Mục |
| --- | --- | --- | --- |
| 1 | Focus cho mọi thứ; 24 Focus trước lựa chọn lớn đầu tiên | Đào tạo và tổ chức thành Decision; còn 8 Focus dùng chung trước điểm rẽ | 11 |
| 2 | Đường lịch sử không có đích sau điểm rẽ | Thêm nhánh Maritime Denial làm nhánh lịch sử | 11.5 |
| 3 | Focus muộn không có đường ra tàu | Trục 1B với Program Engine và hệ template | 12, 13 |
| 4 | Marine bắt buộc cho cả cây (đã gỡ: Hải quân đánh bộ chuyển sang nhánh Vietnam Special Force) | Gỡ Hải quân đánh bộ khỏi Trục 3; Command Reform I cần cả hai lực lượng còn lại | 11.1, 11.5 |
| 5 | Trục 3 cấp bonus sản xuất, trùng Trục 2 | Quy tắc 10; mặt tổ chức chuyển sang Decision Hiệp đồng | 10.2, 11.3 |
| 6 | Gate bằng `VIE_cap_*` làm Focus chờ Decision | Gate bằng Focus của Trục 2 và số thân tàu; capability chuyển sang Decision chương trình | 11.1, 12.2 |
| 7 | Đụng namespace `VIE_cap_*` | `VIE_org_*` và Quy tắc 11 | 10.2, 14 |
| 8 | Tàu ngầm được mô hình hóa ở hai nơi | Kilo đọc `VIE_var_sub_readiness` chỉ để thưởng | 14.5 |
| 9 | Doctrine trùng node cũ | Node cũ thành lối vào nhánh; cần đối chiếu v7 | 10.2 |
| 10 | Backbone lẫn mốc của Trục 2 (Ba Son, Molniya, TT400TP) | Backbone Trục 3 chỉ giữ mốc nhân sự và tổ chức | 11.1 |
| 11 | "Regional" trùng Greenwater | Đổi thành Extended Range; lệch nhánh thì chịu chi phí chuyển đổi | 11.4 |

### 15.2 Khối lượng nội dung

| Hạng mục | Trục 3 gốc | Bản sửa |
| --- | --- | --- |
| Focus | 48 | 22 node (12–13 mỗi lần chơi) |
| Decision | 0 | 4 Decision lực lượng, cộng 11 chương trình 1B |
| Event | – | Khoảng 12 cho 4 Decision, cộng khoảng 7 của Program Engine dùng chung |
| Template | – | 17 bản ghi (6 lịch sử và dự trữ, 11 alt-history) |

Cộng với mục 9.2, tổng cho ba trục khoảng 58 event và 26 Decision. Chương trình 1B không cần event riêng nhờ Program Engine.

### 15.3 Dữ kiện Trục 3 cần xác minh

Bản Trục 3 gốc không kèm nguồn đã kiểm tra, và tôi chưa mở lại các nguồn này. Các mốc sau dùng làm giá trị khởi điểm.

| Mục | Trong bản gốc | Ảnh hưởng | Vấn đề |
| --- | --- | --- | --- |
| Lữ đoàn 162 (2011) và 167 (2013) | Mốc tổ chức lực lượng mặt nước | T5 ≥ 2010 | Đơn vị có thể tồn tại trước và được tái tổ chức |
| Lực lượng tàu ngầm: chuẩn bị nhân lực 2008, Đoàn 189 (2010), Lữ đoàn 189 (2011), tàu đầu 2014 | Historical của Decision Tàu ngầm | T4 ≥ 2008 | Wikipedia (đoạn trích) ghi lực lượng tàu ngầm và Lữ đoàn 189 chính thức thành lập ngày 29/5/2013 tại Cam Ranh, khác mốc 2011 của bản gốc. Mốc tàu đầu đã khớp mục 8.3 |
| TT400TP: chiếc đầu 2012, chiếc thứ tư 2014 | Template dự trữ | `VIE_std_patrol_tt400` | Xưởng Hồng Hà đã xác minh (mục 8.3); mốc chiếc thứ tư chưa |
| Cơ quan quản lý đóng tàu quân sự 2005 | Mốc T1 | T1 ≥ 2005 | Cần đối chiếu |
| Cấu hình tham chiếu của Molniya, Gepard, Sigma | Mục 13.3 | Template lịch sử | Molniya và Gepard đã mở nguồn; Sigma chưa |

### 15.4 Việc tiếp theo

1. Chốt các mục còn mở ở bảng 18.1: hull của Sigma, tàu ngầm mini và SSN, tàu tiếp tế, quy ước chữ hoa của từ viết tắt.
2. Kiểm các mục ở bảng 18.2 trong repo của bạn, rồi chạy lát cắt Molniya và Decision 1 theo kế hoạch ở mục 18.3.
3. Chốt chủ sở hữu ba flag `VIE_ext_*` ở mục 7.6 và `VIE_ext_nuclear_tech`.
4. Chọn đối tác cho đường nhập khẩu của Trục 1B theo từng nhánh chính trị.
5. Làm mẫu một chương trình 1B (P1) trên Program Engine sau khi lát cắt chạy được.

## 16. Đối chiếu với Millennium Dawn

Mục này dựa trên tài liệu quy ước và mã hỗ trợ trong kho MD (AGENTS.md, Code Style Guide, oob-variants-reference, decision-reference, mio-reference, PR #4473) và trang On actions của wiki HOI4, tất cả đã mở đọc trực tiếp. Tôi chưa đọc mã trong repo của bạn, nên những gì chỉ kiểm được ở đó nằm ở mục 18.

### 16.1 Kết quả đối chiếu

| Hạng mục | Kết quả | Ảnh hưởng đến thiết kế |
| --- | --- | --- |
| Đặt tên | Flag và biến của một nước dùng tiền tố tag (`VIE_`), snake\_case; `GLOBAL_` cho trạng thái toàn cục. Code Style Guide còn ghi giữ các từ viết tắt của hệ thống ở dạng chữ hoa | Tên `VIE_*` hợp lệ. Có thể phải đổi các tên chứa mro, asw, mio sang chữ hoa khi code (cần xác nhận) |
| Flag phản chiếu trạng thái | Guide yêu cầu hỏi trạng thái có sẵn thay vì giữ flag sao chép nó; flag chỉ dành cho chuyển tiếp lịch sử hoặc trạng thái engine không trả lời được | Cắt bớt flag ở mục 7 theo mục 16.3 |
| Nhịp kiểm tra hàng tháng | `on_monthly_TAG` tồn tại và chỉ chạy khi nước còn tồn tại. MD chuộng biến thể theo tag, mọi event đều `is_triggered_only = yes`, và event theo ngày đặt qua `00_yearly_effects.txt` | Dùng `on_monthly_VIE`. Cách yearly của MD không retry được hàng tháng nên không thay thế được |
| Tạo tàu | `create_ship` cần một variant đã thiết kế cho nước tạo tàu. Thiếu thì log "equipment\_variant does not exist for the creator country", tiền bị trừ và tàu không đến (PR #4473). Công nghệ chỉ mở hull, không thiết kế hộ | Template phải gồm `create_equipment_variant` trước `create_ship` |
| Nơi định nghĩa variant | Trong `history/countries/TAG - Name.txt` (khối 2000.1.1) hoặc ngay trong event, decision, focus, scripted effect; validator kiểm tra mọi nơi. Tên `version_name` phải khớp và hull phải khớp `type` của variant | Template alt-history có thể định nghĩa khi mở chương trình |
| Module | Chỉ dùng slot của hull. Corvette có một `fixed_ship_auxillary_slot`, frigate ba, helicopter operator hai (`_2`, `_3`). Slot động cơ `fixed_ship_engine_slot` bắt buộc. Slot sai bị bỏ im lặng, và module cần tech | Trường `modules` phải dùng tên slot thật; chạy `validate_history.py --strict` và `validate_oob_units.py --strict` |
| Decision | Log là câu đầu của mỗi khối effect; `ai_will_do = { base = N }`; `allowed` chỉ đặt ở category, điều kiện động ở `available` và `visible`; mission dùng `activation`, `days_mission_timeout`, `timeout_effect`; `unlock_decision_tooltip` để báo mở khóa | Mỗi Decision CNQP cần một category có `allowed = { original_tag = VIE }` |
| MIO hải quân | Tên `TAG_organization_name`, có `allowed`. Tàu đóng ở xưởng nên `production_bonus` của MIO hải quân chỉ nhận bốn khóa: `production_capacity_factor`, `production_cost_factor`, `production_resource_need_factor`, `production_resource_penalty_factor` | Phần thưởng MIO Ba Son ở Decision 1 và 3 chỉ dùng bốn khóa này |
| Ngân sách | PR #4473 ghi chương trình hải quân của Ukraine trừ 4% ngân khố bằng `treasury_change = -0.04` | `VIE_var_naval_budget_room` phải nối vào ngân khố MD; tên effect áp dụng chưa xác minh |

### 16.2 Ánh xạ hull của MD

| Vai trò trong báo cáo | Hull MD | Ghi chú |
| --- | --- | --- |
| FAC tên lửa (Molniya), tàu tuần tra | `corvette_hull_N` (tier 1–6), có bản `stealth_corvette_hull_N` | MD liệt kê Tarantul và Pauk là corvette hoặc tàu tuần tra, nên Molniya (Tarantul-V) thuộc lớp này; tier chọn theo repo |
| Gepard 3.9 | `frigate_hull_N` (1–6) |  |
| Sigma 9814 (khoảng 2.000 t) | `corvette_hull_N` hoặc `frigate_hull_N` | Chưa quyết. MD xếp Krivak và Perry là frigate |
| Khu trục | `destroyer_hull_N` (1–5) |  |
| Tàu đổ bộ trực thăng và LHD | `helicopter_operator_hull_N` (1–4, loại carrier) | MD dùng hull này cho tàu sân bay trực thăng và LHD; LPD không có hull riêng |
| Tàu sân bay hạng nhẹ | `carrier_hull_N` (1–5) |  |
| Kilo, tàu ngầm diesel khu vực | `attack_submarine_hull_N` (1–6) | MD liệt kê Kilo ở hull này |
| SSN | `attack_submarine_hull_N` | Không có hull SSN riêng; khác biệt hạt nhân nếu có nằm ở module hoặc tech, chưa xác minh |
| Tàu ngầm mini | Không có hull riêng | Cần quyết: dùng `attack_submarine_hull_1` với module tối thiểu, hoặc bỏ P5 khỏi bản đầu |
| Tàu tiếp tế | `support_ship_1`, `support_ship_2`, `repair_ship_1` | Không có module, dùng dạng `upgrades`. Hull mở bằng tech `tech_landing_craft_*`. Tàu tiếp tế hạm đội có thể là support ship, chưa xác minh |

### 16.3 Ba điều chỉnh thiết kế rút ra

1. **Template là cặp `create_equipment_variant` và `create_ship`.** Trường `hull` ở mục 13.1 nay điền theo bảng 16.2, và mỗi template phải gắn tech của hull và module.
2. **Bỏ biến tiến độ và flag phản chiếu.** Mốc 40% và mốc kết thúc của Decision 1 dùng event hẹn giờ thay cho `VIE_dec_*_progress`. Trạng thái lấy từ trạng thái có sẵn: `has_completed_focus` thay `VIE_org_naval_training`, `qty_delivered = qty_ordered` thay `_complete`, mission đang chạy thay `VIE_dec_*_active`. Giữ flag cho các chuyển tiếp: `_contracted`, `_missed`, `_cancelled`, `_suspended`, `_offered`.
3. **Thêm flag `_offered` cho event hỏi.** Event mở chương trình chỉ được bắn một lần khi cổng mở; nếu không có flag này, xung hàng tháng sẽ bắn lại mỗi tháng đến khi người chơi chọn.

## 17. Script mẫu cho lát cắt Molniya và Decision 1

Đây là khung script theo phong cách MD (tab, log ở đầu khối effect, `is_triggered_only`, `ai_will_do` dùng `base`), chưa chạy thử trong game. Dòng có `TODO(MD)` là chỗ chỉ kiểm được trong repo của bạn (mục 18). Flag đã cắt theo mục 16.3.

### 17.1 On action và xung hàng tháng

File `common/on_actions/VIE_naval_on_actions.txt`:

```text
on_actions = {
	on_monthly_VIE = {
		effect = {
			VIE_naval_monthly_pulse = yes
		}
	}
}
```

### 17.2 Scripted effect: xung kiểm tra

File `common/scripted_effects/VIE_naval_scripted_effects.txt`. Cổng chỉ gồm đối tác tồn tại và không chiến tranh; pha 2 thêm cờ xưởng (ngoại lệ có tên ở mục 3.1). Cờ `_offered` chặn việc bắn lại event.

```text
VIE_naval_monthly_pulse = {
	# Molniya pha 1: cửa sổ 2003-06 -> 2005-12
	if = {
		limit = {
			date > 2003.5.31
			date < 2006.1.1
			NOT = { has_country_flag = VIE_molniya_p1_offered }
			country_exists = SOV # TODO(MD): tag của Nga
			NOT = { has_war_with = SOV }
		}
		country_event = { id = VIE_naval.1 }
	}
	else_if = {
		limit = {
			date > 2005.12.31
			NOT = { has_country_flag = VIE_molniya_p1_offered }
			NOT = { has_country_flag = VIE_molniya_p1_missed }
		}
		set_country_flag = VIE_molniya_p1_missed
	}

	# Giao hàng pha 1: sàn ngày tuyệt đối (2007 và 2008)
	if = {
		limit = {
			has_country_flag = VIE_molniya_contracted
			date > 2007.1.31
			check_variable = { VIE_molniya_ru_delivered < 1 }
			check_variable = { VIE_molniya_ru_qty > 0 }
		}
		country_event = { id = VIE_naval.2 }
	}
	if = {
		limit = {
			has_country_flag = VIE_molniya_contracted
			date > 2008.1.31
			check_variable = { VIE_molniya_ru_delivered > 0 }
			check_variable = { VIE_molniya_ru_delivered < 2 }
			check_variable = { VIE_molniya_ru_qty > 1 }
		}
		country_event = { id = VIE_naval.2 }
	}

	# Molniya pha 2: cửa sổ 2009-06 -> 2012-12, cần xưởng Ba Son
	if = {
		limit = {
			date > 2009.5.31
			date < 2013.1.1
			has_country_flag = VIE_cap_ba_son_yard
			NOT = { has_country_flag = VIE_molniya_p2_offered }
			NOT = { has_war_with = SOV }
		}
		country_event = { id = VIE_naval.3 }
	}
	else_if = {
		limit = {
			date > 2012.12.31
			NOT = { has_country_flag = VIE_molniya_p2_offered }
			NOT = { has_country_flag = VIE_molniya_p2_missed }
		}
		set_country_flag = VIE_molniya_p2_missed
	}
}
```

Số tàu lớn hơn hai và quy tắc giao hàng chung thuộc Program Engine, chưa viết ở lát cắt này.

### 17.3 Event Molniya pha 1 và giao hàng

File `events/VIE_naval.txt`. Event .3 (pha 2) cùng dạng với .1 với ba mức 2 + 6, 2 + 8, 2 + 10 và chưa viết ở đây.

```text
add_namespace = VIE_naval

country_event = {
	id = VIE_naval.1
	title = VIE_naval.1.t
	desc = VIE_naval.1.d
	picture = GFX_report_event_generic_read_write # TODO(MD)
	is_triggered_only = yes

	immediate = {
		set_country_flag = VIE_molniya_p1_offered
	}

	option = { # Historical: 2 tàu
		name = VIE_naval.1.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.1.a executed"
		set_country_flag = VIE_molniya_contracted
		set_variable = { VIE_molniya_ru_qty = 2 }
		set_variable = { VIE_molniya_ru_delivered = 0 }
		# TODO(MD): thanh toán qua ngân khố (PR #4473 dùng treasury_change)
		ai_chance = { base = 100 }
	}
	option = { # Alt-history: 4 tàu
		name = VIE_naval.1.b
		log = "[GetDateText]: [This.GetName]: VIE_naval.1.b executed"
		set_country_flag = VIE_molniya_contracted
		set_variable = { VIE_molniya_ru_qty = 4 }
		set_variable = { VIE_molniya_ru_delivered = 0 }
		ai_chance = { base = 0 }
	}
	option = { # Bỏ qua pha 1
		name = VIE_naval.1.c
		set_country_flag = VIE_molniya_p1_skipped
		ai_chance = { base = 0 }
	}
}

country_event = {
	id = VIE_naval.2
	title = VIE_naval.2.t
	desc = VIE_naval.2.d
	picture = GFX_report_event_generic_read_write # TODO(MD)
	is_triggered_only = yes

	option = {
		name = VIE_naval.2.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.2.a executed"
		create_ship = {
			type = corvette_hull_2 # TODO(MD): tier khớp variant và tech
			equipment_variant = "Molniya Class"
			creator = VIE
			name = "HQ-375" # TODO(MD): danh sách tên
		}
		add_to_variable = { VIE_molniya_ru_delivered = 1 }
		add_to_variable = { VIE_var_hulls_operational = 1 }
		add_to_variable = { VIE_var_hulls_corvette = 1 }
		ai_chance = { base = 1 }
	}
}
```

### 17.4 Định nghĩa variant (template Molniya)

Trong `history/countries/VIE - Vietnam.txt`, khối 2000.1.1, đặt trong nhánh DLC Man the Guns nếu repo của bạn gate như vậy. Tên và tier hull lấy từ `MD_mtg_ships.txt`; tên slot và module phải là của hull đó, nếu không MD bỏ chúng im lặng.

```text
create_equipment_variant = {
	name = "Molniya Class"
	type = corvette_hull_2 # TODO(MD): tier của Tarantul-V, phải khớp create_ship
	parent_version = 0
	modules = {
		fixed_ship_engine_slot = TODO # TODO(MD): bắt buộc, kiểm tra tech
		fixed_ship_auxillary_slot = TODO # TODO(MD): corvette chỉ có một slot phụ
		# TODO(MD): các slot vũ khí: 16 tên lửa Uran-E, pháo AK-176M, hai hệ AK-630
	}
}
```

### 17.5 Decision 1: Ba Son

Category trong `common/decisions/categories/`, decision trong `common/decisions/`. `allowed` chỉ đặt ở category (quy ước MD).

```text
VIE_naval_industry_category = {
	icon = generic_decision # TODO(MD)
	allowed = { original_tag = VIE }
	visible = { has_completed_focus = VIE_ba_son_shipyards }
}

VIE_naval_industry_category = {
	VIE_ba_son_development = {
		icon = generic_decision # TODO(MD)
		fire_only_once = yes
		visible = { has_completed_focus = VIE_ba_son_shipyards }
		available = { has_completed_focus = VIE_ba_son_shipyards }

		complete_effect = {
			log = "[GetDateText]: [Root.GetName]: Decision VIE_ba_son_development"
			country_event = { id = VIE_naval.10 }
		}

		ai_will_do = { base = 10 }
	}
}
```

Bốn event của Decision 1, dùng event hẹn giờ thay biến tiến độ. Số ngày tương ứng 12, 18 và 24 tháng, mốc 40% là 146, 219 và 292 ngày:

```text
country_event = { # .10 định hướng
	id = VIE_naval.10
	title = VIE_naval.10.t
	desc = VIE_naval.10.d
	is_triggered_only = yes

	option = { # Shipbuilding trước
		name = VIE_naval.10.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.10.a executed"
		set_variable = { VIE_ba_son_orientation = 1 }
		add_to_variable = { VIE_var_shipbuilding_exp = 12 }
		country_event = { id = VIE_naval.11 }
		ai_chance = { base = 1 }
	}
	option = { # MRO trước
		name = VIE_naval.10.b
		log = "[GetDateText]: [This.GetName]: VIE_naval.10.b executed"
		set_variable = { VIE_ba_son_orientation = 2 }
		add_to_variable = { VIE_var_mro_exp = 12 }
		country_event = { id = VIE_naval.11 }
		ai_chance = { base = 0 }
	}
	option = { # Cân bằng
		name = VIE_naval.10.c
		log = "[GetDateText]: [This.GetName]: VIE_naval.10.c executed"
		set_variable = { VIE_ba_son_orientation = 3 }
		add_to_variable = { VIE_var_shipbuilding_exp = 6 }
		add_to_variable = { VIE_var_mro_exp = 6 }
		country_event = { id = VIE_naval.11 }
		ai_chance = { base = 0 }
	}
}

country_event = { # .11 mức đầu tư
	id = VIE_naval.11
	title = VIE_naval.11.t
	desc = VIE_naval.11.d
	is_triggered_only = yes

	option = { # Cơ bản
		name = VIE_naval.11.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.11.a executed"
		set_variable = { VIE_ba_son_invest = 1 }
		# TODO(MD): chi phí x1,0 qua ngân khố
		country_event = { id = VIE_naval.12 days = 146 }
		country_event = { id = VIE_naval.13 days = 365 }
		ai_chance = { base = 1 }
	}
	option = { # Mở rộng
		name = VIE_naval.11.b
		log = "[GetDateText]: [This.GetName]: VIE_naval.11.b executed"
		set_variable = { VIE_ba_son_invest = 2 }
		country_event = { id = VIE_naval.12 days = 219 }
		country_event = { id = VIE_naval.13 days = 548 }
		ai_chance = { base = 0 }
	}
	option = { # Trọng điểm
		name = VIE_naval.11.c
		log = "[GetDateText]: [This.GetName]: VIE_naval.11.c executed"
		set_variable = { VIE_ba_son_invest = 3 }
		country_event = { id = VIE_naval.12 days = 292 }
		country_event = { id = VIE_naval.13 days = 730 }
		ai_chance = { base = 0 }
	}
}

country_event = { # .12 mốc 40%: xưởng dùng được
	id = VIE_naval.12
	title = VIE_naval.12.t
	desc = VIE_naval.12.d
	is_triggered_only = yes

	option = {
		name = VIE_naval.12.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.12.a executed"
		set_country_flag = VIE_cap_ba_son_yard
		ai_chance = { base = 1 }
	}
}

country_event = { # .13 kết thúc
	id = VIE_naval.13
	title = VIE_naval.13.t
	desc = VIE_naval.13.d
	is_triggered_only = yes

	option = {
		name = VIE_naval.13.a
		log = "[GetDateText]: [This.GetName]: VIE_naval.13.a executed"
		set_country_flag = VIE_cap_ba_son_complete
		set_variable = { VIE_var_ba_son_tier = VIE_ba_son_invest }
		# TODO(MD): cộng exp theo mức (+5, +10, +15) và thưởng MIO Ba Son
		# (chỉ dùng production_capacity_factor, production_cost_factor,
		# production_resource_need_factor, production_resource_penalty_factor)
		ai_chance = { base = 1 }
	}
}
```

Cần thêm khóa localisation (`VIE_naval.*.t`, `.d`, `.a`...) vào file `.yml` tiếng Anh của MD (UTF-8 có BOM); tôi chưa viết phần này.

## 18. Rà soát nhất quán và việc cần kiểm trong repo

Đã rà lại toàn bộ 17 mục sau các bản 2.1 đến 2.4. Bảng 18.1 liệt kê vấn đề và cách xử lý; các sửa nhỏ đã áp dụng thẳng vào báo cáo, phần còn lại ghi là còn mở.

### 18.1 Kết quả rà nhất quán

| # | Vấn đề | Vị trí | Xử lý | Trạng thái |
| --- | --- | --- | --- | --- |
| 1 | `VIE_var_ext_support` khai báo 0–3 nhưng mục 14.5 thêm flag thứ tư `VIE_ext_nuclear_tech` | 7.3, 14.5 | `ext_support` chỉ đếm ba flag hải quân | Đã sửa |
| 2 | Quy tắc 6 nằm ở cả mục 2 và mục 10.2, mục 10.2 vẫn ghi "thay thế bản cũ" | 2, 10.2 | Mục 10.2 nhắc lại và trỏ về mục 2 | Đã sửa |
| 3 | Trường `hull` của template ghi "điền khi code" | 13.1 | Điền theo bảng 16.2 | Đã sửa |
| 4 | Bảng flag ở mục 7 còn nhiều flag phản chiếu trạng thái và biến `_progress`, trái quy ước MD | 7.2–7.5, 14.3 | Ghi chú đầu mục 7 trỏ tới mục 16.3; dọn khi code | Đã ghi chú |
| 5 | Flag chuyển tiếp `_offered` và `_skipped` chưa có trong bảng trạng thái | 7.4 | Ghi ở ghi chú đầu mục 7 | Đã ghi chú |
| 6 | Bước 1 của mục 9.4 vẫn nói khai báo toàn bộ flag | 9.4 | Sửa thành biến và flag chuyển tiếp | Đã sửa |
| 7 | Phần thưởng MIO hải quân có thể dùng khóa production không hợp lệ | 5.2, 5.4 | Chỉ bốn khóa hợp lệ (mục 16.1) | Đã ghi |
| 8 | Decision CNQP cần category mà báo cáo chưa nêu | 5, 7.5 | Category và Decision 1 ở mục 17.5; nhân bản cho Decision 2–5 | Đã xử lý cho Decision 1 |
| 9 | `on_monthly_VIE` khác cách yearly của MD cho event theo ngày | 3.1, 17.1 | Giữ monthly vì cần retry; ghi rõ là ngoại lệ có chủ ý | Đã xử lý |
| 10 | Sigma xếp là corvette ở 13.3 nhưng hull MD chưa quyết | 13.3, 16.2 | Quyết khi chọn hull | Còn mở |
| 11 | Tàu ngầm mini và SSN không có hull riêng trong MD | 13.4, 16.2 | Quyết ở P5 và P11 | Còn mở |
| 12 | Tàu tiếp tế P9 dùng hull `support_ship_*` không có module | 13.4, 16.2 | Template P9 dùng dạng `upgrades` | Còn mở |
| 13 | Tên có từ viết tắt (mro, asw, mio) khác quy ước chữ hoa của Code Style Guide | Toàn báo cáo | Chưa đổi; chốt trước khi code hàng loạt | Còn mở |

### 18.2 Việc cần kiểm trong repo của bạn

| Việc | Nơi kiểm | Kết quả cần có |
| --- | --- | --- |
| Variant hiện có và cách gate DLC | `history/countries/VIE - Vietnam.txt` | Có khối 2000.1.1, biết tên variant tàu hiện hữu và cách gate Man the Guns |
| Tarantul trong OOB 2000 | `history/units/VIE_2000_naval_mtg.txt` | Hull tier và `version_name` để chọn tier cho Molniya |
| Tier và slot của corvette | `common/units/equipment/MD_mtg_ships.txt` | `corvette_hull_N`: tier, tech mở, danh sách slot |
| Tech của hull và module | `common/technologies/` | Tech nào mở module; thêm vào `set_technology` của VIE |
| On action hiện có | `common/on_actions/` | Chưa có `on_monthly_VIE` trùng; nếu có thì gộp |
| Effect ngân khố | `common/scripted_effects/` | Tên effect trừ ngân khố (PR #4473 dùng `treasury_change`) |
| Tag của Nga | Thư mục tag và history | Tag dùng cho điều kiện đối tác |
| MIO Ba Son ở v7 | Thư mục MIO | ID hiện có và có theo quy ước `VIE_organization_name` không |
| Lỗi `create_ship` | Log khi chạy | Không có dòng "equipment\_variant does not exist" |
| Validator (nếu repo là bản fork MD) | `tools/validation/` | `validate_history.py --strict`, `validate_oob_units.py --strict`, `validate_decisions.py`, `validate_mios.py` sạch |

### 18.3 Kế hoạch thử trong game

1. Chạy VIE đến 2003-06: event `VIE_naval.1` xuất hiện đúng một lần (nhờ `_offered`).
2. Chọn 2 tàu: hai tàu đến từ 2007-02 và 2008-02, `VIE_var_hulls_operational` bằng 2, log không có lỗi `create_ship`.
3. Hoàn thành Focus 1 và 2, bấm Decision 1 và chọn Cơ bản: cờ xưởng đặt sau khoảng 146 ngày, `VIE_var_ba_son_tier` bằng 1 sau 365 ngày.
4. Cho VIE chiến tranh với Nga trong cửa sổ pha 1: `VIE_molniya_p1_missed` được đặt sau 2005-12. Đường mở lại bằng Decision `molniya_late` chưa viết trong lát cắt.
5. Chạy AI-only đến 2010: AI VIE có Molniya và Ba Son.
