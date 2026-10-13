# Thiết kế nhánh chính trị Việt Nam: bản cân bằng theo nhiệm kỳ

**Kết luận:** Cây mở theo kỳ đại hội; chương trình trọng điểm có deadline 900 ngày và mốc thưởng sớm riêng: cán bộ/công vụ/dân vận 600, kiểm tra 690 ngày. BoP thay đổi theo hành vi, gồm ba vùng. Tuyến tập trung mua thời gian để giữ cửa sổ cơ hội; tuyến tập thể tích lũy khả năng phối hợp. Tier cán bộ giảm tổn thất chuyển giao, giảm giá khởi động và mở công cụ ký theo ủy quyền. Bản mẫu giữ 12 focus, ba xung đột chính và một event quay lại của DNNN; mục tiêu phát hành là 60–80 focus, danh mục hiện tại có 74 node.

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

Ba event chính dùng ba loại bài toán khác nhau: quyền lợi địa phương, điều kiện vốn DNNN và chất lượng bằng chứng trước deadline. DNNN quay lại trong E104 cùng một hợp đồng, kéo thêm an ninh–quốc phòng vào quyết định. Các tình huống là hư cấu gameplay; nghiên cứu scandal và nhân vật thật là bước riêng.

Cụm DNNN/đất đai mở đầu; đầu tư và hội nhập theo đại hội X; nghĩa vụ trái phiếu từ XI; trách nhiệm người thực thi, dữ liệu và kiêm nhiệm ở các nhóm sau. Điều kiện ngày/kỳ là điều kiện khả dụng cho người chơi, không chỉ trọng số AI.

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

**Bất biến lịch:** bắt đầu muộn nhất+900 phải cách chuẩn bị đại hội sau ít nhất100ngày; khoảng nhỏ nhất380ngày theo mục5.1. I5: đường chuẩn/cấp tốc mặc định phải còn≥100ngày dự phòng; ngoại lệ do người chơi chọn E102-C+E103-B/C được miễn nếu có trong bảng6.5. Deadline900 và mọi giá khác giữ nguyên. Ngoài snapshot cohesion60, kiểm tra chuẩn ở cohesion<20 mất thêm60ngày thành810, dự phòng90: điểm này chưa được miễn hoặc sửa.

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

Caller: chương trình kiểm tra đến ngày 450, xếp một lần theo epoch. F10 mở cách xử lý chuyên sâu; phương án cơ sở đã có từ chương trình. Hạn cam kết là mốc sớm kiểm tra 690 tính từ bắt đầu.

| Lựa chọn | Giá | Kết quả |
| --- | --- | --- |
| A — Cam kết nộp hồ sơ đầy đủ đúng hạn | 0 PP | Đủ 4/4 trước hoặc đúng 690 được chấp nhận và giữ thưởng sớm. Nếu thiếu: cohesion -6; thẩm định lại chạy tuần tự sau cả hạn cam kết và chứng cứ ban đầu, thêm 180 ngày. |
| B — Xin gia hạn, công khai phần còn thiếu | 30 PP | Hạn hợp đồng 810 ngày; đủ chứng cứ mới được chấp nhận. Hủy thưởng PP sớm, không hủy quyền mở dự án phụ nếu programme thực sự full sớm. |
| C — Công bố kết quả có giới hạn | 15 PP | Chốt hợp đồng partial; programme vẫn tiếp tục kiểm chứng tới deadline. Bỏ thưởng PP sớm, vẫn có thể full/tier khi đủ 4/4. |

**Một quy tắc tuần tự:** T là ngày sẵn sàng đủ chứng cứ, gồm trễ E102-C. Nếu A chưa đủ ở hạn cam kết thì ngày full tiềm năng = max(T,690)+180; không chạy thẩm định lại song song. B/C không thêm thẩm định lại do bị bác, vẫn phải có chứng cứ thật. B trượt hạn hợp đồng không tự chốt mission thất bại; programme được đánh giá độc lập ở 900. C không tự tạo nhóm mục tiêu còn thiếu.

**Tổ hợp E102 × E103, tính bằng script.** Tập thể và cân bằng có cùng lịch chuẩn trong bảng; cấp tốc chỉ hợp lệ ở tập trung. Kiêm nhiệm không rút lại timer programme. Ngày full tiềm năng giả định kiến nghị đã được xử lý; thiếu kiến nghị sẽ hiển thị thiếu mục tiêu, không tự full.

