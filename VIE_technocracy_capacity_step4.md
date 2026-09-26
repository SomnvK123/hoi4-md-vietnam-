# Bước 4: Kỹ trị, nhà nước kiến tạo và năng lực nhà nước

> Tiếp theo `VIE_regime_taxonomy_step1_2.md` và `VIE_three_families_step3.md`. **Chưa** thiết kế khung xây dựng nhà nước (STEP 5), **chưa** đề xuất sửa focus.
>
> Nhãn: **[SỰ KIỆN]** · **[HỌC THUẬT]** · **[TƯƠNG TỰ LỊCH SỬ]** · **[TIỀN ĐỀ KỊCH BẢN]** · **[TRỪU TƯỢNG GAMEPLAY]**

---

## 0. Phát hiện quan trọng nhất của bước này

**[SỰ KIỆN]** Millennium Dawn **đã có sẵn một hệ năng lực nhà nước hoàn chỉnh**, gồm 7 họ luật có biến theo dõi, đã được khởi tạo cho Việt Nam bằng giá trị lịch sử hợp lý. Submod `md_vietnam` **chưa từng chạm vào nó một lần nào**.

| Hệ thống MD | Biến | Giá trị khởi đầu của VIE | Số lần submod dùng |
|---|---|---|---|
| Luật bộ máy hành chính | `bureau_law` | **bureau_03** (giữa) | **0** |
| Luật cảnh sát | `police_law` | **police_05** (cao nhất) | **0** |
| Luật giáo dục | `education_law` | edu_03 | **0** |
| Luật y tế | `health_law` | health_02 | **0** |
| Luật an sinh | `social_law` | social_02 | **0** |
| Luật quân sự | `military_law` | defence_02 | **0** |
| Thuế | `tax_rate`, `corporate_tax_rate` | — | **0** |
| Tham nhũng | `corruption_level_XX` | **corruption_level_08** (cao) | 39 |

Submod gọi `treasury_change` **162 lần** nhưng chưa bao giờ đụng tới một luật nào. Nghĩa là: **lớp "năng lực nhà nước" mà bạn muốn xây không cần phát minh — nó đã nằm sẵn trong MD, chỉ chưa được nối vào cây focus.**

---

## 1. Nhà nước kiến tạo thực sự là gì

**[HỌC THUẬT]**

### 1.1 Bốn công trình nền

**Johnson (1982), *MITI and the Japanese Miracle*** — đặt ra thuật ngữ. Phân biệt ba loại nhà nước: **plan-rational** (Nhật — nhà nước đặt mục tiêu thực chất cho nền kinh tế và can thiệp theo cách thuận thị trường), **plan-ideological** (Liên Xô — kế hoạch thay thế thị trường), **market-rational** (Mỹ — nhà nước chỉ đặt luật chơi). Bốn đặc điểm của nhà nước kiến tạo:
1. Một bộ máy kinh tế **nhỏ, tinh hoa, tuyển theo năng lực**
2. Một hệ thống chính trị cho bộ máy đó **không gian để hành động** — "chính trị gia trị vì, quan chức cai trị"
3. Can thiệp bằng phương pháp **thuận thị trường**
4. Có một **cơ quan đầu não** (pilot agency) điều phối

**Amsden (1989), *Asia's Next Giant*** (Hàn Quốc) — đóng góp cơ chế then chốt: **tính có đi có lại** (reciprocity). Nhà nước trợ cấp, nhưng **đổi lấy tiêu chuẩn thành tích** kiểm chứng được, chủ yếu là chỉ tiêu xuất khẩu. Doanh nghiệp không đạt thì bị cắt. Đây là thứ phân biệt chính sách công nghiệp thành công với bảo hộ thất bại.

**Wade (1990), *Governing the Market*** (Đài Loan) — nhà nước hướng đầu tư vào các ngành mà thị trường tự nó không rót vốn vào.

**Evans (1995), *Embedded Autonomy*** — đóng góp lý thuyết quyết định. Nhà nước kiến tạo cần **đồng thời hai điều kiện đối nghịch nhau**:
- **Tự chủ** — bộ máy Weber hóa, tuyển theo năng lực, có bản sắc riêng, **không bị doanh nghiệp bắt cóc**
- **Gắn kết** — mạng lưới quan hệ dày đặc với doanh nghiệp để biết thông tin thật

