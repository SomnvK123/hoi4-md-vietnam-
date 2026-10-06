# Localisation

Thư mục `localisation/english/` chứa toàn tiếng Việt (tên thư mục và `l_english:` chỉ để HOI4 nạp).
Đừng dịch sang tiếng Anh và đừng thêm ngôn ngữ khác nếu người dùng không yêu cầu.

## Định dạng

- UTF-8 **có BOM**, dòng đầu `l_english:` không thụt lề. Mỗi key thụt đúng 1 dấu cách, không tab,
  cả file cùng một kiểu thụt.
- Mod dùng `key:0 "text"` (có số phiên bản `0`). Giữ nguyên kiểu này trong mọi file để nhất quán.
- Escape ngoặc kép trong chuỗi: `\"`. Xuống dòng `\n`.
- Mỗi key một định nghĩa. Trùng key trong cùng thư mục: định nghĩa sau thắng.

## Quy tắc key

- Focus: `VIE_<slug>` và `VIE_<slug>_desc`. Decision, idea cùng kiểu. Idea `name = X` dùng `X` và `X_desc`.
- Event: `id.t`, `id.d`, `id.a`, `id.b`... (hidden event không cần).
- Tooltip tuỳ chỉnh: `VIE_tt_*`. Mọi `custom_effect_tooltip` / `custom_trigger_tooltip` phải có key thật,
  nếu không game hiện nguyên tên key.
- Trigger trong `NOT`: nếu dùng `custom_trigger_tooltip`, cần thêm key `<key>_NOT`.
- Mỗi focus, decision, event hiển thị, idea, tooltip mới phải có loc. Chạy `loc-check` sau khi thêm.

## `replace/` ghi đè thư mục cha

Key trùng giữa `localisation/english/*.yml` và `localisation/english/replace/*.yml`: bản trong `replace/` thắng.
Hiện có khoảng 545 key trùng kiểu này, khoảng 444 key có nội dung khác nhau, tức bản ở thư mục cha là chữ chết.

- **Trước khi sửa một key**, grep key đó trong cả hai thư mục và sửa bản đang thắng (thường là `replace/`).
- Key mới đặt ở file thường, không đặt vào `replace/` trừ khi cố ý ghi đè.
- Khi dọn: xoá bản chết ở thư mục cha, không đổi bản đang hiển thị trừ khi người dùng muốn.

## Màu và định dạng

- Mã màu dùng: `§Y` (thuật ngữ, tên riêng), `§G` (kết quả tốt), `§R` (kết quả xấu, cảnh báo),
  `§W` cho đường kẻ phân cách `§W--------------§!`. Luôn đóng bằng `§!`.
- Không dùng `§` trong tiêu đề focus. Mô tả dùng `§Y`/`§G`/`§R`.
- Ký tự `§` thật viết `§§`. Một `§` lẻ luôn bắt đầu mã màu và làm tràn `error.log` nếu sau nó không phải màu.
- Bảo toàn nguyên văn token động: `§Y...§!`, `£icon`, `\n`, `[Scope.GetName]`, `[?var|format]`, `[!trigger]`,
  scripted loc `[...]`. Đúng chính tả getter: `GetNameWithFlag`, không phải `GetNamewithFlag`.
  Getter sai render ra rỗng và không báo lỗi.
- Mod hiện còn dùng `§g`, `§B`, `§C`, `§O` ở một số file. Khi chạm vào dòng đó, đổi về bộ `Y/G/R/W`.

## Văn phong (nội dung người chơi thấy)

- Có dấu đầy đủ, chính tả đúng, câu hoàn chỉnh. Ngắn gọn, mỗi câu có thông tin thật.
- Tiêu đề focus/idea 3 đến 6 từ, viết hoa chữ đầu theo quy ước tiếng Việt, không mã màu.
- Mô tả 1 đến 3 câu về ý nghĩa lịch sử/chính trị. Không nhắc lại số liệu modifier đã hiện trong tooltip.
- Option event là hành động của người chơi ("Tăng ngân sách quốc phòng"), không phải mô tả thụ động.
- Không `TODO`, không `...`, không em dash (—) trong chuỗi hiển thị (hiện còn khoảng 82 dòng, dọn dần).
- Số liệu cơ chế (thời lượng, %, tiền) phải khớp effect thật. Đổi effect thì sửa loc.

## Loc cho hệ thống mới

Mỗi hệ thống có file riêng `VIE_md_events_<hệ thống>_l_english.yml`, `VIE_<hệ thống>_l_english.yml`.
Tạo file mới theo mẫu (BOM, `l_english:`), không nhét vào file của hệ thống khác.
