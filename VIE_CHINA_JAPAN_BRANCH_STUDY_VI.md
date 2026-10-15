# Nghiên cứu một cụm ngoại giao Trung Quốc: Trung–Nhật → bài học cho Việt–Trung

> **Sau nghiên cứu:** người dùng đã yêu cầu bỏ giới hạn sáu node C và phát triển nội dung. Xem [đặc tả C mở rộng](VIE_CHINA_EXPANDED_BRANCH_DESIGN_VI.md). Phương án sáu vị trí ở mục 10 dưới đây là đề xuất cũ đã bị thay về phạm vi; phần phân tích code Trung–Nhật vẫn giữ làm bằng chứng, không đổi nguồn Trung Quốc.

**Bước hiện tại: phân tích mẫu trước khi thiết kế lại C.** Cụm được chọn là Trung–Nhật trong Ngoại giao khu vực Trung Quốc. Chưa sửa catalog 51 node, giá, layout hoặc gameplay Việt Nam. L1 vẫn mở, J2/J5 vẫn FAIL theo hồ sơ đã bàn giao; đây không phải chuyển sang L2 hoặc triển khai L3.

Điểm cần học là cách một bài toán quan hệ được phát triển thành **lựa chọn chiến lược → công cụ có phản ứng → kết quả giữ dấu vết lựa chọn**. Sáu focus C hiện tại chủ yếu mô tả các bước tổ chức một chương trình thương mại. Chúng đã có quyền chọn gói trong event, nhưng chưa thể hiện các con đường chính sách khác nhau trên cây.

## 1. Nguồn thực và giới hạn

Đọc bản MD tại `D:/ide/Millennium-Dawn`; đường Workshop của báo cáo trước không tồn tại ở phiên này. File focus vẫn có 558 focus; script trích riêng 18 focus từ `CHI_the_japan_question` tới trước `CHI_Form_the_SCO`. Các tên chính sách trong nghiên cứu này là nội dung **kịch bản mod**, không được dùng làm chứng cứ lịch sử.

| Thành phần | Nguồn đã đọc | Vai trò |
|---|---|---|
| Cây | [05_china.txt](<D:/ide/Millennium-Dawn/common/national_focus/05_china.txt:12365>) | Focus, mutex, AND/OR, available, reward, tọa độ |
| Event | [05_china.txt](<D:/ide/Millennium-Dawn/events/05_china.txt:5874>) | Phản ứng CHI/JAP/USA; trả lời Tokyo tại `.224` |
| Decision | [05_CHI_decisions.txt](<D:/ide/Millennium-Dawn/common/decisions/05_CHI_decisions.txt:6254>) | Công cụ hai bên trong category Nhật |
| Category | [99_CHI_decision_categories.txt](<D:/ide/Millennium-Dawn/common/decisions/categories/99_CHI_decision_categories.txt:90>) | Cùng category cho CHI và JAP |
| Idea | [05_china.txt](<D:/ide/Millennium-Dawn/common/ideas/05_china.txt:1566>) | Lợi ích, đánh đổi và điều kiện mất lợi ích |
| Dynamic modifier | [99_CHI_dynamic_modifiers.txt](<D:/ide/Millennium-Dawn/common/dynamic_modifiers/99_CHI_dynamic_modifiers.txt:213>) | Tác dụng thật của cấm vận, hợp tác công nghiệp |
| Influence trigger | [00_influence_scripted_triggers.txt](<D:/ide/Millennium-Dawn/common/scripted_triggers/00_influence_scripted_triggers.txt:212>) | Phân biệt ROOT trong focus với FROM ở event nhận |

SHA-256 đầy đủ và trích đoạn có dòng nguồn nằm trong [evidence.json](artifacts/china_japan_reference/evidence.json). Focus/event hiện tại **khác SHA** của snapshot ở mục 16.5 báo cáo Trung Quốc. Đặc biệt, `CHI_assuage_japanese_concerns` hiện **không còn** gate `CHI_JAP_threat_reduction`; không lặp lại kết luận tự khóa cũ như một lỗi còn tồn tại ở bản này. Báo cáo cũ được giữ nguyên.

## 2. Bài toán nội dung của cụm mẫu

Đích cuối được kịch bản mod đặt ra là giảm hiệu lực chuỗi đảo thứ nhất qua thay đổi vị thế Nhật. Đó là một đích chiến lược cụ thể, có hai cách tạo đòn bẩy:

| Tuyến | Cách tạo đòn bẩy | Nhật có thể phản ứng ra sao? | Hậu quả ở cuối |
|---|---|---|---|
| Historical Reckoning | Huy động lịch sử, tuyên bố chủ quyền, hoạt động trên biển và gây sức ép kinh tế | Nhượng bộ, tăng khả năng chống chịu, tăng hiện diện, mở kênh xuống thang; có tương tác với Mỹ | Focus cuối có nhánh chuyển state/core và áp trung lập cưỡng ép trong kịch bản |
| Fukuda Doctrine Revisited | Văn hóa, thương mại, đầu tư, giảm lo ngại và tác động quan hệ Nhật–Mỹ | Nhận/không nhận từng tiếp xúc; Tokyo có nhận đầy đủ, nhận một phần, từ chối | Focus cuối áp kết quả khác với tuyến đối đầu; một số lợi ích hợp tác có điều kiện mất |

Độ dày nội dung không đến riêng từ số node. Một hành động làm thay đổi vấn đề mà người chơi phải giải tiếp: gây sức ép có thể khiến bên nhận đầu tư chống chịu; tiếp cận kinh tế cần môi trường quan hệ phù hợp; đề nghị chính trị phải được bên nhận trả lời. Tuy vậy, chất lượng thực thi các phản ứng không đồng đều, như mục 8 chỉ ra.

Việt–Trung cần một mục tiêu phù hợp vai trò Việt Nam. Không sao chép mục tiêu kiềm chế Nhật, chuyển lãnh thổ hoặc ép trung lập của cây Trung Quốc vào nhánh hợp tác Việt Nam.

## 3. Phân rã đủ 18 focus

Mã J01–J18 chỉ dùng trong nghiên cứu, không phải ID mới. ID nguồn, cost, anchor và tọa độ có đầy đủ trong [bảng trích tự động](artifacts/china_japan_reference/extracted_layout.md) và [focus.csv](artifacts/china_japan_reference/focus.csv).

| Mã | Nội dung đọc từ focus | Chức năng trong trải nghiệm |
|---|---|---|
| J01 | The Japan Question | Đặt vấn đề, gọi event Nhật và mở phạm vi category |
| J02 | Historical Reckoning | Cam kết tuyến gây sức ép; mutex với J10 |
| J03 | Nanjing Memorial Mandate | Nền huy động chính trị cho công cụ lịch sử |
| J04 | Diaoyu Sovereignty Declaration | Tuyên bố, phản ứng Nhật, quyền tuần tra |
| J05 | Rare Earth Lever | Quyền dùng công cụ cấm vận kinh tế |
| J06 | Yasukuni Protest Doctrine | Vận dụng tuyến lịch sử, có phản ứng và xuống thang |
| J07 | Maritime Militia Initiative | Công cụ hiện diện; decision triển khai/rút |
| J08 | Anti-Japanese Boycott Campaign | Gây sức ép kinh tế, phản ứng chấp nhận thiệt hại/nhượng bộ |
| J09 | Senkaku Crisis | Gom ba tuyến gây sức ép; mở event khủng hoảng có các cách xử lý |
| J10 | Fukuda Doctrine Revisited | Cam kết tuyến tiếp cận; mutex với J02 |
| J11 | Panda Diplomacy Renewal | Xây nền tiếp xúc văn hóa, có phản ứng Nhật |
| J12 | RCEP Acceleration | Xây trục thương mại; mở decision thực hiện |
| J13 | Assuage Japanese Concerns | Trục giảm lo ngại/công nghiệp; mở các công cụ tiếp theo |
| J14 | Anime Generation Gambit | Phát triển trục văn hóa từ J11 |
| J15 | China Plus One Counteroffensive | Khai thác trục đầu tư từ J12 |
| J16 | Quad Wedge Strategy | Cần J13 AND J14; đưa Mỹ vào vòng phản hồi |
| J17 | Tokyo Communiqué | Gom các trục tiếp cận, gửi đề nghị có ba mức trả lời |
| J18 | Break the First Island Chain | OR hai đường tới kết quả; available đọc kết quả, reward phân nhánh |

