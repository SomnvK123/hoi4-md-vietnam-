# Lượt 1: kết quả tính script và điểm cần chốt

Đã áp dụng hai quyết định người dùng:0.25ngân khố/checkpoint thương lượng và ngoại lệ full E102-C+E103-B/C. Giữ55PP/50PP, deadline900, mọi giá khác. Dừng trước lượt2; I3 còn vướng E103-B/C trong ngoại lệ, không sửa thêm giá.

## B1: bảng tham số duy nhất

Nguồn có thể chạy lại: `VIETNAM_POLITICAL_PARAMETERS_VI.json`. Script đọc nguồn này, không đọc số trong văn xuôi làm đầu vào. Bảng ghi đủ giá đã xác định; giá còn thiếu trong 40 node một dòng là CHƯA XÁC ĐỊNH, cần lượt 2. Các source_row của node là chụp đầu vào để kiểm scope, không là nguồn thay thế tham số chung.

| Tham số | Giá trị | Cũ | Mục sử dụng |
| --- | --- | --- | --- |
| program_deadline | 900 | Giữ / bổ sung theo yêu cầu | Kết luận;4.2;6.5;7.3;8.3;10;11;12 |
| early_days | {"cadre": 600, "administration": 600, "inspection": 690, "social": 600} | 660 cho mọi chương trình | Kết luận;4.2;6.5;7.3;8.3;10;11;12 |
| early_pp | 50 | 60 | 4.2;8.3;10;11;12 |
| program_start_latest | 270 | Giữ / bổ sung theo yêu cầu | 4.2;11 |
| program_selection_days | 90 | Giữ / bổ sung theo yêu cầu | 4.2 |
| reserve_days | 100 | Giữ / bổ sung theo yêu cầu | 4.2;6.5;11.3;I5 |
| congress_preparation_days | 180 | Giữ / bổ sung theo yêu cầu | 5.1;4.2;11 |
| congress_session_days | 7 | Giữ / bổ sung theo yêu cầu | 5.1 |
| appointment_days | 30 | Giữ / bổ sung theo yêu cầu | 5.1 |
| congress_dates | {"IX": "2001-04-19", "X": "2006-04-18", "XI": "2011-01-12", "XII": "2016-01-20", "XIII": "2021-01-25", "XIV": "2026-01-19", "XV": "2031-01-19"} | Giữ / bổ sung theo yêu cầu | 5.1;7;11; XV là giả định gameplay, các nguồn giữ ở 5.1 |
| prepare_days | {"collective": 30, "balanced": 30, "central": 15} | Giữ / bổ sung theo yêu cầu | 3.1;4.3;11 |
| action_days | {"training": [180, 150], "succession": [180, 150], "administration_project": [270, 225], "audit": [270, 225], "local_project": [270, 225], "audit_standard": [90, 90], "review": [90, 90]} | Giữ / bổ sung theo yêu cầu | 3.2;4.1;4.3;6.5;11 |
| tools | {"start": [40, 0], "training": [25, 0.25], "succession": [30, 0], "administration_project": [40, 0.5], "audit": [30, 0.25], "local_project": [30, 0.5], "audit_standard": [25, 0.25], "review": [25, 0]} | Giữ / bổ sung theo yêu cầu | 4.3;11; mỗi cặp là [PP,ngân khố] |
| bop_initial | 0 | Giữ / bổ sung theo yêu cầu | 3.1 |
| bop_limits | [-1, 1] | Giữ / bổ sung theo yêu cầu | 3.1 |
| bop_threshold | 0.25 | Giữ / bổ sung theo yêu cầu | 3.1;5.2;10;11.3 |
| bop_route_snapshot | {"collective": -0.3, "balanced": 0, "central": 0.3} | Giữ / bổ sung theo yêu cầu | 3.1;6.2;11; CSV dùng snapshot chuẩn hóa, không mô phỏng focus trước snapshot |
| branch_pp_daily | 0.03 | Giữ / bổ sung theo yêu cầu | 3.1;11 |
| consult_bop | -0.05 | Giữ / bổ sung theo yêu cầu | 3.1;3.2;10;11 |
| override_bop | 0.05 | Giữ / bổ sung theo yêu cầu | 3.1;3.2;10;11 |
| checkpoint_count | 2 | Giữ / bổ sung theo yêu cầu | 3.1;3.2;11 |
| fast_upfront_pp | 25 | Giữ / bổ sung theo yêu cầu | 3.2;4.3;11 |
| checkpoint_treasury | 0.25 | 0 | 3.2;4.2;4.3;6;10;11.1;11.3;CSV;I2;I3; được người dùng chốt, mỗi checkpoint thương lượng |
| choice_full_exception | {"program": "inspection", "e102": "C", "e103": ["B", "C"]} | Giữ / bổ sung theo yêu cầu | 4.2;6.4;6.5;10;11.1;11.3;12;I5; chỉ miễn dự phòng cho tổ hợp người chơi đã chọn, không đổi deadline/giá |
| checkpoint_pp | 15 | Giữ / bổ sung theo yêu cầu | 3.2;4.3;11;I3 |
| override_cohesion | 8 | Giữ / bổ sung theo yêu cầu | 3.1;3.2;10;11 |
| override_floor | 40 | Giữ / bổ sung theo yêu cầu | 3.2;3.3;10;11.3 |
| cohesion_initial | 60 | Giữ / bổ sung theo yêu cầu | 3.3;11 |
| cohesion_limits | [0, 100] | Giữ / bổ sung theo yêu cầu | 3.3 |
| cohesion_price_bands | [[0, 19, 1.25], [20, 39, 1.15], [40, 54, 1.05], [55, 69, 1], [70, 100, 0.9]] | 40–69:1.00 | 3.3;4.3;10;11 |
| low_cohesion_prepare_extra | 60 | Giữ / bổ sung theo yêu cầu | 3.3;11 |
| cadre_cohesion_required | 55 | Giữ / bổ sung theo yêu cầu | 4.1;5.2;11 |
| recovery | {"pp": 30, "low_pp": 15, "low_below": 20, "cohesion": 10, "days": 90, "cooldown": 180} | Giữ / bổ sung theo yêu cầu | 3.3;11 |
| outcome_cohesion | {"full": 6, "partial": 2, "fail": -6} | Giữ / bổ sung theo yêu cầu | 3.3;4.2;11 |
| collective_full_extra | 4 | Giữ / bổ sung theo yêu cầu | 3.1;3.3;11 |
| collective_extra_cap | 70 | Giữ / bổ sung theo yêu cầu | 3.1;3.3;11 |
| tier_cap | 3 | Giữ / bổ sung theo yêu cầu | 4.2;4.4;8.1;11 |
| cadre_discount_pp | [0, 5, 10, 15] | Giữ / bổ sung theo yêu cầu | 3.3;4.4;11 |
| cadre_transition_cohesion | [12, 8, 5, 3] | Giữ / bổ sung theo yêu cầu | 4.4;11 |
| cadre_transition_days | [90, 75, 60, 45] | Giữ / bổ sung theo yêu cầu | 4.4 |
| transition_pp_factor | -0.05 | Giữ / bổ sung theo yêu cầu | 4.4 |
| sign_days | [45, 30, 25, 21] | [45, 35, 30, 21] | 4.4;5.2;6.6;7.XIII09;7.XIV11;10;11 |
| combined | {"pp": 60, "cohesion": -6, "bop": 0.1, "sign_days": 21, "departure_cohesion": -4, "departure_days": 30} | Giữ / bổ sung theo yêu cầu | 3.1;4.4;5.2;6.6;11 |
| split | {"pp": 45, "cohesion": 2, "bop": -0.1, "after_days": 180} | Giữ / bổ sung theo yêu cầu | 3.1;5.2 |
| tier_modifiers | {"bureaucracy": [-0.02, -0.04, -0.06], "corruption_cost": [-0.02, -0.04, -0.06], "stability": [0.01, 0.02, 0.03]} | Giữ / bổ sung theo yêu cầu | 4.4;8.3 |
| gdp_target_factor | 1.04 | Giữ / bổ sung theo yêu cầu | 4.1 |
| bottom_corruption_helper_pp | 150 | Giữ / bổ sung theo yêu cầu | 4.1; tham chiếu repo giữ nguyên, không gọi helper tại đáy |
| timed_reward_days | 365 | Giữ / bổ sung theo yêu cầu | 4.2;6.4;7.XIV10;11 |
| fail_penalty | [-0.03, 180] | Giữ / bổ sung theo yêu cầu | 4.2 |
| side_project | {"pp": 30, "treasury": 0, "days": 270, "bureaucracy_cost_factor": -0.01} | Giữ / bổ sung theo yêu cầu | 4.2;8.1;8.3;10;11; giả định gameplay mới L1.2, deadline là chuẩn bị đại hội sau |
| e101 | {"A": [25, 0.5, 2, -0.05, 60], "B": [0, 0, -8, 0.05, 0], "C": [15, 0.25, 1, 0, 0]} | Giữ / bổ sung theo yêu cầu | 6.3;11; [PP,ngân khố,cohesion,BoP,trễ ngày] |
| e102 | {"A": [30, 0.5, 0], "B": [20, 0.25, 0], "C": [0, 0.75, 90]} | Giữ / bổ sung theo yêu cầu | 6.4;6.5;11; [PP,ngân khố,trễ ngày] |
| e103 | {"caller_day": 450, "A_pp": 0, "rejection_cohesion": -6, "reappraisal_days": 180, "B_pp": 30, "extension_days": 120, "C_pp": 15} | Giữ / bổ sung theo yêu cầu | 6.5;8.3;10;11; B giữ độ gia hạn cũ 780−660=120 |
| e104 | {"caller_day": 500, "window_days": 30, "A_pp": 30, "A_grant": 0.75, "B_pp": 15, "B_grant": 0.25, "B_days": 21, "C_pp": 0} | Giữ / bổ sung theo yêu cầu | 6.6;10;11 |
| late_signature_windows | {"XIII09": 25, "XIV11": 21} | Giữ / bổ sung theo yêu cầu | 7.XIII09;7.XIV11;10;11.3; giả định gameplay L1.5 |
| focus_days_per_cost | 7 | Giữ / bổ sung theo yêu cầu | 6.2;7.3;7.4; giả định chưa đo engine |
| focus_pp | {"F01": 30, "F02": -25, "F03": 0, "F04": -25, "F07": 20} | Giữ / bổ sung theo yêu cầu | 6.2;11; trước snapshot nên tách khỏi CSV chuẩn hóa |
| focus_f03_cohesion | 4 | Giữ / bổ sung theo yêu cầu | 6.2 |
| one_stop_legacy_factor | -0.02 | Giữ / bổ sung theo yêu cầu | 6.2;8.3 |
| accounting_days | 1800 | Giữ / bổ sung theo yêu cầu | 11 |
| r_values | [0.5, 1, 1.5] | Giữ / bổ sung theo yêu cầu | 11; CSV |
| k_values | [20, 40, 60] | Giữ / bổ sung theo yêu cầu | 11; CSV;I3 |
| cohesion_pp_rate | 3 | Giữ / bổ sung theo yêu cầu | 11; CSV;I3 |
| max_fast_reward_pp_difference | 10 | Giữ / bổ sung theo yêu cầu | I2;11.3 |
| focus_nodes | 74 node: cost và hàng nguồn được lưu trong JSON | Giữ / bổ sung theo yêu cầu | 6.2;7.4; toàn bộ cost và giá đã ghi trong các node; giá chưa ghi được đánh dấu ở báo cáo B1 |