| Tuyến | Mode | E102 | E103 | Ngày full tiềm năng | Programme | Hợp đồng | Dự phòng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | E102-A | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-A | E103-B | 750 | full | extended | Trong dự phòng |
| collective | standard | E102-A | E103-C | 750 | full | partial | Trong dự phòng |
| collective | standard | E102-B | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-B | E103-B | 750 | full | extended | Trong dự phòng |
| collective | standard | E102-B | E103-C | 750 | full | partial | Trong dự phòng |
| collective | standard | E102-C | E103-A | 1020 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-C | E103-B | 840 | full | extension_missed | Ngoại lệ lựa chọn |
| collective | standard | E102-C | E103-C | 840 | full | partial | Ngoại lệ lựa chọn |
| central | standard | E102-A | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-A | E103-B | 735 | full | extended | Trong dự phòng |
| central | standard | E102-A | E103-C | 735 | full | partial | Trong dự phòng |
| central | standard | E102-B | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-B | E103-B | 735 | full | extended | Trong dự phòng |
| central | standard | E102-B | E103-C | 735 | full | partial | Trong dự phòng |
| central | standard | E102-C | E103-A | 1005 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-C | E103-B | 825 | full | extension_missed | Ngoại lệ lựa chọn |
| central | standard | E102-C | E103-C | 825 | full | partial | Ngoại lệ lựa chọn |
| central | fast_paid | E102-A | E103-A | 645 | full | accepted | Trong dự phòng |
| central | fast_paid | E102-A | E103-B | 645 | full | extended | Trong dự phòng |
| central | fast_paid | E102-A | E103-C | 645 | full | partial | Trong dự phòng |
| central | fast_paid | E102-B | E103-A | 645 | full | accepted | Trong dự phòng |
| central | fast_paid | E102-B | E103-B | 645 | full | extended | Trong dự phòng |
| central | fast_paid | E102-B | E103-C | 645 | full | partial | Trong dự phòng |
| central | fast_paid | E102-C | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | fast_paid | E102-C | E103-B | 735 | full | extended | Trong dự phòng |
| central | fast_paid | E102-C | E103-C | 735 | full | partial | Trong dự phòng |

**Ngoại lệ partial do lựa chọn.** Tooltip A hiển thị T, phép cộng tuần tự, ngày full tiềm năng và kết quả ở deadline trước khi chọn. Bảng xác nhận đường thay thế trước khi cam kết, hoặc partial rõ ràng sau khi đã cam kết; không có fail giấu kín.

| Tổ hợp lựa chọn | Ngày full tiềm năng | Kết quả | Lý do | Đường thay thế / phục hồi |
| --- | --- | --- | --- | --- |
| collective / standard / E102-A / E103-A | 930 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| collective / standard / E102-B / E103-A | 930 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| collective / standard / E102-C / E103-A | 1020 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| central / standard / E102-A / E103-A | 915 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| central / standard / E102-B / E103-A | 915 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| central / standard / E102-C / E103-A | 1005 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |
| central / fast_paid / E102-C / E103-A | 915 | partial ở deadline | A cam kết quá sớm, bị bác; +180 tuần tự | Chọn B hoặc C ngay từ E103 giữ đường full trước 900; sau khi A bị bác không xóa timer, chốt partial rõ ràng |

**Ngoại lệ full đã chốt:** chỉ người chơi chọn E102-C kết hợp E103-B hoặc C. Bảng riêng bên dưới ghi mọi mode/tuyến hợp lệ, ngày full, dự phòng900−full và thưởng sớm0; chúng không là đường mặc định. Các lựa chọn không đổi deadline900 hoặc có cơ chế bù. Tooltip E102-C/E103-B/C trước khi chọn ghi: “Dự phòng còn X ngày; chậm thêm sẽ rơi xuống partial.” X lấy từ timer hiện hành; câu này nghĩa là chậm thêm vượt hết X, đúng ngày900 vẫn xét full nếu đủ4/4. I3/I10 còn vướng: trong E102-C, C rẻ hơn B15PP ở mọi k/r và cùng ngày/cohesion/cơ hội đã mô hình hóa; B chỉ khác trạng thái hợp đồng được chấp nhận. Báo lệch này, giữ nguyên giá/hậu quả, chưa bổ sung thưởng cho B.