Tổng cost của catalog là 95 nhưng **không phải một đường chơi hợp lệ**, vì J02 và J10 loại trừ nhau. Script tính các tổ tiên bắt buộc từ J01 tới J18: đường qua J09 có cost 51, đường qua J17 có cost 59; đều gồm 10 focus. Chưa tính gốc ngoại giao ngoài cụm, decision, chờ phản hồi hoặc gate bên ngoài. Không quy cost thành ngày khi chưa kiểm cơ chế thời gian tương ứng của MD. [Phép tính đường đi](artifacts/china_japan_reference/route_costs.csv).

## 4. Mutex, AND và OR nằm ở đâu?

### 4.1. Mutex là quyết định chính sách đọc được trên cây

J02 và J10 khai báo `mutually_exclusive` hai chiều. Người chơi chọn cách tiếp cận quan hệ, rồi phát triển các công cụ thuộc cách đó. Ba trục con trong mỗi cánh là công cụ bổ sung, không mutex với nhau.

Một cặp mutex trên cây khác với option loại trừ tại một event. Mutex khóa tiến trình focus thay thế; option chọn gói chỉ quyết định cam kết của một lượt/chương trình nếu thiết kế cho phép đàm phán lại. Cụm C hiện có loại lựa chọn thứ hai, thiếu loại thứ nhất. Không nên gọi C hiện tại hoàn toàn không có lựa chọn, nhưng người xem cây đúng là chưa thấy một lựa chọn đường lối.

### 4.2. OR thật nằm ở hội tụ J18

Code có **một** block prerequisite chứa J17 và J09:

```pdx
prerequisite = {
    focus = CHI_the_tokyo_communique
    focus = CHI_the_senkaku_crisis
}
```

Đây là OR thật. Không phải hoàn thành cả hai cánh đang mutex. Sau prerequisite, `available` vẫn cần kết quả thích hợp:

- Tuyến đối đầu: đã chọn J02 và làm J09; Mỹ chưa can thiệp hoặc Nhật là subject của CHI.
- Tuyến thực dụng: đã chọn J10 và có `tokyo_communique_signed` OR `tokyo_communique_partial`.
- Ngoài hai tuyến còn có điều kiện chung về chính phủ Nhật và ảnh hưởng của CHI tại Nhật.

Vì vậy **focus gửi đề nghị không tự bằng thành công**. Tuyến Tokyo phải có phản hồi được chấp nhận; từ chối chưa mở capstone. Tuyến đối đầu kiểm kết quả lỏng hơn: việc Mỹ chưa can thiệp không tự chứng minh Nhật đã nhượng bộ. Đây là chỗ Việt Nam cần làm chặt hơn, không lấy toàn bộ gate mẫu làm chuẩn.

### 4.3. “Hai trong ba” không phải OR thay thế trong bản hiện tại

J09 có ba block prerequisite riêng từ J06/J07/J08. J17 cũng có ba block riêng từ J14/J15/J16. Dù `available` đếm hai trong ba, người chơi vẫn phải đủ cả ba tiền đề. Ở J09, đạt áp lực thay thế cũng không bỏ các prerequisite.

Script đã liệt kê các tổ hợp trong [gate_truth_table.csv](artifacts/china_japan_reference/gate_truth_table.csv): hai trục hoàn thành vẫn FAIL prerequisite, ngay cả khi điều kiện đếm đạt. Phép tính chỉ giữ các gate bên ngoài ở trạng thái đạt và không xét bypass; không phải mô phỏng engine.

Nếu muốn “một trong hai cách làm” cho Việt Nam, phải có OR đúng ở đồ thị hoặc hai option dẫn đến kết quả riêng. Không đặt AND trước rồi viết tooltip “chọn một” phía sau.

## 5. Vì sao decision làm quan hệ có chiều sâu?

Category `CHI_japan_strategy` có 31 decision: 12 công cụ/ứng phó và 19 lời mời doanh nghiệp. Không đồng nghĩa 31 cơ chế đều cần được sao chép. Bảng dưới tập trung vào những chức năng khác nhau; giá và timer là **số đọc từ Trung Quốc**, không phải tham số đề nghị cho Việt Nam.

