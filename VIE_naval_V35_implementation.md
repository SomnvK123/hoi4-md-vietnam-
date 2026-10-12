# Hải quân V35 — hiện hành V35.4 / cây 47 focus (12/10/2026)

## Greenwater / Bluewater: root chọn hướng, hai nhánh, capstone

H02 mở hai root chọn hướng: G00 Greenwater và B00 Bluewater. Hai root loại trừ
nhau. Mỗi root tỏa ra hai cột, mỗi cột có hai focus, rồi hội tụ AND vào G03/B03.
G00 mở G01/G04; G02 cần G01, G05 cần G04; G03 cần cả G02 và G05. B00 mở
B01/B04; B02 cần B01, B05 cần B04; B03 cần cả B02 và B05. Root áp dụng profile
khởi đầu tương ứng; người chơi vẫn tự chọn grand doctrine MD. Mỗi hướng gồm sáu
focus, 360 ngày; reward nhánh giữ tổng 40 XP/mastery và 75 command power.
Root không cộng XP/CP; reward nhánh có guard nhận một lần.

Layout gom hai root quanh trục H02/F01 X=209; F02 chỉ nối thẳng dưới F01:

| Hàng | Greenwater | Bluewater | Điểm hội tụ |
|---|---|---|---|
| Y=8 | G00 X=206 | B00 X=212 | H02 X=209 phía trên; hai root cân giữa các cột con |
| Y=9 | G01 X=205, G04 X=207 | B01 X=211, B04 X=213 | hai cột song song |
| Y=10 | G02 X=205, G05 X=207 | B02 X=211, B05 X=213 | — |
| Y=11 | G03 X=206 | B03 X=212 | capstone hai hướng |
| Y=12 | — | — | F01 X=209 |
| Y=13 | — | — | F02 X=209 |

PNG biểu diễn tọa độ file; cần kiểm tra dây nối thực tế trong engine HOI4.

G03/B03 cần căn cứ ven biển đang sở hữu/kiểm soát, hai tàu mặt nước phù hợp và
một attack submarine; B03 còn cần đầu tư hỗ trợ biển xa hoàn tất. Tàu mặt nước
tính corvette, stealth corvette, frigate, stealth frigate, heavy frigate, destroyer,
stealth destroyer và screen destroyer. Provider MD xác nhận screen destroyer là
sub-unit riêng dùng equipment destroyer, nên trigger đếm riêng bằng biến engine.
Không cache bộ đếm tàu hằng tháng. Gate mất trong lúc chạy sẽ hủy focus theo
cancel_if_invalid; nghiệm thu đã hoàn tất giữ thưởng.

F01 yêu cầu P06 AND (G03 OR B03). F02 chỉ yêu cầu F01; S03, L04, I07/I08 và carrier
không bắt buộc. B02 mở event vie_nav35.14 chọn bonus frigate hoặc carrier 25%,
một lượt; guard kết quả ngăn replay. AI chọn carrier khi có carrier hoặc có
carrier_operations, còn lại chọn frigate.

Lớp dynamic hàng không hạm đăng ký từ B02, enable khi có carrier và
carrier_operations: sortie +6%, carrier targeting +3%. Mất điều kiện thì tắt,
khôi phục thì bật lại; helicopter_operator không thỏa gate. Không phát lại
reward hoặc tự chọn doctrine. Icon dùng sprite MD GFX_idea_navy_strengthened.

Chương trình hỗ trợ chuyển sang B05, giữ 8 tỷ USD/365 ngày. Ký cần căn cứ và
dockyard ven biển đang sở hữu/kiểm soát; tiền thu một lần qua modify_treasury_effect.
Đủ hạn nhưng mất địa điểm thì ready chờ scheduler. Kết quả chỉ range +5%, không
cấp sortie bonus trước/ngoài lớp carrier. Rule underway replenishment thuộc
grand doctrine blue_water của MD. Lớp bảo đảm Sông Thu giữ G02 AND bàn giao
thực tế, thưởng repair +3% và screening +2% đúng cả hai thứ tự hoàn tất.

