# **Con đường Kiên định** 

Nội dung cây focus giả định khi CPV Hardline đã nắm quyền 

Tài liệu nội dung, chưa code. Dành cho submod Vietnam MD. Bản nháp 04/10/2026. 

## **0. Tóm tắt thiết kế** 

Cây này chỉ mở khi đảng cầm quyền là CPV Hardline. Người chơi không "leo thang" trong cây để lên nắm quyền; việc lên nắm quyền xảy ra ngoài cây, qua event. Cây là phần cai trị sau đó: **25 focus** , chia thành một gốc, ba focus củng cố, bốn trụ cai trị, một focus tổng kết và ba kết cục loại trừ nhau. 

Ba nguyên tắc để nhánh này không biến thành "con đường xấu" hoặc "con đường thắng": 

- **Mỗi lần siết đều có phản ứng.** Một thước đo riêng, **Áp lực cải cách** , tăng theo mức độ siết. Càng siết, event phản ứng càng nặng. 

- **Có van xả có chủ đích.** Một số focus (đối ngoại có chọn lọc, kết cục điều chỉnh) giảm áp lực, đổi lại làm cán bộ bảo thủ bất mãn. 

- **Hardline khác nhánh an ninh.** Quyền lực dựa vào tổ chức Đảng, tư tưởng và chính ủy, không dựa vào giám sát đại trà. Nhánh sec_* hiện có là lớp công an, tách biệt. 

_Các con số (giá, điểm trục, ổn định, ngân sách) là bản nháp theo thang đang dùng trong file hiện tại, cần cân bằng lại khi playtest. Tên trục VIE_ax_* tôi suy ra từ cách dùng trong file, xem mục 9._ 

## **1. Điều kiện mở cây và số phận cây cũ** 

### **1.1 Điều kiện mở** 

- Gốc của cây kiểm tra thẳng: **đảng cầm quyền hiện tại là CPV Hardline** . Không dùng cờ vĩnh viễn. Mất quyền thì cả nhánh đóng ngay, lấy lại quyền thì mở lại; focus đã hoàn thành vẫn giữ. 

- Hiển thị cây cho mọi người chơi Việt Nam nhưng chỉ chọn được khi đủ điều kiện, kèm tooltip nói rõ "cần CPV Hardline cầm quyền". 

### **1.2 Số phận cây hiện có khi hardline lên** 

|**Phần cây cũ**|**Xử lý đề xuất**|
|---|---|
|Chuỗi Đại hội và nghị quyết<br>chưa làm|Đóng, tooltip "Đường lối đã đổi". Những focus đã hoàn thành vẫn giữ<br>nguyên hiệu ứng.|
|Cụm Đảng xây dựng (kỷ luật,<br>thanh tra, clean_cadres)|Vẫn mở và được hardline khai thác thêm, vì cùng hướng.|
|Cụm hội nhập (CPTPP,<br>EVFTA, financial centre,<br>investment_grade)|Vẫn làm được nhưng mỗi focus**giảm Áp lực cải cách**và làm cán bộ<br>bảo thủ bất mãn. Đây là van xả tự nhiên.|
|Cụm tư nhân<br>(private_champions,<br>private_sector_engine)|Vẫn mở, nhưng nếu đã làm A5 thì bị khóa. Hai bên loại trừ nhau.|



|**Phần cây cũ**|**Xử lý đề xuất**|
|---|---|
|Cụm kinh tế nhà nước<br>(conglomerates, scic,<br>soe_gradual_restructuring)|Mở, và nhận bonus nhỏ nếu đã làm A1.|
|Cụm quân sự<br>(modernize_vpa,<br>peoples_defence,<br>def_industry)|Giữ nguyên. Là tiền đề cho trụ Quân – Đảng.|



## **2. Đường lên nắm quyền (nằm ngoài cây)** 

Cả ba đường đều gọi chung **một effect chuyển quyền** (VIE_transition_regime hoặc tương đương) và kết thúc bằng event "Nhận quyền" ở mục 2.4. Không có đường nào thất bại ngẫu nhiên rồi bế tắc: nếu có rủi ro thì phải có cửa thử lại. 

### **2.1 Đường A. Đại hội Đảng: phe bảo thủ thắng thế** 

- **Thời điểm:** vào các mốc Đại hội đã có trong file (sched_congress_*). 

