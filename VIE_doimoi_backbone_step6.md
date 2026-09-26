# Bước 6: Ánh xạ khung xây dựng nhà nước vào "Đổi Mới tiếp tục"

> Tiếp theo STEP 1–5. **Chưa** vẽ transition graph cuối (STEP 8), **chưa** lên kế hoạch code (STEP 9).
> Bảng ánh xạ đầy đủ nằm ở **`D:\HOI4Mods\_gen\axis_map.py`** — file dữ liệu máy đọc được, không phải văn xuôi.
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TIỀN ĐỀ KỊCH BẢN]** · **[TRỪU TƯỢNG GAMEPLAY]**

---

## 0. Kết quả bước này trong một đoạn

Tôi đã gán hiệu ứng trục cho **167 trên 197 focus thân lịch sử (85%)**, rồi chạy thử: nếu người chơi đi hết thân lịch sử, cấu hình nhà nước thu được **tái tạo đúng hồ sơ của Việt Nam thật ở từng giai đoạn** — kể cả những chỗ phản trực giác như thị trường **thụt lùi** giai đoạn 2007–2010 và phân cấp **âm** giai đoạn 2021–2026. Mô hình không được tinh chỉnh để ra kết quả đó; nó ra như vậy vì bản thân các focus đã đúng lịch sử.

Nhưng phép thử cũng phơi ra một vấn đề thật: **bốn trên bảy trục không phải là lựa chọn** trong thân lịch sử — chúng chỉ có một chiều đi. Mục 6 và 7 xử lý chuyện đó.

---

## 1. Đổi Mới: từ một focus thành xương sống

**[SỰ KIỆN]** Hiện nay `VIE_doi_moi_continues` là một focus gốc ở (27, 0), phần thưởng là một idea, và **không có vai trò cơ chế nào sau đó**. 486 focus còn lại không đọc nó.

**[TIỀN ĐỀ KỊCH BẢN]** Trong thiết kế này nó đảm nhận ba việc:

1. **Khởi tạo** bảy trục bằng giá trị Việt Nam năm 2000 và gắn `VIE_state_modifier`
2. **Là điểm đọc**: mọi capstone (`era_of_rising`, `party_centennial_2030`, `developed_nation_2045`) và mọi cửa rẽ chế độ đọc cấu hình trục thay vì đọc cờ
3. **Là khung kể chuyện**: năm giai đoạn ở mục 3 cho người chơi biết mình đang ở đâu trong quá trình

Quan trọng: **không thêm focus mới nào** cho việc này. Đổi Mới thành xương sống bằng cách các focus lịch sử sẵn có bắt đầu đẩy trục.

---

## 2. Việt Nam năm 2000: giá trị khởi đầu của bảy trục

**[SỰ KIỆN] + [HỌC THUẬT]** Mỗi giá trị đều có căn cứ, không phải đoán:

| Trục | Khởi đầu | Căn cứ |
|---|---|---|
| **size** quy mô bộ máy | **+3** | MD đặt VIE ở `bureau_03` trên thang 1–5. Khu vực công 7,9% lực lượng lao động, thuộc nhóm lớn nhất Đông Nam Á (ISEAS 2025/14) |
| **merit** chất lượng bộ máy | **−2** | MD đặt VIE ở `corruption_level_08` trên thang 1–10. Hệ cán bộ vận hành bằng bảo trợ, chưa có thi tuyển cạnh tranh diện rộng |
| **decent** phân cấp | **+1** | Các tỉnh Việt Nam có quyền tự quyết trên thực tế cao bất thường — PCI ra đời năm 2005 chính vì 63 tỉnh quản trị rất khác nhau (Malesky) |
| **checks** ràng buộc quyền lực | **−2** | Quốc hội tồn tại và đang dần chất vấn mạnh hơn, nhưng không có tư pháp độc lập. V-Dem: **closed autocracy** |
| **market** nhà nước ↔ thị trường | **−2** | Năm 2000 DNNN chiếm ưu thế, Luật Doanh nghiệp vừa có hiệu lực, khu vực tư nhân chính thức còn rất nhỏ |
| **civil** cưỡng chế ↔ dân sự | **−3** | MD đặt VIE ở `police_05`, **mức cao nhất**. Không có báo chí độc lập |
| **integ** hội nhập | **0** | Đã vào ASEAN 1995 và bình thường hóa với Mỹ 1995, nhưng chưa có BTA, chưa vào WTO |