Bỏ công trình/convoy/tên lửa/SAM miễn phí khỏi reward G/B; tạo tàu và blueprint
vẫn do công nghiệp/hợp đồng hiện có. Không thay I01-I08 hay OOB/provider MD.
Áp dụng game mới; không migration hoặc phát lại reward cho save cũ.

### Modifier và cân bằng V35.4

| Tuyến | Thưởng tích lũy từ năm focus, ngoài profile |
|---|---|
| Greenwater | coordination +5%, screening +4%, sub detection +4%, sub attack +5%, sub defence +3%, org factor +4% |
| Bluewater | coordination +5%, screening +4%, naval AA +3%, sub attack +3%, sub defence +3%, repair +3%, org factor +4% |

Greenwater profile khởi đầu screening/escort +5%/+4%; capstone +9%/+8% và
org +4 điểm; F02 +12%/+10% và org +6 điểm. Nhân sự +10% ở một profile duy nhất.
Bluewater profile range +6%/+14%/+18%, org capstone/F02 +4/+6 điểm, nhân sự +25%.
Starter/capstone/F02 thay nhau, không cộng chồng. Thưởng range dynamic của B01,
B02, B03 cũ đã bỏ; modifier từ các nhánh khác không bị reset.

Audit đã sửa interpreter để tính add_to_variable, CP, doctrine discount và lớp
dynamic có enable. Tổng range cuối Bluewater trong nội dung V35: profile 18%
+ L04 dynamic 5% + hỗ trợ 5% + VTĐN 4% + cứu hộ 2% = 34%. Org theo điểm và
org factor được báo riêng; trần org factor fixture là 50% cho nội dung V35.
Không tính luật/doctrine/nhánh khác. Các con số là cân bằng gameplay.

PNG và manifest lấy từ focus live, sprite/texture đăng ký thực:
`.claude/docs/naval/naval_v35_4.png` và `green_blue_v35_4.png`.
Tái xuất bằng `python tools/focus_layout/naval_diagram_v35_4.py`; không cần
matplotlib. PNG là sơ đồ tham chiếu, không xác nhận cách engine vẽ dây trong game.

Nghiệm thu tĩnh: `python tools/audit/naval_scenarios.py --md D:/ide/Millennium-Dawn`.
Kết quả 12/10/2026 sau V49: 1.292 scenario PASS; audit cây 408 focus tổng / 47 Hải quân,
không trùng vị trí, anchor treo/forward hoặc vòng prerequisite; references,
event, province, localization và git diff --check đều qua. DDS/GFX xác nhận
icon focus đăng ký đầy đủ, texture không thiếu; cảnh báo event picture ngoại
vi của audit local cần đối chiếu provider/base game, không coi là lỗi gameplay.
Riêng event mới vie_nav35.14 dùng GFX_naval_base với sprite và texture được
xác nhận tại provider MD; không thêm artwork hoặc sprite mới.
Runtime HOI4, save/load thật, Ship Designer và error.log chưa chạy.

Các mục V35.3/V35.2 bên dưới ghi lịch sử triển khai; phần V35.4 phía trên là
chuẩn hiện hành cho G/B, profile và điều kiện F02.

## Bổ sung khinh hạm tàng hình I08

V35.3 thêm focus tùy chọn I08 ngay dưới I07; F01/F02 không phụ thuộc I08.
I08 mở event phê duyệt, còn blueprint và hợp đồng chỉ dùng được sau khi hoàn
thành MD Special Project `sp_stealth_frigate` và có `stealth_frigate_hull_1`.
Project MD chỉ mở sau `frigate_hull_4` và cấp hull stealth bậc 1 khi hoàn tất;
mod không tự hoàn thành project hay cấp tech.