| Công cụ/đối ứng | Chủ thể | Giao dịch/lịch trong code | Tác dụng làm thay đổi lựa chọn |
|---|---|---|---|
| Kích hoạt / gỡ cấm vận đất hiếm | CHI | Kích hoạt 100 PP; gỡ 0 PP | Duy trì hoặc rút một biện pháp cụ thể; modifier ở capital state Nhật, không phải toàn thị trường |
| Nhượng bộ yêu cầu / đa dạng hóa đất hiếm | JAP | Nhượng bộ 200 PP; đa dạng hóa 100 PP, `days_remove=365`, dùng hai civilian factories khi decision hoạt động | Hai cách đáp lại sức ép: chịu tổn thất chính trị để chấm dứt ngay, hoặc chịu chi phí thích nghi để chặn công cụ về sau |
| Tuần tra | CHI | 50 PP; `days_re_enable=90` | Tăng áp lực; lần đầu gửi một yêu cầu tới Nhật |
| Triển khai / rút dân quân biển | CHI | Triển khai 75 PP; rút 0 PP | Thay trạng thái hiện diện và modifier state cụ thể |
| Tăng cường lực lượng / kênh hậu trường | JAP | Lần lượt 50 PP, cooldown 90; 75 PP, cooldown 180 | Một công cụ tăng áp lực; công cụ kia giảm áp lực, cần kênh đã mở |
| Thúc đẩy RCEP | CHI | 75 PP; `days_remove=180` | `remove_effect` cấp idea; focus mở quyền khác với hoàn tất action |
| Hủy diễn tập | CHI | 30 PP; cooldown 60; trừ 5 Army XP | Đổi một năng lực/chi phí cụ thể để giảm aggression và cải thiện quan hệ |
| Họp kênh song phương | CHI | 50 PP; cooldown 365 | Thay quan hệ Nhật–Mỹ/Trung, không tự bằng Nhật ký Tokyo |

Điểm đáng học nhất là **bên nhận cũng có công cụ**. Người chơi không chỉ bấm một lựa chọn rồi nhìn thanh quan hệ tăng. Ví dụ đất hiếm có hành động gây sức ép, phản ứng chịu nhượng bộ/thích nghi và đường gỡ biện pháp. Không gọi hai decision Nhật là mutex engine: chúng là các đường kết thúc thay thế nhờ trạng thái, không có cặp `mutually_exclusive` như focus.

`days_remove` và `days_re_enable` được giữ đúng tên trường trong dữ liệu; chưa kiểm engine nên không đánh đồng mọi timer với thời gian xây dự án hay cooldown.

## 6. Kiến trúc caller → phản hồi → reader

| Caller | Event và scope nhận | Quyết định/kết quả thực | Reader sau đó |
|---|---|---|---|
| J01 | `.250` tại JAP | Một option cấp spirit áp lực lịch sử | Bối cảnh quan hệ; không phải một cuộc đàm phán nhiều lựa chọn |
| J09 | `.200` tại CHI, có thể gọi `.201` tại JAP và `.215` tại USA | CHI chọn xử lý; JAP có chuyển state, phản kháng hoặc tìm bảo đảm; USA có phản ứng can thiệp | J18 đọc trạng thái can thiệp của Mỹ trên CHI |
| J10/J11/J13 | `.220/.221/.222` tại JAP | Nhận hoặc không nhận tiếp xúc; hiệu ứng quan hệ/ảnh hưởng khác nhau | Gate/idea tiếp theo; phải phân biệt phần focus đã cấp với phần event mới cấp |
| J16 | `.223` tại USA | Mỹ tái khẳng định hoặc giảm gắn kết; cờ nằm trên USA | J18 có reader tương ứng, nhưng đang lệch scope như mục 8 |
| J17 | `.224` tại JAP | Full: idea và NAP, CHI nhận cờ signed. Partial: NAP/quan hệ, CHI nhận cờ partial. Reject: tăng aggression phía CHI | J18 nhận full OR partial; `.206/.226/.227` là thông báo tới CHI |
| Mời doanh nghiệp | Ví dụ `.231/.244` tại JAP | Các event mẫu đã đọc chỉ có một option nhận hiệu ứng Nhật | Không được trình bày lời mời này như một vòng thương lượng có quyền từ chối |

Hai loại phản ứng thật sự khác cấu trúc: khủng hoảng mở chuỗi nhiều chủ thể; Tokyo nhận một đề nghị và phân kết quả ba mức. Không cần mọi chương trình cùng một khuôn “gửi–đợi–trả phí tháng”.

