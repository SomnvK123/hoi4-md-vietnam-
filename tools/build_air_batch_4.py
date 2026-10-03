"""Script to build Batch 4 Focus Icons for Vietnam Air Force & Air Defense (PK-KQ) in Millennium Dawn.
Batch 4 focuses (Sở Chỉ huy Phòng không & Không quân Đa nhiệm Hạng nặng - 5 focuses):
1. airf_iads_command: Sở Chỉ huy Phòng không Khu vực (Hồng tâm radar khóa mục tiêu máy bay xâm nhập trong vành nguyệt quế, cánh bay vàng, sao vàng)
2. airf_multirole: Không quân Đa nhiệm (Tiêm kích đa năng hiện đại trong vành nguyệt quế, cánh bay PK-KQ, sao vàng)
3. airf_multirole_fleet: Chương trình Tiêm kích Đa nhiệm 4.5 (Tiêm kích hạng nặng Su-30 mang tên lửa đối hải/đối đất trong vành nguyệt quế, cánh bay vàng, sao vàng)
4. airf_sustainment: Bảo đảm Kỹ thuật Đa nguồn (Động cơ phản lực AL-31F trên bệ thử bảo dưỡng trong vành nguyệt quế, cánh bay vàng, sao vàng)
5. airf_airlift_tanker: Vận tải & Tiếp dầu Trên không (Máy bay vận tải/tiếp dầu quân sự hạng nặng trên tầng mây trong vành nguyệt quế, cánh bay vàng, sao vàng)

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
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals\00_airforce")

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
# 1. VIE_airf_iads_command (Sở Chỉ huy Phòng không Khu vực - Capstone Nhánh A)
# =========================================================================
def build_airf_iads_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: air_superiority.dds (Octagonal HUD reticle target lock on aircraft with laurel wreath)
    base_path = MD_GOALS / "air_superiority.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Glowing cyan tactical lock reticle indicators
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 38
    # Reticle corner ticks
    draw.line((cx - 12, cy - 8, cx - 8, cy - 8), fill=(50, 220, 255, 180), width=1)
    draw.line((cx - 12, cy - 8, cx - 12, cy - 4), fill=(50, 220, 255, 180), width=1)
    draw.line((cx + 12, cy - 8, cx + 8, cy - 8), fill=(50, 220, 255, 180), width=1)
    draw.line((cx + 12, cy - 8, cx + 12, cy - 4), fill=(50, 220, 255, 180), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_iads_command")
    return canvas


# =========================================================================
# 2. VIE_airf_multirole (Không quân Đa nhiệm)
# =========================================================================
def build_airf_multirole() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: fighters2.dds (Canard/delta-wing multirole combat jet in circular bronze ring with wreath)
    base_path = MD_GOALS / "fighters2.dds"
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

    save_game_ready_icon(canvas, "airf_multirole")
    return canvas


# =========================================================================
# 3. VIE_airf_multirole_fleet (Chương trình Tiêm kích Đa nhiệm 4.5)
# =========================================================================
def build_airf_multirole_fleet() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: CHI_focus_j15.dds (Heavy twin-engine Flanker with missiles in maritime blue ring with wreath)
    base_path = MD_GOALS / "CHI_focus_j15.dds"
    base = Image.open(base_path).convert("RGBA")

    # Slight saturation and contrast boost
    base = ImageEnhance.Color(base).enhance(1.12)
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

    save_game_ready_icon(canvas, "airf_multirole_fleet")
    return canvas


# =========================================================================
# 4. VIE_airf_sustainment (Bảo đảm Kỹ thuật Đa nguồn)
# =========================================================================
def build_airf_sustainment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: jet_engine.dds (Turbofan jet engine on test stand with exhaust plume in laurel wreath)
    base_path = MD_GOALS / "jet_engine.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom ribbon
    wings = create_airforce_wings(40, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_sustainment")
    return canvas


# =========================================================================
# 5. VIE_airf_airlift_tanker (Vận tải & Tiếp dầu Trên không)
# =========================================================================
def build_airf_airlift_tanker() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic_Transport_Aircraft.dds (Heavy transport/tanker aircraft in sky with golden wreath)
    base_path = MD_GOALS / "Generic_Transport_Aircraft.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(40, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_airlift_tanker")
    return canvas


def create_showcase(icons, labels):
    """Generate a high-res showcase banner for Batch 4."""
    card_w, card_h = 170, 210
    pad = 20
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

    draw.text((pad, 15), "VIETNAM AIR FORCE & AIR DEFENSE (PK-KQ) - BATCH 4 GFX SHOWCASE", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad, 42), "Sở Chỉ huy Phòng không & Không quân Đa nhiệm Hạng nặng (5 Focuses)", fill=(160, 190, 220, 255), font=font_sub)

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

    out_showcase = BRAIN_DIR / "air_batch_4_showcase.png"
    im.save(out_showcase)
    print(f"Saved Showcase: {out_showcase}")


def create_tree_simulation():
    """Generate in-game focus tree simulation for Batch 4."""
    im = Image.new("RGBA", (860, 480), (14, 18, 26, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_foc = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        font_header = font_foc = ImageFont.load_default()

    draw.text((20, 15), "IN-GAME FOCUS TREE SIMULATION - BATCH 4 (IADS COMMAND & MULTIROLE)", fill=(255, 215, 0, 255), font=font_header)

    c_gold = (212, 175, 55, 200)

    # Left: IADS Capstone (airf_iads_command)
    draw.line((180, 50, 180, 110), fill=c_gold, width=2)

    # Right: Multirole Branch (airf_multirole -> multirole_fleet, sustainment, airlift_tanker)
    draw.line((550, 50, 550, 110), fill=c_gold, width=2)
    draw.line((550, 110 + 70, 550, 240), fill=c_gold, width=2)
    draw.line((370 + 46, 240, 730 + 46, 240), fill=c_gold, width=2)
    draw.line((370 + 46, 240, 370 + 46, 250), fill=c_gold, width=2)
    draw.line((550, 240, 550, 250), fill=c_gold, width=2)
    draw.line((730 + 46, 240, 730 + 46, 250), fill=c_gold, width=2)

    nodes = [
        ("airf_iads_command", "Sở Chỉ huy PK Khu vực (A)", 180 - 46, 110),
        ("airf_multirole", "Không quân Đa nhiệm (B)", 550 - 46, 110),
        ("airf_multirole_fleet", "Tiêm kích Đa nhiệm 4.5", 370, 250),
        ("airf_sustainment", "Bảo đảm Kỹ thuật Đa nguồn", 550 - 46, 250),
        ("airf_airlift_tanker", "Vận tải & Tiếp dầu Trên không", 730, 250),
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

    out_sim = BRAIN_DIR / "air_batch_4_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Air Force Batch 4 focus icons (IADS Command & Multirole)...")
    ic1 = build_airf_iads_command()
    ic2 = build_airf_multirole()
    ic3 = build_airf_multirole_fleet()
    ic4 = build_airf_sustainment()
    ic5 = build_airf_airlift_tanker()
    print("Completed all 5 icons for Air Force Batch 4!")

    icons = [ic1, ic2, ic3, ic4, ic5]
    labels = [
        "Sở Chỉ huy PK\nKhu vực (A)",
        "Không quân\nĐa nhiệm (B)",
        "Chương trình Tiêm kích\nĐa nhiệm 4.5",
        "Bảo đảm Kỹ thuật\nĐa nguồn",
        "Vận tải & Tiếp dầu\nTrên không"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 4 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