**Bảng ngoại lệ full và ngân sách đã tính lại.**

Các bảng dùng snapshot cohesion 60, tier cán bộ 0 và timer đã ký. Toàn bộ tổ hợp mode/tuyến hợp lệ của snapshot được liệt kê; k/r không thay timer. Khi cohesion hoặc trì hoãn khác làm đổi timer, tooltip phải tính lại X, không lấy một số cố định từ bảng.

| Tuyến | Mode | E102 | E103 | Ngày full | Dự phòng còn | Thưởng PP sớm | Kết quả |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | C | B | 840 | 60 | 0 | full |
| collective | standard | C | C | 840 | 60 | 0 | full |
| balanced | standard | C | B | 840 | 60 | 0 | full |
| balanced | standard | C | C | 840 | 60 | 0 | full |
| central | standard | C | B | 825 | 75 | 0 | full |
| central | standard | C | C | 825 | 75 | 0 | full |
| central | fast_paid | C | B | 735 | 165 | 0 | full |
| central | fast_paid | C | C | 735 | 165 | 0 | full |
| central | fast_override | C | B | 735 | 165 | 0 | full |
| central | fast_override | C | C | 735 | 165 | 0 | full |
| central | combined_fast_paid | C | B | 735 | 165 | 0 | full |
| central | combined_fast_paid | C | C | 735 | 165 | 0 | full |

**Mọi tổ hợp full sau mốc sớm:** đường chuẩn A/B+B/C vẫn là mặc định đủ dự phòng; C+B/C là ngoại lệ được chốt. k/r không đổi ngày nên không lặp hàng theo k/r.

| Tuyến | Mode | E102 | E103 | Ngày full | Dự phòng còn | Thưởng PP sớm | Phân loại |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | A | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | A | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | B | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | B | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | C | B | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| collective | standard | C | C | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| balanced | standard | A | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | A | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | B | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | B | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | C | B | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| balanced | standard | C | C | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| central | standard | A | B | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | A | C | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | B | B | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | B | C | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | C | B | 825 | 75 | 0 | Ngoại lệ lựa chọn |
| central | standard | C | C | 825 | 75 | 0 | Ngoại lệ lựa chọn |
| central | fast_paid | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_paid | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_override | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_override | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | combined_fast_paid | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | combined_fast_paid | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |

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

## 7. Mục tiêu phát hành: 60–80 focus, mở theo đại hội

### 7.1. Quy mô theo lựa chọn thực tế

**Mục tiêu thiết kế hiện tại là 74 focus:** 2 node chuẩn bị năm 2000 và 12 node cho mỗi kỳ IX–XIV. Đây là một phương án trong khung 60–80, có thể điều chỉnh khi thử nghiệm. Số 48 của bản trước không còn là chỉ tiêu phát hành.

Tăng số focus để thêm vấn đề, phương án và hậu quả. Thời lượng focus được chọn theo hành động thông qua chính sách; mission vẫn xử lý triển khai. Các node bổ sung đã có hậu quả cụ thể ở bảng dưới, không còn chỉ là vị trí dự phòng.

| Kỳ mở | Nhóm | Số node | Lựa chọn chính |
| --- | --- | ---: | --- |
| Năm 2000 | F01–F02 | 2 | Rà soát và chuẩn trách nhiệm |
| IX, 2001 | F03–F12 + IX11–IX12 | 12 | Tham vấn/chỉ đạo; luân chuyển/giữ đội thí điểm |
| X, 2006 | X01–X12 | 12 | Vốn DNNN, mở cửa, giải ngân có điều kiện/cấp vốn trước |
| XI, 2011 | XI01–XI12 | 12 | Đất đai, bất động sản, trái phiếu, hỗ trợ/tái cơ cấu dự án |
| XII, 2016 | XII01–XII12 | 12 | Phân quyền, điều phối, bảo vệ người thực thi và nhân sự |
| XIII, 2021 | XIII01–XIII12 | 12 | Biển Đông, quan hệ lớn, dữ liệu, đối thoại/hiện diện |
| XIV, 2026 | XIV01–XIV12 | 12 | Xử lý tồn đọng, kiểm toán bàn giao, đội triển khai, kế cận |

