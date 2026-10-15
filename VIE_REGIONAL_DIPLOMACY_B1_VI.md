# B1 — Bảng tham số duy nhất và kiểm baseline

**Phạm vi các kiểm dưới đây: baseline 51 node trước mở rộng C.** Ứng viên C mới có 18 node, toàn nhánh 63; [đặc tả và kiểm riêng](VIE_CHINA_EXPANDED_BRANCH_DESIGN_VI.md). H1 PASS baseline không chứng nhận ứng viên mới hoặc SVG tổng mới; J2/J5 vẫn FAIL.

**L1 đã áp các lựa chọn vào thiết kế: gate sâu C/E, B1=X, S1=XIII, R0 dùng F02 hoặc mặc định đại hội. J2/J5 vẫn FAIL, chưa đóng L1 hoặc sang L2.** Không sửa gameplay/chính trị.

Nguồn chuẩn: [registry](VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json). Dòng politics.* tham chiếu JSON chính trị trực tiếp; không lưu bản số thứ hai.
CSV/Markdown là bản sinh; sửa nguồn chuẩn rồi chạy lại script, không sửa tay bản xuất.
Đủ 11/11 file bắt buộc; chính trị có 74 node. Bảo vệ 19 nguồn: thay đổi ngoài phạm vi=[].
Đối chiếu giá với bảng nguồn: drift=[]; bảng ký/bands khớp tài liệu=True/True.

Đổi nhãn/export sơ đồ được yêu cầu: ['VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.svg', 'VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.png']; hình học giữ nguyên=True, PNG khớp render SVG=True.
[Tính lại gate cohesion đã chọn](VIE_REGIONAL_DIPLOMACY_L1_CALCULATIONS_VI.md); [hồ sơ L1](VIE_REGIONAL_DIPLOMACY_L1_REVIEW_VI.md); [bảng bất biến Markdown](VIE_REGIONAL_DIPLOMACY_L1_INVARIANTS_VI.md).

Đơn vị treasury: **chưa xác định trong tài liệu/JSON chính trị**; k không phải tỷ giá engine.
Ô treasury=null ở start/resume là tham chiếu giá gói/phí tháng, không phải 0.
CSV mentions là các ứng viên tìm theo từ khóa ở mục sử dụng, chưa chứng minh mọi cách diễn đạt đã được tìm.

