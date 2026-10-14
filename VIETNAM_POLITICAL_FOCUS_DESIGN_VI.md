# Thiết kế nhánh chính trị Việt Nam: bản cân bằng theo nhiệm kỳ

**Kết luận:** Cây mở theo kỳ đại hội; chương trình trọng điểm có deadline 900 ngày và mốc thưởng sớm riêng: cán bộ/công vụ/dân vận 600, kiểm tra 690 ngày. BoP thay đổi theo hành vi, gồm ba vùng. Tuyến tập trung mua thời gian để giữ cửa sổ cơ hội; tuyến tập thể tích lũy khả năng phối hợp. Tier cán bộ giảm tổn thất chuyển giao, giảm giá khởi động và mở công cụ ký theo ủy quyền. Bản mẫu giữ 12 focus, ba xung đột chính và một event quay lại của DNNN; mục tiêu phát hành giữ đúng 74 node.

Các giá trị là thông số thiết kế từ [bảng tham số B1](VIETNAM_POLITICAL_PARAMETERS_VI.json), đã tính bằng [script ngân sách](VIETNAM_POLITICAL_BALANCE_VI.py). Báo cáo [hiện hành](VIETNAM_POLITICAL_REVIEW_L3_VI.md) ghi kết quả kiểm mô hình. Đã có [adapter game v57](VIE_political_v57_implementation.md) trong repo; chưa nghiệm thu HOI4. Bảng tính không phải mô phỏng engine.

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
- Full đúng hoặc trước mốc riêng: thêm 70 PP một lần.
- Partial: 2–3/4, cohesion +2, idea hỗ trợ nhỏ 365 ngày.
- Fail: 0–1/4, cohesion -6, PP factor -3% trong 180 ngày.
- Tier tối đa 3; thành công ở tier tối đa nhận thưởng tạm thời thay tier mới.
- E103 ghi kết quả kiểm chứng tự động; E104 giữ cửa sổ hợp đồng riêng. Resolver chương trình giữ deadline900.

**Ngày dư dùng được — decision “Dự án hỗ trợ thực thi sau nghiệm thu”.** Full đúng hoặc trước mốc riêng mở một dự án phụ. Giá 30 PP, ngân khố 0; thời gian 270 ngày, một mục tiêu: hoàn tất dự án hỗ trợ tại cùng bộ phận đã được nghiệm thu. Khi thành công nhận idea bureaucracy cost factor -1% trong 365 ngày; không trao tier hoặc PP. Idea thay thế cùng loại khi còn hạn, không cộng chồng. Deadline dự án phụ là ngày mở chuẩn bị đại hội sau, tách khỏi mission trọng điểm đã đóng. Bắt đầu chỉ khi còn ít nhất thời gian dự án cộng 100 ngày dự phòng. Timeout/cancel không trao thưởng; tooltip báo điều kiện và tiền đã chi. Guard `VIE_last_side_project_epoch` ghi lúc nhận dự án, cùng epoch chương trình: tối đa một lần mỗi nhiệm kỳ, hủy cũng không mở lại. F12/timeout/load save dùng chung guard.

I2 kiểm **chi phí quy đổi và cặp full/cohesion ngang nhau tại k=40**: gói55PP +0.50ngân khố so với thưởng70PP, chênh+5PP, trong ±10PP. Sensitivity k20/40/60 là −5/+5/+15PP; k là tham số kiểm, không phải tỷ giá engine. Dự án phụ30PP/270ngày lấy bureaucracy−1% trong365ngày là khoản mua thêm, không phải phần thưởng và không được dùng để bù chi phí cấp tốc. E103 tự động không có option bỏ thưởng; trượt mốc sớm chỉ mất thưởng sớm.

**Bất biến lịch:** programme900; start≤800/choice≤840 theo cùng forecast_programme_completion. Mọi trễ trong mô hình đều tất định. E103 tự động, không thêm thời gian hoặc ngoại lệ cảnh báo. Phục hồi sau start không xóa thời gian chuẩn bị đã ký; available/tooltip/CSV dùng cùng dự báo.

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

E102-C cộng90ngày vào chuỗi chứng cứ; kiến nghị công khai vẫn phải xử lý để đủ4/4. Tooltip trước lựa chọn đọc ngày full và dự phòng từ forecast_programme_completion: chuẩn tập thể/cân bằng840, tập trung825, cấp tốc735; không có trục E103 A/B/C. Khi chưa chốt mode hiển thị các mode khả dụng; sau chốt giữ timer đã ký. Giá và các cơ hội E102 giữ nguyên.

### 6.5. E103: kết quả kiểm chứng tự động, không phải quyết định

Mốc ngày450 chỉ thông báo tiến độ và chứng cứ còn thiếu. Khi đủ4/4, hệ thống tự ghi kết quả đúng epoch; không có menu A/B/C hoặc lựa chọn đánh đổi ở E103.

| Ngày đủ chứng cứ T | Kết quả tự động | Thưởng sớm |
| --- | --- | --- |
| T≤690 | on_time_full; tăng tier/cohesion theo resolver | 70 PP một lần |
| 690<T≤900 | late_full; vẫn full/tier/cohesion | 0 PP |
| T>900 hoặc chưa đủ4/4 tại deadline | Resolver chấm partial/fail theo số nhóm đã đạt | 0 PP |

T lấy từ lịch triển khai và kiểm chứng thật; E102-C vẫn cộng90ngày. E103 không tự tạo chứng cứ, không thu PP/ngân khố, không trừ cohesion và không cộng180ngày thẩm định. Bỏ hợp đồng780 và phí B/C của thiết kế cũ. E104 vẫn là quyết định hợp đồng riêng.

Chuẩn có T735/750: tự động late_full khi đủ4/4, không bị ép partial vì trượt690. Cấp tốc E102-A/B có T645: tự động on_time_full. Đây là hệ quả mode/E102 đã chọn, không gọi là canh bạc. Lịch E103 vẫn tất định; bất định chỉ được nêu tường minh ở IX11 và XI10, không cộng vào lịch programme này.

