# Lượt 3: hoàn thiện cổng I5, đặc tả I6 và mô hình I10

Đã áp dụng các quyết định người dùng: E103-B0PP+0.50/hạn780; cổng start800/choice840 chỉ xét trễ tất định, không khóa rủi ro A; hoàn thiện22node và consumer40node; chốt giá còn trống. Mọi giá mới là **giả định gameplay, chưa cân bằng bằng engine**. C15PP/E102+90/thẩm định180/programme900 và mọi giá/timer programme giữ nguyên. I3 giữ kiểm tiền trực tiếp; chỉ XII12/XIII12 kiểm Pareto theo xác nhận. Biên nhỏ được báo, không chỉnh số.

## Changelog

| Mục | Cũ | Mới | Lý do | Các chỗ cập nhật |
| --- | --- | --- | --- | --- |
| 7.4 | Bảng6cột nhưng separator5cột | 6cột thống nhất | Sửa Markdown | 5 bảng40node |
| 7.4 XII | Thiếu mutex trong gate | XII01/05 và XII04/08 ghi hai chiều | Khôi phục lựa chọn đã chốt | B1 mutex; script |
| 7.4 prerequisite XII | XII05 phụ thuộc tổ tiênXII01 loại trừ; XII08 quaXII04 loại trừ | Hai rootXII01/05; intermediate dùngOR; XII04/08 cùng sauXII07 | Sửa gate chết, giữ hai cặp loại trừ và node chung | B1 focus_prerequisites;7.4; kiểm mọi đườngOR |
| 7.4 lịch sử | Focus neo2011/2021 có thể phát event lịch sử sớm | XI08 event từ02/05/2014; XIII05 crisis từQ4/2022 | Tách ngày mở focus với ngày caller lịch sử | B1;7.4;10 |
| XIV05 | Thiếu180ngày gia hạn | Gia hạn hồ sơ180ngày; programme900 không đổi | Khôi phục timer đã có | B1 delays;7.4 |
| XIV08 | 20PP, giữ thêm30ngày | 25PP, giảm30ngày gián đoạn | Khôi phục giá/hiệu quả cũ bị đổi thiếu giải thích | B1 prices/delays;7.4;I3 |
| 8.1 | Registry thiếu nhãn/caller/lịch sử | Ghi writer/reader/epoch và pending | Đóng các nhãn hiện dùng | B1 designed_identifiers |
| 7/11.3/12 | Cho thêm node; nhắcCI; kết luận quá mức | Giữ74; script local; ghi FAIL đúng phạm vi | Tuân thủ scope và giới hạn kiểm tra | Kết luận;7.5;11.3;12 |
| Script | Lệnh mặc định quay về hashL1 | --audit-l3 dựngCSV, đối chiếu và xuất báo cáoL3 | Không ghi đè reviewL1/L2 | Script;11.1 |
| Nguồn lịch sử | Link nợ xấu/mốc01May chưa chỉ đúng bài hỗ trợ | Link nghị quyết chuẩn và họp báo07May2014 | Nguồn trực tiếp hỗ trợ mốc được nêu | 2;B1 anchors;I8 |
| E103-B | 30PP, ngân khố0 | 0PP+0.50ngân khố | Người dùng chọn phương án1 | B1;6.5;CSV;event_cost_pp/net_treasury_cost;10;11.1;11.3;12 |
| Hạn B | Bản hiện tại810 | 780 | Mốc780 được người dùng chốt rõ; ghi lệch, không giả vờ đã giữ810 | B1 B_deadline;6.5;contract CSV;10 |
| I5 | Ngoại lệ chỉC+B/C, chưa có sàn | Mặc định100; mọi lựa chọn vào ngoại lệ riêng/sàn60 | Người dùng chọn phương án2 | B1;4.2;6.5;CSV ngoại lệ;10;11.3;12 |
| Biên I3 | Không in đủ hai kịch bản | Đủ/chưa đủ×k20/40/60; biênA/B2 ởk40 | Báo biên<3, không tự chỉnh | 6.5;report;I3 |
| I5 cổng dự báo | 8đường full dưới sàn; chỉ báo | Start≤800; trễ tất định≤840; A rủi ro không khóa | Người dùng chốt cổng, không sửa giá/timer | B1 forecast_gate;4.2;6.4–6.6;8.1;10;11.3;CSV |
| 22node | Thiếu gate/caller/guard/reader | Đặc tả theo legacy_node_specs, prerequisite OR/mutex kiểm bằng script | Hoàn thiện I6 theo yêu cầu | B1;7.4;8.1;11.3;12 |
| 40hậu quả | Quyền/dữ liệu chỉ mô tả | Consumer hành động available1/đối ứng0, record đúng đối tượng/epoch | Lượng hóa I10, không thêm điểm thưởng | B1 node_opportunity_effects;7.4a;8.1;10;CSV720hàng |
| Giá còn trống | 12ô null | Bộ giá được người dùng chốt, XI12 bồi hoàn khác XII12 roster | Giả định gameplay, chưa cân bằng bằng engine | B1 legacy_node_terms;7.4;10;11.3;CSV lựa chọn;report |
| I3 Pareto | Kiểm tiền trực tiếp XII12/XIII12 FAIL | Chỉ hai node này kiểm Pareto đa chiều có tên | Người dùng chốt ngoại lệ; không mở rộng node khác | B1 i3_pareto_exceptions;7.4b;10;11.3;CSV;report |
| XIII12 cổng bổ sung | Sửa bị hủy thống trị khi hỗ trợ/quyền đã cạn | e104_contract_amendment_gate: sửa cần còn hỗ trợ hoặc quyền; hủy luôn mở | Người dùng chốt tránh phương án bị thống trị; giữ giá/timer | 7.4 XIII12;8.1 ledger;10 UI/AI;11.3;CSV;63phép so Pareto |
| Cổng chốt trọng tâm | Có thể chốt kiểm tra dù phục hồi xong271/360/450 | Cùng forecast_programme_completion trả cổng chốt theo ngày khởi động khả thi≤270; phục hồi/hòa giải không bị cổng khóa | Người dùng chốt thêm guard; không đổi giá/timer; cổng riêng theo programme và cổng chung bất kỳ programme | B1 focus_commitment_gate;3.3;4.2;8.1;10;11.3;CSV dự báo;1440probe |
| Dọn đầu ra | Ba báo cáo tách riêng và JSON tự sinh mỗi lần | L1/L2 nguyên văn trong phụ lục L3; xóa hai file cũ; JSON chỉ sinh với --audit-json | Người dùng yêu cầu gộp/xóa sau khi hoàn tất; giữ hai script và ba CSV cần tái tạo | Report hiện hành;hash lịch sử trong B1;CLI;không xóa game files |

## Bất biến I1–I10

| Mã | Kết quả | Phép tính / phạm vi |
| --- | --- | --- |
| I1 | PASS | Cán bộ: 660/645 > 600 >= 555; Công vụ: 660/645 > 600 >= 555; Kiểm tra: 750/735 > 690 >= 645; Dân vận: 660/645 > 600 >= 555 |
| I2 | PASS | 55−50=5 PP; dự án phụ 270 ngày/30 PP |
| I3 | PASS | E101/E102/E104 kiểm tiền trực tiếp;E103 hai kịch bản×3k PASS=True;40node đảo giá theo k=True;XI12/XII10/XIV11 kiểm tiền trực tiếp. Chỉ XII12/XIII12 dùng Pareto theo xác nhận: 63 cặp, 0 cặp thống trị, 0 gần trùng. Biên XII10 k20:30 so29=1PP<3; không chỉnh. |
| I4 | PASS | Năm vùng cohesion có hệ số khác nhau; cổng sau trừ40; BoP qua0.25 làm đổi công cụ. Đây là kiểm vùng/biên, không chứng minh mỗi điểm trong cùng vùng đều đổi giá. |
| I5 | PASS | Cùng trigger: chốt khi còn đường≤270; start≤800/choice≤840. 1440probe0–39/cooldown0/90/180: cổng chung luôn còn công vụ/dân vận trước hạn, kiểm tra không kịp bị khóa riêng. 6/8full cũ dưới sàn bị khóa; 2rủi ro A885/dư15 giữ cảnh báo. Biên19/20 và270/271 có bảng; không cứu hồi tố kỳ đã hết hạn. |
| I6 | PASS | 74=2+6×12; cost/ID/mutex giữ; 40đặc tả+22gate/caller/guard/reader+12lát cắt; thiếu=[]. |
| I7 | PASS | 6 tên VIE và mọi nhãn node/E101–E104 được đăng ký8.1; ID kỹ thuật chưa định nghĩa và chưa xác minh provider. |
| I8 | PASS | Mốc lịch sử có link nguồn hoặc giả định gameplay; event XI08/XIII05 đã chặn phát sớm. Neo quýIV/2022 là gameplay, không giả ngày khởi đầu khủng hoảng. |
| I9 | PASS | Chỉ script/CSV/tài liệu; không chạy engine/console/playtest. |
| I10 | PASS | Ma trận: 0 tổ hợp thắng mọi đối thủ cùng programme/tuyến;0 tổ hợp thắng mọi4programme cùng tuyến ở9k/r. Cho phép đồng hạng với bản sao, phải tốt hơn ít nhất1đối thủ. 168 cặp thống trị là chẩn đoán.40consumer quyền cụ thể;64nhánh32node có reader hiện tại,16nhánhXIV chỉ archive không tăng cơ hội. So tập hành động thay vì điểm tổng; chưa chứng minh engine/sở thích. |

