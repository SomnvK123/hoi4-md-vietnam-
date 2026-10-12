# Kế hoạch code nhánh tên lửa V5

Ngày lập: 12/10/2026. Cập nhật: mốc A đã được code trên nhánh `missile-v5`, header v50; kiểm file/provider qua, chưa chạy HOI4. Mốc B mapping/sản xuất trang bị chưa bật.

## 1. Nguồn thiết kế, phạm vi và kết quả khảo sát

Nguồn người dùng cung cấp:

- `C:/Users/sonds.ctv/Downloads/BAO_CAO_TONG_HOP_TEN_LUA_V5_CONTENT_EFFECT_CONVENTION_LAYOUT.md`: nội dung, reward, ý nghĩa các hệ thống và giới hạn bằng chứng.
- `C:/Users/sonds.ctv/Downloads/TEN_LUA_FOCUS_LAYOUT_EFFECT_V5.html`: thứ tự node và đồ thị prerequisite. HTML là sơ đồ thiết kế, không phải file engine.
- Quy ước repo: `.claude/CLAUDE.md`, `docs/conventions.md`, `docs/localisation.md`, `docs/engine-pitfalls.md`, `docs/validation.md`, `VIE_focus_coding_standards.md`; skills `md-focus`, `validate`, `md-art`; hướng dẫn AI và art guide hiện hành.

Các đoạn code trong báo cáo là ví dụ thiết kế, không phải chỉ thị để chạy formatter upstream hoặc bằng chứng rằng ID mới đã tồn tại. Quy ước repo thực tế quyết định cách tích hợp; yêu cầu người dùng quyết định layout và phạm vi nội dung.

### 1.1. Những điều giữ nguyên

- Chính xác 10 focus, hình `1 → 6 → 2 → 1`, không mutex, không nối prerequisite giữa sáu focus cùng hàng.
- Cánh A: Scud-B, Redut-M, Rubezh; cánh B: chương trình VCM-01, sản phẩm VSM-01A, tổ hợp VCS-01. Không diễn giải cánh B thành ba tên lửa độc lập.
- Focus cấp năng lực và mở Decision; Decision thực hiện đầu tư; kết quả nghiệm thu đến sau thời gian xử lý.
- Không nhập Bastion/Yakhont, EXTRA, AccuLAR, BM-21, SAM vào nhánh mới; không đổi reward Hải quân/PK-KQ/Lục quân hiện có.
- Giữ ma trận reward focus và tổng chi 9,5 tỷ USD của báo cáo làm balance đầu tiên. Các giá trị mới bổ sung trong kế hoạch là mặc định gameplay để playtest, không phải ngân sách hoặc mốc lịch sử.
- M04/M09 có nghĩa tự chủ bảo đảm và một số năng lực công nghiệp; không tuyên bố tự chủ toàn bộ công nghệ tên lửa.

### 1.2. Bằng chứng từ checkout hiện tại

- Cây được nạp là `focus_tree = { id = VIE_md_focus }`, có **408 focus** khi khảo sát. Header mới nhất là v49; phiên bản tiếp theo phải lấy từ header tại lúc code, không hardcode v50 nếu cây đã thay đổi.
- `VIE_modernize_vpa` ở tọa độ tuyệt đối `(202,1)`. X lớn nhất là 267, thuộc `VIE_air8_i06_viettel_tactical_uav` tại Y=4.
- Không tìm thấy định nghĩa mới `VIE_msl_*` hoặc namespace `vie_msl` trong common/events/loc/interface; nhật ký cũ vẫn nhắc tên nhánh tên lửa đã bị gỡ. Không phục hồi từ nhật ký hoặc file lưu trữ.
- Repo có thay đổi hải quân chưa commit. Kế hoạch này chỉ thêm tài liệu; khi code phải giữ toàn bộ thay đổi người dùng và chỉ chèn phần mới vào cây.
- Provider MD đọc từ `D:/ide/Millennium-Dawn`, commit `60accbc19a19369d8c4095b40b5144d5bb6c0fd2`. Ghi lại commit khi triển khai nếu provider thay đổi.
- Hai category nghiên cứu có định nghĩa trong `common/technology_tags/00_technology.txt`: `CAT_missiles`, `CAT_military_electronics`.
- `modify_treasury_effect` được định nghĩa trong `common/scripted_effects/00_budget_effects.txt`, dòng 1487: cộng `treasury_change` vào treasury, cập nhật tiền, có ngoại lệ debug `MD_skip_treasury_cost`. Tooltip MD hiển thị đơn vị Billion. Khoản chi -1,0 tương ứng 1 tỷ USD trong gameplay.
- Guided/ballistic/SAM là mẫu equipment cố định theo công nghệ; `MD_guided_missiles.txt` và `MD_ballistic_missiles.txt` không khai báo module slots/categories cho designer. `guided_missile_equipment_2` là GLCM đời 1975, range 3000, không chứng minh là VSM/VCS.
- MD có `MD_countrymissilesview.gui`, scripted GUI missile/space, Special Project và mô hình sản xuất riêng; những thứ này không chứng minh có designer ráp module cho VCS. Giao diện space còn có OLV/GNSS/COMSAT/SPYSAT/KILLSAT, không được nhầm với dây chuyền Trường Sơn.
- Có `VIE_nav35_P02` cấp guided missiles và spirit coastal batteries; đó là hành vi hiện hữu, không phải mapping tên lửa Việt Nam đã được xác thực.

### 1.3. Quyết định về trang bị theo trả lời của người dùng

Người dùng yêu cầu: có cơ chế thiết kế tên lửa thì mở rộng thiết kế trang bị riêng; không có thì chọn phương án 1. Với provider đã khảo sát, **chọn phương án 1**: không xây designer/equipment tree mới trong đợt này.