Cổng giữ nguyên: lựa chọn gây T>840 bị khóa, không dùng nhãn rủi ro để bỏ qua. Biên840 được mở,841 bị khóa. Sau khi đã ký, timer không giảm hồi tố. [CSV ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv) giữ các ca phản thực bị khóa.

**I2 theo chi phí quy đổi tại k=40, sensitivity báo riêng:**

| k thử | Giá gói PP | Thưởng PP | Chênh PP thuần | Ngân khố gói | Chênh quy đổi |
| --- | --- | --- | --- | --- | --- |
| 20 | 55 | 70 | -15 | 0.5 | -5.0 |
| 40 | 55 | 70 | -15 | 0.5 | 5.0 |
| 60 | 55 | 70 | -15 | 0.5 | 15.0 |

**I3 checkpoint — biên mỏng k=40:**

| k thử | Thương lượng quy đổi | Vượt quy đổi | Thương lượng − vượt |
| --- | --- | --- | --- |
| 20 | 20.0 | 24 | -4.0 |
| 40 | 25.0 | 24 | 1.0 |
| 60 | 30.0 | 24 | 6.0 |


**Cổng dự báo dùng chung:** E102-C và lựa chọn có trễ tất định dùng forecast_programme_completion với timer/mode đã ký; ngày>840 bị khóa. E103 không có lựa chọn hoặc ngoại lệ cảnh báo. E104 kiểm cửa sổ ký theo tier riêng, không tự cộng timer ký vào chuỗi programme.

### 6.6. E104: DNNN quay lại, an ninh và thời gian ký có giá

Caller chương trình kiểm tra ngày 500, chỉ khi đã có điều kiện công khai E102-A. Một đối tác gửi đề nghị hỗ trợ kỹ thuật có hạn **30 ngày**.

- Phân vai tier cán bộ 0: ký liên ngành 45 ngày, trễ cửa sổ.
- Tier 1: 30 ngày; tier 2: 25 ngày; tier 3 hoặc kiêm nhiệm: 21 ngày. Tier 1 đã đủ cửa sổ IX; XIII09 cần 25 ngày và XIV11 cần 21 ngày.
- Giá ký: 30 PP; thanh toán lúc chọn khi lịch ký có khả năng tới hạn. Khi không đủ thời gian, UI giới thiệu hai lựa chọn khác.

| Lựa chọn | Giá và thời gian | Hệ quả |
| --- | --- | --- |
| Ký gói có quyền tiếp cận dữ liệu | 30 PP; thời gian theo roster/tier | Ký trước hoặc đúng hạn xác lập hỗ trợ0.75ngân khố; chỉ nhận sau hai kỳ kiểm tra90/180ngày, mỗi kỳ10PP; hoàn tất một checkpoint hợp tác; an ninh yêu cầu kiểm chứng phạm vi dữ liệu trong review cuối |
| Xin gói thu hẹp dữ liệu | 15 PP, 21 ngày | Hỗ trợ 0.25; chỉ dùng chuyên gia đào tạo, không có checkpoint hợp tác sâu |
| Dùng đội trong nước | 0 PP | Giữ kế hoạch kiểm toán; không nhận hỗ trợ quốc tế |

Hỗ trợ chỉ thanh toán sau khi đối tác chấp nhận, ký đúng hạn và hoàn tất hai kỳ kiểm tra hợp đồng90/180ngày. Bảng ngân sách giả định nghĩa vụ được thực hiện, đã cộng20PP kiểm tra; không tự cộng25PP đào tạo tùy chọn. Nghĩa vụ này không kéo dài timer programme hoặc thay chứng cứ4/4.

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
| IX11 | Luân chuyển cán bộ trong đợt thí điểm | 5 | IX đã giải quyết; từ 19/04/2001; F09; mọi chế độ; dự án đang chạy và roster có người thay; loại trừ IX12 | Luân chuyển20PP: 65% cohesion+4; 35% xử lý lại thêm24PP và cohesion−4. RNG lưu một lần theo hồ sơ/epoch; không coi cohesion+4 là bảo đảm. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader X01: đọc người đã bàn giao và kiến nghị về người mới. |
| IX12 | Giữ người phụ trách đến nghiệm thu | 5 | IX đã giải quyết; từ 19/04/2001; F09; mọi chế độ; dự án đang chạy và có người phụ trách hợp lệ; loại trừ IX11 | Kiểm toán độc lập20PP, kết quả cố định, không nhận bonus cohesion của luân chuyển. Đây là đường chắc chắn đối ứng với IX11 có xác suất thất bại. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader X04: đọc yêu cầu kiểm toán độc lập chưa đóng. |

### Đặc tả Lượt 2 cho 40 node

Cost focus giữ đúng danh mục đã chụp tại B1; gate dùng kỳ đã giải quyết, ngày neo, prerequisite dưới đây và chế độ ghi riêng cho từng node. “Mọi chế độ” là lựa chọn thiết kế, không thêm trigger mới. Mỗi caller là event/decision/milestone được mở bởi focus hoàn thành; mã kỹ thuật sẽ được đăng ký ở lượt 3. Giá PP/ngân khố từng lựa chọn lấy theo node từ `node_choice_prices` trong JSON B1; thời lượng triển khai lấy từ `node_choice_delays`. Tỷ giá k chỉ dùng để so sánh: `chi quy đổi = PP + ngân khố × k + cohesion mất × 3`; thời gian, dữ liệu, quyền hạn và quan hệ chính trị được ghi thành cơ hội/đánh đổi riêng, không quy thành PP.

