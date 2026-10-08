# Tập 4: Quy trình tạo, xuất, tích hợp và kiểm định tài nguyên

## 1. Profile kỹ thuật dựa trên consumer

Đo ngày 08/10/2026; chi tiết nguồn và số lượng ở
[đánh giá phân tích](06_review_modern_day_analysis.md).
Các profile là mặc định đã dùng trong VIE, không là chuẩn toàn engine/MD.
Trước asset mới, đọc .gfx/.gui/field gameplay và mẫu cùng slot.

| Loại | Canvas VIE đã đo | Nền/alpha | Export hiện có |
|---|---|---|---|
| Focus | 93×91 | rời trên alpha | RGB32 DDS BGRA, không mipmap |
| Idea / spirit | 60×68 | rời trên alpha | RGB32 DDS BGRA |
| Decision | 33×32 | rời trên alpha | RGBA TGA |
| Category texture hiện có | 52×40 | rời trên alpha | RGBA TGA; cần kiểm code còn dùng |
| Event picture | 210×176 | cảnh kín | DDS BC1/DXT1 |
| Portrait large | 156×210 | theo asset/slot | RGB32 DDS hoặc BC1/DXT1 |
| Portrait small | 38×51 | theo asset/slot | RGB32 DDS |
| BoP / MIO / trait / flag / other UI | phải tra slot | theo consumer | không suy ra từ focus |

Idea 64×64, decision 44×44, event 450×150 có thể dùng ở nơi khác,
nhưng không thay profile VIE hiện có nếu chưa kiểm GUI.
Master lớn theo tỷ lệ slot, không buộc mọi master vuông. Generator có thể trả
canvas khác yêu cầu; đọc file thật và xuất theo tỷ lệ thay vì báo kích thước từ prompt.

## 2. Hợp đồng xuất và DDS

RGBA mô tả kênh logic khi xử lý ảnh. DDS A8R8G8B8 với masks dưới đây dùng byte
BGRA trên đĩa little-endian. Chỉ viết tên “ARGB 8.8.8.8” chưa đảm bảo channel order đúng.

RGB32 DDS dùng trong các builder VIE:
- Magic: DDS + dấu cách; 4 byte.
- Header: 124 byte (tổng prefix+header 128).
- Pixel format: size 32, flags 0x41, FourCC=0, bitcount 32.
- R/G/B/A masks: 0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000.
- Pitch = width×4; không mipmap cho profile export hiện tại.
- Dung lượng chỉ khi RGB32 một level: 128 + width×height×4.

| RGB32 canvas | Dung lượng |
|---|---:|
| 93×91 | 33.980 byte |
| 60×68 | 16.448 byte |
| 33×32 (nếu chọn DDS thay TGA) | 4.352 byte |
| 52×40 (nếu chọn DDS thay TGA) | 8.448 byte |
| 210×176 (nếu chọn RGB32 thay BC1) | 147.968 byte |
| 156×210 | 131.168 byte |
| 38×51 | 7.880 byte |

Không áp công thức này lên TGA/DXT. BC1/DXT1 mã hóa block 4×4, 8 byte/block;
một level không mipmap có 128 + ceil(width/4)×ceil(height/4)×8 byte.
VIE event 210×176 BC1 một level là 18.784 byte. BC3/DXT5 có 16 byte/block
và alpha khác; chọn khi consumer cần và encoder đã kiểm hỗ trợ.

Compression có trade-off: BC1 dễ có block artifacts/banding và chỉ alpha 1-bit
ở chế độ hỗ trợ transparency; không dùng như RGBA mềm cho lá/cờ/portrait cutout.
Không kết luận file nén hợp lệ gây crash chỉ vì khác byte count RGB32.
Đổi format cần đọc lại file và kiểm consumer trong game khi có runtime.

Alpha icon: ngoài silhouette phải trong suốt thật; kiểm kênh alpha, không
suy từ nền checkerboard trong preview. Focus VIE xuất border 1 px alpha=0.
Cảnh event kín không bắt buộc border alpha; portrait theo slot, không cắt vòng tròn.
Đừng dùng crop/resize kéo méo hoặc sharpening/noise để đạt “2.500 màu”.