Tokyo cũng cho thấy một giới hạn: full và partial có thưởng ban đầu khác nhau, nhưng đoạn reward J18 theo cánh Fukuda không phân tiếp full/partial. Không khẳng định mọi khác biệt phản hồi đều được giữ ở phần thưởng cuối. Với Việt Nam, công nhận cả hai cách thành công vẫn phải giữ phạm vi, nghĩa vụ và quyền tiếp theo khác nhau.

`influence_higher_70` trong focus kiểm ROOT; `sender_influence_higher_70` tại event kiểm FROM và phần tử đầu của mảng ảnh hưởng. Đây không chỉ là opinion cao. Chưa mô phỏng mảng/runtime nên không diễn giải thành xác suất chấp thuận cố định. Việt Nam chỉ nên đọc một yếu tố có provider, nội dung và quyền phản hồi đã xác định.

## 7. Layout truyền đạt tiến trình gì?

Tọa độ tuyệt đối đã được script cộng dồn từ anchor. Không đo theo vị trí Mermaid tự sắp xếp.

| Hàng Y thật | Cánh trái | Cánh phải | Ý nghĩa bố cục |
|---|---|---|---|
| 1 | — | J01 tại X83 | Một vấn đề chung |
| 2 | J02 tại X80 | J10 tại X86 | Hai cam kết mutex, cân hai phía gốc |
| 3 | J03/J04/J05 tại X78/80/82 | J12/J11/J13 tại X84/86/88 | Mỗi cam kết mở một dải công cụ ngang |
| 4 | J06/J07/J08 tiếp các cột | J15/J14 phát triển kinh tế/văn hóa | Hành động sâu thêm đúng chức năng |
| 5 | J09 tại X80 | J16 tại X88 | Bên trái gom khủng hoảng; bên phải thêm phản ứng bên thứ ba |
| 6 | — | J17 tại X86 | Đề nghị Tokyo sau tích lũy đòn bẩy |
| 7 | J18 tại X83, giữa hai cánh | — | Hội tụ OR, về lại trục gốc |

[Sơ đồ đủ node và bảng tọa độ sinh từ code](artifacts/china_japan_reference/extracted_layout.md).

Bố cục có logic thị giác: **tách cam kết → mở công cụ → gom kết quả → trở về trục giữa**. Hai cánh không cần có cùng số tầng. Nhìn cây đã thấy người chơi đang đi con đường nào; event làm dày cách dùng công cụ trong đường đó.

Kiểm nguồn cho thấy gap cùng hàng nhỏ nhất 2, các con thấp hơn cha. Tuy nhiên có **9 anchor không phải prerequisite trực tiếp**: nhiều node neo về gốc cánh để giữ cột thay vì cha trực tiếp. Đây không tự chứng minh lỗi engine; nó không đạt quy ước anchor của repo Việt Nam. Khi áp dụng cho VIE, giữ tọa độ tuyệt đối mong muốn rồi tính lại offset từ cha trực tiếp đã khai báo trước. Không sao chép nguyên anchor mẫu.

Chưa kiểm sprite, hộp tên, dây vẽ trong engine hoặc bố cục đối với các cụm CHI bên cạnh; bảng trên không thay nghiệm thu UI.

## 8. Bẫy phải tách khỏi bài học tốt

| Phát hiện ở bản đang đọc | Bằng chứng cụ thể | Quy tắc cho Việt Nam |
|---|---|---|
| “Hai trong ba” vẫn cần đủ ba | Ba prerequisite block ở J09/J17 | Luật đồ thị và tooltip phải cùng nghĩa |
| Cờ phản ứng Mỹ lệch scope | `.223` nhận tại USA và `set_country_flag` tại scope gốc USA; J18 kiểm `has_country_flag` không scope USA, trong focus CHI | Ghi/đọc cùng chủ thể; chưa coi hai nhánh thưởng theo cờ này hoạt động đúng |
| Thưởng hợp tác có phần cấp trước phản hồi | J13 áp hai dynamic modifier, kể cả phía JAP, trong reward focus; `.222.b` không gỡ chúng tại option đã đọc | Chấp thuận và bàn giao phải có owner riêng, không cấp thưởng song phương chỉ vì gửi |
| “Mời” không phải đàm phán đầy đủ | Decision Mitsubishi cấp bonus/công trình ngay, sau đó gọi `.231` có một option | Không thêm event có hình thức phản hồi nhưng không có quyền chọn |
| Cửa mời doanh nghiệp có thể xuất hiện trước nền dự định | Category mở bởi J01; decision mẫu chỉ kiểm Nhật/ý kiến/hòa bình/count, không kiểm completed J13; count chưa set thường đọc 0 | Kiểm đường mở category và từng action, không tin tooltip unlock là gate thật |
| OR hội tụ không bảo đảm kết quả chặt ở mọi cánh | Cánh khủng hoảng J18 dùng “Mỹ chưa can thiệp hoặc Nhật là subject” | C6 phải đọc thành quả đúng mục tiêu, không chỉ “chưa có cờ thất bại” |
| Một số lợi ích dễ mất bởi nguồn chung | Idea văn hóa/investor/understanding bị cancel khi aggression vượt ngưỡng riêng | Tooltip chỉ rõ nghĩa vụ; không nhập biến aggression chung mới cho VIE |
| Bản cũ và bản mới khác nhau | J13 đã bỏ gate threat reduction ở nguồn hiện tại | Mỗi kết luận gắn source/hash; không sửa upstream hoặc báo cáo cũ |

