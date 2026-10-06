# Quy chuẩn các hệ thống AI của Millennium Dawn

Ngày đối chiếu: 06/10/2026. Nguồn: `D:\ide\Millennium-Dawn\.claude\rules\ai-strategy.md`, hai tài liệu AI reference, `common/ai_focuses/README.md`, tài liệu `common/ai_navy/` và các file cấu hình đang dùng trong MD.

Tài liệu này hướng dẫn mở rộng AI cho VIE. Các hệ thống bên dưới là lớp hỗ trợ cho hai hồ sơ cấp cao `Historical Vietnam` và `Hardline Vietnam`, không tạo thêm persona AI. Một lớp chỉ cần file VIE riêng khi cấu hình dùng chung của MD chưa đáp ứng mục tiêu đã xác định; không tạo folder/file rỗng chỉ để đủ cấu trúc.

## Hiện trạng đã đối chiếu

- Submod có `common/ai_strategy/VIE_md_ai.txt`, `common/ai_strategy_plans/VIE_strategy_plans.txt` và `common/ai_focuses/VIE.txt`.
- `VIE_HISTORICAL_plan` ưu tiên các mốc Đại hội, phát triển/hội nhập và hiện đại hóa phòng thủ. `VIE_historical_force_mix` tăng role `L_Inf`/`infantry`, giảm cơ giới và thiết giáp.
- Trong sáu lớp hỗ trợ, chỉ `ai_focuses` cần override VIE hiện tại. MD generic templates, equipment, strategic areas, faction theaters và naval goals/fleets đã cung cấp hành vi dùng được cho Historical. `ai_strategy` riêng của VIE đặt role ratios lục quân và hải quân.
- Millennium Dawn có `common/ai_equipment/VIE_naval.txt` với các thiết kế tuần dương hạm theo tiến trình công nghệ. `common/ai_navy` có goal coast defense cùng corvette/coastal patrol fleet; OOB VIE đầu game có 13 corvette.
- MD không có `common/ai_strategy/VIE.txt`; `VIE_md_ai.txt` của submod là lớp chiến lược quốc gia riêng.
- Không tạo file rỗng hoặc lặp lại cấu hình MD. Thêm override sau khi phát hiện khoảng trống cụ thể và kiểm tra ảnh hưởng của các cấu hình generic còn đồng thời hoạt động.

## `ai_focuses`: ưu tiên nghiên cứu

- File xác định trọng số các nhóm công nghệ theo AI focus như `peaceful`, `defense`, `military_equipment`, `naval` và `aviation`; đây không phải thứ tự tech cứng.
- Trọng số hợp lệ theo quy ước MD là số nguyên từ 1 đến 10. Bỏ hẳn nhóm không muốn thúc đẩy hoặc chỉ có trọng số 1; không khai báo `= 0`.
- Các nhóm công nghệ cộng trọng số với nhau. Một tech thuộc nhiều `CAT_*` có thể nhận tổng từ nhiều nhóm.
- `ai_focus_<focus>_VIE` thay thế block generic tương ứng cho VIE. Khi tạo override phải chép đầy đủ các trọng số muốn giữ trong block đó; không giả định các dòng generic sẽ được kế thừa.
- Chọn tech cuối cùng vẫn phụ thuộc `ai_will_do` của tech, lịch, GDP và penalty đi trước thời đại. MD có ngưỡng ngẫu nhiên giữa các tech điểm cao, vì vậy đánh giá xu hướng nghiên cứu theo nhóm, không đòi thứ tự tech cố định.
- Không sửa define nghiên cứu toàn cục chỉ để điều chỉnh riêng Việt Nam. Nếu hai hồ sơ Historical/Hardline cần hướng nghiên cứu khác nhau, trước hết so sánh khả năng đặt `research = { CAT_x = N }` trong từng strategy plan; xác nhận hiệu ứng và playtest trước khi chọn cách này.
- Mọi `CAT_*` phải được xác minh trong phiên bản MD đang cài. Không tự đặt tên category theo tên hiển thị.

