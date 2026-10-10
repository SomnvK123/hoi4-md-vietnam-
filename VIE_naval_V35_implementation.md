# Hải quân V35.1 - bản triển khai 11/10/2026

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
F01 nhận P06 **hoặc** G03 **hoặc** B03; neo vào G03 để định vị, không buộc
hoàn thành G03. F02 cần F01, S03 và L04.

Giữ các gate năm của JSON. Vì L04 cần L02, F02 sớm nhất trên đường phòng thủ
là năm 2011; đường green-water cần W05 nên từ 2014; blue-water từ 2015.
Đây là giới hạn dependency theo năm, chưa cộng thời gian focus. I07 và L03
năm 2026 đều tùy chọn đối với F02.

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
3. Chơi/console riêng P, G, B: F01 chỉ cần một capstone, F02 cần thêm S03/L04.
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
