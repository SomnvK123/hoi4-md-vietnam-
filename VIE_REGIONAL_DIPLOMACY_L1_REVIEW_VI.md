# Lượt 1 — Hồ sơ bàn giao, giao diện và ownership

**Đã xử lý các lựa chọn/chỉnh sửa được yêu cầu. Chưa đóng L1: J2 vẫn FAIL ở reader BoP; J5 FAIL là nợ chuyển E104 đã được chấp nhận. Chưa sang L2.** Tất cả thay đổi là tài liệu, script tính/kiểm và sơ đồ; chưa có code ngoại giao trong game.

Đầu ra kiểm độc lập: [bảng bất biến Markdown](VIE_REGIONAL_DIPLOMACY_L1_INVARIANTS_VI.md), [CSV bất biến](VIE_REGIONAL_DIPLOMACY_INVARIANTS_VI.csv), [B1](VIE_REGIONAL_DIPLOMACY_B1_VI.md), [tính cohesion](VIE_REGIONAL_DIPLOMACY_L1_CALCULATIONS_VI.md). Plan chính đã chứa ownership và kế hoạch chuyển thật tại 19.5–19.6; không cần chỉ dựa vào hồ sơ này để hiểu quyết định.

## Trạng thái quyết định

| Nội dung | Quyết định đã áp vào thiết kế | Không được suy ra |
|---|---|---|
| Cohesion | Chọn (b): gói sâu C/E đọc cadre_cohesion_required từ JSON chính trị | Không nhân phí gửi, không khóa focus/gói nhỏ hoặc mọi cụm |
| B1 | Mở từ X; tên/slug cứu nạn được sửa theo catalog | Kỳ X là giả định gameplay, không phải năm lập mọi quan hệ cứu nạn |
| S1 | Giữ XIII sau khi tách khỏi hồ sơ trái phiếu XIII05–08 | Không khẳng định quan hệ với Mỹ/Nga/Ấn bắt đầu ở XIII |
| R0 | IX đã giải quyết AND (F02 OR công cụ mặc định đại hội) | Không buộc AI/người chơi làm F02; không kéo hạn chọn programme vào root |
| Biển | Chính trị giữ XI08, XIII01–04, XIII10–11 | B không sở hữu/cấp lại kết quả tranh chấp; chỉ trợ giúp/kiểm thử/cứu nạn |
| E104 | Instance đầu tiên của một giao thức/một sổ chung, chỉ có kế hoạch chuyển sau C | Chưa chuyển/đụng script chính trị, J5 chưa PASS |
| Chuẩn bị/kiêm nhiệm | Giữ lịch BoP đã chốt, để J2 FAIL và L1 mở theo quyết định bổ sung; B6 đọc B5, kiêm nhiệm chỉ rút ký trong kế hoạch hoãn | Không thêm deadline/tham số để PASS; không tính tier và kiêm nhiệm là hai reader ngoại giao thực |
| Roster/tier | Tạm dùng VIE_dual_role_active; tier đọc idea | Thiết kế mảng roster chưa có provider xác minh; biến tier/idea chưa được kiểm đồng bộ engine |

## Giao diện chính trị → ngoại giao

“Có consumer” trong bảng là hợp đồng thiết kế, không phải script game đã chạy. Bộ hiện tại gồm G/P/C; chỉ G/C đã có đối chứng đổi tập lựa chọn hoặc thời điểm mở. T hoãn và không được đếm thành liên kết đang hoạt động.