## Bảng bất biến I1–I10

| Bất biến | Kết quả | Phép tính / giới hạn |
| --- | --- | --- |
| I1 | PASS | Cán bộ: 660/645 > 600 >= 555; Công vụ: 660/645 > 600 >= 555; Kiểm tra: 750/735 > 690 >= 645; Dân vận: 660/645 > 600 >= 555 |
| I2 | PASS (PP thuần) | 55−50=5 PP; cộng ngân khố, chênh quy đổi [15.0, 25.0, 35.0] ở k=[20, 40, 60]. Giá trị còn lại: dự án phụ L1.2. |
| I3 | FAIL (E103 trong ngoại lệ) | Checkpoint PASS: thương lượng [20.0, 25.0, 30.0] so với vượt 24; k=40 biên1PP. Trong E102-C, E103-C rẻ hơn B 15 PP mọi k, cùng lịch/full/cohesion/cơ hội mô hình. Không tự chỉnh giá. |
| I4 | PASS (vùng) | BoP: thưởng nghiệm thu / chuẩn / công cụ cấp tốc; cohesion: 1.25/1.15/1.05/1.00/0.90; cổng sau trừ >=40 |
| I5 | PASS (snapshot); FAIL ngoài snapshot | Cohesion60: chuẩn750/cấp tốc645 <=900−100=800; ngoại lệ C+B/C đủ điều kiện bảng riêng, không thưởng sớm; lịch cách tối thiểu380 ngày. Cohesion<20: chuẩn kiểm tra810, chỉ còn90 ngày, chưa có ngoại lệ được phép. |
| I6 | FAIL (chưa đạt lượt 2) | Đếm 74=2+6×12; giữ cost. 40 node còn thiếu caller/lựa chọn đầy đủ; chưa tự điền. |
| I7 | FAIL (chưa audit lượt 3) | Guard dự án phụ đã ghi 8.1; registry cũ chưa định danh đầy đủ mission/idea/milestone. |
| I8 | FAIL (chưa xác minh lượt 2) | Nguồn lịch 5.1 giữ nguyên; trái phiếu XI và tiền đề Biển Đông cần tra nguồn ở lượt 2. |
| I9 | PASS | Chỉ tính script; không chạy engine/console/playtest. |
| I10 | PASS (ma trận hữu hạn) | Kiểm PP ròng và quy đổi ở mọi k/r; số tổ hợp thống trị toàn bộ/theo tuyến: 0. Trong cặp ngoại lệ C+B/C, E103-C trội B trong các chỉ số đã mô hình hóa; báo riêng, không sửa giá. |