- **Điều kiện:** trục BoP bảo thủ đang dẫn và popularity của hardline đủ ngưỡng (đề xuất ≥ 15%, hiện khoảng 9,9% trong ảnh bạn gửi). 

- **Event:** Đại hội chọn đường lối. Hai lựa chọn: "Tiếp tục Đổi mới" (kết quả như hiện nay) hoặc "Giữ vững bản chất, kiên định mục tiêu" (chuyển quyền). 

### **2.2 Đường B. Khủng hoảng và Hội nghị Trung ương bất thường** 

- **Kích hoạt:** một trong ba cú sốc: khủng hoảng ngân hàng hoặc nợ (bankruptcy_incoming_collapse, nợ Vinashin lặp lại), cú sốc thuế quan Mỹ khi trục phương Tây đang cao, hoặc khủng hoảng Biển Đông kéo dài. 

- **Event:** Hội nghị Trung ương đánh giá nguyên nhân. Hai phe tranh luận; người chơi chọn "đổ lỗi cho cải cách quá nhanh" (chuyển quyền) hoặc "điều chỉnh trong khuôn khổ cũ". 

### **2.3 Đường C. Từ nhánh an ninh (chờ xác nhận)** 

- Chỉ giữ nếu xác nhận index mà sec_cyber_control chuyển sang đúng là CPV Hardline. Nếu không, bỏ đường này để tránh nhập nhằng với Security State. 

### **2.4 Event "Nhận quyền"** 

- Đặt Áp lực cải cách về **20** . 

- Áp dụng quy tắc cây cũ ở mục 1.2. 

- Cộng popularity hardline cho khớp trạng thái đã cầm quyền, tránh quay lại ngay do bầu cử hoặc nội bộ. 

- Báo cho người chơi rõ: cây "Con đường Kiên định" đã mở. 

## **3. Cơ chế riêng: Áp lực cải cách** 

Thước đo 0–100, ẩn hoặc hiện tùy ý, đây là **biến duy nhất** nhánh này cần thêm. 

|**Mức**|**Khoảng**|**Hệ quả**|
|---|---|---|
|Ổn định|0 – 30|Không có hệ quả xấu. Một số focus củng cố đạt hiệu quả đầy<br>đủ.|
|Âm ỉ|31 – 60|Mở event phản ứng nhẹ (thư kiến nghị, doanh nghiệp rút vốn).<br>Chưa có phạt định kỳ.|
|Căng thẳng|61 – 85|Phạt ổn định nhẹ liên tục. Mở Hội nghị Trung ương bất thường.<br>Mở kết cục Khép cửa.|
|Khủng hoảng|86 – 100|Phạt tăng trưởng và ổn định. Bắt buộc event khủng hoảng, mở<br>lối thoát về điều chỉnh.|



- **Tăng:** hầu hết focus siết (xem từng focus). Một số event cũng làm tăng. 

- **Giảm:** focus mở có chọn lọc (D3, kết cục điều chỉnh), các focus hội nhập cũ, và tự giảm chậm theo thời gian khi không hoàn thành focus siết mới. 

- **Tổng ước tính:** nếu làm hết các focus siết, áp lực chạm khoảng 70–80 (đã tính van D3). Đủ để buộc người chơi chọn giữa giảm tốc và chịu khủng hoảng, mà chưa thành "chắc chắn sụp". 

## **4. Danh sách focus** 

_Ghi chú đọc: "trục" là các biến VIE_ax_* (dấu + hoặc − so với trạng thái hiện tại). "Áp lực" là Áp lực cải cách. Mọi focus tốn kém đều có guard bankruptcy_incoming_collapse giống file hiện tại._ 

## **4.1 Gốc và củng cố** 

### **H0. Thống nhất ý chí và hành động** 

Giá: 5 tuần 

**Mô tả:** Hội nghị Trung ương khẳng định "giữ vững bản chất cách mạng của Đảng". Đây là điểm mở đầu của nhiệm kỳ cai trị mới. 

**Điều kiện:** Đảng cầm quyền là CPV Hardline. 

**Thưởng:** +50 PP. Đặt Áp lực cải cách về 20 (nếu chưa). BoP bảo thủ +nhẹ. Đặt cờ cây đã mở. 

**Giá:** Không. 

### **H1. Chỉnh đốn Đảng, thanh lọc hàng ngũ** 

Giá: 7 tuần 

