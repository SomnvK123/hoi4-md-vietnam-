# Hệ thống mỹ thuật thống nhất cho MD Vietnam

## 1. Phạm vi và thứ tự ưu tiên

Đích là đồng bộ với giao diện Millennium Dawn và nhận diện Việt Nam thời hiện đại,
từ focus đến spirit, decision, ảnh sự kiện, nhân vật, BoP và MIO.
Đồng bộ nghĩa là chung ngôn ngữ vật liệu, cách phân cấp và ngữ nghĩa biểu tượng;
không có nghĩa mọi asset cùng khung, cùng canvas hoặc cùng neon.

Khi tài liệu khác nhau, dùng thứ tự:
1. Yêu cầu hiện tại của người dùng và mẫu đã chọn cho đúng nhóm.
2. Consumer thực tế: gameplay field → sprite/path → texture → GUI slot.
3. Tài liệu hệ thống này và profile kỹ thuật đã đo trong tập 4.
4. Board tham chiếu MD cùng loại có nguồn/commit.
5. Tập 2 và 3 để lấy ý nghĩa văn hóa/concept; các tọa độ, số focus và
   “AAA”, “6-layer”, “3.000 màu” trong bản cũ không phải ràng buộc engine.

[Đánh giá phân tích](06_review_modern_day_analysis.md) phân biệt bằng chứng,
lựa chọn thiết kế và giả thuyết. Không mô tả tài liệu nội bộ là chuẩn chính thức của MD.

## 2. Bốn thành phần cố định, bốn thành phần thay đổi

Cố định:
- Một ý chính rõ ràng; chủ thể được đọc trước nền và trang trí.
- Ánh sáng có hướng, vùng sáng/tối tách vật thể khỏi UI.
- Tông vật liệu có chiều sâu, giới hạn noise và chi tiết dưới một pixel.
- Biểu tượng Việt Nam đúng hình, đúng thời kỳ và đúng nghĩa gameplay.

Thay đổi theo asset:
- Tả thực/cách điệu: portrait cần nhận dạng; decision cần tối giản.
- Khung: focus có thể là huy hiệu; spirit nhẹ; event/portrait thường không có.
- Nền: icon rời alpha; cảnh sự kiện và portrait có thể kín theo slot.
- Chất liệu: đồng/đá/vải ở ngoại giao; thép/radar ở quốc phòng; kính/mạch ở số hóa.

## 3. Palette và vật liệu theo nhóm nội dung

Các mã màu là gợi ý tạo board, không phải khóa RGB bắt buộc cho mọi pixel.

| Nhóm | Tông nền / tông khối | Điểm nhấn | Vật liệu và hình tượng |
|---|---|---|---|
| Ngoại giao | navy #0B2545, jade #1E8449 | brass #C5A059, crimson #DA251D | la bàn, treaty, tre, mốc; đồng, granite, lụa |
| Chính trị / nhà nước | burgundy #800020, slate #2D3748 | đỏ quốc gia, champagne | sách luật, con dấu, tòa nhà, lúa; giấy/đồng/sơn mài |
| Kinh tế / hạ tầng | graphite #263238, blue glass #2980B9 | amber #D89A35, green #2D8659 | cảng, turbine, wafer, đường; thép/kính/bê tông |
| Lục quân | olive #46513B, steel #56616D | đỏ/vàng nhận diện nhỏ | đơn vị, hậu cần, khí tài đúng thời kỳ |
| Hải quân / biển đảo | ocean #12354D, sea green #167D8D | trắng bọt sóng, brass | tàu, đảo, DK1, hải đăng; biển và kim loại |
| Không quân | blue-grey #496476, slate #34495E | trắng kim loại, amber | máy bay/radar/cánh; không thêm động cơ xanh sci-fi |
| An ninh / dữ liệu | dark teal #163A3F, charcoal #20262D | cyan #52BBC7 hoặc crimson | shield, network, relay; mạch có nghĩa, glow tiết chế |

Điểm nhấn cyan không thay cho màu sắc quốc kỳ hoặc emblem chính thức.
Bóng kim loại dùng mảng tối và cạnh bắt sáng; “NMM” là một kỹ thuật hữu ích,
không yêu cầu bề mặt nào cũng mạ vàng. Tả thực không đồng nghĩa phủ rỉ sét/sepia.

## 4. Silhouette và độ phức tạp theo slot

| Slot | Mức chi tiết phù hợp | Cách kể chuyện |
|---|---|---|
| Focus 93×91 | 1 vật thể chính + tối đa 1–2 yếu tố phụ | quyết sách/định hướng |
| Spirit 60×68 | 1 motif, khoảng trống rõ, khung nhẹ hoặc không khung | trạng thái lâu dài/buff/debuff |
| Decision 33×32 | 1 glyph/hành động, vài mảng lớn | động từ: kiểm tra, đầu tư, luân chuyển |
| Category 52×40 | nhóm 1–2 motif, nhìn khác nút hành động | lĩnh vực hoặc tổ chức |
| Event 210×176 | 1 hành động/cảnh, 2–3 lớp chiều sâu | một thời điểm lịch sử |
| Portrait 156×210 / 38×51 | khuôn mặt là vùng quan trọng nhất | người thật và vai trò |
| UI/BoP/MIO | theo slot đã đo | trạng thái, cấp độ, lĩnh vực |