## `ai_templates`: template sư đoàn

- `ai_templates` mô tả vai trò và mẫu sư đoàn mà cơ chế startup của MD cấp hoặc dùng để nâng cấp. Chỉ thêm file không đảm bảo AI sẽ tạo hoặc chuyển sang mẫu mới: phải lần theo `give_AI_templates`, template conversion decisions và các lần refresh khi đổi trạng thái.
- Mỗi entry gắn với role; mẫu con quyết định `regiments`, support, `enable`, thứ tự nâng cấp, ưu tiên củng cố và ngưỡng match. Các role hợp lệ phải lấy từ MD, ví dụ `L_Inf`, `infantry`, `marines`, `apc_mechanized`, `ifv_mechanized`, `armor`.
- Phân biệt template sư đoàn với `ai_strategy` sản xuất: strategy đặt tỷ lệ/nhu cầu role; template cho biết cấu trúc đơn vị tương ứng. Cả hai phải cùng dùng role ID chính xác.
- Trước khi tạo template VIE, so sánh với OOB Việt Nam, mẫu generic MD, doctrine mục tiêu và lượng trang bị có thể sản xuất. Đảm bảo từng role AI được yêu cầu có ít nhất một mẫu hợp lệ và có lộ trình nâng cấp khả thi.
- Không dùng sai role, tên battalion/support hoặc template trùng ID. Kiểm tra mẫu nâng cấp ở các cấp công nghệ và thiếu trang bị; tránh template cuối game chỉ dùng được khi VIE đã vượt ngưỡng công nghiệp không thực tế.

## `ai_equipment`: thiết kế biến thể trang bị

- File mô tả các variant AI sẽ thiết kế/nâng cấp, không phải OOB và không trực tiếp quyết định số lượng sản xuất.
- Mỗi design group cần `category`, `roles`, điều kiện quốc gia, `priority` và các thiết kế con. Mỗi thiết kế phải có priority và `target_variant` hợp lệ; module phải đúng archetype, slot và công nghệ trong MD.
- Chuỗi phải khớp ở ba nơi: role trong `ai_equipment`, `ai_type` của equipment và `role_ratio`/`unit_ratio` trong `ai_strategy`. Sai một mắt xích có thể khiến AI không thiết kế hoặc không sản xuất variant đó.
- ID group/design trùng có thể âm thầm ghi đè cấu hình trước. Mỗi role nên có một thiết kế phù hợp ở mỗi giai đoạn; điều kiện công nghệ phải tránh hai mẫu cùng được ưu tiên hoặc không có mẫu nào hoạt động.
- Generic MD là fallback. Khi thêm thiết kế riêng cho VIE phải kiểm tra từng generic role đang áp dụng. Quy ước upstream yêu cầu chặn TAG khỏi generic nếu đã có custom design; trong submod, phải xác định cách override MD an toàn trước khi sửa block generic, không giả định file mới tự loại cấu hình cũ.
- MD hiện có `VIE_naval.txt`. Đối chiếu nó với mua sắm hải quân, role ratio và tech của mod trước khi mở rộng; không sao chép nguyên thiết kế tàu hay module mà chưa xác minh trong bản MD hiện tại.

## `ai_areas`: nhóm khu vực chiến lược

- Area ID được dùng bởi `ai_strategy = { type = area_priority id = ... }`. MD đã có các nhóm dùng chung theo châu lục và vùng biển; kiểm tra ID tồn tại trước khi gọi.
- Area chứa continent và/hoặc strategic region. Strategic region ID phải lấy từ map MD, không suy từ state ID hay province ID.
- Chỉ tạo nhóm VIE khi cần ưu tiên tác chiến khác với nhóm MD. Trước khi thêm, kiểm tra các area hiện có, vùng chồng lấn và tất cả nơi gọi `area_priority`.
- Đây là nhóm cho strategic AI; nó không tự tạo mục tiêu hải quân hoặc faction theater.