Và hai kiểu hỏng:

| Mất cân bằng | Kết quả | Ví dụ của Evans |
|---|---|---|
| Tự chủ nhiều, gắn kết ít | Nhà nước xa rời, chính sách sai thông tin | Ấn Độ thời kỳ đầu |
| Gắn kết nhiều, tự chủ ít | **Bị bắt cóc — tài phiệt** | Nhiều nước Mỹ Latinh |
| Không có cả hai | **Nhà nước ăn cướp** | Zaire |
| Có cả hai | Nhà nước kiến tạo | Nhật, Hàn, Đài Loan |

**[HỌC THUẬT]** Dòng thứ hai của bảng này là kết nối trực tiếp tới dải `ol_*` trong mod: **tài phiệt không phải một chế độ khác, nó là nhà nước kiến tạo mất tự chủ.** Evans coi chúng là hai điểm trên cùng một chiều.

### 1.2 Điều kiện nào sinh ra nhà nước kiến tạo

**Doner, Ritchie & Slater (2005), "Systemic Vulnerability and the Origins of Developmental States", *International Organization* 59(2)** — công trình quan trọng nhất cho thiết kế game, vì nó nói nhà nước kiến tạo **bị ép ra đời, không phải được chọn**. Ba điều kiện phải hội tụ:

1. **Mối đe dọa an ninh nghiêm trọng từ bên ngoài**
2. **Khan hiếm nguồn lực** — không có dầu, không có viện trợ vô điều kiện
3. **Nhu cầu mua sự trung thành của quần chúng** — tinh hoa cầm quyền phải cần dân ủng hộ

Khi cả ba cùng có, giới cầm quyền **không còn lựa chọn nào khác** ngoài xây dựng bộ máy có năng lực và ép doanh nghiệp làm ăn thật.

**[TIỀN ĐỀ KỊCH BẢN]** Đây là điều kiện tiên quyết có cơ sở cho nhánh kiến tạo trong mod, thay cho điều kiện hiện tại (`VIE_bop_is_reformist`). Việt Nam có điều kiện 1 (Trung Quốc) rõ ràng, điều kiện 2 một phần, điều kiện 3 tùy vào chính danh.

### 1.3 Nó có phải một chế độ không

**Không.** **[HỌC THUẬT]** Bằng chứng trong literature:

| Nước | Thời kỳ | Chế độ | Nhà nước kiến tạo? |
|---|---|---|---|
| Nhật Bản | 1955–1990 | Dân chủ suốt | **Có** |
| Hàn Quốc | 1961–1987 | Độc tài quân sự | **Có** |
| Hàn Quốc | 1987–nay | Dân chủ | **Có**, dạng biến đổi |
| Đài Loan | 1950–1996 | Độc đảng | **Có** |
| Singapore | 1965–nay | Độc đoán bầu cử | **Có** |

Cùng một mô hình kinh tế xuất hiện ở bốn cấu hình chính trị khác nhau, và tồn tại **xuyên qua** chuyển đổi dân chủ ở hai nước. Kết luận: nhà nước kiến tạo là **quan hệ nhà nước – xã hội + hình thái bộ máy + bộ công cụ chính sách**, không phải một loại chế độ.

---

## 2. Kỹ trị thực sự là gì

**[HỌC THUẬT]**

**Centeno (1993), "The New Leviathan: The Dynamics and Limits of Technocracy", *Theory and Society* 22(3)** — định nghĩa được trích dẫn nhiều nhất: sự thống trị hành chính và chính trị của một xã hội bởi **một tinh hoa nhà nước** tìm cách áp đặt **một hệ hình chính sách duy nhất, loại trừ**, dựa trên việc áp dụng các kỹ thuật duy lý công cụ.

Lập luận then chốt của Centeno, và là câu trả lời cho câu hỏi của bạn: **kỹ trị không tự sinh ra tính chính danh.** Nó luôn phải mượn chính danh từ một nguồn khác — một đảng, một lãnh tụ, một cuộc bầu cử, hoặc một cuộc khủng hoảng. Vì vậy nó **không thể là một loại chế độ**: chế độ là câu trả lời cho "ai cầm quyền và bằng quyền gì", mà kỹ trị không có câu trả lời riêng cho vế thứ hai.