Một lượt IX thực hiện khoảng 9 node vì F03/F04 cùng F05/F06 loại trừ theo tuyến, và IX11/IX12 là một lựa chọn. X/XI/XIII khoảng 11 node trước các gate tình huống; XII/XIV khoảng 9–10 khi đáp ứng thành tựu và tình huống. Đây là mục tiêu nhịp, cần đo số node thực sự khả dụng trong playtest.

Ở XII chỉ các cửa quy chế XII01/XII05 và hai kết quả chuyển giao XII04/XII08 loại trừ theo phương án. Các node trung gian và bốn hồ sơ chung không bị khóa thành toàn bộ cây phụ bốn focus. Phương án kiêm nhiệm cần roster phù hợp; người chơi giữ phân vai có lựa chọn công khai quyền hạn tương ứng tại XII11.

### 7.2. Gate theo kỳ và thời gian

`VIE_last_congress` lưu IX=9 đến XIV=14. Một focus cần kỳ tối thiểu, ngày neo, prerequisite và đúng chế độ. Điều kiện nằm trong `available`; AI dùng thêm trọng số riêng.

Ngày neo là ngày mở đại hội, còn node mở sau resolver đã giải quyết kỳ đó. Focus nền đã mở vẫn khả dụng ở kỳ sau; hợp đồng và nhân sự có cửa sổ riêng. Các node tương lai hiện mờ với tooltip ngày/kỳ.

**Ví dụ XI06 — nghĩa vụ trái phiếu:** kỳ đã giải quyết ≥11, ngày từ 12/01/2011, đã hoàn thành XI05 và điều kiện hồ sơ tài chính. Gate năm 2011 là lựa chọn bối cảnh game, không phải khẳng định năm ra đời thị trường. Phép ≥ trên biến dùng `compare = greater_than_or_equals` khi viết script.

X01–X04 giữ chuỗi DNNN, X05–X08 giữ chuỗi mở cửa. XI01–XI04 là đất đai, XI05–XI08 là tài chính. XIII01–XIII04 là Biển Đông, XIII05–XIII08 là quan hệ lớn. Node bổ sung nối vào hồ sơ thích hợp, không buộc làm hết hai cụm để mở mọi lựa chọn.

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

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| IX11 | Luân chuyển cán bộ trong đợt thí điểm | 5 | Event đổi người phụ trách dự án: 20 PP, cohesion +4 sau bàn giao, dự án +30 ngày; loại trừ IX12. |
| IX12 | Giữ người phụ trách đến nghiệm thu | 5 | Event giữ roster dự án: giữ tiến độ, mở yêu cầu kiểm toán độc lập 20 PP; loại trừ IX11. |

**X — ngày neo 18/04/2006.**

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| X01 | Công khai danh mục vốn nhà nước | 5 | Event chọn đối tượng kiểm toán |
| X02 | Tách bảo lãnh khỏi kế hoạch kinh doanh | 7 | Decision tái cơ cấu, chi phí chuyển đổi |
| X03 | Cổ phần hóa theo điều kiện công bố | 7 | Chuỗi đàm phán và trách nhiệm người mua |
| X04 | Kiểm toán sau chuyển đổi sở hữu | 3 | Milestone giám sát |
| X05 | Công bố quy trình chấp thuận đầu tư | 5 | Công cụ xử lý đầu tư minh bạch |
| X06 | Đàm phán tiêu chuẩn tiếp cận thị trường | 7 | Event đối tác chấp nhận/từ chối |
| X07 | Rà soát đầu tư tại ngành nhạy cảm | 7 | Event mở cửa–an ninh |
| X08 | Phân định trách nhiệm quản lý dữ liệu | 3 | Decision ngành có đánh đổi |
| X09 | Giải ngân vốn theo từng đợt kiểm chứng | 5 | Decision chia hai đợt vốn, mỗi đợt cần checkpoint kiểm toán; loại trừ X10. |
| X10 | Cấp vốn trước cho dự án trọng điểm | 5 | Event duyệt vốn trước: chi 0.50 ngân khố, rút 30 ngày dự án, mở kiến nghị giám sát; loại trừ X09. |
| X11 | Công khai bảo lãnh của doanh nghiệp | 7 | Event DNNN công bố nghĩa vụ: mở hồ sơ nợ và decision điều chỉnh bảo lãnh; bổ sung bằng chứng kiểm tra. |
| X12 | Tổ chức đối thoại về điều kiện đầu tư | 5 | Event bộ/ngành–doanh nghiệp: chọn giữ điều kiện hoặc mở có hậu kiểm; phản hồi đổi BoP ±0.05 một lần. |

