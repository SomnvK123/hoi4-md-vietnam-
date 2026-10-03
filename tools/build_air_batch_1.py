"""Script to build Batch 1 Focus Icons for Vietnam Air Force & Air Defense (PK-KQ & APM) in Millennium Dawn.
Batch 1 focuses (Trục 2 Công nghiệp Quốc phòng Hàng không & Nhà máy A32/A31 - 7 focuses):
1. apm_law: Thể chế Công nghiệp Quốc phòng Hàng không (Tổ hợp CNQP hàng không, bánh răng, cánh bay bạc, sao vàng)
2. apm_a32: Nhà máy A32: đại tu và kéo dài niên hạn (Động cơ phản lực AL-31F trên bệ thử, bánh răng kỹ thuật, sao vàng)
3. apm_a31: Nhà máy A31: tên lửa phòng không (Bệ phóng tên lửa SAM đa ống trong vành nguyệt quế, cánh bay PK-KQ, sao vàng)
4. apm_radar: Radar và chỉ huy – điều khiển nội địa (Đài radar cảnh giới nhìn vòng VRS-2DM, vòng quét radar, sao vàng)
5. apm_integration: Tích hợp vũ khí và hệ thống đa nguồn (Mạng liên kết công nghệ, vi mạch xử lý đa nguồn, sao vàng)
6. apm_uav: Chương trình UAV nội địa (UAV trinh sát hiện đại trên khiên đỏ kim cương và vành nguyệt quế vàng, sao vàng)
7. apm_mature: Công nghiệp hàng không – phòng không trưởng thành (Biên đội tiêm kích thế hệ mới trong khiên xanh kim cương, cánh bay vàng, sao vàng)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Artifact showcase & tree simulation images
"""

import os
import sys
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")

TARGET_SIZE = (93, 91)


def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border to guarantee clean cutouts
    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)
    print(f"Saved PNG: {png_path}")

    # Write uncompressed 32-bit BGRA DDS
    r, g, b, a = canvas.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    assert len(dds_path.read_bytes()) == 33980
    print(f"Saved DDS: {dds_path} (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted shading."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1
    r_inner = r_outer * 0.382

    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))

    draw.polygon(pts, fill=(255, 215, 0, 255), outline=(170, 130, 20, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 235, 100, 120))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(200, 150, 10, 140))
    return im