Phân hai mốc nghiệm thu:

1. **Mốc A, triển khai được ngay:** 10 focus, ba bảo dưỡng có lợi ích thực, ba chương trình timed, nghiệm thu VCM/VSM/VCS, ba spirit, AI, loc, layout và audit. M08/M09 phải đạt được, độc lập với mapping trang bị.
2. **Mốc B, sản xuất thật:** chỉ bật batch/công suất khi xác minh được consumer và mapping đúng trong MD. Chưa có mapping thì không thu tiền, không tạo trang bị thay thế, không tuyên bố sản xuất hoàn chỉnh. Giữ hai Decision dưới trạng thái chỉ dành debug để bảo toàn spec V5; bản chơi thường không có nút giả hoạt động.

Không dùng thiếu designer để kết luận MD không có tên lửa hoặc không thể thêm equipment bằng script. Việc tự thiết kế cơ chế chiến đấu cho VCS là phạm vi riêng, chỉ đưa trở lại nếu có bằng chứng hoặc yêu cầu mở rộng sau này.

## 2. Hợp đồng focus và layout

### 2.1. ID, tên và điều kiện

| Mã | ID focus | Tên hiển thị | Prerequisite, tất cả là AND | Available bổ sung | Cost |
|---|---|---|---|---|---:|
| M00 | `VIE_msl_national_program` | Chương trình tên lửa trọng điểm quốc gia | `VIE_modernize_vpa` | Không | 5 |
| M01 | `VIE_msl_scud_b_maintenance` | Duy trì lực lượng Scud-B | M00 | Không | 5 |
| M02 | `VIE_msl_redut_maintenance` | Duy trì tổ hợp Redut-M | M00 | Không | 5 |
| M03 | `VIE_msl_rubezh_maintenance` | Duy trì tổ hợp Rubezh | M00 | Không | 5 |
| M05 | `VIE_msl_vcm01_program` | Chương trình VCM-01 | M00 | Không | 7 |
| M06 | `VIE_msl_vsm01a_song_hong` | VSM-01A Sông Hồng | M00 | Không | 7 |
| M07 | `VIE_msl_vcs01_truong_son` | VCS-01 Trường Sơn | M00 | Không | 7 |
| M04 | `VIE_msl_technical_autonomy` | Làm chủ bảo đảm kỹ thuật tên lửa | M01 + M02 + M03 | Không | 7 |
| M08 | `VIE_msl_cruise_missile_industry` | Làm chủ thiết kế và sản xuất tên lửa hành trình | M05 + M06 + M07 | `VIE_msl_vcs_certified` | **8** |
| M09 | `VIE_msl_national_capability` | Phát triển năng lực tên lửa quốc gia | M04 + M08 | Không | 5 |

M08 cost 8 là ngoại lệ có chủ đích để giữ spec V5, phải ghi trong kế hoạch và test; không tự sửa thành 7 theo mặc định skill. Cost là điểm thời gian, không phải PP hoặc treasury. Tài liệu repo có mô tả số ngày không đồng nhất với renderer hiện có; chỉ ghi cost trong spec, xác nhận số ngày từ defines/game thực trước khi đưa vào loc.

M06/M07 không bị khóa bởi cờ VCM/VSM trong focus: có thể chuẩn bị song song. Chỉ Decision của chúng mới yêu cầu nghiệm thu giai đoạn trước. Không thêm date gate của người chơi khi báo cáo chưa xác lập năm bắt đầu chương trình.

### 2.2. Tọa độ chốt cho cây đang khảo sát

Giữ các độ lệch cục bộ của V5. Đặt M00 bên phải PK-KQ; không dời nhánh cũ. Anchor của capstone đổi sang một prerequisite trực tiếp để phù hợp repo, nhưng tọa độ tuyệt đối và đồ thị HTML không đổi.

| Mã | X tuyệt đối | Y tuyệt đối | Anchor trong code | x tương đối | y tương đối |
|---|---:|---:|---|---:|---:|
| M00 | 284 | 2 | `VIE_modernize_vpa` | 82 | 1 |
| M01 | 269 | 4 | M00 | -15 | 2 |
| M02 | 273 | 4 | M00 | -11 | 2 |
| M03 | 277 | 4 | M00 | -7 | 2 |
| M05 | 291 | 4 | M00 | 7 | 2 |
| M06 | 295 | 4 | M00 | 11 | 2 |
| M07 | 299 | 4 | M00 | 15 | 2 |
| M04 | 273 | 6 | M02 | 0 | 2 |
| M08 | 295 | 6 | M06 | 0 | 2 |
| M09 | 284 | 8 | M04 | 11 | 2 |

Đã tính tọa độ từ parser live: cả 10 vị trí không va chạm/gap<2 với cây 408 focus. M01 cách node ngoài cụm ở X=267 đúng 2. Sáu node giữa có gap nội bộ 4,4,14,4,4. Chiều ngang toàn cây tăng 32 đơn vị ở phía phải; đây là mở lane cho nội dung mới, cần ghi rõ khi review.

Nếu cây thay đổi trước lúc code, tính lại tọa độ và cập nhật manifest, không tin mốc 408 hoặc X=267 cố định. Không tự dời nhánh khác để giữ con số này.

Đồ thị engine phải có đúng **15 cạnh** gồm cạnh từ root quân sự: 1 vào M00, 6 từ M00, 3 vào M04, 3 vào M08, 2 vào M09. Mỗi cha tại capstone là một block prerequisite riêng; không gộp thành OR. Không có bypass, mutex hoặc prerequisite cùng hàng.

Thứ tự khai báo: M00 → M01 → M02 → M03 → M05 → M06 → M07 → M04 → M08 → M09. Thêm một section riêng trong cây sau root đã tồn tại; không tạo focus_tree thứ hai. Không thêm shortcut trong v1.