## Đối chiếu file và bảng

| Kiểm tra | Kết quả | Căn cứ |
| --- | --- | --- |
| Danh mục node/cost | PASS | 74 node; tên và cost theo B1 |
| Mục 1 | PASS | Giữ hash trước Lượt 3 |
| Mục 3 | PASS | Hash sửa E103/I5 đã xác nhận |
| Mục 4 | PASS | Hash sửa E103/I5 đã xác nhận |
| Mục 5 | PASS | Giữ hash trước Lượt 3 |
| Mục 6 | PASS | Hash sửa E103/I5 đã xác nhận |
| Mục 9 | PASS | Giữ hash trước Lượt 3 |
| BLUF | PASS | Giữ dòng cuối |
| Lịch sử Lượt1 đã gộp | PASS | Hash nguyên văn trước gộp; nguồn tham số hiện hành vẫn B1 |
| Lịch sử Lượt2 đã gộp | PASS | Hash nguyên văn trước gộp; nguồn tham số hiện hành vẫn B1 |
| Định dạng bảng | PASS | Hàng lệch số cột: [] |
| Loại trừ F03/F04 | PASS | Phải ghi ở cả hai node |
| Loại trừ IX11/IX12 | PASS | Phải ghi ở cả hai node |
| Loại trừ X09/X10 | PASS | Phải ghi ở cả hai node |
| Loại trừ XI09/XI10 | PASS | Phải ghi ở cả hai node |
| Loại trừ XII01/XII05 | PASS | Phải ghi ở cả hai node |
| Loại trừ XII04/XII08 | PASS | Phải ghi ở cả hai node |
| Loại trừ XIII10/XIII11 | PASS | Phải ghi ở cả hai node |
| Loại trừ XIV05/XIV06 | PASS | Phải ghi ở cả hai node |
| Loại trừ XIV08/XIV09 | PASS | Phải ghi ở cả hai node |
| Prerequisite và mutex | PASS | 62 node: []; thử mọi nhánh OR, không khóa node qua tổ tiên loại trừ |
| Bảng ngày 11.1 | PASS | Tính độc lập từ action_days/prepare_days |
| Bảng công cụ 4.3 | PASS | Ngày/PP/ngân khố của cả bốn chương trình từ B1 |
| Ký theo tier | PASS | 4.4/5.2/6.6 dùng cùng tier/cửa sổ B1 |
| Bảng lịch | PASS | Khoảng nhỏ nhất 380 ngày |
| Số học toàn CSV | PASS | 1296 hàng; 648 hợp lệ; 0 sai tổng/timeline/thu nhập/chi quy đổi |
| Giữ thông số đã chốt | PASS | B0PP+0.50; hạn780; C15/E102+90/thẩm định180/programme900 |
| Phủ ma trận CSV | PASS | 1296 tổ hợp không trùng; hàng khóa vẫn được ghi |
| Bảng ngân sách mẫu 11.1 | PASS | Đối chiếu từng cột CSV ở k=40/r=1 |
| Bảng E102 × E103 6.5 | PASS | 54 tổ hợp lịch tiềm năng |
| Bảng ngoại lệ I5 | PASS | 84 tổ hợp snapshot/thấpcohesion, so CSV ngoại lệ độc lập |
| Bảng hai kịch bản E103 | PASS | 6 kịch bản×k; chiA/B/C và chênh mọi cặp |
| Bảng I2 | PASS | PP thuần và ngân khố không tính trùng |
| Bảng checkpoint | PASS | Từ B1, không dùng số hardcode của bảng |
| Registry 8.1 | PASS | 6 tên thiết kế; 74 nhãn node; E101–E104 có registry; chưa là định nghĩa engine |
| Registry hoàn thiện | PASS | Tên thiết kế mới có writer/reader và vòng đời; chưa tạo ID engine |
| I3 tiền trực tiếp E101/E102/E104 | PASS | Cùng event/tuyến, k20/40/60; E104 dùng bối cảnh đối tác chấp nhận đã công bố |
| XIII12 cổng/softlock/hủy | PASS | 55 trạng thái ledger; hủy luôn mở/idempotent, chỉ chạm ledger; hỗ trợ đã nhận/quyền đã dùng giữ nguyên, không có writer mission/tier/reward |
| Cổng chốt / softlock trong cửa sổ | PASS | 1440 probe toàn bộ0–39/cooldown0/90/180/3tuyến/4programme; phục hồi/hòa giải không bị cổng khóa; không chốt kiểm tra không kịp270 |
| Giữ giá và timer khi thêm cổng | PASS | 19 nhóm tham số giữ hash; khác=[] |
| 22node hoàn thiện | PASS | 22 gate/caller/guard/reader; thiếu=[] |
| Consumer40node | PASS | 720 hàng; hành động riêng và đối ứng khóa; archive_XV không tính utility hiện tại |
| CSV lựa chọn node | PASS | 1089=720 quyền+243giá+126 vector; 0 sai tổng; hỗ trợ mất khác debit thật |
| Cổng dự báo I5 | PASS | 16 probe start, 84 ngoại lệ; trễ tất định bị khóa; 2 nhánh A dưới60 chỉ cảnh báo theo xác nhận |
| XIV10 trần và không chồng | PASS | Nghiệm thu cùng địa điểm; max(tier,idea); một lần/địa điểm/epoch, không cộng thời hạn |
| Phạm vi Pareto | PASS | Chỉ hai node được người dùng chốt; không đổi giá/timer |

## Chi quy đổi mọi lựa chọn event lát cắt

Giá=PP+ngân khố×k−cohesion nhận×3; E104 là kịch bản đối tác chấp nhận. Thời gian và quyền dữ liệu chưa quy đổi thànhPP.

| Event/bối cảnh | Option | k | Chi quy đổi |
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
| E103 | B | 20 | 10.0 |
| E103 | C | 20 | 15 |
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
| E103 | B | 40 | 20.0 |
| E103 | C | 40 | 15 |
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
| E103 | B | 60 | 30.0 |
| E103 | C | 60 | 15 |

| Event | I3 tiền trực tiếp | Rẻ nhất mọi k |
| --- | --- | --- |
| E101 | PASS | không có lựa chọn rẻ nhất mọi k |
| E102 | PASS | không có lựa chọn rẻ nhất mọi k |
| E104 | PASS | không có lựa chọn rẻ nhất mọi k |

## E103: hai kịch bản và mọi biên chênh lệch

A rẻ nhất khi đủ hồ sơ được chấp nhận. A chưa đủ có chi cohesion−6×3=18PP quy đổi và180ngày thẩm định riêng; không cộng ngày thànhPP. CộtB−A/B−C/A−C là chênh có dấu; dùng trị tuyệt đối để báo biên<3. k40/chưa đủ có A18 soB20, biên2PP: cảnh báo, không đổi giá.

| Hồ sơ | k | A | B | C | A thêm ngày | Rẻ nhất | Biên hạng1–2 | B−A | B−C | A−C | Cảnh báo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Đủ hồ sơ | 20 | 0 | 10.0 | 15 | 0 | A | 10.0 | 10.0 | -5.0 | -15 |  |
| Đủ hồ sơ | 40 | 0 | 20.0 | 15 | 0 | A | 15 | 20.0 | 5.0 | -15 |  |
| Đủ hồ sơ | 60 | 0 | 30.0 | 15 | 0 | A | 15 | 30.0 | 15.0 | -15 |  |
| Chưa đủ hồ sơ | 20 | 18 | 10.0 | 15 | 180 | B | 5.0 | -8.0 | -5.0 | 3 |  |
| Chưa đủ hồ sơ | 40 | 18 | 20.0 | 15 | 180 | C | 3 | 2.0 | 5.0 | 3 | BIÊN <3 |
| Chưa đủ hồ sơ | 60 | 18 | 30.0 | 15 | 180 | C | 3 | 12.0 | 15.0 | 3 |  |

## I5: bảng ngoại lệ và cổng đầy đủ

84 tổ hợp phản thực snapshot60/probe<20. Ngày tiềm năng và result cho biết kết quả nếu đi đường đó, không tự trao full cho hàng bị khóa. 6/8đường full cũ dưới sàn bị khóa;2rủi ro A885 còn mở theo xác nhận, nếu bị bác vẫn chỉ dư15. I5 PASS **cổng trễ tất định**, không phải mọi nhánh rủi ro đều bảo đảm60ngày. B/C không cộng ngày programme; mọi900/90/180 giữ nguyên.