## 3. Quy trình từ yêu cầu đến triển khai

### Bước A: brief và phạm vi

Đọc [md-art](../../skills/md-art/SKILL.md), chọn skill theo loại, xem git status.
Lập [brief](templates/asset-brief.md): ID, nghĩa, năm, consumer, canvas,
frame, alpha, nguồn tham chiếu và sample hay triển khai.
Tra live code trước; không lấy ngày/tọa độ ở concept làm dữ kiện gameplay.

Texture có nhiều alias/consumer: xác định tác động trước khi thay.
Dùng sprite VIE riêng cho asset mới; tránh redefine generic base/MD.

### Bước B: reference board

Lấy mẫu cùng slot, xem ảnh thật, ghi nguồn/version và điều cần học:
silhouette, frame, vật liệu, palette, độ chi tiết, alpha.
Một board nhỏ cho nhóm mới đủ để quyết định; không tải toàn MD cho một icon.

Nếu chỉ có local sample không rõ nguồn, ghi “reference cục bộ chưa xác thực”.
Có nguồn upstream: lưu commit + URL + hash. Không tự lấy nguồn mạng có license
chưa biết rồi ghi public domain; generation AI không được gán license ảnh chụp.

### Bước C: prompt và generation

Mỗi prompt phải có:
- chủ thể/ý nghĩa và năm;
- một focal point, phụ cảnh phục vụ câu chuyện;
- mức stylization theo slot, frame hoặc không frame;
- palette/vật liệu/ánh sáng khớp board;
- transparency hoặc cảnh kín;
- chi tiết chính xác và tránh artifact;
- yêu cầu dễ đọc ở final canvas.

Công cụ ảnh có sẵn dùng để tạo/chỉnh artwork; xem reference trước edit.
Không tự tạo artwork bằng ImageDraw để thay yêu cầu gen.
Python/Pillow dùng kiểm tra, resize/conversion phục vụ export theo workflow
được hỗ trợ. Chỉnh logo/chữ hoặc mỹ thuật bằng phương thức mà công cụ/yêu cầu
hiện tại cho phép; không âm thầm dùng pipeline khác.

Một câu “Millennium Dawn style” không đủ. Không nhét suffix --ar/--no vào
công cụ không hỗ trợ. Thông số codec/canvas final thuộc bước export;
generator trả PNG master không tự cung cấp DDS game-ready.

### Bước D: review ở final size

Review sample lớn để nhận ý tưởng, nhưng bắt buộc xem 1:1 sau downsample.
Kiểm nền tối, nền sáng và checkerboard; ghép/preview bằng công cụ được hỗ trợ.
Chủ thể phải nhận ra ngay; frame/texture không làm cùng nhóm nặng hơn.

Chữ/logo/cờ: kiểm từng chi tiết; prompt “accurate” không là chứng nhận.
Không bịa logo chính thức từ ảnh AI. Portrait cần đối chiếu likeness và thời kỳ.

Yêu cầu xem mẫu: bàn giao mẫu. Đã yêu cầu tích hợp: tiếp tục bước E/F,
không hỏi lại duyệt workflow đã rõ. Không tự mở rộng thêm cả nhánh.

### Bước E: export có thể tái lập

Giữ master; không đổi tên extension để “chuyển format”.
Resize giữ tỷ lệ. Với complete badge ngoại giao, chứa toàn ảnh trong 91×89
rồi đặt giữa 93×91; không mask tròn/đóng khung thêm.
Centerpiece chưa có frame có quy trình khác, xem
[tập 5](05_nghien_cuu_va_thiet_ke_khung_focus.md).

Dùng hàm write_dds(path, image) ở tools/build_vie_focus_icons.py cho RGB32;
nó nhận size của ảnh. Import helper không đồng nghĩa chạy builder hàng loạt.
Đọc code trước khi dùng builders khác: chúng có thể overwrite .gfx, tải ảnh,
tạo placeholders hoặc rebuild nhiều stems.