| Liên kết | Nguồn và writer đã đọc | Reader | Hiệu ứng | Tooltip trước / sau | Kết quả phép thử bỏ liên kết |
|---|---|---|---|---|---|
| G — kỳ/công cụ | VIE_last_congress và VIE_congress_resolved do resolver đại hội ghi; F02 completed qua VIE_publish_responsibility_rules | R0 và root cụm tại catalog16, 19.4 | Giữ kỳ tối thiểu; hai nguồn cơ sở thay thế nhau | Trước: kỳ và F02 hoặc mặc định còn thiếu. Sau: nguồn mở thực tế và quyền cụm, chưa có reward bàn giao | Đạt ở mô hình: trước kỳ không mở; đủ kỳ, bỏ F02 nhưng resolver mở mặc định thì vẫn đi được. CSV root đối chứng cả sau hạn programme |
| C — cohesion | VIE_leadership_cohesion do checkpoint/phục hồi/resolver chính trị ghi; ngưỡng lấy cadre_cohesion_required | A04/A05/A08 và nâng gói C; soạn/gửi/start/nâng gói E5/E6 | Thiếu ngưỡng thì chọn nhỏ/đợi phục hồi; không thu phí triển khai hoặc chiếm slot | Trước: hiện tại/ngưỡng, gói nhỏ, giá/lịch phục hồi theo nguồn. Sau: gói/chi phí đã chốt, không hủy hồi tố khi giảm sau start | Đạt: một lần vượt phản đối từ snapshot nguồn làm mất quyền chọn sâu, một lượt phục hồi mở lại. Bảng band và ca riêng do script sinh |
| P — BoP | Engine VIE_leadership_balance qua wrapper VIE_is_collective_zone/VIE_is_central_zone; writer chính trị hiện có | Chuẩn bị B5 và hồ sơ S5, không đổi focus cost; B6 không chuẩn bị lại | Lịch đọc prepare_days theo vùng, chốt lúc bắt đầu | Trước: vùng/lịch. Sau: lịch đã chốt, đổi BoP không viết lại timer | **Chưa đạt J2:** có chênh ngày đo được nhưng chưa chứng minh người chơi đổi lựa chọn. Không tự thêm deadline/bonus hoặc cộng nhiều lượt để tạo PASS |
| T — hoãn | Idea tier và flag VIE_dual_role_active do chính trị ghi | Chỉ kế hoạch chuyển E104 tại19.6; chưa có cửa sổ ký ngoại giao thực | Dự kiến dùng sign_days[tier], min với combined.sign_days nếu kiêm nhiệm | Hợp đồng tương lai phải hiển thị lịch ký/cửa sổ thật | Chưa có consumer hiện tại, không kiểm/đếm như liên kết active; không dùng cửa sổ E104 để giả có cửa sổ E/S/W |

Không thêm biến phản chiếu hoặc writer chính trị trong ngoại giao. Gate C chỉ áp trước start; phản hồi chấp thuận vẫn có thể được ghi khi cohesion giảm trong lúc chờ. Phải phục hồi trong hạn hiện có hoặc thương lượng gói nhỏ; không tự gia hạn, không tự coi gói sâu đã bàn giao. Giá gửi/gửi lại vẫn lấy B1.

## R0: căn cứ provider và kiểm AI

Nguồn thiết kế: chính trị 4.2 và 6.1 quy định công cụ qua F02 hoặc mặc định đại hội. Nguồn runtime đã đọc:

- common/scripted_effects/VIE_md_effects_politics.txt: resolver đại hội ghi VIE_last_congress và VIE_congress_resolved độc lập với completed F02.
- common/decisions/VIE_md_politics_decisions.txt và categories/VIE_md_categories.txt: công cụ chương trình/category đọc VIE_congress_resolved.
- common/scripted_triggers/VIE_md_triggers_politics_runtime.txt: VIE_politics_can_select đọc flag/kỳ nhưng còn hạn và trạng thái programme; không thể gọi nguyên trigger này cho R0 vì ngoại giao sẽ bị khóa sau hạn hoặc khi programme đã chọn.
- common/national_focus/VIE_md_focus.txt: F02 có ai_will_do; common/ai_strategy_plans/VIE_strategy_plans.txt không có chỉ thị F02 bắt buộc. Trọng số không chứng minh AI luôn chọn.

Không tìm thấy provider tên riêng chỉ chứa điều kiện công cụ cơ sở. Vì vậy plan dùng biểu thức OR từ nguồn thật tại19.4, không bịa một trigger đã tồn tại. CSV root kiểm đường bỏ F02, trước/sau kỳ, có/không mặc định và sau hạn programme; đây là kiểm hợp đồng giấy, chưa kiểm AI hoặc routing engine.

## Cohesion và phục hồi

[Tính toán hiện hành](VIE_REGIONAL_DIPLOMACY_L1_CALCULATIONS_VI.md) gồm mọi band và ca snapshot sau một lần vượt phản đối. [CSV band](VIE_REGIONAL_DIPLOMACY_L1_COHESION_BANDS_VI.csv), [CSV mọi trạng thái](VIE_REGIONAL_DIPLOMACY_L1_COHESION_STATES_VI.csv), [CSV sau vượt](VIE_REGIONAL_DIPLOMACY_L1_OVERRIDE_VI.csv), [CSV R0](VIE_REGIONAL_DIPLOMACY_L1_ROOT_CASES_VI.csv) được xuất từ script.

Các số dùng đúng cohesion_initial, override_cohesion, cadre_cohesion_required và recovery của JSON chính trị. Hai khóa đã có ở chính trị là override_cohesion và program_start_latest được thêm dưới dạng tham chiếu B1 để kiểm ca mới; không thêm giá/timer gameplay mới. Phục hồi tính từ cooldown trống, đủ PP và không có biến động khác. Thời gian chờ có thể vượt hạn bắt đầu, nên không khẳng định đường phục hồi luôn kịp.