**Mô tả:** Tinh thần Nghị quyết TW4 khóa XII: ngăn chặn suy thoái tư tưởng, "tự diễn biến, tự chuyển hóa". Kỷ luật những cán bộ bị coi là thân cải cách hoặc nghiêng về phương Tây. **Điều kiện:** H0. 

**Thưởng:** Trục ax_merit +2, ax_checks −1. Ổn định +0.03. Giảm tham nhũng một nấc. Cán bộ cộng sản +3. 

**Giá:** Áp lực +5. Tập đoàn công nghiệp −4. Gắn ý "thận trọng trong bộ máy" 365 ngày (dùng lại ý VIE_official_caution). 

### **H2. Củng cố nền tảng tư tưởng** 

Giá: 7 tuần 

**Mô tả:** Ban Tuyên giáo và hệ thống Học viện được giao thêm nguồn lực. Mục tiêu: giữ định hướng tư tưởng trong báo chí, giáo dục và đoàn thể (tinh thần Nghị quyết 35). **Điều kiện:** H0. 

**Thưởng:** +50 PP, ổn định +0.02. Trục ax_civil −1. Ý "Công tác tư tưởng" (ổn định nhẹ, giảm tác dụng chiến dịch tuyên truyền thân phương Tây nếu cơ chế cho phép). 

**Giá:** Áp lực +5. Trục ax_integ −1. 

### **H3. Thống nhất quản lý cán bộ** 

Giá: 7 tuần 

**Mô tả:** Cán bộ chủ chốt do Trung ương quản chặt hơn, giảm quyền tự quyết của địa phương. 

**Điều kiện:** H1. 

**Thưởng:** Trục ax_decent −2 (tập quyền), ax_merit +1. BoP bảo thủ nhỏ. 

**Giá:** Áp lực +4. Nếu đã làm decentralization hoặc streamline_apparatus: mất bonus của chúng một phần. 

## **4.2 Trụ A. Kinh tế** 

### **A1. Kinh tế nhà nước giữ vai trò chủ đạo** 

Giá: 7 tuần 

**Mô tả:** Khẳng định lại thành phần kinh tế nhà nước là then chốt, đặt lại ưu tiên cho các tập đoàn và tổng công ty. 

**Điều kiện:** H1. 

**Thưởng:** Trục ax_market −3. Ngân sách +2. Ý "Chủ đạo nhà nước". Cán bộ cộng sản +4. Bonus nhỏ cho state_conglomerates nếu đã làm. 

**Giá:** Áp lực +4. Tăng trưởng giảm nhẹ (ý có thời hạn). Tập đoàn công nghiệp −4. 

### **A2. Danh mục ngành then chốt** 

Giá: 7 tuần 

**Mô tả:** Xác định rõ các ngành không nhượng: năng lượng, ngân hàng, viễn thông, quốc phòng. 

**Điều kiện:** A1. 

**Thưởng:** Xây nhà máy công nghiệp ở một đến hai vùng (dùng one_state_industrial_complex). Trục ax_market −1. 

**Giá:** Áp lực +2. Guard staff và bankruptcy như các focus xây nhà máy hiện có. 

### **A3. Tập đoàn nhà nước làm đầu tàu** 

Giá: 7 tuần 

**Mô tả:** Giao các tập đoàn nhiệm vụ dẫn dắt dự án lớn: hạ tầng, năng lượng, đóng tàu. **Điều kiện:** A1. 

**Thưởng:** Một lần tăng trưởng. Ý "Tập đoàn đầu tàu" (xây dựng nhanh hơn, nhẹ). **Giá:** Áp lực +3. Rủi ro Vinashin +2 (dùng lại biến VIE_vinashin_risk): nhắc lại tiền lệ. 

### **A4. Kiểm soát dòng vốn và FDI có chọn lọc** 

Giá: 7 tuần 

**Mô tả:** FDI vẫn được chào đón nhưng theo danh mục ưu tiên; giám sát chặt dòng vốn và chuyển giá. 

**Điều kiện:** A2. 

**Thưởng:** Ổn định +0.01. +25 PP. Giảm phụ thuộc vào các nhà đầu tư nước ngoài lớn. 

**Giá:** Áp lực +5. Ngân sách −2. Ý "FDI chững lại" 365 ngày. Thiện cảm Mỹ, Nhật, Hàn giảm nhẹ (bọc guard country_exists). 