**Putnam (1977)** — "tâm thế kỹ trị" là một thuộc tính **đo được của quan chức**, không phải một hình thức chính thể.

**Dargent (2015), *Technocracy and Democracy in Latin America*** — kỹ trị lên nắm quyền **trong các nền dân chủ** thông qua ủy quyền: ngân hàng trung ương độc lập, cơ quan quản lý, bộ tài chính. Nghĩa là kỹ trị hoàn toàn tương thích với dân chủ.

**Bickerton & Invernizzi Accetti (2021), *Technopopulism*** — kỹ trị và dân túy chia sẻ cùng một logic: cả hai đều viện dẫn **lợi ích chung không qua trung gian**, bỏ qua sự trung giới của đảng phái. Hai thứ có thể hợp nhất.

**[HỌC THUẬT] Kết luận:** kỹ trị là **cách tuyển chọn tinh hoa + cách biện minh chính sách**. Trên khung phân lớp, nó là giá trị cao ở **lớp năng lực** kèm giá trị thấp ở **lớp ràng buộc quyền lực**. Nó không có ô riêng ở lớp chế độ.

---

## 3. Hai thứ này có phải cùng một loại không

**Không.** Chúng trả lời hai câu hỏi khác nhau:

- **Nhà nước kiến tạo** = *nhà nước làm gì với nền kinh tế, và quan hệ với doanh nghiệp ra sao*
- **Kỹ trị** = *ai ngồi trong bộ máy, và họ viện quyền gì*

**[TƯƠNG TỰ LỊCH SỬ]** Bốn ô đều có ca thật:

|  | **Kỹ trị mạnh** | **Kỹ trị yếu** |
|---|---|---|
| **Kiến tạo mạnh** | Nhật (MITI), Singapore, Đài Loan | Hàn Quốc đầu thời Park — quân sự hóa, cá nhân hóa, nhưng vẫn có chính sách công nghiệp có đi có lại |
| **Kiến tạo yếu** | Chile thời "Chicago Boys" — kỹ trị mạnh nhưng **chống** chính sách công nghiệp; các nội các ổn định hóa kiểu IMF | Nhà nước ăn cướp (Evans) |

Ô trên bên phải và ô dưới bên trái chứng minh hai khái niệm **độc lập với nhau**. Đây là lý do không thể gộp `VIE_developmental_state` và `VIE_technocrat_cabinet` thành một thứ, mà cũng không thể tách chúng thành hai chế độ.

---

## 4. Năng lực nhà nước

**[HỌC THUẬT]**

### 4.1 Khái niệm trung tâm: quyền lực chuyên chế ≠ quyền lực hạ tầng

**Mann (1984), "The Autonomous Power of the State", *European Journal of Sociology*** — phân biệt quan trọng nhất trong toàn bộ literature này:

- **Quyền lực chuyên chế (despotic power):** tinh hoa nhà nước **có thể làm gì mà không cần thương lượng** với xã hội
- **Quyền lực hạ tầng (infrastructural power):** nhà nước **thực sự có thể thẩm thấu vào xã hội và thi hành quyết định** tới đâu

Hai thứ này **độc lập**. Một chế độ có thể chuyên chế cao mà hạ tầng yếu — ra lệnh gì cũng được nhưng không thực hiện được lệnh nào. Và ngược lại: các nhà nước Bắc Âu có quyền lực hạ tầng rất cao và quyền lực chuyên chế rất thấp.

**[HỌC THUẬT] Áp dụng cho Việt Nam:** nhà nước Việt Nam có quyền lực hạ tầng tương đối cao so với mức thu nhập — thu được thuế, làm được tổng điều tra, triển khai được tiêm chủng và dân quân tới cấp xã. Các động thái ở Đại hội XIV (hợp nhất TBT–Chủ tịch nước, an ninh nắm vị trí trọng yếu) làm tăng **quyền lực chuyên chế**. Các cải cách bộ máy nhắm vào **quyền lực hạ tầng** nhưng chưa chắc đạt được. **Đây là hai thanh khác nhau và không nên gộp.**

