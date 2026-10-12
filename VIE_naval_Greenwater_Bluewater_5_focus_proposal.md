# Đề xuất nội dung Greenwater / Bluewater — 12/10/2026

Trạng thái: nội dung/reward V35.4 đã triển khai; v47 bổ sung root riêng chọn Greenwater/Bluewater; v48 đặt F02 chỉ cần F01; v49 đặt F01 cần P06 AND (G03 OR B03). Bố cục hiện hành là H02 → G00/B00 → hai cột hai focus → G03/B03. Mỗi hướng có sáu focus; bảng năm focus và tọa độ cũ bên dưới là bản đề xuất ban đầu, xem `VIE_naval_V35_implementation.md` để lấy cấu trúc hiện hành. Các mức thưởng, chi phí và ngưỡng lực lượng là thiết kế cân bằng gameplay, chưa nghiệm thu runtime.

## 1. Cấu trúc và điều kiện

Mỗi hướng có đúng năm focus, bao gồm các focus thể hiện lựa chọn định hướng. Không thêm một root thứ sáu. Giữ H02 là nền tảng chung, giữ G03/B03 là ID hội tụ đang được F01 và refresh tham chiếu.

```text
                    H02 — Nhóm tác chiến đa nhiệm
               /                                      \
       GREENWATER                                  BLUEWATER
 G01                 G04                     B01                 B04
 Huấn luyện cụm      Huấn luyện tàu           Huấn luyện          Huấn luyện tàu
 tác chiến biển gần  ngầm tiến công           hạm đội biển xa     ngầm viễn dương
  |                   |                       |                   |
 G02                 G05                     B02                 B05
 Cụm hộ tống và      Lực lượng tàu            Cụm tác chiến       Bảo đảm và triển
 săn ngầm khu vực    ngầm biển gần            mặt nước–hàng không khai biển xa
   \                 /                         \                 /
      G03 — Kiểm soát vùng biển                    B03 — Hạm đội viễn dương
```

- G01 và G04 cùng yêu cầu H02; G02 yêu cầu G01; G05 yêu cầu G04. G03 yêu cầu G02 AND G05, suy ra phải hoàn tất đủ bốn focus.
- B01 và B04 cùng yêu cầu H02; B02 yêu cầu B01; B05 yêu cầu B04. B03 yêu cầu B02 AND B05.
- Lựa chọn định hướng được thể hiện ở các focus đầu cột. G01/G04 loại trừ B01/B04 đối xứng; hai focus cùng hướng không loại trừ nhau. Hoàn thành focus đầu bất kỳ xác lập hướng đó. Không cho B04 trở thành cửa sau bỏ qua mutex G01/B01 hiện tại.
- Các quan hệ trong từng cột nằm ở prerequisite, không chuyển sang available. Điều kiện thực tế về tàu, ngân sách và kết quả chương trình có tooltip riêng.
- Bản đề xuất ban đầu dùng F01 = P06 OR G03 OR B03, đã được thay bởi V49: P06 AND (G03 OR B03). F02 chỉ cần F01 theo V48. I07/I08 và tàu sân bay không bắt buộc.
- Việc chọn hướng VIE không tự chọn hoặc hoàn tất grand doctrine/subdoctrine MD. Giữ quyền lựa chọn doctrine của người chơi.

Tọa độ đề xuất dưới đây lấy H02 làm `(0,0)` trong cụm; chưa phải tọa độ tuyệt đối toàn cây:

| Hàng | Green trái | Green phải | Blue trái | Blue phải |
|---|---|---|---|---|
| 1 | G01 (-6,1) | G04 (-2,1) | B01 (2,1) | B04 (6,1) |
| 2 | G02 (-6,2) | G05 (-2,2) | B02 (2,2) | B05 (6,2) |
| 3 | G03 (-4,3), giữa hai cột | | B03 (4,3), giữa hai cột | |

Neo các focus hàng 1 vào H02; hàng 2 vào cha cùng cột; G03 neo vào G02 với `(2,1)` và B03 neo vào B02 với `(2,1)`. Khi code phải cộng tọa độ tuyệt đối, rà các cụm lân cận và vị trí P06/F01 trước khi chốt. Gap cùng hàng là 4.

Hai focus huấn luyện mỗi hướng: cost 5, dự kiến 50 ngày/focus. Hai focus tổ chức lực lượng: cost 7, 70 ngày/focus. Capstone: cost 7, 70 ngày. Tổng đường hoàn chỉnh là 310 ngày focus; thời gian chương trình đầu tư tính riêng.