| Tham số | Giá trị | Đơn vị | Nguồn | Các mục sử dụng |
|---|---|---|---|---|
| action.send.pp | 30.0 | PP | 21.1/Gửi đề nghị/pp | 14.3; 14.5; 14.8; 19.2; 21.1 |
| action.send.treasury | 0.0 | treasury_script_unit | 21.1/Gửi đề nghị/treasury | 14.3; 14.5; 14.8; 19.2; 21.1 |
| action.send.timer_days | 60.0 | day | 21.1/Gửi đề nghị/timer | 14.3; 14.5; 14.8; 19.2; 21.1 |
| action.resend.pp | 20.0 | PP | 21.1/Sửa và gửi lại/pp | 13.5; 13.8; 14.3; 14.4; 14.8; 19.2; 21.1 |
| action.resend.treasury | 0.0 | treasury_script_unit | 21.1/Sửa và gửi lại/treasury | 13.5; 13.8; 14.3; 14.4; 14.8; 19.2; 21.1 |
| action.resend.timer_days | 90.0 | day | 21.1/Sửa và gửi lại/timer | 13.5; 13.8; 14.3; 14.4; 14.8; 19.2; 21.1 |
| action.accept_partial.pp | 0.0 | PP | 21.1/Nhận phạm vi thu hẹp/pp | 13.5; 13.6; 14.3; 14.4; 17.1; 19.2; 21.1 |
| action.accept_partial.treasury | 0.0 | treasury_script_unit | 21.1/Nhận phạm vi thu hẹp/treasury | 13.5; 13.6; 14.3; 14.4; 17.1; 19.2; 21.1 |
| action.accept_partial.timer_days | 30.0 | day | 21.1/Nhận phạm vi thu hẹp/timer | 13.5; 13.6; 14.3; 14.4; 17.1; 19.2; 21.1 |
| action.start.pp | 0.0 | PP | 21.1/Bắt đầu sau đồng ý/pp | 14.3; 14.5; 14.8; 18.4; 19.2; 21.1 |
| action.start.treasury | null | treasury_script_unit | 21.1/Bắt đầu sau đồng ý/treasury | 14.3; 14.5; 14.8; 18.4; 19.2; 21.1 |
| action.start.timer_days | 180.0 | day | 21.1/Bắt đầu sau đồng ý/timer | 14.3; 14.5; 14.8; 18.4; 19.2; 21.1 |
| action.contingency_prepare.pp | 50.0 | PP | 21.1/Chuẩn bị dự phòng C/pp | 14.3; 14.7; 14.8; 17.1; 19.2; 21.1 |
| action.contingency_prepare.treasury | 0.0 | treasury_script_unit | 21.1/Chuẩn bị dự phòng C/treasury | 14.3; 14.7; 14.8; 17.1; 19.2; 21.1 |
| action.contingency_prepare.timer_days | 90.0 | day | 21.1/Chuẩn bị dự phòng C/timer | 14.3; 14.7; 14.8; 17.1; 19.2; 21.1 |
| action.contingency_use.pp | 20.0 | PP | 21.1/Kích hoạt dự phòng C/pp | 14.7; 14.8; 20.2; 21.1 |
| action.contingency_use.treasury | 0.0 | treasury_script_unit | 21.1/Kích hoạt dự phòng C/treasury | 14.7; 14.8; 20.2; 21.1 |
| action.contingency_use.timer_days | 90.0 | day | 21.1/Kích hoạt dự phòng C/timer | 14.7; 14.8; 20.2; 21.1 |
| action.issue_dialogue.pp | 35.0 | PP | 21.1/Đối thoại xử lý/pp | 14.6; 14.8; 19.2; 21.1 |
| action.issue_dialogue.treasury | 0.0 | treasury_script_unit | 21.1/Đối thoại xử lý/treasury | 14.6; 14.8; 19.2; 21.1 |
| action.issue_dialogue.timer_days | 30.0 | day | 21.1/Đối thoại xử lý/timer | 14.6; 14.8; 19.2; 21.1 |
| action.w_repair.pp | 20.0 | PP | 21.1/Sửa thực hiện W/pp | 17.7; 19.2; 21.1; 24.2 |
| action.w_repair.treasury | 1.0 | treasury_script_unit | 21.1/Sửa thực hiện W/treasury | 17.7; 19.2; 21.1; 24.2 |
| action.w_repair.timer_days | 90.0 | day | 21.1/Sửa thực hiện W/timer | 17.7; 19.2; 21.1; 24.2 |
| action.w_repair.max_per_run | 1 | count | 21.1/Sửa thực hiện W/một lần | 17.7; 19.2; 21.1; 24.2 |
| action.resume.pp | 20.0 | PP | 21.1/Nối lại chương trình/pp | 14.6; 19.2; 20.3; 21.1; 24.2 |
| action.resume.treasury | null | treasury_script_unit | 21.1/Nối lại chương trình/treasury | 14.6; 19.2; 20.3; 21.1; 24.2 |
| action.cancel.pp | 0.0 | PP | 21.1/Rút/hủy/pp | 5.2; 14.5; 18.4; 19.2; 21.1; 24.2 |
| action.cancel.treasury | 0.0 | treasury_script_unit | 21.1/Rút/hủy/treasury | 5.2; 14.5; 18.4; 19.2; 21.1; 24.2 |
| package.C.small.treasury | 2.0 | treasury_script_unit | 21.2/C thương mại/small | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.C.small.days | 180.0 | day | 21.2/C thương mại/small | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.C.small.monthly | 0.02 | treasury_script_unit/month | 21.2/C thương mại/small | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.C.deep.treasury | 5.0 | treasury_script_unit | 21.2/C thương mại/deep | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.C.deep.days | 365.0 | day | 21.2/C thương mại/deep | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.C.deep.monthly | 0.05 | treasury_script_unit/month | 21.2/C thương mại/deep | 14.8; 17.1; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.small.treasury | 2.0 | treasury_script_unit | 21.2/M dữ liệu/small | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.small.days | 180.0 | day | 21.2/M dữ liệu/small | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.small.monthly | 0.02 | treasury_script_unit/month | 21.2/M dữ liệu/small | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.deep.treasury | 4.0 | treasury_script_unit | 21.2/M dữ liệu/deep | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.deep.days | 365.0 | day | 21.2/M dữ liệu/deep | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.M.deep.monthly | 0.04 | treasury_script_unit/month | 21.2/M dữ liệu/deep | 14.8; 17.2; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.small.treasury | 3.0 | treasury_script_unit | 21.2/A sáng kiến/small | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.small.days | 180.0 | day | 21.2/A sáng kiến/small | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.small.monthly | 0.03 | treasury_script_unit/month | 21.2/A sáng kiến/small | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.deep.treasury | 5.0 | treasury_script_unit | 21.2/A sáng kiến/deep | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.deep.days | 365.0 | day | 21.2/A sáng kiến/deep | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.A.deep.monthly | 0.05 | treasury_script_unit/month | 21.2/A sáng kiến/deep | 14.8; 17.3; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.small.treasury | 1.0 | treasury_script_unit | 21.2/B cứu nạn/small | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.small.days | 120.0 | day | 21.2/B cứu nạn/small | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.small.monthly | 0.01 | treasury_script_unit/month | 21.2/B cứu nạn/small | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.deep.treasury | 3.0 | treasury_script_unit | 21.2/B cứu nạn/deep | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.deep.days | 180.0 | day | 21.2/B cứu nạn/deep | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.B.deep.monthly | 0.03 | treasury_script_unit/month | 21.2/B cứu nạn/deep | 14.8; 17.4; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.small.treasury | 3.0 | treasury_script_unit | 21.2/E công nghệ/small | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.small.days | 180.0 | day | 21.2/E công nghệ/small | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.small.monthly | 0.03 | treasury_script_unit/month | 21.2/E công nghệ/small | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.deep.treasury | 6.0 | treasury_script_unit | 21.2/E công nghệ/deep | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.deep.days | 365.0 | day | 21.2/E công nghệ/deep | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.E.deep.monthly | 0.06 | treasury_script_unit/month | 21.2/E công nghệ/deep | 14.8; 17.5; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.small.treasury | 2.0 | treasury_script_unit | 21.2/S kỹ thuật/small | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.small.days | 180.0 | day | 21.2/S kỹ thuật/small | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.small.monthly | 0.02 | treasury_script_unit/month | 21.2/S kỹ thuật/small | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.deep.treasury | 4.0 | treasury_script_unit | 21.2/S kỹ thuật/deep | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.deep.days | 365.0 | day | 21.2/S kỹ thuật/deep | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.S.deep.monthly | 0.04 | treasury_script_unit/month | 21.2/S kỹ thuật/deep | 14.8; 17.6; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.small.treasury | 2.0 | treasury_script_unit | 21.2/W tiêu chuẩn/small | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.small.days | 180.0 | day | 21.2/W tiêu chuẩn/small | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.small.monthly | 0.02 | treasury_script_unit/month | 21.2/W tiêu chuẩn/small | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.deep.treasury | 5.0 | treasury_script_unit | 21.2/W tiêu chuẩn/deep | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.deep.days | 365.0 | day | 21.2/W tiêu chuẩn/deep | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| package.W.deep.monthly | 0.05 | treasury_script_unit/month | 21.2/W tiêu chuẩn/deep | 14.8; 17.7; 18.4; 20.3; 21.1; 21.2; 24.2 |
| reward.C.trade_targeted.small | 0.05 | targeted_trade_opinion | 20.2/C thương mại/small | 14.2; 17.1; 20.1; 20.2 |
| reward.C.trade_targeted.deep | 0.1 | targeted_trade_opinion | 20.2/C thương mại/deep | 14.2; 17.1; 20.1; 20.2 |
| reward.M.trade_targeted.small | 0.05 | targeted_trade_opinion | 20.2/M kết nối/small | 17.2; 20.1; 20.2 |
| reward.M.trade_targeted.deep | 0.08 | targeted_trade_opinion | 20.2/M kết nối/deep | 17.2; 20.1; 20.2 |
| reward.A.trade_national.small | 0.02 | national_trade_opinion | 20.2/A sáng kiến/small | 17.3; 20.1; 20.2 |
| reward.A.trade_national.deep | 0.03 | national_trade_opinion | 20.2/A sáng kiến/deep | 17.3; 20.1; 20.2 |
| reward.E.research_bonus_percent.small | 10.0 | percent | 20.2/E công nghệ/small | 17.5; 20.2; 22.3 |
| reward.E.research_bonus_percent.deep | 15.0 | percent | 20.2/E công nghệ/deep | 17.5; 20.2; 22.3 |
| reward.E.research_bonus_percent.uses | 1.0 | count | 20.2/E công nghệ/uses | 17.5; 20.2; 22.3 |
| reward.EW.research_speed.small | 0.005 | research_speed_factor | 20.2/E/W đào tạo/small | 17.5; 17.7; 20.1; 20.2 |
| reward.EW.research_speed.deep | 0.01 | research_speed_factor | 20.2/E/W đào tạo/deep | 17.5; 17.7; 20.1; 20.2 |
| reward.S.research_bonus_percent.small | 10.0 | percent | 20.2/S hỗ trợ/small | 17.6; 20.2; 22.3 |
| reward.S.research_bonus_percent.deep | 15.0 | percent | 20.2/S hỗ trợ/deep | 17.6; 20.2; 22.3 |
| reward.S.research_bonus_percent.uses | 1.0 | count | 20.2/S hỗ trợ/uses | 17.6; 20.2; 22.3 |
| reward.W.trade_targeted.small | 0.05 | targeted_trade_opinion | 20.2/W thị trường/small | 17.7; 20.1; 20.2 |
| reward.W.trade_targeted.deep | 0.08 | targeted_trade_opinion | 20.2/W thị trường/deep | 17.7; 20.1; 20.2 |
| reward.C.issue_pp_factor.small | -0.02 | political_power_factor | 20.2/Vướng mắc C/small | 14.6; 14.7; 17.1; 20.2 |
| reward.C.issue_pp_factor.deep | -0.03 | political_power_factor | 20.2/Vướng mắc C/deep | 14.6; 14.7; 17.1; 20.2 |
| reward.C.contingency_pp_factor.small | -0.01 | political_power_factor | 20.2/Dự phòng C/small | 14.7; 17.1; 20.2 |
| reward.C.contingency_pp_factor.deep | -0.015 | political_power_factor | 20.2/Dự phòng C/deep | 14.7; 17.1; 20.2 |
| reward.R1.maintain_cost_factor | -0.05 | improve_relations_maintain_cost_factor | 20.2/R1 | 16; 20.2; 22.3 |
| reward.EW.duration | 730.0 | day | 20.2/EW/lifetime | 20.2; 22.3 |
| cap.research | 0.03 | research_speed_factor | 20.2/caps | 20.1; 20.2; 24.2 |
| cap.trade_national | 0.05 | trade_opinion_factor | 20.2/caps | 20.1; 20.2; 24.2 |
| cap.maintain_reduction | 0.1 | reduction_magnitude | 20.2/caps | 20.1; 20.2; 24.2 |
| cap.trade_targeted | 0.1 | targeted_trade_opinion | 20.2/caps | 20.1; 20.2; 24.2 |
| roster.A.wide_quorum | 3 | country | 17.3/quorum | 17.3; 21.2; 22.3; 24.2 |
| roster.A.deep_quorum | 2 | country | 17.3/quorum | 17.3; 21.2; 22.3; 24.2 |
| roster.A.invited | 5 | country | 17.3/quorum | 17.3; 21.2; 22.3; 24.2 |
| roster.M.quorum | 2 | country | 17.2/quorum | 17.2; 21.2; 22.3; 24.2 |
| roster.M.bilateral_quorum | 1 | country | 17.2/bilateral fallback | 17.2; 22.3 |
| implementation_slots | 2 | program | 18.2/slots | 18.2; 18.4; 19.2; 21.2; 21.3; 24.2 |
| network.min_regions | 3 | region | 22.3/R1 | 16; 22.3; 24.2 |
| network.recognition_days | 730 | day | 22.3/recognition | 20.2; 22.3; 24.2 |
| ai.base_weight.accept | 4.0 | relative_weight | 21.3/weights | 13.6; 14.4; 21.3; 24.2 |
| ai.base_weight.amend | 3.0 | relative_weight | 21.3/weights | 13.6; 14.4; 21.3; 24.2 |
| ai.base_weight.refuse | 2.0 | relative_weight | 21.3/weights | 13.6; 14.4; 21.3; 24.2 |
| politics.cohesion_price_bands | [[0, 19, 1.25], [20, 39, 1.15], [40, 54, 1.05], [55, 69, 1], [70, 100, 0.9]] | [cohesion lower, cohesion upper, PP multiplier] | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cohesion_price_bands.value | B1; L1 rejected fee reader; L1 calculations |
| politics.sign_days | [45, 30, 25, 21] | day, indexed by cadre tier | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.sign_days.value | 6; 19.3; 19.4; L1.T migration pending |
| politics.prepare_days | {"collective": 30, "balanced": 30, "central": 15} | day, indexed by BoP zone | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.prepare_days.value | 6; 16; 19.2; 19.3; 19.4; 21.3; 24.2; L1.P |
| politics.combined | {"pp": 60, "cohesion": -6, "bop": 0.1, "sign_days": 21, "departure_cohesion": -4, "departure_days": 30} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.combined.value | 19.4; L1.T migration pending; L2 not started |
| politics.split | {"pp": 45, "cohesion": 2, "bop": -0.1, "after_days": 180} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.split.value | B1; L1 (pending); L2 (not started) |
| politics.bop_threshold | 0.25 | BoP | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.bop_threshold.value | B1; L1 (pending); L2 (not started) |
| politics.bop_limits | [-1, 1] | BoP | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.bop_limits.value | B1; L1 (pending); L2 (not started) |
| politics.cohesion_initial | 60 | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cohesion_initial.value | B1; L1 (pending); L2 (not started) |
| politics.cohesion_limits | [0, 100] | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cohesion_limits.value | B1; L1 (pending); L2 (not started) |
| politics.collective_full_extra | 4 | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.collective_full_extra.value | B1; L1 (pending); L2 (not started) |
| politics.collective_extra_cap | 70 | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.collective_extra_cap.value | B1; L1 (pending); L2 (not started) |
| politics.outcome_cohesion | {"full": 6, "partial": 2, "fail": -6} | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.outcome_cohesion.value | B1; L1 (pending); L2 (not started) |
| politics.cadre_cohesion_required | 55 | cohesion | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cadre_cohesion_required.value | 14.2; 14.3; 14.8; 16; 17.5; 19.2; 19.4; 21.2; 21.3; 24.2; L1.C selected |
| politics.tier_cap | 3 | tier | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.tier_cap.value | B1; L1 (pending); L2 (not started) |
| politics.cadre_discount_pp | [0, 5, 10, 15] | PP, indexed by tier | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cadre_discount_pp.value | B1; L1 (pending); L2 (not started) |
| politics.low_cohesion_prepare_extra | 60 | day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.low_cohesion_prepare_extra.value | B1; L1 (pending); L2 (not started) |
| politics.recovery | {"pp": 30, "low_pp": 15, "low_below": 20, "cohesion": 10, "days": 90, "cooldown": 180} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.recovery.value | B1; L1 gate candidate calculations |
| politics.congress_dates | {"IX": "2001-04-19", "X": "2006-04-18", "XI": "2011-01-12", "XII": "2016-01-20", "XIII": "2021-01-25", "XIV": "2026-01-19", "XV": "2031-01-19"} | date from source; no new historical claim | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.congress_dates.value | 1; 15.1; 16; 19.4; 21.3; 24.2; 24.3; L1.gates |
| politics.e104 | {"caller_day": 500, "window_days": 30, "A_pp": 30, "A_grant": 0.75, "B_pp": 15, "B_grant": 0.25, "B_days": 21, "C_pp": 0} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.e104.value | B1; L1 (pending); L2 (not started) |
| politics.late_signature_windows | {"XIII09": 25, "XIV11": 21} | day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.late_signature_windows.value | B1; L1 (pending); L2 (not started) |
| politics.contract_obligations | {"check_days": [90, 180], "pp_per_check": 10, "missed_cohesion": 6, "relative_to": "E104 signature or XIII12 amendment", "requires_completed_evidence": true, "settlement": "pay remaining support only after both checks; missed check terminates future duties, forfeits unpaid support/unused training access, never claws back paid history"} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.contract_obligations.value | B1; L1 (pending); L2 (not started) |
| politics.e104_training | {"days": 90, "reward_pp": 25, "requires": ["E102-A", "accepted E104", "both contract checks", "completed training evidence"], "guard": "one object/source epoch; refund only after actual training, cancellation or missed check revokes unused access"} | mixed fields; keys name units, see political source | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.e104_training.value | B1; L1 (pending); L2 (not started) |
| politics.k_values | [20, 40, 60] | PP/treasury script unit, sensitivity only | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.k_values.value | B1; L1 (pending); L2 (not started) |
| politics.r_values | [0.5, 1, 1.5] | PP/day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.r_values.value | B1; L1 (pending); L2 (not started) |
| politics.cohesion_pp_rate | 3 | PP/cohesion, accounting only | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.cohesion_pp_rate.value | B1; L1 (pending); L2 (not started) |
| politics.accounting_days | 1800 | day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.accounting_days.value | B1; L1 (pending); L2 (not started) |
| politics.branch_pp_daily | 0.03 | PP/day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.branch_pp_daily.value | B1; L1 (pending); L2 (not started) |
| politics.focus_days_per_cost | 7 | day/focus_cost, paper assumption | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.focus_days_per_cost.value | B1; L1 (pending); L2 (not started) |
| politics.tools | {"start": [40, 0], "training": [25, 0.25], "succession": [30, 0], "administration_project": [40, 0.5], "audit": [30, 0.25], "local_project": [30, 0.5], "audit_standard": [25, 0.25], "review": [25, 0]} | [PP, treasury script unit] | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.tools.value | B1; L1 (pending); L2 (not started) |
| politics.action_days | {"training": [180, 150], "succession": [180, 150], "administration_project": [270, 225], "audit": [270, 225], "local_project": [270, 225], "audit_standard": [90, 90], "review": [90, 90]} | [standard days, fast days] | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.action_days.value | B1; L1 (pending); L2 (not started) |
| reward.C.issue_max_days | 90.0 | day | 20.2/Vướng mắc C/lifetime | 14.6; 14.7; 20.2; 21.1; 24.2 |
| focus.cost_values | [5, 7] | focus_cost | 16/catalog costs | 16; 22.1; 24.1 |
| politics.override_cohesion | 8 | cohesion lost per override | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.override_cohesion.value | 19.4; 24.2; L1.C override test |
| politics.program_start_latest | 270 | day | VIETNAM_POLITICAL_PARAMETERS_VI.json:parameters.program_start_latest.value | L1.R0 no inherited deadline |