## Ngày full cơ sở

| Chương trình | Chuẩn tập thể/cân bằng | Chuẩn tập trung | Mốc sớm | Cấp tốc hợp lệ |
| --- | --- | --- | --- | --- |
| Cán bộ | 660 | 645 | 600 | 555 |
| Công vụ | 660 | 645 | 600 | 555 |
| Kiểm tra | 750 | 735 | 690 | 645 |
| Dân vận | 660 | 645 | 600 | 555 |

## Giá khởi động tại mọi biên cohesion/tier

Làm tròn lên bằng Decimal; kiểm đủ vùng0–100, không chồng biên. Kiêm nhiệm ngay sau ký mode/giá không tính lại giá đã ký.

| Vùng | Hệ số | Tier0 | Tier1 | Tier2 | Tier3 |
| --- | --- | --- | --- | --- | --- |
| 0–19 | 1.25 | 50 | 44 | 38 | 32 |
| 20–39 | 1.15 | 46 | 41 | 35 | 29 |
| 40–54 | 1.05 | 42 | 37 | 32 | 27 |
| 55–69 | 1 | 40 | 35 | 30 | 25 |
| 70–100 | 0.9 | 36 | 32 | 27 | 23 |

## Khoảng cách bắt đầu muộn nhất tới chuẩn bị đại hội sau