Blueprint VIE riêng dùng `stealth_frigate_hull_1`, hiện trong Ship Designer
trước hợp đồng. Mẫu lấy Istanbul-class làm cảm hứng đa nhiệm; mục tiêu gameplay
4.000 tấn không phải thuộc tính được HOI4 engine kiểm tra. Cấu hình provider đã
đối chiếu gồm diesel 2, fire control tích hợp, radar 4, VLS 16, CIWS 4, pháo
76 mm 3, bệ tên lửa quad, đạn balanced 3 và bãi đáp trực thăng 1. Hull stealth
MD chỉ có hai slot auxiliary và một slot cảm biến, nên blueprint không có slot
sonar/torpedo riêng; năng lực chống ngầm được mô phỏng qua đạn balanced và trực
thăng. Các công nghệ module phải được nghiên cứu riêng.

Hợp đồng gameplay đầu tiên thu 0,8 tỷ USD và chạy 1.460 ngày, bàn giao đúng
một tàu. Hợp đồng dùng chung giới hạn một tàu nội địa đang đóng; mất project,
tech, cảng hoặc xưởng khi đến hạn sẽ chờ scheduler, không hoàn tiền/thu lại hay
khởi động lại timer. Tàu tiếp theo được sản xuất bình thường từ blueprint.

Audit V35.3: `python tools/audit/naval_scenarios.py --md <MD checkout>`; fixture
kiểm gate project, slot/module, giao dịch, timer, khôi phục điều kiện và bàn giao
một lần. Runtime game/Ship Designer chưa chạy.

## Bổ sung công nghiệp đóng tàu V35.2 (nền hiện hành)

## Bổ sung công nghiệp đóng tàu V35.2

Bản này dành cho **game mới**. V35.2 giữ 40 focus, prerequisite, mutex và tọa độ V35;
không sửa history/OOB hoặc thiết kế của MD. Các mục V35.1 bên dưới là ghi nhận
bản trước; phần V35.2 thay thế những mô tả cũ về reward công nghiệp và bàn giao.

- I01 cần Treasury từ 8 tỷ và địa điểm R&D hợp lệ trước khi bắt đầu. Khi hoàn thành,
  tạo một `naval_facility`, ưu tiên 519 → 522 → 521, rồi thu đúng 8 tỷ qua Treasury MD.
  Không gọi helper giá 15 tỷ; không cấp scientist, research slot hoặc công nghệ.
  Focus tiếp tục nếu ngân sách/địa điểm mất giữa chừng; phần R&D chuyển sang pending
  và có decision hoàn tất sau, không phát lại reward focus khác.
- Bốn dockyard/slot I01/I02/I03/I05 là **trợ cấp miễn phí** theo lựa chọn người dùng.
  Ba Son: 519, Hồng Hà: 522, Sông Thu: 521. I07 trợ cấp một cấp căn cứ tại
  state 521, province 10309 (Đà Nẵng). Kiểm ownership/control/coast/capacity;
  công trình bị chặn chờ tại đúng địa điểm, slot không cấp lặp khi retry.
- Đầu tư công nghệ Molniya 1,5 tỷ/365 ngày và TT400 0,75 tỷ/180 ngày vẫn được giữ.
  Finish nhận bonus nghiên cứu một lượt và xếp hàng event phê duyệt. Event chỉ mở
  chương trình, không thu tiền, tạo blueprint hoặc cấp tàu.
- Decision chốt thiết kế không thu thêm tiền nhưng cần đầu tư tương ứng hoàn tất,
  R&D đang sở hữu/kiểm soát và đủ hull/module. Sông Thu cần chương trình Viện Thiết kế
  và tích hợp khí tài hoàn tất. Blueprint tạo trước hợp đồng và dùng được trong
  sản xuất thông thường.

| Hợp đồng chiếc đầu tiên | Tỷ USD | Ngày | Blueprint |
|---|---:|---:|---|
| Molniya | 0,15 | 730 | `VIE Molniya 12418`, `corvette_hull_2` |
| TT400TP | 0,05 | 365 | `VIE TT400TP`, `corvette_hull_2` |
| Sông Thu ASW | 0,6 | 1.095 | `Song Thu ASW 2026`, `frigate_hull_4` |