HTML dùng bus để trực quan; HOI4 tự vẽ connector. Không viết GUI để giả bus. Cạnh `(202,1) → (284,2)` dài 82 đơn vị cần review đường nối trong game, audit tọa độ không xác nhận cạnh đó đẹp.

## 3. Reward, spirit và quy tắc ngân sách

### 3.1. Ma trận reward thực hiện

Mỗi focus gọi một reward effect riêng `VIE_msl_m00_reward` … `VIE_msl_m09_reward`. Đây là ID **mới cần tạo**, không phải helper sẵn có. Focus vẫn log ở dòng đầu; effect dùng guard riêng `VIE_msl_mXX_reward_applied` để ngăn gọi lại từ debug/recovery làm trừ tiền hoặc thưởng hai lần.

| Mã | Reward tức thì | Decision được thông báo mở | Treasury |
|---|---|---|---:|
| M00 | Bonus `CAT_missiles` 0.10, uses=1; set `VIE_msl_program_started` | Category chương trình | -1.0 |
| M01 | Land XP/mastery 5 | `VIE_msl_dec_scud_sustainment` | -0.4 |
| M02 | Naval XP/mastery 5 | `VIE_msl_dec_redut_sustainment` | -0.4 |
| M03 | Naval XP/mastery 5 | `VIE_msl_dec_rubezh_sustainment` | -0.4 |
| M04 | `VIE_msl_sustainment_idea` | Không thêm decision tùy chọn | -0.8 |
| M05 | Bonus `CAT_missiles` 0.25, uses=1 | `VIE_msl_dec_vcm_development` | -1.0 |
| M06 | Bonus `CAT_missiles` 0.15, uses=1 | `VIE_msl_dec_vsm_validation` | -1.5 |
| M07 | Bonus `CAT_military_electronics` 0.20, uses=1 | `VIE_msl_dec_vcs_integration` | -2.0 |
| M08 | `VIE_msl_industry_idea` | Batch/công suất khi integration sẵn sàng; mốc A tooltip nêu sản xuất chưa tích hợp | -2.0 |
| M09 | PP +20; gỡ hai spirit trước; thêm `VIE_msl_integrated_idea` | Không thêm decision tùy chọn | 0 |

Chốt bỏ hai Decision **tùy chọn** joint maintenance/long term trong v1 để không tạo hệ thống thiếu đặc tả. Không đưa `unlock_decision_tooltip` trỏ vào ID chưa định nghĩa.

XP/mastery: áp dụng mẫu doctrine-aware thật của repo. M01: nếu `has_selected_land_grand_doctrine = yes`, `add_mastery = { amount = 5 folder = land }`; còn lại `army_experience = 5`. M02/M03 tương tự naval. Đây là thích nghi convention với V5, giữ giá trị 5, không cộng cả XP và mastery. Dùng một helper naval 5 cho hai reward; phần land 5 có thể inline trong reward. Không gọi helper 10/15 rồi tự trừ phần chênh.

Research: `name` dùng ID focus tương ứng, bonus và uses đúng bảng, không ahead_reduction, không unlock tech tự động. Tổng là ba bonus missiles riêng 10%/25%/15%, mỗi bonus một lượt; không trình bày như +50% vĩnh viễn. Bonus electronics của M07 có tác dụng rộng hơn radar VCS, phải mô tả đúng.

Tiền: đúng country scope, `set_temp_variable = { treasury_change = -N }` rồi `modify_treasury_effect = yes`. Không tự cộng/trừ `treasury`, không chi thêm lần nữa ở event hoàn tất, không cấp nhà máy miễn phí. Debug skip-cost của MD được tôn trọng và test riêng.

Reward focus chi tiền không thêm hard gate treasury cho người chơi, phù hợp thiết kế repo. AI chỉ bắt đầu khi đủ tiền cho focus tương ứng và không đang bankruptcy. Decision có gate đủ vốn thực tế, không được nhấp khi thiếu tiền.

### 3.2. Ba spirit cố định

| Idea | Modifier chính xác | Nguồn cấp |
|---|---|---|
| `VIE_msl_sustainment_idea` | `experience_gain_army_factor = 0.02`; `experience_gain_navy_factor = 0.02` | M04 |
| `VIE_msl_industry_idea` | `production_factory_efficiency_gain_factor = 0.02`; `research_speed_factor = 0.01` | M08 |
| `VIE_msl_integrated_idea` | Army/Navy XP gain 0.02 mỗi loại; efficiency gain 0.025; research speed 0.01 | M09 |

`ideas = { country = { ... } }`; `allowed = { original_tag = VIE }`, không dùng tag cứng để loại quốc gia sau nội chiến. Modifier toàn quốc phải ghi rõ; không gọi chúng là bonus chỉ dành tên lửa.

M09 gỡ M04/M08 riêng, mỗi lần có `has_idea` guard, rồi cấp integrated. Reward M04/M08 khi bị gọi lại sau M09 không tái cấp spirit cũ. Integrated có ưu tiên cao nhất; dùng helper `VIE_msl_refresh_spirits` đọc các cờ reward_applied của M04/M08/M09 để phục hồi đúng tập idea, không phát thêm XP/PP/tiền/research. Set reward_applied trước khi refresh để không phụ thuộc thời điểm engine đánh dấu focus completed. Helper cần ít nhất các call site reward M04/M08/M09, không phải controller hàng tháng.

Không dùng `swap_ideas` một lần để thay hai idea, không dùng dynamic modifier mới. Không đụng `VIE_af_*`, `VIE_armed_forces_modifier` hoặc trần modifier các quân chủng.

### 3.3. Ba timed idea cho bảo dưỡng