### 4.2 Ba chiều đo được

**Hanson & Sigman (2021), "Leviathan's Latent Dimensions: Measuring State Capacity for Comparative Political Research", *Journal of Politics* 83(4)** — phân tích nhân tố trên hàng chục chỉ số, tìm ra **ba chiều**:

1. **Khai thác (extractive)** — thu ngân sách
2. **Cưỡng chế (coercive)** — kiểm soát lãnh thổ, độc quyền bạo lực
3. **Hành chính (administrative)** — cung cấp dịch vụ, đăng ký dân cư, thực thi hợp đồng

**Fukuyama (2013), "What Is Governance?", *Governance* 26(3)** — năng lực và trách nhiệm giải trình là **hai trục trực giao**. Nhà nước có thể mạnh và độc đoán, mạnh và dân chủ, yếu và dân chủ, yếu và độc đoán.

**Evans & Rauch (1999), "Bureaucracy and Growth", *American Sociological Review* 64(5)** — phát hiện dùng được ngay: **thang Weber hóa** gồm hai thành phần, **tuyển theo năng lực** và **lộ trình sự nghiệp dự đoán được**, tương quan có ý nghĩa với tăng trưởng, kiểm soát cả GDP ban đầu lẫn vốn con người. Nghĩa là *cách tuyển người* có hiệu ứng kinh tế đo được, không chỉ là chuyện đạo đức.

**Besley & Persson (2011), *Pillars of Prosperity*** — năng lực tài khóa và năng lực pháp lý là **khoản đầu tư**: tốn chi phí trước, sinh lợi sau. Đây là cơ sở lý thuyết cho việc trong game, nâng năng lực phải **tốn tiền và tốn thời gian**, không phải bấm một cái là có.

---

## 5. Việt Nam: dữ liệu thật về cải cách bộ máy

**[SỰ KIỆN]** (ISEAS Perspective 2025/14, Nguyễn Khắc Giang)

| Chỉ số | Giá trị |
|---|---|
| Khu vực công | ~4 triệu người, **7,9% lực lượng lao động** (2023), thuộc nhóm lớn nhất Đông Nam Á |
| Bộ ngành | 22 → **17** (tính cả cơ quan thuộc Chính phủ: 30 → 22) |
| Tổng cục bị bỏ | **519 đơn vị, 86%** |
| Cục/vụ bị bỏ | **219 đơn vị, 54%** |
| Mỗi bộ phải cắt tầng trung gian | **30%** |
| Công an cấp huyện | **705 đơn vị bị giải thể** |
| Tinh giản ngay | **100.000 người trong 6 tháng** |
| Mục tiêu dài hạn | **giảm 20%, khoảng 400.000 người** |
| Chi phí | **130.000 tỷ đồng ≈ 5,1 tỷ USD = 6,4% chi ngân sách 2024** |
| Văn bản pháp luật phải sửa hoặc bỏ | **hơn 5.000**, khoảng 300 luật trong một kỳ họp |

**[HỌC THUẬT] Chẩn đoán của tác giả:** vấn đề cốt lõi **không phải số lượng biên chế** mà là **phân mảnh** — nhiều đầu mối nắm quyền, chồng lấn thẩm quyền. Nhà đầu tư phải xin **30–40 con dấu** từ các sở ngành, mất **hai đến ba năm**.

**[HỌC THUẬT] Rủi ro tác giả nêu — và đây là chất liệu đánh đổi tốt nhất trong toàn bộ nghiên cứu này:**

- Tiến độ gấp tạo lỗ hổng cho tham nhũng và **"chạy ghế"**
- Có thể **giữ lại người kém và mất người giỏi**, dẫn tới "chính quyền do những người kém năng lực nhất điều hành"
- Siêu bộ có thể **tập trung quyền quá mức** và giảm kiểm soát
- Gián đoạn chuyển tiếp làm giảm niềm tin nhà đầu tư

Nói cách khác: **một cuộc cải cách nhằm tăng năng lực nhà nước có thể làm giảm năng lực nhà nước.** Đó chính xác là kiểu đánh đổi bạn muốn, và nó có nguồn.

