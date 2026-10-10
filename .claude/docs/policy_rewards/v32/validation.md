# Nghiệm thu effect chính sách v32 — 10/10/2026

## File tĩnh và scenario

Chạy `tools/audit/policy_rewards.py`. PASS cho:

- 46 reward trực tiếp, reward chạy trước khi engine đặt completed focus; replay không thêm PP/tiền/điểm/bonus/công trình. Bốn mutex bảo vệ cả hai chiều.
- 35 idea đúng modifier; mỗi nhóm một bậc, không downgrade, refresh idempotent. Cảng/logistics và đa phương thức không tồn tại cộng chồng.
- Thiết kế/OSAT, đô thị/HSR đi hai thứ tự; các biên km; bậc chính sách không thay gate bàn giao.
- Refund giữ chính sách, không nâng năng lực. Hợp đồng start, finish, refund, cleanup, bonus, công trình và điểm giữ nguyên tại AST ngoài thay đổi idea.
- Toàn bộ focus block và decision/trigger/event giữ nguyên theo baseline mới. Baseline v30/v31 không sửa.
- 64 tổ hợp công nghiệp, 20 bộ ba, 16 tổ hợp hạ tầng; 8 đường công nghiệp và 12 đường hạ tầng đúng ngân sách. Kiểm trần modifier ở từng bước effect, không chỉ lúc hoàn thiện.
- Lifecycle thiếu tiền/đúng giá/bấm lặp/mất state/state đầy/slot song song; scheduler/catch-up, Vinashin, Formosa, HSR debt và các thông báo không thưởng lại.

Các fixture JSON kiểm lưu dữ liệu và timer trong evaluator; không phải save/load HOI4. Evaluator có giới hạn, token lạ bị từ chối. Trục/opinion upstream được ghi nhận lời gọi, không mô phỏng toàn bộ hệ thống chính trị MD.

Audit repo chạy focus/reference/event/state/localisation/DDS-GFX; log và exit code tại `audit_logs/`. Đọc diagnostic ngay cả exit 0. Cảnh báo cũ về idea PK-KQ mồ côi, loc event ngoài phạm vi và sprite event vanilla được báo riêng; không sửa nhánh khác hoặc giảm độ nghiêm của validator.

## Tích hợp/provider

`tools/audit/policy_assets.py <MD directory>` kiểm toàn bộ 35 idea mới từ consumer → sprite → texture. Bốn picture tái sử dụng: digitalize_idea, economic_boom, economic_road_idea, industrial_focus. Kiểm native size/frame và xem contact sheet không resize. Modifier, bao gồm tốc độ xây dockyard, có định nghĩa sử dụng thật trong MD. Tên vùng tooltip đối chiếu MD state_names.

Không có artwork mới, không đổi DDS/GFX/master. Provider kiểm file trên máy; chưa xác minh cách engine render tooltip mới.

## In-game — chưa thực hiện

Game mới bắt buộc. Chưa có phiên HOI4 nghiệm thu v32. Cần kiểm:

1. Hover đủ 46 focus: ba phần reward rõ ràng, tên vùng/idea render đúng, modifier nhận ngay đúng với idea sau hoàn thành. Không dùng ignoreprerequisites làm bằng chứng.
2. Theo từng nhóm: focus cấp chính sách → đầu tư → bàn giao thay bậc; không hai idea cùng nhóm. Đường bộ chọn bậc cao nhất, cảng/logistics hội tụ, sân bay 25/50/75/87,5/100%, fab thay nền tảng.
3. Cả hai thứ tự thiết kế/OSAT và metro/HSR; policy không mở innovation/EV alliance/capstone trước bàn giao thật.
4. Treasury trước/sau start, finish và refund; không helper thu thêm. Mất sở hữu/kiểm soát, state đầy, slot song song và save/load khi đang đầu tư.
5. Mutex, gọi/event lặp, debt HSR/Vinashin giữ nguyên; AI chính sách/giải ngân theo điều kiện thật; error.log không có lỗi effect/idea/tooltip mới.

Chỉ báo nghiệm thu runtime sau khi hoàn thành checklist trong game. File/scenario/provider PASS không thay thế bước này.

## Snapshot audit cuối

- Focus: 353 toàn cây, giữ 24 công nghiệp/22 hạ tầng; không dangling, trùng ô, forward anchor, cycle hoặc thiếu x/y.
- Policy scenario: PASS (exit 0), bao gồm hai nhánh cùng nước, root init một lần, slot độc lập và replay mỗi remove_effect trong các route.
- Provider: PASS 35 consumer idea, bốn sprite/texture native. Không có lỗi modifier thuộc v32.
- Localization: 0 lỗi cú pháp, 0 focus thiếu title/desc; file mới 116 key, BOM. DDS/GFX: 0 lỗi format/texturefile.
- Reference audit exit 0 nhưng diagnostic có **4 focus + 1 tooltip ngoài phạm vi chưa khép kín** trong mã quân sự được bổ sung đồng thời: VIE_lf_complex_terrain_mobile_capstone, VIE_lf_modern_elite_combined_army_capstone, VIE_lf_operational_counteroffensive_capstone, VIE_lf_sf_special_warfare_capstone; tooltip VIE_v31_joint_modernization_ready_tt. Các effect/idea/tooltip v32 không MISSING. Không sửa hoặc bỏ qua diagnostic này.
- Một idea ngoài phạm vi chưa có caller: VIE_vpa_modern_joint_autonomous_idea. Event audit còn 12 diagnostic loc quân sự/chính trị cũ; DDS audit liệt kê ảnh event vanilla đã có provider ngoài submod.
- git diff --check exit 0 tại snapshot cuối.

Audit policy ban đầu gặp modifier dạng block trong idea quân sự mới ngoài phạm vi. Đã giới hạn việc đổi numeric vào danh sách idea mà audit v32 sở hữu, vẫn kiểm chính xác toàn bộ modifier của các idea đó; không thay reference validator hoặc các baseline cũ. Lần chạy lại policy cuối đã PASS, log/results ghi riêng thời điểm chạy lại. Không coi exit 0 của reference audit là toàn repo sạch.
