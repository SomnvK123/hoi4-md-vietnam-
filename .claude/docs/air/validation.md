## Current v24 - PK-KQ Y1-Y12 layout

- Focus tree: 424 total; 37 PK-KQ focuses. `audit.py`: no duplicate coordinates, dangling prerequisites/anchors, forward anchors, or cycles.
- `air_scenarios.py`: ALL PASS, 144 paths; covers all four First Force prerequisites, Teaming's Datalink gate, and D5's 2/3 capstone condition.
- Absolute PK-KQ rows: root y=2; readiness y=5; structures y=7; C2/Medium Force y=8; specialty roots y=9; components and Datalink y=10; tanker y=11; capstones y=12; integration y=13.
- HOI4 was not launched; PNG/XML are static diagrams and do not verify engine connector rendering.

## Reward chuẩn bị lực lượng v25 — 09/10/2026

- Hoàn thiện bốn reward sau Cải tổ I; chi tiết ở `VIE_air_force_documentation.md`, mục v25. Tổng 25 XP/mastery và 15 CP; modifier riêng GCI +0,25% detection, trung đoàn −0,5% chi phí nhân sự, căn cứ dự bị +1% home defence.
- `air_scenarios.py`: PASS từng reward, nhánh XP/mastery, 48 thứ tự hoàn thành và 144 đường hoàn chỉnh. `air_force_balance.py`: ALL PASS, đối chiếu 26/26 reward; detection gồm các trục khác tối đa 19,75/20%, home defence 16,5/20%, mission efficiency vẫn 16/16%.
- `audit.py`: 424 focus, 0 lỗi anchor/prerequisite/vòng lặp/tọa độ. `live.py`: 0 MISSING; vẫn ghi nhận idea cũ không dùng `VIE_airf_branch_mismatch_idea`, không phát sinh từ sửa reward này. Hai kiểm tra localisation: 0 lỗi, 3641 key.
- Chưa kiểm tra trong HOI4: tooltip reward, mastery khi đã chọn học thuyết, CP khi gần trần và dynamic modifier sau khi hoàn tất từng focus. Save đã hoàn tất các focus này không được hồi tố reward mới.

# Kiểm định PK-KQ v23 — 09/10/2026

## Bổ sung v23 — 09/10/2026

- Căn Cải cách II, Tiêm kích đa nhiệm và focus tích hợp tối cao về trục tuyệt đối x=220; cân các nhóm con quanh trục cha và giữ ba capstone cùng hàng y=15.
- Thêm `VIE_airf_tactical_exercises` giữa Cải cách I và Củng cố lực lượng; diễn tập cho 10 air XP. Tanker xuống y=16; focus tích hợp ở (220,17) chỉ nối ba capstone, bỏ cạnh trực tiếp dài từ Cải cách II vì quan hệ đó đã được bao hàm.
- Datalink đặt dưới Cải cách II và thành prerequisite trực tiếp của Tiêm kích đa nhiệm, tránh node treo; Teaming vẫn đòi B1 qua tooltip, nên gate C3 của Teaming được giữ mà không cần cạnh cắt nhánh.
- Kết quả: `audit.py` 421 focus, 0 trùng tọa độ/anchor/prerequisite treo/forward-ref/chu trình; `air_scenarios.py` ALL PASS (144 đường); giao cắt orthogonal của PK-KQ = 0 (Manhattan 209); `air_ai_options.py` problems 0; `air_force_balance.py` ALL PASS; localisation 0 lỗi, 3635 key; draw.io XML hợp lệ; `git diff --check` sạch.
- Đã xuất lại preview/sơ đồ/tài liệu quan hệ. Chưa mở HOI4 runtime để xác nhận cách engine vẽ dây trong game.

## Bổ sung v22 — 09/10/2026

- Tăng khoảng cách các node cùng hàng chuyên ngành từ 2 lên 4; cột SAM/tiêm kích/UAV và ba capstone được đặt lại trên lưới rộng hơn.
- Chuyển điều kiện hoàn tất Datalink và Tiêm kích đa năng của `VIE_airf_teaming` sang `available` với tooltip hiển thị rõ hai focus; điều kiện chơi không đổi nhưng hai dây chéo nhánh được bỏ khỏi cây.
- Đưa Datalink sang phía trái nhánh và căn `teaming` dưới strike UAV để tránh đường từ Cải tổ II cắt vào B1 và tránh dây C3 chạy qua các node chuyên ngành.
- Kết quả: `audit.py` 420 focus, 0 ô trùng/anchor lỗi/forward-ref/chu trình; `air_scenarios.py` ALL PASS (144 đường); giao cắt orthogonal trong PK-KQ = 0; `audit_loc_errors.py` 0 lỗi; `verify_all_loc.py` 3633 key, 0 lỗi; `git diff --check` sạch.
- Đã xuất lại `air_after.json`, `air_changes.md`, `air_redesign.drawio` và `air_after.png`, xem PNG ở kích thước render. HOI4 runtime vẫn chưa được mở để kiểm tra pixel/layout của engine.