Reader phí cũ chỉ được giữ trong CSV chẩn đoán với trạng thái retired; không áp dụng. Bảng tính không quy trade opinion, research bonus, thời gian hoặc tên cờ cơ hội thành PP.

## Gate và ownership đã có ngay trong plan

B1=X theo lựa chọn người dùng, là giả định gameplay. Bối cảnh hợp tác hàng hải/cứu nạn trước XIII đã có tại [DOC của ASEAN](https://asean.org/declaration-on-the-conduct-of-parties-in-the-south-china-sea-3/); không dùng tên DOC cho chương trình giả định B. S1=XIII là giả định phân kỳ nội dung, dù quan hệ có nền sớm; không dùng gate này để khẳng định niên đại quan hệ. Ngày các đại hội lấy từ JSON/tài liệu chính trị, không tạo ngày mới.

| Chủ đề | Owner | Ranh giới ngoại giao / consumer | Vị trí plan |
|---|---|---|---|
| Sự cố biển đã viết | Chính trị XI08, XIII01–04, XIII10–11 | B chỉ đọc đúng hồ sơ/kết quả; cứu nạn mới có owner B riêng, không thưởng cùng đối tượng | 6,17.4,19.3,19.5 |
| Hồ sơ vốn/trái phiếu và bảo lãnh | Chính trị XIII05–08 | S không sửa kỳ hạn, cứu dự án/người mua hoặc bảo lãnh; S chỉ chương trình kỹ thuật/đào tạo nước ngoài khác hồ sơ | 17.6,19.5 |
| Mở cửa/quyền dữ liệu trong nước | Chính trị X05–X08 | W3 là bằng chứng gói kỹ thuật cụ thể; W4 là hỗ trợ/đánh giá đối tác. Không thay ngoại lệ, quyền truy cập hoặc thưởng lại cải cách X | 17.7,19.5 |
| Hợp đồng kỹ thuật E104/XIII09/XIII12 | Hiện chính trị; đích một owner giao thức chung | E/S/W chưa ghi vào cùng record; chỉ chuyển sau C qua kiểm và kiểm adapter riêng | 19.6 |

Catalog chính trị ghi XIII05–08 là hồ sơ trái phiếu trong nước; câu tóm tắt cũ “quan hệ lớn” không được dùng làm bằng chứng rằng chúng sở hữu mọi quan hệ với nước ngoài. Nếu hai nhánh chạm cùng đối tượng/source epoch thì chỉ owner ghi reward/điều kiện, nhánh kia đọc. Không sửa node chính trị để đạt bảng này.

W3/W4 không tạo quyền chia sẻ dữ liệu bị record X chặn: chọn phạm vi được phép hoặc dừng gói. Không tự thêm khoản hoàn PP/thưởng theo reader W. Chưa có ID state mới được coi là provider thật.

## Đổi tên/slug B và sơ đồ

Mapping đầy đủ nằm trong registry và [CSV đổi tên](VIE_REGIONAL_DIPLOMACY_L1_B_RENAMES_VI.csv). B7 đã phù hợp cứu nạn nên giữ; các node còn lại đổi tên/slug. Đây là ID tài liệu dự kiến, chưa là ID engine/loc được nạp. Không sửa loc hoặc gameplay hiện tại.

Catalog, title metadata và chữ hiển thị SVG đã đồng bộ, PNG xuất lại từ SVG ở kích thước gốc. Hình học, số node, cost, prerequisite/AND-OR, anchor và tọa độ giữ nguyên. Đã xem preview; kiểm kích thước và độ vừa hộp chữ bằng font/pixel gốc. Không suy từ preview sơ đồ sang nghiệm thu UI HOI4.

**N1 của B vẫn FAIL:** chưa đủ hai gói khác loại, hai event khác cấu trúc, yếu tố phản hồi đối tác và hậu quả kỳ sau theo yêu cầu L3. Không giảm cụm/node hoặc lấp bằng node rỗng.

## Kế hoạch chuyển E104

Kế hoạch có mục riêng ngay trong plan19.6: điều kiện C qua kiểm; mapping đối tác/đối tượng/source epoch và mọi hỗ trợ/quyền/nghĩa vụ; adapter một owner; chiều ngược chỉ đọc chứng cứ đúng hợp đồng; kiểm phản hồi cũ/thanh toán/migration; điều kiện đóng nợ. Giữ giá/lịch/nghĩa vụ E104, không thu phí/slot lần hai. Chưa thực hiện bước chuyển nào. **J5 giữ FAIL như nợ đã biết.**

## Changelog kiểm soát

| Mục | Cũ | Mới | Lý do | Các chỗ cập nhật theo |
|---|---|---|---|---|
| R0 | IX AND F02 | IX AND (F02 OR mặc định đại hội) | Không tự khóa khi bỏ F02; dùng provider nền đã đọc | 1,6,15.1,16,19.3–19.4,21.3,24.2,SVG,CSV root/hồ sơ |
| Reader cohesion | Chờ bỏ/thay; từng có đề xuất nhân phí | Chọn gate sâu C/E theo ngưỡng hiện có; phí gốc giữ nguyên | Có tác dụng lựa chọn sau vượt phản đối | 6,14.2–14.3,14.8,16,17.5,19.2–19.4,21.2–21.3,24.2,script/B1/CSV |
| B1 | Tạm XIII | X, giả định gameplay | Đã chọn kỳ sớm, tách khỏi sự cố chính trị | 15.1,16,17.4,registry,SVG/B1/hồ sơ |
| Tên/slug B | Các nhãn cũ còn mang nghĩa tranh chấp | Nhãn cứu nạn theo mapping | Tránh kỳ vọng sai | Catalog16,17.4,SVG/PNG,CSV mapping/hồ sơ |
| S vs XIII05–08 | Chưa ghi rõ tại17.6 | S khác hồ sơ trái phiếu nội địa; S1 giữ XIII giả định | Có một owner đúng hồ sơ | 15.1,16,17.6,19.5,hồ sơ |
| W vs X05–X08 | Chưa ghi rõ tại17.7 | W3/W4 không viết lại quy trình/quyền dữ liệu chính trị | Không thưởng/điều kiện trùng | 17.7,19.5,hồ sơ |
| E104 | Câu hứa/đường dẫn kế hoạch | Mục riêng19.6 trong plan | Có nội dung review được | 19.4–19.6,24.3,hồ sơ/J5 |
| Kiểm liên kết file | Đếm cố định cũ | Đếm lần xuất hiện và đích duy nhất khi chạy | Không giữ số lỗi thời | 24.3,báo cáo bất biến/kiểm/script |
| Trạng thái liên kết | Tier/kiêm nhiệm chưa có consumer | G/P/C có consumer thiết kế; T hoãn. J2 không tự PASS vì chênh ngày | Không thổi số liên kết thực | 6,19.3–19.4,21.3,hồ sơ/J1/J2 |

## Các mục không đổi

Giữ tổng focus/cụm, mã R/C/M/A/B/E/S/W, cost, đồ thị/anchor/tọa độ, giá triển khai/phí tháng/trần modifier. Các phần ngoài L1 không được thiết kế lại; chưa hợp nhất bản cũ hoặc viết sáu cụm theo L3. Các mâu thuẫn A04/duy trì/tham số ở bản cũ còn báo H2 FAIL để xử lý đúng L4.

Giữ nguyên tài liệu/JSON/CSV/script chính trị, Trung Quốc, game focus/effect/event/decision/idea/loc, AI runtime và generator. Giữ hai master ngoại giao và export game của chúng. Hash gốc vẫn giữ, không reset để che đổi nguồn; thay SVG/PNG sơ đồ được kiểm riêng là export được yêu cầu.

## Kiểm chứng và điểm cần quyết

Chạy python -X utf8 VIE_REGIONAL_DIPLOMACY_REVIEW_VI.py --self-test; chỉ thêm --export-layout khi cần dựng lại sơ đồ. Script trả exit1 khi bất biến còn FAIL. [Bảng bất biến bàn giao](VIE_REGIONAL_DIPLOMACY_L1_INVARIANTS_VI.md) có số link thực, ca R0/AI và kết quả kiểm bảo toàn; chưa kiểm engine/playtest.

**J1 PASS ở mức giao diện thiết kế; J4 PASS; J2 FAIL do P; J5 FAIL do chuyển E104 còn hoãn.** Không có xác nhận rằng ba reader đều đổi hành vi: chỉ G/C có đối chứng đủ, P còn thiếu, T chưa active.

Quyết định bổ sung của người dùng: giữ P đúng lịch đã chốt, để J2 FAIL và chưa đóng L1. Không còn câu hỏi mở về P cho lần bàn giao này. Không tự thêm deadline, tham số hoặc đổi nghĩa bất biến để đóng L1. Chưa bắt đầu L2.
