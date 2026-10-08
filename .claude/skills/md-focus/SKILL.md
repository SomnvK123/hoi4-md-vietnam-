---
name: md-focus
description: 'Toàn bộ quy trình và chuẩn mực National Focus MD Vietnam: thêm focus mới, cấu trúc cây & bố cục, quy chuẩn Millennium Dawn, reward/treasury, thiết kế & đăng ký icon DDS (93x91, 33.980B), loc và checklist nghiệm thu.'
---

# Cẩm nang Toàn diện National Focus Millennium Dawn (MD Vietnam)

Dùng cho mọi công việc liên quan đến National Focus trong `common/national_focus/VIE_md_focus.txt`:
từ tạo focus mới, tái bố cục nhánh, viết reward/tiền tệ theo chuẩn Millennium Dawn, đến thiết kế/đăng ký icon đồ họa và kiểm thử khép kín.

Nguồn đối chiếu chuẩn MD:
- Ba cây tham chiếu: `D:\ide\Millennium-Dawn\common\national_focus\` (`05_germany.txt`, `05_china.txt`, `05_thailand.txt`).
- Tài liệu MD: `D:\ide\Millennium-Dawn\docs\src\content\resources\` (`focus-tree-design-principles.md`, `code-stylization-guide.md`, `content-review-guide.md`, `search-filters.md`).
- Quy ước riêng VIE: `.claude/docs/conventions.md`, `VIE_focus_coding_standards.md` và `.claude/docs/art-style-guide/`.

---

## 1. Quy trình Thêm Focus Mới từ A-Z (Workflow)

Khi nhận yêu cầu thêm focus (ví dụ `/new-focus VIE_xyz dưới VIE_abc` hoặc thiết kế nhánh mới):

1. **Xác định vị trí & Anchor:**
   - Tìm focus cha (prerequisite). Chọn `relative_position_id` là một prerequisite trực tiếp khai báo trước nó.
   - Mặc định con nằm ngay dưới cha: `y = 1`, `x` lệch anh em $\pm 1$ đến $\pm 2$.
   - Chèn khối code focus **sau** anchor của nó trong `VIE_md_focus.txt`.
2. **Khai báo nội dung theo chuẩn:**
   - ID: `VIE_<tên_ngắn_gọn>`.
   - Cost: `5` (focus nhánh nhỏ/bước đệm) hoặc `7` (chính sách lớn/đổi mới/capstone).
   - Icon: `GFX_focus_VIE_<stem>` (xem Mục 5 về chuẩn đồ họa).
   - `search_filters`: Gán đúng danh mục (chính trị, kinh tế, quân sự, nghiên cứu).
   - `available`: Điều kiện mở (ngày tháng, cờ sự kiện, đảng phái).
   - `ai_will_do`: Trọng số AI với các điều kiện guard rõ ràng (Mục 4).
   - `completion_reward`: Thiết kế reward đa dạng, trừ tiền quỹ quốc gia đúng chuẩn (Mục 3).
3. **Khai báo Dịch thuật (Localisation):**
   - Thêm vào `localisation/english/replace/VIE_md_vi_p<N>_b_l_english.yml`:
     - `VIE_<id>:0 "Tên tiếng Việt hiển thị"`
     - `VIE_<id>_desc:0 "Mô tả bối cảnh và ý nghĩa quyết sách..."`
4. **Đăng ký Đồ họa (Icon):**
   - Tạo file PNG master -> xuất DDS $93\times 91$ px (chuẩn 33.980B) vào `gfx/interface/goals/<stem>.dds`.
   - Khai báo `spriteType` vào `interface/VIE_md_focus_icons.gfx`.
5. **Kiểm tra Nghiệm thu:**
   - Chạy `python tools/audit/audit.py` (cây focus).
   - Chạy `python tools/verify_all_loc.py` (dịch thuật).
   - Chạy `python tools/audit_dds_and_gfx.py` (texture đồ họa).

---

## 2. Nguyên tắc Bố cục & Bố trí Nhánh (Architecture & Layout)

Đọc chi tiết tại [references/focus-branch-design.md](references/focus-branch-design.md).

- **Phụ thuộc nội bộ bằng Prerequisite:** Hiện rõ quan hệ cha-con bằng `prerequisite = { focus = ... }` (AND) hoặc khối lồng (OR). Đặt con thấp hơn mọi cha. Tuyệt đối không dùng `available` chỉ để giấu đường nối hay làm phẳng cây một cách giả tạo.
- **Không kéo chuỗi tuyến tính rỗng:** Tránh chuỗi 4-5 focus chỉ cộng dồn chỉ số tĩnh. Tạo ra các ngã rẽ lựa chọn chính sách có đánh đổi thực sự.
- **Không `mutually_exclusive` cỡ lớn:** Mutex chỉ dùng cho lựa chọn chính sách loại trừ nhau ngay tức thì, không khóa vĩnh viễn cả một cụm năng lực dài hạn.
- **Capstone mở:** Focus cuối nhánh phản ánh sự hội tụ của nhiều hướng đi thành công hợp lệ, không ép buộc người chơi phải đi duy nhất một đường độc đạo.
- **Khoảng cách toạ độ:** Gap cùng hàng giữa các nút anh em tối thiểu $\ge 2$ để tránh đè giao diện. Điểm hội tụ nằm thấp hơn tất cả các nhánh cha.

---

## 3. Cấu trúc Code & Thứ tự Trường dữ liệu chuẩn MD

Mỗi khối focus trong `VIE_md_focus.txt` phải tuân thủ nghiêm ngặt thứ tự trường sau:

```pdx
focus = {
    id = VIE_focus_name
    icon = GFX_focus_VIE_focus_name

    x = 0
    y = 1
    relative_position_id = VIE_parent_focus

    cost = 7

    prerequisite = { focus = VIE_parent_focus }
    # mutually_exclusive = { focus = VIE_alternative_focus }

    search_filters = { FOCUS_FILTER_POLITICAL FOCUS_FILTER_ECONOMY }

    available = {
        # Điều kiện mở khóa
    }

    bypass = {
        # Điều kiện nhảy cóc (nếu có)
    }

    ai_will_do = {
        factor = 10
        modifier = {
            factor = 0
            # AI guard
        }
    }

    completion_reward = {
        log = "[GetDateText]: [Root.GetName]: Focus VIE_focus_name"
        # Scripted effects & rewards
    }
}
```

---

## 4. Thiết kế Reward Effect đa dạng & Cơ chế Trừ tiền Millennium Dawn

### A. Quy tắc trừ tiền (Treasury Change)
**Tuyệt đối không dùng `add_building_construction` trần để xây dựng nhà máy/công trình kinh tế.** Mọi khoản chi ngân sách quốc gia phải đi qua hệ thống tài chính của Millennium Dawn:
- Dùng scripted effect:
  ```pdx
  one_state_office = yes              # Văn phòng hành chính
  one_state_agri = yes                # Nông nghiệp
  one_random_civilian_factory = yes   # Nhà máy dân sự ngẫu nhiên
  ```
- Hoặc trừ tiền treasury trực tiếp:
  ```pdx
  set_temp_variable = { treasury_change = -15 }
  modify_treasury_effect = yes
  ```
- Công trình theo province (bunker, coastal_bunker, naval_base) bắt buộc phải có tham số `province = <ID>`.

### B. Cơ cấu Reward đa dạng (Không chỉ cộng PP/Stability)
1. **Kinh tế / GDP:** Tăng năng suất (`productivity_modifier`), tăng chi tiêu R&D, mở rộng văn phòng, cảng biển.
2. **Quân sự:** Giảm thời gian huấn luyện, mở variant trang bị qua scripted effect, kinh nghiệm quân chủng, học thuyết quân sự.
3. **Xã hội & Thể chế:** Điều chỉnh luật pháp, tăng tính giải trình, giảm tham nhũng, điều chỉnh cán cân quyền lực (BoP).
4. **Log đầu ra:** Mọi `completion_reward` phải mở đầu bằng dòng log chuẩn:
   ```pdx
   log = "[GetDateText]: [Root.GetName]: Focus VIE_<id>"
   ```

---

## 5. Tiêu chuẩn Mỹ thuật Icon Focus & Đăng ký GFX

Mọi focus icon của VIE phải tuân thủ nghiêm ngặt các quy chuẩn đồ họa:

1. **Quy cách file:**
   - Kích thước: Đúng $93\times 91$ px RGBA.
   - Định dạng: 32-bit BGRA uncompressed DDS, **không mipmap**, dung lượng chính xác **33.980 bytes**.
   - Alpha viền: Viền ngoài cùng 1 pixel ($x=0, x=92, y=0, y=90$) bắt buộc có Alpha = 0 để tránh vệt đen viền trong engine Clausewitz.
2. **Phong cách Thẩm mỹ (3D Heraldic Relief):**
   - Chủ thể là biểu tượng nổi khối (vũ khí, tài liệu, ấn chương, công trình, phương tiện), chiếm **80–85% diện tích**.
   - Không ép ảnh phong cảnh thu nhỏ vào vòng tròn 62px làm mờ nhạt chi tiết.
   - Áp dụng bộ lọc **Unsharp Mask ($180\%$, threshold 1)** khi downscale từ master sang $93\times 91$ px.
   - Vòng nguyệt quế / khung kim loại vẽ sơn dầu tả thực với bóng đổ ambient mềm mại.
3. **Đăng ký Sprite trong `interface/VIE_md_focus_icons.gfx`:**
   ```pdx
   spriteType = {
       name = "GFX_focus_VIE_<stem>"
       texturefile = "gfx/interface/goals/<stem>.dds"
   }
   ```
4. **Lưu trữ:**
   - File chơi: `gfx/interface/goals/<stem>.dds`
   - File nguồn: `assets/focus_icons/png/<stem>.png`

---

## 6. Chuẩn Dịch thuật (Localisation) & Tooltip

1. **Quy tắc file:** Dịch tiếng Việt có dấu đặt trong `localisation/english/replace/VIE_md_vi_p<N>_b_l_english.yml`.
2. **Cặp key bắt buộc:**
   - `VIE_<id>:0 "Tiêu đề focus"`
   - `VIE_<id>_desc:0 "Mô tả chi tiết nội dung và ý đồ chính sách"`
3. **Mã màu Clausewitz:**
   - `§Y...§!` cho số liệu, danh từ riêng, ngày tháng.
   - `§G...§!` cho hiệu ứng tích cực / buff.
   - `§R...§!` cho hiệu ứng tiêu cực / debuff / cảnh báo.
   - `§W...§!` cho chữ trắng nhấn mạnh.
4. **Custom Tooltip:**
   Khi reward phức tạp hoặc điều kiện ẩn, dùng `custom_effect_tooltip` hoặc `custom_trigger_tooltip` với key rõ nghĩa, tránh để người chơi đọc code thô.

---

## 7. Checklist Nghiệm thu Focus (15 Tiêu chí Vàng)

Trước khi coi một focus hoặc nhánh focus là hoàn thành, phải vượt qua checklist 15 điểm:

- [ ] 1. **Toạ độ & Anchor:** Không trùng toạ độ tuyệt đối với focus khác; `relative_position_id` trỏ đúng vào cha phía trên.
- [ ] 2. **Không vòng lặp:** Cây quan hệ cha-con khép kín, không có prerequisite lặp hoặc forward-reference.
- [ ] 3. **Cost hợp lệ:** Cost là 5 hoặc 7 (tuân thủ nhịp độ gameplay của VIE).
- [ ] 4. **Trừ tiền đúng:** Mọi chi phí đầu tư đều qua scripted effect MD hoặc `modify_treasury_effect`.
- [ ] 5. **Scope State an toàn:** Chỉ scope vào các state VIE sở hữu (518-524, 526, 801, 802, 813, 816).
- [ ] 6. **Tham chiếu khép kín:** Mọi effect, trigger, idea, event gọi trong focus phải tồn tại thật.
- [ ] 7. **Log chuẩn:** Khối reward có dòng `log = "[GetDateText]: [Root.GetName]: Focus ..."` ở đầu.
- [ ] 8. **AI Guard:** AI will do có factor hợp lý và modifier guard ngăn AI tự hủy hoặc min-max phi lịch sử.
- [ ] 9. **Search Filters:** Gán ít nhất 1 search filter phù hợp.
- [ ] 10. **Loc đầy đủ:** Cả `VIE_<id>` và `VIE_<id>_desc` đều có mặt trong file yml replace.
- [ ] 11. **Icon tồn tại:** Icon sprite `GFX_focus_VIE_<stem>` trỏ đúng file DDS có trên đĩa.
- [ ] 12. **DDS chuẩn:** File DDS đúng $93\times 91$ px, đúng 33.980 bytes, 1px alpha viền ngoài.
- [ ] 13. **Chủ thể rõ nét:** Icon không bị mờ nhòe, nhận diện được chủ thể ở tỷ lệ 1:1 trong game.
- [ ] 14. **Audit sạch:** Chạy `python tools/audit/audit.py` trả về 0 lỗi.
- [ ] 15. **Nhật ký thay đổi:** Cập nhật dòng `## vN (dd/mm/yyyy)` ở đầu `VIE_md_focus.txt`.