**XI — ngày neo 12/01/2011.**

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| XI01 | Công bố hồ sơ thu hồi đất | 5 | Event địa phương–người dân–nhà đầu tư |
| XI02 | Lập quỹ đền bù trước triển khai | 7 | Decision chi ngân khố |
| XI03 | Mở phiên giải quyết tranh chấp đất | 7 | Đóng kiến nghị hoặc tạm dừng |
| XI04 | Kiểm tra nguồn thu từ đất | 3 | Event hụt thu và điều chỉnh ngân sách |
| XI05 | Rà soát tín dụng bất động sản | 5 | Kiểm tra dự án có vốn vay |
| XI06 | Yêu cầu công bố nghĩa vụ trái phiếu | 7 | Event tổ chức phát hành–người mua |
| XI07 | Tái cơ cấu dự án mất khả năng thanh toán | 7 | Hỗ trợ có điều kiện |
| XI08 | Bảo vệ người mua trong phương án xử lý | 3 | Milestone dân vận |
| XI09 | Lập quỹ xử lý dự án dở dang | 7 | Decision chi 0.50 ngân khố cứu dự án theo kiến nghị người mua; loại trừ XI10. |
| XI10 | Buộc dự án dở dang tái cơ cấu | 7 | Event chủ đầu tư và người mua chịu phương án tái cơ cấu: chậm 90 ngày, giữ ngân khố; loại trừ XI09. |
| XI11 | Công khai kết quả thanh tra đất đai | 5 | Công bố một hồ sơ cụ thể, đóng hoặc chuyển kiến nghị qua event dân vận; thưởng theo bằng chứng. |
| XI12 | Kiểm tra trách nhiệm bên bảo lãnh trái phiếu | 5 | Event xác định bên chịu trách nhiệm; mở decision bồi hoàn có điều kiện và hậu quả đối với nhóm lợi ích. |

**XII — ngày neo 20/01/2016.**

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| XII01 | Mở rộng quyền ký theo ủy quyền | 5 | Nâng quy chế sau 2016, không lặp F03 |
| XII02 | Giao quyền phê duyệt kèm hậu kiểm | 7 | Event trách nhiệm |
| XII03 | Công khai biên bản nghiệm thu cải cách | 7 | Checkpoint và cohesion có trần |
| XII04 | Chốt chuyển giao trước đại hội | 3 | Event tái nhiệm/chuyển giao |
| XII05 | Điều phối nhiều chương trình liên ngành | 5 | Quy chế mới sau 2016, không lặp F04 |
| XII06 | Phê chuẩn phương án kiêm nhiệm dài hạn | 7 | Event thay điều kiện nhiệm kỳ, không lặp bonus ký |
| XII07 | Kiểm tra trách nhiệm người đứng đầu | 7 | Event giám sát |
| XII08 | Bàn giao hai chức vụ theo kế cận | 3 | Kiện toàn nhiều vai trò |
| XII09 | Ban hành quy trình bảo vệ quyết định đúng | 7 | Mở lựa chọn thẩm định trách nhiệm trước ký trong E103 kế tiếp; phải hoàn thành đào tạo 90 ngày. |
| XII10 | Đặt thời hạn xử lý hồ sơ liên ngành | 5 | Decision xử lý một hồ sơ tồn đọng 180 ngày; chọn đầu mối hoặc hội đồng, trả PP/cohesion theo cách làm. |
| XII11 | Công khai quyền hạn khi kiêm nhiệm | 5 | Event giám sát roster kiêm nhiệm hoặc phân vai: công bố quyền hạn, mở checkpoint kiểm tra người đứng đầu. |
| XII12 | Thẩm định phương án thay người giữa nhiệm kỳ | 5 | Event tái phân công vai trò: lựa chọn bàn giao 60 ngày hoặc kiện toàn ngay với mất cohesion được công bố. |