**X — neo 18/04/2006; đầu tư công và doanh nghiệp nhà nước.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XI |
| --- | --- | ---: | --- | --- | --- |
| X01 | Công khai danh mục vốn nhà nước | 5 | X đã giải quyết; từ 18/04/2006; F07; mọi chế độ | Event chọn hồ sơ. A: 20 PP, mở XI05. B: 0 PP, cohesion−6, khóa XI05. Gate chỉ áp cùng hồ sơ nguồn; chưa chốt thì reader bị khóa, không giả có quyền mở cả hai. | Bộ/ngành và DNNN; XI đọc hồ sơ trách nhiệm còn thiếu trước khi phân loại nợ. |
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
| XI09 | Lập quỹ xử lý dự án dở dang | 7 | XI đã giải quyết; từ 12/01/2011; XI07; mọi chế độ; có dự án dở dang và kiến nghị người mua; loại trừ XI10 | Cứu dự án0.50ngân khố; sau nghiệm thu thu hồi0.75ngân khố, kết quả cố định. Không trao khoản thu hồi nếu chưa có chứng cứ bàn giao. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader XII10: đọc nghĩa vụ cứu dự án chưa nghiệm thu. |
| XI10 | Buộc dự án dở dang tái cơ cấu | 7 | XI đã giải quyết; từ 12/01/2011; XI07; mọi chế độ; có dự án dở dang và hồ sơ chủ đầu tư; loại trừ XI09 | Tái cơ cấu90ngày, không ứng ngân khố: 70% thu hồi0.75ngân khố; 30% không thu hồi và cohesion−12. RNG một lần/đối tượng/epoch, không reroll khi load. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader XII10: đọc lịch tái cơ cấu và cam kết chưa bàn giao. |
| XI11 | Công khai kết quả thanh tra đất đai | 5 | XI đã giải quyết; từ 12/01/2011; XI04; mọi chế độ; có hồ sơ thanh tra đất đai và kiến nghị định danh | Công bố một hồ sơ cụ thể, đóng hoặc chuyển kiến nghị qua event dân vận; thưởng theo bằng chứng. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XII07: đọc kết luận và kiến nghị đã đóng hoặc chuyển. |
| XI12 | Kiểm tra trách nhiệm bên bảo lãnh tín dụng | 5 | XI đã giải quyết; từ 12/01/2011; XI06; mọi chế độ; có nghĩa vụ bảo lãnh và chứng cứ trách nhiệm | Event xác định bên chịu trách nhiệm; mở decision bồi hoàn có điều kiện và hậu quả đối với nhóm lợi ích. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Bồi hoàn chọn 20 PP hoặc 0.50 ngân khố; cùng nghĩa vụ, khác nguồn chi. Giá này thuộc XI12, không thuộc XII12. Reader XII07: đọc bên chịu trách nhiệm và bồi hoàn còn thiếu. |

**XII — neo 20/01/2016; phân quyền, trách nhiệm và chuyển giao.**

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller và hai lựa chọn có giá khác loại | Trung tâm phản ứng; hậu quả ở XIII |
| --- | --- | ---: | --- | --- | --- |
| XII01 | Mở rộng quyền ký theo ủy quyền | 5 | XII đã giải quyết; từ 20/01/2016; XI08 hoặc F07; mọi chế độ; loại trừ XII05 | Decision chọn phạm vi ủy quyền. A: 20 PP giữ ký tập trung, mất thời gian xử lý; B: 0,50 ngân khố đào tạo đầu mối địa phương, nhường quyền ký hồ sơ chuẩn cho cấp dưới. | Bộ/ngành và địa phương; XIII đọc ai được ký hợp đồng kỹ thuật trong cửa sổ ngắn. |
| XII02 | Giao quyền phê duyệt kèm hậu kiểm | 7 | XII; từ 20/01/2016; XII01 hoặc XII05; mọi chế độ | Event chọn trách nhiệm. A: 25 PP, mở XIII09. B: 0 PP, cohesion−8, khóa XIII09. Gate được AND với prerequisite/kỳ; không tự cho chữ ký hoặc bỏ kiểm chứng. | Cơ quan kiểm tra và người thực thi; XIII dùng tiền lệ này khi hợp tác an ninh cần quyết nhanh. |
| XII03 | Công khai biên bản nghiệm thu cải cách | 7 | XII; từ 20/01/2016; XII02; mọi chế độ | Milestone chọn mức công khai. A: 15 PP công bố kết quả tổng hợp, giữ dữ liệu cá nhân; B: 0,50 ngân khố cho phép kiểm toán đọc hồ sơ gốc, giảm quyền sửa biên bản sau nghiệm thu. | Cơ quan kiểm toán và địa phương; XIII biết dữ liệu nào có thể chia sẻ ra ngoài. |
| XII04 | Chốt chuyển giao trước đại hội | 3 | XII; từ 20/01/2016; XII07; mọi chế độ; loại trừ XII08 | Event roster chọn bàn giao. A: 20 PP giữ nguyên người phụ trách thêm 30 ngày; B: 0,50 ngân khố tổ chức bàn giao ngay, mất một lượt đào tạo nhưng không kéo dài quyền của người cũ. | Văn phòng điều phối và người kế cận; XIII thừa kế hồ sơ có chủ mới/đang chờ bàn giao. |
| XII05 | Điều phối nhiều chương trình liên ngành | 5 | XII; từ 20/01/2016; XI08 hoặc F07; mọi chế độ; loại trừ XII01 | Decision chọn trung tâm điều phối. A: 25 PP để từng bộ tự quyết, từ bỏ quyền ưu tiên lịch chung; B: 0,75 ngân khố lập đầu mối chung, nhường quyền đặt lịch cho cơ quan điều phối. | Bộ/ngành và văn phòng điều phối; XIII dùng lịch chung hoặc phải thương lượng lại từng hợp đồng. |
| XII06 | Phê chuẩn phương án kiêm nhiệm dài hạn | 7 | XII; từ 20/01/2016; XII01 hoặc XII05; roster hợp lệ, mọi chế độ | Event chốt giám sát chức vụ. A: 20 PP giữ hai chức vụ nhưng công khai xung đột lịch; B: 0,50 ngân khố tách quy trình ký, trả bằng thêm bước xác nhận cho hồ sơ khẩn. | Lãnh đạo, văn phòng và cơ quan giám sát; XIII tier ký không được suy ra tự động từ việc kiêm nhiệm. |
| XII07 | Kiểm tra trách nhiệm người đứng đầu | 7 | XII; từ 20/01/2016; XII03 hoặc XII06; mọi chế độ | Event chọn chuẩn xem xét. A: 25 PP chỉ xử lý sai phạm rõ, giữ quyền miễn trừ quyết định thiện chí; B: 0,75 ngân khố mở kiểm tra độc lập, mất quyền đóng hồ sơ nội bộ. | Cơ quan kiểm tra và người thực thi; XIII có hoặc không có cơ chế bảo vệ quyết định có căn cứ. |
| XII08 | Bàn giao hai chức vụ theo kế cận | 3 | XII; từ 20/01/2016; XII07; roster hợp lệ, mọi chế độ; loại trừ XII04 | Event chọn tiến độ. A: 15 PP bàn giao theo thứ tự, mất 60 ngày nhưng giữ chuyên môn; B: 0,50 ngân khố bàn giao đồng thời, giảm gián đoạn nhưng cắt quyền truy cập của người cũ sớm. | Văn phòng và người kế cận; XIII giữ trạng thái phân vai/kiêm nhiệm làm điều kiện cửa sổ 25 ngày. |