### **A5. Đảng viên không làm kinh tế tư nhân** 

Giá: 7 tuần 

**Mô tả:** Đảo ngược tinh thần party_members_private_business: cấm đảng viên giữ chức vụ đồng thời kinh doanh tư nhân. 

**Điều kiện:** H1. Loại trừ với private_champions và private_sector_engine. 

**Thưởng:** Trục ax_merit +1, ax_market −1. BoP bảo thủ nhỏ. Cán bộ cộng sản +3. 

**Giá:** Áp lực +4. Tập đoàn công nghiệp −5. 

### **A6. Kế hoạch 5 năm phiên bản mới** 

Giá: 7 tuần 

**Mô tả:** Quay lại tư duy kế hoạch định hướng: mục tiêu sản lượng, tỷ trọng và danh mục dự án quốc gia theo nhiệm kỳ. 

**Điều kiện:** A3 và A4. 

**Thưởng:** Trục ax_mob +1, ax_market −1. Ngân sách +3. Ý "Kế hoạch định hướng". **Giá:** Áp lực +3. Trục ax_size +1 (bộ máy phình ra). 

## **4.3 Trụ B. Quân – Đảng** 

### **B1. Đảng lãnh đạo tuyệt đối, trực tiếp trong quân đội** 

Giá: 7 tuần 

**Mô tả:** Nguyên tắc hiện hành của Quân đội nhân dân được nhấn mạnh trở lại, thông qua Tổng cục Chính trị và hệ thống chính ủy. 

**Điều kiện:** H0 và đã hoàn thành modernize_vpa. 

**Thưởng:** Quân đội +3 (opinion). Trục ax_mob +1. BoP bảo thủ nhỏ. Ý "Công tác Đảng, công tác chính trị trong quân đội". Mastery hoặc XP lục quân 10. 

**Giá:** Áp lực +2. Trục ax_civil −1. 

### **B2. Giáo dục chính trị trong lực lượng vũ trang** 

Giá: 5 tuần 

**Mô tả:** Chương trình huấn luyện chính trị bắt buộc, gắn với đánh giá cán bộ chỉ huy. **Điều kiện:** B1. 

**Thưởng:** War support +0.03. Ổn định +0.01. XP lục quân 10. 

**Giá:** Áp lực +1. Ngân sách −1. 

### **B3. Phòng thủ toàn dân gắn với Đảng cơ sở** 

Giá: 7 tuần 

**Mô tả:** Mở rộng thế trận quốc phòng toàn dân, đặt tổ chức Đảng ở cấp cơ sở làm trục tổ chức lực lượng. 

**Điều kiện:** B1 và đã hoàn thành peoples_defence. 

**Thưởng:** Trục ax_mob +2, ax_decent −1. Nhân lực +. Ý "Thế trận toàn dân kiểu hardline". **Giá:** Áp lực +3. Trục ax_civil −1. 

### **B4. Công nghiệp quốc phòng do Đảng chỉ đạo** 

Giá: 7 tuần 

**Mô tả:** Gắn công nghiệp quốc phòng với kế hoạch nhà nước và kiểm soát chính trị chặt hơn. **Điều kiện:** B1 và (đã chọn military_enterprises_core, hoặc chưa chọn divest). 

**Thưởng:** Cộng 1 cấp VIE_def_industry_level (dùng lại effect có sẵn). Ổn định +0.01. 

**Giá:** Áp lực +2. Trục ax_market −1. 

## **4.4 Trụ C. Xã hội và thông tin** 

### **C1. Bảo vệ nền tảng tư tưởng trên không gian mạng** 

Giá: 7 tuần 

**Mô tả:** Kiểm soát nội dung "sai trái, thù địch" trên mạng và nền tảng xuyên biên giới. Khác nhánh an ninh: mục tiêu là nội dung và tuyên truyền, không phải giám sát hàng loạt. **Điều kiện:** H2. 

**Thưởng:** Trục ax_civil −2, ax_west −1. Ý "Quản lý nội dung mạng". Giảm tác động của các chiến dịch tuyên truyền thân phương Tây nếu cơ chế cho phép. 

**Giá:** Áp lực +6. Trục ax_integ −1. 

### **C2. Giáo dục lý luận chính trị trong nhà trường** 

Giá: 7 tuần 

**Mô tả:** Tăng thời lượng và vị thế các môn lý luận chính trị ở các bậc học. 