---

## 3. Năm giai đoạn của Đổi Mới và hồ sơ trục

**[SỰ KIỆN]** Chia theo mốc có thật, rồi cộng hiệu ứng trục của các focus bị khóa theo năm trong từng khoảng. **Không tinh chỉnh gì** — đây là kết quả thô:

| Giai đoạn | Focus | Trục chuyển mạnh nhất | Có khớp lịch sử không |
|---|---|---|---|
| **1. 2000–2006** Hội nhập và luật chơi thị trường | 82 | `integ +38`, `merit +33`, `decent +11`, `market +9` | **Khớp.** BTA 2001, Luật Doanh nghiệp, Luật Đầu tư chung 2005, Luật PCTN 2005, PAR 2001–2010, chuẩn bị WTO |
| **2. 2007–2010** Vào WTO rồi vấp | 14 | `integ +7`, `merit +4`, **`market −2`** | **Khớp, và đây là chỗ đáng chú ý.** Trục thị trường **đi lùi** — đúng với thời kỳ tập đoàn kinh tế nhà nước, Vinashin, và lạm phát 2008 |
| **3. 2011–2015** Tái cơ cấu và HD-981 | 13 | `integ +9`, **`checks +4`**, `civil +1` | **Khớp.** Hiến pháp 2013, Luật Biển 2012, tái cơ cấu ba trọng tâm |
| **4. 2016–2020** Đốt lò và thắt chặt | 19 | `merit +7`, **`civil −6`**, `west +5` | **Khớp.** Chống tham nhũng mạnh lên **đồng thời** Luật An ninh mạng 2018 và Lực lượng 47 siết không gian mạng. Hai chiều ngược nhau cùng lúc |
| **5. 2021–2026** Tinh gọn và Kỷ nguyên vươn mình | 26 | `integ +13`, **`decent −7`**, `market +6`, **`size −5`** | **Khớp.** Sáp nhập tỉnh, bỏ cấp huyện, hợp nhất bộ — vừa thu nhỏ bộ máy vừa **tập trung** quyền lực. Nghị quyết 68 đẩy thị trường |

**[HỌC THUẬT]** Ba chỗ mô hình nói đúng điều mà một thiết kế "chọn ý thức hệ" sẽ bỏ sót:

- **Giai đoạn 2, thị trường đi lùi.** Hội nhập và tự do hóa **không** đi cùng nhau. Vào WTO xong, Việt Nam lập tập đoàn kinh tế nhà nước. Đây là ca ràng buộc ngân sách mềm của Kornai, xảy ra thật.
- **Giai đoạn 4, hai chiều ngược nhau.** Chất lượng bộ máy tăng **cùng lúc** quyền dân sự giảm. Chống tham nhũng và siết kiểm soát là hai mặt của cùng một chiến dịch, không phải hai lựa chọn loại trừ.
- **Giai đoạn 5, tinh gọn là tập trung.** Bộ máy nhỏ đi nhưng quyền lực **tập trung hơn**, không phân tán hơn. `size` và `decent` cùng âm.

---

## 4. Bảng ánh xạ

**[SỰ KIỆN]** File `D:\HOI4Mods\_gen\axis_map.py`. Đã kiểm: **mọi ID đều tồn tại trong mod**, không có ID sai.

| | |
|---|---|
| Focus thân lịch sử | 197 |
| Đã gán hiệu ứng trục | **167 (85%)** |
| Chưa gán | 30 |