## 2. Nội dung Greenwater

Greenwater hướng đến kiểm soát vùng biển và bảo vệ tuyến hàng hải khu vực bằng tàu mặt nước, tàu ngầm và hiệp đồng với lực lượng trên bờ. Trong provider MD, `green_water` được mô tả là regional power projection, có hai track capital ships, hai escort ships, một submarines và một operations. Vì vậy nội dung này rộng hơn tuần tra sát bờ; tác chiến ven bờ chỉ là một thành phần.

### G01 — Huấn luyện cụm tác chiến biển gần

Nội dung: chuẩn hóa chỉ huy cụm, liên lạc, chia sẻ tình huống và phân công tàu tuần tra–tàu bảo vệ; diễn tập hiệp đồng với không quân và cơ sở quan sát trên bờ. Hình thành quy trình dùng lực lượng đã có.

Reward đề xuất:

- 10 naval mastery nếu đã chọn grand doctrine; nếu chưa, 10 navy XP, qua helper cùng mẫu `VIE_nav_xp_*`.
- 10 command power.
- `naval_coordination` +3%.
- Xác lập hướng Greenwater; starter idea chỉ xuất hiện một lần dù G04 được hoàn thành trước hay sau.

### G02 — Tổ chức cụm hộ tống và săn ngầm khu vực

Nội dung: xây dựng cơ cấu cụm tàu hộ tống, phân công tàu mặt nước bảo vệ, chuẩn hóa khai thác sonar và hiệp đồng phương tiện săn ngầm. Kết nối học thuyết với lực lượng corvette/frigate hiện có và chương trình Sông Thu.

Reward đề xuất:

- 15 command power.
- `screening_efficiency` +4%.
- `navy_submarine_detection_factor` +4%: đây là năng lực phát hiện tàu ngầm, không đồng nhất với tăng sức tấn công tàu ngầm.
- Một bonus nghiên cứu 50%, một lượt, cho `CAT_naval_sonar`, giữ chuyên ngành bonus hiện tại.
- Lớp bảo đảm nội địa giữ điều kiện G02 AND hợp đồng Sông Thu đã bàn giao: `repair_speed_factor` +3%, `screening_efficiency` +2%. Focus mở khung tổ chức; chưa có tàu Sông Thu thì chưa nhận lớp bảo đảm này. Kiểm cả hai thứ tự hoàn tất.

Thay dockyard trợ cấp đang gắn ở G02 bằng năng lực tổ chức và bảo đảm. Phần công trình thuộc chuỗi công nghiệp, cần xử lý theo chương trình công nghiệp có địa điểm/chi phí hợp lệ khi triển khai.

### G04 — Huấn luyện kíp tàu ngầm tiến công

Nội dung: chuẩn hóa kíp tàu, diễn tập kiểm soát hư hỏng, sử dụng khí tài và phối hợp chỉ huy; hình thành năng lực duy trì tàu ngầm hoạt động trong khu vực.

Reward đề xuất:

- 10 naval mastery hoặc navy XP theo trạng thái doctrine.
- 10 command power.
- `navy_submarine_defence_factor` +3%.
- Xác lập cùng hướng Greenwater nếu đây là focus đầu tiên hoàn thành; không phát lại starter hay thưởng của G01.

### G05 — Xây dựng lực lượng tàu ngầm biển gần

Nội dung: tổ chức phân đội tàu ngầm tiến công, chu kỳ trực chiến–huấn luyện–bảo dưỡng và phối hợp với cụm mặt nước. Đây là tổ chức lực lượng tác chiến; chưa phải chương trình tàu ngầm mang tên lửa đạn đạo.

Reward đề xuất:

- 15 command power.
- `navy_submarine_attack_factor` +5%.
- Một bonus nghiên cứu 25%, một lượt, cho `CAT_attack_submarines`.
- Mở kiểm tra lực lượng cho capstone: tàu ngầm thực tế được mua/đóng qua hệ thống trang bị hiện hành. Focus không tạo tàu hoặc variant.

### G03 — Lực lượng kiểm soát vùng biển

Nội dung: nghiệm thu khả năng hiệp đồng mặt nước–tàu ngầm, bảo vệ tuyến hàng hải và duy trì luân phiên trực chiến khu vực.

Gate đề xuất: G02 AND G05; có căn cứ hải quân đang sở hữu/kiểm soát; tối thiểu hai tàu mặt nước thuộc nhóm corvette/frigate/destroyer và một tàu thuộc nhóm `attack_submarine`. Đây là ngưỡng tổ chức gameplay, không phải biên chế lịch sử. Phải đối chiếu bộ đếm provider khi code; không tự tạo task force hoặc ép đội hình của người chơi.