Lưu master ở assets/<nhóm>/raw/, PNG xuất ở png/, export trong gfx/ theo slot.
Kèm [hồ sơ asset](templates/asset-record.md) và câu lệnh rebuild nếu không tự rõ.
Kiểm round-trip PNG → DDS màu/alpha và header; TGA đọc lại mode/size/alpha.
Không khẳng định master còn alpha nếu file thực tế không có.

### Bước F: mapping và nghiệm thu

Consumer đi theo đường cụ thể ở mục 5. Giữ mapping cũ nếu chỉ thay texture.
Thêm block sprite nhỏ khi cần, không recreate file .gfx.
Không đổi gameplay/cost/effects/vị trí khi yêu cầu chỉ đổi artwork.

Chạy audit file liên quan, tự kiểm loại field mà audit không bao phủ.
Game không có: báo “đã tích hợp texture/sprite, chưa xem trong game”.
Có game: xem đúng slot, hover/disabled, đúng event/character/year.
Không dùng preview ở localhost; screenshot/image trực tiếp đủ cho review.

## 4. Prompt templates theo loại

Thay nội dung trong dấu ngoặc nhọn bằng brief thật. Đây là gợi ý câu chữ,
không params bắt buộc hay style chính thức của một model.

**Focus ngoại giao**
~~~text
One complete diplomatic focus badge about {policy/year}, dominated by {centerpiece},
restrained modern emblem illustration with sculpted brass and {material},
{reference-matched wreath/frame}, directional warm light with cool fill,
navy/jade accents, clear silhouette readable at 93x91,
full badge visible with padding, transparent outside silhouette.
No unrelated HUD, no rectangular backdrop, no tiny caption.
~~~

**Idea / spirit**
~~~text
Compact symbolic illustration of {persistent state/buff/debuff},
one bold {motif}, restrained {branch material/palette}, lightweight frame or no frame,
large simple value shapes, readable at 60x68, transparent outside.
No landscape scene, no miniature focus wreath, no tiny lettering.
~~~

**Decision / category**
~~~text
A compact action glyph for {action}, dominated by {one symbol},
few large shapes with restrained dimensional shading,
{category palette}, readable at {verified final size}, transparent outside.
No decorative badge crown, no fine text, no dense map, no broad glow.
~~~

**Event**
~~~text
A modern historical editorial illustration of {event} in {place/year},
{verified subjects} doing {one action}, realistic period-appropriate materials,
{camera/composition matched to 210x176}, quieter background and clear focal point,
opaque scene, no emblem border, no caption or invented text.
~~~

**Portrait**
~~~text
An editorial painted portrait of {identified person} at {age/year/role},
preserve facial likeness from the supplied verified references,
{verified clothing/insignia}, head and shoulders with safe headroom,
restrained lighting and simple backdrop, large portrait framing 156x210,
a separate face-focused small crop will be exported at 38x51.
No invented decorations, no badge frame, no altered identity.
~~~

**UI/BoP/MIO**
~~~text
A {verified UI slot} symbol representing {state/trait/organization},
{motif}, {reference-matched material and line weight},
consistent silhouette scale with its sibling states,
readable at {verified size}, {alpha/frame requirements}.
No assumed focus wreath; follow the documented {frame/state contract}.
~~~

Không dùng template portrait nếu thiếu reference nhận diện.
Không gọi logo AI hoặc cảnh AI là bản chính thức/ảnh tư liệu.

## 5. Consumer và đường dẫn VIE

| Loại | Field và mapping cần đọc | Export thường dùng |
|---|---|---|
| Focus | icon full GFX_focus_VIE_* → .gfx texturefile | gfx/interface/goals/ |
| Idea | picture token → GFX_idea_<token> | gfx/interface/ideas/ |
| Decision/category | icon theo block live → sprite đã định nghĩa | gfx/interface/decisions/ |
| Event | picture full sprite → VIE_md_event_pictures.gfx | gfx/event_pictures/ |
| Character | portraits army/civilian large/small path hoặc advisor mapping | gfx/leaders/VIE/ và small/ |
| BoP/MIO/trait/UI | icon/sprite/GUI slot thực tế, frame/state | tra consumer |