Công thức: chênh ngày hai đại hội − chuẩn bị 180 − khởi động muộn 270 − deadline 900.

| Nhiệm kỳ | Ngày còn cách chuẩn bị kỳ sau |
| --- | --- |
| IX | 475 |
| X | 380 |
| XI | 484 |
| XII | 482 |
| XIII | 470 |
| XIV | 476 |

## E102 × E103: chuỗi và ngoại lệ do lựa chọn

T là ngày chứng cứ sẵn sàng. E103-A bị bác: full tiềm năng=max(T,690)+180, chạy tuần tự. Nếu quá 900 thì chốt partial; lựa chọn B hoặc C ngay tại E103 giữ đường full theo T. T nằm 801–900 cũng là ngoại lệ dự phòng có cảnh báo, không phải đường mặc định. B sau 810 trượt hợp đồng nhưng programme vẫn được xét đủ chứng cứ trước 900. C chốt hợp đồng partial, tiếp tục hồ sơ để full programme; không nhận thưởng sớm. Không có fail bất ngờ trong các tổ hợp này. Thời gian chứng cứ dưới đây giả định kiến nghị đã xử lý; chưa xử lý thì tooltip nêu nhóm mục tiêu còn thiếu.

| Tuyến | Mode | E102 | E103 | Full tiềm năng | Kết quả | Hợp đồng | Dự phòng |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | E102-A | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-A | E103-B | 750 | full | extended | Trong dự phòng |
| collective | standard | E102-A | E103-C | 750 | full | partial | Trong dự phòng |
| collective | standard | E102-B | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-B | E103-B | 750 | full | extended | Trong dự phòng |
| collective | standard | E102-B | E103-C | 750 | full | partial | Trong dự phòng |
| collective | standard | E102-C | E103-A | 1020 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| collective | standard | E102-C | E103-B | 840 | full | extension_missed | Ngoại lệ lựa chọn |
| collective | standard | E102-C | E103-C | 840 | full | partial | Ngoại lệ lựa chọn |
| balanced | standard | E102-A | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| balanced | standard | E102-A | E103-B | 750 | full | extended | Trong dự phòng |
| balanced | standard | E102-A | E103-C | 750 | full | partial | Trong dự phòng |
| balanced | standard | E102-B | E103-A | 930 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| balanced | standard | E102-B | E103-B | 750 | full | extended | Trong dự phòng |
| balanced | standard | E102-B | E103-C | 750 | full | partial | Trong dự phòng |
| balanced | standard | E102-C | E103-A | 1020 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| balanced | standard | E102-C | E103-B | 840 | full | extension_missed | Ngoại lệ lựa chọn |
| balanced | standard | E102-C | E103-C | 840 | full | partial | Ngoại lệ lựa chọn |
| central | standard | E102-A | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-A | E103-B | 735 | full | extended | Trong dự phòng |
| central | standard | E102-A | E103-C | 735 | full | partial | Trong dự phòng |
| central | standard | E102-B | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-B | E103-B | 735 | full | extended | Trong dự phòng |
| central | standard | E102-B | E103-C | 735 | full | partial | Trong dự phòng |
| central | standard | E102-C | E103-A | 1005 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | standard | E102-C | E103-B | 825 | full | extension_missed | Ngoại lệ lựa chọn |
| central | standard | E102-C | E103-C | 825 | full | partial | Ngoại lệ lựa chọn |
| central | fast_paid | E102-A | E103-A | 645 | full | accepted | Trong dự phòng |
| central | fast_paid | E102-A | E103-B | 645 | full | extended | Trong dự phòng |
| central | fast_paid | E102-A | E103-C | 645 | full | partial | Trong dự phòng |
| central | fast_paid | E102-B | E103-A | 645 | full | accepted | Trong dự phòng |
| central | fast_paid | E102-B | E103-B | 645 | full | extended | Trong dự phòng |
| central | fast_paid | E102-B | E103-C | 645 | full | partial | Trong dự phòng |
| central | fast_paid | E102-C | E103-A | 915 | partial ở 900 | rejected | Ngoại lệ lựa chọn |
| central | fast_paid | E102-C | E103-B | 735 | full | extended | Trong dự phòng |
| central | fast_paid | E102-C | E103-C | 735 | full | partial | Trong dự phòng |

