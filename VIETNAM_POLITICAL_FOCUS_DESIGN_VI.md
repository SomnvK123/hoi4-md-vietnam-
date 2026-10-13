# Thiết kế nhánh chính trị Việt Nam: bản cân bằng theo nhiệm kỳ

**Kết luận:** Cây mở theo kỳ đại hội; chương trình trọng điểm có deadline 900 ngày và mốc thưởng sớm riêng: cán bộ/công vụ/dân vận 600, kiểm tra 690 ngày. BoP thay đổi theo hành vi, gồm ba vùng. Tuyến tập trung mua thời gian để giữ cửa sổ cơ hội; tuyến tập thể tích lũy khả năng phối hợp. Tier cán bộ giảm tổn thất chuyển giao, giảm giá khởi động và mở công cụ ký theo ủy quyền. Bản mẫu giữ 12 focus, ba xung đột chính và một event quay lại của DNNN; mục tiêu phát hành giữ đúng 74 node.

Các giá trị là thông số thiết kế từ [bảng tham số B1](VIETNAM_POLITICAL_PARAMETERS_VI.json), đã tính bằng [script ngân sách](VIETNAM_POLITICAL_BALANCE_VI.py). Báo cáo [lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md) ghi các bất biến còn FAIL. Chưa triển khai game file hoặc chạy HOI4. Bảng tính không phải mô phỏng engine.

## 1. Trang tóm tắt

| Thành phần | Người chơi quyết định | Kết quả cụ thể |
| --- | --- | --- |
| Cây theo đại hội | Chọn trong nhóm chính sách của nhiệm kỳ hiện tại | Nội dung mới mở dần từ 2001 đến 2026 |
| BoP | Tham vấn hoặc vượt phản đối | Thanh trôi theo hành động, đổi công cụ cho chương trình tiếp theo |
| Cohesion | Trả PP, chịu bất đồng hoặc phục hồi | Giá khởi động, khả năng phối hợp và tổn thất thay người |
| Chương trình nhiệm kỳ | Chọn một trong bốn lĩnh vực | Một tier khi đủ mục tiêu; thưởng sớm có hạn |
| Nhân sự | Phân vai, ủy quyền hoặc kiêm nhiệm | Khác thời gian ký, giá tổ chức và rủi ro chuyển giao |
| Event | Chọn giữa tiến độ, bằng chứng và quyền lợi | Kiến nghị, hợp đồng và phản hồi của cùng đối tượng |
| Resolver | Đánh giá đúng một lần | Full/partial/fail cùng guard kỳ |
| Bảng ngân sách | So PP, tiền, cohesion và thời gian | Thấy trường hợp cấp tốc có ích hoặc lãng phí |

**Phạm vi:** nội dung Việt Nam mới hoàn toàn. Các API chung và tham chiếu quốc tế được kiểm kê để kết nối mod; baseline và nhân vật của nhánh cũ không định hình nội dung mới.

**Lát cắt:** hai focus chuẩn bị năm 2000 và mười focus mở từ đại hội IX. Bản này giữ kiến trúc và số liệu lát cắt; danh mục phát hành mở rộng thành 74 focus có hậu quả và gate riêng, khoảng 12 node mỗi nhiệm kỳ.

## 2. Nội dung và trung tâm quyết định

| Trung tâm | Điều họ muốn | Xung đột được chơi |
| --- | --- | --- |
| Bộ/ngành | Rõ trách nhiệm, giữ chất lượng quyết định | Ký nhanh so với chứng cứ kiểm toán |
| Địa phương | Tiến độ và nguồn thu | Đền bù, giải ngân, kiến nghị chưa xử lý |
| DNNN | Vốn và quyền chủ động | Bảo lãnh, công khai nghĩa vụ, đổi điều kiện hỗ trợ |
| An ninh–quốc phòng | Giữ quyền kiểm soát rủi ro | Quyền tiếp cận dữ liệu của đối tác kỹ thuật |