**[SỰ KIỆN] Đo lường sẵn có của Việt Nam:** **PAPI** (UNDP, từ 2009, cả 63 tỉnh) đo 8 chiều: *tham gia ở cấp cơ sở, công khai minh bạch, trách nhiệm giải trình với người dân, kiểm soát tham nhũng, thủ tục hành chính công, cung ứng dịch vụ công, quản trị môi trường, quản trị điện tử*. **PCI** (từ 2005) đo chất lượng điều hành kinh tế cấp tỉnh. Edmund Malesky là tác giả chính của PCI và thành viên nhóm nghiên cứu PAPI từ đầu.

**[TIỀN ĐỀ KỊCH BẢN]** Tám chiều PAPI là quá nhiều cho gameplay, nhưng chúng là **bộ khung Việt Nam chính thức** để rút gọn, thay vì tự nghĩ ra.

---

## 6. MD đã có gì, và nó mô hình hóa đúng đến đâu

**[SỰ KIỆN]** Đối chiếu ba chiều Hanson–Sigman với cơ chế MD:

| Chiều năng lực | Cơ chế MD sẵn có | VIE khởi đầu | Mô hình hóa đúng không |
|---|---|---|---|
| **Khai thác** | `tax_rate`, `corporate_tax_rate`, hệ ngân sách `treasury` | — | **Khá đúng** |
| **Cưỡng chế** | `police_law` 1–5, `military_law` | **police_05 — cao nhất** | **Đúng**, và giá trị khởi đầu hợp lý |
| **Hành chính** | `bureau_law` 1–5 | **bureau_03** | **Chỉ một nửa** — xem dưới |

**[HỌC THUẬT] Hạn chế quan trọng:** `bureau_law` của MD mô hình hóa **quy mô và chi phí** của bộ máy, không phải **chất lượng** của nó. Ở mức 5, hiệu ứng là `political_power_gain = 1.0` và `production_speed_buildings_factor = -0.2` — bộ máy to hơn thì ra quyết định chính trị nhanh hơn nhưng xây dựng chậm hơn và tốn ngân sách hơn.

Đó là chiều **"nhiều hay ít"**, không phải chiều **"tốt hay tệ"**. Thang Weber hóa của Evans & Rauch — tuyển theo năng lực và lộ trình dự đoán được — **không có đại diện nào trong MD**. Thứ gần nhất là `corruption_level_XX`, nhưng tham nhũng là **hệ quả** của chất lượng bộ máy, không phải bản thân chất lượng đó.

**[TIỀN ĐỀ KỊCH BẢN] Hệ quả:** submod cần **đúng một** đại lượng mới — chất lượng bộ máy theo nghĩa Weber — và nối vào bốn thứ đã có sẵn (`bureau_law`, `police_law`, `tax_rate`, `corruption_level`). Không cần xây cả một hệ thống năng lực nhà nước.

---

## 7. Trả lời năm câu hỏi của bạn

**1. Nhà nước kiến tạo thực sự là gì?**
Một **quan hệ nhà nước–xã hội** (tự chủ gắn kết, theo Evans) cộng một **hình thái bộ máy** (cơ quan đầu não tuyển theo năng lực, theo Johnson) cộng một **bộ công cụ chính sách** (trợ cấp có đi có lại đổi lấy thành tích xuất khẩu, theo Amsden). Nó bị ép ra đời bởi tổn thương hệ thống, chứ không được chọn tùy ý (Doner–Ritchie–Slater).

**2. Kỹ trị thực sự là gì?**
Một **cách tuyển chọn tinh hoa** và một **cách biện minh chính sách**, không tự sinh ra chính danh (Centeno). Nó luôn ký sinh vào một nguồn chính danh khác.

**3. Hai thứ này có cùng một loại không?**
**Không.** Bốn ô trong bảng 2×2 ở mục 3 đều có ca lịch sử thật. Chúng độc lập với nhau.