| Cohesion | Tuyến | Mode | E102 | E103 | Ngày tiềm năng | Dự phòng | Programme | Hợp đồng | Sàn | Lý do | Cổng | Dự báo tất định | Dự phòng dự báo | Rủi ro A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| snapshot | collective | standard | A | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | collective | standard | A | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | A | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | B | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | collective | standard | B | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | B | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | collective | standard | C | A | 1020 | -120 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 840 | 60 | CẢNH BÁO |
| snapshot | collective | standard | C | B | 840 | 60 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | collective | standard | C | C | 840 | 60 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | balanced | standard | A | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | balanced | standard | A | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | A | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | B | A | 930 | -30 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 750 | 150 | CẢNH BÁO |
| snapshot | balanced | standard | B | B | 750 | 150 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | B | C | 750 | 150 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 750 | 150 |  |
| snapshot | balanced | standard | C | A | 1020 | -120 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 840 | 60 | CẢNH BÁO |
| snapshot | balanced | standard | C | B | 840 | 60 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | balanced | standard | C | C | 840 | 60 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 840 | 60 |  |
| snapshot | central | standard | A | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | standard | A | B | 735 | 165 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | A | C | 735 | 165 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | B | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | standard | B | B | 735 | 165 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | B | C | 735 | 165 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | standard | C | A | 1005 | -105 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 825 | 75 | CẢNH BÁO |
| snapshot | central | standard | C | B | 825 | 75 | full | extension_missed | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 825 | 75 |  |
| snapshot | central | standard | C | C | 825 | 75 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 825 | 75 |  |
| snapshot | central | fast_paid | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_paid | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | fast_paid | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_paid | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_override | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | fast_override | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | fast_override | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | fast_override | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | combined_fast_paid | A | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | A | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | B | B | 645 | 255 | full | extended | ĐẠT | E103-B:hợp đồng780, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | B | C | 645 | 255 | full | partial | ĐẠT | E103-C:hợp đồng partial, không cộng ngày programme | available | 645 | 255 |  |
| snapshot | central | combined_fast_paid | C | A | 915 | -15 | partial_at_deadline | rejected | DƯỚI SÀN | E102-C:+90; E103-A bị bác:+180 tuần tự | available | 735 | 165 | CẢNH BÁO |
| snapshot | central | combined_fast_paid | C | B | 735 | 165 | full | extended | ĐẠT | E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 735 | 165 |  |
| snapshot | central | combined_fast_paid | C | C | 735 | 165 | full | partial | ĐẠT | E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 735 | 165 |  |
| low | collective | standard | A | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | collective | standard | A | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | A | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | B | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | collective | standard | B | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | B | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | collective | standard | C | A | 1080 | -180 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_start | 900 | 0 | CẢNH BÁO |
| low | collective | standard | C | B | 900 | 0 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | collective | standard | C | C | 900 | 0 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | balanced | standard | A | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | balanced | standard | A | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | A | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | B | A | 990 | -90 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | locked_start | 810 | 90 | CẢNH BÁO |
| low | balanced | standard | B | B | 810 | 90 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | B | C | 810 | 90 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 810 | 90 |  |
| low | balanced | standard | C | A | 1080 | -180 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_start | 900 | 0 | CẢNH BÁO |
| low | balanced | standard | C | B | 900 | 0 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | balanced | standard | C | C | 900 | 0 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_start | 900 | 0 |  |
| low | central | standard | A | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | standard | A | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | A | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | B | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | standard | B | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | B | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |
| low | central | standard | C | A | 1065 | -165 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | locked_choice | 885 | 15 | CẢNH BÁO |
| low | central | standard | C | B | 885 | 15 | full | extension_missed | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | locked_choice | 885 | 15 |  |
| low | central | standard | C | C | 885 | 15 | full | partial | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | locked_choice | 885 | 15 |  |
| low | central | fast_paid | A | A | 885 | 15 | full | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 705 | 195 | CẢNH BÁO |
| low | central | fast_paid | A | B | 705 | 195 | full | extended | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | A | C | 705 | 195 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | B | A | 885 | 15 | full | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E103-A bị bác:+180 tuần tự | available | 705 | 195 | CẢNH BÁO |
| low | central | fast_paid | B | B | 705 | 195 | full | extended | ĐẠT | cohesion<20: chuẩn bị+60; E103-B:hợp đồng780, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | B | C | 705 | 195 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E103-C:hợp đồng partial, không cộng ngày programme | available | 705 | 195 |  |
| low | central | fast_paid | C | A | 975 | -75 | partial_at_deadline | rejected | DƯỚI SÀN | cohesion<20: chuẩn bị+60; E102-C:+90; E103-A bị bác:+180 tuần tự | available | 795 | 105 | CẢNH BÁO |
| low | central | fast_paid | C | B | 795 | 105 | full | extension_missed | ĐẠT | cohesion<20: chuẩn bị+60; E102-C:+90; E103-B:hợp đồng780, không cộng ngày programme | available | 795 | 105 |  |
| low | central | fast_paid | C | C | 795 | 105 | full | partial | ĐẠT | cohesion<20: chuẩn bị+60; E102-C:+90; E103-C:hợp đồng partial, không cộng ngày programme | available | 795 | 105 |  |

## I5: kiểm kẹt và phục hồi

| Programme | Tuyến | Mode | Cohesion | Lịch mặc định | Dự phòng | Start | Mở lại |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cadre | collective | standard | 0–19 | 720 | 180 | MỞ |  |
| cadre | balanced | standard | 0–19 | 720 | 180 | MỞ |  |
| cadre | central | standard | 0–19 | 705 | 195 | MỞ |  |
| cadre | central | fast_paid | 0–19 | 615 | 285 | MỞ |  |
| administration | collective | standard | 0–19 | 720 | 180 | MỞ |  |
| administration | balanced | standard | 0–19 | 720 | 180 | MỞ |  |
| administration | central | standard | 0–19 | 705 | 195 | MỞ |  |
| administration | central | fast_paid | 0–19 | 615 | 285 | MỞ |  |
| inspection | collective | standard | 0–19 | 810 | 90 | KHÓA | Họp xử lý bất đồng trước khởi động; sau ký timer không giảm |
| inspection | balanced | standard | 0–19 | 810 | 90 | KHÓA | Họp xử lý bất đồng trước khởi động; sau ký timer không giảm |
| inspection | central | standard | 0–19 | 795 | 105 | MỞ |  |
| inspection | central | fast_paid | 0–19 | 705 | 195 | MỞ |  |
| social | collective | standard | 0–19 | 720 | 180 | MỞ |  |
| social | balanced | standard | 0–19 | 720 | 180 | MỞ |  |
| social | central | standard | 0–19 | 705 | 195 | MỞ |  |
| social | central | fast_paid | 0–19 | 615 | 285 | MỞ |  |

Phục hồi0→20 với decision hiện có; cooldown tính từ lúc chọn, không phải hoàn tất:

| Chọn ngày | Xong ngày | Cohesion sau | PP lượt | PP tổng |
| --- | --- | --- | --- | --- |
| 0 | 90 | 10 | 15 | 15 |
| 180 | 270 | 20 | 15 | 30 |

Kết thúc270ngày, bằng cửa sổ start270 inclusive: không có độ dư. Chỉ riêng cohesion/cổng không khóa cả bốn programme: công vụ/dân vận vẫn mở ở mọi tuyến trong cửa sổ; kiểm tra chuẩn tập thể/cân bằng bị khóa ở0–19, tập trung chuẩn795 và cấp tốc705 vẫn mở nếu BoP cho phép. Giả định decision phục hồi sẵn ởngày0, đủPP, chọn ngay, không dùng cooldown để đóng kiến nghị. Chọn chậm1ngày làm phục hồi xong271, lỡ cửa sổ; đây là rủi ro lịch, không tự kéo270. Không kết luận tránh softlock cho mọi save: thiếuPP/ngân khố, hết cửa sổ, chưa mở công cụ và trạng thái chiến tranh nằm ngoài probe. Đề xuất vận hành: tooltip báo hạn phục hồi và chọn công vụ/dân vận nếu cần; không tự đổi luật.


### Đường kẹt trước cổng: đối chiếu để chặn chốt

Nếu đã chọn kiểm tra, tuyến tập thể/cân bằng không có cấp tốc theo snapshot BoP, không được coi công vụ/dân vận là lựa chọn thay thế miễn phí trong cùng kỳ. Trong mô hình cô lập không có nguồn cohesion khác hoặc cách đổi tuyến hợp lệ trước270, cohesion0–9 và phục hồi chọn chậm1ngày, hoặc cooldown180đang chạy, không lên20 trước270; trọng tâm này không thể khởi động trong kỳ. Đây là kẹt mục tiêu do cổng mới, dù game và focus khác vẫn tiếp tục. Bảng sau chỉ tính decision đã có, không đổi phí/timer/cửa sổ:

| Cohesion đầu | Trễ chọn lượt đầu | Cooldown còn | Số lượt | Phục hồi xong | Cohesion sau | PP tổng | Dư cửa sổ270 | Kết quả trọng tâm kiểm tra chuẩn tập thể/cân bằng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 2 | 270 | 20 | 30 | 0 | CHỐT ĐƯỢC |
| 0 | 0 | 180 | 2 | 450 | 20 | 30 | -180 | KHÓA CHỐT KIỂM TRA |
| 0 | 1 | 0 | 2 | 271 | 20 | 30 | -1 | KHÓA CHỐT KIỂM TRA |
| 0 | 1 | 180 | 2 | 451 | 20 | 30 | -181 | KHÓA CHỐT KIỂM TRA |
| 9 | 0 | 0 | 2 | 270 | 29 | 30 | 0 | CHỐT ĐƯỢC |
| 9 | 0 | 180 | 2 | 450 | 29 | 30 | -180 | KHÓA CHỐT KIỂM TRA |
| 9 | 1 | 0 | 2 | 271 | 29 | 30 | -1 | KHÓA CHỐT KIỂM TRA |
| 9 | 1 | 180 | 2 | 451 | 29 | 30 | -181 | KHÓA CHỐT KIỂM TRA |
| 10 | 0 | 0 | 1 | 90 | 20 | 15 | 180 | CHỐT ĐƯỢC |
| 10 | 0 | 180 | 1 | 270 | 20 | 15 | 0 | CHỐT ĐƯỢC |
| 10 | 1 | 0 | 1 | 91 | 20 | 15 | 179 | CHỐT ĐƯỢC |
| 10 | 1 | 180 | 1 | 271 | 20 | 15 | -1 | KHÓA CHỐT KIỂM TRA |
| 19 | 0 | 0 | 1 | 90 | 29 | 15 | 180 | CHỐT ĐƯỢC |
| 19 | 0 | 180 | 1 | 270 | 29 | 15 | 0 | CHỐT ĐƯỢC |
| 19 | 1 | 0 | 1 | 91 | 29 | 15 | 179 | CHỐT ĐƯỢC |
| 19 | 1 | 180 | 1 | 271 | 29 | 15 | -1 | KHÓA CHỐT KIỂM TRA |