## `ai_faction_theaters`: theater cho chiến tranh trong faction

- Theater gom strategic regions cho chiến tranh của faction. Block có ID, `name` localisation, `ai_will_do` và danh sách `regions`; các region phải tạo thành vùng kết nối theo yêu cầu engine.
- Mẫu MD bật theater theo chiến tranh/faction liên quan và hủy khi điều kiện không còn. Không để AI dựng theater thời bình hoặc áp dụng cho faction không liên quan.
- Chỉ thêm theater VIE khi gameplay thực sự cần AI lãnh đạo hoặc phối hợp mặt trận của faction. Phải xác minh region trên bản đồ, localization và điều kiện chọn/hủy.
- Không nhầm theater này với `ai_areas`: area priority ảnh hưởng ưu tiên khu vực của chiến lược, faction theater cấu hình tổ chức mặt trận của faction.

## `ai_navy`: goals, taskforces và fleets

- MD dùng goal-based naval AI: goal đặt khoảng `min_priority`/`max_priority`; engine chấm các objective theo mức quan trọng trong khoảng đó. Goal là loại nhiệm vụ, objective là nhiệm vụ gắn với một mục tiêu cụ thể.
- Tài liệu `common/ai_navy/_documentation.md` liệt kê 10 `objective_type` hợp lệ: `naval_invasion_support`, `naval_invasion_defense`, `coast_defense`, `convoy_protection`, `convoy_raiding`, `naval_dominance`, `naval_blockade`, `mines_sweeping`, `mines_planting`, `training`. `strike_force_objective` không hợp lệ; strike force được xử lý bằng taskforce/fleet.
- Có mâu thuẫn tài liệu upstream: `.claude/docs/ai-equipment-reference.md` nói 11 loại và có `strike_force_objective`, còn tài liệu chuyên biệt trong `common/ai_navy/` loại nó ra. Khi viết goal, theo danh sách objective của `common/ai_navy/_documentation.md` và kiểm tra runtime.
- Nếu thêm goal quốc gia, đối chiếu đủ các loại objective cần dùng và đảm bảo goal generic không đồng thời áp dụng cho VIE. Upstream yêu cầu thêm TAG vào `blocked_for` của goal generic tương ứng; với submod phải thiết kế override MD cẩn thận và xác nhận kết quả trong game.
- Fleet templates được xử lý theo thứ tự. Đặt nhóm nhỏ, khả thi trước; tách fleet cốt lõi, mở rộng và tùy chọn. Taskforce lớn chưa đủ tàu có thể giữ tàu trong reserve khiến các nhóm nhỏ hữu ích không hình thành.
- Không đặt `optimal_composition` vượt giới hạn tàu của taskforce trong MD defines; tàu vượt cap có thể bị bỏ qua. Khi cần năng lực hải quân cho Việt Nam, kiểm tra cùng lúc goal, fleet, taskforce, `ai_equipment` và tỷ lệ sản xuất.
- Dùng `imgui show ai_navy` để quan sát goal/objective khi playtest. Kiểm tra cả hòa bình, khủng hoảng và chiến tranh.

## Trình tự rà soát khi triển khai

1. Ghi mục tiêu hành vi đo được cho VIE và xác định phần nào dùng chung cho Historical/Hardline, phần nào cần đổi theo trạng thái.
2. Đối chiếu generic MD và cấu hình VIE đã được MD cung cấp trước khi tạo override.
3. Xác minh mọi role, category, equipment, module, strategic region, objective type và trigger trong MD đang cài.
4. Kiểm tra giao diện giữa research, role ratios, templates, equipment designs, areas, theaters và naval goals; tránh cấu hình rời rạc.
5. Chạy audit tham chiếu/cú pháp có sẵn trong submod, đọc `error.log`, rồi playtest AI. Các validator riêng của repo Millennium Dawn không nằm trong submod này; không gọi chúng như thể đã có sẵn.