**4. Kỹ trị nên là gì?**
**Phong cách cầm quyền cộng mô hình năng lực nhà nước** — tức là **lớp 2 và lớp 3**, dùng được cho mọi family. **Không phải** chế độ, **không phải** nhánh con của một chế độ duy nhất.
*Bạn nghi ngờ đúng, và literature xác nhận, chứ không phải tôi chiều theo ý bạn: lập luận quyết định là của Centeno về việc kỹ trị không thể tự sinh chính danh, cộng với bằng chứng của Dargent rằng kỹ trị tồn tại bình thường trong các nền dân chủ.*
**Lưu ý:** `VIE_ng_technocratic_caretaker` trong mod là **chính phủ lâm thời kỹ trị**, một thứ khác — đó là một **cơ chế chuyển tiếp** có thời hạn, không phải kỹ trị như phong cách cầm quyền. Hai cái trùng tên nhưng khác loại.

**5. Nhà nước kiến tạo nên nằm ở đâu?**
**Ở nhiều family, nhưng với điều kiện tiên quyết và trần khác nhau.** Bằng chứng: Nhật dân chủ, Hàn và Đài độc tài rồi dân chủ, Singapore độc đoán bầu cử — cùng mô hình, bốn cấu hình chính trị.
Cụ thể cho mod:
- **Trong Đổi Mới (slot 19):** có — đây là vị trí hiện tại và nó đúng
- **Trong Family B dân tộc chủ nghĩa:** có — đó chính là "phát triển chủ nghĩa dân tộc", nấc B2
- **Trong nhánh độc đoán:** có — `wa_*` Hội đồng Phát triển là mô hình Park Chung-hee
- **Trong nhánh dân chủ:** có — Nhật và Hàn sau 1987
- **Điều kiện khác nhau:** dân chủ thì khó giữ tự chủ hơn (áp lực cử tri), độc đoán thì dễ mất gắn kết hơn (không có kênh phản hồi)

---

## 8. Cập nhật khung phân lớp sau bước 4

Khung 5 lớp ở STEP 2 vẫn đứng vững, nhưng lớp 2 cần tách đôi theo Mann:

| Lớp | Nội dung | Cơ chế MD sẵn có |
|---|---|---|
| 1. **Chế độ** | Ai chọn người cầm quyền | `ruling_party`, `VIE_transition_regime` |
| 2a. **Quyền lực hạ tầng** | Nhà nước thực thi được tới đâu | `bureau_law`, `police_law`, `tax_rate` — **chưa dùng** |
| 2b. **Chất lượng bộ máy** | Tuyển theo năng lực, dự đoán được | **Chưa có — cần thêm đúng một đại lượng** |
| 3. **Ràng buộc quyền lực** | Tư pháp, Quốc hội, báo chí, phân cấp | `VIE_party_balance` một phần |
| 4. **Mô hình kinh tế** | Nhà nước ↔ thị trường, tự chủ ↔ gắn kết | Luật kinh tế MD, `treasury` |
| 5. **Đối ngoại** | Tự chủ / cân bằng / nghiêng bên nào | Ý tưởng Ba–Bốn Không, cặp loại trừ đã có |

**[TIỀN ĐỀ KỊCH BẢN]** Lớp 2b là nơi "kỹ trị" sống. Lớp 4 là nơi "nhà nước kiến tạo" sống. Chúng gặp nhau ở **tự chủ gắn kết** của Evans: tự chủ cao mà gắn kết thấp thì thành nhà nước xa rời; gắn kết cao mà tự chủ thấp thì **thành dải `ol_*` tài phiệt**.

---

## 9. Hệ quả thiết kế