**XIII — ngày neo 25/01/2021.**

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| XIII01 | Thiết lập kênh xử lý sự cố trên biển | 5 | Event đối thoại/ứng phó |
| XIII02 | Giao nhiệm vụ phối hợp chấp pháp | 7 | Decision có deadline |
| XIII03 | Công bố lập trường tại diễn đàn khu vực | 7 | Phản hồi đối tác |
| XIII04 | Bảo vệ hoạt động kinh tế biển | 3 | Công cụ giảm tổn thất hoặc tăng áp lực |
| XIII05 | Đa dạng hóa hợp đồng và đối tác | 5 | Đàm phán hữu hạn |
| XIII06 | Công khai giới hạn hợp tác an ninh | 7 | Event an ninh–ngoại giao |
| XIII07 | Đàm phán quyền tiếp cận có điều kiện | 7 | Đối tác chọn |
| XIII08 | Điều chỉnh hợp tác sau khủng hoảng | 3 | Thay điều kiện theo kết quả |
| XIII09 | Công khai điều kiện hợp tác kỹ thuật | 5 | Event đối tác–an ninh xác nhận quyền dữ liệu; mở hợp đồng hữu hạn nối tiếp E104, cửa sổ 25 ngày (giả định gameplay); tier 2 trở lên hoặc kiêm nhiệm có thể ký đúng hạn, tier 1 có phương án thu hẹp. |
| XIII10 | Xử lý sự cố trên biển qua đối thoại | 5 | Event đối tác chấp nhận hoặc từ chối kênh đối thoại; loại trừ XIII11 trong cùng hồ sơ sự cố. |
| XIII11 | Duy trì hiện diện chấp pháp sau sự cố | 7 | Decision 180 ngày có ngân sách, sự kiện phản hồi và rủi ro tăng áp lực; loại trừ XIII10. |
| XIII12 | Điều chỉnh hợp đồng sau cảnh báo an ninh | 5 | Chọn sửa điều kiện dữ liệu hoặc hủy hợp đồng; trả giá mất hỗ trợ hoặc kéo dài xác minh. |

**XIV — ngày neo 19/01/2026.**

| Node | Focus | Cost | Hậu quả cụ thể |
| --- | --- | ---: | --- |
| XIV01 | Áp chuẩn công vụ sau thí điểm | 5 | Tier theo thành tựu |
| XIV02 | Công khai kết quả kiểm toán nhiệm kỳ | 7 | Resolver vốn nhà nước |
| XIV03 | Nghiệm thu dịch vụ và đền bù | 7 | Kết quả tại địa điểm |
| XIV04 | Bàn giao chương trình cho nhiệm kỳ mới | 3 | Giữ nhiệm vụ cục bộ hợp lệ |
| XIV05 | Gia hạn chương trình chưa hoàn thành | 5 | Event gia hạn một hồ sơ 180 ngày, 30 PP, giữ đánh giá partial và bỏ thưởng sớm; loại trừ XIV06. |
| XIV06 | Chuyển nguồn lực khỏi chương trình thất bại | 5 | Event đóng hồ sơ không đạt, bảo toàn nguồn lực còn lại, mở chương trình phục hồi có mục tiêu mới; loại trừ XIV05. |
| XIV07 | Kiểm toán kết quả bàn giao | 7 | Decision kiểm toán 180 ngày; công bố chênh lệch giữa báo cáo cũ và nghiệm thu, cập nhật milestone theo kết quả. |
| XIV08 | Giữ nhóm chuyên môn qua chuyển giao | 5 | Event giữ đội triển khai trong khi đổi lãnh đạo; chi 25 PP và giảm 30 ngày gián đoạn dự án; loại trừ XIV09. |
| XIV09 | Thay nhóm triển khai sau kiểm toán | 5 | Event đổi đội phụ trách: dự án +30 ngày, xử lý kiến nghị nhân sự theo chứng cứ; loại trừ XIV08. |
| XIV10 | Công khai cam kết dịch vụ đã nghiệm thu | 3 | Event địa phương phản hồi cam kết; trao idea ổn định 365 ngày chỉ khi đã có nghiệm thu tương ứng. |
| XIV11 | Rà soát hợp đồng có nghĩa vụ kéo dài | 5 | Mở danh sách hợp đồng đang hiệu lực và lựa chọn giữ, sửa hoặc chấm dứt với giá có thật; hồ sơ gia hạn có cửa sổ 21 ngày (giả định gameplay), tier 3 hoặc kiêm nhiệm ký kịp, các tier thấp hơn chọn sửa/chấm dứt. |
| XIV12 | Chốt phương án chuyển giao năm 2031 | 7 | Event chuẩn bị roster kế tiếp, kiểm tra kiêm nhiệm và kế cận; tạo phương án cho XV giả định, chưa tự thay người. |


