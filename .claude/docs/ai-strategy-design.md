# Thiết kế AI cho submod Việt Nam

Ngày rà soát: 06/10/2026

## Mục tiêu đã chốt

Submod chỉ xây dựng hai hồ sơ AI cấp cao:

1. `Historical Vietnam`: đi theo diễn biến chính trị và đối ngoại lịch sử.
2. `Hardline Vietnam`: đưa AI vào nhánh Con đường Kiên định và ưu tiên các quyết định của nhánh này.

Không tạo AI plan riêng cho Institutional Opening, Concentration of Power hoặc các biến thể mua sắm. Hai focus kết cục sau Đại hội XIV là các kết quả chính trị bên trong đường đi, không phải persona AI riêng. Mua sắm thay thế tiếp tục do game rule `rule_vie_alt_procurement` quản lý độc lập.

## Convention rút ra từ Millennium Dawn

Đã đọc `.claude/rules/ai-strategy.md`, `.claude/docs/ai-strategy-reference.md` và skill `country-ai-path` cùng các tài liệu `references/write.md` / `references/audit.md` tại repo MD.

MD dùng các lớp sau:

- `common/game_rules/`: cho người chơi chọn hồ sơ đường đi AI.
- `common/on_actions/`: chuyển lựa chọn thành cờ đường đi; plan và trigger đọc cờ này thay vì đọc game rule trực tiếp.
- `common/ai_strategy_plans/`: đặt ưu tiên focus, ý tưởng và chiến lược cho một đường đi.
- `common/ai_strategy/`: các chiến lược liên tục, có điều kiện bật/tắt theo focus, cờ hoặc tình hình; phù hợp với ngoại giao và hành vi tổng quát hơn là thay thế focus plan.
- `ai_will_do` và `ai_chance`: xử lý lựa chọn focus và event ở đúng nơi lựa chọn xảy ra.

Theo tài liệu MD, `focus_factors` nhân với trọng số `ai_will_do` của focus; `ai_national_focuses` là danh sách ưu tiên đặc biệt, không phải danh sách cho phép độc quyền. Plan được bật khi điều kiện `enable` đạt; điều kiện `abort` được kiểm tra để gỡ plan. Vì vậy, plan chỉ ưu tiên một đường đi, không tự đổi ruling party, không đặt cờ gameplay và không thay thế điều kiện `available`/prerequisite của focus.

MD chuẩn hóa AI path đầy đủ theo `Historical` + từng đường thay thế + `Random Path` + `No Path`. Submod này chủ động theo quyết định sản phẩm chỉ có hai hồ sơ Historical/Hardline; không tự thêm Random hoặc No Path. Khi triển khai game rule, cần xác định rõ hồ sơ mặc định. Đề xuất mặc định là Historical.

Ví dụ gần nhất là `D:\ide\Millennium-Dawn\common\ai_strategy_plans\SIA_strategy_plans.txt`: có plan lịch sử và các plan đường thay thế; mỗi plan kết hợp `focus_factors` với `ai_strategy`. `D:\ide\Millennium-Dawn\common\ai_strategy\SIA.txt` cho thấy chiến lược ngoại giao có thể được chuyển theo focus đã hoàn thành. Đây là mẫu kiến trúc để tham khảo, không sao chép trọng số của Thái Lan.

## Hiện trạng submod

