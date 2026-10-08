# Millennium Dawn: Vietnam Submod (VIE)

Dự án submod hoàn chỉnh mở rộng quốc gia Việt Nam (`VIE`) trong mod **Millennium Dawn: Modern Day Mod** cho Hearts of Iron IV (phiên bản game `1.19.*`), tái hiện giai đoạn lịch sử hiện đại từ năm 2000 đến 2026+.

---

## 1. Tổng quan Dự án

- **Quốc gia mục tiêu:** Việt Nam (`VIE`)
- **Khung thời gian:** 2000 – 2026+ (Thời kỳ Đổi Mới, hiện đại hóa, hội nhập quốc tế)
- **Hệ thống chính trị & Đại hội Đảng:** Mô phỏng các kỳ Đại hội Đảng IX, X, XI, XII, XIII, XIV với các trục phát triển Kinh tế, Thể chế, An ninh và Quốc phòng.
- **Hệ thống Ngoại giao Đa phương:** Đường lối Đối ngoại độc lập tự chủ, Ngoại giao Cây tre, tiến trình hội nhập ASEAN, Đối tác Chiến lược Toàn diện với các cường quốc.
- **Hệ thống Quốc phòng & Quân sự:** 3 quân chủng Lục quân, Hải quân, Phòng không - Không quân, lực lượng tác chiến không gian mạng và công nghiệp quốc phòng.

---

## 2. Hệ sinh thái Chuẩn hóa & Hỗ trợ Phát triển (`.claude/`)

Hệ thống tài liệu, tiêu chuẩn kỹ thuật và bộ công cụ tự động hóa được tổ chức tập trung tại thư mục [`.claude/`](.claude/README.md):

- **[Cẩm nang Hướng dẫn Dự án (`.claude/CLAUDE.md`)](.claude/CLAUDE.md):** Quy tắc cứng, quy chuẩn mã nguồn, cơ chế trừ tiền quỹ quốc gia Millennium Dawn và quy trình commit.
- **[Hệ thống 3 Trụ cột Kỹ năng Chuẩn hóa (`.claude/skills/README.md`)](.claude/skills/README.md):** 3 skill master chuyên biệt (`md-focus`, `md-art`, `validate`) hỗ trợ tự động hóa toàn bộ vòng đời phát triển submod.
- **[Bộ Cẩm nang Mỹ thuật Submod (`.claude/docs/art-style-guide/README.md`)](.claude/docs/art-style-guide/README.md):** Chuẩn hóa toàn bộ phong cách đồ họa, khoa học màu sắc Chiaroscuro, giải pháp công nghệ DDS và biểu tượng văn hóa Việt Nam.
- **[Kho Tài nguyên Đồ họa Nguồn (`assets/README.md`)](assets/README.md):** Quản lý toàn bộ source PNG, RAW master renders, thông tin bản quyền và quy tắc đồng bộ 1:1 với `gfx/`.
- **[Hướng dẫn Kiểm tra & Nghiệm thu (`.claude/docs/validation.md`)](.claude/docs/validation.md):** Các công cụ kiểm tra tự động cây focus, tính toàn vẹn tham chiếu chéo, định dạng DDS và ngôn ngữ.

---

## 3. Hệ thống 3 Kỹ năng Master Chuẩn hóa

| Trụ cột | Tên Skill | Chức năng chính |
|---|---|---|
| **[1. Focus]** | [`md-focus`](.claude/skills/md-focus/SKILL.md) | Toàn diện vòng đời National Focus: workflow thêm mới, kiến trúc cây, reward/tiền treasury, icon $93\times 91$ px và loc |
| **[2. Mỹ thuật]** | [`md-art`](.claude/skills/md-art/SKILL.md) | Cẩm nang & Quy trình sản xuất đồ họa toàn diện: Focus, Idea, Decision, Event, Portrait, UI, chuẩn uncompressed DDS/TGA |
| **[3. Kiểm thử]** | [`validate`](.claude/skills/validate/SKILL.md) | Bộ kiểm tra tĩnh tự động (`audit.py`, `live.py`, `prov.py`), thẩm định ngôn ngữ localisation và checklist review PR trước khi merge |

---

## 4. Công cụ Kiểm tra Thường dùng

Chạy từ thư mục gốc của repository:

```bash
# Kiểm tra cấu trúc cây National Focus (toạ độ, prerequisite, relative_id)
python tools/audit/audit.py

# Kiểm tra tham chiếu chéo toàn diện (effect, trigger, idea, modifier thật của MD)
python tools/audit/live.py

# Kiểm tra tính toàn vẹn ngôn ngữ và dịch thuật
python tools/verify_all_loc.py

# Kiểm tra định dạng DDS (kích thước, 32-bit BGRA, 33.980 byte) và khai báo GFX
python tools/audit_dds_and_gfx.py
```
