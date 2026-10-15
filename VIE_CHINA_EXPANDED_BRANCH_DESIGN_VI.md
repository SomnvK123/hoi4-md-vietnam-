# Việt–Trung mở rộng — quan hệ láng giềng, giao thương và xử lý bất đồng

**Bản phát triển nội dung theo yêu cầu bỏ giới hạn sáu node C.** Đề xuất hiện tại có **18 focus C**; nếu giữ nguyên các cụm khác, tổng nhánh là **51 − 6 + 18 = 63 focus**, tăng 12. Đây là số đếm do script lấy từ catalog, không phải yêu cầu phải dùng đủ số node của mẫu Trung Quốc. Nội dung và định danh mới vẫn là đề xuất để xét duyệt, chưa là gameplay đã được chốt hoặc triển khai.

Tài liệu này là đặc tả C mở rộng hiện hành để review. Mục 13–14/17.1 và sáu node C trong plan tổng là **baseline trước mở rộng**; bảng 51 node/SVG cũ không chứng nhận bố cục mới. Chưa hợp nhất toàn bộ các bản cũ, chưa sang cân bằng L2; L1 vẫn mở với J2/J5 FAIL. Chỉ yêu cầu giữ sáu node C được thay bởi chỉ đạo mới; không tự sửa nội dung sáu cụm còn lại.

Nguồn nội dung/kiến trúc: [nghiên cứu Trung–Nhật](VIE_CHINA_JAPAN_BRANCH_STUDY_VI.md), [plan nền](VIE_REGIONAL_DIPLOMACY_CODE_PLAN_VI.md), [giao diện và ownership L1](VIE_REGIONAL_DIPLOMACY_L1_REVIEW_VI.md). **Mọi chương trình, tình huống và cam kết mới bên dưới là giả định gameplay**; không gọi bằng tên hiệp định thật, không thêm ngày hoặc nhân vật lịch sử.

## 1. Trải nghiệm chủ đạo

Người chơi cần đưa quan hệ Việt–Trung từ các đầu mối liên lạc thành những cơ chế thực sự dùng được: hàng hóa đi theo phạm vi hai bên đã nhận; vụ việc dân sự có đầu mối xác minh và bàn giao; khi xảy ra vướng mắc, biết phần nào còn hoạt động, điều kiện nào phải thương lượng lại và có thể phục hồi theo căn cứ nào.

Nhánh có bốn mảng bổ sung cho nhau:

| Mảng | Câu hỏi của người chơi | Thành công quan sát được |
|---|---|---|
| Giao thương | Dùng quy trình chung hay xác nhận riêng từng phạm vi? | Một trong hai chế độ được CHI chấp thuận và triển khai thật |
| Tham vấn | Đầu mối kỹ thuật có đủ thẩm quyền giải quyết bất đồng không? | Có đường làm rõ, sửa điều kiện hoặc kết thúc; giải pháp được đúng hai bên nhận |
| Dân sự–lãnh sự biên giới | Một hồ sơ được xác minh và chuyển cho ai, theo quyền nào? | Cơ chế dân sự hoặc lãnh sự được đưa vào sử dụng; không chỉ một lần gửi event |
| Dự phòng và phục hồi | Duy trì phần nào khi giao thương gián đoạn? | Chuẩn bị trong nước có tác dụng giảm tổn thất; nối lại dựa trên thỏa thuận còn hiệu lực |

Mục tiêu cuối C18 cần **giao thương vận hành AND một cơ chế dân sự/lãnh sự hoạt động**. Không bắt xảy ra khủng hoảng để hoàn thành nhánh. C16/C17 là nội dung có điều kiện khi người chơi thực sự trải qua gián đoạn, không phải các focus bắt buộc phải dựng một thất bại giả mới làm được.

## 2. Catalog, đồ thị và layout có nguồn duy nhất

Catalog máy đọc đặt trong [registry B1](VIE_REGIONAL_DIPLOMACY_PARAMETERS_VI.json), khóa `design_variants.C_expanded`. Không tạo bảng số kinh tế thứ hai. Cost đọc `focus.cost_values` của cùng registry; không thêm giá, timer hay trần modifier.