Cổng chốt đã được áp dụng: KHÓA CHỐT KIỂM TRA là không được chọn programme đích; cổng chung vẫn mở nếu còn programme khác. Ngày/phí dự kiến đều lấy từ cùng forecast_programme_completion, không tính lịch phục hồi ở một trigger khác. Những cổng phase90ngày, giá và điều kiện chế độ vẫn giữ nguyên.

### Cổng chốt: cohesion/cooldown đầy đủ

Mỗi vùng được kiểm mọi điểm, không chỉ đầu/cuối. MỞ@T là còn đường khởi động ở ngàyT tính từ đại hội; KHÓA@T nghĩa đường sớm nhất vẫn quá270, thiếu số ngày nêu trong ô. ĐủPP/ngân khố, không có event cohesion chưa biết và các bước còn lại thành công là giả định của probe. Lịch còn các milestone kinh tế/cán bộ chưa chứng minh bằng engine.

| Cohesion | Cooldown còn | Tuyến | Cán bộ | Công vụ | Kiểm tra | Dân vận | Cổng chung | Nếu programme bị khóa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0–9 | 0 | collective | MỞ@0 | MỞ@0 | MỞ@270 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 0 | balanced | MỞ@0 | MỞ@0 | MỞ@270 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 0 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 90 | collective | MỞ@0 | MỞ@0 | KHÓA@360; thiếu90 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 90 | balanced | MỞ@0 | MỞ@0 | KHÓA@360; thiếu90 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 90 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 180 | collective | MỞ@0 | MỞ@0 | KHÓA@450; thiếu180 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 180 | balanced | MỞ@0 | MỞ@0 | KHÓA@450; thiếu180 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 0–9 | 180 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 0 | collective | MỞ@0 | MỞ@0 | MỞ@90 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 0 | balanced | MỞ@0 | MỞ@0 | MỞ@90 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 0 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 90 | collective | MỞ@0 | MỞ@0 | MỞ@180 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 90 | balanced | MỞ@0 | MỞ@0 | MỞ@180 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 90 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 180 | collective | MỞ@0 | MỞ@0 | MỞ@270 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 180 | balanced | MỞ@0 | MỞ@0 | MỞ@270 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 10–19 | 180 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 0 | collective | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 0 | balanced | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 0 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 90 | collective | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 90 | balanced | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 90 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 180 | collective | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 180 | balanced | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |
| 20–39 | 180 | central | MỞ@0 | MỞ@0 | MỞ@0 | MỞ@0 | CÒN LỐI | trọng tâm bị khóa không được chốt; chọn chương trình đang mở |

Trong1440probe còn ít nhất một đường: công vụ/dân vận không cần phục hồi để qua cổng lịch800. Kiểm tra chuẩn tập thể/cân bằng:0–9/cooldown0 phục hồi xong270 còn mở; cooldown90/180 xong360/450 bị khóa;10–19/cooldown0/90/180 xong90/180/270 còn mở;20–39 khởi động ngay. Tuyến tập trung có chuẩn795 hoặc cấp tốc705 khi dưới20 nên vẫn mở theo gateBoP hiện có.

### Biên19/20

| Cohesion | Cooldown còn | Tuyến | Full nếu start ngay | Start ngay mở | Start khả thi sớm nhất | Ngày thiếu | Chốt programme mở |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | 0 | collective | 810 | 0 | 90 | 0 | 1 |
| 19 | 0 | balanced | 810 | 0 | 90 | 0 | 1 |
| 19 | 0 | central | 795 | 1 | 0 | 0 | 1 |
| 19 | 90 | collective | 810 | 0 | 180 | 0 | 1 |
| 19 | 90 | balanced | 810 | 0 | 180 | 0 | 1 |
| 19 | 90 | central | 795 | 1 | 0 | 0 | 1 |
| 19 | 180 | collective | 810 | 0 | 270 | 0 | 1 |
| 19 | 180 | balanced | 810 | 0 | 270 | 0 | 1 |
| 19 | 180 | central | 795 | 1 | 0 | 0 | 1 |
| 20 | 0 | collective | 750 | 1 | 0 | 0 | 1 |
| 20 | 0 | balanced | 750 | 1 | 0 | 0 | 1 |
| 20 | 0 | central | 735 | 1 | 0 | 0 | 1 |
| 20 | 90 | collective | 750 | 1 | 0 | 0 | 1 |
| 20 | 90 | balanced | 750 | 1 | 0 | 0 | 1 |
| 20 | 90 | central | 735 | 1 | 0 | 0 | 1 |
| 20 | 180 | collective | 750 | 1 | 0 | 0 | 1 |
| 20 | 180 | balanced | 750 | 1 | 0 | 0 | 1 |
| 20 | 180 | central | 735 | 1 | 0 | 0 | 1 |

19 có+60chuẩn bị;20 không có. Phục hồi trước start có thể mở chốt cho19, nhưng không mở start trước khi đủ điều kiện. Phục hồi sau start không giảm timer đã ký. Lượt phục hồi đang chạy được đọc theo purpose=cohesion: không tính thêm phí đã trả hoặc nhầm lượt hòa giải thành+10.

### Biên cửa sổ270/271

| Ngày từ đại hội | Cổng chung mở | Programme còn đường | Ngày thiếu | Cổng khóa phục hồi | Cổng khóa hòa giải |
| --- | --- | --- | --- | --- | --- |
| 270 | 1 | cadre,administration,inspection,social | 0 | False | False |
| 271 | 0 | không còn trong kỳ | 1 | False | False |

Ngày271 cửa sổ khởi động đã hết: không chốt programme cho kỳ hiện tại, phục hồi/hòa giải vẫn không bị cổng chốt khóa; không tự fail mission, trao tier hoặc hoàn tiền. Đại hội theo lịch vẫn tiếp tục; kỳ sau có cửa sổ mới. Cổng này không tự sửa save đã chốt từ trước hoặc xử lý hành động làm lỡ kế hoạch sau chốt. Nếu cần chính sách riêng cho dữ liệu cũ/kỳ bỏ lỡ, có ba phương án để người dùng quyết định: (1) giữ kỳ bỏ lỡ và chờ cửa sổ đại hội sau; (2) ghi trạng thái “chưa triển khai” khi cửa sổ đóng; (3) ghi0/4 và áp penalty fail đã có. Chưa thêm phương án2/3, không đổi timer/giá. Không có trạng thái kẹt toàn bộ programme do riêng cổng mới trong vùng/cooldown được yêu cầu trước khi cửa sổ đóng.


## Thay đổi ngân sách E103-B

Mọi kịch bản B giảm30PP và tăng0.50ngân khố ròng; E104 và các event khác giữ nguyên.

| k | ΔPP ròng | Δngân khố ròng | Δchi quy đổi |
| --- | --- | --- | --- |
| 20 | -30 | 0.5 | -20.0 |
| 40 | -30 | 0.5 | -10.0 |
| 60 | -30 | 0.5 | 0.0 |

## Giá A/B của40node