XII09–XII12 giữ nguyên nội dung, cost và điều kiện.

| Node | Focus | Cost | Gate: kỳ; ngày; prerequisite; chế độ | Caller, giá và hậu quả cụ thể |
| --- | --- | ---: | --- | --- |
| XII09 | Ban hành quy trình bảo vệ quyết định đúng | 7 | XII đã giải quyết; từ 20/01/2016; XII07; mọi chế độ; có người thực thi và hồ sơ quyết định cần bảo vệ | Mở công cụ thẩm định trách nhiệm, chứng chỉ được E103 tự động đọc khi kiểm hồ sơ kế tiếp; phải hoàn thành đào tạo 90 ngày. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader E103: đọc chứng chỉ đào tạo trước khi mở thẩm định trách nhiệm. |
| XII10 | Đặt thời hạn xử lý hồ sơ liên ngành | 5 | XII đã giải quyết; từ 20/01/2016; XII02; mọi chế độ; có hồ sơ liên ngành tồn đọng | Decision xử lý một hồ sơ tồn đọng 180 ngày; chọn đầu mối hoặc hội đồng, trả PP/cohesion theo cách làm. **Bổ sung hoàn thiện:** Decision do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Đầu mối 30 PP; hội đồng 8 cohesion + 0.25 ngân khố; chỉ trả một cách, cả hai giữ 180 ngày. Reader XIII09: đọc đầu mối hoặc hội đồng chịu trách nhiệm hồ sơ. |
| XII11 | Công khai quyền hạn khi kiêm nhiệm | 5 | XII đã giải quyết; từ 20/01/2016; XII06; mọi chế độ; roster hợp lệ, phân vai hoặc kiêm nhiệm | Event giám sát roster kiêm nhiệm hoặc phân vai: công bố quyền hạn, mở checkpoint kiểm tra người đứng đầu. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả.  Reader XIII09: đọc quyền ký đã công khai và checkpoint giám sát. |
| XII12 | Thẩm định phương án thay người giữa nhiệm kỳ | 5 | XII đã giải quyết; từ 20/01/2016; XII07; mọi chế độ; roster có phương án thay người hợp lệ | A bàn giao60ngày, không thu phí nhưng khóa XII09 trong kỳ. B mất6cohesion, mở XII09 ngay; gate được AND với prerequisite/roster hợp lệ, không tự hoàn tất đào tạo. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader XIII09: đọc bàn giao đang chờ hoặc kiện toàn đã trả cohesion. |

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
| XIII12 | Điều chỉnh hợp đồng sau cảnh báo an ninh | 5 | XIII đã giải quyết; từ 25/01/2021; XIII09; mọi chế độ; có cảnh báo an ninh đối với hợp đồng đang hiệu lực | Sửa chỉ khi còn lợi ích và đối tác chấp nhận, mở XIV11; kiểm chứng sau90/180ngày, mỗi lần10PP. Hủy khóa XIV11, mất hỗ trợ chưa nhận và đóng nghĩa vụ; không trừ khoản hỗ trợ chưa nhận vào ngân khố thực. **Bổ sung hoàn thiện:** Event do focus hoàn thành mở; một lần trên node/đối tượng/epoch; pending và resolved riêng; trả phí trước ghi kết quả. Reader XIV11: đọc điều kiện đã sửa hoặc hỗ trợ đã mất khi hủy. |

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


### 7.4a. Tác dụng có giá và tám node đổi cấu trúc

Nguồn thực thi mô hình giấy: [consumer](VIETNAM_POLITICAL_CONSUMERS_VI.py). Các tỷ lệ65/35 và70/30 là giả định gameplay. RNG lấy một lần khi giải quyết hồ sơ, lưu theo node/đối tượng/epoch; load/replay không reroll hoặc thu lại phí. Thu hồi tài sản yêu cầu chứng cứ dự án/tái cơ cấu đã hoàn tất. Thất bại là kết quả có tác dụng, không phải option biết trước sẽ thua.