**Điều kiện:** H2. 

**Thưởng:** Ổn định +0.02. Ý "Giáo dục lý luận". Tăng nhẹ hỗ trợ của cán bộ. 

**Giá:** Áp lực +4. Nếu đã làm education_law_2019 hoặc higher_education_law: giảm một phần bonus nghiên cứu của chúng. 

### **C3. Quản lý báo chí và xuất bản** 

Giá: 5 tuần 

**Mô tả:** Hệ thống báo chí được rà soát lại về định hướng và quản lý thông tin. **Điều kiện:** C1. 

**Thưởng:** +25 PP. Trục ax_checks −1, ax_civil −1. 

**Giá:** Áp lực +4. Thiện cảm các nước dân chủ giảm nhẹ. 

### **C4. Phát huy Mặt trận Tổ quốc và các đoàn thể** 

Giá: 7 tuần 

**Mô tả:** Dùng Mặt trận Tổ quốc, Công đoàn, Hội Nông dân và Đoàn Thanh niên làm kênh tập hợp và phản biện trong khuôn khổ. 

#### **Điều kiện:** H3. 

**Thưởng:** Trục ax_mob +2. Nông dân +4. Ổn định +0.02. 

**Giá:** Trục ax_size +1. (Không tăng Áp lực: đây là van mềm.) 

## **4.5 Trụ D. Đối ngoại** 

_Ở v14 bạn đã gỡ các focus "chọn phe" (socialist_bloc, join_bri, pivot_to_the_west...). Trụ này cố ý không chọn phe: chỉ là ngoại giao giữa các đảng và một van mở có chọn lọc._ 

### **D1. Ngoại giao Đảng** 

Giá: 7 tuần 

**Mô tả:** Tăng cường kênh quan hệ giữa các đảng cộng sản và đảng cầm quyền ở Lào, Trung Quốc, Cuba, bên cạnh ngoại giao nhà nước. 

**Điều kiện:** H0. 

**Thưởng:** +50 PP. Thiện cảm Lào và Trung Quốc +nhẹ (dùng lại modifier có sẵn). Trục ax_integ −1. 

**Giá:** Áp lực +2. Thiện cảm Mỹ, Nhật giảm nhẹ. 

### **D2. Hợp tác nhưng không lệ thuộc** 

Giá: 7 tuần 

**Mô tả:** Đảng khẳng định hợp tác ý thức hệ không thay thế lợi ích chủ quyền. Đây là focus điều tiết căng thẳng nội tại của hardline: gần Bắc Kinh về tư tưởng, nhưng không nhường ở Biển Đông. 

**Điều kiện:** D1. 

**Thưởng:** War support +0.03. Giảm căng thẳng Biển Đông một nấc. Ổn định +0.01. Gắn cờ để event "phản ứng dân tộc chủ nghĩa" có lựa chọn. 

**Giá:** Không tăng Áp lực. Thiện cảm Trung Quốc giảm nhẹ so với D1. 

### **D3. Đối tác chiến lược có chọn lọc** 

Giá: 7 tuần 

**Mô tả:** Duy trì quan hệ với Nhật Bản, Ấn Độ, Hàn Quốc trên cơ sở "ba không" hoặc "bốn không": hợp tác kinh tế và an ninh, không liên minh quân sự. 

**Điều kiện:** D1, và đã có ít nhất một trong japan_partnership, india_partnership, korea_partnership. 

**Thưởng: Áp lực −8** (van xả). Trục ax_integ +1. Thiện cảm Nhật, Ấn, Hàn +. 

**Giá:** Cán bộ cộng sản −2. 

## **4.6 Tổng kết nhiệm kỳ** 

### **E1. Tổng kết và định hướng nhiệm kỳ mới** 

Giá: 7 tuần 

**Mô tả:** Hội nghị Trung ương tổng kết kết quả củng cố, đặt ra hướng đi cho các năm tiếp theo. Điểm hội tụ trước ngã ba cuối. 

**Điều kiện:** Đã hoàn thành đủ **ba trong bốn trụ** : A6, B3 hoặc B4, C4, D2. 

**Thưởng:** +100 PP, ổn định +0.03. Ý "Mô hình cai trị kiên định". Mở ba focus kết cục. 

**Giá:** Không. Kích hoạt event Hội nghị Trung ương bất thường (mục 5, sự kiện 4). 

