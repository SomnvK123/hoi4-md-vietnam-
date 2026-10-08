---
name: md-focus-art
description: 'Tạo hoặc thay icon National Focus cho MD Vietnam; giữ canvas 93x91, silhouette và frame theo nhánh, alpha và sprite mapping. Dùng cùng md-art.'
---

# Mỹ thuật National Focus

Đọc [md-art](../md-art/SKILL.md) và [khung](../../docs/art-style-guide/05_nghien_cuu_va_thiet_ke_khung_focus.md).
Mặc định VIE: 93×91 RGBA; RGB 32-bit DDS không nén, không mipmap, 33.980 byte.
Đây là profile checkout, không là kích thước duy nhất của mọi focus MD.

## Concept và nhận diện

Đọc focus ID, localisation và reward để hiểu quyết sách. Tập 3 cung cấp metaphor,
nhưng phải tra code live: tọa độ/năm/số focus trong concept không được coi là dữ kiện mới nhất.
Chọn một centerpiece riêng cho từng focus; tránh lặp hai cờ chéo + thay nhãn.
So với icon cùng nhánh ở 1:1; giữ lượng khung, sắc kim loại và quy mô chủ thể tương tự.

Ngoại giao có hai master đã chọn:
assets/focus_icons/raw/asean_integration.png và border_settlement.png.
Chúng là complete badge; không crop chỉ phần giữa hoặc đóng khung thêm lần nữa.
Ý nghĩa: compass định hướng ngoại giao; granite xác lập biên giới.
Ba sao, vòng lá và huy hiệu đỏ là lựa chọn nhóm này, không quy tắc toàn MD.

Chủ thể chính nên đọc trước frame. Giảm microdetail của compass/địa hình nếu bản nhỏ
bị rối; không chỉ tăng sharpen. Quân sự/số hóa có thể dùng frame nhẹ hoặc mở theo board.

## Tạo và xuất

1. Lưu master PNG alpha và prompt/tư liệu. Xem mẫu trước khi edit.
2. Tạo hình theo canvas gần tỷ lệ 93:91; giữ toàn silhouette và khoảng trống.
3. Khi xuất, dùng contain vào vùng tối đa 91×89 rồi đặt giữa 93×91 để giữ
   1 px alpha ngoài cùng. Không kéo dãn sai tỷ lệ; không thêm nền đen.
4. Lưu assets/focus_icons/png/<stem>.png và gfx/interface/goals/<stem>.dds.
5. Dùng write_dds của tools/build_vie_focus_icons.py cho RGB32 BGRA.
   Không chạy toàn bộ builder, vì có thể ghi lại assets/sprite ngoài phạm vi.
   Recipe hai mẫu đã dùng: assets/focus_icons/raw/README.md.
6. Kiểm DDS decode có cùng pixel RGBA với PNG, border alpha sạch,
   không mipmap và byte count phù hợp.

## Mapping và kiểm tra

Tìm sprite GFX_focus_VIE_<stem> trong interface/VIE_md_focus_icons.gfx và
icon của focus ở common/national_focus/VIE_md_focus.txt.
Nếu mapping đã đúng, chỉ thay texture; không sửa reward, prerequisite, cost hay vị trí.
Nếu phải thêm sprite, thêm đúng block, không tạo lại toàn file .gfx.

Chạy python3 tools/audit_dds_and_gfx.py; đọc mục DDS, texture và focus sprite.
Nếu đổi ID/mapping, kiểm riêng ID đó và python3 tools/audit/live.py.
Chỉ cần audit cây khi có thay đổi cây, không vì thay pixel đơn thuần.

Xem final 93×91 ở 1:1 trên nền tối/sáng và cạnh icon cùng nhánh.
Trong game: mở cây VIE, kiểm icon thường và shine/hover khi có runtime.
Báo rõ chưa chạy game nếu chỉ audit file.