**[Catalog đủ 18 node, đồ thị Mermaid và tọa độ](artifacts/vie_china_expanded/catalog_and_layout.md)** được sinh từ registry. [CSV catalog](artifacts/vie_china_expanded/catalog.csv) và [CSV layout](artifacts/vie_china_expanded/layout.csv) là bản xuất. ID mới dự kiến dùng `VIE_rd_<slug>`, chưa có provider game.

| Cụm chức năng | Node | Nội dung riêng |
|---|---|---|
| Đầu mối chung | C01–C04 | Mở quan hệ; tham vấn cấp chính phủ; xác định chương trình giao thương; phối hợp dân sự |
| Hai chế độ giao thương | C05/C06 | Mutex của kiến trúc cùng một chương trình, không khóa các công cụ khác |
| Điều khoản của từng chế độ | C07/C08 | Quy trình/hồ sơ chung hoặc danh mục/ngoại lệ có xác nhận riêng |
| Thành quả thương mại | C09/C10 | Hai kết quả thay thế, đều cần bàn giao thật |
| Phối hợp xuyên biên giới | C11/C12 → C13 | Đầu mối vụ việc dân sự OR cơ chế lãnh sự–hồi hương |
| Bảo đảm và xử lý gián đoạn | C14–C17 | Chuẩn bị điều chỉnh; tham vấn cấp chương trình; biên bản khắc phục; nối lại có căn cứ |
| Hội tụ | C18 | Một thành quả thương mại AND một cơ chế dân sự, giữ nghĩa vụ của cách đạt |

### Các điểm AND/OR phải nhìn thấy trên cây

- C05/C06 đều cần **C03 AND C02**: đã xác định vấn đề thương mại và có đầu mối thương lượng. Chọn một trong hai; không chọn cả hai.
- C09 theo C05 → C07; C10 theo C06 → C08. Không có đường bỏ qua cam kết rồi tự nhận thành quả.
- C13 nhận **C11 OR C12**, đồng thời đọc cơ chế thực sự đã bàn giao. Không cần làm cả hai chức năng dân sự.
- C15 cần **C02 AND (C09 OR C10)**. Năng lực tham vấn nâng cao có thể chuẩn bị khi đang vận hành, trước khi phát sinh sự cố.
- C17 nhận **C14 OR C16**, nhưng còn cần chương trình đã từng bàn giao và căn cứ nối lại hợp lệ. C14 chưa chuẩn bị xong hoặc không có điều khoản dự phòng được CHI nhận thì không đủ.
- C18 cần **(C09 OR C10) AND C13**, còn cả hai kết quả phải đang hoạt động. Dự phòng trong nước không thay thành quả song phương.

## 3. Hai cam kết giao thương thực sự khác nhau

### C05 — Một quy trình phối hợp chung

Việt Nam chọn đề nghị giao một phạm vi công việc kỹ thuật cho cơ chế phối hợp chung: bộ hồ sơ hai bên nhận, cách thông báo thay đổi và cách xử lý phần bị vướng. Phạm vi được ủy nhiệm phải ghi rõ trước khi CHI trả lời. Không suy ra quyền truy cập dữ liệu quốc gia hoặc quyền thay luật trong nước.

C07 mở ba điều khoản để thương lượng: hồ sơ nào được chấp nhận trong chương trình; loại thay đổi nào phải báo đầu mối còn lại; có chấp thuận trước một phạm vi vận hành thu hẹp hay không. CHI có thể nhận bộ điều khoản, yêu cầu loại một phần hồ sơ hoặc không nhận quyền vận hành thu hẹp từ trước.

**Quyền riêng của tuyến này:** khi vướng mắc chỉ ảnh hưởng phần đã định nghĩa, được dùng phạm vi dự phòng *đã ký trước* mà không giả tạo một lần chấp thuận mới. Nếu đối tác không nhận điều khoản đó từ đầu, quyền này không xuất hiện. **Nghĩa vụ riêng:** muốn thay đổi phần thuộc quy trình chung phải đi qua tham vấn; tự bỏ phần nghĩa vụ thì lợi ích tương ứng ngừng cho tới khi có phạm vi mới được nhận.

Đây không phải lời bảo đảm CHI luôn làm theo mong muốn Việt Nam. Giải pháp giữ phạm vi đầy đủ vẫn cần CHI trả lời. C09 chỉ mở khi gói thực đã bàn giao và vận hành; gói bị thu hẹp dùng đúng giá/lợi ích của phạm vi được nhận.