## **4.7 Ba kết cục (chọn một)** 

### **X1. Kiên định có điều chỉnh** 

Giá: 7 tuần 

**Mô tả:** Giữ vững mục tiêu nhưng điều chỉnh phương thức: nhà nước giữ then chốt, kinh tế tư nhân và hội nhập tiếp tục trong khuôn khổ kiểm soát. 

**Điều kiện:** E1. Áp lực dưới 85. 

**Thưởng:** Áp lực về 30. Trục ax_market +1, ax_integ +1. Tăng trưởng nhẹ. Mở lại các focus hội nhập cũ không bị phạt. Ý "Kiên định, đổi mới có kiểm soát". 

**Giá:** Cán bộ cộng sản −3. BoP bảo thủ −nhẹ. 

### **X2. Đảng hóa toàn diện** 

Giá: 7 tuần 

**Mô tả:** Hợp nhất lãnh đạo Đảng và quản lý nhà nước ở mọi cấp, giảm không gian độc lập của các thiết chế khác. 

**Điều kiện:** E1, đã hoàn thành ít nhất ba trụ, trục ax_civil ≤ −3 và ax_checks ≤ −2. 

**Thưởng:** +150 PP. Ổn định +0.05. Trục ax_checks −2, ax_decent −2. Ý "Nhất thể hóa Đảng và Nhà nước". 

**Giá:** Áp lực +10. Trục ax_integ −2, ax_market −2. Khóa investment_grade và international_financial_centre. Phạt tăng trưởng. 

### **X3. Khép cửa** 

Giá: 7 tuần 

**Mô tả:** Thu hẹp quan hệ với bên ngoài, ưu tiên tự cung tự cấp và an ninh chế độ. Không phải con đường mong muốn; được mở như hệ quả của việc siết quá đà. 

**Điều kiện:** E1. **Áp lực ≥ 70** hoặc ASEAN/phương Tây đã phản ứng mạnh (qua event). 

**Thưởng:** Ổn định +0.06. Ý "Tự lực tự cường" (giảm phụ thuộc nhập khẩu, tăng xây dựng nhà máy nội địa). 

**Giá:** Trục ax_integ −3, ax_west −3. Thiện cảm ASEAN và phương Tây giảm. Phạt tăng trưởng nặng. Kích hoạt event lối thoát sau khoảng hai năm: "Hội nghị Trung ương đánh giá lại", cho phép chuyển về hiệu ứng của X1 (mất một phần thưởng). 

_AI: mặc định đã là hardline thì base 60–80 cho các focus củng cố và trụ. Kết cục X2 và X3: factor 0 nếu VIE_ai_historical = yes, để AI theo lịch sử không đi hướng cực đoan._ 

## **5. Sự kiện phản ứng** 

|**#**|**Sự kiện**|**Kích hoạt**|**Lựa chọn chính**|
|---|---|---|---|
|1|Thư kiến nghị của các cựu<br>cán bộ|Áp lực ≥ 30, đã làm H1|Tiếp thu: áp lực −10, ổn định −. Bác bỏ:<br>áp lực +5, ổn định +0.01.|
|2|Doanh nghiệp tư nhân rút<br>vốn|Áp lực ≥ 40, đã làm A5<br>hoặc A4|Trấn an: ngân sách −2, trục ax_market<br>+1. Mặc kệ: tăng trưởng giảm.|
|3|Cảnh báo lao động và<br>thương mại từ<br>EVFTA/CPTPP|Đã có evfta hoặc<br>cptpp_member, đã làm<br>C1 hoặc C3|Điều chỉnh: áp lực −5. Chấp nhận áp<br>lực: thiện cảm EU/Nhật giảm.|



|**#**|**Sự kiện**|**Kích hoạt**|**Lựa chọn chính**|
|---|---|---|---|
|4|Hội nghị Trung ương bất<br>thường|Hoàn thành E1, hoặc<br>áp lực ≥ 61|Ba phe: giữ nguyên, nới nhẹ, siết thêm.<br>Dẫn tới các focus X1, X2, X3.|
|5|Phản ứng dân tộc chủ<br>nghĩa về Biển Đông|Căng thẳng Biển Đông<br>cao, đã làm D1|Có D2: có lựa chọn cứng rắn. Không có<br>D2: ổn định −0.02, áp lực +5.|
|6|Khủng hoảng tăng trưởng|Áp lực ≥ 86|Bắt buộc chọn: về hướng X1 (áp lực<br>−20) hoặc kiên trì (ổn định −0.04, mở<br>X3).|