- `common/ai_strategy_plans/VIE_strategy_plans.txt` có `VIE_HISTORICAL_plan`, ưu tiên chuỗi Đại hội, các mốc kinh tế/đối ngoại, quốc phòng lục quân và hải quân phòng thủ; sau Đại hội XIV, ưu tiên chuỗi cán bộ/chính phủ điện tử và nhánh tập quyền chỉ khi điều kiện focus cho phép. Tham chiếu focus đã qua audit tĩnh; chưa playtest.
- `common/ai_focuses/VIE.txt` bổ sung trọng số nghiên cứu phòng thủ, SAM/phòng không, vũ khí bộ binh và tàu hộ vệ/tuần tra; giữ đầy đủ các category MD muốn dùng trong từng block override.
- `common/ai_strategy/VIE_md_ai.txt` có `VIE_historical_force_mix` cho lục quân và `VIE_historical_naval_mix` cho hải quân; chúng điều chỉnh role ratios theo Historical, còn thiết kế tàu VIE vẫn do MD cung cấp.
- `common/ai_strategy/VIE_md_ai.txt` hiện có chiến lược kết bạn ASEAN/đối tác, tránh chiến tranh với Trung Quốc và láng giềng, cùng hạn chế mở thêm chiến tranh khi đang thua.
- `VIE_ai_historical` trong `common/scripted_triggers/VIE_md_triggers_p4.txt` hiện là `always = yes`; các lựa chọn event thay thế có `factor = 0 VIE_ai_historical = yes` vì vậy bị khóa cho AI.
- `VIE_ai_behavior` trong `common/game_rules/VIE_md_rules.txt` hiện chỉ có `NO_PATH`. Game rule này chưa cung cấp lựa chọn Historical/Hardline.
- Focus gốc Hardline chỉ khả dụng khi đảng `emerging_communist_state` đang nắm quyền hoặc trong liên minh. `ai_strategy_plan` không thể tự đưa đảng đó lên cầm quyền.
- `rule_vie_alt_procurement` là rule mua sắm riêng, được kiểm tra qua `VIE_proc_alt_allowed`; giữ riêng khỏi hai AI path.

## Thiết kế hai hồ sơ

### Historical Vietnam

- Là plan mặc định cho AI.
- Ưu tiên chuỗi focus nghị quyết Đại hội theo prerequisite và ngày đã có trong cây; sau đó ưu tiên WTO, EVFTA, CPTPP, ASEAN, phát triển trong nước và hiện đại hóa quốc phòng theo chronology của submod.
- Giữ các lựa chọn historical hiện có trong event và decision; không dùng plan để bỏ qua điều kiện ngày, focus prerequisite hoặc cờ lịch sử.
- Tiếp tục cân bằng ngoại giao “cây tre” và tránh chiến tranh chủ động. Dùng war-weight riêng cho VIE khi cần thể hiện rõ chính sách quốc gia mà AI toàn cục của MD không cung cấp; các lệnh cấm chiến tranh mạnh dùng mức `-4000` theo mẫu MD. Đây vẫn là trọng số AI, không phải luật cấm tuyệt đối.
- Bảo vệ ngân sách và năng lực nhân lực qua guard AI ở focus tốn tiền hoặc xây công trình. Role ratios chỉ là ưu tiên sản xuất, không đặt hạn mức; cần playtest để xác nhận mức chi tiêu thực tế.
- Dùng `focus_factors` để ưu tiên các mốc; không dùng `ai_national_focuses` làm một danh sách focus cứng nếu chronology/prerequisite đã biểu diễn được đường đi.

### Hardline Vietnam

- Plan chỉ bật khi `VIE_hl_in_power = yes`; nên tự gỡ khi điều kiện đó không còn đúng.
- Ưu tiên focus Hardline đang khả dụng, các lựa chọn event và decision của nhánh; không ưu tiên chúng trước khi điều kiện cầm quyền được thỏa.
- Giữ một lối vào hợp lệ cho AI. Cần kiểm tra event/chọn lựa chuyển đảng, AI chance, popularity ramp và điều kiện focus để bảo đảm AI có thể thực sự đạt tới `VIE_hl_in_power`.
- Chỉ những lựa chọn được thiết kế cho Hardline mới được tăng trọng số. Không đổi `VIE_ai_historical` thành false trên toàn Hardline path mà chưa rà soát: cách đó có thể mở tất cả lựa chọn phi lịch sử trong event, không chỉ nhánh Hardline.
- Chọn đối ngoại, an ninh và kinh tế dựa trên mechanics Hardline hiện có; không mặc định Hardline đồng nghĩa với hiếu chiến hoặc gia nhập một khối.

## Các nhánh/hệ thống không tạo thành plan thứ ba