### 7.5. Điều kiện hoàn thiện sau playtest

74 là danh mục thiết kế có nội dung, chưa phải 74 node đã cân bằng hoặc triển khai. Trước hết làm lát cắt; sau đó dựng từng gói nhiệm kỳ, kiểm tra mỗi focus có caller, tool hoặc hậu quả thực thi.

Đo khoảng 90 ngày một lần: node khả dụng, node bị khóa theo lựa chọn, hồ sơ đang chạy, và vấn đề người chơi còn cần giải quyết. Nếu thiếu lựa chọn thì thêm node có gate, prerequisite và effect riêng; nếu một node chỉ lặp chức năng, gộp hoặc viết lại.

Nhịp mong muốn khoảng 10 lựa chọn thực hiện đáng cân nhắc mỗi nhiệm kỳ. Khung 60–80 cho phép thay đổi cấu trúc theo dữ liệu; số node lớn không thay thế kiểm tra chất lượng. Các lần thử XII và XIV phải kiểm tra riêng việc người chơi có quá ít node dù toàn tầng có 12.

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
| BoP | Engine BoP |
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

UI hiển thị mốc600/690, deadline900, ký45/30/25/21 và giá sau tier/cohesion. Giá mỗi checkpoint thương lượng15PP+0.25ngân khố, gói trả đủ55PP+0.50; vượt8cohesion/cổng sau trừ≥40. Báo trước BoP+0.30→+0.20: giữ timer hiện tại, khóa cấp tốc lần tới. E103-A hiển thị max(T,690)+180. E102-C/E103-B/C hiển thị ngày full, dự phòng X, kết quả partial nếu chậm vượt X; đối chiếu bảng ngoại lệ6.5, không có thưởng sớm cho ngoại lệ. Ký IX/XIII09/XIV11 có cửa sổ30/25/21ngày. Dự án phụ:30PP/270ngày, deadline chuẩn bị kỳ sau, guard một lần. k là tham số kiểm tra, không hiển thị như tỷ giá thật của game.

AI chọn cấp tốc khi ngày dư mở dự án phụ hoặc có nhu cầu/cơ hội có hạn; so cả55PP+0.50ngân khố với phương án chuẩn, không lấy thưởng50PP làm lợi nhuận chắc chắn. AI kiểm cổng cohesion sau trừ và kho bạc đủ trả0.25 ở mỗi checkpoint; không miễn phí phí thiếu. Giữ timer đã ký khi BoP giảm. Với E102-C+E103-B/C, AI đọc dự phòng còn60/75/165, không tính thưởng sớm hay dự án phụ; không chọn A nếu hồ sơ chắc trễ690. B cần giá trị chấp nhận hợp đồng được chốt, chưa gán trọng số thưởng mới để che lệch với C.

Tên focus phản ánh việc làm và event có source trung tâm quyết định. Những bonus chưa được đo giá kinh tế được đánh dấu trong review, không quy đổi tùy ý thành PP.

## 11. Bảng tính trước code và playtest theo hai bước

### 11.1. Bảng ngân sách một nhiệm kỳ