Giá/thời gian là cân bằng gameplay, không phải hợp đồng lịch sử. Tối đa một
hợp đồng đang đóng; không giữ chỗ production queue hoặc trừ vật liệu. Mỗi hợp đồng
thu tiền khi ký một lần. Finish kiểm đủ thời gian; thiếu căn cứ, xưởng hoặc công nghệ
thì ready chờ và scheduler thử lại. Blueprint, event phê duyệt và bàn giao có cờ
một lần; bàn giao không tạo lại variant.

Molniya dùng cấu hình module của Molniya Class trong nguồn MD, tạo variant VIE riêng
với `parent_version = 0`. TT400 mô phỏng tàu tuần tra/pháo bằng corvette, không có
tên lửa và không yêu cầu Jeune École. **Hiệu chỉnh theo slot MD:** slot sau corvette
không nhận fuel tank; đặt fuel tank ở auxiliary, CIWS ở front, rear để trống.
I03/TT400 dùng bonus `CAT_corvettes` 50%/25%, một lượt. I05 tiếp tục là năng lực
bảo đảm, chưa có tàu mới.

Provider đã đọc: `D:/ide/Millennium-Dawn`, gồm buildings, naval technologies,
module/hull slots, lịch sử state và tài liệu engine về construction/trigger.
`python tools/audit/naval_scenarios.py --md <MD checkout>` kiểm script live;
có thể thêm `--game` để kiểm engine/sprite provider như trước.
Runtime trong game: **NOT RUN**. Fixture không thay kiểm Ship Designer hoặc save HOI4.

Kết quả kiểm tra V35.2: 621 scenario tĩnh khi có provider MD (480 khi không
đối chiếu provider), gồm giao dịch, công trình, blueprint, ba hợp đồng và cân bằng.
Audit focus, references, event, localisation, province và diff đều đạt các mục
liên quan. Đối chiếu Git baseline xác nhận toàn bộ 401 focus giữ ID, tọa độ,
anchor, prerequisite, mutex và cost; chỉ năm reward focus công nghiệp được sửa.

## Bản triển khai V35.1 (11/10/2026) — ghi nhận lịch sử

Triển khai trực tiếp trên `main`, thay đúng 40 focus V34 bằng 40 focus
`VIE_nav35_*`. Tổng cây vẫn có 359 focus. Dành cho **game mới**; không có lớp
chuyển đổi save V34. Không thay history/OOB, thiết kế tàu của MD hoặc tài nguyên
ngoại giao đã chọn.

## Nguồn và phạm vi

- JSON `Hai_quan_V35_40_focus.json` là đặc tả quan hệ, năm, tên và nội dung;
  snapshot kiểm tra được lưu tại `tools/audit/naval_v35_spec.json`.
- HTML Organic Diamond là bản thiết kế hình học, không phải tọa độ engine.
  Root tuyệt đối `(210,2)`; nhánh chiếm X 197-224, Y 2-26. Tọa độ đã quy đổi
  thành relative offsets với anchor khai báo trước, là prerequisite trực tiếp.
- Đối chiếu MD Workshop `2777392649`, descriptor 2.0.2 / HOI4 1.19.* và
  tài liệu engine của HOI4 1.19.3. Không xác nhận playset đang hoạt động hoặc
  commit upstream. Cache `tools/audit/md_ref` không được coi là source đầy đủ.
- Các tài liệu cũ về ba trục và những file fragment đã bị xóa là tư liệu lịch sử,
  không phải cấu trúc live. Nội dung mới nằm trong các file consolidated.

## Cây và các tuyến

Giữ parent + `all` thành nhiều prerequisite AND, `any` thành một prerequisite
OR, mutex P01/H01 và G01/B01 đối xứng. N00 nối với `VIE_modernize_vpa`.
Trước V49, F01 nhận P06 **hoặc** G03 **hoặc** B03; neo vào G03 để định vị,
không buộc hoàn thành G03. Quy tắc F02 cần F01, S03 và L04 thuộc cấu trúc trước V48;
V48 bỏ S03/L04 làm điều kiện.