| Node/nhánh | Option | Chi lúc chọn | Kết quả quan sát được |
| --- | --- | --- | --- |
| IX11 / IX12 | A | 20PP +0ngân khố +0cohesion | 65% Luân chuyển đạt đồng thuận: PP+0, ngân khố+0, cohesion+4; 35% Bị phản đối, phải xử lý lại: PP-24, ngân khố+0, cohesion-4 |
| IX11 / IX12 | B | 20PP +0ngân khố +0cohesion | 100% Kiểm toán độc lập, chi phí cố định: PP+0, ngân khố+0, cohesion+0 |
| XI09 / XI10 | A | 0PP +0.5ngân khố +0cohesion | 100% Cứu và thu hồi tài sản đã nghiệm thu: PP+0, ngân khố+0.75, cohesion+0 |
| XI09 / XI10 | B | 0PP +0ngân khố +0cohesion | 70% Tái cơ cấu thu hồi đủ: PP+0, ngân khố+0.75, cohesion+0; 30% Tái cơ cấu thất bại: PP+0, ngân khố+0, cohesion-12 |
| XII12 | A | 0PP +0ngân khố +0cohesion | 100% Bàn giao tuần tự; bỏ đợt đào tạo kỳ này: PP+0, ngân khố+0, cohesion+0, khóa XII09 |
| XII12 | B | 0PP +0ngân khố +6cohesion | 100% Kiện toàn ngay; mở đào tạo trách nhiệm: PP+0, ngân khố+0, cohesion+0, mở XII09 |
| XIII12 | A | 0PP +0ngân khố +0cohesion | 100% Sửa, giữ hợp đồng; phải hoàn tất hai kỳ kiểm tra: PP+0, ngân khố+0, cohesion+0, mở XIV11 |
| XIII12 | B | 0PP +0ngân khố +0cohesion | 100% Hủy, đóng nghĩa vụ và mất hỗ trợ chưa nhận: PP+0, ngân khố+0, cohesion+0, khóa XIV11 |
| X01 | A | 20PP +0ngân khố +0cohesion | 100% Hồ sơ kiểm toán vốn; mở xử lý nợ: PP+0, ngân khố+0, cohesion+0, mở XI05 |
| X01 | B | 0PP +0ngân khố +6cohesion | 100% Chấp nhận tranh chấp để giữ vốn tại ngành; khóa xử lý nợ qua hồ sơ này: PP+0, ngân khố+0, cohesion+0, khóa XI05 |
| XII02 | A | 25PP +0ngân khố +0cohesion | 100% Thẩm định trước, mở ký liên ngành: PP+0, ngân khố+0, cohesion+0, mở XIII09 |
| XII02 | B | 0PP +0ngân khố +8cohesion | 100% Trách nhiệm cá nhân, khóa ký liên ngành: PP+0, ngân khố+0, cohesion+0, khóa XIII09 |

XII12-A giữ bàn giao60ngày nhưng khóa XII09 trong kỳ; B mở XII09 ngay. Node XII09 cần cả prerequisite cũ và gate này. X01 đọc tại XI05; XII02 đọc tại XIII09; XIII12 đọc tại XIV11. Gate mặc định đóng trước khi có record và được AND với prerequisite; không bỏ qua kỳ/ngày/đối tượng. Nhánh khóa không cho chọn node rồi mới fail. Một node đã hoàn thành không nhận lại reward từ gate.

### 7.4b. Hoàn trả công việc và nghĩa vụ hợp đồng

Các consumer còn lại hoàn trả chi phí tái sử dụng hồ sơ: A +8PP, B +0.20ngân khố khi reader hoàn thành trên cùng hồ sơ/source epoch; phí mở hồ sơ vẫn trả trước. Không nhận reader hoặc chưa đủ chứng cứ thì chưa hoàn trả. Archive XIV→XV chỉ lưu, thưởng0. Guard lưu consumed; hủy hoặc đọc sai đối tượng/epoch không tạo khoản hoàn trả. Các khoản này là giả định gameplay, không phải điểm cơ hội.

| Writer | Reader | A: PP hoàn trả | B: ngân khố hoàn trả |
| --- | --- | --- | --- |
| X02 | XI06 | 8 | 0.2 |
| X03 | XI07 | 8 | 0.2 |
| X04 | XI12 | 8 | 0.2 |
| X05 | XI01 | 8 | 0.2 |
| X06 | XI03 | 8 | 0.2 |
| X07 | XI08 | 8 | 0.2 |
| X08 | XII10 | 8 | 0.2 |
| XI01 | XII07 | 8 | 0.2 |
| XI02 | XII10 | 8 | 0.2 |
| XI03 | XII12 | 8 | 0.2 |
| XI04 | XII07 | 8 | 0.2 |
| XI05 | XII10 | 8 | 0.2 |
| XI06 | XII10 | 8 | 0.2 |
| XI07 | XII10 | 8 | 0.2 |
| XI08 | XIII01 | 8 | 0.2 |
| XII01 | XIII09 | 8 | 0.2 |
| XII03 | XIII09 | 8 | 0.2 |
| XII04 | XIII09 | 8 | 0.2 |
| XII05 | XIII09 | 8 | 0.2 |
| XII06 | XIII09 | 8 | 0.2 |
| XII07 | XIII12 | 8 | 0.2 |
| XII08 | XIII09 | 8 | 0.2 |
| XIII01 | XIV11 | 8 | 0.2 |
| XIII02 | XIV07 | 8 | 0.2 |
| XIII03 | XIV11 | 8 | 0.2 |
| XIII04 | XIV07 | 8 | 0.2 |
| XIII05 | XIV02 | 8 | 0.2 |
| XIII06 | XIV11 | 8 | 0.2 |
| XIII07 | XIV03 | 8 | 0.2 |
| XIII08 | XIV02 | 8 | 0.2 |
| XIV01 | archive_XV | 0 | 0 |
| XIV02 | archive_XV | 0 | 0 |
| XIV03 | archive_XV | 0 | 0 |
| XIV04 | archive_XV | 0 | 0 |
| XIV05 | archive_XV | 0 | 0 |
| XIV06 | archive_XV | 0 | 0 |
| XIV07 | archive_XV | 0 | 0 |
| XIV08 | archive_XV | 0 | 0 |

E102-A mở E104 theo hồ sơ công khai thật. Đào tạo E104 là task90ngày, cùng đối tượng/epoch, không có phí riêng; nhận25PP sau chứng cứ hoàn thành và hai kỳ kiểm tra hợp đồng. Cột training_reward_if_completed_pp chỉ là kết quả nếu thực hiện task, không cộng vào pp_net_cost trước khi hoàn tất và không dùng trong Pareto programme. Hủy hoặc thiếu kiểm tra thu hồi quyền chưa dùng; không thu hồi PP đã nhận.

