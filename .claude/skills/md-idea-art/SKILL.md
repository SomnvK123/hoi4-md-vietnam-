---
name: md-idea-art
description: 'Tạo national spirit, idea hoặc law icon VIE với motif cô đọng, kiểm picture-to-GFX_idea mapping, canvas và alpha thực tế; tránh ghi đè sprite generic của MD.'
---

# Mỹ thuật Idea / National Spirit / Law

Đọc [md-art](../md-art/SKILL.md). Idea diễn tả trạng thái/bản sắc/buff hoặc debuff,
khác focus diễn tả một lựa chọn và decision diễn tả một hành động.
Đọc tên, mô tả, modifier, thời hạn và các biến thể của idea trước khi chọn hình.

## Profile và bố cục

Sáu DDS VIE hiện có: 60×68 RGBA, RGB32 BGRA không nén, không mipmap,
16.448 byte = 128 + 60×68×4. Đừng thay mặc định thành 64×64 hoặc 156×156.
Kiểm texture/slot mục tiêu trước khi thêm nhóm mới.

Ưu tiên một motif lớn, ít layer, khoảng trống rõ. Không thu nhỏ nguyên badge focus.
Dùng vật liệu cùng branch nhưng frame nhẹ hoặc không frame; tránh text nhỏ và HUD dày.
Buff/debuff phải khác nhau bằng silhouette/chi tiết, không chỉ xanh/đỏ.
Ví dụ: năng lực hậu cần dùng thùng hàng + đường vận chuyển; thiếu hụt dùng
thùng rỗng/đường gián đoạn, cùng palette và vùng chiếm dụng.

## Generation và export

Prompt: “compact symbolic illustration of <state>, one dominant motif,
restrained <branch> material shading, readable at 60x68 pixels,
lightweight framing, isolated on transparent background”.
Thay placeholders, thêm ý nghĩa và reference thực tế; không cố định mã màu bằng prompt.

Lưu source/provenance, PNG, rồi DDS trong gfx/interface/ideas/.
Theo codec/header đã đo; alpha mềm giữ silhouette, không halo.
Dùng helper write_dds tổng quát sau khi kiểm signature; kiểm round-trip pixel.
Không gọi build_ideas_icons.py không chọn lọc: script build lại nhiều tài nguyên
và đăng ký một số generic alias.

## Consumer và QA

Idea thường có picture = <token>, engine dùng tên GFX_idea_<token>.
Tra block thực tế và sprite trong interface/*.gfx; không thêm tiền tố GFX_
vào picture một cách máy móc.
Chọn token VIE riêng, ví dụ picture = VIE_military_rescue chỉ khi sprite
GFX_idea_VIE_military_rescue thật sự được định nghĩa.

Liệt kê alias trỏ texture nếu overwrite; không định nghĩa lại generic sprite MD
cho icon VIE mới. Aliases có sẵn chỉ thay khi nằm trong phạm vi được yêu cầu.

Kiểm sprite/path/alpha, xem 60×68 1:1 trong một hàng national spirits.
Chạy python3 tools/audit_dds_and_gfx.py cho DDS/path; tool này không xác minh
mọi idea picture token. Kiểm trực tiếp từng picture → sprite.
Nếu có game: xem thanh spirit, law slot và tooltip theo đúng consumer.