## Số dẫn xuất

- Đúng một chương trình/cụm: phí tháng nhỏ=0.15; sâu=0.32. Đây không là tổng tối đa của hệ thống.
- CSV costs: PP gửi + treasury triển khai × k; phí tháng riêng, chưa chọn horizon duy trì.
- pp_days_to_fund = chi quy đổi / r là thời gian gom nguồn lực giả định, không phải hoàn vốn.
- Không cộng branch_pp_daily chính trị vào r lần nữa khi chưa chốt baseline thu PP ngoại giao.
- CSV reader_probes lưu phép tính reader phí đã bị rút, không áp theo cohesion. Gate sâu C/E đã chọn; các bảng band/override được sinh riêng.

| Bất biến | PASS/FAIL | Bằng chứng / giới hạn |
|---|---|---|
| J1 | PASS | Ba giao diện thiết kế G/P/C có writer, consumer, hiệu ứng và tooltip; root OR nguồn thật=True/True; 9 mục C/E đọc gate. Không có script game ngoại giao mới; T tier/kiêm nhiệm hoãn, không tính active. |
| J2 | FAIL | G có 16 ca đối chứng đường mặc định/bỏ F02; C: 60−8=52<55, phục hồi 30PP mở lại. P chỉ đổi chuẩn bị 15 ngày, chưa chứng minh đổi lựa chọn. Người dùng chọn giữ lịch, J2 FAIL và L1 mở; không đổi định nghĩa. |
| J3 | PASS | Đọc JSON trực tiếp; bảng ký/bands khớp tài liệu=True/True; drift=[]; nguồn đổi=[]. |
| J4 | PASS | 7/7 cụm có đúng kỳ và nhãn giả định gameplay; R0 IX+(F02 OR mặc định)=True. B1=X, S1=XIII với phạm vi tách XIII05–08; không coi là năm hình thành quan hệ. |
| J5 | FAIL | NỢ ĐÃ BIẾT: ownership biển/S-vs-XIII05–08/W-vs-X05–X08/hợp đồng ghi ngay trong plan 19.5. E104 chỉ có kế hoạch chuyển riêng19.6, sau C qua kiểm; chưa chuyển/kiểm thật nên J5 giữ FAIL. |
| D1 | FAIL | Chưa chứng minh mọi chương trình: C sâu có trade opinion cao hơn; quyền sâu E/S chưa có consumer đo được. |
| D2 | FAIL | Chưa có ngưỡng hoàn vốn người dùng chọn; trade opinion/research chưa định giá; gom PP không là hoàn vốn. |
| D3 | FAIL | Đúng một chương trình/cụm: phí tháng nhỏ=0.15, sâu=0.32; không có thu treasury. r là PP/ngày; M/E/W có thể nhiều chương trình. |
| D4 | FAIL | Research: 3×0.01=0.03 chạm trần nếu đủ 3 nguồn. R1 duy nhất 0.05 < trần 0.1; chưa có nguồn thứ hai. |
| D5 | FAIL | Category/điều kiện/consumer riêng JAP/KOR và USA/SOV/RAJ chưa đủ; không so bằng tên lĩnh vực. |
| D6 | FAIL | Đã nhập k và công cụ chính trị; chưa có mô hình đủ phản hồi/hủy/vướng mắc hoặc lợi ích định giá. |
| D7 | PASS | Đơn vị treasury trong tài liệu/JSON chính trị: chưa xác định; k chỉ là sensitivity, không là tỷ giá engine. |
| D8 | FAIL | Chưa định nghĩa đủ chiều có tác dụng; không dùng tên cờ cơ hội để tạo PASS. |
| N1 | FAIL | M/A/B/E/S/W chưa đủ bảy thành phần; dành L3, chưa viết lại. |
| N2 | FAIL | Chưa có event mới để thử lựa chọn rẻ nhất. |
| N3 | FAIL | Quyền hợp tác sâu E/S chưa có consumer chốt; không tính vào so thống trị. |
| N4 | FAIL | Chưa rà nguồn toàn tài liệu; không thêm mốc/nhân vật; các gate ứng viên ghi giả định gameplay. |
| H1 | PASS | catalog/layout/SVG=[51, 51, 51]; 49+2=51; edges=74; errors=[] |
| H2 | FAIL | Mâu thuẫn cũ:14.3 A04 sau A02+A03,17.1 từ C4;14.6 chưa chọn duy trì,20.3 có phí tháng;11/14 còn nói chưa có số trong khi21 có bộ thử. Chờ L4. |
| H3 | PASS | 50 anchor trước node/cha trực tiếp; relative=node-anchor; 74 cạnh con thấp hơn cha; min gap=4>=2; errors=[]. |
| H4 | PASS | Chỉ Python/XML/CSV; chưa chạy HOI4, chưa playtest hay xác nhận cân bằng. |

FAIL bao gồm yêu cầu chưa hoàn thành/chưa đủ bằng chứng; không đồng nghĩa vừa sinh lỗi gameplay.
Các mục D/N thuộc L2/L3 giữ FAIL, không đổi định nghĩa để PASS.

## Tái tạo

Chạy: python -X utf8 VIE_REGIONAL_DIPLOMACY_REVIEW_VI.py
Exit 1 khi còn bất biến FAIL; đọc diagnostics. Không chạy balance chính trị để ghi lại CSV.
B1 chưa thay mô hình đủ kịch bản L2; trade opinion/research/cơ hội chưa được quy tùy ý ra PP.