| Node | k20 A/B | k40 A/B | k60 A/B |
| --- | --- | --- | --- |
| X01 | 20/10 | 20/20 | 20/30 |
| X02 | 25/10 | 25/20 | 25/30 |
| X03 | 30/15 | 30/30 | 30/45 |
| X04 | 15/10 | 15/20 | 15/30 |
| X05 | 20/10 | 20/20 | 20/30 |
| X06 | 25/15 | 25/30 | 25/45 |
| X07 | 20/10 | 20/20 | 20/30 |
| X08 | 15/10 | 15/20 | 15/30 |
| XI01 | 20/10 | 20/20 | 20/30 |
| XI02 | 15/25 | 30/25 | 45/25 |
| XI03 | 20/10 | 20/20 | 20/30 |
| XI04 | 15/10 | 15/20 | 15/30 |
| XI05 | 20/10 | 20/20 | 20/30 |
| XI06 | 25/15 | 25/30 | 25/45 |
| XI07 | 20/10 | 20/20 | 20/30 |
| XI08 | 15/10 | 15/20 | 15/30 |
| XII01 | 20/10 | 20/20 | 20/30 |
| XII02 | 25/15 | 25/30 | 25/45 |
| XII03 | 15/10 | 15/20 | 15/30 |
| XII04 | 20/10 | 20/20 | 20/30 |
| XII05 | 25/15 | 25/30 | 25/45 |
| XII06 | 20/10 | 20/20 | 20/30 |
| XII07 | 25/15 | 25/30 | 25/45 |
| XII08 | 15/10 | 15/20 | 15/30 |
| XIII01 | 20/10 | 20/20 | 20/30 |
| XIII02 | 25/15 | 25/30 | 25/45 |
| XIII03 | 15/10 | 15/20 | 15/30 |
| XIII04 | 20/15 | 20/30 | 20/45 |
| XIII05 | 20/10 | 20/20 | 20/30 |
| XIII06 | 25/15 | 25/30 | 25/45 |
| XIII07 | 20/10 | 20/20 | 20/30 |
| XIII08 | 15/10 | 15/20 | 15/30 |
| XIV01 | 20/10 | 20/20 | 20/30 |
| XIV02 | 25/15 | 25/30 | 25/45 |
| XIV03 | 15/10 | 15/20 | 15/30 |
| XIV04 | 20/10 | 20/20 | 20/30 |
| XIV05 | 30/15 | 30/30 | 30/45 |
| XIV06 | 20/10 | 20/20 | 20/30 |
| XIV07 | 25/15 | 25/30 | 25/45 |
| XIV08 | 25/10 | 25/20 | 25/30 |

## I10: cặp thống trị được phát hiện

Không có một tổ hợp thắng toàn ma trận không loại trừ cặp bị thống trị. Các hàng sau dùng cùng programme/tuyến, k40/r1; thời gian là full tiềm năng, cơ hội gồm dự án phụ/chuyên gia/dữ liệu sâu. Giá trị hợp đồng E103 không được tự quy thànhPP.

| Programme | Tuyến | Tổ hợp trội | Tổ hợp bị trội | PP trội | PP bị trội | Ngày trội | Ngày bị trội |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cadre | central | fast_override/NA/NA | combined_fast_paid/NA/NA | 180 | 240 | 555 | 555 |
| administration | central | fast_paid/NA/NA | combined_fast_paid/NA/NA | 150 | 210 | 555 | 555 |
| inspection | collective | standard/A/B | standard/A/A | 195 | 195 | 750 | 930 |
| inspection | collective | standard/A/B | standard/A/C | 195 | 210 | 750 | 750 |
| inspection | collective | standard/B/B | standard/B/A | 170 | 170 | 750 | 930 |
| inspection | collective | standard/B/B | standard/B/C | 170 | 185 | 750 | 750 |
| inspection | collective | standard/C/B | standard/B/A | 150 | 170 | 840 | 930 |
| inspection | collective | standard/C/B | standard/C/A | 150 | 150 | 840 | 1020 |
| inspection | collective | standard/C/B | standard/C/C | 150 | 165 | 840 | 840 |
| inspection | collective | standard/C/C | standard/B/A | 165 | 170 | 840 | 930 |
| inspection | balanced | standard/A/B | standard/A/A | 195 | 195 | 750 | 930 |
| inspection | balanced | standard/A/B | standard/A/C | 195 | 210 | 750 | 750 |

## Ánh xạ ID và giá đã chốt

XI12 là trách nhiệm bảo lãnh/bồi hoàn; XII12 là tái phân công roster. Không thấy giá bị gán nhầm giữa hai node trong bản B1 trước khi sửa. Mọi giá mới là giả định gameplay, chưa cân bằng bằng engine.

| Node | Tham số | Cũ | Mới |
| --- | --- | --- | --- |
| X09 | treasury_per_installment | chưa định lượng | 0.25 |
| XI12 | reparation_pp / treasury | chưa định lượng | 20PP /0.50 |
| XII10 | pp / cohesion / alternative_treasury | chưa định lượng | 30PP /8cohesion+0.25 |
| XII12 | immediate_cohesion_loss | chưa định lượng | 6 |
| XIII11 | treasury | chưa định lượng | 0.5 |
| XIII12 | cancellation_cost | chưa định lượng | hỗ trợ E104 chưa nhận; không phí mới |
| XIV10 | stability_reward | chưa định lượng | +1%,365ngày,trần1%,max với tier,nghiệm thu tương ứng |
| XIV11 | retain / amend / cancel | chưa định lượng | 15PP /0.50 /hỗ trợ chưa nhận |

## I3: giá lựa chọn node mới và mọi biên

Chi quy đổi=PP+ngân khố×k+cohesion mất×3; cohesion nhận được trừ tương ứng. Không đổi ngày sangPP. Các cặp focus loại trừ là so sánh riêng, không giả là lựa chọn trong cùng event.

| Node/cặp | Bối cảnh A/B | k | A | B | B−A | Biên tuyệt đối | Cảnh báo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IX11 / IX12 | luân chuyển / kiểm toán độc lập | 20 | 8 | 20 | 12 | 12 |  |
| IX11 / IX12 | luân chuyển / kiểm toán độc lập | 40 | 8 | 20 | 12 | 12 |  |
| IX11 / IX12 | luân chuyển / kiểm toán độc lập | 60 | 8 | 20 | 12 | 12 |  |
| X09 / X10 | hai đợt / ứng trước | 20 | 10.0 | 10.0 | 0.0 | 0.0 | BIÊN <3 |
| X09 / X10 | hai đợt / ứng trước | 40 | 20.0 | 20.0 | 0.0 | 0.0 | BIÊN <3 |
| X09 / X10 | hai đợt / ứng trước | 60 | 30.0 | 30.0 | 0.0 | 0.0 | BIÊN <3 |
| XI09 / XI10 | cứu dự án / tái cơ cấu | 20 | 10.0 | 0 | -10.0 | 10.0 |  |
| XI09 / XI10 | cứu dự án / tái cơ cấu | 40 | 20.0 | 0 | -20.0 | 20.0 |  |
| XI09 / XI10 | cứu dự án / tái cơ cấu | 60 | 30.0 | 0 | -30.0 | 30.0 |  |
| XI12 | bồi hoàn PP / ngân khố | 20 | 20 | 10.0 | -10.0 | 10.0 |  |
| XI12 | bồi hoàn PP / ngân khố | 40 | 20 | 20.0 | 0.0 | 0.0 | BIÊN <3 |
| XI12 | bồi hoàn PP / ngân khố | 60 | 20 | 30.0 | 10.0 | 10.0 |  |
| XII10 | đầu mối / hội đồng | 20 | 30 | 29.0 | -1.0 | 1.0 | BIÊN <3 |
| XII10 | đầu mối / hội đồng | 40 | 30 | 34.0 | 4.0 | 4.0 |  |
| XII10 | đầu mối / hội đồng | 60 | 30 | 39.0 | 9.0 | 9.0 |  |
| XII12 | bàn giao / kiện toàn ngay | 20 | 0 | 18 | 18 | 18 |  |
| XII12 | bàn giao / kiện toàn ngay | 40 | 0 | 18 | 18 | 18 |  |
| XII12 | bàn giao / kiện toàn ngay | 60 | 0 | 18 | 18 | 18 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0 | 20 | 0 | 0 | 0 | 0 | BIÊN <3 |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0 | 40 | 0 | 0 | 0 | 0 | BIÊN <3 |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0 | 60 | 0 | 0 | 0 | 0 | BIÊN <3 |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.25 | 20 | 0 | 5.0 | 5.0 | 5.0 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.25 | 40 | 0 | 10.0 | 10.0 | 10.0 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.25 | 60 | 0 | 15.0 | 15.0 | 15.0 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.75 | 20 | 0 | 15.0 | 15.0 | 15.0 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.75 | 40 | 0 | 30.0 | 30.0 | 30.0 |  |
| XIII12 | sửa / hủy; hỗ trợ chưa nhận=0.75 | 60 | 0 | 45.0 | 45.0 | 45.0 |  |

| Node | Hỗ trợ | k | Giữ | Sửa | Hủy | Sửa−Giữ,Hủy−Giữ,Hủy−Sửa | Cảnh báo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0 | 20 | 15 | 10.0 | 0 | -5,-15,-10 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0 | 40 | 15 | 20.0 | 0 | 5,-15,-20 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0 | 60 | 15 | 30.0 | 0 | 15,-15,-30 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.25 | 20 | 15 | 10.0 | 5.0 | -5,-10,-5 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.25 | 40 | 15 | 20.0 | 10.0 | 5,-5,-10 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.25 | 60 | 15 | 30.0 | 15.0 | 15,0,-15 | BIÊN <3 |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.75 | 20 | 15 | 10.0 | 15.0 | -5,0,5 | BIÊN <3 |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.75 | 40 | 15 | 20.0 | 30.0 | 5,15,10 |  |
| XIV11 | giữ / sửa / hủy; hỗ trợ chưa nhận=0.75 | 60 | 15 | 30.0 | 45.0 | 15,30,15 |  |

XI12/XII10/XIV11 giữ kiểm tiền trực tiếp; chỉ XII12/XIII12 dùng Pareto theo xác nhận mới. Biên1PP XII10 và2PP E103 giữ nguyên. Các caller chỉ mở công cụ không được gán hai giá giả; XI11 đóng/chuyển kiến nghị phụ thuộc hồ sơ/decision hiện có, không được giả là hai lựa chọn có giá riêng để chứng minh cân bằng.


## I3 Pareto: chỉ XII12 và XIII12