def create_vpa_cockade(size: int = 30) -> Image.Image:
    """Generate an official VPA roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(212, 175, 55, 255), outline=(130, 95, 20, 255), width=1)
    r_inner = r_outer - 2.5
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(185, 25, 25, 255), outline=(120, 15, 15, 255), width=1)
    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_airforce_wings(w: int = 34, h: int = 14) -> Image.Image:
    """Generate sleek golden air force pilot wings with central star."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cy = h / 2
    cx = w / 2

    # Left wing feathers
    for i in range(3):
        y_off = (i - 1) * 2.5
        pts_left = [
            (cx - 3, cy + y_off),
            (cx - w // 2, cy - 2 + y_off * 1.3),
            (cx - w // 2 + 4, cy + 2 + y_off),
            (cx - 3, cy + 3 + y_off)
        ]
        draw.polygon(pts_left, fill=(235, 195, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx - 3, cy + y_off, cx - w // 2, cy - 2 + y_off * 1.3), fill=(255, 240, 120, 255), width=1)

    # Right wing feathers
    for i in range(3):
        y_off = (i - 1) * 2.5
        pts_right = [
            (cx + 3, cy + y_off),
            (cx + w // 2, cy - 2 + y_off * 1.3),
            (cx + w // 2 - 4, cy + 2 + y_off),
            (cx + 3, cy + 3 + y_off)
        ]
        draw.polygon(pts_right, fill=(235, 195, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx + 3, cy + y_off, cx + w // 2, cy - 2 + y_off * 1.3), fill=(255, 240, 120, 255), width=1)

    # Central red roundel with gold star
    r = 4.5
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(200, 25, 25, 255), outline=(140, 100, 15, 255), width=1)
    star = create_gold_star(7)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_gear(r: int = 14) -> Image.Image:
    """Generate industrial cog gear with metallic brass shading."""
    sz = r * 2 + 4
    im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = sz / 2, sz / 2
    n_teeth = 8
    pts = []
    for i in range(n_teeth * 2):
        ang = i * math.pi / n_teeth
        curr_r = r if i % 2 == 0 else r * 0.8
        pts.append((cx + curr_r * math.cos(ang), cy + curr_r * math.sin(ang)))
    draw.polygon(pts, fill=(185, 150, 65, 255), outline=(100, 75, 25, 255))
    draw.ellipse((cx - r * 0.45, cy - r * 0.45, cx + r * 0.45, cy + r * 0.45), fill=(40, 45, 55, 255), outline=(100, 75, 25, 255))
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 1. VIE_apm_law (Thể chế Công nghiệp Quốc phòng Hàng không)
# =========================================================================
def build_apm_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: army_military_industryy.dds (industrial plant with gears, wings, and missile launcher)
    p_ind = MD_GOALS / "00_army" / "army_military_industryy.dds"
    if p_ind.exists():
        im_ind = Image.open(p_ind).convert("RGBA")
        im_ind = im_ind.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_ind, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Air Force wings
    wings = create_airforce_wings(34, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "apm_law")
    return canvas


# =========================================================================
# 2. VIE_apm_a32 (Nhà máy A32: đại tu và kéo dài niên hạn)
# =========================================================================
def build_apm_a32() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: jet_engine.dds (turbofan engine on overhaul test rig with exhaust flame inside golden wreath)
    p_eng = MD_GOALS / "00_airforce" / "jet_engine.dds"
    if p_eng.exists():
        im_eng = Image.open(p_eng).convert("RGBA")
        im_eng = im_eng.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_eng, offset_x=0, offset_y=-2)

    # Industrial gear at bottom center
    gear = create_gear(r=10)
    paste_centered(canvas, gear, offset_x=0, offset_y=24)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Small gold star on gear
    s_mini = create_gold_star(8)
    paste_centered(canvas, s_mini, offset_x=0, offset_y=24)

    save_game_ready_icon(canvas, "apm_a32")
    return canvas


# =========================================================================
# 3. VIE_apm_a31 (Nhà máy A31: tên lửa phòng không)
# =========================================================================
def build_apm_a31() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: SAM.dds (multi-tube SAM launcher inside golden wreath)
    p_sam = MD_GOALS / "00_army" / "SAM.dds"
    if p_sam.exists():
        im_sam = Image.open(p_sam).convert("RGBA")
        im_sam = im_sam.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_sam, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Air Force wings
    wings = create_airforce_wings(34, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "apm_a31")
    return canvas


# =========================================================================
# 4. VIE_apm_radar (Radar và chỉ huy – điều khiển nội địa)
# =========================================================================
def build_apm_radar() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: army_radar.dds (rotating early-warning radar dish on control cabin inside golden wreath)
    p_rad = MD_GOALS / "00_army" / "army_radar.dds"
    if p_rad.exists():
        im_rad = Image.open(p_rad).convert("RGBA")
        im_rad = im_rad.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_rad, offset_x=0, offset_y=-2)

    # Tactical radar range arcs on upper left quadrant
    arcs = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    a_draw = ImageDraw.Draw(arcs)
    rcx, rcy = 46, 28
    for r_arc in [16, 24, 32]:
        a_draw.arc((rcx - r_arc, rcy - r_arc, rcx + r_arc, rcy + r_arc), start=190, end=310, fill=(90, 205, 235, 160), width=1)
    canvas.paste(arcs, (0, 0), arcs)

    # Top apex: 3D Faceted Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Air Force wings
    wings = create_airforce_wings(34, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "apm_radar")
    return canvas


# =========================================================================
# 5. VIE_apm_integration (Tích hợp vũ khí và hệ thống đa nguồn)
# =========================================================================
def build_apm_integration() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: tech_sharing.dds (network nodes in circular brass/bronze frame)
    p_tech = MD_GOALS / "00_science" / "tech_sharing.dds"
    if p_tech.exists():
        im_tech = Image.open(p_tech).convert("RGBA")
        im_tech = im_tech.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_tech, offset_x=0, offset_y=-2)

    # Central digital avionics chip
    chip = Image.new("RGBA", (22, 22), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(chip)
    c_draw.rounded_rectangle((2, 2, 20, 20), radius=2, fill=(28, 48, 72, 255), outline=(215, 185, 60, 255), width=1)
    # Circuit pins
    for i in [5, 9, 13, 17]:
        c_draw.line((i, 0, i, 2), fill=(215, 185, 60, 255), width=1)
        c_draw.line((i, 20, i, 22), fill=(215, 185, 60, 255), width=1)
        c_draw.line((0, i, 2, i), fill=(215, 185, 60, 255), width=1)
        c_draw.line((20, i, 22, i), fill=(215, 185, 60, 255), width=1)
    c_star = create_gold_star(10)
    chip.paste(c_star, (6, 6), c_star)
    paste_centered(canvas, chip, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Air Force wings
    wings = create_airforce_wings(34, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "apm_integration")
    return canvas


# =========================================================================
# 6. VIE_apm_uav (Chương trình UAV nội địa)
# =========================================================================
def build_apm_uav() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: drone2.dds (modern UAV on diamond red shield with golden wreath and banner)
    p_drone = MD_GOALS / "00_airforce" / "drone2.dds"
    if p_drone.exists():
        im_drone = Image.open(p_drone).convert("RGBA")
        im_drone = im_drone.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_drone, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Center bottom banner: VPA cockade mini
    cockade = create_vpa_cockade(size=14)
    paste_centered(canvas, cockade, offset_x=0, offset_y=24)

    save_game_ready_icon(canvas, "apm_uav")
    return canvas


# =========================================================================
# 7. VIE_apm_mature (Công nghiệp hàng không – phòng không trưởng thành - Capstone APM)
# =========================================================================
def build_apm_mature() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Jet_Fighters.dds (two modern stealth fighters banking inside diamond blue shield with golden laurel wreath)
    p_jet = MD_GOALS / "00_airforce" / "Jet_Fighters.dds"
    if p_jet.exists():
        im_jet = Image.open(p_jet).convert("RGBA")
        im_jet = im_jet.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_jet, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Air Force wings
    wings = create_airforce_wings(36, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "apm_mature")
    return canvas


def create_showcase(icons, labels):
    """Generate professional Batch 1 showcase artifact."""
    n = len(icons)
    card_w = 110
    total_w = n * card_w + 30
    total_h = 165

    im = Image.new("RGBA", (total_w, total_h), (16, 22, 30, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 13)
        font_label = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    except Exception:
        font_title = ImageFont.load_default()
        font_label = ImageFont.load_default()

    draw.text((15, 12), "PHÒNG KHÔNG - KHÔNG QUÂN (PK-KQ) - BATCH 1: CNQP HÀNG KHÔNG & RADAR (APM)", fill=(255, 215, 0, 255), font=font_title)

    for i, (icon, label) in enumerate(zip(icons, labels)):
        cx = 15 + i * card_w + 8
        cy = 40

        # Card container
        draw.rounded_rectangle((cx - 4, cy - 4, cx + 93 + 4, cy + 91 + 4), radius=4, fill=(24, 32, 44, 255), outline=(48, 64, 84, 255), width=1)
        im.paste(icon, (cx, cy), icon)

        # Label underneath
        draw.text((cx - 2, cy + 98), label, fill=(215, 225, 235, 255), font=font_label)

    out_path = BRAIN_DIR / "air_batch_1_showcase.png"
    im.save(out_path)
    print(f"Saved Showcase: {out_path}")


def create_tree_simulation():
    """Generate in-game focus tree simulation diagram for Batch 1."""
    canvas_w = 780
    canvas_h = 380
    im = Image.new("RGBA", (canvas_w, canvas_h), (16, 20, 28, 255))
    draw = ImageDraw.Draw(im)

    # Grid lines
    for x in range(0, canvas_w, 35):
        draw.line((x, 0, x, canvas_h), fill=(25, 32, 45, 255), width=1)
    for y in range(0, canvas_h, 35):
        draw.line((0, y, canvas_w, y), fill=(25, 32, 45, 255), width=1)

    try:
        font_header = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 14)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
        font_foc = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    except Exception:
        font_header = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_foc = ImageFont.load_default()

    draw.text((20, 15), "HOI4 / MILLENNIUM DAWN - CÂY TIÊU ĐIỂM PK-KQ (BATCH 1: TRỤC 2 CNQP HÀNG KHÔNG APM)", fill=(255, 215, 0, 255), font=font_header)
    draw.text((20, 35), "Mô phỏng hiển thị in-game: Thể chế Hàng không, Nhà máy A32/A31, Radar nội địa, Tích hợp, UAV & Capstone Trưởng thành", fill=(160, 175, 195, 255), font=font_sub)

    c_gold = (190, 150, 45, 255)

    # Tree Layout for APM:
    # Root: VIE_apm_law at center (x=340, y=55)
    # Tier 1: VIE_apm_a32 (x=160, y=145), VIE_apm_a31 (x=340, y=145), VIE_apm_radar (x=520, y=145)
    # Tier 2: VIE_apm_integration (x=160, y=235), VIE_apm_uav (x=520, y=235)
    # Capstone: VIE_apm_mature (x=340, y=295)

    # Connect law to a32, a31, radar
    draw.line((340 + 46, 55 + 70, 340 + 46, 135), fill=c_gold, width=2)
    draw.line((160 + 46, 135, 520 + 46, 135), fill=c_gold, width=2)
    draw.line((160 + 46, 135, 160 + 46, 145), fill=c_gold, width=2)
    draw.line((340 + 46, 135, 340 + 46, 145), fill=c_gold, width=2)
    draw.line((520 + 46, 135, 520 + 46, 145), fill=c_gold, width=2)

    # Connect a32 to integration
    draw.line((160 + 46, 145 + 70, 160 + 46, 235), fill=c_gold, width=2)

    # Connect radar to uav
    draw.line((520 + 46, 145 + 70, 520 + 46, 235), fill=c_gold, width=2)

    # Connect integration & uav to mature
    draw.line((160 + 46, 235 + 70, 160 + 46, 285), fill=c_gold, width=2)
    draw.line((520 + 46, 235 + 70, 520 + 46, 285), fill=c_gold, width=2)
    draw.line((160 + 46, 285, 520 + 46, 285), fill=c_gold, width=2)
    draw.line((340 + 46, 285, 340 + 46, 295), fill=c_gold, width=2)

    nodes = [
        ("apm_law", "Thể chế CNQP Hàng không", 340, 55),
        ("apm_a32", "Nhà máy A32 (Su-30)", 160, 145),
        ("apm_a31", "Nhà máy A31 (Tên lửa)", 340, 145),
        ("apm_radar", "Radar Nội địa", 520, 145),
        ("apm_integration", "Tích hợp Đa nguồn", 160, 235),
        ("apm_uav", "Chương trình UAV", 520, 235),
        ("apm_mature", "CN Hàng không Trưởng thành", 340, 295),
    ]

    for stem, title, nx, ny in nodes:
        png_p = PNG_DIR / f"{stem}.png"
        if png_p.exists():
            ic = Image.open(png_p).convert("RGBA").resize((70, 68), Image.Resampling.LANCZOS)
        else:
            ic = Image.new("RGBA", (70, 68), (40, 50, 60, 255))

        outline_c = (235, 195, 60, 255)
        fill_c = (26, 36, 50, 255)
        draw.rounded_rectangle((nx, ny, nx + 92, ny + 74), radius=4, fill=fill_c, outline=outline_c, width=2)
        im.paste(ic, (nx + 11, ny + 3), ic)

        tb_w = 145
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255), font=font_foc)

    out_sim = BRAIN_DIR / "air_batch_1_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Air Force Batch 1 focus icons (APM)...")
    ic1 = build_apm_law()
    ic2 = build_apm_a32()
    ic3 = build_apm_a31()
    ic4 = build_apm_radar()
    ic5 = build_apm_integration()
    ic6 = build_apm_uav()
    ic7 = build_apm_mature()
    print("Completed all 7 icons for Air Force Batch 1!")

    icons = [ic1, ic2, ic3, ic4, ic5, ic6, ic7]
    labels = [
        "Thể chế CN Hàng không",
        "Nhà máy A32 (Su-30)",
        "Nhà máy A31 (SAM)",
        "Radar Nội địa",
        "Tích hợp Đa nguồn",
        "Chương trình UAV",
        "CN Hàng không Trưởng thành"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 1 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