## Ngoại lệ full được người dùng chốt

Chỉ E102-C cùng E103-B hoặc C; không là đường mặc định. Miễn yêu cầu dự phòng100ngày nếu nằm trong bảng; deadline900 giữ nguyên. Không nhận thưởng PP sớm hoặc dự án phụ. Các hàng có dự phòng>=100 vẫn được liệt kê vì full sau mốc sớm. Tooltip trước khi chọn ghi ngày full, dự phòng còn X ngày, chậm thêm quá dự phòng sẽ rơi xuống partial. Không có cơ chế bù.

| Tuyến | Mode | E102 | E103 | Ngày full | Dự phòng còn | Thưởng PP sớm | Kết quả |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | C | B | 840 | 60 | 0 | full |
| collective | standard | C | C | 840 | 60 | 0 | full |
| balanced | standard | C | B | 840 | 60 | 0 | full |
| balanced | standard | C | C | 840 | 60 | 0 | full |
| central | standard | C | B | 825 | 75 | 0 | full |
| central | standard | C | C | 825 | 75 | 0 | full |
| central | fast_paid | C | B | 735 | 165 | 0 | full |
| central | fast_paid | C | C | 735 | 165 | 0 | full |
| central | fast_override | C | B | 735 | 165 | 0 | full |
| central | fast_override | C | C | 735 | 165 | 0 | full |
| central | combined_fast_paid | C | B | 735 | 165 | 0 | full |
| central | combined_fast_paid | C | C | 735 | 165 | 0 | full |

## Mọi tổ hợp full sau mốc sớm

Các lựa chọn chuẩn A/B+B/C đủ dự phòng là đường cơ sở, tách khỏi ngoại lệ C+B/C. Mọi mode hợp lệ có trong bảng, k/r không đổi timer nên không lặp hàng theo chúng.

| Tuyến | Mode | E102 | E103 | Ngày full | Dự phòng còn | Thưởng PP sớm | Phân loại |
| --- | --- | --- | --- | --- | --- | --- | --- |
| collective | standard | A | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | A | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | B | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | B | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| collective | standard | C | B | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| collective | standard | C | C | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| balanced | standard | A | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | A | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | B | B | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | B | C | 750 | 150 | 0 | Chuẩn mặc định, đủ dự phòng |
| balanced | standard | C | B | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| balanced | standard | C | C | 840 | 60 | 0 | Ngoại lệ lựa chọn |
| central | standard | A | B | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | A | C | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | B | B | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | B | C | 735 | 165 | 0 | Chuẩn mặc định, đủ dự phòng |
| central | standard | C | B | 825 | 75 | 0 | Ngoại lệ lựa chọn |
| central | standard | C | C | 825 | 75 | 0 | Ngoại lệ lựa chọn |
| central | fast_paid | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_paid | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_override | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | fast_override | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | combined_fast_paid | C | B | 735 | 165 | 0 | Ngoại lệ lựa chọn |
| central | combined_fast_paid | C | C | 735 | 165 | 0 | Ngoại lệ lựa chọn |

## I2: PP thuần và chênh quy đổi bổ sung

k chỉ là tham số sensitivity, không phải tỷ giá thật trong game. I2 theo yêu cầu kiểm PP thuần; không chuyển định nghĩa sang quy đổi. Dự án phụ L1.2 là phần giá trị còn lại; cửa sổ ký được theo dõi độc lập.