I3 của hai node này được đánh giá bằng Pareto, **không bằng chi phí tiền đơn lẻ**: có đánh đổi lịch/roster hoặc quyền hỗ trợ/nghĩa vụ hợp đồng đã tồn tại. Các node/event khác không được dùng ngoại lệ này. Thời gian/quyền không quy raPP. Chi phí hủy là hỗ trợ chưa nhận bị mất, không phải khoản trừ ngân khố thực; không thu hồi khoản đã nhận. Kết quả bằng nhau ở cả ba tuyến; bảng hiển thị một tuyến, CSV/JSON có đủ mọi tuyến.

| Node | Bối cảnh | k | Option | Chi quy đổi | Bàn giao/khóa roster ngày | Mất cohesion | Quyền người cũ | Quyền ký người mới | Mất hỗ trợ chưa nhận | Quyền hợp tác chưa dùng | Nghĩa vụ hợp đồng mở | Trạng thái | Trung tâm phản ứng | Cổng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XII12 | roster hợp lệ | 20 | A | 0 | 60 | 0 | 1 | 0 | — | — | — | pending_handover | văn phòng và người kế cận | MỞ |
| XII12 | roster hợp lệ | 20 | B | 18 | 0 | 6 | 0 | 1 | — | — | — | replacement_effective | văn phòng và người kế cận | MỞ |
| XII12 | roster hợp lệ | 40 | A | 0 | 60 | 0 | 1 | 0 | — | — | — | pending_handover | văn phòng và người kế cận | MỞ |
| XII12 | roster hợp lệ | 40 | B | 18 | 0 | 6 | 0 | 1 | — | — | — | replacement_effective | văn phòng và người kế cận | MỞ |
| XII12 | roster hợp lệ | 60 | A | 0 | 60 | 0 | 1 | 0 | — | — | — | pending_handover | văn phòng và người kế cận | MỞ |
| XII12 | roster hợp lệ | 60 | B | 18 | 0 | 6 | 0 | 1 | — | — | — | replacement_effective | văn phòng và người kế cận | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 20 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 20 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 40 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 40 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 60 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | KHÓA |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 60 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 20 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 20 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 40 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 40 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 60 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 60 | B | 0 | 0 | 0 | — | — | 0 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 20 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 20 | B | 5.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 40 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 40 | B | 10.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 60 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 60 | B | 15.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 20 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 20 | B | 5.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 40 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 40 | B | 10.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 60 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 60 | B | 15.0 | 0 | 0 | — | — | 0.25 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 20 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 20 | B | 15.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 40 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 40 | B | 30.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 60 | A | 0 | 0 | 0 | — | — | 0 | 0 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 60 | B | 45.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 20 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 20 | B | 15.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 40 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 40 | B | 30.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 60 | A | 0 | 0 | 0 | — | — | 0 | 1 | 1 | modified_active_if_partner_accepts | đối tác/DNNN giữ quyền hỗ trợ; an ninh tiếp tục kiểm chứng điều kiện sửa | MỞ |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 60 | B | 45.0 | 0 | 0 | — | — | 0.75 | 0 | 0 | terminated | đối tác/DNNN mất kênh hỗ trợ; an ninh đóng nghĩa vụ dữ liệu tương lai | MỞ |

Ngày của XII12 là thời gian bàn giao đã có; khóa quyền người mới trong cùng hồ sơ tới khi bàn giao, không dừng dự án khác. XIII12 không cộng ngày programme mới (0 cho cả hai); kiểm chứng đang có vẫn theo timer đã ký. Trạng thái quyền hợp tác chưa dùng đọc hợp đồng thực tế, không tự sinh quyền khi hỗ trợ đã cạn. An ninh đóng nghĩa vụ dữ liệu tương lai khi hủy, lịch sử hồ sơ và trách nhiệm quá khứ không xóa. Tooltip phải hiển thị mọi chiều trước chọn.

| Node | Bối cảnh | k | So từng cặp | ΔB−A từng chiều | Chênh tương đối từng chiều | Biên10% |
| --- | --- | --- | --- | --- | --- | --- |
| XII12 | roster hợp lệ | 20 | không thống trị | converted_cost:18; handover_pending_days:-60; cohesion_loss:6; old_holder_access:-1; new_holder_authority:1 | converted_cost:100%; handover_pending_days:100%; cohesion_loss:100%; old_holder_access:100%; new_holder_authority:100% | không gần trùng |
| XII12 | roster hợp lệ | 40 | không thống trị | converted_cost:18; handover_pending_days:-60; cohesion_loss:6; old_holder_access:-1; new_holder_authority:1 | converted_cost:100%; handover_pending_days:100%; cohesion_loss:100%; old_holder_access:100%; new_holder_authority:100% | không gần trùng |
| XII12 | roster hợp lệ | 60 | không thống trị | converted_cost:18; handover_pending_days:-60; cohesion_loss:6; old_holder_access:-1; new_holder_authority:1 | converted_cost:100%; handover_pending_days:100%; cohesion_loss:100%; old_holder_access:100%; new_holder_authority:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 20 | A KHÓA, B khả dụng | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 40 | A KHÓA, B khả dụng | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=0 | 60 | A KHÓA, B khả dụng | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 20 | không thống trị | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 40 | không thống trị | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0; quyền chưa dùng=1 | 60 | không thống trị | converted_cost:0; unreceived_support_lost:0; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:0%; unreceived_support_lost:0%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 20 | không thống trị | converted_cost:5; unreceived_support_lost:0.25; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 40 | không thống trị | converted_cost:10; unreceived_support_lost:0.25; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=0 | 60 | không thống trị | converted_cost:15; unreceived_support_lost:0.25; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 20 | không thống trị | converted_cost:5; unreceived_support_lost:0.25; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 40 | không thống trị | converted_cost:10; unreceived_support_lost:0.25; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.25; quyền chưa dùng=1 | 60 | không thống trị | converted_cost:15; unreceived_support_lost:0.25; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 20 | không thống trị | converted_cost:15; unreceived_support_lost:0.75; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 40 | không thống trị | converted_cost:30; unreceived_support_lost:0.75; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=0 | 60 | không thống trị | converted_cost:45; unreceived_support_lost:0.75; unused_cooperation_access:0; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:0%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 20 | không thống trị | converted_cost:15; unreceived_support_lost:0.75; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 40 | không thống trị | converted_cost:30; unreceived_support_lost:0.75; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |
| XIII12 | hỗ trợ=0.75; quyền chưa dùng=1 | 60 | không thống trị | converted_cost:45; unreceived_support_lost:0.75; unused_cooperation_access:-1; contract_obligation_open:-1 | converted_cost:100%; unreceived_support_lost:100%; unused_cooperation_access:100%; contract_obligation_open:100% | không gần trùng |

Chênh tương đối=|B−A|/max(|A|,|B|); cả hai0 thì0%; gần trùng khi mọi chiều<10%. Đây là quy ước báo biên, không đổi giá. Trước cổng, B hủy thống trị A sửa ở trạng thái hỗ trợ/quyền0. Cổng được người dùng chốt khóa **phương án bị thống trị A sửa**, B hủy vẫn mở. Không có cặp hai phương án khả dụng để bị thống trị trong trạng thái này; không gọi đó là cân bằng hai phương án.


### XIII12: đủ9phép so trạng thái đã cạn

| Tuyến | k | Sửa | Hủy | So cặp còn khả dụng | PASS/FAIL |
| --- | --- | --- | --- | --- | --- |
| collective | 20 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| collective | 40 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| collective | 60 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| balanced | 20 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| balanced | 40 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| balanced | 60 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| central | 20 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| central | 40 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |
| central | 60 | KHÓA | MỞ | A KHÓA, B khả dụng | PASS |

Các trạng thái XIII12 còn hỗ trợ hoặc quyền có45phép so;45cặp thống trị, 0gần trùng. Cổng chỉ XIII12, không dùng XIV11 hoặc node khác.

### XIII12: kiểm softlock và fail ngầm

| State | Hỗ trợ cam kết | Đã nhận | Chưa nhận | Quyền chưa dùng | Sửa mở | Hủy mở | Giữ paid/history và chỉ ghi ledger | Hủy lặp không phí/hiệu ứng mới | Kết quả |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pending | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| pending | 0.25 | 0 | 0.25 | 0 | 1 | 1 | 1 | 1 | PASS |
| pending | 0.25 | 0 | 0.25 | 0 | 1 | 1 | 1 | 1 | PASS |
| pending | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| pending | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0 | 0.75 | 0 | 1 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0 | 0.75 | 0 | 1 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0 | 0.75 | 0 | 1 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| pending | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| accepted | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| accepted | 0.25 | 0 | 0.25 | 1 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.25 | 0 | 0.25 | 0 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.25 | 0.25 | 0 | 1 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0 | 0.75 | 2 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0 | 0.75 | 1 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0 | 0.75 | 0 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0.75 | 0 | 2 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0.75 | 0 | 1 | 1 | 1 | 1 | 1 | PASS |
| accepted | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| modified | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| modified | 0.25 | 0 | 0.25 | 1 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.25 | 0 | 0.25 | 0 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.25 | 0.25 | 0 | 1 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0 | 0.75 | 2 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0 | 0.75 | 1 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0 | 0.75 | 0 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0.75 | 0 | 2 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0.75 | 0 | 1 | 1 | 1 | 1 | 1 | PASS |
| modified | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.25 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.25 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| terminated | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.25 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.25 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.25 | 0.25 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |
| refused | 0.75 | 0.75 | 0 | 0 | 0 | 1 | 1 | 1 | PASS |