Nguồn duy nhất: [B1 JSON](VIETNAM_POLITICAL_PARAMETERS_VI.json), [script .py](VIETNAM_POLITICAL_BALANCE_VI.py), [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv), [báo cáo lượt 1](VIETNAM_POLITICAL_REVIEW_L1_VI.md). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py` để dựng lại CSV và bảng kiểm; kết quả là số học, chưa kiểm engine.

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

**So cùng E102-A, E103-B, k=40, r=1:** B đã bỏ thưởng PP sớm ở mọi tuyến. E104 dùng cùng phản hồi đối tác chấp nhận: phân vai tier0 lấy gói thu hẹp, kiêm nhiệm ký gói đầy đủ.

| Tuyến | Mode | Chi PP ròng | Chi ngân khố ròng | Ngày full | Thưởng PP sớm | Cohesion cuối | BoP cuối | Chi quy đổi | Dự án phụ mở |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | 225 | 1.0 | 750 | 0 | 70 | -0.3 | 235.0 | 0 |
| balanced | standard | 225 | 1.0 | 750 | 0 | 66 | 0 | 247.0 | 0 |
| central | standard | 225 | 1.0 | 735 | 0 | 66 | 0.3 | 247.0 | 0 |
| central | fast_paid | 280 | 1.5 | 645 | 0 | 66 | 0.2 | 322.0 | 1 |
| central | fast_override | 250 | 1.0 | 645 | 0 | 50 | 0.4 | 320.0 | 1 |
| central | combined_fast_paid | 355 | 1.0 | 645 | 0 | 60 | 0.3 | 395.0 | 1 |

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

Chiến tranh, counter reset, kiến nghị chưa đóng, công cụ mở muộn và chỉ tiêu kinh tế chưa đạt nằm ngoài lịch cơ sở. CSV không chứng minh full chắc chắn trong game. Checkpoint I3 đã đổi lựa chọn rẻ nhất theo k; ngoại lệ full I5 đã được chốt trong snapshot. E103-C còn trội B trong cặp ngoại lệ; vùng cohesion<20 còn thiếu dự phòng trên đường kiểm tra chuẩn. Các điểm này được báo, không chỉnh thêm số.

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
- I5: chuẩn/cấp tốc mặc định full trước900−100=800; deadline+900 cách chuẩn bị kỳ sau≥100. Ngoại lệ full chỉ E102-C+E103-B/C có bảng riêng, ngày/dự phòng và thưởng sớm0. Tooltip báo partial nếu chậm vượt dự phòng; kiểm đúng ngày900 và901. Cohesion<20/kiểm tra chuẩn810 còn cần chốt riêng, chưa được miễn.
- A-E103 thiếu hồ sơ phải bị bác; trả PP gia hạn không tạo hồ sơ.
- E104 dùng cùng nhân vật/đối tượng E102; dữ liệu hợp đồng và an ninh xuất hiện trong review.
- BoP dịch -0.05/+0.05 theo checkpoint thật, lặp hành động không farm thanh.
- Tier cán bộ và kiêm nhiệm có đường đạt cửa sổ ngay khi đủ điều kiện.
- Thu/chi, cohesion được duy trì đủ 90 ngày; corruption ở đáy dùng mục tiêu thay thế.
- Tập thể/tập trung có trade-off về PP, tiền, cohesion và cơ hội; không kết luận thống trị từ một chỉ số.
- Kiểm tra biên BoP ±0.25, cohesion 19/20/39/40/54/55/69/70, ngày 600/690/900, hạn ký 30/25/21 ngày, load save trước resolver.
- Gate 2006/2011/2016/2021/2026 chặn chọn sớm; mỗi gói có khoảng 10 lựa chọn đáng cân nhắc trong một lượt; cost đúng defines.
- Counter liên tục theo ngày chỉ chạy trên chương trình active của VIE; content validation để GitHub CI.
- Cohesion 0→40 có đường phục hồi số học 630 ngày; playtest xác nhận với thu nhập/event thực.

## 12. Trạng thái hoàn thành

Đã cập nhật lượt1 theo hai quyết định người dùng và tính CSV từ B1: checkpoint15PP+0.25ngân khố, gói55PP+0.50, thưởng50; ngoại lệ full E102-C+E103-B/C có bảng riêng, không thưởng sớm. I2 PASS theo PP thuần; checkpoint I3 PASS với biên k40 chỉ1PP; I3 còn FAIL trong cặp E103-B/C. I5 đạt trong snapshot, chưa đạt ở cohesion<20/kiểm tra chuẩn810. I10 không có tổ hợp thống trị toàn bộ hoặc từng tuyến ở mọi k/r đã kiểm, nhưng C trội B trong cặp ngoại lệ. Lượt2/3 và engine/playtest chưa chạy.

Mục tiêu phát hành 60–80 focus; danh mục hiện tại có 74 node, gồm hai mở đầu và 12 mỗi kỳ IX–XIV. Chưa triển khai game, audit chéo đầy đủ hoặc chạy console/20–30 năm. Các nguồn lịch sử đã giữ từ bản được xác minh; ID treaty và behavior corruption tại đáy vừa được đối chiếu code.

BLUF