Báo cáo yêu cầu cờ bảo dưỡng có consumer hoặc timed idea hữu ích. Repo chưa có consumer bảo dưỡng Scud/Redut/Rubezh, nên chọn timed idea; không tạo cờ chỉ để tồn tại.

| Idea mới | Modifier | Duration | Ý nghĩa |
|---|---|---:|---|
| `VIE_msl_scud_sustainment_active_idea` | `experience_gain_army_factor = 0.005` | 365 ngày | Chu kỳ bảo đảm và huấn luyện |
| `VIE_msl_redut_sustainment_active_idea` | `experience_gain_navy_factor = 0.0025` | 365 ngày | Chu kỳ bảo đảm khí tài bờ |
| `VIE_msl_rubezh_sustainment_active_idea` | `experience_gain_navy_factor = 0.0025` | 365 ngày | Chu kỳ bảo đảm khí tài bờ |

Đây là bổ sung balance cho phần báo cáo chưa chốt, không phải sửa reward ba spirit. Ba Decision không cho XP tức thì mỗi lần, không sản sinh đạn, không tăng attack/range/reliability. Timed idea có tác dụng toàn quân chủng; đây là proxy nhỏ cho huấn luyện bảo đảm, không giả lập sức khỏe một quả tên lửa.

Trần đóng góp nhánh mới khi M09 và đủ ba chu kỳ đang active: Army XP gain 2,5%, Navy XP gain 2,5%, efficiency gain 2,5%, research speed 1%. Không cộng timed idea thành spirit vĩnh viễn. Không tự hết hạn M04 khi timed idea kết thúc.

## 4. Decision, tiến trình và vòng đời trạng thái

### 4.1. Category và cơ chế chung

Tạo `VIE_msl_program_category`, `allowed = { original_tag = VIE }`, `visible = { has_country_flag = VIE_msl_program_started }`, priority=80 theo nhóm chương trình hiện có.

`unlock_decision_tooltip` chỉ là mô tả. Mở khóa thật nằm trong category/Decision `visible` và `available`. Focus không đặt cờ duplicate kiểu M05_unlocked khi có thể đọc `has_completed_focus`.

Decision thu PP bằng `cost`, treasury bằng effect; hai khoản hiển thị riêng. Mỗi complete_effect log trước, sau đó gọi start effect có kiểm lại gate và giao dịch một lần. Tiến trình timed dùng `days_remove` + `remove_effect`, như hợp đồng/chương trình live của repo; không giả thanh tiến độ bằng country_event days=180.

Không dùng `fire_only_once = yes` cùng timer cho các Decision timed. Done/certified là gate kết thúc thật. Timer runtime phải test save/load, trạng thái active/visibility, kết thúc và chọn lại; fixture chỉ kiểm script không xác nhận timer engine.

### 4.2. Ba Decision bảo dưỡng lặp

| ID | Visible | Available | PP | Treasury | Cooldown |
|---|---|---|---:|---:|---:|
| `VIE_msl_dec_scud_sustainment` | M01 completed | Chưa có timed idea Scud; treasury≥0.1 | 20 | -0.1 | 365 ngày |
| `VIE_msl_dec_redut_sustainment` | M02 completed | Chưa có timed idea Redut; treasury≥0.1 | 15 | -0.1 | 365 ngày |
| `VIE_msl_dec_rubezh_sustainment` | M03 completed | Chưa có timed idea Rubezh; treasury≥0.1 | 15 | -0.1 | 365 ngày |

`days_re_enable = 365`, không fire_only_once; complete_effect trừ vốn rồi add_timed_idea theo bảng. Không cần days_remove hoặc event bảo dưỡng. Nếu người chơi mất timed idea sớm, cooldown engine vẫn chặn spam. Available dùng `has_idea`, không cần flag maintained trùng trạng thái.

0,1 tỷ/lần là mặc định mới của plan. Cả ba lần một chu kỳ tốn 50 PP và 0,3 tỷ USD; không thưởng lại research/XP khi chọn. Gate lực lượng/OOB thật chưa được thiết kế thì không invent `has_scud_unit`.

### 4.3. Ba chương trình phát triển tuần tự

| Decision | Visible | Available bắt buộc | PP | Vốn | Timer | Callback | Kết quả |
|---|---|---|---:|---:|---:|---|---|
| `VIE_msl_dec_vcm_development` | M05 completed; chưa vcm_ready | Chưa vcm_in_progress; treasury≥0.5 | 50 | -0.5 | 180 ngày | `vie_msl.10` | vcm_ready |
| `VIE_msl_dec_vsm_validation` | M06 completed; chưa vsm_certified | vcm_ready; chưa vsm_in_progress; treasury≥0.75 | 50 | -0.75 | 180 ngày | `vie_msl.20` | vsm_certified |
| `VIE_msl_dec_vcs_integration` | M07 completed; chưa vcs_certified | vsm_certified; chưa vcs_in_progress; treasury≥1.0 | 75 | -1.0 | 180 ngày | `vie_msl.30` | vcs_certified |

VCM 0,5 tỷ/180 ngày lấy từ ví dụ báo cáo. VSM 0,75 tỷ/180 ngày và VCS 1 tỷ/180 ngày là mặc định bổ sung của plan; không giả nhận báo cáo đã chốt chúng. Không lấy năm công bố 2024 làm gate bắt đầu R&D.

Start effect đặt cờ in_progress **không hạn**, chi vốn một lần. Không cho cờ hết hạn đúng ngày callback để tránh race. PP do engine trừ khi chọn; không trừ PP trong helper hoặc callback. Timer completion gọi event **ngay lúc remove_effect**, không đặt thêm delay 180 ngày nữa.