**30 focus chưa gán** là các focus thuần kết quả, không phải lựa chọn thể chế: mốc thu nhập (`upper_middle_income`, `high_income_2045`), môi trường (`forest_protection`, `plastic_waste`), văn hóa thể thao (`sea_games_bid`, `heritage_preservation`), vệ tinh và chip (`vinasat`, `chip_design`). **[TIỀN ĐỀ KỊCH BẢN]** Để trống là đúng — không phải focus nào cũng phải đẩy trục, nếu không mô hình thành nhiễu.

**Quy tắc gán đã dùng:**

1. **Biên độ 1 / 2 / 3** — nhỏ, vừa, lớn. Không có 4 trở lên.
2. **Một focus tối đa 3 trục.** Nếu phải gán 4 thì focus đó mơ hồ, nên xem lại.
3. **Capstone đọc trục, không đẩy trục** — trừ `era_of_rising`, xem dưới.
4. **Cùng một cải cách có thể đẩy hai trục ngược nhau.** `two_tier_local_gov`: `size −2` và `decent −1`. Bỏ cấp huyện làm xã mạnh hơn nhưng giảm số đầu mối trung gian.
5. **Hiệu ứng theo bản chất thể chế, không theo tên.** `VIE_party_inspection` (Ủy ban Kiểm tra TƯ) cho `merit +1` nhưng `checks −1`: đó là trách nhiệm giải trình **dọc** trong Đảng, không phải kiểm soát **ngang** theo nghĩa O'Donnell.

**Một ngoại lệ có chủ ý:** `era_of_rising` được gán `checks −2, size −1` dù là capstone. **[SỰ KIỆN]** Căn cứ là ISEAS 2026/29: hợp nhất Tổng Bí thư và Chủ tịch nước đưa mô hình lãnh đạo sang dạng "hạt nhân", và tác giả cảnh báo hệ thống yếu kiểm soát ngang khó xử lý đánh đổi và khó tiếp thu phản hồi. Capstone của giai đoạn 5 phải phản ánh điều đó, nếu không mô hình sẽ nói dối về thời kỳ hiện tại.

---

## 5. Kiểm chứng: đi hết thân lịch sử thì ra nhà nước nào

**[SỰ KIỆN]** Cộng tất cả, bỏ các lựa chọn loại trừ nhau:

| Trục | Tổng thô | Trần dương | Trần âm | Chuẩn hóa −10…+10 |
|---|---|---|---|---|
| size | −3 | +6 | −12 | **+2** (nhỏ hơn một chút) |
| merit | +48 | +50 | 0 | **+10** (kịch trần) |
| decent | +6 | +15 | −10 | **+4** |
| checks | +6 | +16 | −8 | **+4** |
| market | +17 | +38 | −19 | **+4** |
| civil | −12 | +2 | −11 | **−11** (kịch trần âm) |
| integ | +75 | +77 | −2 | **+10** (kịch trần) |
| west | +22 | +22 | 0 | **+10** |
| mob | +4 | +4 | 0 | +10 |

**[HỌC THUẬT] Đối chiếu với Việt Nam thật 2026:**

| Trục | Mô hình nói | Thực tế | |
|---|---|---|---|
| integ kịch trần | Hội nhập tối đa | Thương mại trên GDP thuộc nhóm cao nhất thế giới; 17 FTA | ✅ |
| civil kịch trần âm | Cưỡng chế rất mạnh | V-Dem closed autocracy; `police_05` | ✅ |
| market chỉ +4 | Vẫn nhiều nhà nước | Kinh tế nhà nước vẫn giữ vai trò chủ đạo theo Hiến pháp | ✅ |
| size +2 | Bộ máy thu nhỏ nhẹ | Đang giảm 20% biên chế nhưng vẫn 7,9% lực lượng lao động | ✅ |
| checks +4 | Ràng buộc tăng nhẹ | Quốc hội mạnh hơn 2000, nhưng 2026 đi lùi | ✅ hợp lý |
| **merit kịch trần** | Bộ máy chất lượng cao | `corruption_level` thực tế **vẫn cao**; PAPI cải thiện chậm | ❌ **Mô hình nói quá** |