Các mốc năm của S03/L04 và những focus liên quan vẫn giữ nguyên. Trước V48,
gate L04 khiến F02 sớm nhất trên đường phòng thủ là năm 2011; đường green-water
cần W05 nên từ 2014; blue-water từ 2015. Từ V48, F02 chỉ cần F01 nên các mốc
này không còn giới hạn thời điểm mở F02. I07 và L03 năm 2026 vẫn tùy chọn.

Các gate nằm trong `available`; không bypass lịch sử bằng việc tự trao focus.
Historical AI ưu tiên P, Hardline ưu tiên G; B có trọng số thấp và guard
treasury 15 tỷ USD cho AI. Các guard phá sản ở `ai_will_do` không khóa người chơi.
Giữ nguyên hai persona, các template/variant/area/theater/naval goal của MD;
không thêm rule mua sắm hoặc override AI equipment khi chưa chứng minh cần thiết.

## Reward và cân bằng

`VIE_nav_xp_*` tiếp tục chuyển XP thành naval mastery nếu đã chọn grand doctrine.
Org/MDA/Industry/Logistics mỗi nhóm giữ một bậc idea cao nhất. S03/S02 nhận
bonus bổ sung theo cả hai thứ tự hoàn thành. T04 cần đủ T02 và T03.

`VIE_nav35_refresh` chỉ tính idea, không trao XP, nghiên cứu, tiền hoặc tàu.
Starter học thuyết, giai đoạn trung gian, capstone tuyến và F02 thay thế nhau,
không cộng chồng. Chỉ gọi refresh sau focus hoặc kết quả dự án, không chạy
vòng gỡ/cấp idea hằng tháng.

Chi phí nhân sự hải quân do modifier MD `navy_personnel_cost_multiplier_modifier`
tính: H +5%, G +10%, B +25%, P không thêm. Không tạo ngân sách tháng riêng.
Modifier country đã đối chiếu engine; bỏ các token cũ sai scope như
`surface_detection`, `sub_detection`, `naval_org`, `amphibious_defense`,
`patrol_efficiency`, `escort_efficiency`, `research_speed_naval`.

Trần fixture V35 trên mỗi đường sau năm 2026: organization <=14, range <=34%,
dockyard output <=20%, XP/mastery một lần <=450.
Đây là trần của nội dung V35, không bao gồm mọi luật/bonus MD và nhánh khác.
Chưa cân bằng bằng playtest.

## Các chương trình đầu tư

Giá dưới đây là giá **cân bằng gameplay**, không tuyên bố là giá hợp đồng lịch sử.
Chương trình chỉ thực hiện một lần, dùng trạng thái chưa bắt đầu/running/done.
Riêng hộ vệ có trạng thái ready chờ bàn giao khi thiếu căn cứ hoặc công nghệ.
Guard treasury, focus, giai đoạn trước và running/done được kiểm tra lại ở
scripted effect; duplicate start/finish không thu tiền hoặc nhận thưởng lần hai.
State được lưu bởi engine; không reset ở startup.

| Chương trình | Focus | Tỷ USD | Ngày | Kết quả |
|---|---|---:|---:|---|
| Xưởng đóng tàu | I01 | 7,5 | 365 | Một dockyard qua helper MD, xây khi giải ngân |
| Công nghệ đóng tàu | I01 | 2 | 365 | +3% sản lượng dockyard |
| Ba Son/Molniya | I02 | 1,5 | 365 | Nghiên cứu corvette 25%, 1 lượt |
| Hồng Hà/TT400 | I03 | 0,75 | 180 | Nghiên cứu patrol boat 25%, 1 lượt |
| Viện Thiết kế | I04 | 1 | 365 | Nghiên cứu frigate 25%, 1 lượt |
| Sông Thu/tàu bảo đảm | I05 | 1 | 180 | 15 naval XP/mastery |
| Tích hợp khí tài | I06 | 1,5 | 365 | Nghiên cứu sonar 25%, 1 lượt |
| Bảo đảm căn cứ | L01 | 2 | 365 | +3% sortie efficiency |
| Tiếp nhận năng lực VTĐN-01 | L03 | 2 | 180 | +4% range, +3% convoy escort |
| Đóng hộ vệ Sông Thu | I07 | 0,6 | 1.095 | Bàn giao một frigate; mở bonus hỗ trợ G02/F02 |
| Bảo đảm triển khai biển xa | B02 | 8 | 365 | +5% range, +3% sortie efficiency |