Ví dụ đang tồn tại, không phải ID cần thêm:
- VIE_asean_integration → GFX_focus_VIE_asean_integration →
  gfx/interface/goals/asean_integration.dds.
- GFX_idea_VIE_military_rescue →
  gfx/interface/ideas/VIE_idea_military_rescue.dds.
- GFX_decision_VIE_civil_service_examination →
  gfx/interface/decisions/VIE_civil_service_examination.tga.
- VIE_army_phung_quang_thanh có army large/small paths trong character file.

Không phải mọi field dùng cùng tiền tố. Kiểm số frame/scale/effect nếu sprite
có thuộc tính ấy; không tạo sprite sheet bằng cách nối file tùy ý.
Sprite từ MD/base game có thể không xuất hiện trong checkout submod.

## 6. Lệnh kiểm tra không sửa tài nguyên

Chạy từ gốc repository. Inventory này đo cả TGA, không dựa vào bảng ghi nhớ:

~~~bash
python3 - <<'PY'
from collections import Counter
from pathlib import Path
from PIL import Image
for folder in ("gfx/interface/goals", "gfx/interface/ideas",
               "gfx/interface/decisions", "gfx/event_pictures", "gfx/leaders/VIE"):
    result = Counter()
    for path in Path(folder).rglob("*"):
        if path.suffix.lower() in (".dds", ".tga", ".png"):
            with Image.open(path) as img:
                img.load()
                result[(img.size, img.mode, path.suffix.lower())] += 1
    print(folder, dict(result))
PY
python3 tools/audit_dds_and_gfx.py
~~~

Ví dụ kiểm round-trip cho hai focus đã tích hợp:

~~~bash
python3 - <<'PY'
from pathlib import Path
from PIL import Image
import struct
for stem in ("asean_integration", "border_settlement"):
    png = Path("assets/focus_icons/png") / (stem + ".png")
    dds = Path("gfx/interface/goals") / (stem + ".dds")
    with Image.open(png) as p, Image.open(dds) as d:
        p.load(); d.load()
        assert p.size == d.size == (93, 91)
        assert p.convert("RGBA").tobytes() == d.convert("RGBA").tobytes()
        a = d.convert("RGBA").getchannel("A")
        for box in ((0,0,93,1),(0,90,93,91),(0,0,1,91),(92,0,93,91)):
            assert a.crop(box).getextrema() == (0, 0)
    data = dds.read_bytes()
    assert data[:4] == b"DDS " and len(data) == 33980
    pf = struct.unpack("<II4s5I", data[76:108])
    assert pf == (32, 0x41, b"\0\0\0\0", 32,
                  0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    print(stem, "export verified")
PY
~~~

Kiểm này xác minh hai file hiện có; thay asset thì cập nhật hồ sơ/profile thích hợp.
Đây không là bài test xem trong game.

## 7. QA phân lớp và giới hạn công cụ

| Lớp | Cần xác minh | Điều không thể suy ra |
|---|---|---|
| File | decode, size, alpha, masks/codec, frames | thẩm mỹ hoặc game render đúng |
| Mapping | ID → sprite/path → file; aliases | GUI/slot nằm ngoài checkout tự động đúng |
| Visual 1:1 | chủ thể, palette, frame, crop/likeness | chỉ master đẹp là đủ |
| Runtime | popup/panel, hover/disabled, đúng năm | audit exit=0 là runtime pass |

tools/audit_dds_and_gfx.py hiện kiểm DDS, texture .gfx, focus GFX và một phần
event pictures. Không kiểm đủ TGA, idea picture, decision/category fields,
character paths hoặc GUI state. Nó in cảnh báo generic MD references không có
trong submod; phải tra provider trước kết luận thiếu. Đọc output dù exit=0.

Chạy tools/audit/live.py nếu đổi ID/reference có liên quan; audit cây chỉ cần
khi đổi cấu trúc focus. Không chạy suite gameplay không liên quan cho thay pixel.
Giữ status/diff sạch ngoài phạm vi và báo cả skipped/unrun checks.