### C06 — Hợp tác theo từng phạm vi

Việt Nam giữ quyền xem xét từng nội dung trước khi đưa nó vào chương trình. C08 cho lập danh mục hợp tác và tách nội dung chưa chấp thuận. Phạm vi độc lập phải được ghi từ đầu, không tự cắt một nửa nghĩa vụ rồi giữ nguyên thưởng của toàn gói.

**Quyền riêng của tuyến này:** CHI đề nghị bổ sung một yêu cầu thì Việt Nam có thể từ chối phần bổ sung, giữ những phạm vi độc lập còn hợp lệ mà hai bên đã nhận. **Giới hạn riêng:** không có thẩm quyền điều phối chung để tự xử lý nội dung ngoài danh mục; muốn đổi danh mục hoặc mở rộng phải được hai bên xác nhận. Không mặc nhiên có điều khoản vận hành thu hẹp của tuyến C05.

C10 công nhận hợp tác chọn lọc là thành công đầy đủ của mục tiêu đã thống nhất. Không mô tả nó như thất bại hoặc bắt chuyển sang C05 để tới C18.

### Vì sao mutex và nó khóa tới đâu?

C05 và C06 phân định **cùng một công việc** được ủy nhiệm xử lý theo quy trình chung hay phải được xác nhận riêng trước khi áp dụng. Hai thẩm quyền đối lập không đồng thời áp cho cùng phạm vi. Focus biểu thị kiến trúc lâu dài của chương trình, nên đề xuất mutex hai chiều. Gói nhỏ/sâu, danh mục và biện pháp tạm thời vẫn sửa được trong kiến trúc đã chọn; không mutex chúng.

Mutex không áp cho C02/C04/C11/C12/C14–C17, không khóa quan hệ với nước khác, không biến BoP thành thân/chống Trung Quốc. Khi rút hoặc ký lại cùng loại chương trình, không reset completed focus để đổi kiến trúc lách quyền; khả năng đổi toàn bộ kiến trúc về sau chưa được đặc tả, không coi là có sẵn.

**Chưa chứng minh hai tuyến cân bằng.** Quyền được nêu là option/điều kiện thực, chưa quy thành PP; không tự thêm bonus để tuyên bố tuyến nào tương đương tuyến kia.

## 4. Phối hợp dân sự–lãnh sự: thêm nội dung quan hệ ngoài thương mại

C04 không mở lại việc ký hiệp ước, phân định hay tranh chấp đã thuộc chính trị. Nó xác định đầu mối dân sự cho các hồ sơ giả định trên đất liền. Người chơi có thể làm một hoặc cả hai chương trình bên dưới; C13 chỉ cần một chương trình hoạt động đúng phạm vi.

| Chương trình | Gói thứ nhất | Gói thứ hai | Đánh đổi khác với quy mô thương mại |
|---|---|---|---|
| `C.border_civil`, mở bởi C11 | **Xác minh theo yêu cầu:** đầu mối nhận hồ sơ rồi hỏi từng thông tin cần thiết | **Chia sẻ bộ hồ sơ được phép từ trước:** hai bên nhận một danh mục thông tin giới hạn để dùng khi xử lý vụ việc | Giảm nhu cầu xin xác nhận lặp đối với trường đã đồng ý, đổi lại nghĩa vụ giữ đúng phạm vi và cập nhật thông tin; không phải tăng opinion |
| `C.consular_return`, mở bởi C12 | **Xử lý riêng từng trường hợp:** xác minh nhân thân và xin xác nhận tiếp nhận cho mỗi hồ sơ | **Quy trình tiếp nhận đã thỏa thuận:** xác định bằng chứng và đầu mối bàn giao từ trước | Có thể hoàn tất trường hợp đủ hồ sơ mà không mở lại toàn bộ thương lượng; thiếu bằng chứng vẫn phải bổ sung hoặc dừng, không tự coi người đã được tiếp nhận |

Đây là hai chương trình giả định mới, **chưa có giá ngân khố/lịch triển khai/phí tháng trong B1**. Không dùng giá thương mại làm mặc định, không coi chưa định giá là miễn phí. Cấu trúc và lựa chọn được viết trước; thiếu bảng giá chặn code giao dịch. Nếu cần triển khai thường xuyên, chúng dùng cùng giới hạn triển khai hiện có; không tự mở thêm slot.