Reward đề xuất:

- 20 naval mastery hoặc navy XP; 25 command power.
- Một giảm chi phí doctrine 35%, một lượt, chuyển từ điểm chọn hướng sang nghiệm thu để chỉ nhận một lần.
- `navy_org_factor` +4%; `naval_coordination` +2%.
- Idea Greenwater capstone thay starter: tổng trong idea là screening +9%, convoy escort +8%, organization +4 điểm, chi phí nhân sự hải quân +10%.
- Các mức idea là giá trị thay thế, không cộng thêm starter. Khi F02 hoàn tất, profile cuối thay capstone theo cơ chế refresh: screening +12%, convoy escort +10%, organization +6 điểm, nhân sự +10%.
- Capstone mở F01; không tự cấp tên lửa, SAM hoặc khí tài.

Tổng phần thưởng trực tiếp năm focus: 40 XP/mastery và 75 command power, giữ tổng hiện có của tuyến ba focus. Ngoài profile thay thế: coordination +5%, screening +4%, submarine detection +4%, submarine attack +5%, submarine defence +3%, organization factor +4%. Lớp Sông Thu bổ sung repair +3% và screening +2% khi hợp đồng thực sự hoàn tất.

## 3. Nội dung Bluewater

Bluewater phát triển tác chiến hạm đội ngoài vùng hỗ trợ thường xuyên của bờ, kết hợp mặt nước, tàu ngầm và bảo đảm triển khai dài ngày. Provider `blue_water` nhấn mạnh carrier/global power projection, có track tàu ngầm và cho phép underway replenishment qua effect của doctrine. Có nội dung hàng không hạm là hợp lý; năng lực này phát triển theo lực lượng thực tế thay vì trao tàu sân bay miễn phí.

### B01 — Huấn luyện hiệp đồng hạm đội biển xa

Nội dung: chuẩn hóa sở chỉ huy hạm đội, phối hợp đội tàu hộ tống và tàu chủ lực, diễn tập chỉ huy khi tách xa căn cứ; xây dựng quy trình triển khai dài ngày.

Reward đề xuất:

- 10 naval mastery hoặc navy XP; 10 command power.
- `naval_coordination` +3%.
- Xác lập hướng Bluewater; starter idea chỉ xuất hiện một lần dù B04 hoàn thành trước.
- Profile khởi đầu đề xuất: range +6%, chi phí nhân sự hải quân +25%. Không phát lại doctrine discount ở hai điểm vào.

### B02 — Cụm tác chiến mặt nước và hàng không hạm

Nội dung: tổ chức nhóm tàu mặt nước đa nhiệm, hộ tống phòng không/chống ngầm, đồng thời chuẩn bị đội ngũ và quy trình vận hành hàng không hạm. Có thể xây dựng cụm mặt nước trước và hoàn thiện carrier capability khi người chơi sở hữu tàu sân bay.

Reward đề xuất:

- 15 command power.
- `screening_efficiency` +4%; `navy_anti_air_attack_factor` +3%.
- Event lựa chọn bonus nghiên cứu, chỉ một phương án được nhận: `CAT_frigates` 25%/một lượt cho hướng nhóm mặt nước, hoặc `CAT_aircraft_carriers` 25%/một lượt cho hướng hàng không hạm. Lựa chọn bonus không thay hướng chính và không tự chọn doctrine.
- Đánh dấu hoàn thành chuẩn bị hàng không hạm. Lớp sẵn sàng hàng không hạm chỉ có hiệu lực khi còn sở hữu tàu loại `carrier` và đã chọn subdoctrine `carrier_operations`: `sortie_efficiency` +6%, `navy_carrier_air_targetting_factor` +3%. Khi thiếu điều kiện, lớp này tắt và có thể bật lại; không nhận lại XP/research/tiền.
- Tàu loại `helicopter_operator` không được coi là carrier có máy bay cánh bằng. Không tạo carrier/air wing/hull hoặc hoàn tất project từ reward này.

### B04 — Huấn luyện tàu ngầm viễn dương

Nội dung: đào tạo kíp triển khai dài ngày, tổ chức phiên trực, bảo đảm kỹ thuật và hiệp đồng với hạm đội. Trọng tâm là tàu ngầm tiến công thực hiện nhiệm vụ hỗ trợ hạm đội và kiểm soát biển.

Reward đề xuất:

- 10 naval mastery hoặc navy XP; 10 command power.
- `navy_submarine_defence_factor` +3%.
- Một bonus nghiên cứu 25%, một lượt, cho `CAT_attack_submarines`.
- Xác lập cùng hướng Bluewater nếu đây là focus đầu tiên; starter không cộng chồng với B01.

### B05 — Bảo đảm và triển khai lực lượng biển xa

Nội dung: thiết lập chu kỳ tiếp tế, bảo dưỡng và thay kíp cho tàu mặt nước và tàu ngầm; triển khai lực lượng tàu ngầm cùng kế hoạch hạm đội. Dùng logistics hiện có thay vì thêm một chương trình đóng tàu tiếp dầu mới.

Reward đề xuất:

- 15 command power.
- `navy_submarine_attack_factor` +3%; `repair_speed_factor` +3%.
- Chuyển quyền mở `VIE_nav35_blue_support_program` từ B02 sang B05 cho khớp nội dung. Giữ chương trình hiện có: 8 tỷ USD, 365 ngày, trừ một lần qua `modify_treasury_effect`.
- Focus mở chương trình; range +5% của chương trình chỉ có hiệu lực sau khi đầu tư hoàn tất. Lớp hàng không của B02 quản lý carrier sortie bonus; chương trình hậu cần không tự cấp thêm bonus carrier riêng.
- Chương trình hỗ trợ yêu cầu căn cứ và khả năng hậu cần phù hợp đang sở hữu/kiểm soát. Tình trạng hoàn tất và thưởng được bảo vệ chống gọi lại; nếu mất địa điểm khi đến hạn thì giữ trạng thái chờ và thử lại.
- Rule `can_use_underway_replenishment` do doctrine MD `blue_water` cấp. Chọn focus VIE hoặc hoàn tất đầu tư không tự mở rule này nếu người chơi chưa chọn doctrine tương ứng.

### B03 — Hạm đội viễn dương sẵn sàng triển khai

Nội dung: nghiệm thu cả chỉ huy, nhóm tàu mặt nước, tàu ngầm và bảo đảm dài ngày; chứng nhận hạm đội có thể triển khai ngoài khu vực biển gần.

Gate đề xuất: B02 AND B05; hoàn tất chương trình hỗ trợ biển xa; có căn cứ đang sở hữu/kiểm soát; tối thiểu hai tàu corvette/frigate/destroyer và một tàu `attack_submarine`. Tàu sân bay được phát triển qua lớp capability B02, không bắt buộc để mở B03/F01/F02.

Reward đề xuất:

- 20 naval mastery hoặc navy XP; 25 command power.
- Một giảm chi phí doctrine 35%, một lượt.
- `navy_org_factor` +4%; `naval_coordination` +2%.
- Profile Bluewater capstone thay starter: range +14%, organization +4 điểm, chi phí nhân sự hải quân +25%. Bonus carrier do lớp B02 quản lý để tránh cộng chồng.
- Profile sau F02 thay capstone: range +18%, organization +6 điểm, nhân sự +25%. Capstone mở F01.

Tổng trực tiếp năm focus: 40 XP/mastery và 75 command power. Ngoài profile thay thế: coordination +5%, screening +4%, naval AA +3%, submarine attack +3%, submarine defence +3%, repair +3%, organization factor +4%. Lớp carrier thêm sortie +6%, carrier targeting +3% khi đủ điều kiện.

## 4. Cân bằng và cơ chế effect

Các giá trị trên áp dụng cho phạm vi modifier country tương ứng. Ví dụ `navy_submarine_attack_factor` áp dụng cho tàu ngầm nói chung; không tuyên bố chỉ áp dụng riêng tàu ngầm attack hoặc chỉ một vùng biển. Modifier range áp dụng chung cho hải quân; các tên chương trình là ý nghĩa thiết kế, không phải cơ chế giới hạn theo fleet/sea zone.

Mỗi reward một lần có guard riêng theo focus. Refresh chỉ tính trạng thái/profile/capability, không cấp XP, tiền, tech, blueprint hoặc tàu. Chi phí nhân sự MD +10% Greenwater/+25% Bluewater giữ đúng một lớp profile, không cộng hai focus đầu hay starter–capstone–F02.

### Sai lệch audit hiện tại cần xử lý khi code

`balance_tests()` hiện cộng modifier trong idea nhưng chưa cộng giá trị từ `VIE_armed_forces_modifier`; interpreter còn bỏ qua `add_to_variable`. Do đó kết quả đạt trần range của audit cũ chưa phản ánh toàn bộ reward.