Mọi ledger probe có hủy mở, không softlock do cổng sửa. Paper transition chỉ ghi support_forfeited/rights_revoked/contract_state; không có writer mission/tier/PP sớm/reward, không thu hồi tiền đã nhận hoặc quyền đã dùng. Do đó thiết kế hủy không fail mission hoặc mất thưởng ngoài tooltip. Kiểm này là script mô hình, cần xác minh adapter engine khi triển khai; không tuyên bố engine đã chạy.


## X09 và X10: kiểm thống trị riêng

| Phương án | Ngân khố tổng | Δngày dự án | Checkpoint trước trả | Kiến nghị giám sát do ứng trước |
| --- | --- | --- | --- | --- |
| X09 | 0.5 | 0 | 2 | 0 |
| X10 | 0.5 | -30 | 0 | 1 |

Không bên nào thống trị: X10 có−30ngày và không chờ checkpoint trước trả, nhưng mở thêm1kiến nghị chưa đóng; X09 không mở kiến nghị do ứng trước, nhưng chờ2checkpoint và không rút30ngày. Đo kiến nghị/đợt vốn cùng một hồ sơ, không tính checkpoint như phần thưởng tự động hoặc trừ phí kiểm toán lần nữa. Giá bằng nhau ở k20/40/60; khác biệt nằm ở lịch và nghĩa vụ.


## XIV10: trần idea và tier dân vận

| Tier | Ổn định tier | Idea | Ổn định hiệu lực | Phần tăng do idea |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0.01 | 0.01 | 0.01 |
| 1 | 0.01 | 0.01 | 0.01 | 0.0 |
| 2 | 0.02 | 0.01 | 0.02 | 0.0 |
| 3 | 0.03 | 0.01 | 0.03 | 0.0 |

Idea365ngày chỉ trao sau nghiệm thu cùng địa điểm, một lần/địa điểm/epoch; refresh thay thế, không cộng thời hạn. Dùng max(tier,idea), không áp hai modifier cộng dồn; hết hạn idea trả về tier đang có. Adapter engine chưa triển khai.


### Tham số còn trống trong B1

| Node | Tham số | Cách xử lý hiện tại |
| --- | --- | --- |

## I6/I10: kết quả và phạm vi

22node có kỳ/ngày/prerequisite/chế độ/đối tượng, caller, guard và reader;62node ngoài lát cắt được kiểm cùng danh mục74.40node có80hành động mang tên riêng (64nhánh hoạt động ở reader trong phạm vi;16nhánhXIV chỉ archive), CSV720hàng. Không dùng archive_XV làm cơ hội hiện tại. Các consumer là nhánh của caller có sẵn; phí mở quyền trả một lần, đủ quyền không tự đủ milestone. Ma trận programme không có universal winner theo từng programme/tuyến/k/r; pairwise dominance được giữ để chẩn đoán, không đổi giá. I10 PASS mô hình giấy hiện hành, chưa chứng minh utility theo sở thích, AI hoặc engine.

Kiểm thêm toàn4programme cùng mỗi tuyến ở9k/r: 0universal winner; trường hợp đồng hạng không che một ứng viên thắng các đối thủ khác.

CSV lựa chọn node tổng1089hàng:720hàng quyền,243hàng giá đã chốt, 126vector ngoại lệ Pareto. Cộtactual_treasury_debit tách tiền thực trừ khỏi unreceived_support_lost; không cộng trùng hai khoản. Bảng ma trận programme độc lập vẫn1296hàng/648hợp lệ, không bị giá node sửa.

## Mục không đổi

Mục1,5 và9 giữ hash trước Lượt3. Mục3 chỉ bổ sung cổng tại3.3; mục4/6 cập nhật đúng I5/E103 đã xác nhận và kiểm hash mới.20nhóm giá/timer giữ hash trước cổng chốt. Giữ ID/số dòng/tham chiếu repo9, cost74focus, deadline900, gói55PP/thưởng50, giá E101/E102/E104/C15; E102+90/thẩm định180. Lượt1/Lượt2 giữ nguyên văn trong lịch sử nếu đã gộp. Không sửa game files/localisation/artwork hoặc file kinh tế trong Downloads.

## Giới hạn và quyết định còn lại

- Các sửa đổi giá/cổng/Pareto và cổng chốt đã được chốt, không còn quyết định chặn hoàn thiện mô hình trước cửa sổ270.1440probe không có lối cụt toàn bộ programme do cổng mới; không tự cứu dữ liệu save đã chốt trước luật này. Các phương án xử lý kỳ đã bỏ lỡ nêu riêng để quyết định nếu cần, chưa triển khai.
- Rủi ro E103-A885/dư15 còn mở theo xác nhận: I5 PASS cổng trễ tất định, không bảo đảm nhánh rủi ro giữ60ngày.
- Engine/AI/playtest chưa chạy; giá mới là giả định gameplay. Không suy ra cân bằng theo sở thích hoặc lịch nhiều nhiệm kỳ từ một snapshot.

## Đầu ra

Tài liệu đầy đủ: [thiết kế](VIETNAM_POLITICAL_FOCUS_DESIGN_VI.md); nguồn [B1](VIETNAM_POLITICAL_PARAMETERS_VI.json); script chính [balance](VIETNAM_POLITICAL_BALANCE_VI.py), script đối chiếu [crosscheck](VIETNAM_POLITICAL_CROSSCHECK_VI.py); ma trận [CSV](VIETNAM_POLITICAL_BALANCE_VI.csv); [CSV ngoại lệ I5](VIETNAM_POLITICAL_I5_EXCEPTIONS_VI.csv); [CSV giá/quyền/Pareto node](VIETNAM_POLITICAL_NODE_CHOICES_VI.csv). Chạy `python VIETNAM_POLITICAL_BALANCE_VI.py --audit-l3` để dựng lại và đọc báo cáo; `--sync-approved` đồng bộ các bảng đã chốt vào tài liệu. JSON debug chỉ sinh khi thêm --audit-json. Exit2 nghĩa là cònFAIL thiết kế, không phải lỗi chạyPython.

<!-- HISTORICAL_REVIEW_ARCHIVE_START -->

## Phụ lục lịch sử Lượt 1–2

Các bản dưới đây được giữ nguyên văn để truy vết. Số liệu và PASS/FAIL là trạng thái tại lượt cũ; B1 và phần báo cáo hiện hành phía trên là nguồn đang áp dụng.

<details>
<summary>Lượt 1 — lịch sử đã gộp</summary>

<!-- SNAPSHOT_L1_START -->
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

<!-- SNAPSHOT_L1_END -->

</details>

<details>
<summary>Lượt 2 — lịch sử đã gộp</summary>

<!-- SNAPSHOT_L2_START -->
# Lượt 2: nội dung và lịch sử

Đã hoàn tất đặc tả 40 node được yêu cầu, giữ tổng danh mục 74, không thêm focus hoặc mã kỹ thuật event/flag mới. Nội dung lịch sử được xác minh bằng nguồn; hiệu ứng gameplay và quyết định trong event được ghi là giả định gameplay. Dừng sau Lượt 2 theo quy trình đã yêu cầu; chưa làm Lượt 3.

## Changelog

| Mục | Cũ | Mới | Lý do | Các chỗ đã cập nhật theo |
| --- | --- | --- | --- | --- |
| 2 / 7.1 / 7.2 | XI có cụm nghĩa vụ trái phiếu; Biển Đông chỉ mở ở XIII | XI chuyển sang nợ xấu/bất động sản, thêm hồ sơ giàn khoan 2014; XIII tiếp nối Biển Đông và nhận cụm trái phiếu cuối 2022 | Sắp nội dung theo mốc có nguồn | 2;7.1;7.2;7.4;11.3;12;B1 history anchors |
| X01–X08 | Một dòng đầu ra | Mỗi node có cost, gate ngày/kỳ/prerequisite/chế độ, caller, hai lựa chọn có giá khác loại, trung tâm phản ứng và hậu quả XI | Đạt yêu cầu chi tiết node, giữ cost | 7.4;B1 focus_nodes và node_choice_prices;script `--check-l2` |
| XI05–XI08 | Tín dụng bất động sản, trái phiếu, tái cơ cấu dự án, bảo vệ người mua | Nợ xấu có tài sản bất động sản, cơ chế mua bán nợ, dự án đóng băng, hồ sơ giàn khoan 2014 | Khớp chủ đề XI và gieo tiền đề Biển Đông | 2;7.1;7.2;7.4;B1 names/history anchors |
| XI12 | Trách nhiệm bên bảo lãnh trái phiếu | Trách nhiệm bên bảo lãnh tín dụng | Không để cụm trái phiếu còn sót ở XI | 7.4;B1 name;changelog |
| XII01–XII08 | Một dòng đầu ra | Đủ gate, caller, lựa chọn, trung tâm phản ứng và kết quả XIV | Hoàn thành 8 node XII | 7.4;B1 node_choice_prices/delays;script `--check-l2` |
| XIII01–XIII08 | Biển Đông, hợp tác và dữ liệu | Bốn node đầu tiếp tục hồ sơ biển; bốn node sau xử lý nghĩa vụ, cơ cấu hạn, người mua và bên phân phối/bảo lãnh trái phiếu | Chuyển cụm trái phiếu đến kỳ có khủng hoảng cuối 2022 | 2;7.1;7.4;11.3;B1 history anchors/names |
| XIV01–XIV08 | Một dòng đầu ra | Đủ gate, caller, lựa chọn, trung tâm phản ứng và kết quả XV giả định | Hoàn thành 8 node XIV | 7.4;B1 node_choice_prices/delays;script `--check-l2` |
| B1 | Chưa có giá theo từng node cho 40 event | Bổ sung bản đồ PP/ngân khố cho từng node; thêm các mốc lịch sử và thời lượng gameplay dùng ở lựa chọn | Giữ JSON làm nguồn giá duy nhất | `VIETNAM_POLITICAL_PARAMETERS_VI.json`;7.4;11.3 |
| Script/CSV | Chỉ dựng ma trận CSV Lượt 1 | Thêm `--check-l2` để đối chiếu 74 cost, 40 gate/caller/giá và thứ hạng chi phí ở k=20/40/60; `--csv-only` dựng lại CSV mà không ghi đè báo cáo Lượt 1 | Tính lặp lại được phép thử lựa chọn và tái tạo ma trận ngân sách | `VIETNAM_POLITICAL_BALANCE_VI.py`;`VIETNAM_POLITICAL_BALANCE_VI.csv`;11.3 |
| 12 | Ghi Lượt 2 chưa chạy | Ghi nội dung Lượt 2 đã làm, các FAIL Lượt 1 còn tồn tại, và giới hạn chưa triển khai | Không tuyên bố hoàn tất quá mức | 12 |