Chọn callback **hidden**, `is_triggered_only = yes`, không MTTH, namespace `vie_msl`. Không tạo hai option nhận cùng kết quả nhưng một option phạt PP vô lý như ví dụ báo cáo. Đây là nghiệm thu kỹ thuật tất định, không cần ba popup một nút OK. Trong `immediate` của event: log, gọi finish effect; finish kiểm in_progress và chưa done, đặt cờ ready/certified, clear in_progress. Không thu tiền thêm, không grant research thêm. Callback chỉ được gọi từ remove_effect của chương trình, không đặt trigger chạy tự động toàn thế giới.

Các cờ:

| Cờ mới | Ai ghi | Ai đọc | Khi clear |
|---|---|---|---|
| `VIE_msl_program_started` | Reward M00 | Category | Không, thành tựu chương trình |
| `VIE_msl_vcm_in_progress` | Start VCM | Available và finish VCM | Finish VCM |
| `VIE_msl_vcm_ready` | Finish VCM | Available VSM | Không |
| `VIE_msl_vsm_in_progress` | Start VSM | Available và finish VSM | Finish VSM |
| `VIE_msl_vsm_certified` | Finish VSM | Available VCS | Không |
| `VIE_msl_vcs_in_progress` | Start VCS | Available và finish VCS | Finish VCS |
| `VIE_msl_vcs_certified` | Finish VCS | M08, batch/công suất | Không |
| `VIE_msl_mXX_reward_applied` | Reward focus tương ứng | Guard reward, refresh spirit | Không |

Không random failure, không delayed event có hai caller, không flags expiry dùng thay timer. Với luồng tất định không cần retry gameplay; callback trùng vô hại. Nếu runtime chứng minh timer mất khi hủy/reload, phải sửa lifecycle trước nghiệm thu, không bỏ gate M08 để che bug.

M08 available dùng custom_trigger_tooltip giải thích phải hoàn thành nghiệm thu VCS, với key `VIE_tt_msl_vcs_certified`. VSM/VCS visible ngay sau focus tương ứng, available tooltip chỉ rõ chương trình trước còn thiếu. Người chơi thấy việc cần làm, không giấu Decision rồi để focus khóa không lời giải.

Tổng vốn focus + ba chương trình bắt buộc: **11,75 tỷ USD**; PP chương trình: **175**. Bảo dưỡng lặp tùy chọn không phải gate M04/M09. Thời gian nghiên cứu tối thiểu tuần tự 540 ngày sau khi đủ điều kiện; focus có thể thực hiện trong lúc chương trình chạy.

### 4.4. Batch/công suất: hợp đồng tích hợp ở mốc B

Tạo đúng ID báo cáo `VIE_msl_dec_batch_production` và `VIE_msl_dec_expand_industry`; mốc A chỉ visible khi debug AND M08 completed. Available đọc trigger mới `VIE_msl_equipment_mapping_ready` trả false trong mốc A, có tooltip dành developer. Không nút disabled cho người chơi thường, không dùng always=no trên M08.

M08 ở mốc A vẫn cấp spirit và thể hiện thành tựu thiết kế/nghiệm thu; mô tả nói rõ công nghiệp được công nhận, cơ chế giao trang bị chưa thuộc bản tích hợp hiện hành. Không dùng lời hứa đã giao tên lửa. Khi mốc B đạt, thay trigger bằng kiểm tra mapping/tech thật, cho hai Decision visible sau M08, cập nhật tooltip unlock/loc và ghi phiên bản.

Checklist bắt buộc trước khi bật mapping:

1. Xác định sản phẩm delivery là đạn VSM, launcher hay tổ hợp VCS; chỉ định consumer thật: equipment/unit/mission hoặc hệ thống scripted MD sử dụng nó.
2. Có định nghĩa archetype/type và tech unlock, khả năng hoạt động trong combat; đối chiếu DLC Gotterdammerung bật/tắt. Không thấy designer không phải bằng chứng về compatibility DLC.
3. Có bằng chứng tên, range, role và quantity không nhầm GLCM/IRBM/SAM với hệ thống đối hạm; không lấy existing stockpile reward P02 làm bằng chứng.
4. Ghi manifest mapping: provider commit, definition path/ID, technology, delivery effect, quantity/unit, relevant mission/consumer, DLC condition và case test engine. Khi chưa có hàng mapping hợp lệ, giữ trigger false.
5. Không bật bằng cờ developer do focus tự set. Mapping readiness là điều kiện kỹ thuật tích hợp thực, không phải cờ tiến độ gameplay.

Thiết kế giao dịch dự kiến sau khi mapping qua review: batch 50 PP, -0,5 tỷ, 180 ngày, một lô active; expansion 50 PP, -1,5 tỷ, 365 ngày, một lần, tăng tier 0→1. Expansion nâng **năng lực lô** bằng dữ liệu delivery đã xác minh, không thêm modifier toàn quốc vô hạn. Lượng giao và mức tăng tier phải chốt trong manifest mốc B theo đơn vị sản phẩm đã xác minh; hiện chưa có bằng chứng để chốt số quả/tổ hợp.

Hai con số tiền/thời gian trên là budget đề xuất cho mốc B, không phải giao dịch đang được phép chạy. Không thể nghiệm thu sản xuất chỉ với hai nút chưa có delivery. Nếu mapping không tồn tại, mốc A vẫn hoàn thành nhưng báo cáo phải ghi rõ mốc B chưa triển khai; không invent equipment tree hoặc designer để lấp chỗ trống.

## 5. Convention và bố trí code

### 5.1. Những file sẽ thêm/sửa khi triển khai