_Mọi sự kiện đều có lựa chọn và không có lựa chọn nào dẫn tới bế tắc. Sự kiện 4 có thể chỉ xuất hiện một lần._ 

## **6. Ba kết cục tóm tắt** 

|**Kết cục**|**Được**|**Mất**|
|---|---|---|
|X1 Kiên định có điều<br>chỉnh|Ổn định cao, hội nhập tiếp tục<br>trong khuôn khổ, áp lực về mức<br>thấp.|Cán bộ bảo thủ bất mãn, hiệu quả<br>hardline giảm.|
|X2 Đảng hóa toàn diện|PP và ổn định cao nhất, kiểm soát<br>chặt.|Cô lập, tăng trưởng thấp, khóa các<br>hướng tài chính.|
|X3 Khép cửa|Ổn định ngắn hạn, tự lực.|Đứt gãy ASEAN và phương Tây, tăng<br>trưởng thấp; có lối thoát nhưng mất<br>thưởng.|



## **7. Đối chiếu với cây hiện có** 

|**Focus hiện có**|**Quan hệ**|
|---|---|
|party_discipline,<br>cadre_accountability,<br>clean_cadres|Bổ sung cho H1. Có thể cho bonus nhỏ nếu đã làm trước.|
|military_enterprises_core /<br>divest|B4 chỉ mở khi chưa chọn divest.|
|peoples_defence,<br>provincial_defence_zones|Tiền đề cho B3.|
|sec_cyber_control và các sec_*|Tách biệt với C1: sec_* là lớp công an, C1 là lớp nội dung. Nếu bạn<br>muốn gộp, nên bàn lại.|
|party_members_private_busine<br>ss, private_champions,<br>private_sector_engine|Loại trừ với A5.|
|state_conglomerates, scic,<br>soe_gradual_restructuring|Nhận bonus nhỏ từ A1.|
|evfta, cptpp_member,<br>investment_grade,<br>international_financial_centre|Giảm áp lực khi hoàn thành. X2 khóa hai focus cuối.|



|**Focus hiện có**|**Quan hệ**|
|---|---|
|four_nos_doctrine,|Nền cho D2 và D3. Không tạo thêm focus chọn phe.|
|bamboo_diplomacy,||
|indochina_solidarity||



## **8. Bố cục tham khảo (khi sang bước code)** 

- Đặt khối mới ở vùng trống bên trái khối chính trị, khoảng x −85 đến −80 và y 8 đến 18, khai báo sau các anchor mà nó dựa vào để tránh forward-ref. 

- Bố cục theo trục dọc: H0 ở trên cùng, H1–H3 ở hàng thứ hai, bốn trụ chạy song song theo bốn cột, E1 hội tụ ở dưới, ba kết cục xếp ngang dưới cùng. 

- Dùng search_filters hiện có (POLITICAL, STABILITY, ECONOMY, ARMY) để không cần thêm filter mới. 

## **9. Điều cần xác nhận trước khi code** 

- **Index của CPV Hardline.** Tài liệu MD ghi index 7 là Autocracy (Emerging). Cần xem file định nghĩa party để biết gốc kiểm tra theo đảng nào. 

- **VIE_party_rule_active** phản ứng thế nào khi hardline lên. Cờ này nằm trong bypass của chuỗi Đại hội. 

- **VIE_transition_regime** còn đổi gì ngoài ruling_party (tên chính phủ, ý quốc gia, cờ). 

- **Tên trục VIE_ax_*.** Tôi suy ra: checks (kiểm soát quyền lực), merit (liêm chính, thực tài), market (thị trường), integ (hội nhập), west (hướng phương Tây), civil (tự do dân sự), mob (huy động), decent (phân quyền), size (quy mô bộ máy). Cần đối chiếu với file loc. 

- **Chiến dịch tuyên truyền** (Pro-Western, Emerging, Non-Aligned, Nationalist, Salafi trong ảnh). Chưa biết nó có hook script để H2/C1 chặn hay không. 

- **Cân bằng số liệu.** Toàn bộ điểm trục, giá, ngân sách và Áp lực cải cách ở đây chỉ là đề xuất khởi điểm. 

- **Đường C** (từ nhánh an ninh): giữ hay bỏ. 