## Mục không đổi

Trong tài liệu thiết kế: mục 1; mục 3–6; mục 7.3, 7.5; mục 8–10; mục 11.1–11.2; và dòng `BLUF` cuối. Danh sách tham chiếu repo ở mục 9 không đổi. Tổng focus 74, cost của node và các tham chiếu kỹ thuật ở mục 9 được giữ. Các node IX09–XIV12 không nằm trong 40 node mục tiêu được khôi phục nguyên nội dung/cost/loại trừ; XI12 chỉ đổi cụm “trái phiếu” thành “tín dụng” để không mâu thuẫn với chuyển cụm.

CSV được dựng lại bằng `python VIETNAM_POLITICAL_BALANCE_VI.py --csv-only`: 1.296 hàng, 648 hàng hợp lệ, 74 node. Số liệu ma trận không đổi vì Lượt 2 không đổi giá chương trình hoặc E101–E104; 40 event/decision node mới được kiểm riêng, không được cộng nhầm vào cùng một event bundle.

## Bất biến I1–I10 sau Lượt 2

| Mã | Kết quả | Phép tính / căn cứ |
| --- | --- | --- |
| I1 | PASS | Cán bộ/công vụ/dân vận: chuẩn 660 > mốc 600 ≥ cấp tốc 555; kiểm tra: chuẩn 750 > mốc 690 ≥ cấp tốc 645. |
| I2 | PASS | 55−50=5 PP; chênh giá PP thuần đúng giới hạn 10. Giá trị còn lại được gọi tên là dự án phụ 270 ngày/30 PP. |
| I3 | FAIL tổng; PASS cho 40 node mới | `--check-l2` kiểm 40 cặp qua 3 tuyến × 3 mức r × k=20/40/60; ở từng node cả A lẫn B đều rẻ hơn trong ít nhất một mức k. Ví dụ X01: A/B = 20/(10,20,30); X03 = 30/(15,30,45). Nhưng E103-C vẫn rẻ hơn E103-B 15 PP trong ngoại lệ E102-C, cùng ngày/cohesion/cơ hội đã mô hình, nên I3 tổng chưa đạt. |
| I4 | PASS (theo Lượt 1) | Cổng cohesion sau trừ ≥40, hệ số giá 1.25/1.15/1.05/1.00/0.90; BoP +0.30→+0.20 khi trả đủ hai checkpoint. Lượt 2 không đổi số cân bằng này. |
| I5 | FAIL | Cohesion<20 làm kiểm tra chuẩn 750+60=810 ngày; dự phòng 900−810=90 <100. Các ngoại lệ E102-C/E103-B/C ở ngày 840/825 cũng chỉ có 60/75 ngày dự phòng (central fast 735 có 165). Các ngoại lệ này chưa thỏa cách viết I5 nghiêm ngặt 100 ngày cho mọi chuỗi. |
| I6 | PASS | Script đếm 74 cost khớp JSON B1; 40 node mục tiêu đều có cost, gate, caller, hai lựa chọn có giá khác loại và hậu quả nhiệm kỳ kế tiếp. Không thêm node. |
| I7 | FAIL/chờ Lượt 3 | 40 nhãn node hiện có trong B1; không tạo technical event/flag/variable ID mới. Tuy nhiên registry ở mục 8.1 chưa được rà và đồng bộ sau đặc tả caller, phải hoàn tất ở Lượt 3. |
| I8 | PASS | Nợ xấu/VAMC năm 2013: Nghị quyết 02/NQ-CP và thông tin VAMC; giàn khoan: nguồn Bộ Ngoại giao Việt Nam ghi phát hiện 01/05 và hạ đặt 02/05/2014; trái phiếu: IMF ghi phát hành dừng đột ngột từ cuối 2022 và thị trường đóng băng quý IV/2022. Event lựa chọn/nhân vật không được dựng như lịch sử. |
| I9 | PASS | Đã chạy phép tính script; không chạy HOI4, console hoặc playtest. |
| I10 | FAIL/chưa đủ mô hình | Ma trận Lượt 1 có 0 tổ hợp thống trị trong các k/r đã mô hình, nhưng chưa ghép 40 lựa chọn mới với PP ròng/ngày/cohesion/cơ hội của từng tổ hợp; cần audit Lượt 3. |

### Phép tính giá của event mới

Chi trực tiếp `PP + ngân khố × k`; giá trị cohesion mất bằng 0 trong các cặp mới. Với cặp A=20 PP, B=0.50 ngân khố: A/B lần lượt 20/10, 20/20, 20/30 ở k=20/40/60. Với A=25 PP, B=0.75 ngân khố: 25/15, 25/30, 25/45. Vì hai lựa chọn đảo thứ hạng theo k, chọn phương án rẻ nhất luôn không dẫn đến cùng một phương án ở mọi k. Tỷ lệ r và tuyến không làm đổi chi phí lựa chọn; script đã chạy đủ ba giá trị r và ba tuyến để kiểm chứng điều đó.

## Điểm chưa chắc / cần quyết định

1. **E103-B và E103-C:** muốn I3 tổng PASS, cần quyết định giá E103-C có thêm khoản ngân khố hay tạo lợi ích/chi phí khác biệt có thể đo được cho hợp đồng B. Chưa tự thay giá của Lượt 1.
2. **Dự phòng I5:** chốt cách xử lý chuỗi full 810 ngày ở cohesion<20 và các đường E102-C ngày 825/840. Nếu áp dụng I5 tuyệt đối, các đường 825/840 phải thành partial hoặc cần rút ngắn thời gian; hiện chưa tự nới ngoại lệ đã ghi trước đó.
3. **I10:** trước khi PASS cần đưa lựa chọn node vào mô hình đầy đủ hoặc ghi rõ phạm vi nào không thuộc tổ hợp mạnh nhất; hiện chỉ có kiểm chéo giá trực tiếp.
4. Các số giá node mới đã đưa vào B1; nội dung event mới vẫn là thiết kế giấy. Chưa có API/idea/focus game files hoặc định danh kỹ thuật được xác minh.

## Xác minh lịch sử

- Chính phủ Việt Nam, Nghị quyết 02/NQ-CP ngày 07/01/2013 về hỗ trợ sản xuất, thị trường và xử lý nợ xấu: [cổng Chính phủ](https://en.baochinhphu.vn/solutions-to-remove-difficulties-against-production-and-business-support-the-market-and-deal-with-bad-debts-11115783.htm).
- Chính phủ mô tả thị trường bất động sản đóng băng trong tháng 01/2013: [cổng Chính phủ](https://en.baochinhphu.vn/rescuing-estate-market-benefits-the-poor-11115890.htm).
- VAMC được thành lập và bắt đầu hoạt động 09/07/2013: [cổng Chính phủ](https://en.baochinhphu.vn/asset-management-company-established-11117099.htm).
- Bộ Ngoại giao Việt Nam về HYSY-981, phát hiện 01/05 và hạ đặt 02/05/2014: [Bộ Ngoại giao](https://mofa.gov.vn/web/ministry-of-foreign-affairs/detail/chi-tiet/contents-of-the-international-press-conference-on-developments-in-the-east-sea-june-5th-2014-51.html).
- IMF ghi nhận phát hành trái phiếu doanh nghiệp dừng đột ngột từ cuối 2022, thị trường đóng băng quý IV/2022: [IMF Country Report 23/338](https://www.imf.org/-/media/files/publications/cr/2023/english/1vnmea2023003.pdf).

BLUF

<!-- SNAPSHOT_L2_END -->

</details>

<!-- HISTORICAL_REVIEW_ARCHIVE_END -->

BLUF