XIII12 sửa giữ hợp đồng phải kiểm hồ sơ sau90và180ngày tính từ lần sửa; mỗi lần10PP. Qua cả hai mới nhận phần hỗ trợ chưa thanh toán. Thiếu một lần: chấm dứt nghĩa vụ tương lai, mất hỗ trợ chưa nhận/quyền đào tạo chưa dùng và cohesion−6 đúng một lần. Hủy đóng nghĩa vụ ngay, mất hỗ trợ chưa nhận, khóa XIV11 cho hợp đồng này; không trừ ngân khố bằng khoản hỗ trợ chưa nhận và không thu hồi lịch sử. Nếu không còn lợi ích thì sửa bị khóa; đối tác phải chấp nhận sửa. Các chi phí tương lai chỉ ghi khi còn chưa trả, không thu hai lần khi sửa/timeout/load.

I3 chỉ báo REVIEW: kiểm được giao dịch, gate và kết quả hai nhánh, nhưng không tuyên bố mọi chiều sở thích hoặc thời gian có tỷ giá PP. So tiền trực tiếp vẫn chỉ rõ các phương án rẻ hơn; không dùng tên hành động hoặc cờ nghĩa vụ để đổi FAIL thành PASS.


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
| Kiểm chứng E103 / hợp đồng E104 | E103 ghi tiến độ/kết quả tự động; E104 lưu pending và deadline ký riêng |
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
| `forecast_programme_completion` | Trigger thiết kế; Python cùng tên là nguồn tính dự báo duy nhất cho CSV/available/tooltip | Đọc timer/mode đã ký, chuẩn bị tại start, trễ tất định đã biết; xuất ngày/dự phòng/cổng. E103 tự động không thêm trễ; mọi ngày trong mô hình đều tất định; chưa là trigger engine |
| `node_opportunity_effects`; `legacy_node_specs`; `legacy_node_terms`; `archive_XV` | Focus/caller đã có ghi record node/đối tượng/epoch và phí một lần | Reader ở7.4/7.4a đọc; quyền đối ứng khóa, archive chỉ lưu không trao gameplay; giá mới là giả định gameplay |
| `i3_pareto_exceptions` | Caller XII12/XIII12 đọc record roster/hợp đồng đã có | Lưu lựa chọn/trạng thái theo đối tượng/epoch, chiều/biên ở7.4b; Pareto chỉ hai node, tooltip trước chọn; chưa là ID engine |
| `e104_contract_amendment_gate`; `e104_contract_ledger` | Ký/phản hồi E104 và sửa/hủy XIII12 ghi ledger: support_promised, support_received, support_forfeited, rights_granted, rights_used, rights_revoked, contract_state | Available và tooltip sửa XIII12 đọc cùng trigger; hủy luôn mở. Hủy giữ tiền đã nhận/quyền đã dùng/lịch sử, không ghi mission/tier/reward; chưa là ID engine |
| `focus_commitment_gate`; elapsed_congress_days; recovery_cooldown_remaining; pending_recovery_remaining | Scheduler đại hội/decision cập nhật tuổi cửa sổ, cooldown và lượt phục hồi purpose=cohesion đang chạy | Cùng forecast_programme_completion trả focus_available, earliest_feasible_start_day, latest_start_day, start_days_short cho available/tooltip/AI; cổng chung bất kỳ programme, cổng lựa chọn programme đích; không là trigger engine mới |

Registry này đóng phạm vi các ID/nhãn đã viết, không chứng minh tồn tại API hoặc định nghĩa trong game. Giá lựa chọn ở `node_choice_prices`/`legacy_node_terms`, timer ở `node_choice_delays`, gate/caller22node ở `legacy_node_specs`, consumer quyền ở `node_opportunity_effects`, lịch sử ở `l2_history_anchors` của B1. Quyền đọc theo đúng node/đối tượng/epoch; available=1 cho hành động đã chọn, 0 cho đối ứng; không cộng điểm quyền và không trao kết quả tự động.

### 8.2. Kiểm chứng 90 ngày và tránh lách

Trong phase nghiệm thu, hook theo ngày chỉ kiểm tra VIE khi đúng chương trình hoạt động. Mỗi điều kiện cần chuỗi 90 ngày liên tục: đạt thì tăng counter, không đạt thì reset. Khi counter đủ 90, ghi milestone lịch sử và kết thúc kiểm chứng.

Cán bộ theo dõi cohesion; công vụ theo dõi thu/chi; kiểm tra ở baseline đáy theo dõi giữ mức corruption thấp nhất. Các counter chỉ tồn tại trong phase liên quan. Phương án này thêm vài check trên một nước, không quét toàn quốc.

Chỉ tiêu từ hoạt động bắt buộc và lịch sử 90 ngày không được thay bằng ảnh chụp đúng ngày chấm. GDP không thay thế nghiệm thu dự án.

### 8.3. Resolver và phạm vi thưởng

- Resolver đại hội guard kỳ, kiểm tra chế độ, ghi kết quả và kiện toàn.
- Adapter nhân sự kiểm tra tổ hợp vai trò, áp hiệu ứng theo người và đợt chuyển giao.
- Resolver programme guard epoch, chấm 4 nhóm, tính mốc sớm theo chương trình 600/690 và chứng cứ đã kiểm chứng; E103 ghi cùng kết quả tự động, ghi kết quả trước thưởng.
- Review sớm chỉ chốt full; nếu chưa đủ, mission tiếp tục.
- E103 không có resolver hợp đồng riêng: cùng resolver programme ghi đúng một kết quả/epoch trước thưởng. E104 có guard hợp đồng riêng, không tự hoàn thành programme.
- Một programme full được +70 PP sớm tối đa một lần; gọi lại F12, load save hay đến timeout không trao lại.
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

UI hiển thị giá và ngày/cổng từ forecast_programme_completion. E103 chỉ báo tiến độ ngày450 và kết quả kiểm chứng tự động; không menu A/B/C, không cảnh báo rủi ro giả. E104 giữ cửa sổ ký theo tier; các node đọc record đúng đối tượng/epoch.

AI chọn cấp tốc khi đạt thưởng70PP hoặc cơ hội có ích; so gói55PP+0.50 với70PP, chênh+5PP ởk40. E103 không có lựa chọn AI; E102 và mode mới là quyết định. Đọc cổng start800/choice840/chốt270 từ cùng dự báo; dự án phụ là khoản mua thêm.

