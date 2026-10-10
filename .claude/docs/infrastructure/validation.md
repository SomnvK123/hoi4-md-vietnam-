# Kiểm định hạ tầng v30 — 09/10/2026

**File tĩnh và fixture tích hợp đạt; chưa kiểm thử trong HOI4.** Yêu cầu game mới. Fixture timer/save không chứng minh runtime của engine.

**Cập nhật kiểm tra cuối:** guard bảo toàn baseline hiện trả lỗi vì 18 block Lục quân tiếp tục thay đổi trong workspace sau lần kiểm hash 394/394 đạt trước đó. Baseline không được sửa và các thay đổi ngoài hạ tầng được giữ nguyên. Mọi scenario chức năng/graph hạ tầng và AI vẫn đạt; lệnh tổng `infra_scenarios.py` kết thúc khác 0 ở guard baseline. Đây là chênh lệch workspace, không phải một kết quả xanh hoàn toàn của lệnh tổng.

## File tĩnh

| Script | Kết quả |
|---|---|
| `tools/audit/audit.py` | 416 focus; 0 prerequisite/anchor/mutex treo, trùng ô, forward anchor, cycle, thiếu tọa độ |
| `tools/audit/live.py` | 0 MISSING mọi nhóm; 0 event mồ côi; idea mồ côi có sẵn `VIE_airf_branch_mismatch_idea` ngoài phạm vi |
| `tools/audit/prov.py` | Tổng lỗi 0; không còn cảnh báo state 813 sau điều chỉnh |
| `tools/audit_loc_errors.py` | 0 lỗi cú pháp, thiếu title/desc/tooltip |
| `tools/verify_all_loc.py` | 69 YML đạt; 240 key infra; 416 focus đủ title/desc |
| `tools/audit/ev.py` | 0 ID trùng, 0 event mồ côi; 9 event hạ tầng đủ loc; 14 cảnh báo loc ngoài hạ tầng |
| `tools/audit_dds_and_gfx.py` | 405 DDS: 0 lỗi/blank; 0 texture thiếu, 0 custom focus sprite thiếu; 240 reference event picture ngoài checkout |

## Fixture tích hợp

`python tools/audit/infra_scenarios.py` đọc AST code thật và helper MD trong snapshot repo. Evaluator giới hạn token, không mô phỏng đầy đủ engine, opinion, axes hay AI.

- Graph 22 node, archive 28, hash 394 block ngoài hạ tầng nguyên vẹn; anchor trực tiếp, mutex đối xứng, gap hàng ≥2, state đất liền VIE.
- Cả 16 trạng thái ngành: 0–2 khóa capstone, 3–4 mở; focus chưa bàn giao không đủ.
- 12 đường vốn/partner, ngân sách 83,25–98,5 tỷ, idea không cộng dồn, bonus một lần; sân bay dân dụng không cấp air base.
- Đủ tiền đúng bằng chi phí, bấm/finish lặp, slot từng ngành/song song, mất sở hữu/kiểm soát hoàn tiền/thử lại, trần công trình không fallback; fixture lưu/nạp timer.
- Km 999/1.000, 2.999/3.000, 4.999/5.000; debt early 10 năm/China lịch sử 5 năm; Vân Đồn/lưỡng dụng tùy chọn.
- Cooldown giữ lựa chọn bắt buộc, catch-up, partner biến mất/chờ/thử lại, option lặp; thông báo không reward.
- Growth 0,088/trade 0,073/construction 0,20; loc consumer duy nhất, title/desc ID bỏ đã dọn.
- Trọng số AI lịch sử/chính sách, partner 50/50/40; bankruptcy chỉ chặn AI, không chặn player gate.

## Sơ đồ và sprite

Sơ đồ trước/sau xuất bằng Pillow từ snapshot/mã hiện tại, đã xem ảnh. Hình kiểm bố trí quan hệ, chưa kiểm routing/icon HOI4. Không chạy layout tool toàn cây.