Các điểm trên là nhận xét từ cấu trúc đã đọc, không phải lỗi đã tái hiện trong HOI4. Không sửa Trung Quốc trong đợt nghiên cứu này.

## 9. Cụm Việt–Trung hiện tại thiếu gì khi đặt cạnh mẫu?

Đọc [catalog và đặc tả C hiện hành](VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md#16-catalog-51-focus-đề-xuất-và-đồ-thị-nội-bộ): C1 mở hợp tác; C2 chuẩn bị; C3 đối thoại; C4 mở đề nghị; C5 dự phòng; C6 công nhận kết quả.

| Mặt thiết kế | Trung–Nhật | Việt–Trung hiện tại | Nhận định |
|---|---|---|---|
| Đích đến | Một biến đổi chiến lược, hai cách tạo đòn bẩy | Một chương trình thương mại vận hành | C có mục tiêu rõ nhưng hẹp; chưa đủ làm đại diện cho chiều sâu cả quan hệ |
| Cam kết thấy trên cây | J02 mutex J10 | Không mutex trong toàn catalog | Hai gói C là quy mô, chưa là hai chính sách khác nhau |
| Tổ chức công cụ | Các trục lịch sử/biển/kinh tế hoặc văn hóa/đầu tư/bảo đảm | Chuẩn bị và đối thoại đều bắt buộc trước C4 | Chọn thứ tự hai focus không đổi cách đạt mục tiêu |
| OR nội bộ | J18 nhận J09 OR J17 | C không có OR prerequisite; C6 chỉ sau C4 | OR giữa gói đã bàn giao chỉ nằm trong available; cùng một đường focus |
| Quyền đối tác | Phản ứng nhiều chủ thể, công cụ phía JAP | Full/partial/sửa/từ chối đã có, nhưng chưa có yếu tố riêng của CHI được chốt | Giao thức khá rõ; nội dung thương lượng/động cơ đối tác còn mỏng |
| Dự phòng | Có hành động rút biện pháp và phản ứng thích nghi | Giảm phạt chậm phối hợp | C5 có tác dụng nhưng chưa tạo một cách tiếp tục/đạt kết quả khác |
| Hội tụ | OR hai tuyến; thưởng theo tuyến | C6 đọc chương trình đã hoạt động, không thưởng lại | Guard cấp thưởng C tốt; kết quả/đường đi thiếu đa dạng |

**Nhận định:** điểm yếu chính là cây C đang trình bày workflow thay vì lựa chọn chính sách. Bổ sung thêm event nhỏ/lớn hoặc một cặp mutex chỉ đổi bonus sẽ chưa sửa được điều này.

## 10. Nên áp dụng điều gì cho Việt Nam ở bước thiết kế kế tiếp?

Chỉ là kết luận nghiên cứu, **chưa thay bất kỳ node nào** và không tự chốt chính sách mới.

1. **Viết một bài toán Việt–Trung trước khi vẽ lại.** Giữ thành quả hợp tác có ích và quyền xử lý gián đoạn; xác định điều gì thực sự cần người chơi lựa chọn về quyền/nghĩa vụ. Không thay bằng bài toán lãnh thổ do chính trị đang sở hữu.
2. **Chọn cặp cam kết đủ lý do mutex.** Hướng đáng xét là hai cách tổ chức cùng một chương trình: quy trình song phương ràng buộc chung, hoặc hợp tác chọn lọc giữ quyền rà soát riêng. Phải viết rõ quyền ai chấp thuận thay đổi, quyền rút, khả năng yêu cầu đối tác xem xét lại và phần cam kết không thể đồng thời có. Nếu viết ra vẫn có thể cùng tồn tại, không ép mutex để làm cây trông phân nhánh.
3. **Tách trục chính sách khỏi quy mô nhỏ/sâu.** Gói sâu vẫn đọc gate cohesion đã chốt. Không tự biến cặp thí điểm/mở rộng hiện tại thành hai focus khóa vĩnh viễn, vì thiết kế cho phép nâng gói.
4. **Tạo OR nơi có hai thành quả thay thế thật.** Cả hai phải đạt mục tiêu đã định nghĩa, có chứng cứ bàn giao; chuẩn bị dự phòng đơn thuần không được gọi thành công song phương. Dự phòng vẫn có thể đi cùng mọi đường hợp tác.
5. **Dùng decision cho cách vận dụng cam kết.** Đối thoại, sửa phạm vi, chấp nhận nghĩa vụ bổ sung hoặc kết thúc phải thay một quyền/nghĩa vụ cụ thể. Mỗi option cần trả lời “sau chọn này, option nào lần sau có/không còn?”. Không lấy tên cờ cơ hội làm chiều lợi ích.
6. **Bố trí từ lựa chọn tới kết quả.** Cam kết thay thế đặt cạnh nhau cùng hàng; các công cụ thuộc cam kết ở phía dưới; node OR ở trục giữa, thấp hơn mọi cha. Đối thoại/dự phòng bổ sung không bị đặt bên cánh đối lập để ngụ ý chúng không đi cùng hợp tác.

Với giới hạn **6 node C**, có thể xét cấu trúc chức năng **mở vấn đề + hai cam kết thay thế + một điểm OR mở thực hiện + một công cụ dự phòng chung + một hội tụ kết quả**. Đây là cách phân bổ sáu vị trí để viết thử, không phải catalog đã chốt. Hai cam kết vẫn phải vượt kiểm nội dung ở ý 2; phần chuẩn bị/đối thoại chỉ được chuyển sang hành động khi chúng còn có kết quả thực và gate đạt được. Không tăng tổng 51 focus hoặc tự đổi cost/layout để ghép mẫu này vào plan.

Trình tự cần duyệt kế tiếp là **mục tiêu → hai cam kết và đánh đổi → hành động/đối tác phản hồi → kết quả hợp lệ → AND/OR/mutex → layout**. Chưa chọn giá mới, định giá lợi ích hoặc cân bằng ở nghiên cứu này.

## 11. Đầu ra, kiểm chứng và phần giữ nguyên

- [Script trích nguồn](tools/analyze_china_japan_reference.py): parser giữ chuỗi có `#`/ngoặc, đọc block thật, cộng anchor và xuất bảng kiểm.
- [Bảng node/đồ thị/layout](artifacts/china_japan_reference/extracted_layout.md); [CSV focus](artifacts/china_japan_reference/focus.csv); [CSV decision](artifacts/china_japan_reference/decisions.csv).
- [Bảng chân trị gate](artifacts/china_japan_reference/gate_truth_table.csv); [cost đường đi](artifacts/china_japan_reference/route_costs.csv); [manifest/trích đoạn nguồn](artifacts/china_japan_reference/evidence.json).

Tái tạo:

```powershell
python -X utf8 tools/analyze_china_japan_reference.py --md D:/ide/Millennium-Dawn
```

Script đã chạy trên nguồn thật: 18 focus, một cặp mutex, 24 cạnh prerequisite tính cả cạnh từ root ngoài cụm, 31 decision. Gap node cùng hàng đạt 2; có 9 anchor lệch quy ước cha trực tiếp của VIE. Phép kiểm này chỉ đọc block/gate; chưa kiểm UI, routing scope hoặc gameplay engine.

**Không đổi:** plan chính và B1/registry; hồ sơ L1; toàn bộ source Trung Quốc/chính trị; focus/decision/event/loc game; SVG/PNG hiện có; giá/timer và tổng 51 node. Chỉ thêm nghiên cứu, script và các bản xuất bằng chứng. Không đổi nghĩa các bất biến hoặc dùng nghiên cứu mẫu để đóng L1.