| k thử | Giá gói PP | Thưởng PP | Chênh PP thuần | Ngân khố gói | Chênh quy đổi |
| --- | --- | --- | --- | --- | --- |
| 20 | 55 | 50 | 5 | 0.5 | 15.0 |
| 40 | 55 | 50 | 5 | 0.5 | 25.0 |
| 60 | 55 | 50 | 5 | 0.5 | 35.0 |

## I3: biên checkpoint từng k

Dấu âm: thương lượng rẻ hơn; dấu dương: vượt rẻ hơn theo giá quy đổi. Biên k=40 chỉ1PP; chưa kiểm sức mua/engine, không chỉnh rộng biên.

| k thử | Thương lượng quy đổi | Vượt quy đổi | Thương lượng − vượt |
| --- | --- | --- | --- |
| 20 | 20.0 | 24 | -4.0 |
| 40 | 25.0 | 24 | 1.0 |
| 60 | 30.0 | 24 | 6.0 |

## I3 trên ngoại lệ: có rẻ nhất ở mọi k không?

So cùng tuyến/mode với mọi lựa chọn E102×E103 cho kết quả full trong programme kiểm tra; ngày chậm và dữ liệu được giữ riêng.

| Tuyến | Mode | E102 | E103 | Rẻ nhất ở mọi k |
| --- | --- | --- | --- | --- |
| collective | standard | C | B | Không |
| collective | standard | C | C | Không |
| balanced | standard | C | B | Không |
| balanced | standard | C | C | Không |
| central | standard | C | B | Không |
| central | standard | C | C | Không |
| central | fast_paid | C | B | Không |
| central | fast_paid | C | C | Không |
| central | fast_override | C | B | Không |
| central | fast_override | C | C | Không |
| central | combined_fast_paid | C | B | Không |
| central | combined_fast_paid | C | C | Không |

## Điểm lệch trong chính cặp ngoại lệ

Giữ E102-C, E103-C luôn tiết kiệm15PP so với B trong mọi k/r; cùng ngày/cohesion/cơ hội trong CSV. B chỉ mua trạng thái hợp đồng được chấp nhận, chưa có lợi ích gameplay được định nghĩa riêng. Đây là rủi ro lựa chọn B bị trội, không được che bằng thưởng mới.

| Tuyến | Mode | C tiết kiệm PP so B | Ngày full chung | Cohesion chung | Kết luận |
| --- | --- | --- | --- | --- | --- |
| balanced | standard | 15 | 840 | 66 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |
| central | combined_fast_paid | 15 | 735 | 60 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |
| central | fast_override | 15 | 735 | 50 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |
| central | fast_paid | 15 | 735 | 66 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |
| central | standard | 15 | 825 | 66 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |
| collective | standard | 15 | 840 | 70 | C trội B trong ma trận; B chỉ khác trạng thái hợp đồng |

## I10: chạy lại sau khi thêm ngân khố

Mỗi hàng kiểm toàn ma trận và từng tuyến. Cơ hội so theo dự án phụ, chuyên gia và hợp tác sâu; không gộp chúng thành một điểm tùy ý. PP ròng và chi quy đổi được kiểm riêng; r chỉ đổi mẫu số thu nhập, không đổi tier/thời gian.

| k | r | Thước đo chi | Thống trị toàn bộ | Tập thể | Cân bằng | Tập trung |
| --- | --- | --- | --- | --- | --- | --- |
| 20 | 0.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 20 | 0.5 | converted_cost | 0 | 0 | 0 | 0 |
| 20 | 1 | pp_net_cost | 0 | 0 | 0 | 0 |
| 20 | 1 | converted_cost | 0 | 0 | 0 | 0 |
| 20 | 1.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 20 | 1.5 | converted_cost | 0 | 0 | 0 | 0 |
| 40 | 0.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 40 | 0.5 | converted_cost | 0 | 0 | 0 | 0 |
| 40 | 1 | pp_net_cost | 0 | 0 | 0 | 0 |
| 40 | 1 | converted_cost | 0 | 0 | 0 | 0 |
| 40 | 1.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 40 | 1.5 | converted_cost | 0 | 0 | 0 | 0 |
| 60 | 0.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 60 | 0.5 | converted_cost | 0 | 0 | 0 | 0 |
| 60 | 1 | pp_net_cost | 0 | 0 | 0 | 0 |
| 60 | 1 | converted_cost | 0 | 0 | 0 | 0 |
| 60 | 1.5 | pp_net_cost | 0 | 0 | 0 | 0 |
| 60 | 1.5 | converted_cost | 0 | 0 | 0 | 0 |

## Giá quy đổi từng lựa chọn

Giá=PP+ngân khố×k−cohesion nhận×3; số âm là nguồn lực nhận ròng. Ngày và quyền dữ liệu được ghi riêng, không quy thành PP giả. Không cộng thưởng chương trình vào giá event để tránh tính trùng.