C11/C12 mở quyền gửi đề nghị; option CHI mới ghi phạm vi nhận. C13 cần cơ chế đã triển khai và đang hoạt động, không chỉ một vụ việc ngẫu nhiên đã kết thúc. Một hồ sơ đơn lẻ thành công là chứng cứ xử lý, không tự trở thành một cơ chế vĩnh viễn.

Không mô phỏng cưỡng bức di cư, chuyển dân số, core hoặc quyền cảnh sát xuyên biên giới. “Hồi hương” ở đây chỉ là hồ sơ lãnh sự và xác nhận bàn giao có đủ căn cứ; không tự di chuyển một người vì người chơi đã hoàn thành focus.

## 5. Tham vấn, dự phòng và phục hồi có chức năng riêng

**C02:** mở đối thoại ban đầu, giải thích yêu cầu, nhận phản hồi khác gói và rút hồ sơ. Không đợi hoàn thành C15 mới có đường giải quyết từ chối. Trường hợp kỹ thuật nằm trong phạm vi đã giao được xử lý qua C07/C08.

**C14:** mở A12 của đặc tả thương mại gốc. Decision mới trả phí chuẩn bị, chờ đúng lịch và ghi sẵn sàng; focus không trả phí hay cấp trạng thái lần nữa. Khi kích hoạt, giảm đúng khoản phạt chậm phối hợp hiện có. Không có reward giao thương thứ hai, không tự giữ một cam kết đã mất hiệu lực.

**C15:** mở quyền đưa trở ngại vượt phạm vi kỹ thuật lên tham vấn cấp chương trình. Ví dụ hai bên bất đồng về việc một yêu cầu mới có nằm trong điều khoản đã ký không. Lựa chọn là sửa điều khoản, đề nghị thu hẹp hoặc kết thúc; CHI có quyền không nhận. Không tự cộng xác suất nhận vì focus nghe có vẻ “cấp cao”.

**C16:** chỉ có khi thực sự đã thương lượng được biên bản khắc phục. Nó ghi nhận chính xác điều khoản thay thế: phần giữ, phần đình chỉ và phần chờ bằng chứng bổ sung. Khi lặp lại cùng loại vướng mắc, reader kiểm biên bản này để biết điều kiện nào đã được sửa; không cho trả lại phí “sửa cùng một lỗi” nếu hồ sơ đã đáp ứng, cũng không bỏ qua một yêu cầu khác.

**C17:** đưa vào sử dụng quyền nối lại giới hạn: hoặc phương án đã được đồng ý từ trước, hoặc biên bản khắc phục mới. Decision nối lại vẫn kiểm tiền, đối tác và phạm vi hợp lệ, dùng phí nối lại hiện có cho C.trade. Chưa có căn cứ song phương thì chỉ được dùng dự phòng trong nước, không được bật lại idea thương mại. C17 không cấp lại bonus hoặc xóa lịch sử phí.

C16/C17 có thể chưa làm trong một lượt chơi hợp tác suôn sẻ; C18 vẫn đạt được. Sau khi C18 đã hoàn thành, gián đoạn thật vẫn mở nội dung phục hồi và refresh đúng lợi ích đang hoạt động.

## 6. Event có lựa chọn và hậu quả quay lại

Các mã CT/CB/CR chỉ là tham chiếu đặc tả, chưa cấp namespace/ID game. Từng luồng dùng cùng contract owner VIE và đối tác CHI; không lấy thông báo kết quả làm writer thành công.