| Phần | Đường dẫn dự kiến | Nội dung |
|---|---|---|
| Cây | `common/national_focus/VIE_md_focus.txt` | Chèn 10 focus, section và header phiên bản |
| Reward/state | `common/scripted_effects/VIE_md_effects_missile.txt` | 10 reward, start/finish, refresh spirit, helper naval 5 |
| Gates | `common/scripted_triggers/VIE_md_triggers_missile.txt` | Gates start dùng chung available/start guard; mapping readiness |
| Decision | `common/decisions/VIE_md_missile_decisions.txt` | 3 bảo dưỡng, 3 chương trình, 2 integration stub debug |
| Category | `common/decisions/categories/VIE_md_missile_categories.txt` | Một category |
| Ideas | `common/ideas/VIE_md_missile_ideas.txt` | 3 permanent + 3 timed |
| Callback | `events/VIE_md_missile_events.txt` | Namespace vie_msl; hidden .10/.20/.30 |
| Loc | `localisation/english/VIE_missile_l_english.yml` | Focus/category/Decision/idea/tooltip tiếng Việt |
| AI | `common/ai_strategy_plans/VIE_strategy_plans.txt` | Chỉ thêm trọng số focus vào hồ sơ hiện có |
| Test | `tools/audit/missile_v5_spec.json`, `tools/audit/missile_scenarios.py` | Hợp đồng dữ liệu và fixture đọc live script |
| Layout | `tools/focus_layout/missile_diagram_v5.py` | Manifest/PNG từ tọa độ và prerequisite live |
| Tài liệu | Kế hoạch này và `.claude/docs/validation.md` | Phiên bản, lựa chọn, kết quả và giới hạn runtime |

Không sửa consolidated effects/events/decisions/ideas cũ chỉ để nhét nhánh mới. Reward riêng từng focus theo conventions repo dù báo cáo gợi ý chỉ tách helper khi có lặp; helper generic mới chỉ tạo khi có nhiều call site thật. Start trigger dùng chung available và start guard đáp ứng điều đó.

### 5.2. Format script

- Script `.txt`: UTF-8 không BOM; tab indent; mở `{` cùng dòng; line ending khớp file đích; một dòng trắng giữa focus.
- Thứ tự: id → icon → x/y → relative_position_id → cost → prerequisite → search_filters → available → completion_reward → ai_will_do cuối.
- Log focus trước reward effect. Decision complete/remove callback và event có log đúng ID/scope. Comment tiếng Việt không dấu.
- Không block rỗng, duplicate available, unknown modifier, reference treo, flags chỉ đọc không ghi, flags chỉ ghi không ai đọc, biến khởi tạo 0 vô ích.
- ID `VIE_msl_*`, tooltip `VIE_tt_msl_*`; event `vie_msl.N`. Không đổi prefix các nhánh cũ hoặc dùng `CHI_*` backing variable.
- Không gọi formatter upstream trên toàn cây. Repo không có standardization/pre-commit/pytest upstream; dùng bộ audit repo, review diff giới hạn vào phần mới.

### 5.3. Filters chốt

| Focus | Filters |
|---|---|
| M00, M05, M06, M07 | `FOCUS_FILTER_RESEARCH FOCUS_FILTER_EXPENDITURE` |
| M01 | `FOCUS_FILTER_ARMY FOCUS_FILTER_EXPENDITURE` |
| M02, M03 | `FOCUS_FILTER_NAVY FOCUS_FILTER_EXPENDITURE` |
| M04 | `FOCUS_FILTER_MILITARY_LAWS FOCUS_FILTER_EXPENDITURE` |
| M08 | `FOCUS_FILTER_INDUSTRY FOCUS_FILTER_EXPENDITURE` |
| M09 | `FOCUS_FILTER_MILITARY_LAWS` |

Một dòng, tối đa hai filter theo repo. M08 không sao chép ba filter trong ví dụ báo cáo. Không tạo filter riêng VIE_MISSILES hoặc dùng legacy MILITARY/AIR.

### 5.4. AI

- Base focus: M00=50; M01–M03=50; M04=45; M05–M07=50; M08=45; M09=40.
- Focus có chi vốn: factor=0 nếu đang bankruptcy hoặc treasury không đủ khoản chi bảng. M09 không bankruptcy guard vì không chi tiền. Dù mỗi focus dưới 5 tỷ, guard ở đây là lựa chọn thận trọng riêng cho chương trình mới; không hiểu cost 8 là chi 8 tỷ.
- Decision bảo dưỡng base=5; Decision nghiên cứu base=10; factor=0 khi bankruptcy/thiếu vốn/chưa thỏa gate. Mốc A batch/expansion factor=0.
- Historical ưu tiên tuyến A sớm bằng factor=2 ở M01–M04; tuyến B base=50 nhưng factor=0.25 khi historical trước 2015. Đây là pacing gameplay, không khẳng định năm bắt đầu thật; không gate date người chơi.
- Thêm các focus mới vào focus_factors của Historical và Hardline đang hoạt động; không tạo persona/plan thứ ba, không sửa chính trị/đối ngoại hoặc alt procurement rule.
- Rà sáu lớp AI theo tài liệu repo: focus/Decision cần thay đổi; templates/equipment/areas/theaters/navy chưa có consumer/trang bị mới ở mốc A nên kế thừa MD, không tạo override rỗng. Playtest phải xác nhận AI dành đủ PP/vốn cho ba bước và thực sự đạt M08.

### 5.5. Localisation và asset

