"""Script to build Batch 5 Focus Icons for Vietnam Air Force & Air Defense (PK-KQ & APM) in Millennium Dawn.
Batch 5 focuses (Cánh Tiêm kích Độc lập & Tác chiến Không người lái MUM-T - 6 focuses):
1. airf_multirole_wing: Cánh Không quân Đa nhiệm (Capstone Tiêm kích Nhánh B - Tiêm kích trên khiên đỏ vinh quang, quân hiệu PK-KQ, cánh bay vàng, sao vàng)
2. airf_unmanned: Không người lái & Mạng hóa (Khởi đầu Nhánh C - UAV trinh sát trên khung tròn radar trong vành nguyệt quế, cánh bay vàng, sao vàng)
3. airf_isr_uav: UAV Trinh sát & Chỉ thị Mục tiêu (UAV tầm cao MALE sải cánh dài trên khiên kim cương đỏ trong vành nguyệt quế, cánh bay vàng, sao vàng)
4. airf_datalink: Mạng Liên kết Dữ liệu Hàng không (Vệ tinh C4ISR quỹ đạo truyền chùm dữ liệu chiến thuật thời gian thực, cánh bay vàng, sao vàng)
5. airf_strike_uav: UAV Tấn công & Tên lửa Hành trình (UAV cảm tử đạn tuần kích bổ nhào trên khiên danh dự trong vành nguyệt quế, cánh bay vàng, sao vàng)
6. airf_teaming: Phối hợp Có người – Không người (MUM-T Capstone - UAV phản lực tàng hình Loyal Wingman trong vành nguyệt quế kiếm lệnh, cánh bay vàng, sao vàng)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Artifact showcase & tree simulation images
- all_29_air_focuses_master_sheet.png (Master sheet of all 29 Air Force & APM focuses)
"""

import os
import sys
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

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
        draw.polygon([center, tip, valley_left], fill=(255, 235, 100, 140))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 140, 10, 160))
    return im


def create_gold_star_with_glow(size: int) -> Image.Image:
    """Generate faceted gold star with high-depth drop shadow."""
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(1.2))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas


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


def create_airforce_wings(w: int = 36, h: int = 14) -> Image.Image:
    """Generate sleek golden air force pilot wings with central star and drop shadow."""
    pad = 3
    full_w = w + pad * 2
    full_h = h + pad * 2
    wings_raw = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(wings_raw)
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
        draw.polygon(pts_left, fill=(240, 200, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx - 3, cy + y_off, cx - w // 2, cy - 2 + y_off * 1.3), fill=(255, 245, 130, 255), width=1)

    # Right wing feathers
    for i in range(3):
        y_off = (i - 1) * 2.5
        pts_right = [
            (cx + 3, cy + y_off),
            (cx + w // 2, cy - 2 + y_off * 1.3),
            (cx + w // 2 - 4, cy + 2 + y_off),
            (cx + 3, cy + 3 + y_off)
        ]
        draw.polygon(pts_right, fill=(240, 200, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx + 3, cy + y_off, cx + w // 2, cy - 2 + y_off * 1.3), fill=(255, 245, 130, 255), width=1)

    # Central red roundel with gold star
    r = 5
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(205, 25, 25, 255), outline=(140, 100, 15, 255), width=1)
    star = create_gold_star(8)
    wings_raw.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)

    # Composite with drop shadow
    im = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))
    shadow.paste(wings_raw, (pad, pad + 1), wings_raw)
    r_ch, g_ch, b_ch, a_ch = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a_ch)).filter(ImageFilter.GaussianBlur(1.0))
    im.paste(shadow, (0, 0), shadow)
    im.paste(wings_raw, (pad, pad), wings_raw)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 1. VIE_airf_multirole_wing (Cánh Không quân Đa nhiệm - Capstone Nhánh B)
# =========================================================================
def build_airf_multirole_wing() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/air_force.dds (Fighter climbing over maroon shield in golden laurel wreath)
    base_path = MD_GOALS / "00_airforce" / "air_force.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Central VPA cockade roundel on the shield
    cockade = create_vpa_cockade(18)
    paste_centered(canvas, cockade, offset_x=0, offset_y=3)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Grand golden Air Force wings at bottom
    wings = create_airforce_wings(42, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_multirole_wing")
    return canvas


# =========================================================================
# 2. VIE_airf_unmanned (Không người lái & Mạng hóa - Khởi đầu Nhánh C)
# =========================================================================
def build_airf_unmanned() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/drone.dds (Modern UAV banking across circular radar frame in laurel wreath)
    base_path = MD_GOALS / "00_airforce" / "drone.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_unmanned")
    return canvas