| Event và cấu trúc | Caller/scope | Lựa chọn | Kết quả và reader lần sau |
|---|---|---|---|
| **CT1 — Một phạm vi hay một quy trình?**; đề nghị có phản hồi đối ứng | C03 mở tham vấn VIE; event CHI trả lời | CHI nêu hồ sơ cần làm rõ hoặc phạm vi có thể xét. VIE tiếp tục/đổi dự thảo/rút | Đưa trở ngại cụ thể vào dự thảo C07/C08; chưa trả phí gửi hoặc đặt cờ accepted |
| **CT2 — Quyền điều phối đến đâu?**; thương lượng thẩm quyền theo C05 | Decision gửi của VIE → CHI | Nhận quy trình và dự phòng; chỉ nhận quy trình; yêu cầu loại trường dữ liệu; từ chối | Ghi riêng phạm vi và điều khoản dự phòng được nhận. C17 chỉ có đường dùng dự phòng song phương nếu điều khoản đó đã có |
| **CT3 — Ngoại lệ trong danh mục hợp tác**; sửa từng phần theo C06 | CHI trả lời bản danh mục → VIE nhận/sửa/rút | Giữ phần độc lập; bỏ nội dung bổ sung; đổi danh mục để gửi lại | Gói nhỏ/sâu và lợi ích theo phần hai bên nhận; không gọi từ chối một phần là thành công toàn gói |
| **CB1 — Hai bộ hồ sơ không trùng khớp**; kiểm bằng chứng | Caller chương trình dân sự → VIE, CHI xác minh | Dùng trường thông tin đã được phép chia sẻ; xin bổ sung; không chuyển thông tin chưa được phép | Dùng bộ hồ sơ đã ký hoặc mở một yêu cầu bổ sung. Không tự hoàn tất qua một nút “đã xác minh” nếu bên kia chưa xác nhận |
| **CB2 — Đầu mối tiếp nhận chưa xác nhận**; bàn giao nhiều bước | Caller hồ sơ lãnh sự → VIE/CHI đúng bước | Gửi bằng chứng còn thiếu; đề nghị đầu mối đã thỏa thuận kiểm lại; tạm dừng | Chỉ ghi xử lý hoàn tất khi cả bằng chứng và xác nhận tiếp nhận đủ. Lần sau đọc cùng danh mục bằng chứng đã nhận, không tự miễn kiểm |
| **CR1 — Yêu cầu giao thương bị áp dụng khác nhau**; phản ứng khi đang vận hành | Caller vướng mắc C.trade → VIE | Dùng quy trình kỹ thuật; dự phòng nếu sẵn sàng; tham vấn cấp chương trình nếu đã mở; tạm dừng | Dự phòng giảm phạt; đối thoại có thể sửa phạm vi. Nếu kết thúc, không còn lợi ích giao thương dù C09/C10 đã completed |
| **CR2 — Biên bản khắc phục**; đối tác trả giải pháp rồi VIE quyết định | Tham vấn VIE → CHI → VIE | Nhận sửa đổi; đề nghị phạm vi khác; không nhận và kết thúc | Ghi điều khoản thay thế đúng phiên, mở C16 khi hợp lệ. Nối lại theo phạm vi được nhận, không bật lại toàn gói cũ |

**Phép thử chọn rẻ nhất:** CT2/CT3 là lựa chọn quyền và phạm vi; chưa có giá trị định giá nên chưa kết luận không thống trị. CB1/CB2: bỏ bước bổ sung giữ nguồn lực nhưng hồ sơ chưa hoàn tất, không được nhận cùng kết quả miễn phí. CR1: tạm dừng ngừng lợi ích, dự phòng chỉ giảm phạt; chưa chứng minh trả phí dự phòng có lợi hơn mọi trường hợp. CR2: không nhận giải pháp thì không được dùng nội dung chưa được CHI nhận để nối lại. N2/N3 không được cho PASS chỉ từ lời mô tả đánh đổi.

## 7. Decision — chỉ phần khác với giao thức chung

| Hành động định danh tài liệu | Quyền mở | Giao dịch/điều kiện | Hiệu ứng thực |
|---|---|---|---|
| Soạn quy trình chung | C07 | Chọn trường hồ sơ, thông báo và điều khoản dự phòng; quyền dữ liệu phải hợp lệ | Bản dự thảo có phạm vi/điều khoản để CHI trả lời |
| Soạn danh mục và ngoại lệ | C08 | Các phần độc lập được nêu trước gửi; không đang sửa phiên khác | Bản dự thảo đúng chế độ C06, không tự thêm quyền điều phối |
| Đề nghị cơ chế dân sự | C11 | Giá/lịch chưa định; không được triển khai giao dịch cho tới khi chốt | Một contract C.border_civil, nhận đúng gói |
| Đề nghị cơ chế lãnh sự | C12 | Giá/lịch chưa định; quyền chia sẻ và đầu mối hợp lệ | Một contract C.consular_return, không có quyền chuyển dân cư |
| Chuẩn bị/kích hoạt điều chỉnh giao thương | C14 | Đọc action.contingency_prepare/use; một lần cho đúng đợt; không trừ lại ở focus | Sẵn sàng sau tiến trình; giảm đúng phạt khi dùng |
| Đưa vướng mắc lên tham vấn | C15 | Đọc action.issue_dialogue; giữ cùng issue epoch | Đề nghị sửa điều khoản có phản hồi, chưa tự khôi phục |
| Nối lại phạm vi hợp lệ | C17 | Đọc action.resume; phần nối lại đã được nhận, còn điều kiện duy trì | Áp gói nhỏ/sâu đúng phạm vi; phí thay tháng đầu theo luật gốc, không thu đôi |