## Bổ sung v21 — 09/10/2026

- `VIE_airf_multirole` yêu cầu AND `VIE_airf_command_reform_2` và `VIE_airf_medium_force`.
- `VIE_airf_multirole_fleet`, `VIE_airf_sustainment` và `VIE_airf_operating_range` cùng mở trực tiếp từ `VIE_airf_multirole`; `VIE_airf_multirole_wing` cần cả ba. Tanker tiếp tục phụ thuộc bán kính tác chiến nhưng không bắt buộc cho capstone.
- Cập nhật fixture `air_scenarios.py` để kiểm graph/tầng mới, tanker còn dưới operating range và ba capstone cùng hàng.
- Kết quả: `audit.py` 420 focus, 0 trùng tọa độ/prerequisite/anchor/forward-ref/chu trình; `air_scenarios.py` ALL PASS (144 đường); `air_ai_options.py` problems 0; `air_force_balance.py` ALL PASS; `git diff --check` sạch.
- Chưa mở game để xác nhận line routing/render thực tế.

## Bổ sung v20 — 09/10/2026

- Bố cục PK-KQ được xếp lại theo tầng; ba capstone ở hàng y=14, `VIE_airf_integrated_force` ở y=16. Quan hệ/reward và preview đã xuất lại trong `air_after.json`, `air_changes.md`, `air_redesign.drawio` và `air_after.png`.
- `VIE_airf_teaming` nay yêu cầu trực tiếp `VIE_airf_multirole`, ngoài datalink và hai focus UAV; trigger tích hợp/D1 và reward không đổi.
- `python tools/audit/audit.py`: 420 focus; 0 trùng tọa độ, prerequisite/anchor treo, forward anchor hoặc chu trình.
- `python tools/audit/air_scenarios.py`: ALL PASS, gồm 144 đường phát triển và kiểm tra chặn teaming khi thiếu focus đa nhiệm.
- `python tools/audit/air_ai_options.py`: problems 0.
- Chưa mở game để kiểm tra routing, tooltip hoặc runtime; sơ đồ tĩnh không xác nhận cách HOI4 vẽ đường nối.

## Kiểm tra tĩnh

12 lệnh bên dưới đã chạy sau khi đổi sang một hàng lựa chọn và chức năng chuyên ngành song song, bằng Python runtime có sẵn. Ba kiểm tra không quân ban đầu bị mất module trong đợt dọn tool đồng thời; đã chuyển sang module hiện hành `air_scenarios.py` và chạy lại các kiểm tra bị ảnh hưởng. Kết quả cuối: cả 12 exit 0. Diagnostics đầy đủ ở từng log; không dùng exit code riêng làm bằng chứng sạch.

| Kiểm tra | Kết quả | Log |
|---|---|---|
| `tools/audit/audit.py` | 420 focus; 0 ID/anchor/prerequisite treo, chu trình, trùng ô, forward anchor, thiếu vị trí | [focus](audit_logs/audit.log) |
| `tools/audit/live.py` | 0 MISSING; 1 idea legacy không còn caller mới, giải thích dưới | [refs](audit_logs/live.log) |
| `tools/audit/ev.py` | 0 ID trùng; cảnh báo loc 14 event ẩn có từ trước | [event](audit_logs/ev.log) |
| `tools/audit/prov.py` | Tổng lỗi 0 | [province](audit_logs/prov.log) |
| `tools/audit_loc_errors.py` | 0 lỗi; không thiếu tên/mô tả/tooltip focus | [loc syntax](audit_logs/audit_loc_errors.log) |
| `tools/verify_all_loc.py` | 69 file, 3632 key; 0 lỗi/BOM/key focus thiếu | [loc](audit_logs/verify_all_loc.log) |
| `tools/audit_dds_and_gfx.py` | 405 DDS; 0 lỗi file/texture/sprite focus; 234 cảnh báo event sprite ngoài submod | [DDS/GFX](audit_logs/audit_dds_and_gfx.log) |
| `tools/audit/air_proc_balance.py` | ALL PASS; mua sắm không đổi | [procurement](audit_logs/air_proc_balance.log) |
| `tools/audit/air_ind_balance.py` | ALL PASS; giá/thời lượng cơ sở giữ nguyên | [industry](audit_logs/air_ind_balance.log) |
| `tools/audit/air_force_balance.py` | ALL PASS; đọc effects thật, kiểm 8 tập hợp cụm cùng tồn tại | [force](audit_logs/air_force_balance.log) |
| `tools/audit/air_ai_options.py` | problems 0; `.13` được kiểm theo gate/weight thật | [AI options](audit_logs/air_ai_options.log) |
| `tools/audit/air_scenarios.py` | ALL PASS, các fixture bên dưới | [scenarios](audit_logs/air_scenarios.log) |