Đã tra sprite dùng trong Workshop MD trên máy: blueprint, hai chính sách vốn, improve roads, supply line, industry investment, maritime trade, aviation industry; category/decision và idea đường bộ. Không sửa DDS. Audit submod không kiểm đầy đủ sprite ngoài checkout; kiểm consumer/provider riêng và hình trong game vẫn cần.

`python tools/audit/infra_assets.py <MD-directory>` đã xác nhận 10 sprite/texture provider và xuất [contact sheet kích thước gốc](reused_icons_native.png), đã xem ảnh: 7 focus icon 100×88, maritime 89×84, decision 33×32, idea 60×68; một frame mỗi sprite. Không áp kích thước icon custom của repo lên asset MD có sẵn. Đây là kiểm file/provider và preview 1:1, chưa xác nhận consumer render trong engine.

## Checklist trong game — chưa thực hiện

1. Game VIE 2000 mới, playset MD trước submod; đọc `error.log` khi nạp và sau từng kịch bản.
2. Hover bốn trục, mutex, AND/OR/capstone; icon/title UI scale thật. Không dùng `ignoreprerequisites` làm bằng chứng.
3. Hai vốn đường bộ, hai vốn sân bay, ba partner HSR: treasury trước/sau chi/sau bàn giao, không thu lần hai, bậc idea/km đúng.
4. HSR sớm và lịch sử: ngày mở, vote một lần, debt khi giải ngân, bonus đào tạo một lần, mô tả rollout ban đầu.
5. Bấm lặp/thiếu tiền; mất sở hữu/kiểm soát khi đang chạy, hoàn đúng khoản; state đầy không xây ngẫu nhiên.
6. Save/load giữa đợt ở bốn ngành; timer/busy/finish một lần. Bốn ngành song song, không hai đợt cùng ngành.
7. Capstone 0–4 ngành và cả bốn bộ ba hợp lệ; focus mở chưa đủ; tooltip progress/màu đúng.
8. Cooldown qua mốc event, save/load khi queue, catch-up dài, lặp event; partner biến mất trước/sau ký, pending không bị mất.
9. Vân Đồn/lưỡng dụng tùy chọn; dân dụng không tăng air base; optional không khóa capstone.
10. AI lịch sử đủ/thiếu tiền và mission phá sản; không chi mất khả năng thanh toán; `error.log` không lỗi mới.

## Diagnostic toàn repo

Idea mồ côi PK-KQ có sẵn được giữ nguyên. Validator event có thể báo nhầm thiếu loc cho event ẩn ngoài hạ tầng như hướng dẫn repo đã ghi; không giảm mức kiểm tra để làm xanh.

Danh sách 14 cảnh báo loc ngoài hạ tầng: `vie_air_force.51`, `vie_lf.2`, `vie_lf.4`, `vie_nav_force.51`, `vie_nav_force.71`, `vie_naval.45`, `.52`, `.54`, `.56`, `vie_p1b.12`, `.14`, `.17`, `.18`, `.21`. Không thay code những nhánh này trong đợt triển khai. Cảnh báo 240 event picture có các token `GFX_report_event_generic_*` do vanilla/MD cung cấp, như hạn chế validator đã ghi; không coi tất cả là asset lỗi của submod.

18 block khác baseline ở lần cuối: `VIE_lf_fs_main_corps`, `VIE_lf_fs_lean_corps`, `VIE_lf_mech_fire_support`, `VIE_lf_mech_coordination`, `VIE_lf_mech_equipment`, `VIE_lf_mech_sustainment`, `VIE_lf_mech_complete`, `VIE_lf_fs_mobile_force`, `VIE_lf_fs_mobile_corps`, `VIE_lf_mobile_sustainment`, `VIE_lf_mobile_fire_support`, `VIE_lf_dev_strategic`, `VIE_lf_fs_depth_defence`, `VIE_lf_fs_militia_units`, `VIE_lf_territorial_coordination`, `VIE_lf_territorial_reserve`, `VIE_lf_dev_territorial`, `VIE_lf_command_reform_2`.