| Phát hiện | Hệ quả cho STEP 5 |
|---|---|
| MD có 7 họ luật, submod dùng 0 | Focus cải cách bộ máy nên **đổi `bureau_law`**, không chỉ cho PP. Việc này gần như miễn phí về kỹ thuật |
| `bureau_law` đo quy mô, không đo chất lượng | Cần **một** đại lượng mới duy nhất: chất lượng bộ máy kiểu Weber |
| Evans: tài phiệt = kiến tạo mất tự chủ | `ol_*` nên là **điểm cuối của một chiều đo**, không phải một chế độ tách rời |
| Doner–Ritchie–Slater: kiến tạo bị ép ra đời | Điều kiện mở nhánh kiến tạo nên là **đe dọa + khan hiếm + cần chính danh quần chúng**, không phải `VIE_bop_is_reformist` |
| Amsden: có đi có lại | Focus vô địch quốc gia nên **kèm điều kiện thành tích**, nếu không đạt thì mất — đây là đánh đổi có nguồn |
| Cải cách có thể làm giảm năng lực | Chuỗi tinh gọn bộ máy 2024–2025 nên có **rủi ro thật**, không chỉ toàn lợi ích |
| Mann: chuyên chế ≠ hạ tầng | Hợp nhất TBT–Chủ tịch nước tăng chuyên chế, **không** tăng hạ tầng. Hai thứ nên tách |
| Kỹ trị dùng được ở mọi family | `technocrat_cabinet`, `meritocratic_service` nên **thoát khỏi** dải kiến tạo và thành lựa chọn chung |
| PAPI 8 chiều | Rút gọn thành 3 chiều làm khung đo, thay vì tự nghĩ |

---

## 10. Khoảng trống cần kiểm chứng thêm

1. **Giới hạn kỹ thuật của việc đổi luật MD bằng focus.** Luật MD có `available` gắn với `budget_law_parliament_change_allowed` và chi phí PP. Cần thử xem `swap_ideas` từ `bureau_03` sang `bureau_04` trong `completion_reward` có chạy sạch không, hay phải dùng effect riêng của MD.
2. **Chi phí ngân sách.** Nâng `bureau_law` làm tăng `expected_adm_spending`. Nếu focus nâng luật mà người chơi không đủ ngân sách thì hệ thống ngân sách MD phản ứng thế nào — chưa kiểm.
3. **Literature về quan hệ dân sự – quân sự Việt Nam** vẫn chưa đọc (nợ từ STEP 3). Cần cho lớp 2a chiều cưỡng chế.
4. **Dữ liệu PAPI theo năm** chưa dùng. Nếu muốn đặt giá trị khởi đầu và mục tiêu cho đại lượng chất lượng bộ máy, nên lấy mốc từ PAPI 2011 và 2024 thay vì đoán.
5. **Cách MD tính `corruption_level` tác động lên PP và ngân sách** — cần biết để không cộng dồn hai lần với đại lượng chất lượng bộ máy mới.

---

## Nguồn

**Nhà nước kiến tạo:** Johnson (1982) *MITI and the Japanese Miracle*; Amsden (1989) *Asia's Next Giant*; Wade (1990) *Governing the Market*; Evans (1995) *Embedded Autonomy*; Woo-Cumings ed. (1999) *The Developmental State*; Doner, Ritchie & Slater (2005) *International Organization* 59(2); Haggard (2018) *Developmental States*.

**Kỹ trị:** Centeno (1993) *Theory and Society* 22(3); Putnam (1977) *Comparative Political Studies*; Meynaud (1968) *Technocracy*; Dargent (2015) *Technocracy and Democracy in Latin America*; Bickerton & Invernizzi Accetti (2021) *Technopopulism*.

**Năng lực nhà nước:** Mann (1984) *European Journal of Sociology* 25(2); Soifer (2008) *Studies in Comparative International Development* 43; Fukuyama (2013) *Governance* 26(3); Hanson & Sigman (2021) *Journal of Politics* 83(4); Evans & Rauch (1999) *American Sociological Review* 64(5); Besley & Persson (2011) *Pillars of Prosperity*.

**Việt Nam:** [ISEAS Perspective 2025/14, Nguyen Khac Giang, về cải cách bộ máy](https://www.iseas.edu.sg/articles-commentaries/iseas-perspective/2025-14-vietnams-bureaucratic-reforms-opportunities-and-challenges-in-the-era-of-national-rise-by-nguyen-khac-giang/); [PAPI, UNDP Việt Nam](https://papi.org.vn/eng/); [Chỉ số quản trị của Edmund Malesky, Duke](https://sites.duke.edu/malesky/governance-indices/).

**Cơ chế MD (đọc trực tiếp từ file):** `common/ideas/AA_law_budget.txt` (bureau_01…05, police, edu, health, social, military), `common/scripted_effects/00_budget_effects.txt` (tax_rate, corruption), `history/countries/VIE - Vietnam.txt` (giá trị khởi đầu của Việt Nam).