# =========================================================================
# 3. VIE_airf_isr_uav (UAV Trinh sát & Chỉ thị Mục tiêu)
# =========================================================================
def build_airf_isr_uav() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/drone2.dds (Long-endurance MALE UAV on red diamond shield in golden laurel wreath)
    base_path = MD_GOALS / "00_airforce" / "drone2.dds"
    base = Image.open(base_path).convert("RGBA")

    # Slight contrast boost
    base = ImageEnhance.Color(base).enhance(1.10)
    base = ImageEnhance.Contrast(base).enhance(1.08)

    # Resize to fit frame
    base_resized = base.resize((86, 74), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_isr_uav")
    return canvas


# =========================================================================
# 4. VIE_airf_datalink (Mạng Liên kết Dữ liệu Hàng không C4ISR)
# =========================================================================
def build_airf_datalink() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_science/weaponized_satellites.dds (Orbital C4ISR communications satellite with solar panels)
    base_path = MD_GOALS / "00_science" / "weaponized_satellites.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Draw cyan data transmission beams connecting satellite to tactical elements
    draw = ImageDraw.Draw(canvas)
    # Beams
    draw.line((46, 36, 30, 62), fill=(60, 220, 255, 180), width=1)
    draw.line((46, 36, 62, 62), fill=(60, 220, 255, 180), width=1)
    draw.line((46, 36, 46, 65), fill=(255, 230, 80, 200), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_datalink")
    return canvas


# =========================================================================
# 5. VIE_airf_strike_uav (UAV Tấn công & Tên lửa Hành trình)
# =========================================================================
def build_airf_strike_uav() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/shahed.dds (Delta-wing strike UAV / loitering munition in dive on shield in wreath)
    base_path = MD_GOALS / "00_airforce" / "shahed.dds"
    base = Image.open(base_path).convert("RGBA")

    # Slight contrast boost
    base = ImageEnhance.Contrast(base).enhance(1.08)

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_strike_uav")
    return canvas


# =========================================================================
# 6. VIE_airf_teaming (Phối hợp Có người – Không người - MUM-T Capstone)
# =========================================================================
def build_airf_teaming() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/blr_yastreb.dds (Jet-powered stealth Loyal Wingman in red roundel with wreath and swords)
    base_path = MD_GOALS / "00_airforce" / "blr_yastreb.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Grand golden Air Force wings with central red cockade at bottom
    wings = create_airforce_wings(42, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_teaming")
    return canvas


def create_showcase(icons, labels):
    """Generate a high-res showcase banner for Batch 5."""
    card_w, card_h = 165, 210
    pad = 18
    n = len(icons)
    total_w = pad + n * (card_w + pad)
    total_h = card_h + pad * 2 + 50

    im = Image.new("RGBA", (total_w, total_h), (16, 22, 32, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 20)
        font_sub = ImageFont.truetype("arial.ttf", 12)
        font_card = ImageFont.truetype("arialbd.ttf", 12)
    except Exception:
        font_title = font_sub = font_card = ImageFont.load_default()

    draw.text((pad, 15), "VIETNAM AIR FORCE & AIR DEFENSE (PK-KQ) - BATCH 5 GFX SHOWCASE", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad, 42), "Cánh Tiêm kích Độc lập & Tác chiến Không người lái MUM-T (6 Focuses)", fill=(160, 190, 220, 255), font=font_sub)

    for i, (ic, lbl) in enumerate(zip(icons, labels)):
        cx = pad + i * (card_w + pad)
        cy = pad + 50

        draw.rounded_rectangle((cx, cy, cx + card_w, cy + card_h), radius=8, fill=(24, 32, 46, 255), outline=(50, 70, 100, 255), width=2)
        draw.ellipse((cx + card_w // 2 - 45, cy + 20, cx + card_w // 2 + 45, cy + 110), fill=(10, 40, 75, 120))

        # Paste preview icon
        preview_sz = (93, 91)
        im.paste(ic, (cx + (card_w - preview_sz[0]) // 2, cy + 20), ic)

        # Label text box
        lines = lbl.split("\n")
        ty = cy + 125
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_card)
            tw = bbox[2] - bbox[0]
            draw.text((cx + (card_w - tw) // 2, ty), line, fill=(230, 240, 255, 255), font=font_card)
            ty += 16

        draw.text((cx + card_w // 2 - 32, cy + card_h - 22), "33,980 B (DDS)", fill=(130, 170, 200, 255), font=font_sub)

    out_showcase = BRAIN_DIR / "air_batch_5_showcase.png"
    im.save(out_showcase)
    print(f"Saved Showcase: {out_showcase}")


def create_tree_simulation():
    """Generate in-game focus tree simulation for Batch 5."""
    im = Image.new("RGBA", (880, 520), (14, 18, 26, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_foc = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        font_header = font_foc = ImageFont.load_default()

    draw.text((20, 15), "IN-GAME FOCUS TREE SIMULATION - BATCH 5 (CAPSTONES & MUM-T)", fill=(255, 215, 0, 255), font=font_header)

    c_gold = (212, 175, 55, 200)

    # Left: Multirole Capstone (airf_multirole_wing)
    draw.line((180, 50, 180, 110), fill=c_gold, width=2)

    # Right: Unmanned Branch (airf_unmanned -> isr_uav, datalink -> strike_uav -> teaming)
    draw.line((550, 50, 550, 110), fill=c_gold, width=2)
    draw.line((550, 110 + 70, 550, 220), fill=c_gold, width=2)
    draw.line((400 + 46, 220, 700 + 46, 220), fill=c_gold, width=2)
    draw.line((400 + 46, 220, 400 + 46, 230), fill=c_gold, width=2)
    draw.line((700 + 46, 220, 700 + 46, 230), fill=c_gold, width=2)

    # isr_uav -> strike_uav
    draw.line((400 + 46, 230 + 70, 400 + 46, 330), fill=c_gold, width=2)

    # strike_uav & datalink -> teaming
    draw.line((400 + 46, 330 + 70, 400 + 46, 420), fill=c_gold, width=2)
    draw.line((700 + 46, 230 + 70, 700 + 46, 420), fill=c_gold, width=2)
    draw.line((400 + 46, 420, 700 + 46, 420), fill=c_gold, width=2)
    draw.line((550, 420, 550, 430), fill=c_gold, width=2)

    nodes = [
        ("airf_multirole_wing", "Cánh KQ Đa nhiệm (B)", 180 - 46, 110),
        ("airf_unmanned", "Chiến lược UAV (C)", 550 - 46, 110),
        ("airf_isr_uav", "UAV Trinh sát MALE", 400, 230),
        ("airf_datalink", "Mạng Liên kết C4ISR", 700, 230),
        ("airf_strike_uav", "UAV Tấn công / Cảm tử", 400, 330),
        ("airf_teaming", "Phối hợp MUM-T Capstone", 550 - 46, 430),
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

        tb_w = 155
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255), font=font_foc)

    out_sim = BRAIN_DIR / "air_batch_5_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def create_master_sheet():
    """Generate a comprehensive Master Sheet of all 29 Air Force & APM Focus Icons."""
    all_29_stems = [
        # Batch 1 (APM)
        ("apm_law", "Thể chế CNQP Hàng không", "Batch 1: APM"),
        ("apm_a32", "Nhà máy A32 (Su-30)", "Batch 1: APM"),
        ("apm_a31", "Nhà máy A31 (Tên lửa)", "Batch 1: APM"),
        ("apm_radar", "Radar Nội địa (VRS-2DM)", "Batch 1: APM"),
        ("apm_integration", "Tích hợp Đa nguồn", "Batch 1: APM"),
        ("apm_uav", "Chương trình UAV", "Batch 1: APM"),
        ("apm_mature", "CN Hàng không Trưởng thành", "Batch 1: APM"),
        # Batch 2 (Trục 3 Nòng cốt)
        ("airf_training_standardization", "Chuẩn hóa Đào tạo Phi công", "Batch 2: Nòng cốt"),
        ("airf_fighter_force", "Lực lượng Tiêm kích", "Batch 2: Nòng cốt"),
        ("airf_sam_force", "Lực lượng Tên lửa SAM", "Batch 2: Nòng cốt"),
        ("airf_command_reform_1", "Cải cách Chỉ huy PK-KQ I", "Batch 2: Nòng cốt"),
        ("airf_first_force", "Cơ cấu Lực lượng Ban đầu", "Batch 2: Nòng cốt"),
        # Batch 3 (Bán kính & IADS)
        ("airf_command_reform_2", "Cải cách Chỉ huy PK-KQ II", "Batch 3: IADS"),
        ("airf_medium_force", "Không quân Tầm trung", "Batch 3: IADS"),
        ("airf_operating_range", "Mở rộng Bán kính Tác chiến", "Batch 3: IADS"),
        ("airf_iads", "Phòng không Tích hợp", "Batch 3: IADS"),
        ("airf_layered_defence", "Mạng Tên lửa Nhiều tầng", "Batch 3: IADS"),
        ("airf_ew_antistealth", "Tác chiến ĐT & Chống tàng hình", "Batch 3: IADS"),
        # Batch 4 (Bộ Chỉ huy & Tiêm kích Đa nhiệm)
        ("airf_iads_command", "Sở Chỉ huy PK Khu vực", "Batch 4: Đa nhiệm"),
        ("airf_multirole", "Không quân Đa nhiệm", "Batch 4: Đa nhiệm"),
        ("airf_multirole_fleet", "Tiêm kích Đa nhiệm 4.5", "Batch 4: Đa nhiệm"),
        ("airf_sustainment", "Bảo đảm Kỹ thuật Đa nguồn", "Batch 4: Đa nhiệm"),
        ("airf_airlift_tanker", "Vận tải & Tiếp dầu", "Batch 4: Đa nhiệm"),
        # Batch 5 (Capstone & MUM-T)
        ("airf_multirole_wing", "Cánh Không quân Đa nhiệm", "Batch 5: MUM-T"),
        ("airf_unmanned", "Chiến lược UAV", "Batch 5: MUM-T"),
        ("airf_isr_uav", "UAV Trinh sát MALE", "Batch 5: MUM-T"),
        ("airf_datalink", "Mạng Liên kết C4ISR", "Batch 5: MUM-T"),
        ("airf_strike_uav", "UAV Tấn công / Cảm tử", "Batch 5: MUM-T"),
        ("airf_teaming", "Phối hợp MUM-T Capstone", "Batch 5: MUM-T"),
    ]

    cols = 6
    rows = math.ceil(len(all_29_stems) / cols)
    card_w, card_h = 160, 175
    pad_x, pad_y = 16, 16
    total_w = pad_x * 2 + cols * (card_w + pad_x) - pad_x
    total_h = 100 + rows * (card_h + pad_y)

    im = Image.new("RGBA", (total_w, total_h), (14, 18, 26, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 24)
        font_sub = ImageFont.truetype("arial.ttf", 13)
        font_name = ImageFont.truetype("arialbd.ttf", 11)
        font_cat = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        font_title = font_sub = font_name = font_cat = ImageFont.load_default()

    draw.text((pad_x, 20), "VIETNAM AIR FORCE & AIR DEFENSE (PK-KQ & APM) - MASTER GFX SHEET", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 54), "Toàn bộ 29 Tiêu điểm Quân chủng PK-KQ & Công nghiệp Quốc phòng Hàng không (Chuẩn Millennium Dawn 33,980 Bytes)", fill=(160, 190, 220, 255), font=font_sub)

    for i, (stem, title, category) in enumerate(all_29_stems):
        col = i % cols
        row = i // cols
        x = pad_x + col * (card_w + pad_x)
        y = 95 + row * (card_h + pad_y)

        # Card container
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=6, fill=(22, 28, 40, 255), outline=(45, 60, 85, 255), width=1)

        # Load PNG icon
        png_p = PNG_DIR / f"{stem}.png"
        if png_p.exists():
            ic = Image.open(png_p).convert("RGBA").resize((76, 74), Image.Resampling.LANCZOS)
            im.paste(ic, (x + (card_w - 76) // 2, y + 14), ic)

        # Category badge
        draw.rounded_rectangle((x + 10, y + 95, x + card_w - 10, y + 112), radius=3, fill=(15, 20, 28, 220), outline=(60, 80, 110, 255), width=1)
        draw.text((x + 16, y + 98), category, fill=(255, 215, 0, 220), font=font_cat)

        # Title text
        words = title.split()
        if len(words) > 3:
            l1 = " ".join(words[:3])
            l2 = " ".join(words[3:])
            draw.text((x + 10, y + 120), l1, fill=(240, 245, 255, 255), font=font_name)
            draw.text((x + 10, y + 136), l2, fill=(240, 245, 255, 255), font=font_name)
        else:
            draw.text((x + 10, y + 126), title, fill=(240, 245, 255, 255), font=font_name)

        # Technical label
        draw.text((x + 10, y + 154), "33,980 B (DDS)", fill=(120, 155, 185, 255), font=font_cat)

    out_master = BRAIN_DIR / "all_29_air_focuses_master_sheet.png"
    im.save(out_master)
    print(f"Saved Master Sheet: {out_master}")


def main():
    print("Building Air Force Batch 5 focus icons (Capstones & MUM-T)...")
    ic1 = build_airf_multirole_wing()
    ic2 = build_airf_unmanned()
    ic3 = build_airf_isr_uav()
    ic4 = build_airf_datalink()
    ic5 = build_airf_strike_uav()
    ic6 = build_airf_teaming()
    print("Completed all 6 icons for Air Force Batch 5!")

    icons = [ic1, ic2, ic3, ic4, ic5, ic6]
    labels = [
        "Cánh Không quân\nĐa nhiệm (B)",
        "Chiến lược UAV &\nMạng hóa (C)",
        "UAV Trinh sát MALE\n(VT-Patrol)",
        "Mạng Liên kết C4ISR\nVệ tinh Quỹ đạo",
        "UAV Tấn công &\nTên lửa Hành trình",
        "Phối hợp MUM-T\nCapstone Toàn Nhánh"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    create_master_sheet()
    print("Batch 5 build, showcase, simulation & Master Sheet finished successfully!")


if __name__ == "__main__":
    main()