Chương trình xưởng phải có state đang sở hữu, kiểm soát, ven biển và còn slot.
`one_state_dockyard` tự thu 7,5 tỷ qua MD; không thu thêm ở country scope hoặc
khi finish. `skip_payment`/quy tắc bỏ chi phí của MD giữ semantics gốc.
Chương trình hộ vệ thay thế ba bước R&D cũ bằng một hợp đồng đóng tàu.

Bảy decision lặp lại quản lý sản xuất, bảo dưỡng, tuần tra và diễn tập; thu tiền
qua `modify_treasury_effect`, thêm bonus có hạn hoặc XP. Không cấp hạm tàu.
Tên các decision cũ được sửa để không tuyên bố mua sắm/bàn giao khi thực tế
chỉ cấp bonus bảo đảm. Decision phòng thủ đảo không còn xây coastal bunker
thiếu province như V34.

## Hợp đồng hộ vệ I07

I07 xếp hàng event phê duyệt sau một ngày. Khi nhận event, decision đóng tàu
được mở. Người chơi bấm decision mới trả **0,6 tỷ USD**, bắt đầu **1.095 ngày**;
khi hết hạn bàn giao **một** tàu `Song Thu ASW 2026`, rồi thông báo `vie_nav35.6`.
I07 vẫn tùy chọn, không chặn F02. Bonus hỗ trợ G02 và đóng tàu F02 chỉ áp dụng
sau bàn giao, bất kể thứ tự hoàn thành focus và hợp đồng.

Dùng `frigate_hull_4` (hull 2010 của MD), không tạo equipment type mới hoặc tự
cấp công nghệ. Cấu hình cố định dùng diesel 2, fire control tích hợp, sonar 4,
CIWS 4, torpedo 4, pháo 76 mm 3, bệ tên lửa quad, đạn balanced 3 và fuel tank.
Từng module và slot đã đối chiếu nguồn MD đang cài. Radar và sonar dùng chung
một slot cảm biến của hull: chọn sonar phục vụ chống ngầm. Cấu hình này là mô
phỏng gameplay tham khảo dự án 2026, không xác nhận trang bị thực tế của tàu.
Variant được tạo trong country scope lúc bàn giao; sau đó có thể dùng thiết kế
trong sản xuất thông thường. Decision chỉ đóng chiếc đầu tiên.

Điều kiện bắt đầu: I07 hoàn thành, event đã phê duyệt, đủ các công nghệ được
liệt kê trong trigger, treasury đủ, có căn cứ hải quân và dockyard ở state
ven biển đang sở hữu/kiểm soát. Hợp đồng không giữ chỗ trong production queue
hoặc trừ vật liệu. Thời gian bao gồm đóng, tích hợp và thử nghiệm dưới dạng
trừu tượng gameplay; mất xưởng sau giải ngân không dừng đồng hồ hoặc hoàn tiền.

Finish chỉ hợp lệ khi cờ running đã đủ 1.095 ngày (`days > 1094`). Hết hạn mà
không còn căn cứ hoặc công nghệ cần thiết thì chuyển sang ready, chờ đủ điều
kiện để bàn giao. Monthly scheduler thử lại và cũng khôi phục hợp đồng đủ hạn
nếu callback bị bỏ lỡ; không đặt lại đồng hồ hoặc giải ngân thêm. Cờ done được
ghi trước khi tạo tàu để ngăn các đường gọi lặp tạo chiếc thứ hai.