| Event / bối cảnh | Lựa chọn | k | Giá quy đổi |
| --- | --- | --- | --- |
| E101 | A | 20 | 29.0 |
| E101 | B | 20 | 24 |
| E101 | C | 20 | 17.0 |
| E102 | A | 20 | 40.0 |
| E102 | B | 20 | 25.0 |
| E102 | C | 20 | 15.0 |
| E104 | A | 20 | 15.0 |
| E104 | B | 20 | 10.0 |
| E104 | C | 20 | 0 |
| E103 hồ sơ đúng hạn | A | 20 | 0 |
| E103 hồ sơ trễ | A | 20 | 18 |
| E103 | B | 20 | 30 |
| E103 | C | 20 | 15 |
| checkpoint | thương lượng | 20 | 20.0 |
| checkpoint | vượt | 20 | 24 |
| E101 | A | 40 | 39.0 |
| E101 | B | 40 | 24 |
| E101 | C | 40 | 22.0 |
| E102 | A | 40 | 50.0 |
| E102 | B | 40 | 30.0 |
| E102 | C | 40 | 30.0 |
| E104 | A | 40 | 0.0 |
| E104 | B | 40 | 5.0 |
| E104 | C | 40 | 0 |
| E103 hồ sơ đúng hạn | A | 40 | 0 |
| E103 hồ sơ trễ | A | 40 | 18 |
| E103 | B | 40 | 30 |
| E103 | C | 40 | 15 |
| checkpoint | thương lượng | 40 | 25.0 |
| checkpoint | vượt | 40 | 24 |
| E101 | A | 60 | 49.0 |
| E101 | B | 60 | 24 |
| E101 | C | 60 | 27.0 |
| E102 | A | 60 | 60.0 |
| E102 | B | 60 | 35.0 |
| E102 | C | 60 | 45.0 |
| E104 | A | 60 | -15.0 |
| E104 | B | 60 | 0.0 |
| E104 | C | 60 | 0 |
| E103 hồ sơ đúng hạn | A | 60 | 0 |
| E103 hồ sơ trễ | A | 60 | 18 |
| E103 | B | 60 | 30 |
| E103 | C | 60 | 15 |
| checkpoint | thương lượng | 60 | 30.0 |
| checkpoint | vượt | 60 | 24 |

## Cohesion và phục hồi

60→52→44: một gói vượt đủ hai checkpoint; lần vượt tiếp theo 44−8=36<40 bị khóa. Gói thứ hai cần 44+2×10=64: 60 PP; phục hồi hoàn tất sau 270 ngày nếu chọn ngay ngày 0 và 180. Từ 44 chỉ một lượt 30 PP cho 54 mở được một checkpoint (54−8=46), chưa mở đủ hai (46−8=38). Cadre đòi 55 trong review, nên case vượt cần hai lượt phục hồi trong lúc triển khai: chọn sau checkpoint đầu tại ngày 165, kết thúc 255; chọn lại 345, kết thúc 435; phương án kế cận xong 465, review tới 555. Chi phí 60 PP đã cộng CSV. Đây là lịch số học, chưa kiểm engine.

## Scope CSV

Ma trận chuẩn hóa tại bắt đầu programme: cohesion 60, tier cán bộ 0, BoP −0.30/0/+0.30. Focus trước snapshot, thay người, tăng trưởng/chiến tranh và 62 node mở rộng không được giả lập. Cùng một E102×E103 và phản hồi E104 được áp cho mọi tuyến trong chương trình kiểm tra; programme khác không nhận event kiểm toán. Không tự cấp gói cấp tốc cho tập thể/cân bằng: hàng bị khóa có eligible=0 và số kết quả để trống. Kiêm nhiệm được chọn ngay sau khi ký giá/mode programme, trước checkpoint khi BoP/cohesion còn đủ cổng; không chọn sau khi BoP đã giảm về0.20. Cadre kiêm nhiệm mất6 về54, cần một lượt phục hồi30PP trước review (CSV đã cộng); recovery có thể xong ngày90, trước kiểm chứng465. Side project là lựa chọn sau full trước mốc, độc lập quyền nhận thưởng PP; cột chi/finish nếu chọn được tách khỏi tổng programme.

Đã tạo 1296 hàng, 648 hàng hợp lệ. Tất cả k=20/40/60 và r=0.5/1.0/1.5.

## Mục không đổi

Mục 1, 2, 6.1–6.3, danh mục node/cost/loại trừ, 7 trừ hai cửa sổ và tham chiếu timer, 8.2, toàn mục 9 (bao gồm ID và số dòng), 11.2 và dòng BLUF. Không sửa game file, history, localisation hoặc báo cáo Trung Quốc.