Gửi/sửa/bắt đầu/hủy vẫn dùng giao thức gốc, không chép thêm một bộ A01–A13. Hủy không hoàn khoản tổ chức đã dùng. Các timer mới của CB1/CB2/CT1 chưa được định giá; không mượn hạn của action khác chỉ vì có cùng số ngày. Khi code phải có deadline/rút cho từng bước trước khi được coi là luồng khép kín.

## 8. Phản hồi CHI phải đọc điều gì?

Không đặt công thức chung “opinion cao thì nhận”. Phản hồi đọc nội dung chương trình và khả năng thực hiện:

| Chương trình | Yếu tố thực sự phải xét | Phản hồi có ý nghĩa |
|---|---|---|
| Quy trình giao thương chung | Có nhận đầu mối/ủy nhiệm không; bộ hồ sơ có thể dùng; yêu cầu chia sẻ có hợp lệ; có nhận phạm vi dự phòng không | Nhận quy trình nhưng không nhận dự phòng là phản hồi khác với nhận đầy đủ |
| Phạm vi chọn lọc | Phần Việt Nam loại bỏ có làm phần còn lại không thể thực hiện không; danh mục mới có độc lập thật không | Đề nghị sửa danh mục hoặc từ chối; không tự tách một gói phụ thuộc thành các phần thành công |
| Phối hợp dân sự | Đầu mối bên nhận có được xác nhận không; hồ sơ đủ chứng cứ; trường thông tin có trong danh mục chia sẻ | Xin xác minh đúng phần, chấp nhận chuyển hồ sơ hoặc không nhận |
| Lãnh sự–hồi hương | Nhân thân/đầu mối tiếp nhận được xác nhận; các bước bàn giao đã được hai bên nhận | Chấp nhận bước hiện tại, yêu cầu bổ sung hoặc dừng; không tự công nhận hoàn tất |
| Khắc phục vướng mắc | Nguyên nhân của chính đợt đó đã thay đổi chưa; biên bản sửa điều khoản nào; phạm vi muốn nối lại có còn khả thi | Nhận sửa đổi, đề nghị phần nhỏ hơn hoặc kết thúc |

Các đầu mối/phạm vi được ghi bởi phản hồi cụ thể của chương trình, không suy từ focus completed. Provider cho năng lực chuyên ngành CHI chưa được tra đầy đủ, nên chưa viết token trigger hay trọng số AI giả như đã có. Opinion có thể là yếu tố phụ sau khi eligibility nội dung đã đúng. Chiến tranh trực tiếp/nước biến mất dùng cleanup theo từng contract, không trả lời ngẫu nhiên.

## 9. Kiến trúc trạng thái và quyền cấp thưởng

Không thêm GUI, điểm ngoại giao hoặc sổ vay. Dùng contract chương trình có đối tác/phạm vi/epoch và một owner VIE. Ba loại hồ sơ C.trade, C.border_civil, C.consular_return là các chương trình hữu hạn, không phải ba ledger tài chính.