Ba event lát cắt tiếp tục xử lý quyền lợi địa phương, điều kiện vốn DNNN và chất lượng bằng chứng trước deadline. Cụm XI chuyển trọng tâm tài chính sang nợ xấu ngân hàng và thị trường bất động sản đóng băng; Nghị quyết 02/NQ-CP ngày 07/01/2013 nêu xử lý nợ xấu và hỗ trợ thị trường, còn tin Chính phủ cùng năm mô tả thị trường bất động sản đóng băng; VAMC bắt đầu hoạt động trong 2013. Cụm Biển Đông được gieo ở XI qua sự cố giàn khoan HYSY-981 năm 2014, rồi được các node XIII tiếp tục dưới dạng bài toán hiện diện và kênh liên lạc. Cụm trái phiếu doanh nghiệp chuyển sang XIII: IMF ghi nhận thị trường đóng băng trong quý IV/2022 sau khi phát hành ngừng đột ngột từ cuối năm. [Nghị quyết 02/NQ-CP](https://en.baochinhphu.vn/solutions-to-remove-difficulties-against-production-and-business-support-the-market-and-deal-with-non-performing-loans-11115783.htm), [thị trường bất động sản đóng băng](https://en.baochinhphu.vn/rescuing-estate-market-benefits-the-poor-11115890.htm), [VAMC hoạt động từ 09/07/2013](https://en.baochinhphu.vn/asset-management-company-established-11117099.htm), [Bộ Ngoại giao Việt Nam về HYSY-981](https://mofa.gov.vn/vi/tin-chi-tiet/chi-tiet/hop-bao-quoc-te-ve-viec-trung-quoc-ha-dat-gian-khoan-trai-phep-trong-vung-bien-viet-nam-254.html), [IMF 2023 Article IV, Box 1](https://www.imf.org/-/media/files/publications/cr/2023/english/1vnmea2023003.pdf). Các event lựa chọn phản ứng, hiệu ứng lên nhóm lợi ích và hậu quả nhiệm kỳ sau vẫn là giả định gameplay; không gán quyết định hay động cơ cho nhân vật có thật.

Cụm DNNN/đất đai mở đầu; đầu tư và hội nhập theo đại hội X; XI xử lý nợ xấu, bất động sản đóng băng và tiền đề Biển Đông; cụm trái phiếu doanh nghiệp đặt ở XIII theo khủng hoảng cuối 2022. Trách nhiệm người thực thi, dữ liệu và kiêm nhiệm tiếp tục ở XII–XIV. Điều kiện ngày/kỳ là điều kiện khả dụng cho người chơi, không chỉ trọng số AI.

## 3. BoP và cohesion được đơn giản hóa

### 3.1. Ba vùng, thanh trôi theo hành vi

`VIE_leadership_balance` bắt đầu 0.00, giới hạn -1..1.

| Khoảng thiết kế | Vùng | PP/ngày thêm từ nhánh | Chuẩn bị và công cụ |
| --- | --- | ---: | --- |
| Dưới -0.25 | Tập thể | +0.03 | Chuẩn bị 30 ngày; nghiệm thu full nhận thêm cohesion tối đa +4, phần này có trần 70 |
| -0.25 đến +0.25 | Cân bằng | +0.03 | Chuẩn bị 30 ngày; giá và thời gian chuẩn |
| Trên +0.25 | Tập trung | +0.03 | Chuẩn bị 15 ngày; mở gói cấp tốc định danh |

- F03: BoP -0.30; F04: +0.30.
- Một tham vấn thành công có thay đổi thỏa thuận: BoP -0.05; tối đa hai checkpoint khác nhau mỗi chương trình.
- Một lần vượt phản đối: BoP +0.05, cohesion -8 ngay.
- Hòa giải thành công kiến nghị đó: BoP -0.05.
- Kiêm nhiệm/tách chức vụ: +0.10/-0.10.
- Tái nhiệm, thời gian trôi và bấm lại cùng checkpoint giữ nguyên BoP.

Một chương trình chốt mode tại lúc khởi động. Thay đổi BoP giữa chương trình không viết lại timer đã ký; công cụ của lần khởi động tiếp theo dùng giá trị mới. Đây là hợp đồng thực thi của nhiệm vụ hiện hành, không phải bản sao BoP. Trả đủ hai checkpoint đưa BoP +0.30 xuống +0.20: chương trình hiện tại giữ timer cấp tốc, lần khởi động tiếp theo bị khóa cấp tốc vì BoP không còn trên +0.25. Đây là chủ đích quản lý thanh; tooltip báo trước cả hai thời điểm.

### 3.2. Gói cấp tốc áp đúng thời gian của từng hành động

Giá gói: **25 PP** khi bắt đầu, cộng hai checkpoint. **Giá checkpoint đã chốt:** mỗi lần thương lượng trả **15 PP và 0.25 ngân khố**; hoặc vượt phản đối với cohesion -8 và BoP +0.05. Thương lượng thành công đẩy BoP -0.05. Vượt chỉ khả dụng nếu cohesion sau trừ ≥40. Từ60, hai lần vượt còn44, lần thứ ba44−8=36 bị khóa. Hai lần thương lượng vẫn đưa+0.30→+0.20, khóa cấp tốc lần tới nhưng giữ timer đã ký.

Giá thanh toán đủ hai checkpoint: **55 PP và 0.50 ngân khố**. Giá vượt cả hai: **25 PP, ngân khố0 và cohesion -16**. Giá event riêng giữ nguyên. Gói hỗn hợp thu đúng giá mỗi checkpoint: thương lượng có PP/ngân khố, vượt có cohesion/BoP; không thu phí thương lượng cho checkpoint đã vượt.

Bản mới thu chi phí phản đối một lần. Kiến nghị là milestone kết quả còn mở, không có hồ sơ hao mòn 90/180 ngày hoặc bộ đếm phí định kỳ.

| Hành động | Chuẩn | Cấp tốc | Phạm vi |
| --- | ---: | ---: | --- |
| Một đợt đào tạo | 180 ngày | 150 ngày | Chương trình cán bộ |
| Chuẩn bị phương án kế cận | 180 | 150 | Chương trình cán bộ |
| Một dự án thủ tục | 270 | 225 | Chương trình công vụ |
| Một cuộc kiểm toán DNNN | 270 | 225 | Chương trình kiểm tra |
| Một dự án địa phương | 270 | 225 | Chương trình dân vận |
| Chuẩn kiểm toán | 90 | 90 | Nền pháp lý |
| Nghiệm thu và kiểm chứng cuối | 90 | 90 | Bằng chứng và các chỉ số liên tục |

Gói trả đủ55PP +0.50ngân khố hoặc vượt đủ25PP/ngân khố0 mua cùng gói chương trình; không thu lại trên từng hành động. Có đúng hai checkpoint định danh. k=20/40/60 chỉ là tham số kiểm tra, không phải tỷ giá thật của game. Biên giá checkpoint và ngân sách đầy đủ ở11.1.

### 3.3. Cohesion và một công cụ phục hồi

`VIE_leadership_cohesion` khởi đầu **60**, clamp 0–100.

| Cohesion | Hệ số giá PP khởi động | Hậu quả |
| --- | ---: | --- |
| 70–100 | 0.90 | Phối hợp vững |
| 55–69 | 1.00 | Giá chuẩn; đủ ngưỡng nhân sự/kiểm chứng cán bộ |
| 40–54 | 1.05 | Giá khởi động cao hơn; kiêm nhiệm và kiểm chứng cán bộ chưa đủ ngưỡng |
| 20–39 | 1.15 | Bất đồng cao |
| 0–19 | 1.25 | Thêm 60 ngày chuẩn bị; công cụ phục hồi vẫn mở |

Giá khởi động = làm tròn lên của `(40 - giảm từ tier cán bộ) × hệ số cohesion`. Phụ phí cấp tốc, ký hợp đồng và event là khoản riêng.

Decision **Họp xử lý bất đồng**: 30 PP, 90 ngày, cohesion +10; dưới 20 giá 15 PP; cooldown 180 ngày từ lúc chọn. Có thể dùng cùng decision để đóng một kiến nghị định danh, đổi lại bỏ thưởng cohesion +10 của lượt đó. Đây là một decision với hai mục đích và một cooldown chung.

Cohesion 0→40 trong tình huống cô lập: bốn lượt tại ngày 90/270/450/630, giá 15+15+30+30=90 PP. Đây là số học, chưa bao gồm event và thu nhập thực của game.

Muốn vượt đủ hai checkpoint của gói kế tiếp từ 44 cần ít nhất 56; hai lượt phục hồi đưa lên 64, tổng 60 PP, hoàn tất sau 270 ngày nếu chọn ngay và dùng cooldown chung. Một lượt 30 PP đưa lên 54 chỉ đủ một checkpoint. Chương trình cán bộ cấp tốc vượt cần hai lượt phục hồi trước chuỗi kiểm chứng 90 ngày; lịch và chi phí có trong CSV/báo cáo lượt 1.

Full chương trình: cohesion +6; partial +2; fail -6. Tập thể nhận phần bổ sung tối đa +4 trước thưởng full, chỉ tăng tới 70. Một lượt full nhận phần bổ sung này một lần.

**Cổng trọng tâm và phục hồi:** forecast_programme_completion chỉ chặn chốt trọng tâm khi không còn đường khởi động của lựa chọn trong270ngày. Họp xử lý bất đồng và hòa giải/đóng kiến nghị không đọc cổng này; chúng vẫn mở theo các điều kiện PP, giá và cooldown hiện có, không được miễn cooldown. Lượt đang chạy phải đọc đúng purpose: chỉ tính +10nếu đã chọn phục hồi, không tính +10của lượt đóng kiến nghị. Tooltip hiển thị cohesion, ngày khởi động sớm nhất/muộn nhất, ngày thiếu và hành động mở lại.

## 4. Giá trị thời gian, chương trình và tier

### 4.1. Một nhiệm kỳ, một trọng tâm

Đại hội chọn **một chương trình trong bốn lĩnh vực**. Bỏ lớp “hai ưu tiên” vì chưa có lợi ích độc lập. Tier cũ vẫn tồn tại khi nhiệm kỳ sau đổi lĩnh vực.

| Chương trình → lĩnh vực | Bốn nhóm mục tiêu |
| --- | --- |
| Đào tạo kế cận → Tổ chức–cán bộ | Quy trình trách nhiệm; hai đợt đào tạo; phương án kế cận hợp lệ; cohesion ≥55 liên tục 90 ngày sau khi phương án hoàn thành |
| Chuẩn hóa thủ tục → Điều hành–công vụ | Quy trình một cửa; hai dự án thủ tục; nghiệm thu công khai; thu ≥ chi liên tục 90 ngày sau dự án thứ hai |
| Minh bạch vốn → Kiểm tra–giám sát | Chuẩn kiểm toán; hai cuộc kiểm toán; công khai và xử lý kiến nghị; giảm một bậc corruption theo baseline, hoặc kiểm chứng duy trì mức thấp nhất |
| Đền bù và dịch vụ → Dân vận–xã hội | Quy trình tiếp nhận; hai dự án có địa điểm; đóng kiến nghị của hai dự án; nghiệm thu dịch vụ và GDP/người ≥104% baseline sau hai dự án |

Nhóm GDP chỉ hợp lệ khi cả hai dự án đã có kết quả được nghiệm thu; tăng trưởng thụ động riêng không hoàn thành nhóm đó. Hồ sơ giảm corruption ghi lần chuyển bậc thực tế sau khởi động.

Ở baseline `corruption_level_01`, mục tiêu cuối chuyển thành **duy trì mức thấp nhất trong 90 ngày kiểm chứng và đóng mọi kiến nghị kiểm toán**. Resolver không gọi giảm bậc tại đáy: helper hiện có trao 150 PP trong trường hợp này, có nguy cơ thành nguồn thưởng sai. Nguồn: `common/scripted_effects/00_budget_effects.txt:783`, nhánh `corruption_level_01`.

### 4.2. Hai deadline với chức năng khác nhau

- Chọn trọng tâm trong 90 ngày sau bước kiện toàn.
- Khởi động trong 270 ngày sau đại hội. Các công cụ cơ sở mở qua F02 hoặc phương án mặc định của đại hội; focus sau đó mở cách làm chuyên sâu.
- Deadline cuối = ngày bắt đầu +900 ngày; lịch đại hội vẫn độc lập.
- Mốc thưởng sớm tính từ ngày bắt đầu: cán bộ/công vụ/dân vận 600 ngày; kiểm tra 690 ngày. Các mốc bao gồm chuẩn bị, triển khai và kiểm chứng cuối.
- Full: đủ 4/4, tăng một tier và cohesion +6.
- Full đúng hoặc trước mốc riêng: thêm 50 PP một lần, trừ hợp đồng E103 đã bỏ quyền thưởng sớm theo mục 6.5.
- Partial: 2–3/4, cohesion +2, idea hỗ trợ nhỏ 365 ngày.
- Fail: 0–1/4, cohesion -6, PP factor -3% trong 180 ngày.
- Tier tối đa 3; thành công ở tier tối đa nhận thưởng tạm thời thay tier mới.
- E103 và E104 có cửa sổ hợp đồng riêng; resolver chương trình giữ deadline cuối của mình.

**Ngày dư dùng được — decision “Dự án hỗ trợ thực thi sau nghiệm thu”.** Full đúng hoặc trước mốc riêng mở một dự án phụ, kể cả khi đã bỏ thưởng PP qua E103-B/C. Giá 30 PP, ngân khố 0; thời gian 270 ngày, một mục tiêu: hoàn tất dự án hỗ trợ tại cùng bộ phận đã được nghiệm thu. Khi thành công nhận idea bureaucracy cost factor -1% trong 365 ngày; không trao tier hoặc PP. Idea thay thế cùng loại khi còn hạn, không cộng chồng. Deadline dự án phụ là ngày mở chuẩn bị đại hội sau, tách khỏi mission trọng điểm đã đóng. Bắt đầu chỉ khi còn ít nhất thời gian dự án cộng 100 ngày dự phòng. Timeout/cancel không trao thưởng; tooltip báo điều kiện và tiền đã chi. Guard `VIE_last_side_project_epoch` ghi lúc nhận dự án, cùng epoch chương trình: tối đa một lần mỗi nhiệm kỳ, hủy cũng không mở lại. F12/timeout/load save dùng chung guard.

I2 kiểm **PP thuần**: gói55PP so với thưởng50PP chênh5PP, PASS. Gói trả đủ còn chi0.50ngân khố; chênh quy đổi ở k20/40/60 lần lượt15/25/35PP. Đây là sensitivity, không phải giá engine; không dùng chênh quy đổi để đổi định nghĩa I2. Giá trị còn lại của cấp tốc đến từ dự án phụ L1.2; cửa sổ hợp đồng được theo dõi riêng.

**Bất biến lịch:** deadline programme vẫn bắt đầu+900. Trigger thiết kế `forecast_programme_completion` tính ngày từ timer/mode đã ký, chuẩn bị tại start và trễ tất định đã biết. Start chỉ mở khi lịch mặc định≤800; lựa chọn gây trễ chỉ mở khi dự báo≤840. Available, tooltip và CSV dùng chung kết quả trigger, không tự tính lại. E103-A chưa đủ hồ sơ chỉ là rủi ro: hiển thị nhánh thẩm định+180, không khóa chỉ vì rủi ro chưa hiện thực. Nếu rủi ro xảy ra, ghi ngày thực tế và dự phòng dưới sàn; không tự sửa timer hoặc ép partial. Sau start phục hồi cohesion không xóa+60ngày chuẩn bị đã ký. Đây là phạm vi I5 theo xác nhận mới: cổng trễ tất định, không bảo đảm mọi nhánh rủi ro giữ60ngày.

**Kiểm kẹt cửa sổ khởi động:** cổng chốt đã được bổ sung. Available/tooltip/AI chỉ đọc forecast_programme_completion. Với một lựa chọn, phải còn đường của programme mà nó chốt; cổng chung cần ít nhất một trong bốn programme. Trước start, trigger xét cohesion hiện tại, +60chuẩn bị khi dưới20, cooldown còn lại và lượt phục hồi đang chạy. Tính ngày khởi động sớm nhất trước hoặc đúng270, giả định các bước còn lại thành công; không chốt programme không thể mở trong cửa sổ. Sau start, timer/mode đã ký không giảm hồi tố. Gate kỳ/chế độ/90ngày chọn trọng tâm, PP/ngân khố giữ nguyên. Cổng không khóa phục hồi/hòa giải; giá/cooldown của chúng vẫn áp dụng. Không tự cứu trọng tâm đã chốt từ save cũ, không tạo fallback hoặc penalty mới.

### 4.3. Lịch tuần tự và ngân sách công cụ

| Chương trình | Chuỗi tuần tự, bỏ qua focus đã làm | Chuẩn, gồm chuẩn bị | Cấp tốc, gồm chuẩn bị | Giá công cụ cơ sở |
| --- | --- | ---: | ---: | --- |
| Cán bộ | 2×180 đào tạo +180 kế cận +90 kiểm chứng | 660 ngày | 555 | 40+2×25+30+25 =145 PP; 0.50 ngân khố |
| Công vụ | 2×270 dự án +90 kiểm chứng | 660 | 555 | 40+2×40+25 =145 PP; 1.00 ngân khố |
| Kiểm tra | 90 chuẩn +2×270 kiểm toán +90 kiểm chứng | 750 | 645 | 40+25+2×30+25 =150 PP; 0.75 ngân khố |
| Dân vận | 2×270 dự án +90 kiểm chứng | 660 | 555 | 40+2×30+25 =125 PP; 1.00 ngân khố |

Cấp tốc thêm55PP và0.50ngân khố nếu thương lượng cả hai checkpoint, hoặc25PP/ngân khố0/cohesion-16 nếu vượt cả hai. Giá bảng là tier cán bộ0, cohesion60; công cụ cơ sở giữ nguyên. CSV cộng phí ngân khố checkpoint một lần cho gói trả đủ, kể cả kiêm nhiệm; event và kiêm nhiệm kê riêng.

Hai dự án/đào tạo/kiểm toán trong lịch là tuần tự vì dùng cùng đội triển khai. Dự án khác hệ thống vẫn có thể chạy song song; chúng không rút lịch chứng cứ của chương trình. Focus chạy song song với mission; bảng ngày không cộng focus vào timeline chương trình.

### 4.4. Tier cán bộ có giá trị sử dụng hằng nhiệm kỳ

| Lĩnh vực | Tier 1 | Tier 2 | Tier 3 |
| --- | --- | --- | --- |
| Tổ chức–cán bộ | Đợt chuyển giao mất cohesion 8 thay vì 12; giảm PP khởi động 5; ký theo ủy quyền 30 ngày | Mất 5; giảm 10; ký 25 ngày | Mất 3; giảm 15; ký 21 ngày |
| Điều hành–công vụ | Bureaucracy cost -2% | -4% | -6% |
| Kiểm tra–giám sát | Corruption cost factor -2% | -4% | -6% |
| Dân vận–xã hội | Stability modifier +1 điểm phần trăm | +2 | +3 |

Thời gian penalty thay người vẫn 75/60/45 ngày theo tier, so với 90 ngày và PP factor -5% ở tier 0. Giảm cohesion và giá khởi động là lợi ích chính; rút penalty chỉ là phần phụ.

Một đợt kiện toàn có thay người thu mất cohesion một lần, không nhân theo số slot. Khi người kiêm nhiệm rời chức, surcharge **cohesion -4 và penalty +30 ngày** vẫn giữ riêng. Tier cán bộ không xóa giá cấp tốc hoặc vượt phản đối.

Tier 1 đáp ứng cửa sổ E104 30 ngày; tier 2 đáp ứng XIII09 25 ngày; tier 3 hoặc kiêm nhiệm đáp ứng XIV11 21 ngày. Vì vậy có một đường xây bộ máy dài hạn thay cho gộp chức vụ.

## 5. Đại hội và roster nhiều vai trò

### 5.1. Lịch được chốt

| Kỳ | Ngày mở theo mốc lịch sử | Năm nhiệm kỳ để neo chương trình |
| --- | --- | --- |
| IX | 19/04/2001 | 2001–2006 |
| X | 18/04/2006 | 2006–2011 |
| XI | 12/01/2011 | 2011–2016 |
| XII | 20/01/2016 | 2016–2021 |
| XIII | 25/01/2021 | 2021–2026 |
| XIV | 19/01/2026 | 2026–2031 |
| XV, giả định gameplay | 19/01/2031 | 2031–2036 |

Chu kỳ được neo khoảng năm năm, với ngày thực tế từng kỳ. XV là lịch giả định của game, tách khỏi lịch sử đã xảy ra. Thời gian chuẩn bị **180 ngày trước ngày mở**; phiên đại hội **7 ngày gameplay**; kiện toàn **30 ngày gameplay**. Hai khoảng sau là trừu tượng hóa, không khẳng định thời gian tổ chức thật.

Nguồn ngày IX–XI: [Các kỳ Đại hội Đảng](https://baochinhphu.vn/thong-tin-ve-cac-ky-dai-hoi-dang-toan-quoc-10256170.htm); XII: [Nghị quyết Đại hội XII](https://baochinhphu.vn/nghi-quyet-dai-hoi-dai-bieu-toan-quoc-lan-thu-xii-102197756.htm); XIII: [Nghị quyết Đại hội XIII](https://baochinhphu.vn/toan-van-nghi-quyet-dai-hoi-dai-bieu-toan-quoc-lan-thu-xiii-cua-dang-102288263.htm); XIV: [Bế mạc Đại hội XIV](https://baochinhphu.vn/truc-tiep-phien-be-mac-dai-hoi-dai-bieu-toan-quoc-lan-thu-xiv-cua-dang-102260123120755096.htm).

Scheduler tháng xếp event đến đúng ngày milestone và lưu trạng thái pending. Focus chuẩn bị cho lợi thế nhưng lịch độc lập. Kỳ đã giải quyết được guard bằng `VIE_last_congress`.


### 5.2. Phân vai, ủy quyền và kiêm nhiệm

Nguồn chân lý là mảng `VIE_office_holders`, index 1–4: Tổng Bí thư, Chủ tịch nước, Thủ tướng, Chủ tịch Quốc hội; index 0 để trống. Cùng mã nhân vật có thể giữ Tổng Bí thư và Chủ tịch nước theo tổ hợp hợp lệ. Adapter dựng country leader/advisor/GUI từ mảng, trait cá nhân một lần.

Tiền lệ giữ đồng thời hai vai trò năm 2024 đã được xác minh: [Thông tin ngày 03/08/2024](https://media.chinhphu.vn/tieu-su-tong-bi-thu-chu-tich-nuoc-to-lam-102240803110403772.htm). Việc cho phép từ 2001 là lựa chọn giả định gameplay, cần ghi rõ trong game.

| Phương án | Điều kiện | Giá và hiệu quả |
| --- | --- | --- |
| Phân vai | Roster hợp lệ | Gói ký liên ngành cần 45 ngày ở tier cán bộ 0, cải thiện theo tier |
| Kiêm nhiệm | IX đã giải quyết; BoP >0.25; cohesion ≥55; roster hợp lệ | 60 PP, cohesion -6, BoP +0.10; ký liên ngành 21 ngày |
| Tách lại | Kiêm nhiệm ít nhất 180 ngày; ứng viên hợp lệ | 45 PP, cohesion +2, BoP -0.10 |
| Thay người kiêm nhiệm | Có tình huống rời chức | Adapter kiện toàn hai vai trò; surcharge riêng |

F04 đưa BoP lên +0.30 nên kiêm nhiệm có đường mở ngay trong lát cắt. Ký liên ngành phục vụ E104 ở nhiệm kỳ IX, không đợi cụm ngoại giao mở rộng. Deadline chương trình nội trị không được rút lần thứ hai do kiêm nhiệm.

Ký theo tier cán bộ 0/1/2/3 là 45/30/25/21 ngày; kiêm nhiệm 21 ngày. Tier cán bộ/kiêm nhiệm dùng thời gian ký thấp hơn khi cùng áp dụng, không cộng hai mức giảm. Mỗi kỳ có một hợp đồng E104, nên lợi ích kiêm nhiệm không thành nguồn tiền vô hạn.

## 6. Lát cắt 12 focus và event khác nhau

### 6.1. Cây mở theo kỳ

F01/F02 mở năm 2000. F03–F12 cần đại hội IX đã giải quyết. F03/F04 loại trừ; F05 đi F03, F06 đi F04; F07 cần F05 OR F06; F08 sau F07; F09/F10 sau F08; F11 sau F09, F12 sau F10.

Lịch và công cụ cơ sở của chương trình có phương án mặc định tại đại hội khi người chơi bỏ focus chuẩn bị. Focus tạo chính sách và lựa chọn riêng, không sở hữu quyền cho đại hội diễn ra.

### 6.2. Focus thông qua chính sách, mission thực hiện chương trình

Cost dự kiến 3/5/7 tương ứng 21/35/49 ngày ở 7 ngày/đơn vị. Focus lớn mở chương trình dùng cost 7; defines thực tế cần xác nhận trước khi triển khai.

| ID | Focus | Cost | Gate | Hậu quả |
| --- | --- | ---: | --- | --- |
| F01 `review_public_administration` | Rà soát thủ tục và vốn nhà nước | 5 | Năm 2000 | PP +30; chẩn đoán bộ/ngành và địa phương |
| F02 `publish_responsibility_rules` | Công bố quy trình trách nhiệm | 7 | F01 | PP -25; mở công cụ cơ sở bốn chương trình |
| F03 `consult_provincial_leaders` | Tham vấn địa phương trước giải ngân | 5 | IX; F02; loại trừ F04 | BoP -0.30; cohesion +4; công cụ tham vấn có kết quả |
| F04 `establish_project_command` | Lập đầu mối chỉ đạo dự án | 5 | IX; F02; loại trừ F03 | BoP +0.30; PP -25; gói cấp tốc, decision kiêm nhiệm |
| F05 `publish_land_compensation_plan` | Công khai phương án đền bù đất | 7 | F03 | E101, dự án có kiến nghị định danh |
| F06 `audit_state_enterprise_guarantees` | Kiểm toán bảo lãnh DNNN | 7 | F04 | E102; điều kiện vốn và dữ liệu cho E104 |
| F07 `publish_term_action_plan` | Công bố kế hoạch thực hiện nghị quyết | 5 | F05 OR F06 | PP +20; chương trình đã chọn và giá khởi động rõ |
| F08 `pilot_one_stop_service` | Thí điểm thủ tục một cửa | 7 | F07 | Công cụ chuyên sâu: nghiệm thu hai dự án; một lần nhận DM bureaucracy cost -2% khi đủ chứng cứ |
| F09 `train_successor_candidates` | Đào tạo cán bộ và người kế cận | 5 | F08 | Hai đợt đào tạo và phương án kế cận; bằng chứng cho tier |
| F10 `publish_procurement_audits` | Công bố kiểm toán mua sắm công | 5 | F08 | Quy trình xử lý hồ sơ E103 và công cụ giải quyết kiến nghị |
| F11 `establish_grievance_hearings` | Mở phiên tiếp nhận khiếu nại dự án | 5 | F09 | Hai hồ sơ khác nhau; đóng kiến nghị theo lựa chọn |
| F12 `review_program_delivery` | Nghiệm thu và công bố kết quả | 3 | F10 | Yêu cầu review sớm; resolver full hoặc chờ deadline |

Một lượt chọn một nhánh F03/F04 có 10 focus, tổng cost 54, khoảng **378 ngày focus cơ sở**. Lịch chương trình chạy song song. Một nhiệm kỳ có thời gian cho focus kinh tế/quân sự và quyết định triển khai; cây chính trị không cần chiếm mọi ngày.

F08 và F09 cung cấp công cụ chuyên sâu, không thêm tier trực tiếp. Công cụ cơ sở qua F02/đại hội giữ mọi lĩnh vực khả thi trên cả hai tuyến.

### 6.3. E101: giải ngân và đền bù là quyền lợi, không chỉ PP

Caller F05, một lần. Kiến nghị đền bù gắn với cùng dự án khi quay lại nghiệm thu.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| Chốt đền bù trước triển khai | 25 PP, 0.50 ngân khố | Cohesion +2; BoP -0.05; đóng kiến nghị, dự án địa phương +60 ngày |
| Triển khai trước theo giá đã duyệt | Cohesion -8, BoP +0.05 | Giữ tiến độ; kiến nghị tồn tại; nghiệm thu dân vận bị thiếu nhóm nếu chưa giải quyết |
| Giảm diện tích thu hồi | 15 PP, 0.25 ngân khố | Cohesion +1; dự án nhỏ đạt một checkpoint; dự án thứ hai vẫn cần theo mục tiêu công bố |

Ngân sách đền bù mua giải pháp cụ thể cho dự án, không bảo đảm mọi lĩnh vực đồng thuận.

### 6.4. E102: bảo lãnh được đổi lấy điều kiện công khai

Caller F06 hoặc lần khởi động kiểm toán cơ sở đầu tiên của chương trình, với guard để chỉ mở một lần trong kỳ. Cả hai tuyến gặp cùng DNNN khi kiểm toán; F06 cho phép xử lý phương án sớm. DNNN giữ lịch sử lựa chọn để E104 đọc.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| Cấp vốn có điều kiện kiểm toán và công khai | 30 PP, 0.50 ngân khố | Mở hồ sơ có quyền tiếp cận dữ liệu; vẫn phải làm kiểm toán; đủ điều kiện E104 |
| Kiểm toán bằng đội trong nước, giữ dữ liệu hạn chế | 20 PP, 0.25 ngân khố | Hồ sơ kiểm toán hợp lệ; giữ phương án đối nội; E104 không mở gói quốc tế |
| Giữ bảo lãnh, hoãn công khai | 0.75 ngân khố | Xây dựng +2% trong 365 ngày; kiểm toán +90 ngày; kiến nghị công khai còn mở |

E102-C cộng90ngày vào chuỗi chứng cứ, kiến nghị công khai vẫn phải xử lý để đủ mục tiêu. Tooltip trước lựa chọn E102-C hiển thị kết quả dự kiến từng E103: nếu B/C, full840/825/735 và dự phòng60/75/165 theo mode; nếu A, hiển thị thẩm định lại và partial dự kiến. Khi mode chưa chốt, hiển thị các mode khả dụng; sau khi chốt lấy timer đã ký. Các phương án không tự cho cohesion dương. B rẻ hơn A nhưng bỏ cơ hội kỹ thuật; C hỗ trợ ngắn hạn nhưng làm trễ chứng cứ. Tất cả giá E102 giữ nguyên.

### 6.5. E103: bằng chứng trước hạn, trả tiền không làm chứng cứ xuất hiện

Caller: programme kiểm tra đến ngày450, xếp một lần theo epoch. F10 mở công cụ chuyên sâu. Hạn cam kết A vẫn là mốc sớm kiểm tra690.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| A — Cam kết nộp hồ sơ đầy đủ đúng hạn | 0 PP | Đủ4/4 trước hoặc đúng690 được chấp nhận và giữ thưởng sớm. Nếu thiếu: cohesion-6; thẩm định lại tuần tự thêm180ngày. |
| B — Xin gia hạn, công khai phần còn thiếu | 0 PP + 0.50 ngân khố | Gia hạn hợp đồng đến ngày780; đủ chứng cứ mới chấp nhận. Hủy thưởng PP sớm của kỳ; giữ quyền dự án phụ nếu programme full sớm. Không cộng thêm ngày programme. |
| C — Công bố kết quả có giới hạn | 15 PP | Chốt hợp đồng partial; programme tiếp tục kiểm chứng tới deadline. Bỏ thưởng PP sớm, vẫn có thể full/tier khi đủ4/4. |

**Quy tắc tuần tự giữ nguyên:** T là ngày chứng cứ sẵn sàng, gồm E102-C cộng90ngày. A thiếu ở hạn cam kết có ngày full tiềm năng=max(T,690)+180. B/C không thêm thẩm định lại; gia hạn không tạo chứng cứ. B trượt hạn hợp đồng780 không đổi deadline programme900. C không tự tạo nhóm mục tiêu còn thiếu.

**Lệch đã xử lý theo xác nhận mới:** bản trước ghi B30PP và hạn810. Bạn chốt B0PP+0.50ngân khố, hạn780; do đó dùng780, không tự coi810 là hiệu ứng đã giữ. E102+90, thẩm định+180, C15PP và programme900 giữ nguyên.

**I3 — hai kịch bản:** A rẻ nhất khi hồ sơ đã đủ là chấp nhận được. A chưa đủ gồm6cohesion×3=18PP quy đổi và180ngày thẩm định riêng; không gán tỷ giá ngày sangPP. Không option nào rẻ nhất đồng thời ở cả hai kịch bản và mọi k. Cột B−A/B−C/A−C ghi chênh có dấu; cảnh báo dùng trị tuyệt đối. Biên nhỏ hơn3PP được báo, không chỉnh số.

| Hồ sơ | k | A | B | C | A thêm ngày | Rẻ nhất | Biên hạng1–2 | B−A | B−C | A−C | Cảnh báo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Đủ hồ sơ | 20 | 0 | 10.0 | 15 | 0 | A | 10.0 | 10.0 | -5.0 | -15 |  |
| Đủ hồ sơ | 40 | 0 | 20.0 | 15 | 0 | A | 15 | 20.0 | 5.0 | -15 |  |
| Đủ hồ sơ | 60 | 0 | 30.0 | 15 | 0 | A | 15 | 30.0 | 15.0 | -15 |  |
| Chưa đủ hồ sơ | 20 | 18 | 10.0 | 15 | 180 | B | 5.0 | -8.0 | -5.0 | 3 |  |
| Chưa đủ hồ sơ | 40 | 18 | 20.0 | 15 | 180 | C | 3 | 2.0 | 5.0 | 3 | BIÊN <3 |
| Chưa đủ hồ sơ | 60 | 18 | 30.0 | 15 | 180 | C | 3 | 12.0 | 15.0 | 3 |  |

**E102 × E103, snapshot cohesion60:** ngày tiềm năng/kết quả hợp đồng lấy từ CSV; k/r không đổi timer.

| Tuyến | Mode | E102 | E103 | Ngày full tiềm năng | Programme | Hợp đồng | Dự phòng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | E102-A | E103-A | 930 | partial ở 900 | rejected | Không full |
| collective | standard | E102-A | E103-B | 750 | full | extended | 150 |
| collective | standard | E102-A | E103-C | 750 | full | partial | 150 |
| collective | standard | E102-B | E103-A | 930 | partial ở 900 | rejected | Không full |
| collective | standard | E102-B | E103-B | 750 | full | extended | 150 |
| collective | standard | E102-B | E103-C | 750 | full | partial | 150 |
| collective | standard | E102-C | E103-A | 1020 | partial ở 900 | rejected | Không full |
| collective | standard | E102-C | E103-B | 840 | full | extension_missed | 60 |
| collective | standard | E102-C | E103-C | 840 | full | partial | 60 |
| balanced | standard | E102-A | E103-A | 930 | partial ở 900 | rejected | Không full |
| balanced | standard | E102-A | E103-B | 750 | full | extended | 150 |
| balanced | standard | E102-A | E103-C | 750 | full | partial | 150 |
| balanced | standard | E102-B | E103-A | 930 | partial ở 900 | rejected | Không full |
| balanced | standard | E102-B | E103-B | 750 | full | extended | 150 |
| balanced | standard | E102-B | E103-C | 750 | full | partial | 150 |
| balanced | standard | E102-C | E103-A | 1020 | partial ở 900 | rejected | Không full |
| balanced | standard | E102-C | E103-B | 840 | full | extension_missed | 60 |
| balanced | standard | E102-C | E103-C | 840 | full | partial | 60 |
| central | standard | E102-A | E103-A | 915 | partial ở 900 | rejected | Không full |
| central | standard | E102-A | E103-B | 735 | full | extended | 165 |
| central | standard | E102-A | E103-C | 735 | full | partial | 165 |
| central | standard | E102-B | E103-A | 915 | partial ở 900 | rejected | Không full |
| central | standard | E102-B | E103-B | 735 | full | extended | 165 |
| central | standard | E102-B | E103-C | 735 | full | partial | 165 |
| central | standard | E102-C | E103-A | 1005 | partial ở 900 | rejected | Không full |
| central | standard | E102-C | E103-B | 825 | full | extension_missed | 75 |
| central | standard | E102-C | E103-C | 825 | full | partial | 75 |
| central | fast_paid | E102-A | E103-A | 645 | full | accepted | 255 |
| central | fast_paid | E102-A | E103-B | 645 | full | extended | 255 |
| central | fast_paid | E102-A | E103-C | 645 | full | partial | 255 |
| central | fast_paid | E102-B | E103-A | 645 | full | accepted | 255 |
| central | fast_paid | E102-B | E103-B | 645 | full | extended | 255 |
| central | fast_paid | E102-B | E103-C | 645 | full | partial | 255 |
| central | fast_paid | E102-C | E103-A | 915 | partial ở 900 | rejected | Không full |
| central | fast_paid | E102-C | E103-B | 735 | full | extended | 165 |
| central | fast_paid | E102-C | E103-C | 735 | full | partial | 165 |
| central | fast_override | E102-A | E103-A | 645 | full | accepted | 255 |
| central | fast_override | E102-A | E103-B | 645 | full | extended | 255 |
| central | fast_override | E102-A | E103-C | 645 | full | partial | 255 |
| central | fast_override | E102-B | E103-A | 645 | full | accepted | 255 |
| central | fast_override | E102-B | E103-B | 645 | full | extended | 255 |
| central | fast_override | E102-B | E103-C | 645 | full | partial | 255 |
| central | fast_override | E102-C | E103-A | 915 | partial ở 900 | rejected | Không full |
| central | fast_override | E102-C | E103-B | 735 | full | extended | 165 |
| central | fast_override | E102-C | E103-C | 735 | full | partial | 165 |
| central | combined_fast_paid | E102-A | E103-A | 645 | full | accepted | 255 |
| central | combined_fast_paid | E102-A | E103-B | 645 | full | extended | 255 |
| central | combined_fast_paid | E102-A | E103-C | 645 | full | partial | 255 |
| central | combined_fast_paid | E102-B | E103-A | 645 | full | accepted | 255 |
| central | combined_fast_paid | E102-B | E103-B | 645 | full | extended | 255 |
| central | combined_fast_paid | E102-B | E103-C | 645 | full | partial | 255 |
| central | combined_fast_paid | E102-C | E103-A | 915 | partial ở 900 | rejected | Không full |
| central | combined_fast_paid | E102-C | E103-B | 735 | full | extended | 165 |
| central | combined_fast_paid | E102-C | E103-C | 735 | full | partial | 165 |

**I5 — mọi đường ngoại lệ:** sàn60ngày. Bảng có snapshot60 và probe cohesion<20; probe thấp chỉ kiểm lịch kiểm tra, không giả lập thu nhập hoặc phục hồi của programme khác. Loại mode vượt/kiêm nhiệm nếu không đủ cohesion. Dự phòng=900−ngày full tiềm năng; số âm là chuỗi không full, được chốt partial tại deadline. Các hàng DƯỚI SÀN được báo, không tự sửa kết quả/timer.

| Cohesion | Tuyến | Mode | E102 | E103 | Ngày tiềm năng | Dự phòng | Programme | Hợp đồng | Sàn | Lý do | Cổng | Dự báo tất định | Dự phòng dự báo | Rủi ro A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| snapshot | collective | standard | A | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | collective | standard | A | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | A | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | B | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | collective | standard | B | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | B | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | C | A | 1020 | -120 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 840 | 60 | CẢNH BÁO |
| snapshot | collective | standard | C | B | 840 | 60 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | collective | standard | C | C | 840 | 60 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | balanced | standard | A | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | balanced | standard | A | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | A | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | B | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | balanced | standard | B | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | B | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | C | A | 1020 | -120 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 840 | 60 | CẢNH BÁO |
| snapshot | balanced | standard | C | B | 840 | 60 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | balanced | standard | C | C | 840 | 60 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | central | standard | A | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | standard | A | B | 735 | 165 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | A | C | 735 | 165 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | B | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | standard | B | B | 735 | 165 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | B | C | 735 | 165 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | C | A | 1005 | -105 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 825 | 75 | CẢNH BÁO |
| snapshot | central | standard | C | B | 825 | 75 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 825 | 75 |  |
| snapshot | central | standard | C | C | 825 | 75 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 825 | 75 |  |
| snapshot | central | fast_paid | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | fast_paid | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_paid | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_override | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | fast_override | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_override | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | combined_fast_paid | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | combined_fast_paid | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | combined_fast_paid | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| low | collective | standard | A | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | collective | standard | A | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | A | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | B | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | collective | standard | B | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | B | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | C | A | 1080 | -180 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_start | 900 | 0 | CẢNH BÁO |
| low | collective | standard | C | B | 900 | 0 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | collective | standard | C | C | 900 | 0 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | balanced | standard | A | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | balanced | standard | A | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | A | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | B | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | balanced | standard | B | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | B | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | C | A | 1080 | -180 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_start | 900 | 0 | CẢNH BÁO |
| low | balanced | standard | C | B | 900 | 0 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | balanced | standard | C | C | 900 | 0 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | central | standard | A | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | standard | A | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | A | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | B | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | standard | B | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | B | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | C | A | 1065 | -165 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_choice | 885 | 15 | CẢNH BÁO |
| low | central | standard | C | B | 885 | 15 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_choice | 885 | 15 |  |
| low | central | standard | C | C | 885 | 15 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_choice | 885 | 15 |  |
| low | central | fast_paid | A | A | 885 | 15 | full | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 705 | 195 | CẢNH BÁO |
| low | central | fast_paid | A | B | 705 | 195 | full | extended | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | A | C | 705 | 195 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | B | A | 885 | 15 | full | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 705 | 195 | CẢNH BÁO |
| low | central | fast_paid | B | B | 705 | 195 | full | extended | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | B | C | 705 | 195 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | C | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | fast_paid | C | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | fast_paid | C | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |

Ngày tiềm năng/kết quả ở bảng là phản thực để nhìn thấy đường bị khóa, không phải kết quả đã trao. Cột cổng dùng duy nhất `forecast_programme_completion`: locked_start khi lịch mặc định>800; locked_choice khi trễ tất định>840; A chưa đủ chỉ cảnh báo nhánh rủi ro. Trong8đường full cũ dưới sàn,6đường bị cổng start/choice khóa;2đường A cấp tốc thấp cohesion còn khả dụng với rủi ro885/dự phòng15. Chúng không được gọi là bảo đảm đạt sàn. Full825/840 giữ nguyên; A quá900 vẫn partial theo luật cũ. Tooltip nêu ngày, dự phòng, lý do khóa và cách mở lại; timer đã ký không bị phục hồi hồi tố.

**I2 theo PP thuần, chênh quy đổi báo riêng:**

| k thử | Giá gói PP | Thưởng PP | Chênh PP thuần | Ngân khố gói | Chênh quy đổi |
| --- | --- | --- | --- | --- | --- |
| 20 | 55 | 50 | 5 | 0.5 | 15.0 |
| 40 | 55 | 50 | 5 | 0.5 | 25.0 |
| 60 | 55 | 50 | 5 | 0.5 | 35.0 |

**I3 checkpoint — biên mỏng k=40:**

| k thử | Thương lượng quy đổi | Vượt quy đổi | Thương lượng − vượt |
| --- | --- | --- | --- |
| 20 | 20.0 | 24 | -4.0 |
| 40 | 25.0 | 24 | 1.0 |
| 60 | 30.0 | 24 | 6.0 |








**Cổng dự báo dùng chung:** E102-C và các lựa chọn có trễ tất định gọi forecast_programme_completion với mode/timer đã ký; khóa khi ngày dự báo>840. E103-A chưa đủ hồ sơ chỉ hiển thị rủi ro; không khóa chỉ vì khả năng bị bác. E104 và hợp đồng nối tiếp vẫn kiểm riêng cửa sổ ký theo tier; không tự cộng timer ký vào chuỗi programme, không gia hạn cửa sổ để vượt cổng.


### 6.6. E104: DNNN quay lại, an ninh và thời gian ký có giá

Caller chương trình kiểm tra ngày 500, chỉ khi đã có điều kiện công khai E102-A. Một đối tác gửi đề nghị hỗ trợ kỹ thuật có hạn **30 ngày**.

- Phân vai tier cán bộ 0: ký liên ngành 45 ngày, trễ cửa sổ.
- Tier 1: 30 ngày; tier 2: 25 ngày; tier 3 hoặc kiêm nhiệm: 21 ngày. Tier 1 đã đủ cửa sổ IX; XIII09 cần 25 ngày và XIV11 cần 21 ngày.
- Giá ký: 30 PP; thanh toán lúc chọn khi lịch ký có khả năng tới hạn. Khi không đủ thời gian, UI giới thiệu hai lựa chọn khác.

| Lựa chọn | Giá và thời gian | Hệ quả |
| --- | --- | --- |
| Ký gói có quyền tiếp cận dữ liệu | 30 PP; thời gian theo roster/tier | Trước hoặc đúng hạn nhận 0.75 ngân khố hỗ trợ; hoàn tất một checkpoint hợp tác; an ninh yêu cầu kiểm chứng phạm vi dữ liệu trong review cuối |
| Xin gói thu hẹp dữ liệu | 15 PP, 21 ngày | Hỗ trợ 0.25; chỉ dùng chuyên gia đào tạo, không có checkpoint hợp tác sâu |
| Dùng đội trong nước | 0 PP | Giữ kế hoạch kiểm toán; không nhận hỗ trợ quốc tế |

Hỗ trợ chỉ được trao khi đối tác chấp nhận và ký đúng hạn; bảng tính dùng tình huống họ chấp nhận. Checkpoint hợp tác là lợi ích riêng, không thay mục tiêu giảm corruption. Kiểm chứng dữ liệu gộp vào 90 ngày review, không cộng timer giấu kín.

Kiêm nhiệm có lợi ích ngay trong lát cắt, nhưng trả 60 PP/cohesion và đánh đổi dữ liệu. Đầu tư tier cán bộ mở cùng cửa sổ mà không gộp chức vụ.

## 7. Mục tiêu phát hành: đúng 74 focus, mở theo đại hội

### 7.1. Quy mô theo lựa chọn thực tế

**Mục tiêu thiết kế hiện tại là 74 focus:** 2 node chuẩn bị năm 2000 và 12 node cho mỗi kỳ IX–XIV. Đây là tổng cố định của yêu cầu sửa hiện tại; thử nghiệm chỉ thay nội dung node, không đổi tổng. Số 48 của bản trước không còn là chỉ tiêu phát hành.

Tăng số focus để thêm vấn đề, phương án và hậu quả. Thời lượng focus được chọn theo hành động thông qua chính sách; mission vẫn xử lý triển khai. Các node bổ sung đã có hậu quả cụ thể ở bảng dưới, không còn chỉ là vị trí dự phòng.

| Kỳ mở | Nhóm | Số node | Lựa chọn chính |
| --- | --- | ---: | --- |
| Năm 2000 | F01–F02 | 2 | Rà soát và chuẩn trách nhiệm |
| IX, 2001 | F03–F12 + IX11–IX12 | 12 | Tham vấn/chỉ đạo; luân chuyển/giữ đội thí điểm |
| X, 2006 | X01–X12 | 12 | Vốn DNNN, mở cửa, giải ngân có điều kiện/cấp vốn trước |
| XI, 2011 | XI01–XI12 | 12 | Đất đai, nợ xấu, bất động sản đóng băng; tiền đề hồ sơ Biển Đông |
| XII, 2016 | XII01–XII12 | 12 | Phân quyền, điều phối, bảo vệ người thực thi và nhân sự |
| XIII, 2021 | XIII01–XIII12 | 12 | Biển Đông, khủng hoảng trái phiếu doanh nghiệp, dữ liệu và đối thoại |
| XIV, 2026 | XIV01–XIV12 | 12 | Xử lý tồn đọng, kiểm toán bàn giao, đội triển khai, kế cận |

Một lượt IX thực hiện khoảng 9 node vì F03/F04 cùng F05/F06 loại trừ theo tuyến, và IX11/IX12 là một lựa chọn. X/XI/XIII khoảng 11 node trước các gate tình huống; XII/XIV khoảng 9–10 khi đáp ứng thành tựu và tình huống. Đây là mục tiêu nhịp, cần đo số node thực sự khả dụng trong playtest.

Ở XII chỉ các cửa quy chế XII01/XII05 và hai kết quả chuyển giao XII04/XII08 loại trừ theo phương án. Các node trung gian và bốn hồ sơ chung không bị khóa thành toàn bộ cây phụ bốn focus. Phương án kiêm nhiệm cần roster phù hợp; người chơi giữ phân vai có lựa chọn công khai quyền hạn tương ứng tại XII11.

### 7.2. Gate theo kỳ và thời gian

`VIE_last_congress` lưu IX=9 đến XIV=14. Một focus cần kỳ tối thiểu, ngày neo, prerequisite và đúng chế độ. Điều kiện nằm trong `available`; AI dùng thêm trọng số riêng.

Ngày neo là ngày mở đại hội, còn node mở sau resolver đã giải quyết kỳ đó. Focus nền đã mở vẫn khả dụng ở kỳ sau; hợp đồng và nhân sự có cửa sổ riêng. Các node tương lai hiện mờ với tooltip ngày/kỳ.

**Ví dụ XI06 — tái cơ cấu nợ xấu:** kỳ đã giải quyết ≥11, ngày từ 12/01/2011, đã hoàn thành XI05 và có hồ sơ tín dụng. Gate năm 2011 là lựa chọn bối cảnh game; nội dung tham chiếu hoạt động xử lý nợ xấu và VAMC năm 2013, không khẳng định mọi hồ sơ đều xảy ra đúng cùng ngày. Phép ≥ trên biến dùng `compare = greater_than_or_equals` khi viết script. Nghĩa vụ trái phiếu doanh nghiệp nằm ở cụm XIII, gắn với biến động thị trường cuối 2022.

X01–X04 giữ chuỗi DNNN, X05–X08 giữ chuỗi mở cửa. XI01–XI04 là đất đai, XI05–XI08 là nợ xấu/bất động sản cùng tiền đề Biển Đông. XIII01–XIII04 là Biển Đông, XIII05–XIII08 là thị trường trái phiếu doanh nghiệp và quan hệ lớn. Node bổ sung nối vào hồ sơ thích hợp, không buộc làm hết hai cụm để mở mọi lựa chọn.

XII nâng cấp cách quyết định từ giai đoạn IX, không trao lại công cụ F03/F04. XIV kiểm tra kết quả và tồn đọng của kỳ trước, không yêu cầu đạt tier tối đa ở mọi lĩnh vực.

### 7.3. Nhịp focus và layout

- Focus phản hồi hoặc công bố: cost 3, khoảng 21 ngày cơ sở.
- Chính sách có một hành động chủ đạo: cost 5, khoảng 35 ngày.
- Mở chương trình lớn hoặc thương lượng nhiều bên: cost 7, khoảng 49 ngày.
- Cost 10 chỉ cân nhắc cho một bước ngoặt đặc biệt sau playtest; không tăng đồng loạt để bù số lượng.

Tính ngày dùng giả định 7 ngày/đơn vị trước modifier. Defines thực tế cần xác nhận lúc triển khai. Lát cắt 12 node được đưa về nhịp 3/5/7, một lượt mười focus khoảng **378 ngày cơ sở**; timer programme dùng mốc sớm 600/690 theo lĩnh vực và deadline 900 ngày.

Cây có sáu tầng theo đại hội và hai node mở đầu. Mỗi tầng có chính sách chung ở giữa, hai lựa chọn xử lý hồ sơ hai bên và node đánh giá phía dưới. Shortcut đưa tới kỳ hiện tại. Mission và decision cung cấp hoạt động giữa các tầng, còn focus tiếp tục mở vấn đề mới và hệ quả.

### 7.4. Danh mục 62 focus ngoài lát cắt

IX11/IX12 bổ sung cho gói IX; F03–F12 là mười node còn lại. Các mã bên dưới là nhãn thiết kế, chưa phải ID script. Gate mỗi dòng gồm kỳ đã giải quyết, ngày neo, chế độ và prerequisite. Cost 3/5/7 là 21/35/49 ngày cơ sở, cần xác nhận defines khi triển khai.

**IX — ngày neo 19/04/2001.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| IX11 | Luân chuyển cán bộ trong đợt thí điểm | 5 | IX đã giải quyết; từ 19/04/2001; F09; mọi chế độ; dự án đang chạy và roster có người thay; loại trừ IX12 | Event đổi người phụ trách dự án: 20 PP, cohesion +4 sau bàn giao, dự án +30 ngày; loại trừ IX12. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader X01: đọc người đã bàn giao và kiến nghị về người mới. |
| IX12 | Giữ người phụ trách đến nghiệm thu | 5 | IX đã giải quyết; từ 19/04/2001; F09; mọi chế độ; dự án đang chạy và có người phụ trách hợp lệ; loại trừ IX11 | Event giữ roster dự án: giữ tiến độ, mở yêu cầu kiểm toán độc lập 20 PP; loại trừ IX11. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader X04: đọc yêu cầu kiểm toán độc lập chưa đóng. |

### Đặc tả Lượt 2 cho 40 node

Cost focus giữ đúng danh mục đã chụp tại B1; gate dùng kỳ đã giải quyết, ngày neo, prerequisite dưới đây và chế độ ghi riêng cho từng node. “Mọi chế độ” là lựa chọn thiết kế, không thêm trigger mới. Mỗi caller là event/decision/milestone được mở bởi focus hoàn thành; mã kỹ thuật sẽ được đăng ký ở lượt 3. Giá PP/ngân khố từng lựa chọn lấy theo node từ `node_choice_prices` trong JSON B1; thời lượng triển khai lấy từ `node_choice_delays`. Tỷ giá k chỉ dùng để so sánh: `chi quy đổi = PP + ngân khố × k + cohesion mất × 3`; thời gian, dữ liệu, quyền hạn và quan hệ chính trị được ghi thành cơ hội/đánh đổi riêng, không quy thành PP.

**X — neo 18/04/2006; đầu tư công và doanh nghiệp nhà nước.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XI |
| --- | --- | ---: | --- | --- | --- |
| X01 | Công khai danh mục vốn nhà nước | 5 | X đã giải quyết; từ 18/04/2006; F07; mọi chế độ | Event phân loại danh mục. A: 20 PP để mở hồ sơ kiểm toán, giữ quyền truy cập nội bộ. B: 0,50 ngân khố để thuê đối chiếu độc lập, đổi lại công khai sớm và mất 30 ngày tiến độ. | Bộ/ngành và DNNN; XI đọc hồ sơ trách nhiệm còn thiếu trước khi phân loại nợ. |
| X02 | Tách bảo lãnh khỏi kế hoạch kinh doanh | 7 | X; từ 18/04/2006; X01; mọi chế độ | Decision chia rủi ro. A: 25 PP, giữ quyền điều phối của bộ chủ quản nhưng hoãn 60 ngày. B: 0,50 ngân khố cho kiểm toán tách biệt, đổi quyền tiếp cận dữ liệu của DNNN lấy báo cáo có thể dùng ở XI. | Bộ Tài chính và DNNN; XI thừa kế đánh dấu bảo lãnh đã tách/đang gộp. |
| X03 | Cổ phần hóa theo điều kiện công bố | 7 | X; từ 18/04/2006; X01; mọi chế độ | Event thương lượng với người mua. A: 30 PP để giữ điều khoản lao động và quyền phủ quyết, chấp nhận giảm số nhà đầu tư. B: 0,75 ngân khố cho định giá độc lập, nhường quyền chọn thời điểm bán để giữ bằng chứng định giá. | DNNN, người lao động và nhà đầu tư; XI nhận nghĩa vụ sau chuyển đổi để xét khi tài sản đóng băng. |
| X04 | Kiểm toán sau chuyển đổi sở hữu | 3 | X; từ 18/04/2006; X03; mọi chế độ | Milestone chọn phạm vi. A: 15 PP, kiểm tra hẹp và giữ kín hồ sơ; B: 0,50 ngân khố cho kiểm toán bên ngoài, công bố bất thường nhưng tiêu hao một lượt giám sát của bộ/ngành. | Cơ quan kiểm toán và DNNN; XI lưu cờ hồ sơ có/không có truy vết chủ sở hữu. |
| X05 | Công bố quy trình chấp thuận đầu tư | 5 | X; từ 18/04/2006; F07; mọi chế độ | Decision chốt cửa vào. A: 20 PP để giữ quyền xét riêng từng dự án, đổi lấy thời gian xử lý dài hơn; B: 0,50 ngân khố thiết lập tiêu chí công khai, mất quyền tùy nghi trong hồ sơ này. | Bộ/ngành và địa phương; XI dùng tiêu chí đã công bố làm chuẩn đối chiếu thu hồi đất. |
| X06 | Đàm phán tiêu chuẩn tiếp cận thị trường | 7 | X; từ 18/04/2006; X05; mọi chế độ | Event đối tác đưa điều kiện. A: 25 PP giữ ngoại lệ ngành, từ chối quyền xem dữ liệu nhà cung ứng; B: 0,75 ngân khố mở dữ liệu kiểm chứng, đổi lấy cam kết rà soát sau 90 ngày. | Đối tác và bộ/ngành; XI thừa kế quyền truy cập dữ liệu có điều kiện trong dự án đất. |
| X07 | Rà soát đầu tư tại ngành nhạy cảm | 7 | X; từ 18/04/2006; X05; mọi chế độ | Event chọn quy trình thẩm tra. A: 20 PP giữ quyền quyết định kín, chấp nhận mất một cửa sổ đàm phán; B: 0,50 ngân khố cho hội đồng thẩm tra, đổi quyền chủ trì của bộ kinh tế lấy biên bản dùng lại. | An ninh–quốc phòng và bộ/ngành; XI giữ hoặc mất tiền lệ chia sẻ hồ sơ nhạy cảm. |
| X08 | Phân định trách nhiệm quản lý dữ liệu | 3 | X; từ 18/04/2006; X06 hoặc X07; mọi chế độ | Decision phân quyền truy cập. A: 15 PP giữ dữ liệu tại bộ chủ quản, từ chối quyền liên thông cho địa phương; B: 0,50 ngân khố mở kho dùng chung, nhường quyền duyệt truy cập cho cơ quan kiểm toán. | Bộ/ngành và địa phương; XII đọc tiền lệ ai có quyền ký khi dữ liệu liên ngành bị tranh chấp. |

X09–X12 giữ nguyên nội dung, cost và loại trừ không đổi.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| X09 | Giải ngân vốn theo từng đợt kiểm chứng | 5 | X đã giải quyết; từ 18/04/2006; X02; mọi chế độ; có dự án vốn nhà nước và hồ sơ kiểm toán; loại trừ X10 | Decision chia hai đợt vốn, mỗi đợt cần checkpoint kiểm toán; loại trừ X10. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Mỗi đợt 0.25 ngân khố; tổng 0.50; không trả đợt sau trước checkpoint riêng. Reader XI05: đọc hai đợt vốn đã trả và checkpoint còn thiếu. |
| X10 | Cấp vốn trước cho dự án trọng điểm | 5 | X đã giải quyết; từ 18/04/2006; X02; mọi chế độ; có dự án vốn nhà nước và đủ ngân khố; loại trừ X09 | Event duyệt vốn trước: chi 0.50 ngân khố, rút 30 ngày dự án, mở kiến nghị giám sát; loại trừ X09. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XI05: đọc vốn ứng trước và kiến nghị giám sát. |
| X11 | Công khai bảo lãnh của doanh nghiệp | 7 | X đã giải quyết; từ 18/04/2006; X01; mọi chế độ; có hồ sơ bảo lãnh định danh | Event DNNN công bố nghĩa vụ: mở hồ sơ nợ và decision điều chỉnh bảo lãnh; bổ sung bằng chứng kiểm tra. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XI06: đọc bảo lãnh và nghĩa vụ nợ đã công bố. |
| X12 | Tổ chức đối thoại về điều kiện đầu tư | 5 | X đã giải quyết; từ 18/04/2006; X06 hoặc X07; mọi chế độ; có đối tượng đầu tư và điều kiện được đề nghị | Event bộ/ngành–doanh nghiệp: chọn giữ điều kiện hoặc mở có hậu kiểm; phản hồi đổi BoP ±0.05 một lần. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XI01: đọc điều kiện giữ hoặc mở cùng trách nhiệm hậu kiểm. |

**XI — neo 12/01/2011; đất đai, nợ xấu và tiền đề Biển Đông.** Mốc tham chiếu nợ xấu/bất động sản là giả định đặt trong nhiệm kỳ: văn bản Chính phủ năm 2013 nói rõ xử lý nợ xấu, hỗ trợ thị trường bất động sản và thành lập VAMC; sự kiện giàn khoan năm 2014 được đặt làm hồ sơ tiền đề cho XIII.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XII |
| --- | --- | ---: | --- | --- | --- |
| XI01 | Công bố hồ sơ thu hồi đất | 5 | XI đã giải quyết; từ 12/01/2011; F07; mọi chế độ | Event địa phương chọn mức công khai. A: 20 PP để giữ danh sách hộ trong phạm vi hẹp; B: 0,50 ngân khố lập sổ đối chiếu công khai, mất 30 ngày và trao quyền phản hồi cho người dân. | Địa phương, người dân và nhà đầu tư; XII thừa kế kiến nghị còn mở/đã đối chiếu. |
| XI02 | Lập quỹ đền bù trước triển khai | 7 | XI; từ 12/01/2011; XI01; mọi chế độ | Decision bố trí ngân sách. A: 0,75 ngân khố khóa quỹ cho hộ đủ hồ sơ, không dùng được cho dự án khác; B: 25 PP chọn chi theo tiến độ, đổi nguy cơ tranh chấp tồn tại. | Địa phương và người dân; XII mang theo khoản cam kết chưa giải ngân để giám sát. |
| XI03 | Mở phiên giải quyết tranh chấp đất | 7 | XI; từ 12/01/2011; XI01; mọi chế độ | Event chọn trọng tài. A: 20 PP cho phiên kín, giữ quyền quyết định ở tỉnh; B: 0,50 ngân khố mở phiên có biên bản, nhường một lượt chủ trì cho đại diện hộ bị ảnh hưởng. | Địa phương và người dân; XII ghi tiền lệ phiên kín/công khai khi đổi người đứng đầu. |
| XI04 | Kiểm tra nguồn thu từ đất | 3 | XI; từ 12/01/2011; XI01; mọi chế độ | Milestone truy khoản hụt. A: 15 PP rà soát nội bộ, giữ quyền truy cập sổ thu; B: 0,50 ngân khố cho đối chiếu liên ngành, mất 60 ngày nhưng mở dấu vết trách nhiệm. | Tài chính và địa phương; XII thừa kế hồ sơ chênh lệch hoặc xác nhận sổ khớp. |
| XI05 | Rà soát nợ xấu có tài sản bảo đảm là bất động sản | 5 | XI; từ 12/01/2011; XI01; mọi chế độ | Event xử lý hồ sơ tín dụng và tài sản khó thanh khoản. A: 20 PP ưu tiên giữ sổ vay tại ngân hàng, chấp nhận đình hoãn thu hồi; B: 0,50 ngân khố định giá chéo, công khai tài sản và mất 90 ngày xử lý. | Ngân hàng, doanh nghiệp vay và địa phương; XII dùng kết quả để phân biệt tái cơ cấu với kéo dài khoản nợ. |
| XI06 | Xử lý nợ xấu qua cơ chế mua bán nợ | 7 | XI; từ 12/01/2011; XI05; mọi chế độ | Decision chọn cách ghi nhận khoản nợ. A: 25 PP giữ khoản vay tại ngân hàng và quyền xử lý nội bộ; B: 0,75 ngân khố chuyển hồ sơ sang cơ chế mua bán nợ, đổi quyền thu hồi tức thời lấy kế hoạch xử lý theo kỳ. | Ngân hàng, cơ quan quản lý và doanh nghiệp vay; XII đọc được nợ đã chuyển giao hay còn treo. |
| XI07 | Xử lý dự án bất động sản đóng băng | 7 | XI; từ 12/01/2011; XI05; mọi chế độ | Event chọn đối tượng ưu tiên. A: 20 PP ưu tiên hoàn thiện dự án có người mua, từ bỏ quyền cứu chủ đầu tư; B: 0,50 ngân khố tái cơ cấu chủ đầu tư, giữ năng lực thi công nhưng hoãn bàn giao 60 ngày. | Người mua, doanh nghiệp và địa phương; XII thừa kế danh sách bàn giao dở dang và bên chịu trách nhiệm. |
| XI08 | Lập hồ sơ ứng phó sự cố giàn khoan | 3 | XI; từ 12/01/2011; XI07; mọi chế độ | Focus chỉ xếp event vào hàng đợi; event lịch sử chỉ mở từ 02/05/2014 theo B1, nếu focus hoàn thành muộn thì đọc lại hồ sơ. Event có mốc lịch sử 2014: nguồn Bộ Ngoại giao ghi nhận phát hiện giàn khoan ngày 01/05 và hạ đặt ngày 02/05/2014. A: 15 PP ưu tiên kênh trao đổi kín, giữ dư địa ngoại giao nhưng không mở dữ liệu cho bên thứ ba; B: 0,50 ngân khố lập hồ sơ chứng cứ công khai, mất 30 ngày nhưng tạo tiền lệ phối hợp chấp pháp. | Ngoại giao, an ninh–quốc phòng và cơ quan chấp pháp; XIII đọc tiền lệ trao đổi kín/công khai khi chọn kênh xử lý sự cố. |

XI09–XI12 giữ nguyên nội dung, cost và loại trừ; XI12 xử lý bảo lãnh tín dụng, không còn nhắc trái phiếu doanh nghiệp.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| XI09 | Lập quỹ xử lý dự án dở dang | 7 | XI đã giải quyết; từ 12/01/2011; XI07; mọi chế độ; có dự án dở dang và kiến nghị người mua; loại trừ XI10 | Decision chi 0.50 ngân khố cứu dự án theo kiến nghị người mua; loại trừ XI10. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XII10: đọc nghĩa vụ cứu dự án chưa nghiệm thu. |
| XI10 | Buộc dự án dở dang tái cơ cấu | 7 | XI đã giải quyết; từ 12/01/2011; XI07; mọi chế độ; có dự án dở dang và hồ sơ chủ đầu tư; loại trừ XI09 | Event chủ đầu tư và người mua chịu phương án tái cơ cấu: chậm 90 ngày, giữ ngân khố; loại trừ XI09. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XII10: đọc lịch tái cơ cấu và cam kết chưa bàn giao. |
| XI11 | Công khai kết quả thanh tra đất đai | 5 | XI đã giải quyết; từ 12/01/2011; XI04; mọi chế độ; có hồ sơ thanh tra đất đai và kiến nghị định danh | Công bố một hồ sơ cụ thể, đóng hoặc chuyển kiến nghị qua event dân vận; thưởng theo bằng chứng. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XII07: đọc kết luận và kiến nghị đã đóng hoặc chuyển. |
| XI12 | Kiểm tra trách nhiệm bên bảo lãnh tín dụng | 5 | XI đã giải quyết; từ 12/01/2011; XI06; mọi chế độ; có nghĩa vụ bảo lãnh và chứng cứ trách nhiệm | Event xác định bên chịu trách nhiệm; mở decision bồi hoàn có điều kiện và hậu quả đối với nhóm lợi ích. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Bồi hoàn chọn 20 PP hoặc 0.50 ngân khố; cùng nghĩa vụ, khác nguồn chi. Giá này thuộc XI12, không thuộc XII12. Reader XII07: đọc bên chịu trách nhiệm và bồi hoàn còn thiếu. |

**XII — neo 20/01/2016; phân quyền, trách nhiệm và chuyển giao.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XIII |
| --- | --- | ---: | --- | --- | --- |
| XII01 | Mở rộng quyền ký theo ủy quyền | 5 | XII đã giải quyết; từ 20/01/2016; XI08 hoặc F07; mọi chế độ; loại trừ XII05 | Decision chọn phạm vi ủy quyền. A: 20 PP giữ ký tập trung, mất thời gian xử lý; B: 0,50 ngân khố đào tạo đầu mối địa phương, nhường quyền ký hồ sơ chuẩn cho cấp dưới. | Bộ/ngành và địa phương; XIII đọc ai được ký hợp đồng kỹ thuật trong cửa sổ ngắn. |
| XII02 | Giao quyền phê duyệt kèm hậu kiểm | 7 | XII; từ 20/01/2016; XII01 hoặc XII05; mọi chế độ | Event chọn thứ tự kiểm soát. A: 25 PP giữ phê duyệt trước, làm chậm 60 ngày; B: 0,75 ngân khố lập hậu kiểm, đổi quyền chặn trước lấy trách nhiệm cá nhân sau ký. | Cơ quan kiểm tra và người thực thi; XIII dùng tiền lệ này khi hợp tác an ninh cần quyết nhanh. |
| XII03 | Công khai biên bản nghiệm thu cải cách | 7 | XII; từ 20/01/2016; XII02; mọi chế độ | Milestone chọn mức công khai. A: 15 PP công bố kết quả tổng hợp, giữ dữ liệu cá nhân; B: 0,50 ngân khố cho phép kiểm toán đọc hồ sơ gốc, giảm quyền sửa biên bản sau nghiệm thu. | Cơ quan kiểm toán và địa phương; XIII biết dữ liệu nào có thể chia sẻ ra ngoài. |
| XII04 | Chốt chuyển giao trước đại hội | 3 | XII; từ 20/01/2016; XII07; mọi chế độ; loại trừ XII08 | Event roster chọn bàn giao. A: 20 PP giữ nguyên người phụ trách thêm 30 ngày; B: 0,50 ngân khố tổ chức bàn giao ngay, mất một lượt đào tạo nhưng không kéo dài quyền của người cũ. | Văn phòng điều phối và người kế cận; XIII thừa kế hồ sơ có chủ mới/đang chờ bàn giao. |
| XII05 | Điều phối nhiều chương trình liên ngành | 5 | XII; từ 20/01/2016; XI08 hoặc F07; mọi chế độ; loại trừ XII01 | Decision chọn trung tâm điều phối. A: 25 PP để từng bộ tự quyết, từ bỏ quyền ưu tiên lịch chung; B: 0,75 ngân khố lập đầu mối chung, nhường quyền đặt lịch cho cơ quan điều phối. | Bộ/ngành và văn phòng điều phối; XIII dùng lịch chung hoặc phải thương lượng lại từng hợp đồng. |
| XII06 | Phê chuẩn phương án kiêm nhiệm dài hạn | 7 | XII; từ 20/01/2016; XII01 hoặc XII05; roster hợp lệ, mọi chế độ | Event chốt giám sát chức vụ. A: 20 PP giữ hai chức vụ nhưng công khai xung đột lịch; B: 0,50 ngân khố tách quy trình ký, trả bằng thêm bước xác nhận cho hồ sơ khẩn. | Lãnh đạo, văn phòng và cơ quan giám sát; XIII tier ký không được suy ra tự động từ việc kiêm nhiệm. |
| XII07 | Kiểm tra trách nhiệm người đứng đầu | 7 | XII; từ 20/01/2016; XII03 hoặc XII06; mọi chế độ | Event chọn chuẩn xem xét. A: 25 PP chỉ xử lý sai phạm rõ, giữ quyền miễn trừ quyết định thiện chí; B: 0,75 ngân khố mở kiểm tra độc lập, mất quyền đóng hồ sơ nội bộ. | Cơ quan kiểm tra và người thực thi; XIII có hoặc không có cơ chế bảo vệ quyết định có căn cứ. |
| XII08 | Bàn giao hai chức vụ theo kế cận | 3 | XII; từ 20/01/2016; XII07; roster hợp lệ, mọi chế độ; loại trừ XII04 | Event chọn tiến độ. A: 15 PP bàn giao theo thứ tự, mất 60 ngày nhưng giữ chuyên môn; B: 0,50 ngân khố bàn giao đồng thời, giảm gián đoạn nhưng cắt quyền truy cập của người cũ sớm. | Văn phòng và người kế cận; XIII giữ trạng thái phân vai/kiêm nhiệm làm điều kiện cửa sổ 25 ngày. |

XII09–XII12 giữ nguyên nội dung, cost và điều kiện.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| XII09 | Ban hành quy trình bảo vệ quyết định đúng | 7 | XII đã giải quyết; từ 20/01/2016; XII07; mọi chế độ; có người thực thi và hồ sơ quyết định cần bảo vệ | Mở lựa chọn thẩm định trách nhiệm trước ký trong E103 kế tiếp; phải hoàn thành đào tạo 90 ngày. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader E103: đọc chứng chỉ đào tạo trước khi mở thẩm định trách nhiệm. |
| XII10 | Đặt thời hạn xử lý hồ sơ liên ngành | 5 | XII đã giải quyết; từ 20/01/2016; XII02; mọi chế độ; có hồ sơ liên ngành tồn đọng | Decision xử lý một hồ sơ tồn đọng 180 ngày; chọn đầu mối hoặc hội đồng, trả PP/cohesion theo cách làm. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Đầu mối 30 PP; hội đồng 8 cohesion + 0.25 ngân khố; chỉ trả một cách, cả hai giữ 180 ngày. Reader XIII09: đọc đầu mối hoặc hội đồng chịu trách nhiệm hồ sơ. |
| XII11 | Công khai quyền hạn khi kiêm nhiệm | 5 | XII đã giải quyết; từ 20/01/2016; XII06; mọi chế độ; roster hợp lệ, phân vai hoặc kiêm nhiệm | Event giám sát roster kiêm nhiệm hoặc phân vai: công bố quyền hạn, mở checkpoint kiểm tra người đứng đầu. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XIII09: đọc quyền ký đã công khai và checkpoint giám sát. |
| XII12 | Thẩm định phương án thay người giữa nhiệm kỳ | 5 | XII đã giải quyết; từ 20/01/2016; XII07; mọi chế độ; roster có phương án thay người hợp lệ | Event tái phân công vai trò: lựa chọn bàn giao 60 ngày hoặc kiện toàn ngay với mất cohesion được công bố. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Bàn giao 60 ngày, không thêm phí; kiện toàn ngay mất 6 cohesion, chỉ khi roster thay thế hợp lệ. Reader XIII09: đọc bàn giao đang chờ hoặc kiện toàn đã trả cohesion. |

**XIII — neo 25/01/2021; Biển Đông và trái phiếu doanh nghiệp.** Cụm trái phiếu đặt trong thời kỳ có sự kiện thị trường: IMF ghi nhận phát hành dừng đột ngột từ cuối 2022 và thị trường đóng băng trong quý IV/2022. Các phản ứng trong node dưới đây là giả định gameplay, không mô tả hồ sơ hay tổ chức phát hành có thật. Focus có thể mở từ neo nhiệm kỳ, nhưng caller dùng bối cảnh khủng hoảng lịch sử chỉ chạy từ quý IV/2022; lựa chọn neo đầu quý là giả định gameplay, không khẳng định ngày khủng hoảng bắt đầu.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XIV |
| --- | --- | ---: | --- | --- | --- |
| XIII01 | Thiết lập kênh xử lý sự cố trên biển | 5 | XIII đã giải quyết; từ 25/01/2021; XI08; mọi chế độ | Event gọi lại hồ sơ giàn khoan XI. A: 20 PP duy trì trao đổi kín, không chia bản đồ hoạt động; B: 0,50 ngân khố chia sẻ tọa độ với đối tác, đổi quyền kiểm soát thông tin lấy cảnh báo sớm. | Ngoại giao và chấp pháp; XIV đọc kênh nào còn hoạt động khi rà hợp đồng kéo dài. |
| XIII02 | Giao nhiệm vụ phối hợp chấp pháp | 7 | XIII; từ 25/01/2021; XIII01; mọi chế độ | Decision chọn quyền chỉ huy. A: 25 PP để một cơ quan giữ lệnh, giảm linh hoạt địa phương; B: 0,75 ngân khố lập đầu mối liên ngành, nhường quyền chỉ huy riêng của từng lực lượng. | Chấp pháp và an ninh–quốc phòng; XIV thừa kế bản đồ trách nhiệm khi kiểm toán bàn giao. |
| XIII03 | Công bố lập trường tại diễn đàn khu vực | 7 | XIII; từ 25/01/2021; XIII01; mọi chế độ | Event chọn mức công khai. A: 15 PP công bố nguyên tắc chung, giữ chi tiết vận hành kín; B: 0,50 ngân khố công bố hồ sơ chứng cứ, mất dư địa đàm phán riêng nhưng tăng khả năng đối chiếu. | Ngoại giao và đối tác khu vực; XIV phải lưu hoặc giải mật hồ sơ đã công bố. |
| XIII04 | Bảo vệ hoạt động kinh tế biển | 3 | XIII; từ 25/01/2021; XIII02; mọi chế độ | Decision chia nguồn lực. A: 20 PP bảo vệ tuyến ưu tiên, bỏ bảo đảm cho tuyến phụ; B: 0,75 ngân khố lập cơ chế chia sẻ rủi ro, đổi chủ động điều phối lấy bảo vệ rộng hơn. | Ngư nghiệp, doanh nghiệp biển và chấp pháp; XIV đọc danh sách nghĩa vụ hỗ trợ còn hiệu lực. |
| XIII05 | Công khai nghĩa vụ trái phiếu doanh nghiệp | 5 | XIII; từ 25/01/2021; XIII03; mọi chế độ | Event xử lý hồ sơ nghĩa vụ đáo hạn; nếu dùng bối cảnh khủng hoảng lịch sử thì chỉ mở từ quý IV/2022 theo B1 (neo quý là giả định gameplay). A: 20 PP cho rà soát từng tổ chức phát hành, giữ dữ liệu nhà đầu tư hạn chế; B: 0,50 ngân khố lập sổ nghĩa vụ công khai, đổi quyền riêng tư hồ sơ lấy đối chiếu tập thể. | Bộ Tài chính, tổ chức phát hành và người mua; XIV nhận danh sách nghĩa vụ đã xác minh/chưa xác minh. |
| XIII06 | Đàm phán cơ cấu lại kỳ hạn | 7 | XIII; từ 25/01/2021; XIII05; mọi chế độ | Event thương lượng với chủ nợ. A: 25 PP để giữ hạn gốc và yêu cầu thanh toán đầy đủ; B: 0,75 ngân khố hỗ trợ hòa giải, đổi quyền đòi ngay lấy lịch trả nợ được chủ nợ chấp thuận. | Người mua trái phiếu, tổ chức phát hành và trung gian; XIV thừa kế hợp đồng được sửa hay đang tranh chấp. |
| XIII07 | Bảo vệ người mua trong phương án xử lý | 7 | XIII; từ 25/01/2021; XIII05; mọi chế độ | Decision chọn ưu tiên. A: 20 PP lập quỹ xử lý hồ sơ cá nhân, không cứu dự án; B: 0,50 ngân khố giữ dự án vận hành, chấp nhận người mua chờ lâu hơn và nhận quyền giám sát. | Người mua, doanh nghiệp và cơ quan quản lý; XIV kiểm tra cam kết đã hoàn thành hay còn chuyển kỳ. |
| XIII08 | Kiểm tra trách nhiệm bên phân phối và bảo lãnh | 3 | XIII; từ 25/01/2021; XIII06 hoặc XIII07; mọi chế độ | Milestone chọn phạm vi điều tra. A: 15 PP kiểm tra một hợp đồng, giữ quan hệ trung gian; B: 0,50 ngân khố đối chiếu toàn chuỗi, mất 60 ngày nhưng mở hồ sơ trách nhiệm cho kỳ sau. | Trung gian, ngân hàng và cơ quan kiểm tra; XIV thừa kế kết luận và nghĩa vụ khắc phục. |

XIII09–XIII12 giữ nguyên nội dung, cost và loại trừ; XIII09 vẫn có cửa sổ ký 25 ngày (giả định gameplay).

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| XIII09 | Công khai điều kiện hợp tác kỹ thuật | 5 | XIII đã giải quyết; từ 25/01/2021; XIII03; mọi chế độ; có hợp đồng kỹ thuật pending và phản hồi an ninh | Event đối tác–an ninh xác nhận quyền dữ liệu; mở hợp đồng hữu hạn nối tiếp E104, cửa sổ 25 ngày (giả định gameplay); tier 2 trở lên hoặc kiêm nhiệm có thể ký đúng hạn, tier 1 có phương án thu hẹp. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XIV11: đọc phạm vi dữ liệu và chữ ký trong cửa sổ. |
| XIII10 | Xử lý sự cố trên biển qua đối thoại | 5 | XIII đã giải quyết; từ 25/01/2021; XIII01; mọi chế độ; có hồ sơ sự cố và đối tác đối thoại; loại trừ XIII11 | Event đối tác chấp nhận hoặc từ chối kênh đối thoại; loại trừ XIII11 trong cùng hồ sơ sự cố. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XIV11: đọc đối tác chấp nhận hoặc từ chối kênh liên lạc. |
| XIII11 | Duy trì hiện diện chấp pháp sau sự cố | 7 | XIII đã giải quyết; từ 25/01/2021; XIII02; mọi chế độ; có hồ sơ sự cố và lực lượng chấp pháp hợp lệ; loại trừ XIII10 | Decision 180 ngày có ngân sách, sự kiện phản hồi và rủi ro tăng áp lực; loại trừ XIII10. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Ngân sách 0.50 ngân khố cho 180 ngày; phản hồi theo hồ sơ, không tự cộng thưởng chương trình. Reader XIV07: đọc cam kết hiện diện và phản hồi chưa xử lý. |
| XIII12 | Điều chỉnh hợp đồng sau cảnh báo an ninh | 5 | XIII đã giải quyết; từ 25/01/2021; XIII09; mọi chế độ; có cảnh báo an ninh đối với hợp đồng đang hiệu lực | Chọn sửa điều kiện dữ liệu hoặc hủy hợp đồng; trả giá mất hỗ trợ hoặc kéo dài xác minh. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Hủy không thu thêm phí; mất hỗ trợ E104 chưa nhận theo hợp đồng, không thu hồi khoản đã nhận hoặc tạo nợ âm. Sửa giữ điều kiện đối tác chấp nhận, không tự tạo hỗ trợ mới. Cổng bổ sung e104_contract_amendment_gate chỉ áp cho sửa tại XIII12: hỗ trợ chưa nhận>0 HOẶC quyền hợp tác chưa dùng>0. Cả hai0 thì sửa bị khóa; hủy luôn mở. Hủy chỉ đóng ledger/nghĩa vụ tương lai, không fail mission, không xóa bằng chứng đã hoàn tất, không mất tier/PP sớm/thưởng đã nhận. Giá/timer giữ nguyên. Reader XIV11: đọc điều kiện đã sửa hoặc hỗ trợ đã mất khi hủy. |

**XIV — neo 19/01/2026; nghiệm thu và bàn giao.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả sang XV giả định |
| --- | --- | ---: | --- | --- | --- |
| XIV01 | Áp chuẩn công vụ sau thí điểm | 5 | XIV đã giải quyết; từ 19/01/2026; XII07; mọi chế độ | Event chọn tiêu chuẩn. A: 20 PP công nhận theo hồ sơ cũ, giữ quyền đánh giá tại bộ; B: 0,50 ngân khố kiểm chứng độc lập, đổi quyền công nhận nhanh lấy tiêu chí công khai. | Bộ/ngành và người thực thi; XV biết chuẩn nào là chuẩn mặc định, chưa tự mở chức danh mới. |
| XIV02 | Công khai kết quả kiểm toán nhiệm kỳ | 7 | XIV; từ 19/01/2026; X04 hoặc XIII08; mọi chế độ | Resolver chọn hồ sơ. A: 25 PP công bố bản tóm tắt, giữ phụ lục nhạy cảm; B: 0,75 ngân khố công bố dữ liệu kiểm tra được, chấp nhận mở lại một kiến nghị chưa đóng. | Cơ quan kiểm toán và công chúng; XV đọc kiến nghị đang mở thay vì nhận kết luận sạch mặc định. |
| XIV03 | Nghiệm thu dịch vụ và đền bù | 7 | XIV; từ 19/01/2026; XI02 hoặc F05; mọi chế độ | Event địa điểm chọn người xác nhận. A: 15 PP nghiệm thu bởi cơ quan chủ quản, giữ thời gian bàn giao; B: 0,50 ngân khố mời đại diện người dùng, có thể phát sinh hồ sơ khắc phục. | Địa phương và người dân; XV thừa kế địa điểm đạt/chưa đạt cùng quyền yêu cầu sửa. |
| XIV04 | Bàn giao chương trình cho nhiệm kỳ mới | 3 | XIV; từ 19/01/2026; XIV02; mọi chế độ | Decision phân quyền tiếp nhận. A: 20 PP giữ nhóm cũ hỗ trợ, giảm quyền chủ động của nhóm mới; B: 0,50 ngân khố chuyển hồ sơ ngay, mất 30 ngày để xác nhận lại trách nhiệm. | Văn phòng điều phối và người kế nhiệm; XV đọc chủ sở hữu từng mission, không tự nhận mission đã xong. |
| XIV05 | Gia hạn chương trình chưa hoàn thành | 5 | XIV; từ 19/01/2026; XIV03; mọi chế độ; loại trừ XIV06 | Event chỉ mở nếu còn hồ sơ hợp lệ. A: 30 PP gia hạn hồ sơ triển khai 180 ngày, giữ kết quả programme partial và bỏ thưởng sớm; deadline programme 900 ngày không gia hạn; B: 0,75 ngân khố mời đơn vị kiểm chứng mới, mất quyền chọn mục tiêu thay thế trong lần gia hạn. | Địa phương và đơn vị thực hiện; XV nhận hạn tồn đọng có chủ thể chịu trách nhiệm, không nhận thưởng full. |
| XIV06 | Chuyển nguồn lực khỏi chương trình thất bại | 5 | XIV; từ 19/01/2026; XIV03; mọi chế độ; loại trừ XIV05 | Event đóng hồ sơ và phân bổ lại. A: 20 PP giữ nguồn lực cho cùng mục tiêu, chấp nhận chậm 90 ngày; B: 0,50 ngân khố chuyển sang mục tiêu khác, mất tính liên tục của hồ sơ cũ. | Bộ/ngành và địa phương; XV đọc nguyên nhân đóng và không thể tính lại hồ sơ cũ là thành công. |
| XIV07 | Kiểm toán kết quả bàn giao | 7 | XIV; từ 19/01/2026; XIV02; mọi chế độ | Decision chọn mẫu. A: 25 PP kiểm tra hồ sơ có rủi ro cao, giữ thời gian; B: 0,75 ngân khố kiểm tra ngẫu nhiên, giảm khả năng chọn hồ sơ nhưng tăng phát hiện lệch báo cáo. | Cơ quan kiểm toán và đơn vị bàn giao; XV nhận dấu vết mẫu đã kiểm tra và các điểm chưa lấy mẫu. |
| XIV08 | Giữ nhóm chuyên môn qua chuyển giao | 5 | XIV; từ 19/01/2026; XIV04; mọi chế độ; loại trừ XIV09 | Event chọn giữ tri thức. A: 25 PP giữ nhóm hiện tại, giảm 30 ngày gián đoạn dự án như giá/hiệu quả trước Lượt 2; B: 0,50 ngân khố lập hồ sơ bàn giao, giải tán nhóm cũ sớm và giảm quyền tiếp cận của họ. | Nhóm chuyên môn và lãnh đạo mới; XV biết chọn giữ người hay giữ hồ sơ, không tự cộng cả hai lợi ích. |

XIV09–XIV12 giữ nguyên nội dung, cost và loại trừ; XIV11 vẫn có cửa sổ ký 21 ngày ở một node muộn, còn XV là giả định gameplay.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| XIV09 | Thay nhóm triển khai sau kiểm toán | 5 | XIV đã giải quyết; từ 19/01/2026; XIV04; mọi chế độ; có kết luận kiểm toán và đội thay thế hợp lệ; loại trừ XIV08 | Event đổi đội phụ trách: dự án +30 ngày, xử lý kiến nghị nhân sự theo chứng cứ; loại trừ XIV08. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XIV12: đọc roster mới và phần bàn giao chậm. |
| XIV10 | Công khai cam kết dịch vụ đã nghiệm thu | 3 | XIV đã giải quyết; từ 19/01/2026; XIV03; mọi chế độ; có nghiệm thu tương ứng và phản hồi địa phương | Event địa phương phản hồi cam kết; trao idea ổn định 365 ngày chỉ khi đã có nghiệm thu tương ứng. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Idea ổn định +1% trong 365 ngày; trần 1%; không cộng chồng tier dân vận: dùng max(thưởng tier, idea). Chỉ nhận sau nghiệm thu cùng địa điểm, một lần/địa điểm/epoch; refresh thay thế, không cộng thời hạn. Reader XIV12: đọc cam kết dịch vụ đã công khai, không cộng lại thưởng. |
| XIV11 | Rà soát hợp đồng có nghĩa vụ kéo dài | 5 | XIV đã giải quyết; từ 19/01/2026; XIV02; mọi chế độ; có hợp đồng còn nghĩa vụ và phản hồi đối tác | Mở danh sách hợp đồng đang hiệu lực và lựa chọn giữ, sửa hoặc chấm dứt với giá có thật; hồ sơ gia hạn có cửa sổ 21 ngày (giả định gameplay), tier 3 hoặc kiêm nhiệm ký kịp, các tier thấp hơn chọn sửa/chấm dứt. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Giữ 15 PP; sửa 0.50 ngân khố; chấm dứt mất hỗ trợ chưa nhận. Giữ chỉ khả dụng nếu ký kịp cửa sổ 21 ngày; sửa cần đối tác đồng ý, không tự gia hạn ký. Reader XIV12: đọc hợp đồng giữ, sửa hoặc chấm dứt cùng hỗ trợ còn lại. |
| XIV12 | Chốt phương án chuyển giao năm 2031 | 7 | XIV đã giải quyết; từ 19/01/2026; XIV04; mọi chế độ; có hồ sơ bàn giao và phương án roster kế tiếp | Event chuẩn bị roster kế tiếp, kiểm tra kiêm nhiệm và kế cận; tạo phương án cho XV giả định, chưa tự thay người. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader archive_XV: lưu phương án cho XV giả định; không tự đổi người hoặc thêm focus. |


### 7.4a. Quyền và cơ hội có consumer cụ thể

Đổi hậu quả chỉ mô tả thành gate hành động đọc được. Mỗi hồ sơ lưu đúng một lựa chọn A/B theo node/đối tượng/epoch. Khi reader xử lý đúng hồ sơ, hành động tương ứng có available=1, hành động đối ứng=0; không mở cả hai và không thu lại phí đã trả. Đây là nhánh của caller hiện có, không thêm focus, event hay currency. Quyền không tự cộng tier, bằng chứng, thưởng PP hoặc rút timer ký. Thời gian ở bảng áp vào hồ sơ/dự án tương ứng, không tự cộng vào chuỗi programme độc lập. Gate điều kiện thực tế của reader vẫn áp dụng.

Mỗi hành động là một cơ hội mang tên riêng; script so tập quyền theo quan hệ bao hàm, không cộng số quyền thành điểm. I10 kiểm cả hai nhu cầu hành động tại từng node, mọi tuyến/k, rồi đối chiếu ma trận programme. Không có một lựa chọn thắng tất cả nếu nó khóa hành động đối ứng mà đối thủ mở. Đây là kết luận của mô hình giấy, không chứng minh AI hay game thực thi đúng.

`archive_XV` là nhãn lưu trữ cho XV giả định: lưu cả hai loại hồ sơ khác nhau, không tính là cơ hội sử dụng được trong phạm vi 2026 và không thêm node XV. Các quyền XIV chỉ dùng để kiểm khác biệt hồ sơ bàn giao, không được dùng để tăng opportunity_count hiện tại.

| Node | Reader | Hành động nếu A (B khóa) | Hành động nếu B (A khóa) | Timer đã có |
| --- | --- | --- | --- | --- |
| X01 | XI05 | rà soát hồ sơ vốn nội bộ | đối chiếu vốn bằng bản công khai | B: 30 ngày |
| X02 | XI06 | bộ chủ quản điều phối bảo lãnh | dùng báo cáo bảo lãnh tách biệt | A: 60 ngày |
| X03 | XI07 | áp điều khoản lao động và phủ quyết đã giữ | dùng định giá độc lập khi xử lý tài sản | Theo quyền, không tự gán thêm timer |
| X04 | XI12 | thẩm tra chủ sở hữu trong phạm vi nội bộ | truy vết chủ sở hữu qua kiểm toán ngoài | Theo quyền, không tự gán thêm timer |
| X05 | XI01 | xét ngoại lệ đầu tư theo từng hồ sơ | đối chiếu thu hồi đất theo tiêu chí công khai | Theo quyền, không tự gán thêm timer |
| X06 | XI03 | bảo lưu ngoại lệ ngành đã đàm phán | đọc dữ liệu nhà cung ứng theo cam kết rà soát | B: 90 ngày |
| X07 | XI08 | giữ quyền thẩm tra kín hồ sơ nhạy cảm | dùng tiền lệ chia sẻ hồ sơ với hội đồng | Theo quyền, không tự gán thêm timer |
| X08 | XII10 | bộ chủ quản tự duyệt truy cập hồ sơ | cơ quan kiểm toán duyệt liên thông hồ sơ | Theo quyền, không tự gán thêm timer |
| XI01 | XII07 | xem danh sách hộ trong phạm vi cơ quan | đối chiếu kiến nghị người dân qua sổ công khai | B: 30 ngày |
| XI02 | XII10 | giải ngân từ quỹ đã khóa cho hộ đủ hồ sơ | giữ ngân sách chưa khóa và xét cam kết theo tiến độ | Theo quyền, không tự gán thêm timer |
| XI03 | XII12 | tỉnh chủ trì xử lý theo biên bản kín | đại diện hộ bị ảnh hưởng chủ trì phiên có biên bản | Theo quyền, không tự gán thêm timer |
| XI04 | XII07 | địa phương tự kiểm sổ thu đã giữ | cơ quan kiểm tra truy trách nhiệm từ sổ liên ngành | B: 60 ngày |
| XI05 | XII10 | ngân hàng tiếp tục xử lý khoản vay nội bộ | đối chiếu tài sản từ định giá chéo công khai | B: 90 ngày |
| XI06 | XII10 | ngân hàng trực tiếp quyết thu hồi khoản vay | đọc kế hoạch xử lý theo kỳ của hồ sơ đã chuyển | Theo quyền, không tự gán thêm timer |
| XI07 | XII10 | yêu cầu bàn giao theo danh sách người mua ưu tiên | dùng năng lực thi công của chủ đầu tư được tái cơ cấu | B: 60 ngày |
| XI08 | XIII01 | tái sử dụng kênh trao đổi kín | tái sử dụng hồ sơ chứng cứ công khai | B: 30 ngày |
| XII01 | XIII09 | đầu mối trung ương ký hồ sơ chuẩn | đầu mối địa phương ký hồ sơ chuẩn | Theo quyền, không tự gán thêm timer |
| XII02 | XIII09 | thẩm định trách nhiệm trước khi ký | ký theo hậu kiểm với trách nhiệm cá nhân | A: 60 ngày |
| XII03 | XIII09 | chia sẻ bản tổng hợp giữ dữ liệu cá nhân kín | cho đối tác kiểm toán đọc hồ sơ gốc | Theo quyền, không tự gán thêm timer |
| XII04 | XIII09 | nhóm cũ hỗ trợ hồ sơ trong bàn giao tuần tự | chủ mới tự xác nhận trách nhiệm khi đã bàn giao | A: 30 ngày |
| XII05 | XIII09 | từng bộ thương lượng lịch hợp đồng riêng | đầu mối chung đặt lịch hợp đồng liên ngành | Theo quyền, không tự gán thêm timer |
| XII06 | XIII09 | ký theo roster kiêm nhiệm đã công khai xung đột | ký tách quy trình với xác nhận độc lập | Theo quyền, không tự gán thêm timer |
| XII07 | XIII12 | yêu cầu miễn trừ quyết định thiện chí có căn cứ | mở kiểm tra độc lập mà cơ quan nội bộ không đóng được | Theo quyền, không tự gán thêm timer |
| XII08 | XIII09 | nhóm cũ truy cập hồ sơ trong bàn giao tuần tự | chủ mới truy cập độc quyền hồ sơ bàn giao đồng thời | A: 60 ngày |
| XIII01 | XIV11 | duy trì liên lạc kín không chia tọa độ | nhận cảnh báo sớm qua tọa độ đã chia sẻ | Theo quyền, không tự gán thêm timer |
| XIII02 | XIV07 | cơ quan chủ lệnh tự điều phối lực lượng | đầu mối liên ngành phối hợp theo bản đồ trách nhiệm | Theo quyền, không tự gán thêm timer |
| XIII03 | XIV11 | thương lượng riêng với chi tiết vận hành kín | giải mật và đối chiếu chứng cứ đã công bố | Theo quyền, không tự gán thêm timer |
| XIII04 | XIV07 | ưu tiên tuyến chính theo quyền điều phối riêng | thực hiện nghĩa vụ chia sẻ rủi ro cho tuyến phụ | Theo quyền, không tự gán thêm timer |
| XIII05 | XIV02 | rà soát nghĩa vụ của từng tổ chức phát hành | đối chiếu nghĩa vụ bằng sổ công khai | Theo quyền, không tự gán thêm timer |
| XIII06 | XIV11 | yêu cầu thanh toán theo hạn gốc | thực hiện lịch trả nợ đã được chủ nợ đồng ý | Theo quyền, không tự gán thêm timer |
| XIII07 | XIV03 | xử lý hồ sơ của từng người mua | giám sát dự án còn vận hành theo cam kết | Theo quyền, không tự gán thêm timer |
| XIII08 | XIV02 | duy trì quan hệ trung gian khi kiểm một hợp đồng | mở trách nhiệm toàn chuỗi phân phối và bảo lãnh | B: 60 ngày |
| XIV01 | archive_XV | bộ tự công nhận chuẩn theo hồ sơ cũ | đơn vị độc lập công nhận theo tiêu chí công khai | Theo quyền, không tự gán thêm timer |
| XIV02 | archive_XV | lưu bản tổng hợp và phụ lục hạn chế | xử lý kiến nghị được mở lại từ dữ liệu công khai | Theo quyền, không tự gán thêm timer |
| XIV03 | archive_XV | cơ quan chủ quản xác nhận địa điểm nghiệm thu | đại diện người dùng yêu cầu khắc phục địa điểm | Theo quyền, không tự gán thêm timer |
| XIV04 | archive_XV | nhóm cũ hỗ trợ tiếp nhận mission | nhóm mới tự xác nhận trách nhiệm mission | B: 30 ngày |
| XIV05 | archive_XV | tiếp tục hồ sơ cũ trong thời hạn gia hạn | đơn vị mới kiểm chứng đúng mục tiêu đã khóa | A: 180 ngày |
| XIV06 | archive_XV | giữ nguồn lực cho mục tiêu cũ chưa đạt | dùng nguồn lực đã chuyển cho mục tiêu thay thế | A: 90 ngày |
| XIV07 | archive_XV | chủ động chọn hồ sơ rủi ro cao để kiểm | đối chiếu mẫu ngẫu nhiên đã được khóa | Theo quyền, không tự gán thêm timer |
| XIV08 | archive_XV | nhóm chuyên môn cũ tiếp tục hỗ trợ dự án | nhóm mới tự dùng hồ sơ bàn giao không phụ thuộc nhóm cũ | A: -30 ngày |

Các giá/hiệu quả mới của22node là **giả định gameplay, chưa cân bằng bằng engine**. Giữ cost và loại trừ; không dùng giá mới để thay timer/deadline/giá programme. Bảng đối chiếu và biên giá ở báo cáo Lượt3.

### 7.4b. I3 Pareto chỉ cho XII12 và XIII12

I3 của XII12 và XIII12 được đánh giá bằng Pareto, không bằng chi phí tiền đơn lẻ, theo xác nhận người dùng: chúng đổi thời gian/roster hoặc quyền hỗ trợ/nghĩa vụ đang có. Mọi node/event khác giữ phép kiểm chi phí quy đổi trực tiếp. Không quy ngày/quyền thànhPP, không thêm thưởng hay đổi timer. Available và tooltip đọc `i3_pareto_exceptions`/record hồ sơ: phí, bàn giao/khóa roster, cohesion mất, quyền người cũ/người mới, hỗ trợ chưa nhận bị mất, quyền hợp tác chưa dùng, nghĩa vụ hợp đồng mở. Hủy không thu hồi hỗ trợ đã nhận và không xóa lịch sử trách nhiệm.

| Node | Bối cảnh | k | Option | Chi quy đổi | Chiều ngoài tiền | Trạng thái | Cổng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XII12 | roster hợp lệ | 20 | A | 0 | handover_pending_days=60; cohesion_loss=0; old_holder_access=1; new_holder_authority=0 | pending_handover | MỞ |
| XII12 | roster hợp lệ | 20 | B | 18 | handover_pending_days=0; cohesion_loss=6; old_holder_access=0; new_holder_authority=1 | replacement_effective | MỞ |
| XII12 | roster hợp lệ | 40 | A | 0 | handover_pending_days=60; cohesion_loss=0; old_holder_access=1; new_holder_authority=0 | pending_handover | MỞ |
| XII12 | roster hợp lệ | 40 | B | 18 | handover_pending_days=0; cohesion_loss=6; old_holder_access=0; new_holder_authority=1 | replacement_effective | MỞ |
| XII12 | roster hợp lệ | 60 | A | 0 | handover_pending_days=60; cohesion_loss=0; old_holder_access=1; new_holder_authority=0 | pending_handover | MỞ |
| XII12 | roster hợp lệ | 60 | B | 18 | handover_pending_days=0; cohesion_loss=6; old_holder_access=0; new_holder_authority=1 | replacement_effective | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 20 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 40 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 60 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 20 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 40 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 60 | B | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 20 | B | 5.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 40 | B | 10.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 60 | B | 15.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 20 | B | 5.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 40 | B | 10.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 60 | B | 15.0 | unreceived_support_lost=0.25; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 20 | B | 15.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 40 | B | 30.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=0; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 60 | B | 45.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 20 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 20 | B | 15.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 40 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 40 | B | 30.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 60 | A | 0 | unreceived_support_lost=0; unused_cooperation_access=1; contract_obligation_open=1 | modified_active_if_partner_accepts | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 60 | B | 45.0 | unreceived_support_lost=0.75; unused_cooperation_access=0; contract_obligation_open=0 | terminated | MỞ |

Script kiểm63cặp mọi tuyến/k; có0cặp thống trị còn khả dụng, 0gần trùng. Bảng Δtừng chiều và so cặp ở báo cáoLượt3; near=mọi |B−A|/max(|A|,|B|)<10%, cả hai0 tính0%. XIII12 không còn hỗ trợ/quyền hợp tác: sửa (phương án bị thống trị) bị khóa theo cổng mới; hủy vẫn mở. Các9phép so của trạng thái này PASS cổng: chỉ còn1phương án, không được tuyên bố đã cân bằng2phương án. Các trạng thái còn lợi ích giữ2phương án và kiểm Pareto riêng.

### 7.5. Điều kiện hoàn thiện sau playtest

74 là danh mục thiết kế có nội dung, chưa phải 74 node đã cân bằng hoặc triển khai. Trước hết làm lát cắt; sau đó dựng từng gói nhiệm kỳ, kiểm tra mỗi focus có caller, tool hoặc hậu quả thực thi.

Đo khoảng 90 ngày một lần: node khả dụng, node bị khóa theo lựa chọn, hồ sơ đang chạy, và vấn đề người chơi còn cần giải quyết. Nếu thiếu lựa chọn thì thay nội dung node hiện có với gate, prerequisite và effect riêng; tổng giữ đúng 74. Nếu một node lặp chức năng, thay nội dung node đó, không thêm hoặc gộp làm đổi tổng.

Nhịp mong muốn khoảng 10 lựa chọn thực hiện đáng cân nhắc mỗi nhiệm kỳ. Danh mục giữ đúng 74 node, chỉ thay nội dung theo dữ liệu; số node lớn không thay thế kiểm tra chất lượng. Các lần thử XII và XIV phải kiểm tra riêng việc người chơi có quá ít node dù toàn tầng có 12.

## 8. Kiến trúc kỹ thuật và dữ liệu

| Lớp | Trách nhiệm |
| --- | --- |
| Focus | Chính sách, caller và tool chuyên sâu |
| Decision | Thu PP/tiền, chọn mode, triển khai |
| Mission | Deadline và milestone |
| Event | Xung đột, cửa sổ cơ hội, phản hồi |
| Trigger | Cùng điều kiện cho requirement và UI |
| Resolver | Chấm và trao kết quả một lần |
| Idea/DM | Tier và di sản hữu hạn |
| Adapter | Roster, mode ký và phần hiển thị |
| Scheduler | Đại hội, E103/E104, kiểm chứng bounded |
| GUI | Giá, hạn, kết quả dự kiến và source dữ liệu |

File dự kiến giữ cách chia: focus, decisions/categories, political_effects/triggers, ideas, dynamic_modifiers, bop, traits, on_actions, events và English localisation dưới các thư mục game tương ứng. Identifier mới phải định nghĩa và xác minh trước triển khai.

### 8.1. Nguồn chân lý

| Dữ liệu | Nơi lưu |
| --- | --- |
| BoP | Engine BoP, ID thiết kế `VIE_leadership_balance`; resolver khởi tạo, checkpoint thay đổi, gate và UI đọc |
| Cohesion | `VIE_leadership_cohesion` |
| Đại hội đã giải quyết | `VIE_last_congress` |
| Nhân sự | `VIE_office_holders` |
| Trọng tâm | Một idea chương trình |
| Tier | Idea tier 0–3 |
| Mission đang chạy | Mission |
| Chương trình đã trả kết quả | Epoch của kỳ và `VIE_last_resolved_program` |
| Baseline | GDP/corruption lúc bắt đầu |
| Milestone | Lịch sử hành động định danh |
| Mode và timer đã ký | Dữ liệu nhiệm vụ, chốt lúc bắt đầu |
| Kiến nghị | Milestone mở/đã giải quyết |
| Chuỗi 90 ngày | Bộ đếm của điều kiện cần kiểm chứng |
| Hợp đồng E103/E104 | Pending/kết quả lịch sử và deadline |
| Event đã xếp hàng | Pending guard |
| Dự án phụ đã nhận trong kỳ | `VIE_last_side_project_epoch`, ghi tại nhận; mission phụ lưu deadline chuẩn bị đại hội sau, mục tiêu và kết quả |

Bỏ hai slot ưu tiên và hồ sơ hao mòn. Kiêm nhiệm query roster; phase query mission. Dữ liệu thời hạn hợp đồng cần giữ vì đó là một cơ hội lịch sử không truy vấn từ focus hoàn thành.


**Đăng ký nhãn và dữ liệu Lượt 3 (thiết kế, chưa là định nghĩa engine):**

| Nhãn / nhóm đã dùng | Writer / caller | Reader và vòng đời |
| --- | --- | --- |
| F01–F12 và các slug ở 6.2 | Focus completion; 12 slug là alias thiết kế, chưa tự thêm prefix hoặc namespace | Gate focus, mở công cụ và resolver; cost/tên tại `focus_nodes` của B1 |
| IX11–IX12; X01–X12; XI01–XI12; XII01–XII12; XIII01–XIII12; XIV01–XIV12 | Focus completion mở caller được mô tả ở 7.4; nhãn node không phải ID script đã xác minh | Lưu lựa chọn A/B và đối tượng hồ sơ theo node/epoch; kỳ sau đọc cùng đối tượng, không reset lịch sử khi bắt đầu programme mới |
| E101–E104 | F05; F06 hoặc khởi động kiểm toán; scheduler programme; phản hồi hợp đồng E102 | Giá trong B1 `e101`–`e104`; pending và trạng thái hợp đồng riêng, resolver chỉ chạy một lần theo epoch; đây là nhãn event thiết kế |
| `VIE_leadership_cohesion` | Khởi tạo, checkpoint, phục hồi, resolver | Gate/giá/kiểm chứng liên tục đọc; clamp theo B1 |
| `VIE_last_congress` | Resolver đại hội ghi kỳ đã giải quyết | Focus, scheduler và guard đọc; không reset khi đổi programme |
| `VIE_office_holders` | Adapter kiện toàn hoặc phân vai | GUI và truy vấn kiêm nhiệm đọc; thay holder theo roster hợp lệ, không nhân đôi trait |
| `VIE_last_resolved_program` | Resolver ghi epoch trước trao thưởng | Guard F12/timeout/load đọc; epoch cũ lưu để chống thưởng lại |
| `VIE_last_side_project_epoch` | Ghi epoch khi nhận dự án phụ trước thu phí | Gate nhận lại đọc, không clear khi hủy; kết quả mission phụ tách riêng |
| Baseline, mode/timer, counter, kiến nghị, hợp đồng, lựa chọn node và bộ nhớ trung tâm | Dữ liệu nhiệm vụ/hồ sơ được chốt khi bắt đầu hoặc khi người chơi chọn | Giữ record node/đối tượng/epoch, kết quả, giá đã trả, hạn và quyền dữ liệu; kỳ sau chỉ đọc record liên quan. Chưa gán thêm tên biến/flag/idea kỹ thuật; phải định danh và kiểm provider trước code |
| `forecast_programme_completion` | Trigger thiết kế; Python cùng tên là nguồn tính dự báo duy nhất cho CSV/available/tooltip | Đọc timer/mode đã ký, chuẩn bị tại start, trễ tất định đã biết; xuất ngày/dự phòng/cổng. Rủi ro E103-A chưa hiện thực chỉ cảnh báo; chưa là trigger engine |
| `node_opportunity_effects`; `legacy_node_specs`; `legacy_node_terms`; `archive_XV` | Focus/caller đã có ghi record node/đối tượng/epoch và phí một lần | Reader ở7.4/7.4a đọc; quyền đối ứng khóa, archive chỉ lưu không trao gameplay; giá mới là giả định gameplay |
| `i3_pareto_exceptions` | Caller XII12/XIII12 đọc record roster/hợp đồng đã có | Lưu lựa chọn/trạng thái theo đối tượng/epoch, chiều/biên ở7.4b; Pareto chỉ hai node, tooltip trước chọn; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `focus_commitment_gate`; elapsed_congress_days; recovery_cooldown_remaining; pending_recovery_remaining | Scheduler đại hội/decision cập nhật tuổi cửa sổ, cooldown và lượt phục hồi purpose=cohesion đang chạy | Cùng forecast_programme_completion trả focus_available, earliest_feasible_start_day, latest_start_day, start_days_short cho available/tooltip/AI; cổng chung bất kỳ programme, cổng lựa chọn programme đích; không là trigger engine mới |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |

Registry này đóng phạm vi các ID/nhãn đã viết, không chứng minh tồn tại API hoặc định nghĩa trong game. Giá lựa chọn ở `node_choice_prices`/`legacy_node_terms`, timer ở `node_choice_delays`, gate/caller22node ở `legacy_node_specs`, consumer quyền ở `node_opportunity_effects`, lịch sử ở `l2_history_anchors` của B1. Quyền đọc theo đúng node/đối tượng/epoch; available=1 cho hành động đã chọn, 0 cho đối ứng; không cộng điểm quyền và không trao kết quả tự động.

### 8.2. Kiểm chứng 90 ngày và tránh lách

Trong phase nghiệm thu, hook theo ngày chỉ kiểm tra VIE khi đúng chương trình hoạt động. Mỗi điều kiện cần chuỗi 90 ngày liên tục: đạt thì tăng counter, không đạt thì reset. Khi counter đủ 90, ghi milestone lịch sử và kết thúc kiểm chứng.

Cán bộ theo dõi cohesion; công vụ theo dõi thu/chi; kiểm tra ở baseline đáy theo dõi giữ mức corruption thấp nhất. Các counter chỉ tồn tại trong phase liên quan. Phương án này thêm vài check trên một nước, không quét toàn quốc.

Chỉ tiêu từ hoạt động bắt buộc và lịch sử 90 ngày không được thay bằng ảnh chụp đúng ngày chấm. GDP không thay thế nghiệm thu dự án.

### 8.3. Resolver và phạm vi thưởng

- Resolver đại hội guard kỳ, kiểm tra chế độ, ghi kết quả và kiện toàn.
- Adapter nhân sự kiểm tra tổ hợp vai trò, áp hiệu ứng theo người và đợt chuyển giao.
- Resolver programme guard epoch, chấm 4 nhóm, tính mốc sớm theo chương trình 600/690 và kết quả hợp đồng E103, ghi kết quả trước thưởng.
- Review sớm chỉ chốt full; nếu chưa đủ, mission tiếp tục.
- E103/E104 có guard hợp đồng riêng; resolver chúng không ghi programme đã hoàn thành.
- Một programme full được +50 PP sớm tối đa một lần; gọi lại F12, load save hay đến timeout không trao lại.
- Di sản một cửa +tier công vụ được kiểm kê riêng: tối đa -2% dự án một lần và -6% tier.

Programme, deadline, mode và giá được tính khi bắt đầu; expiry timed idea không tự tạo success reward. Dự án phụ ghi guard nhận theo epoch trước thu PP, không mở lại sau hủy; resolver phụ chỉ trao idea khi mục tiêu đạt, timeout/cancel không thưởng.

## 9. Tham chiếu chéo và ID đã xác minh

Bỏ nội dung cũ là thay gameplay, còn các nước khác và hệ thống chung vẫn cần giao diện hợp lệ. Những tham chiếu đã tìm thấy:

| Người gọi/đọc | Tham chiếu và bằng chứng | Hướng xử lý khi triển khai |
| --- | --- | --- |
| History Lào | `lao_vietnan_treaty`, `history/countries/LAO - Laos.txt:80` | Giữ hoặc thiết kế lại giao diện song phương; đổi cả hai caller khi đổi ID |
| Spirit ASEAN | `socialist_vietnam`, `lao_vietnan_treaty`, `common/ideas/asean.txt:48`, `:63` | Kiểm kê điều kiện chế độ và nơi cấp idea trước khi loại |
| On action Việt Nam | Gọi `vietnam.1` dựa trên spirit cũ, `common/on_actions/99_VIE_on_actions.txt:5` | Thay caller cùng nội dung mới, loại logic cũ hết người dùng |
| Dispatcher toàn cục | `set_leader_[TAG]`, `common/scripted_effects/00_leader_setup_scripted_effects.txt:20` | Adapter mới đáp ứng lối gọi nhân sự chung |
| Focus Ấn Độ | Gate theo các trigger cộng sản rồi gửi event cho VIE, `common/national_focus/05_india.txt:11776` | Kiểm tra mapping chế độ mới vẫn cho tuyến hợp tác mong muốn |
| Focus Trung Quốc | Gửi `china_scs.10/.30/.50`, cấp spirit áp lực, `common/national_focus/05_china.txt:9850`, `:10086`, `:10139`, `:10413` | Giữ tiếp nhận xung đột Biển Đông hoặc cập nhật event theo cơ chế mới |
| Focus Trung Quốc | Áp lực Mekong với VIE/LAO/CAM, `common/national_focus/05_china.txt:15624` | Kiểm tra việc nhận modifier/opinion sau thay nội dung |
| Country groups | VIE trong nhóm toàn cục, `common/scripted_triggers/MD_Country_Groups_Triggers.txt:500`, `:1057` | Giữ nhận diện quốc gia và vai trò khu vực |

Đây là kiểm kê ban đầu, chưa phải audit toàn bộ repository. Đã tìm thấy trực tiếp một shared idea trong history Lào; chưa xác minh hết caller Campuchia hoặc các namespace quốc tế.

Audit triển khai phải lập danh sách **định nghĩa, caller, reader, scope, điều kiện chế độ và cách thay thế** cho từng ID bị thay. Tìm cả tên event/flag/biến/idea cụ thể, macro nhân sự và English loc. Sau đổi, tìm lại caller để xác nhận mỗi tham chiếu còn trỏ tới định nghĩa đúng.

Phần này xử lý code hiện hành và tương tác giữa nước. Thiết kế không thêm migration cho save của nhánh cũ.


**Xác minh bổ sung:** `lao_vietnan_treaty` là exact ID hiện hữu, kể cả cách viết “vietnan”: định nghĩa `common/ideas/asean.txt:63`, caller history Lào `:80`, history Việt Nam `:153`, English loc `localisation/english/MD_ideas_l_english.yml:421`. Đã tìm cả biến thể `vietnan` và `vietnam`; trong phạm vi common/events/history/English loc, tên treaty đang dùng là `lao_vietnan_treaty`. Audit phải tìm cả hai dạng, giữ nguyên ID đến khi có thay thế đồng bộ.

## 10. Tooltip và AI

UI hiển thị giá B1 và đầu ra duy nhất của `forecast_programme_completion`: ngày full dự báo, dự phòng, cổng và lý do khóa. Start>800: phục hồi bằng “Họp xử lý bất đồng” trước start; choice>840: chọn phương án không cộng trễ, không rút timer đã ký. A chưa đủ hiển thị riêng rủi ro cohesion−6/thẩm định+180/ngày và dự phòng nếu bị bác, không khóa vì rủi ro chưa hiện thực. B0PP+0.50/hạn780/bỏ thưởng; C15PP; E104 giữ ký theo tier45/30/25/21 và cửa sổ30/25/21. Node22 hiển thị legacy_node_terms, ghi “giả định gameplay, chưa cân bằng bằng engine”; XI12 bồi hoàn khác XII12 roster. Consumer40node hiển thị hành động được mở/đối ứng bị khóa, reader và thời điểm; archive_XV chỉ lưu. Giữ checkpoint15PP+0.25, gói55PP+0.50, vượt8/cổng40, BoP+0.30→+0.20, dự án phụ30PP/270ngày/guard một lần; k chỉ là tham số kiểm.

AI chọn cấp tốc khi ngày dư mở dự án phụ hoặc cơ hội có hạn; so đủ55PP+0.50ngân khố với50PP sớm. Start và choice chỉ đọc cổng forecast_programme_completion, không tự tính ngày. B cần0.50ngân khố và khả năng hoàn tất hợp đồng780. A chưa đủ không bị khóa tự động; AI đọc cả dự báo tất định lẫn rủi ro+180 trước cam kết. Consumer đọc record đúng đối tượng/epoch, chọn hành động có ích thay vì cộng điểm quyền; archive_XV không tăng utility hiện tại. Giữ cổng cohesion/BoP/hàng đợi lịch sử; không thêm miễn phí hoặc trọng số thưởng.

Tên focus phản ánh việc làm và event có source trung tâm quyết định. Những bonus chưa được đo giá kinh tế được đánh dấu trong review, không quy đổi tùy ý thành PP.

XIII12 — tooltip/cổng: available và tooltip chỉ gọi e104_contract_amendment_gate trên cùng ledger E104/đối tượng/source epoch. Khi khóa, hiển thị “hỗ trợ chưa nhận=0; quyền chưa dùng=0; sửa không giữ lợi ích; hủy vẫn khả dụng”. Khi hủy, hiển thị lượng hỗ trợ chưa nhận và quyền chưa dùng sẽ mất, nghĩa vụ tương lai sẽ đóng; mission/tier/PP sớm/thưởng đã nhận và hỗ trợ đã thanh toán giữ nguyên. Không tạo quyền mới, không thu hồi lịch sử, không cộng timer. Chỉ áp cổng tại XIII12, không áp XIV11 hoặc node khác.

AI XIII12 chỉ đọc cùng e104_contract_amendment_gate: sửa khi còn lợi ích và đối tác chấp nhận điều kiện; cả hai cạn thì chọn hủy đang mở. Trước xác nhận đọc lại ledger để tránh tooltip cũ. Không tự giảm giá hoặc bỏ guard một lần/đối tượng/epoch.

Trọng tâm — tooltip/AI: lấy toàn bộ ngày/cổng từ forecast_programme_completion, không tự tính. Chặn phải hiển thị cohesion hiện tại, hạn khởi động270, ngày sớm nhất, ngày còn thiếu, phục hồi/cooldown cần chờ; không hứa phục hồi mở được kỳ đã hết hạn. AI chỉ chốt programme có focus_available=1, ưu tiên đường đang mở phù hợp mục tiêu; phục hồi/hòa giải không bị cổng chốt khóa. Lựa chọn kiểm tra bị khóa vẫn để công vụ/dân vận khả dụng nếu đủ gate cũ. Rủi ro E103-A chỉ cảnh báo như đã chốt; không đổi800/840/900, giá hoặc timer.

## 11. Bảng tính trước code và playtest theo hai bước

### 11.1. Bảng ngân sách một nhiệm kỳ

Nguồn duy nhất: [B1 JSON](VIETNAM_POLITICAL_PARAMETERS_VI.json), [script .py](VIETNAM_POLITICAL_BALANCE_VI.py), [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv), [báo cáo lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3` để dựng lại CSV, đối chiếu bảng và xuất báo cáo Lượt 3; kết quả là số học, chưa kiểm engine.

CSV có 1296 hàng: bốn chương trình × ba tuyến × bốn mode × k/r, với chín tổ hợp E102×E103 cho chương trình kiểm tra. 648 hàng hợp lệ; các hàng cấp tốc/kiêm nhiệm bị BoP khóa có `eligible=0`, không có kết quả giả. Mỗi tuyến nhận cùng bộ event và lựa chọn khi so cùng programme. Programme khác không tự nhận event kiểm toán.

Snapshot chuẩn hóa: tier cán bộ 0, cohesion 60, BoP −0.30/0/+0.30. Các khoản focus và kiện toàn trước snapshot được tách khỏi phép so: F01/F07 trao 50 PP, F02 thu25, F04 thu thêm25 ở đường mở tập trung; CSV không giả vờ cân bằng có cùng lịch focus. E101 có caller riêng F05, được kiểm giá trong báo cáo, không cộng vào ma trận programme rồi làm lệch bộ event giữa tuyến. Cần chốt nếu muốn mở rộng snapshot sang cả lịch focus và E101.

Thu nhập r=[0.5,1,1.5], bonus nhánh0.03PP/ngày, cửa sổ1800ngày. k=[20,40,60] **chỉ là tham số kiểm tra**, không phải tỷ giá thật của game. Thu PP=(r+bonus)×cửa sổ; chưa mô hình stock/cap/luật/chiến tranh. Chi quy đổi=PP ròng+ngân khố ròng×k+(cohesion đầu−cuối)×3; cohesion nhận là khoản âm, không thành thu PP thật. CSV có `treasury_checkpoints`:0.50 khi trả cả hai,0 khi vượt hoặc chuẩn; đã cộng vào ngân khố ròng. Side project là lựa chọn riêng, chưa cộng vào tổng programme.

**Ngày full và mốc sớm cơ sở, tính từ B1:**

| Programme | Chuẩn tập thể/cân bằng | Chuẩn tập trung | Mốc sớm | Cấp tốc |
| --- | --- | --- | --- | --- |
| Cán bộ | 660 | 645 | 600 | 555 |
| Công vụ | 660 | 645 | 600 | 555 |
| Kiểm tra | 750 | 735 | 690 | 645 |
| Dân vận | 660 | 645 | 600 | 555 |



**Cột ngân sách E103-B:** `event_cost_pp` là PP của E102+E103+ký E104; `net_treasury_cost` là alias của `treasury_net_cost`. B0PP+0.50ngân khố làm PP ròng giảm30 và ngân khố ròng tăng0.50 so bản trước, trước các quy đổi k; mọi số ở bảng lấy từ script, không sửa tay.

**So cùng E102-A, E103-B, k=40, r=1:** B đã bỏ thưởng PP sớm ở mọi tuyến. E104 dùng cùng phản hồi đối tác chấp nhận: phân vai tier0 lấy gói thu hẹp, kiêm nhiệm ký gói đầy đủ.

| Tuyến | Mode | Chi PP ròng | Chi ngân khố ròng | Ngày full | Thưởng PP sớm | Cohesion cuối | BoP cuối | Chi quy đổi | Dự án phụ mở |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | 195 | 1.5 | 750 | 0 | 70 | -0.3 | 225.0 | 0 |
| balanced | standard | 195 | 1.5 | 750 | 0 | 66 | 0 | 237.0 | 0 |
| central | standard | 195 | 1.5 | 735 | 0 | 66 | 0.3 | 237.0 | 0 |
| central | fast_paid | 250 | 2.0 | 645 | 0 | 66 | 0.2 | 312.0 | 1 |
| central | fast_override | 220 | 1.5 | 645 | 0 | 50 | 0.4 | 310.0 | 1 |
| central | combined_fast_paid | 325 | 1.5 | 645 | 0 | 60 | 0.3 | 385.0 | 1 |

Case đổi E103 sang A trên cùng chứng cứ chuẩn phải cộng thẩm định lại tuần tự; CSV ghi cả ngày full tiềm năng và kết quả partial khi quá 900. Case cấp tốc A đủ hồ sơ nhận 50 PP, còn B/C bỏ thưởng PP nhưng vẫn có ngày dư để mở dự án phụ nếu full trước mốc riêng.

**Khoảng cách lịch:** chênh ngày đại hội −180 chuẩn bị −270 khởi động muộn −900 deadline.

| Nhiệm kỳ | Ngày còn cách chuẩn bị kỳ sau |
| --- | --- |
| IX | 475 |
| X | 380 |
| XI | 484 |
| XII | 482 |
| XIII | 470 |
| XIV | 476 |

Từ cohesion60, một gói vượt đưa về44; lần vượt tiếp theo bị khóa. Muốn vượt đủ gói sau cần hai lượt phục hồi:60PP, lên64, hoàn tất270ngày với cooldown180. Cadre cần giữ55 liên tục90ngày nên CSV cộng hai lượt30PP trong lúc triển khai; lịch165→255 và345→435 cho phép kiểm chứng465→555. Cadre kiêm nhiệm mất6 về54, cần thêm một lượt30PP trước kiểm chứng; CSV đã cộng. Kiêm nhiệm được chọn ngay sau khi chốt giá/mode programme, trước checkpoint khi BoP/cohesion còn đủ cổng, nên giá đã ký không bị tính lại. Các programme khác chưa cần phục hồi để nghiệm thu theo giả định của ma trận. BoP cuối chỉ tính hành động đã kê: snapshot tập trung +0.30, trả đủ →+0.20, vượt đủ →+0.40, trả đủ kèm kiêm nhiệm →+0.30. Cả mode hiện tại và quyền lần tới đều được nêu ở tooltip.

Chiến tranh, counter reset, kiến nghị chưa đóng và chỉ tiêu kinh tế chưa đạt nằm ngoài lịch cơ sở. CSV không chứng minh full chắc chắn trong game. I5 cổng dự báo chỉ xử lý trễ tất định; rủi ro A và các tình huống ngoài mô hình được cảnh báo riêng. Không rút timer hoặc đổi900.

### 11.2. Thứ tự kiểm tra tiết kiệm công

1. **Trước code:** kiểm tra ngân sách và timeline trong CSV; điều chỉnh mốc/giá khi cấp tốc không thay kết quả.
2. **Một nhiệm kỳ bằng console:** sau triển khai, dùng checkpoint save và thay nhanh BoP/cohesion/tier; chạy chuẩn/cấp tốc, chờ E103/E104, kiểm tra resolver.
3. **So sánh 3–5 năm:** chạy A tập thể, B cân bằng, C tập trung và D kiêm nhiệm trên cùng baseline; lặp từ save chung khi một kết quả chưa rõ.
4. **20–30 năm:** chỉ chạy profile có trade-off rõ và AI sau khi lượt ngắn đạt yêu cầu; thêm lượt lặp khi có vấn đề chưa giải thích.
5. **Dựng gói nhiệm kỳ:** đưa danh mục 74 node vào game theo từng kỳ, ghi số lựa chọn thực sự khả dụng và sửa các node thiếu hậu quả hoặc trùng chức năng.

Console và spreadsheet không thay playtest engine. Hiện mới hoàn thành bước 1, chưa có code để thực hiện bước 2.

### 11.3. Tiêu chí

- Đúng một kết quả mỗi kỳ/epoch; mọi lĩnh vực lên tier bằng chương trình của mình.
- Chuẩn→cấp tốc đổi mốc600/690; I2 kiểm PP thuần55−50=5. Gói trả đủ còn0.50ngân khố; chênh quy đổi15/25/35 ở k20/40/60 chỉ là tham số kiểm tra. Giá trị còn lại: dự án phụ270ngày/30PP. Kiểm checkpoint:20/25/30 so với vượt24, biên k40 chỉ1PP; không tự nới biên.
- 40 event/decision của X01–X08, XI01–XI08, XII01–XII08, XIII01–XIII08 và XIV01–XIV08 dùng giá từng node trong B1. Script `python VIETNAM_POLITICAL_BALANCE_VI.py --check-l2` đối chiếu bảng 40 node, giá B1, cost focus và gate/caller; `--csv-only` dựng lại ma trận ngân sách mà không ghi đè báo cáo lịch sử Lượt 1. Với cặp 20 PP so 0.50 ngân khố, chi quy đổi A/B tại k20/40/60 là 20/(10,20,30); với 25 PP so 0.75 ngân khố là 25/(15,30,45); với 15 PP so 0.50 ngân khố là 15/(10,20,30). Các profile còn lại cũng đảo thứ hạng trong ba mức k được thử. Vì vậy thứ hạng chi phí trực tiếp đổi theo k ở từng event; không có lựa chọn nào rẻ nhất ở cả ba k. K không đổi theo tuyến, r chỉ đổi mẫu số thu nhập PP; mọi tuyến dùng cùng event nên phép so giữ nguyên. Consumer quyền/dữ liệu và timer hồ sơ ở7.4a được kiểm riêng, không quy đổi thànhPP; chỉ XII12/XIII12 dùng Pareto tại7.4b theo xác nhận, các node/event khác giữ phép kiểm tiền trực tiếp.
- I5: dùng cùng forecast_programme_completion cho start≤800/choice≤840, CSV và tooltip; không khóa rủi ro A chưa hiện thực. Kiểm cohesion0–19, phục hồi0→20 và cửa sổ270; ghi cả đường phản thực bị khóa và nhánh rủi ro còn khả dụng. Timer/mode đã ký không đổi sau phục hồi; programme900/E102+90/thẩm định180 giữ nguyên.
- A-E103 thiếu hồ sơ bị bác, cohesion−6 và thẩm định180ngày; A khi đủ được rẻ nhất. B0PP+0.50ngân khố/hạn780; C15PP. I3 kiểm hai kịch bản×k20/40/60, in chênh từng cặp; báo mọi biên<3PP, không tự chỉnh.
- E104 dùng cùng nhân vật/đối tượng E102; dữ liệu hợp đồng và an ninh xuất hiện trong review.
- BoP dịch -0.05/+0.05 theo checkpoint thật, lặp hành động không farm thanh.
- Tier cán bộ và kiêm nhiệm có đường đạt cửa sổ ngay khi đủ điều kiện.
- Thu/chi, cohesion được duy trì đủ 90 ngày; corruption ở đáy dùng mục tiêu thay thế.
- Tập thể/tập trung có trade-off về PP, tiền, cohesion và cơ hội; không kết luận thống trị từ một chỉ số.
- Kiểm tra biên BoP ±0.25, cohesion 19/20/39/40/54/55/69/70, ngày 600/690/900, hạn ký 30/25/21 ngày, load save trước resolver.
- Gate 2006/2011/2016/2021/2026 chặn chọn sớm; 40 node L2 đều có cost, gate kỳ/ngày/prerequisite/chế độ, caller và hậu quả quay lại kỳ sau; cost vẫn là dữ liệu B1, chưa xác nhận defines.
- Mốc nợ xấu/VAMC 2013, sự cố giàn khoan 2014 và thị trường trái phiếu đóng băng quý IV/2022 có nguồn ở mục 2; động cơ và kết quả của lựa chọn gameplay vẫn ghi là giả định.
- Counter liên tục theo ngày chỉ chạy trên chương trình active của VIE; content validation chạy bằng script trong repo.
- Cohesion 0→40 có đường phục hồi số học 630 ngày; playtest xác nhận với thu nhập/event thực.

- I6/I10 hoàn thiện: đối chiếu gate/caller/guard/reader22node theo legacy_node_specs; consumer40node available1/đối ứng0 theo node_opportunity_effects. Script kiểm các nhu cầu hành động riêng, không cộng điểm quyền, không tính archive_XV là cơ hội hiện tại.
- Giá node mới: XI12 bồi hoàn20PP/0.50; XII12 kiện toàn−6cohesion; XII10 30PP so8cohesion+0.25, báo biên1PP tại k20 không chỉnh. X09 hai đợt0.25, X10 ứng0.50/rút30/kiến nghị; kiểm cả thời gian và trạng thái checkpoint/kiến nghị. XIV10 ổn định+1%365ngày, trần1%, dùng max với tier dân vận, phải có nghiệm thu đúng địa điểm. XIV11 giữ15/sửa0.50/hủy mất hỗ trợ chưa nhận. Mọi số là giả định gameplay, chưa cân bằng bằng engine; không thay giá/timer programme.

- XIII12 cổng bổ sung: e104_contract_amendment_gate dùng chung available/tooltip, chỉ sửa nếu hỗ trợ chưa nhận>0 hoặc quyền chưa dùng>0; hủy luôn mở. Kiểm9phép so trạng thái đã cạn và mọi trạng thái còn lợi ích; hủy chỉ ghi ledger E104, không fail mission/tier/reward/paid_support. Các chiều Pareto ngoài tiền phải hiện trước chọn; báo từng Δ và gần trùng<10%, không đổi giá/timer.

- Cổng chốt: cùng forecast_programme_completion với full800/840; kiểm mọi cohesion0–39, cooldown0/90/180, mọi tuyến/4programme; biên19/20 và270/271, lượt phục hồi đang chạy. Chỉ chốt programme có đường trước270. Cổng không khóa phục hồi/hòa giải, không thay gate90ngày/giá/cooldown/timer; trường hợp hết cửa sổ ghi không còn đường kỳ hiện tại, không tự fail mission hoặc trao thưởng.

## 12. Trạng thái hoàn thành

Đã áp dụng xác nhận E103-B0PP+0.50ngân khố và hạn hợp đồng780, giữ C15PP/E102+90/thẩm định180/programme900. Script tính lại PP/ngân khố và mọi bảng liên quan. I3 đã kiểm hai kịch bản đủ/chưa đủ hồ sơ, A được rẻ nhất khi đủ; biên nhỏ được báo chứ không điều chỉnh. I5 có bảng ngoại lệ/cổng đầy đủ:6/8đườngfull cũ dưới sàn bị khóa,2rủi ro A885 còn mở theo xác nhận; không đổi timer. Các giá mới22node đã chốt, là giả định gameplay, chưa cân bằng bằng engine.

Danh mục vẫn74node. Đã bổ sung gate/caller/guard/reader22node và consumer quyền40node; I6/I10 được kiểm bằng script. I5 dùng cổng trễ tất định được chốt, vẫn cảnh báo rủi ro A; I3 được mở rộng kiểm giá22node và có kết quả chi tiết tại báo cáo. Chưa nghiệm thu gameplay; báo cáo hiện hành ở [Lượt 3](VIETNAM_POLITICAL_REVIEW_L3_VI.md). Changelog ghi cả lệch810→780 theo mốc người dùng vừa chốt. Tham chiếu repo tại9 và BLUF được giữ.

Chỉ tính bằng script, chưa triển khai định nghĩa game của thiết kế này hoặc chạy engine/console/playtest.

BLUF