## Lịch sử, dự án và những khác biệt có chủ ý

Scheduler duy nhất được nối vào monthly hook hiện có và catch-up helper.
Mốc cơ cấu Vùng năm 2009, tích hợp khí tài 2022/2025 ghi nhận một lần; khi
focus hoàn thành muộn vẫn nhận kết quả nhưng không xếp hàng popup lịch sử cũ.
Caller ghi cờ và reward trước; các event milestone và hoàn tất chỉ thông báo.
Event phê duyệt `vie_nav35.5` mở decision sau I07, không thu tiền hoặc cấp tàu.
Replay event không mở hợp đồng mới hoặc trao thưởng lần nữa.

Tin đặt ky lịch sử 5/10/2026 là thông tin bối cảnh, không hoàn tất hợp đồng
đóng tàu của người chơi. Monthly hook có thể
hiển thị tin ở tháng kế tiếp. Nguồn lịch sử:
[Hải quân Việt Nam](https://baohaiquanvietnam.vn/tin-tuc/le-dat-ky-dong-moi-tau-ho-ve-chong-ngam-da-nang).

**Phạm vi hiện vật chưa triển khai:** province Cam Ranh chưa được xác nhận nên
L01 không xây naval base tại một province thay thế. VTĐN-01 vẫn chỉ cấp năng lực
bảo đảm, không tạo tàu 530/531. Hộ vệ I07 dùng hull/module có thật của MD theo
cấu hình gameplay nêu dưới đây. Molniya/Gepard/Kilo focus nâng
khả năng khai thác lực lượng, không thêm tàu vào OOB hoặc một hợp đồng mua mới.
Nếu mở rộng mua sắm hiện vật sau này, cần xác minh variant, tech/slot/DLC,
số lượng, giá và lịch bàn giao; không dùng các gói bảo đảm hiện tại làm giao tàu.

Không có fallback DLC chưa được chứng minh cần thiết. Dùng research category,
country idea, helper và MIO Ba Son có sẵn; không tự cấp equipment/DLC token.

## File đã thay đổi

- `common/national_focus/VIE_md_focus.txt`: 40 node, v40/v41, gates/layout/reward/AI.
- `common/scripted_effects/VIE_md_effects.txt`: refresh, start/finish, milestones.
- `common/scripted_triggers/VIE_md_triggers.txt`: guards chương trình.
- `common/ideas/VIE_md_ideas.txt`: bậc và route, modifier hợp lệ.
- `common/decisions/VIE_md_decisions.txt`: 11 dự án và 7 decision lặp lại.
- `common/decisions/categories/VIE_md_categories.txt`: root V35.
- `common/on_actions/VIE_md_on_actions.txt`: gọi scheduler mới.
- `events/VIE_md_events.txt`: 7 event namespace `vie_nav35`, gồm phê duyệt và thông báo bàn giao.
- `common/ai_strategy_plans/VIE_strategy_plans.txt`: ưu tiên P trong Historical.
- `localisation/english/replace/VIE_replace_military_l_english.yml`: loc tiếng Việt,
  BOM, đủ focus/idea/program/event/tooltip, chỉnh mô tả reward cũ không còn đúng.
- `tools/audit/naval_scenarios.py`, `naval_v35_spec.json`: fixture đọc live script.
- `tools/audit/naval_balance.py`: chuyển entry point cũ sang kiểm tra V35 live.

Tái sử dụng 27 focus sprites đã có texture, idea picture `generic_navy_bonus`,
decision `GFX_decision_generic_naval`, event `GFX_report_event_military_planning`
do base game/MD cung cấp. Không sửa PNG/DDS/GFX. Kiểm file/tích hợp riêng với
kiểm hiển thị ở kích thước game và kiểm trong game.

## Kiểm tra đã chạy

- `audit.py`: 359 focus; 0 dangling, 0 duplicate coordinates, 0 forward anchor,
  0 prerequisite cycle, mọi focus có icon/reward.
  Kiểm bổ sung: 40/40 tọa độ tuyệt đối khớp layout đã quy đổi và không có
  khoảng cách ngang dưới 2 giữa focus Hải quân với bất kỳ focus cùng hàng.
- `live.py`: không thiếu scripted effect/trigger, idea, focus, event, tooltip.
- `ev.py`: không trùng event ID, không orphan, không thiếu loc event hiển thị.
- `verify_all_loc.py`, `audit_loc_errors.py`: không lỗi cú pháp/BOM hoặc thiếu
  title/description/tooltip.
- `audit_dds_and_gfx.py`: 382 DDS; 0 lỗi format, 0 texture path thiếu,
  0 focus sprite thiếu (sửa được 9 reference sai của V34 bằng reuse).
  Audit này chỉ nhìn trong checkout, còn báo event pictures external; provider
  của 7 event mới đã xác minh ở base game.
- `prov.py`: 0 lỗi; V35 không thêm công trình province hoặc scope state cứng.
- `naval_scenarios.py`: 260 scenario độc lập; 343 khi thêm đối chiếu provider
  MD/game, bao gồm dependency, ba route, chi phí, idempotency, milestone,
  bonus ở cả hai thứ tự, trần reward từng tuyến, đủ công nghệ/module/slot,
  ngày 1.094/1.095, mất căn cứ, khôi phục bàn giao và chống tạo tàu trùng.
- `git diff --check`: không lỗi whitespace.

Fixture giả lập một tập trigger/effect giới hạn, đọc mã thật nhưng **không thay
thế engine**. Build xưởng, thời gian decision, save giữa chương trình, DLC,
AI kinh tế, hiệu năng, nối dây/hover và `error.log` trong game: **NOT RUN**.
Ca sao chép trạng thái trong fixture chỉ là giả lập save/load, không phải save
HOI4 thật. Cần kiểm model/entity của tàu, slot đạn tên lửa của MD, countdown,
callback, DLC và thay đổi chủ quyền/civil war trực tiếp trong game.

## Nghiệm thu trong game tiếp theo

1. Game mới VIE năm 2000; playset nạp submod sau MD, kiểm `error.log`.
2. Xem nhánh X197-224 ở mức zoom thực tế; thử hover F01/F02 và các edge AND/OR.
3. Chơi/console riêng P, G, B: F01 chỉ cần một capstone; F02 mở sau F01.
4. Treasury thiếu/đủ và thiếu coastal slot: chỉ chương trình hợp lệ được giải ngân.
5. Chạy hết một project, thử start/finish lại; không thu/trao thêm. Save/load giữa
   `days_remove` phải giữ countdown và running/done đúng.
6. I07 → event phê duyệt → decision: thiếu từng công nghệ/căn cứ/xưởng hoặc
   ngân sách thì không giải ngân. Đủ điều kiện: trừ 0,6 tỷ một lần; ngày 1.094
   chưa có tàu, ngày 1.095 có đúng một hộ vệ và thông báo bàn giao. Save/load
   giữa hợp đồng, thử lại start/finish/event; không thu tiền hoặc tạo tàu trùng.
   Mất căn cứ trước hạn: chờ; lấy lại căn cứ: bàn giao một lần. Kiểm số lượng,
   thiết kế và module của tàu thật trong màn hình hải quân.
   Hoàn thành S02/S03, G02/dự án ASW, L04/dự án VT theo hai thứ tự.
7. Đi qua 2009, 2013, 2014, 2015, 2022, 2025, 2026 và hoàn thành focus muộn;
   không replay milestone hoặc giao tàu trùng. I07 không chặn F02.
8. Kiểm idea và ngân sách: một bậc/family, một route idea, G +10% và B +25%
   nhân sự hải quân; không có quỹ tháng thứ hai.
9. Chạy Historical/Hardline nhiều năm; xác nhận AI không tự phá sản hoặc lao vào
   B trước đủ ngân sách. Kiểm với DLC người chơi thực sự bật/tắt.