Tên focus phản ánh việc làm và event có source trung tâm quyết định. Những bonus chưa được đo giá kinh tế được đánh dấu trong review, không quy đổi tùy ý thành PP.

XIII12 — tooltip/cổng: available và tooltip chỉ gọi e104_contract_amendment_gate trên cùng ledger E104/đối tượng/source epoch. Khi khóa, hiển thị “hỗ trợ chưa nhận=0; quyền chưa dùng=0; sửa không giữ lợi ích; hủy vẫn khả dụng”. Khi hủy, hiển thị lượng hỗ trợ chưa nhận và quyền chưa dùng sẽ mất, nghĩa vụ tương lai sẽ đóng; mission/tier/PP sớm/thưởng đã nhận và hỗ trợ đã thanh toán giữ nguyên. Không tạo quyền mới, không thu hồi lịch sử, không cộng timer. Chỉ áp cổng tại XIII12, không áp XIV11 hoặc node khác.

AI XIII12 chỉ đọc cùng e104_contract_amendment_gate: sửa khi còn lợi ích và đối tác chấp nhận điều kiện; cả hai cạn thì chọn hủy đang mở. Trước xác nhận đọc lại ledger để tránh tooltip cũ. Không tự giảm giá hoặc bỏ guard một lần/đối tượng/epoch.

Trọng tâm — tooltip/AI: lấy ngày/cổng từ cùng dự báo. Hiển thị cohesion, hạn270, ngày khởi động khả thi, cooldown và ngày thiếu. AI chỉ chốt programme có focus_available=1; phục hồi/hòa giải vẫn mở, không cứu hồi tố cửa sổ đã hết. E103 chỉ đọc chứng cứ để ghi kết quả tự động; giữ800/840/900.

## 11. Bảng tính trước code và playtest theo hai bước

### 11.1. Bảng ngân sách một nhiệm kỳ