| Dữ kiện khái niệm | Writer | Reader/tác dụng định nghĩa |
|---|---|---|
| Kiến trúc giao thương | Completed C05 hoặc C06 | Chỉ mở bộ điều khoản tương ứng; không tạo biến thứ hai phản chiếu completed focus |
| Phạm vi và hồ sơ được nhận | Phản hồi CHI + VIE nhận nếu có sửa | Triển khai đúng gói; CT/CB không dùng dữ liệu ngoài phạm vi |
| Điều khoản dự phòng song phương | CHI nhận đúng điều khoản trong CT2 | C17 được dùng phương án nhận trước; thiếu nó phải thương lượng, không tự bật idea |
| Dự phòng trong nước | Decision chuẩn bị C14 hoàn tất | Option CR1 giảm đúng phạt, không giữ quyền song phương |
| Bằng chứng và xác nhận dân sự/lãnh sự | Caller xử lý + đúng đầu mối trả lời | Chỉ chuyển bước khi đủ bằng chứng; không tự bàn giao vì người gửi nói đã đủ |
| Biên bản khắc phục | CHI/VIE nhận đúng CR2 và issue epoch | C16, C17 và lần xét cùng điều khoản sau đó |
| Đã bàn giao / đang hoạt động | Complete một lần / maintenance và cleanup | C09/C10/C13/C18; owner reward refresh từ trạng thái |

Tên dữ kiện trên là đặc tả, chưa là ID engine. Các callback phải mang đúng phiên; chưa giải quyết scope bất đồng bộ thì chưa code P2. C09/C10/C13/C16/C18 không cấp lại tiền/research/idea đã bàn giao. Chương trình dân sự chủ yếu mở quyền xử lý và cơ chế bằng chứng, chưa thêm modifier quốc gia vĩnh viễn. Reward trade hiện có giữ nguyên nguồn B1; không nhân hai bộ thưởng theo hai chế độ.

## 10. Chính trị, cụm khác và R1

- C01 giữ gate IX và đường công cụ cơ sở của R0 đã chốt. Các chương trình giả định không có gate ngày lịch sử mới.
- Gói sâu C.trade đọc cadre_cohesion_required theo B1 ở các điểm đã chọn. Không biến ngưỡng này thành yêu cầu cho mọi focus C hoặc cho cả hai chương trình mới.
- Không tự áp lịch BoP B5/S5 lên focus C mới; không thêm reader kiêm nhiệm khi chưa có cửa sổ ký ngoại giao. J2 vẫn FAIL theo quyết định người dùng.
- Chính trị giữ XI08, XIII01–04, XIII10–11; C không tạo sự cố biển, không đặt lại phản hồi đã xảy ra. C02/C15 chỉ đọc kết quả đúng đối tượng khi provider tồn tại, không mặc định mọi bất đồng biển làm mất hợp tác dân sự.
- Chính trị X05–X08 giữ quyền trong nước/tiếp cận dữ liệu; C07/C11/C12 không cấp vượt quyền đó. E104 vẫn chỉ có kế hoạch chuyển sau kiểm C; ba hồ sơ mới không ghi chồng E104. J5 giữ FAIL.
- M sở hữu lưu vực/kết nối với LAO/CAM; B sở hữu cứu nạn biển; E/S/W giữ đối tác của mình. C dân sự chỉ là hồ sơ xuyên biên giới đất liền với CHI, không thay các owner này.
- Trong đồ thị ứng viên toàn nhánh, OR của R1 thay C6 cũ bằng C18 mới, các cha khác giữ nguyên. C chỉ tính một cụm; nghĩa vụ C.trade và cơ chế dân sự/lãnh sự cần còn hiệu lực để tính kết quả C18. Không cho ba chương trình C tự tính thành ba cụm của mạng lưới.

Thay capstone C làm tăng yêu cầu nội dung của đường C→R1; chưa kết luận công bằng với các cụm khác. Cần xét ở L2 cùng giá của hai chương trình mới, không tự hạ gate hoặc cấp thưởng thêm để che chênh.

## 11. Layout và kiểm bằng script

Vùng ứng viên C nằm trong X308–332; root C01 ở Y2, kết quả thương mại và dân sự tại Y10, C18 tại Y14. C15/C16/C17 là cột xử lý gián đoạn, có thể tiếp tục đến Y16 sau khi đã đạt C18. Các root/capstone và tọa độ của sáu cụm khác giữ nguyên; R1 vẫn tại vị trí nền, chỉ đổi consumer C trong bản ghép ứng viên.

Không bắt các node theo tuyến mutex phải được hoàn thành hết. Tổng cost catalog không phải chi phí một đường chơi. Mermaid trong bản sinh giúp đọc đồ thị; chưa có SVG/PNG tổng 63 node và chưa kiểm dây/hộp tên trong HOI4. SVG 51 node cũ được giữ làm baseline, không gắn nhãn mới lên hình cũ để coi đã đồng bộ.