Fixture kiểm 29 ID cũ/33 tổng, tọa độ/anchor/gap, một hàng mutex, củng cố trước lựa chọn, các cặp chức năng cùng hàng và AND hội tụ, CNF 2/3, F7 đúng 3/4. Có 144 đường phát triển (save mới hoặc 3 biến policy legacy ×3 cơ cấu ×3 cặp đích ×BBA/non-BBA ×AAT/no-AAT), với thứ tự điện tử trước radar và tấn công UAV trước trinh sát để chứng minh độc lập. A+B không cần UAV; cả ba cặp không cần tanker. Kiểm thiếu thành phần/đích/D4/F7 bị chặn, 174 ca giá công nghiệp/giảm giá độc lập policy legacy, giá D1/D2, bonus chuyển vị trí chống lặp, D5 chọn rõ mục tiêu và chỉ một lần, slot/pending và 620 trạng thái AI có gate thật.

### Cảnh báo đã đọc

- `VIE_airf_branch_mismatch_idea` giữ định nghĩa cho save cũ; không còn caller cấp mới vì đã bỏ phạt lệch hướng. Không thêm caller giả để audit xanh; không xóa buff/debuff đã nhận từ save cũ.
- 14 event bị báo thiếu loc là event ẩn, gồm `vie_air_force.51` với `hidden = yes`; nội dung/ID của các event này giữ nguyên. Đây là hạn chế nhận diện của audit, không thêm loc giả.
- Kiểm toàn bộ 234 cảnh báo sprite event ngoài submod, không chỉ 20 dòng mẫu: cả **31 token duy nhất** đều có định nghĩa trong bản HOI4/MD đã cài. [Danh sách provider](external_sprite_providers.json). Sprite focus mới đều dùng định nghĩa hiện hữu và texture thật trong submod.
- Các dòng `ZERO` của AI options là chủ đích historical, không phải lỗi. `.12/.13/.21/.23` được kiểm bằng trạng thái khả đạt và trigger option thực; không thêm lựa chọn giả. Cảnh báo cũ `.13` không còn là kết luận thiếu option.

## Tích hợp

Cây, effects/triggers, decisions/events, loc/getters và AI factors đã tích hợp trên `main`. 387 focus ngoài phạm vi có AST và tọa độ trùng HEAD. Artwork/assets/interface không đổi; không sửa hải quân, mua sắm hoặc BBA/non-BBA equipment effects. Localisation PK-KQ ở file thường, không có key PK-KQ trùng trong `replace/`; file mới có UTF-8 BOM. XML có hai trang, không nén, rectangle cho focus, dashed OR và một LINK mỗi cặp mutex.

Root chung ở (220, 2); công nghiệp ở hàng 3/4/6/8, lực lượng giữ năm tầng và rút từ 18 xuống 16 hàng. Bỏ ba focus ngân sách v18; T5 mở từ Cải cách I, A2/A3 và C2/C4 mở ngang, A4/C5 hội tụ AND đủ thành phần, B2/B3 cùng hàng. Tám key tên/mô tả của ba cơ cấu và đích hiệp đồng có đúng một provider trong file localisation PK-KQ hiện hữu, UTF-8 BOM, không bị replace ghi đè. Các ngưỡng công nghiệp và reward thường trực của v18 giữ nguyên; bonus 25% chuyển sang A1/B1/C1, giá không còn hệ số toàn nhánh, D5 có ba decision dùng chung guard một lần.

XML đã kiểm hai trang 36/33 rectangle, các connection FROM/TO và đúng ba cặp LINK của một nhóm mutex; tên trước sửa được đóng băng trong manifest v18. Bản preview chỉ biểu diễn sơ đồ; các dải tầng trong ảnh là chú thích tài liệu, không phải GUI được thêm vào game. Tài liệu hợp nhất hiện hành là [VIE_air_force_documentation.md](../../../VIE_air_force_documentation.md).

`git diff --check` trong phạm vi code/tool PK-KQ không có lỗi whitespace. Kiểm toàn workspace còn báo hai dấu cách cuối dòng 418 của `VIE_economic_branch_redesign.md`, thuộc thay đổi tài liệu kinh tế đồng thời; đợt PK-KQ không sửa dòng đó.

## Kiểm trong game

**Chưa thực hiện.** Không có thao tác mở cây/chạy chương trình/hover hoặc `error.log` của một phiên HOI4 mới làm bằng chứng. Cần save mới, kiểm các bước ở [tools/TESTING.md](../../../tools/TESTING.md). Không gọi fixture Python là mô phỏng đầy đủ HOI4; không xác nhận designer/DLC, thời lượng engine hoặc AI chạy đúng từ fixture.