Riêng Bluewater hiện có +6%/+4%/+8% range từ B01/B02/B03 trong dynamic modifier. Cộng profile F02 +22% và chương trình hỗ trợ +5% đã thành +45%, chưa tính logistics chung. Không sao chép các khoản range này sang năm focus mới.

Phân bổ mới dự kiến đạt trần 34% của nội dung hải quân V35 ở đường cuối:

- Profile Bluewater F02: +18%.
- Logistics L04 dynamic: +5%.
- Chương trình hỗ trợ biển xa: +5%.
- VTĐN: +4%.
- Lớp cứu hộ L04: +2%.
- Tổng: +34%. Trước F02, profile capstone +14% cho tổng +30% nếu đã hoàn tất mọi chương trình trên.

Đây là phạm vi nhánh Hải quân V35, không bao gồm toàn bộ luật, doctrine và các nhánh khác của MD/VIE. Khi triển khai, audit phải cộng cả idea và dynamic; organization theo điểm (`navy_org`) và theo hệ số (`navy_org_factor`) phải báo riêng. Không dùng một trần điểm organization để chứng minh đã giới hạn cả hệ số.

Các khoản dockyard, cảng, convoy và tên lửa miễn phí hiện nằm trong G02/B02/G03/B03 được thay bằng nội dung năng lực trên. Công nghiệp đóng tàu và mua sắm giữ trách nhiệm tạo công trình, blueprint và tàu thật theo các hợp đồng hiện có. I07/I08 không bị sửa bởi đề xuất này.

### Nghiệm thu khi triển khai

- Kiểm từng hướng bắt đầu từ cột trái hoặc phải: khóa được hai điểm vào hướng đối lập, không khóa cột còn lại cùng hướng.
- Capstone khóa khi thiếu bất kỳ focus bắt buộc, lực lượng thực hoặc hỗ trợ đầu tư cần thiết; F01 vẫn nhận các đường OR hợp lệ.
- Không có carrier thì hoàn tất Bluewater được; bonus carrier vẫn tắt. Có đúng carrier và carrier_operations mới bật; mất tàu thì tắt; khôi phục không phát lại reward.
- Tổng 40 mastery/XP và 75 CP mỗi tuyến; kiểm cả hai trạng thái doctrine, cả thứ tự hoàn thành hai cột và gọi lại refresh/event.
- Event bonus B02 chỉ cho một lựa chọn research; gọi lại không đổi hoặc cấp thêm bonus.
- Programme hỗ trợ thu đúng 8 tỷ một lần, giữ thời gian 365 ngày, không cấp hiệu quả hoạt động trước hoàn tất.
- Kiểm tổng modifier idea + dynamic, từng nhóm profile không cộng chồng; XP/mastery cả tuyến V35 vẫn nằm trong ngân sách fixture.
- Rà tọa độ tuyệt đối, anchor trực tiếp, hội tụ AND, khoảng cách với nhánh phòng thủ và F01; sau đó kiểm UI trong game.

## 5. Nguồn và giới hạn

- Skill: `.claude/skills/md-focus/SKILL.md` và `references/focus-branch-design.md`.
- Live VIE: focus G01–G03/B01–B03; effect reward/refresh/blue support; idea doctrine/capstone và `tools/audit/naval_scenarios.py`.
- Provider đọc tại `D:/ide/Millennium-Dawn`: `common/doctrines/grand_doctrines/naval_doctrine.txt`, `common/doctrines/subdoctrines/sea/naval.txt`, `common/technologies/naval.txt`, `common/technologies/naval_modules.txt`. Xác nhận blue_water, green_water, carrier_operations, các modifier carrier và category corvette/frigate/attack submarine/aircraft carrier/sonar.
- [Royal Australian Navy — Sea control / Sea denial](https://seapower.navy.gov.au/glossary/s): tham khảo mục tiêu kiểm soát vùng biển và ngăn đối phương sử dụng vùng biển.
- [US Navy — Carrier Strike Group Nine](https://www.surfpac.navy.mil/Warships/Carrier-Strike-Group-9-CSG-9/About/): tham khảo cấu trúc hiệp đồng mặt nước, dưới mặt nước, hàng không và strike.

Thiết kế đã được triển khai và audit tĩnh trong V35.4; chưa nghiệm thu runtime. Các ngưỡng tàu, thời gian focus và tỷ lệ thưởng là giá trị cân bằng gameplay, không phải số liệu thống kê hoặc biên chế lịch sử. Provider MD có screen_destroyer là sub-unit riêng; bản triển khai đếm riêng loại này và kiểm sprite/texture của event nghiên cứu mới.