Chạy:

```powershell
python -X utf8 tools/review_expanded_china_branch.py
```

[Kết quả máy đọc](artifacts/vie_china_expanded/checks.json) và [CSV ca AND/OR](artifacts/vie_china_expanded/gate_cases.csv) đi kèm. Script xét toàn bộ tổ hợp completed của 18 node để kiểm tính nhất quán đồ thị, chưa mô phỏng available, giao dịch hoặc engine.

| Bất biến | Kết quả đối với bản mở rộng |
|---|---|
| J1/J3/J4 | Giữ giao diện/kỳ và tham chiếu nguồn đã chốt; chưa kiểm triển khai mới trong game |
| J2 | **FAIL** — quyết định giữ lịch BoP, chưa chứng minh đổi lựa chọn |
| J5 | **FAIL** — nợ chuyển E104, không đổi owner chính trị |
| D1–D6/D8 | **FAIL/chưa nghiệm thu** — chưa định giá quyền, chi phí hai chương trình mới và hành vi đối tác; không tuyên bố cân bằng |
| D7 | Giữ “đơn vị treasury chưa xác định”; k không thành tỷ giá engine |
| N1 | C có thêm bài toán, gói, hành động, nhiều cấu trúc event và hậu quả đọc lại; sáu cụm khác chưa hoàn thiện, không cho toàn nhánh PASS |
| N2/N3 | **Chưa PASS** — option có tác dụng định nghĩa nhưng chưa đủ định giá/luồng thực để loại thống trị mọi trường hợp |
| N4 | Nội dung thêm ghi rõ giả định gameplay; không thêm mốc/nhân vật lịch sử |
| H1 | **FAIL theo định nghĩa cũ 51 node/SVG** — chỉ đạo mới đã bỏ trần C, chưa có SVG tổng mới. Không tự sửa bất biến để PASS |
| H2 | **FAIL** — các bảng tổng nền chưa hợp nhất; banner phân biệt bản nền với đặc tả mới |
| H3 | **PASS kiểm node/anchor ứng viên** khi errors rỗng trong bản sinh; chưa kiểm đường dây/hộp icon |
| H4 | **PASS giới hạn báo cáo** — chưa chạy HOI4/playtest |

## 12. Changelog, phần không đổi và việc còn phải chốt

| Mục | Cũ | Đề xuất mới | Các chỗ chịu tác động |
|---|---|---|---|
| Phạm vi C | Sáu node phục vụ một chương trình thương mại | 18 node: thương mại, tham vấn, dân sự–lãnh sự, phục hồi | Registry variant, đặc tả này, catalog/layout/CSV sinh |
| Tổng node | Baseline 51 | Ứng viên 63, tăng 12 | Bản ghép global CSV; banner plan; không tự gọi SVG cũ là 63 |
| Mutex | Không có | C05/C06, riêng chế độ C.trade | Bộ điều khoản C07/C08; nhận phản hồi/triển khai/thu hẹp |
| OR | C không có OR prerequisite | C13, C15, C17 và C18 có OR rõ | Graph, gate_cases và phép duyệt completed |
| Reader kết quả C | C6 cũ | C09/C10 là kết quả trade; C18 là hội tụ mở rộng | R1 candidate và mapping trong registry |
| Tham số | B1 hiện có | Không thêm tham số kinh tế; chương trình mới chưa định giá | Không đổi bảng giá 20–21 hoặc CSV cân bằng cũ |

**Không đổi:** gameplay VIE/CHI; chính trị và nguồn báo cáo Trung Quốc; giá/timer/cap B1; sáu cụm còn lại; AI profile và trọng số; E104; master/icon/game export; SVG/PNG nền. Hồ sơ L1 và kết quả 51 node là snapshot trước mở rộng, không được dùng để nhận nghiệm thu bản này.

Phần cần quyết sau khi đọc nội dung: nhận/sửa hai chế độ giao thương; phạm vi thông tin dân sự/lãnh sự được phép trong gameplay; giá/lịch/duy trì cho hai chương trình mới; việc C18 yêu cầu cả thương mại và dân sự so với các cụm khác. Đây là các đề xuất review được, chưa tự coi đã được người dùng chốt. Chưa tự đi tiếp L2 hoặc xây gameplay khi các phần này chưa rõ.