**[TIỀN ĐỀ KỊCH BẢN] Chỗ sai duy nhất, và cách sửa:** trục `merit` quá dễ lên vì có **25 focus** cùng đẩy nó lên và **không focus nào** kéo xuống. Sửa không phải bằng cách giảm con số, mà bằng cách gắn **cái giá của Geddes**: mỗi lần `merit` tăng thì mất một ít opinion của `communist_cadres` và một ít ổn định. Cải cách công vụ tước đi nguồn lực mua liên minh — đó là lý thuyết, và nó biến trục một chiều thành trục có đánh đổi.

---

## 6. Vấn đề thật: trục nào là lựa chọn, trục nào không

**[SỰ KIỆN]** Đây là phát hiện quan trọng nhất của bước 6.

| Trục | Số focus đẩy lên | Số focus kéo xuống | Có phải lựa chọn không |
|---|---|---|---|
| **market** | nhiều | nhiều (`state_conglomerates −3`, `petrovietnam −2`…) | **Có** — trục tốt nhất |
| **decent** | 15 điểm | 10 điểm | **Có** |
| **checks** | 16 điểm | 8 điểm | **Có** |
| **size** | 6 điểm | 12 điểm | **Có**, lệch một chiều |
| **civil** | chỉ 2 điểm | 11 điểm | **Gần như không** |
| **merit** | 50 điểm | **0** | **Không** |
| **integ** | 77 điểm | chỉ 2 điểm | **Không** |

Ba trục cuối chỉ có một chiều đi. **[HỌC THUẬT]** Và điều đó **đúng về mặt lịch sử** — Việt Nam 2000–2026 thực sự chỉ đi một chiều trên cả ba: hội nhập ngày càng sâu, chống tham nhũng ngày càng mạnh, kiểm soát không gian mạng ngày càng chặt. Nếu cho người chơi "chọn không hội nhập" trong thân lịch sử thì đó không còn là lịch sử.

**Vậy vấn đề không phải mô hình sai, mà là: lựa chọn không nằm ở thân lịch sử.**

---

## 7. Bốn cách tạo lựa chọn thật mà không phá lịch sử

**[TIỀN ĐỀ KỊCH BẢN]**

### 7.1 Khan hiếm thời gian — đã có sẵn, chưa được dùng

**[SỰ KIỆN]** Toàn bộ nội dung lịch sử tốn **45 năm** thời gian focus, và một ván 2000–2045 có đúng **45 năm**. Người chơi **không thể lấy hết**. Mỗi focus lịch sử bỏ qua là một điểm trục không được cộng.

Đây là cơ chế lựa chọn **mạnh nhất và đã tồn tại**, nhưng hiện vô hình. Chỉ cần làm cho nó **nhìn thấy được**: hiển thị cấu hình trục để người chơi biết mình đang đánh đổi cái gì khi bỏ qua một nhánh.

### 7.2 Giá của mỗi bước — biến trục một chiều thành trục có giá

Ba trục một chiều đều có cái giá trong literature:

| Trục | Cái giá | Nguồn |
|---|---|---|
| `merit` | Mất công cụ bảo trợ → giảm opinion `communist_cadres`, giảm ổn định | Geddes (1994) *Politician's Dilemma* |
| `integ` | Tăng phụ thuộc bên ngoài, dễ tổn thương trước cú sốc; và **linkage tạo áp lực thể chế** | Kuik (2008); Levitsky & Way (2010) |
| `civil` âm | Bộ máy cưỡng chế mạnh lên thì **tự nó thành mối đe dọa**; và giảm khả năng tiếp thu phản hồi | Greitens (2016); ISEAS 2026/29 |

Không cần đổi hướng, chỉ cần **mỗi điểm trục đều có hóa đơn**.

### 7.3 Sáu cặp loại trừ đã có, giữ nguyên

**[SỰ KIỆN]** Thân lịch sử đã có 6 focus loại trừ nhau: xây ↔ gác điện hạt nhân, pháp lý biển ↔ khẳng định chủ quyền, ngả Trung Quốc ↔ ngả phương Tây. Cả ba cặp đều gắn với **điểm quyết định có thật** — đúng nguyên tắc của plan v6. **Không thêm cặp loại trừ mới vào thân lịch sử**, vì làm vậy sẽ bịa ra ngã rẽ không có thật.