Con số yếu tố phụ là hướng dẫn bố cục; điều chỉnh nếu mẫu cùng nhóm chứng minh
bố cục khác vẫn đọc rõ. Luôn xem bản final 1:1; phóng lớn chỉ để kiểm viền.
Sự khác nhau giữa icon không được dựa chỉ vào một dòng chữ cực nhỏ.

## 5. Khung và mức trang trọng

Xem [tập khung](05_nghien_cuu_va_thiet_ke_khung_focus.md).

- Ngoại giao VIE: có thể dùng khung vàng và ba sao của hai mẫu được chọn.
- Quân sự: silhouette khí tài hoặc shield nhẹ; tránh biến mọi icon thành huy chương.
- Hạ tầng/số hóa: bezel kỹ thuật hoặc vành mở nếu board cùng nhóm hỗ trợ.
- Spirit: bớt khung để motif chiếm ô nhỏ.
- Decision và trait: ưu tiên glyph rõ, không thu nhỏ nguyên badge focus.
- Event/portrait: không gắn vòng lá/ba sao nếu consumer không có yêu cầu.

Tách “khung bên trong ảnh” và “khung do GUI vẽ”. Đọc sprite/GUI trước để tránh
hai lớp viền. Khung ba sao không phải dấu xác nhận chuẩn quốc gia hoặc quy tắc MD.

## 6. Cờ, quốc huy, lịch sử và người thật

Dùng tư liệu đã xác minh cho quốc kỳ, quốc huy, ASEAN/LHQ và insignia quân phục.
Tập 2 là nguồn concept; kiểm tra lại những thông số chưa dẫn nguồn.

Quốc kỳ Việt Nam có tỷ lệ cao:rộng 2:3, nền đỏ và một sao vàng năm cánh
với đỉnh hướng lên. Palette có thể thay đổi dưới ánh sáng nhưng hình và số cánh
không được đổi. Không lẫn Đảng kỳ, Quốc kỳ, Quân kỳ, badge trang trí ba sao.
Không thêm “Quyết Thắng” vào mọi lá cờ.

Logo và chữ quan trọng cần kiểm tra sau generation. Nếu AI bịa nét/diacritics,
dùng nguồn vector/raster đáng tin và quy trình chỉnh sửa được công cụ hỗ trợ,
không chỉ ghi “logo chính xác” rồi coi là đúng.
Logo AI gần giống chỉ được ghi nhận là minh họa cách điệu, không là bản chính thức.

Nhân vật, tàu/máy bay, vũ khí và công trình phải khớp năm/chức vụ/version trong brief.
Dùng tưởng tượng cho alt-history đã được gameplay xác định; ghi nhãn concept.
Kiểm tra quyền sử dụng và provenance của ảnh tải; không bịa license cho ảnh AI.

## 7. Board tham chiếu và lô sản xuất

Trước lô lớn, chọn 3–5 mẫu cùng loại, gồm mẫu đơn giản, mẫu phức tạp và một
ảnh UI nếu có. Ghi nguồn, commit/ngày, canvas, frame, alpha và điều sẽ học từ mẫu.
Không lấy event panorama làm chuẩn bố cục decision 33×32.

Hai nguồn ngoại giao được chọn:
- assets/focus_icons/raw/asean_integration.png: mốc palette/vật liệu compass.
- assets/focus_icons/raw/border_settlement.png: mốc granite/độ sâu/khung.

Chúng có khung khá đậm và nhiều microdetail; khi tạo các mẫu tiếp theo phải
kiểm ở 93×91 để chủ thể không bị vành vàng lấn. Không coi chất lượng bản lớn
là bằng chứng bản nhỏ đã được người dùng duyệt trong game.

Làm mẫu đại diện theo nhóm đã được yêu cầu; nếu chỉ yêu cầu xem thử, dừng ở
sample/preview. Khi yêu cầu triển khai đã rõ, tiếp tục xuất, tích hợp và kiểm tra.
Mẫu dùng chung khung có thể đổi góc vật thể/silhouette; không lặp cùng đôi cờ
với một nhãn chữ khác.

## 8. Dấu hiệu lệch phong cách và cách sửa

| Dấu hiệu | Nguyên nhân thường gặp | Sửa có mục tiêu |
|---|---|---|
| Nhìn như loot mobile game | khung quá dày, vàng quá bóng, flare lớn | thu khung, bớt glow, tăng chủ thể |
| Neon phủ mọi nhánh | prompt “modern = cyberpunk” | xóa HUD không có ngữ nghĩa |
| Loang/bệt ở bản nhỏ | quá nhiều texture/microdetail | giảm chi tiết và nền, tăng khối chính |
| Icon nặng/dày hơn cùng hàng | scale và frame không đồng bộ | so 1:1, khớp vùng chiếm dụng |
| Hai focus khó phân biệt | chung vật thể hoặc silhouette | đổi metaphor và bố cục trước palette |
| Viền đen/xám ở alpha | RGB nền cũ hoặc alpha sai | kiểm checkerboard, đen và sáng, xử lý export |
| Portrait không giống người | sai nguồn/tuổi/tóc/cấu trúc mặt | quay lại tư liệu, không chỉ tăng độ nét |

## 9. Định nghĩa hoàn thành

Brief → board → master → preview đúng canvas → kiểm kỹ thuật →
mapping consumer → kiểm trong game khi có runtime.

Báo riêng “đã tạo”, “đã xuất”, “đã tích hợp”, “đã audit”, “đã xem trong game”.
Không nâng một bước thành bằng chứng cho bước sau.