- Toàn bộ text mới tiếng Việt có dấu trong file `l_english`, UTF-8 BOM, key `:0`, một space đầu dòng; ID mới đặt ở file thường, không replace nếu không ghi đè. Quy tắc này ưu tiên hơn ví dụ tiếng Anh và hướng dẫn replace cũ trong skill.
- 10 title/desc focus, category name/desc, 8 Decision name/desc, 6 idea name/desc; tooltip đủ vốn/chứng nhận/chương trình đang chạy/bảo dưỡng/mapping debug. Hidden event không cần title/desc/option loc.
- Mô tả focus nói ý nghĩa và phạm vi; tooltip chia lợi ích nhận ngay, Decision mở, gate nghiệm thu, PP, vốn và thời gian. Nêu bonus toàn quốc ở spirit, không viết sản xuất xong khi chỉ mở cơ chế.
- Không TODO hoặc tên token kỹ thuật trong giao diện người chơi. Tooltip mapping kỹ thuật chỉ hiện debug.
- Mốc A tái sử dụng sprite có định nghĩa thật, không sinh artwork trong đợt code logic. Có thể dùng `GFX_focus_VIE_nf_denial_defence` cho nhóm bảo dưỡng, `GFX_focus_VIE_nf_command_reform_2` cho root/capstone, sprite research có provider đã kiểm cho cánh B. Danh sách cuối cùng phải nằm trong manifest và xác nhận texture thực trước patch, không khai báo `GFX_focus_VIE_msl_*` chưa có ảnh.
- Ideas dùng picture token đã kiểm: `army_planning` cho sustainment/timed, `economic_boom` cho industry; integrated dùng army_planning. Provider xác nhận `GFX_idea_army_planning` và `GFX_idea_economic_boom` trong MD_ideas.gfx. Không đặt nguyên sprite token vào picture nếu consumer yêu cầu stem.
- Decision dùng provider đã xác minh: `GFX_decision_generic_military`, `GFX_decision_generic_naval`, `GFX_decision_generic_research`; category theo pattern repo không cần invent category icon. Callback hidden không cần ảnh event.
- Nếu thêm artwork riêng sau này, áp dụng md-art/art guide hiện hành, đo consumer thực, kiểm native size và alpha/format/frame. Focus profile hiện có 93×91 DDS BGRA không mipmap; không ép mọi consumer dùng khung vàng hoặc HUD. Hai master ngoại giao và export giữ nguyên.

## 6. Trình tự code và nghiệm thu

### P0 — Baseline và chốt dữ liệu

1. Khi bắt đầu code, tạo nhánh riêng hệ thống lớn; giữ thay đổi chưa commit, không reset/checkout đè file. Nếu cần isolated worktree, mang đúng baseline đã thỏa thuận thay vì vô tình bỏ patch hải quân.
2. Chụp status/diff hiện hữu, ghi provider commit, đếm focus/namespace/loc, tính lại tọa độ; baseline audit phải đọc diagnostics chứ không chỉ exit code.
3. Tạo spec JSON ghi 10 ID, AND groups, anchors, absolute/relative coordinates, cost/reward, money, Decisions/timers, idea modifiers và mapping status. Spec là hợp đồng QA, game không nạp.
4. Resolve sprite/texture thực và encoding; chưa có asset mới thì dùng provider thật. Không coi grep một usage là định nghĩa.

### P1 — Cơ chế hoàn chỉnh trước gate focus

1. Thêm category, ideas, reward/start/finish effects, reusable triggers, Decisions, hidden callbacks và loc cùng một thay đổi review được.
2. Kiểm start đủ tiền/đúng focus/giai đoạn trước; finish chỉ một lần; three-stage pipeline tất định; spirit không cộng chồng.
3. Mốc A batch/expansion debug-only không thu tiền. Không ship M08 gate chứng nhận nếu .10/.20/.30 chưa có caller hoàn tất.
4. Chuẩn bị scenario fixture đọc file thật; không kiểm chỉ bảng spec rồi tuyên bố script đúng.

### P2 — Focus, layout và AI

1. Chèn 10 focus vào cây hiện có theo bảng, trường và thứ tự đã chốt; cập nhật header phiên bản bằng ngày thực tế lúc triển khai.
2. Sinh PNG/manifest live, đối chiếu 15 cạnh với HTML, kiểm cả vùng lân cận PK-KQ. Preview không phải ảnh chụp game.
3. Thêm weights vào AI hiện hữu; không để AI phải click GUI player_context để nghiên cứu.
4. Chạy audit tổng và scenario; không sửa bug cũ hải quân ngoài phạm vi để làm output đẹp.

### P3 — Kiểm thử tĩnh

Các lệnh sau là nghiệm thu của **lần triển khai**, chưa chạy với nhánh tên lửa vì hiện chỉ có kế hoạch:

```text
python tools/audit/audit.py
python tools/audit/live.py
python tools/audit/ev.py
python tools/audit/prov.py
python tools/audit_loc_errors.py
python tools/verify_all_loc.py
python tools/audit_dds_and_gfx.py
python tools/audit/missile_scenarios.py --md D:/ide/Millennium-Dawn
python tools/focus_layout/missile_diagram_v5.py
git diff --check
```

Hai tool missile là **file mới phải viết**, không gọi trước khi tạo. Python stdout UTF-8 theo settings repo. Fixtures chỉ hỗ trợ những statement cần cho cơ chế, gặp token không hỗ trợ phải fail thay vì coi là pass. Không import audit.py trực tiếp để vô tình chạy reporting/ghi output; tái sử dụng parser theo AST hoặc helper parser thuần như naval_scenarios.

Cases bắt buộc:

| Nhóm | Scenario và kết quả mong đợi |
|---|---|
| Graph | 10 node; 6 cùng Y; đúng anchors; 15 cạnh; không OR/mutex/bypass/cycle/forward-ref; gap≥2, tọa độ đúng |
| Gate M04 | Từng trường hợp thiếu M01/M02/M03 đều khóa; đủ ba mở, không cần chạy bảo dưỡng |
| Gate M08 | Từng trường hợp thiếu M05/M06/M07 hoặc thiếu vcs_certified đều khóa; đủ bốn mở |
| Gate M09 | Thiếu từng capstone đều khóa; đủ hai mở |
| XP/mastery | M01/M02/M03 trước/sau chọn doctrine; đúng 5, không phát đồng thời, reward gọi lại không thưởng |
| Research | Đúng category/bonus/uses; bảo dưỡng không có bonus missile; callback không thưởng lại research |
| Treasury | Mỗi focus trừ đúng một lần, tổng -9.5; chương trình -2.25; thiếu/exact/above tiền; debug skip-cost không báo giao dịch thường |
| Programs | VSM trước VCM không start; VCS trước VSM không start; timer callback đúng cờ; thiếu in_progress/duplicate callback không nghiệm thu giả hoặc cộng reward |
| Timed lifecycle | Không nhấp lặp khi đang chạy; không trừ hai lần; finish clear đúng flag; hoàn tất xong không nghiên cứu lại |
| Maintenance | PP/vốn đúng; cooldown365; timed idea365; hết hạn làm Decision chọn lại; không đạn/XP tức thì/farm; trần modifier đúng |
| Spirits | M04/M08 riêng và kết hợp; M09 gỡ cả hai; gọi reward/refresh lặp vẫn chỉ spirit đúng, không cộng chồng |
| Integration | Mapping false: player không thấy stub, debug bị khóa, không chi/không equipment; chứng nhận VCS không tự bật mapping |
| Assets/loc | Mọi ref có định nghĩa; sprite ngoài checkout có provider; texture tồn tại; BOM/keys/tooltip/encoding đúng |
| Regression | IDs/gates/reward/event/cờ cũ hải quân và PK-KQ không thay đổi bởi patch missile; baseline lỗi cũ ghi riêng |

Đọc diagnostic output kể cả command trả 0. live.py không xác minh scope/runtime; event audit có thể báo hidden event thiếu loc sai; ảnh MD/base game ngoài checkout phải tra provider, không invent sprite để dập cảnh báo.

### P4 — Runtime tối thiểu

- Game mới VIE 2000, HOI4 1.19.*, playset submod sau MD; thử historical/hardline và Gotterdammerung bật/tắt.
- Kiểm UI toàn cây: root mới/cạnh dài, sáu node cùng hàng, AND hội tụ, icon/hover/tooltip gate; không đường đi qua card gây nhầm.
- Hoàn thành tuyến A/B với điều kiện thật; không chỉ dùng focus.autocomplete vì có thể bỏ qua lỗi gate. Xem M08 khóa trước và mở sau nghiệm thu.
- Chạy timer180 thực bằng tăng tốc thời gian, save/load giữa mỗi chương trình và sát ngày kết thúc; callback hoàn tất một lần, không thêm 180 ngày; không mất chương trình khi visible đổi.
- Bảo dưỡng hết hạn365/cooldown, ngân sách/PP thiếu, reward capstone không cộng spirit, AI click đủ ba giai đoạn và có khả năng đạt M09.
- Kiểm error.log/game.log với VIE_msl/vie_msl và token unknown. Không báo runtime PASS khi chỉ có fixture.
- Nếu không có game, báo rõ runtime chưa kiểm, để checklist cho người dùng; không gọi mốc A là đã hoạt động trong game.

### P5 — Mốc B sản xuất

Chỉ thực hiện sau khi manifest mapping có definition/consumer/tech/DLC và review gameplay. Bổ sung test start/cost/timer/delivery/duplicate delivery/expansion cap/đơn vị quantity/save-load/combat thật; giữ M09 không phụ thuộc một lô sản xuất. Nếu không thể mapping đúng, kết thúc ở mốc A và ghi giới hạn, không biến generic GLCM thành VCS bằng localisation.

## 7. Tiêu chí bàn giao

- Diff chỉ gồm nhánh mới và tích hợp cần thiết; giữ nguyên patch người dùng. Không tự commit/merge trong lần lập kế hoạch.
- Spec/manifest/layout, file gameplay, loc và tests khớp nhau; mọi giá trị bổ sung ngoài báo cáo ghi là balance dự kiến.
- Chính xác 10 focus, layout HTML được giữ, M08 có đường đạt chắc chắn, spirit không cộng chồng, tiền/reward chỉ phát một lần.
- Báo kết quả **file validation**, **integration validation**, **in-game validation** riêng; chỉ đánh dấu loại kiểm tra đã thực hiện.
- Mốc A có thể nghiệm thu riêng. Sản xuất trang bị mốc B là giới hạn còn mở do thiếu mapping, không phải lời hứa cơ chế đã hoàn thiện.
- Khi đổi thiết kế/balance lúc triển khai, cập nhật tài liệu này, spec và loc trước bàn giao để lần code tiếp theo không dùng hai chuẩn khác nhau.

## 8. Kết quả triển khai ngày 12/10/2026

- Đã thêm đúng 10 focus, 8 Decision (6 hoạt động + 2 stub debug), 6 idea và 3 hidden callback; cây 408 → 418 focus, 76 key loc mới.
- Giữ các tọa độ, anchor, cost và reward của plan; dùng sprite có định nghĩa thật. M08 cost 8 vẫn là ngoại lệ V5.
- Vốn ba chương trình 0,5/0,75/1,0 tỷ USD, thời gian 180 ngày mỗi chương trình; bảo dưỡng 0,1 tỷ USD/365 ngày theo mặc định balance kế hoạch.
- Fixture missile: 2.888 assertions PASS với provider MD và baseline. Hải quân: 1.292 scenario PASS. Không sửa reward/cơ chế quân chủng hiện hữu.
- Audit focus/ref/loc/province/DDS qua. Event audit có hai cảnh báo loc sai cho callback hidden; ảnh event cũ ngoài checkout vẫn có cảnh báo local.
- Sơ đồ live, manifest, native icon board và chi tiết kiểm định: [.claude/docs/missile/validation.md](.claude/docs/missile/validation.md).
- Chưa chạy game; không nghiệm thu timer/save-load/AI runtime. Không migration save cũ, không bật mapping sản xuất giả.