### 7.4 Quyết định lặp lại — chỗ duy nhất nên thêm cơ chế mới

**[SỰ KIỆN]** Mod đã có `VIE_military_readiness_category` với 6 quyết định lặp lại, có `days_re_enable` và chi phí PP/ngân khố. Mẫu này chạy được.

**[TIỀN ĐỀ KỊCH BẢN]** Một danh mục song song — tạm gọi "Xây dựng nhà nước" — cho phép người chơi **chủ động đẩy một trục** ngoài dòng lịch sử, với chi phí thật và thời gian chờ. Ví dụ về dạng thức, chưa phải danh sách cuối:

- Đợt thi tuyển công chức cạnh tranh: `merit +1`, tốn PP, giảm opinion cán bộ
- Giao quyền cho tỉnh thí điểm: `decent +1`, tăng chênh lệch vùng
- Nâng mức luật bộ máy: đổi `bureau_law`, tốn ngân sách thường xuyên
- Nới kiểm soát nội dung: `civil +1`, giảm ổn định ngắn hạn

Đây là chỗ **nên** thêm cơ chế, vì nó cho lựa chọn mà không đụng vào tính lịch sử của cây.

---

## 8. Chuẩn hóa và hiển thị

**[TRỪU TƯỢNG GAMEPLAY]**

- **Chuẩn hóa:** giá trị hiển thị = `round(10 × tổng / trần cùng dấu)`, cho mọi trục nằm trong −10…+10 và so sánh được với nhau. Biến thô vẫn lưu nguyên để tính điều kiện.
- **Hiển thị:** một mục trong danh sách modifier quốc gia, đúng như `VIE_armed_forces_modifier` đang làm. Bảy dòng, mỗi dòng một trục, kèm tên hai cực.
- **Không** làm GUI riêng, **không** thêm power balance (MD tối đa 3, VIE đã dùng hết 3).

---

## 9. Việc chưa làm và chỗ cần kiểm chứng

1. **Chưa gán trục cho dải chế độ (159 focus).** Đó là STEP 7.
2. **Chưa gán trục cho nhánh quân sự (133 focus).** Theo nguyên tắc mục XIII của bạn, quân sự nối vào `decent` (dân quân), `market` (công nghiệp quốc phòng), `integ` (nội địa hóa) — nhưng chưa làm.
3. **Ngưỡng cho điều kiện mở nhánh chưa có số.** Cần chốt ở STEP 8.
4. **Chưa kiểm `merit` sau khi thêm cái giá của Geddes** — phải chạy lại mô phỏng.
5. **30 focus chưa gán** cần rà lại một lượt xem có cái nào thực sự nên có trục không.
6. **Chưa thử đổi `bureau_law` bằng focus trong game** — nợ từ STEP 5, và nó chặn mục 7.4.

---

## Nguồn mới dùng ở bước này

Geddes (1994) *Politician's Dilemma*; Kornai (1986) "The Soft Budget Constraint"; O'Donnell (1998) về trách nhiệm giải trình ngang; Greitens (2016); Kuik (2008); Levitsky & Way (2010).

Dữ liệu Việt Nam: [ISEAS Perspective 2025/14](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/) · [ISEAS Perspective 2026/29](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2026-29-vietnams-reconfigured-leadership-personnel-and-power-in-the-new-era-by-nguyen-khac-giang/) · [PAPI](https://papi.org.vn/eng/) · [Chỉ số quản trị – Malesky, Duke](https://sites.duke.edu/malesky/governance-indices/) · [V-Dem Democracy Report 2025](https://v-dem.net/documents/54/v-dem_dr_2025_lowres_v1.pdf).

Dữ liệu mod: `D:\HOI4Mods\_gen\axis_map.py` (167 ánh xạ, đã kiểm ID), `D:\HOI4Mods\_gen\trunk_list2.txt` (197 focus kèm mốc năm).