Đối chiếu trực tiếp bản đầu vào đã đọc xác nhận 6.1/6.2/6.3/8.2/11.2 giữ nguyên văn và danh sách tham chiếu repo không đổi. Script kiểm hash mục1/2/9, cost của74node và ba bảng ngày/lịch/E102×E103 khớp B1 mỗi lần chạy.

## Cần người dùng quyết định

Checkpoint và ngoại lệ C+B/C đã được chốt, không hỏi lại. Còn I3: khi đã chọn E102-C, E103-C luôn rẻ nhất trong ba lựa chọn (15 so A bị bác mất6cohesion quy đổi18, B30); C cũng trội B trong các chỉ số đã mô hình. Có thể chốt hệ quả cụ thể của hợp đồng được chấp nhận hoặc chấp nhận B là lựa chọn tình huống ngoài các chỉ số này; chưa tự thêm thưởng hay đổi giá. Còn I5 ở cohesion<20: chuẩn kiểm tra750+60=810, dự phòng90<100, không thuộc ngoại lệ E102-C+B/C được phép. Có thể giới hạn I5 cho snapshot hoặc chốt xử lý phase chuẩn bị; chưa chọn thay bạn. E101 không cộng vào ma trận vì caller F05 riêng; các node chưa viết và API/idea chưa có game file vẫn cần lượt2/3.

## Changelog lượt 1

| Mục | Cũ | Mới | Lý do | Cập nhật theo |
| --- | --- | --- | --- | --- |
| L1.1 | Mốc sớm chung 660 | {'cadre': 600, 'administration': 600, 'inspection': 690, 'social': 600} | Chuẩn trượt, cấp tốc đạt | Kết luận;4.2;6.5;7.3;8.3;10;11;12;CSV |
| L1.2 | Thưởng 60 PP | 50 PP; dự án phụ 270 ngày/30 PP | Chênh gói trả đủ chỉ 5 PP | 4.2;8.1;8.3;10;11;12;CSV |
| L1.3 | Vượt không có cổng;40–69 hệ số1 | Sau trừ >=40;40–54 hệ số1.05 | Giá/cổng tác động trước khi cohesion tụt thấp | 3.2;3.3;10;11.3;CSV |
| L1.4 | Thẩm định lại thiếu quy tắc tuần tự | Nếu A trượt: max(T,690)+180; B đến810; C partial hợp đồng | Hậu quả E102-C được tính chung | 6.4;6.5;8.3;10;11;CSV |
| L1.5 | Ký tier1/2:35/30 | Tier1/2:30/25; XIII09:25;XIV11:21 | Ba cửa sổ có giá trị ở ba tier | 4.4;5.2;6.6;hai hàng7.4;10;11.3 |
| L1.6 | Drift có nhưng thiếu cảnh báo | +0.30→+0.20 khi trả đủ; khóa cấp tốc lần tới | Giữ mode đã ký, báo trước | 3.1;10;11;CSV |
| L1.7 | min(+900,chuẩn bị kỳ sau) | +900 cố định; nhỏ nhất còn380 ngày | Lịch độc lập có dự phòng | 4.2;11;CSV |
| L1.8 | 15 hàng; chỉ kiểm tra, event khác giữa tuyến | Ma trận1296 hàng,648 hợp lệ; cùng E102×E103 ở mọi tuyến | Tách snapshot, chi từng khoản, k và r | 11.1;CSV;script;B1 |
| Theo dõi phạm vi | Không có nguồn B1 | JSON + bảng B1 + hash mục không đổi | Giữ nguồn duy nhất và kiểm scope | Báo cáo lượt1 |
| Quyết định checkpoint | 15PP, ngân khố0 mỗi checkpoint | 15PP + 0.25 ngân khố; gói55PP + 0.50 | Người dùng chốt; I3 đổi lựa chọn rẻ nhất theo k | B1;3.2;4.2–4.3;6;10;11.1;11.3;12;CSV |
| Quyết định I2 | Chỉ báo chênh5PP | PP thuần5; quy đổi15/25/35 ở k20/40/60 | Giữ định nghĩa PP thuần đã chốt | 4.2;10;11.1;11.3;Báo cáo |
| Quyết định I5 | Ngoại lệ840/825 chưa cho phép | C+B/C:full840/825/735, dự phòng60/75/165; không thưởng sớm | Chỉ ngoại lệ do lựa chọn có bảng; không đổi deadline/giá | B1;4.2;6.4–6.5;10;11.1;11.3;12;CSV |

Giữ74node, deadline900, gói55PP/thưởng50PP và mọi giá khác. k chỉ là tham số kiểm tra; không dùng để đổi định nghĩa I2. Chưa triển khai engine/playtest.

BLUF