Nguồn tham số và công cụ tái tạo (đi kèm trong gói): [B1 JSON](VIETNAM_POLITICAL_PARAMETERS_VI.json), [script .py](VIETNAM_POLITICAL_BALANCE_VI.py), [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv), [báo cáo hiện hành](VIETNAM_POLITICAL_REVIEW_L3_VI.md). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3` để dựng lại CSV, đối chiếu bảng và xuất báo cáo Lượt 3; kết quả là số học, chưa kiểm engine.

CSV chính có324hàng hợp lệ: bỏ324tổ hợp khóa BoP và trục lựa chọn E103 A/B/C đã bỏ. Script kiểm đúng tập tổ hợp và không trùng. Các ca khóa lịch E102-C/cohesion thấp ở CSV ngoại lệ I5; toàn bộ probe chỉ xuất khi dùng --audit-json.

Snapshot chuẩn hóa: tier cán bộ 0, cohesion 60, BoP −0.30/0/+0.30. Các khoản focus và kiện toàn trước snapshot được tách khỏi phép so: F01/F07 trao 50 PP, F02 thu25, F04 thu thêm25 ở đường mở tập trung; CSV không giả vờ cân bằng có cùng lịch focus. E101 có caller riêng F05, được kiểm giá trong báo cáo, không cộng vào ma trận programme rồi làm lệch bộ event giữa tuyến. Cần chốt nếu muốn mở rộng snapshot sang cả lịch focus và E101.

Thu nhập r=[0.5,1,1.5], bonus nhánh0.03PP/ngày, cửa sổ1800ngày. k=[20,40,60] **chỉ là tham số kiểm tra**, không phải tỷ giá thật của game. Thu PP=(r+bonus)×cửa sổ; chưa mô hình stock/cap/luật/chiến tranh. Chi quy đổi=PP ròng+ngân khố ròng×k+(cohesion đầu−cuối)×3; cohesion nhận là khoản âm, không thành thu PP thật. CSV có `treasury_checkpoints`:0.50 khi trả cả hai,0 khi vượt hoặc chuẩn; đã cộng vào ngân khố ròng. Side project là lựa chọn riêng, chưa cộng vào tổng programme.

**Ngày full và mốc sớm cơ sở, tính từ B1:**

| Programme | Chuẩn tập thể/cân bằng | Chuẩn tập trung | Mốc sớm | Cấp tốc |
| --- | --- | --- | --- | --- |
| Cán bộ | 660 | 645 | 600 | 555 |
| Công vụ | 660 | 645 | 600 | 555 |
| Kiểm tra | 750 | 735 | 690 | 645 |
| Dân vận | 660 | 645 | 600 | 555 |


**Cột ngân sách E103 tự động:** pp_e103=0, treasury_e103=0. event_cost_pp gồm E102, ký E104 và pp_contract_checks=20 khi nhận hợp đồng; thưởng đào tạo chưa làm không trừ vào ngân sách; net_treasury_cost là alias của treasury_net_cost. Kết quả E103 suy từ ngày chứng cứ, không phải một option để tối ưu.

**So cùng E102-A, E103 tự động, k=40, r=1:** chuẩn trượt690 vẫn late_full khi đủ4/4; cấp tốc đạt690 nhận70PP. E104 dùng cùng phản hồi đối tác chấp nhận; phân vai tier0 ký gói thu hẹp, kiêm nhiệm ký gói đầy đủ.

| Tuyến | Mode | Chi PP ròng | Chi ngân khố ròng | Ngày full | Thưởng PP sớm | Cohesion cuối | BoP cuối | Chi quy đổi | Dự án phụ mở |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | 215 | 1.0 | 750 | 0 | 70 | -0.3 | 225.0 | 0 |
| balanced | standard | 215 | 1.0 | 750 | 0 | 66 | 0 | 237.0 | 0 |
| central | standard | 215 | 1.0 | 735 | 0 | 66 | 0.3 | 237.0 | 0 |
| central | fast_paid | 200 | 1.5 | 645 | 70 | 66 | 0.2 | 242.0 | 1 |
| central | fast_override | 170 | 1.0 | 645 | 70 | 50 | 0.4 | 240.0 | 1 |
| central | combined_fast_paid | 275 | 1.0 | 645 | 70 | 60 | 0.3 | 315.0 | 1 |

E103 không có lựa chọn để đổi. Chuẩn T735/750 là late_full; cấp tốc T645 là on_time_full; T>900 chấm partial/fail theo số nhóm thực đạt ởdeadline, không trao full theo ngày tiềm năng. CSV là fixture lịch khi hoàn tất chứng cứ, không tạo chứng cứ trong game.

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

Chiến tranh, counter reset, kiến nghị chưa đóng và chỉ tiêu kinh tế chưa đạt nằm ngoài fixture lịch cơ sở. Không giả định một xác suất trễ E103. Khi đã biết trễ, dự báo và cổng phải tính đầy đủ; CSV không chứng minh full chắc chắn trong game.

### 11.2. Thứ tự kiểm tra tiết kiệm công

1. **Trước code:** kiểm tra ngân sách và timeline trong CSV; điều chỉnh mốc/giá khi cấp tốc không thay kết quả.
2. **Một nhiệm kỳ bằng console:** sau triển khai, dùng checkpoint save và thay nhanh BoP/cohesion/tier; chạy chuẩn/cấp tốc, chờ E103/E104, kiểm tra resolver.
3. **So sánh 3–5 năm:** chạy A tập thể, B cân bằng, C tập trung và D kiêm nhiệm trên cùng baseline; lặp từ save chung khi một kết quả chưa rõ.
4. **20–30 năm:** chỉ chạy profile có trade-off rõ và AI sau khi lượt ngắn đạt yêu cầu; thêm lượt lặp khi có vấn đề chưa giải thích.
5. **Dựng gói nhiệm kỳ:** đưa danh mục 74 node vào game theo từng kỳ, ghi số lựa chọn thực sự khả dụng và sửa các node thiếu hậu quả hoặc trùng chức năng.

Console và spreadsheet không thay playtest engine. Hiện mới hoàn thành bước 1, chưa có code để thực hiện bước 2.

### 11.3. Tiêu chí

- Đúng một kết quả mỗi kỳ/epoch; mọi lĩnh vực lên tier bằng chương trình của mình.
- Chuẩn→cấp tốc giữ mốc600/690; thưởng sớm70PP thay50PP theo yêu cầu cân lại ngày14/10/2026. I2 kiểm55+0.50×40−70=+5PP và bốn cặp full/cohesion66 ởk40 trong ±10PP. Sensitivity k20/40/60:−5/+5/+15PP; dự án phụ270ngày/30PP là khoản mua thêm. Kiểm checkpoint giữ20/25/30 so với vượt24, biên k40 chỉ1PP; không tự nới biên.
- 38 node thông thường giữ phép so tiền trực tiếp; X01/XII02 đổi nguồn chi sang cohesion và gate. Tám node trong7.4a có nhánh thất bại hoặc reader mở/khóa thật. I3/I10 là REVIEW, không suy ra cân bằng từ tên quyền hoặc chiều chưa định nghĩa.
- I5: cùng forecast_programme_completion cho start≤800/choice≤840, CSV và tooltip. Mọi trễ trong mô hình tất định; khóa T>840, không có ngoại lệ rủi ro E103. Kiểm cohesion0–19, phục hồi0→20 và cửa sổ270; timer/mode đã ký không đổi, programme900/E102+90 giữ nguyên.
- E103 tự động: không thuộc phép so lựa chọn I3. Kiểm T690/691,735/750,840/841,900/901 và một kết quả mỗi epoch; E103 không thu phí hoặc kéo dài thẩm định.
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

- I6/I10: đọc record cùng đối tượng/epoch; consumer hoàn trả8PP hoặc0.20ngân khố một lần khi reader hoàn thành. Archive không có reward. Bỏ cờ cơ hội khỏi so programme; I10 là REVIEW, không tuyên bố utility bằng tên hành động.
- Giá node mới: XI12 bồi hoàn20PP/0.50; XII12 kiện toàn−6cohesion; XII10 30PP so8cohesion+0.25, báo biên1PP tại k20 không chỉnh. X09 hai đợt0.25, X10 ứng0.50/rút30/kiến nghị; kiểm cả thời gian và trạng thái checkpoint/kiến nghị. XIV10 ổn định+1%365ngày, trần1%, dùng max với tier dân vận, phải có nghiệm thu đúng địa điểm. XIV11 giữ15/sửa0.50/hủy mất hỗ trợ chưa nhận. Mọi số là giả định gameplay, chưa cân bằng bằng engine; không thay giá/timer programme.

- XIII12: sửa cần lợi ích còn lại và đối tác chấp nhận; phải kiểm hồ sơ ngày90/180, mỗi lần10PP. Thiếu một lần mất hỗ trợ chưa nhận/quyền đào tạo chưa dùng, cohesion-6; không thu hồi tiền đã nhận. Hủy luôn mở.

- Cổng chốt: cùng forecast_programme_completion với full800/840; kiểm mọi cohesion0–39, cooldown0/90/180, mọi tuyến/4programme; biên19/20 và270/271, lượt phục hồi đang chạy. Chỉ chốt programme có đường trước270. Cổng không khóa phục hồi/hòa giải, không thay gate90ngày/giá/cooldown/timer; trường hợp hết cửa sổ ghi không còn đường kỳ hiện tại, không tự fail mission hoặc trao thưởng.


## 12. Trạng thái hoàn thành

Mô hình giấy có74node; E103 đã chuyển thành hệ quả tự động của chứng cứ, không còn A/B/C hoặc phí/thẩm định cũ. Mode và E102 giữ quyết định thực. Thưởng sớm70PP; programme900/E102+90/start800/choice840 giữ nguyên.

Báo cáo hiện hành ở [Lượt 3](VIETNAM_POLITICAL_REVIEW_L3_VI.md). Các giá là giả định gameplay; adapter game v57 đã được triển khai trong repo và có fixture đọc script; chưa nghiệm thu engine/AI/playtest.

BLUF
