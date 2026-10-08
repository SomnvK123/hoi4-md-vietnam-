# Cấu trúc Hệ thống Hỗ trợ Phát triển `.claude/` (MD Vietnam)

Thư mục `.claude/` là trung tâm cấu hình, tài liệu kỹ thuật, quy tắc mã hóa và kỹ năng chuyên biệt cho quá trình phát triển submod **Millennium Dawn: Vietnam** (nhắm đến Hearts of Iron IV phiên bản `1.19.*`).

---

## 1. Bản đồ Thư mục `.claude/`

```
.claude/
├── CLAUDE.md               # [CẨM NANG CHÍNH] Quy ước repository, quy tắc cứng và lệnh kiểm tra
├── README.md               # [FILE NÀY] Tổng quan và mục lục điều hướng hệ sinh thái .claude/
│
├── skills/                 # Hệ thống 3 Kỹ năng Master Chuẩn hóa
│   ├── README.md           # [CATALOG] Danh mục chi tiết, phân loại và quy trình phối hợp 3 master skills
│   ├── md-focus/           # [TRỤ CỘT 1] Toàn diện về National Focus (workflow, chuẩn MD, icon 93x91, loc)
│   ├── md-art/             # [TRỤ CỘT 2] Toàn diện về Mỹ thuật & Đồ họa (focus, idea, decision, event, portrait, UI)
│   └── validate/           # [TRỤ CỘT 3] Toàn diện về Kiểm thử tĩnh, Dịch thuật (loc) và Code Review (PR)
│
├── docs/                   # Cẩm nang kỹ thuật & Hướng dẫn thiết kế chuyên sâu
│   ├── art-style-guide/    # Bộ tài liệu Art Bible toàn diện (8 tập phân tích phong cách & quy chuẩn)
│   ├── mod-overview.md     # Cấu trúc thư mục, prefix VIE_ và namespace
│   ├── conventions.md      # Quy ước lập trình focus, effect, decision, idea, tiền tệ
│   ├── engine-pitfalls.md  # Các cạm bẫy engine Clausewitz (scope, FROM, guard)
│   ├── bug-patterns.md     # Mô hình lỗi thường gặp và cách khắc phục
│   ├── known-issues.md     # Danh sách lỗi tồn đọng và nợ kỹ thuật đã ghi nhận
│   ├── localisation.md     # Hướng dẫn viết localisation, mã màu và getter
│   └── validation.md       # Cẩm nang chạy bộ script kiểm tra và đọc log
│
├── agents/                 # Cấu hình các Sub-agent chuyên biệt (Dev, Art, QA)
└── rules/                  # Các quy tắc kiểm tra ràng buộc cục bộ
```

---

## 2. Tài liệu Cốt lõi & Điểm bắt đầu (Quick Links)

1. **Bắt đầu làm việc:** Đọc [`.claude/CLAUDE.md`](CLAUDE.md) để nắm rõ quy tắc cứng, danh mục scripted effect của Millennium Dawn và các lệnh kiểm tra trước khi commit.
2. **Hệ thống Kỹ năng:** Đọc [`.claude/skills/README.md`](skills/README.md) để tra cứu cách gọi và phối hợp 12 skills trong các tác vụ phát triển.
3. **Mỹ thuật & Đồ họa:** Đọc [`.claude/docs/art-style-guide/README.md`](docs/art-style-guide/README.md) để áp dụng chuẩn màu sắc Chiaroscuro, biểu tượng chính thống của Việt Nam và quy chuẩn kỹ thuật xuất DDS.
4. **Kiểm tra & Nghiệm thu:** Đọc [`.claude/docs/validation.md`](docs/validation.md) để chạy các công cụ kiểm tra tĩnh trong `tools/`.