- `VIE_concentration_of_power` và `VIE_institutional_opening` loại trừ nhau, mở ở giai đoạn sau Đại hội XIV theo cờ và điều kiện lãnh đạo. Đây là kết cục chính trị, không phải hai AI persona mới. Plan nào ưu tiên kết cục nào cần được quyết định theo lịch sử/hardline và event dẫn tới nó.
- Institutional Opening hiện bị AI lịch sử bỏ qua qua `VIE_ai_historical`; không tự bật nó chỉ vì có focus trong cây.
- Mua sắm alt-history tiếp tục theo `rule_vie_alt_procurement`, không lấy cờ Hardline làm điều kiện thay thế.
- Chiến lược ngoại giao hoặc xây lực lượng là lớp hành vi bổ trợ có thể dùng chung hoặc thay theo trạng thái; không cần nhân số AI plan theo từng quân chủng.

## Các hệ thống AI hỗ trợ cần rà cho VIE

AI hoàn chỉnh của VIE cần được đánh giá ở cả sáu lớp `ai_focuses`, `ai_templates`, `ai_equipment`, `ai_areas`, `ai_faction_theaters` và `ai_navy`. Historical hiện có override nghiên cứu riêng; các lớp còn lại đang dùng cấu hình MD sau khi rà với OOB VIE, đội corvette, tư thế Four Nos và vùng chiến lược châu Á. Đánh giá lại nếu Hardline cần hành vi khác hoặc playtest bộc lộ khoảng trống.

Quy ước chi tiết, role chain, token, giới hạn và checklist cho từng lớp nằm ở [ai-subsystems-reference.md](ai-subsystems-reference.md). Rà soát cả sáu lớp là bắt buộc; tạo file VIE riêng chỉ khi cần thay đổi hoặc bổ sung hành vi so với MD.

## Trình tự triển khai

1. Playtest `Historical Vietnam`; trọng số focus, nghiên cứu và force mix đã được bổ sung, cần xác nhận nhịp chọn focus, hướng tech, tỷ lệ role và ngân sách trong game.
2. Nếu playtest cho thấy MD generic không tạo đúng hành vi, bổ sung override đúng lớp theo `ai-subsystems-reference.md`: template, variant trang bị, area/theater hoặc naval goal/fleet/taskforce.
3. Chốt game rule hai hồ sơ và cách lưu path flags trước khi bật AI Hardline; không để `VIE_ai_historical` khóa các lựa chọn cần thiết cho Hardline.
4. Rà luồng AI vào Hardline trước khi viết plan: điểm khởi đầu, lựa chọn event, thay đổi popularity/ruling party, lối thoát khỏi nhánh và tương tác với `VIE_ai_historical`.
5. Thêm `Hardline Vietnam` chỉ bật khi Hardline thực sự nắm quyền; đồng bộ focus, event, decision và các hệ thống hỗ trợ cần khác với Historical.
6. Audit hai hồ sơ riêng rồi playtest. Audit tĩnh không chứng minh AI chọn đúng hướng hoặc cân đối ngân sách trong game.

## Quy tắc khi tiếp tục thiết kế

- Không coi `focus_factors` là killswitch duy nhất nếu các event/decision cũng cần chặn lựa chọn thuộc path kia.
- Không thêm đường chuyển chế độ bằng scripted effect ép ruling party; phải dùng luồng gameplay có trigger, AI chance và ramp hợp lệ.
- Không thêm decision-only cure cho AI nếu decision category không hiển thị với AI; scripted GUI thuần người chơi không phải cách AI sử dụng mechanics.
- Guard bankruptcy và `can_staff_an_industrial_complex` nằm trong `ai_will_do`, không đặt vào `available` làm khóa người chơi.
- Đọc quy tắc chiến lược AI hiện hành trong MD trước khi sửa `VIE_md_ai.txt`; đừng nhân đôi cơ chế chiến tranh toàn cục.
- Mỗi thay đổi AI path phải được kiểm tra bằng audit tham chiếu và focus; kết luận về hành vi cuối cùng cần playtest.
