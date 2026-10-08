# Kho Tài nguyên Đồ họa Gốc (`assets/`)

Thư mục lưu trữ toàn bộ tài nguyên đồ họa nguồn (source assets), ảnh RAW gốc độ phân giải cao, ảnh PNG chuẩn bị xuất, metadata bản quyền và công cụ build/export cho mod **Millennium Dawn: Vietnam Submod**.

---

## 1. Cấu trúc Thư mục

```
assets/
├── event_pictures/     # Tài nguyên cho Event Pictures
│   ├── CREDITS.json    # Nguồn gốc, tác giả và giấy phép Commons của 56 ảnh
│   ├── png/            # 56 ảnh PNG đã crop kích thước 210x176 px
│   └── raw/            # 56 ảnh JPG chất lượng gốc từ nguồn tài liệu
│
├── focus_icons/        # Tài nguyên cho National Focus Icons
│   ├── CREDITS.json    # Nguồn ảnh và tác giả cho các icon Wikimedia
│   ├── selection.json  # Toạ độ crop tự động cho pipeline Wikimedia
│   ├── preview.png     # Bảng tổng hợp (contact sheet) kiểm tra visual
│   ├── png/            # 229 icon PNG chuẩn 93x91 px (đồng bộ 1:1 với gfx/interface/goals/)
│   ├── raw/            # Master render độ phân giải cao (1024x1024) & pipeline xuất
│   └── previews/       # Ảnh preview native/large phục vụ review theo batch
│
└── ideas/              # Tài nguyên cho National Spirit / Ideas
    └── png/            # 6 icon PNG chuẩn 60x68 px (đồng bộ 1:1 với gfx/interface/ideas/)
```

---

## 2. Tiêu chuẩn Kỹ thuật Đồ họa

Mọi asset trong thư mục này tuân thủ nghiêm ngặt tiêu chuẩn đồ họa tại [`.claude/skills/md-art/`](../.claude/skills/md-art/SKILL.md) và [`.claude/docs/art-style-guide/`](../.claude/docs/art-style-guide/README.md):

| Loại Asset | Thư mục PNG | Kích thước | Tương ứng trong `gfx/` | Định dạng Ingame |
| :--- | :--- | :--- | :--- | :--- |
| **Focus Icon** | `assets/focus_icons/png/` | $93 \times 91$ px | `gfx/interface/goals/*.dds` | 32-bit BGRA Uncompressed (33.980 byte), 1px viền trong suốt |
| **Idea / Spirit** | `assets/ideas/png/` | $60 \times 68$ px | `gfx/interface/ideas/*.dds` | 32-bit BGRA Uncompressed, alpha chuẩn |
| **Event Picture** | `assets/event_pictures/png/` | $210 \times 176$ px | `gfx/event_pictures/*.dds` | 32-bit DDS / DXT1 tuỳ engine |

---

## 3. Quy tắc Đồng bộ và Tính Toàn vẹn (1:1 Sync)

1. **Đồng bộ 1:1 giữa `assets/<type>/png/` và `gfx/`**:
   - Mỗi file DDS trong `gfx/interface/goals/` đều có một file PNG tương ứng trong `assets/focus_icons/png/`.
   - Mỗi file DDS trong `gfx/interface/ideas/` đều có một file PNG tương ứng trong `assets/ideas/png/`.
   - Mỗi file DDS trong `gfx/event_pictures/` đều có một file PNG tương ứng trong `assets/event_pictures/png/`.

2. **Bảo tồn Master Render**:
   - Các file master độ phân giải cao (như ngoại giao ASEAN, Cây tre, Lào, HĐBA,...) được bảo quản trong `assets/focus_icons/raw/` cùng với file prompt JSON và script xuất tự động.
   - Không xóa bỏ các master đã được phê duyệt.

3. **Kiểm tra tính toàn vẹn**:
   - Sử dụng `python tools/audit_dds_and_gfx.py` để tự động kiểm tra kích thước, header DDS và liên kết spriteType trong `interface/*.gfx`.
