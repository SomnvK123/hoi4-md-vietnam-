"""Script to build Batch 3 Focus Icons for Vietnam Navy (Hải quân) in Millennium Dawn.
Batch 3 focuses (Trục 3 Tầm hoạt động & Học thuyết Ngăn chặn Biển A2/AD - 5 focuses):
13. nf_medium_force: Lực lượng Hải quân Trung bình (Biên đội khinh hạm tàng hình cỡ trung, săn ngầm ASW, khiên hải quân)
14. nf_operating_range: Mở rộng Phạm vi Hoạt động (Đài radar quét tầm xa, la bàn hoa tiêu hàng hải, vòng sóng mở rộng trên biển)
15. nf_denial: Ngăn chặn biển / Maritime Denial (Tên lửa diệt hạm siêu âm rời bệ phóng, hồng tâm khóa mục tiêu A2/AD, vòng nguyệt quế)
16. nf_denial_defence: Phòng thủ Ven bờ Tích hợp (Pháo đài / bệ phóng tên lửa bờ Bastion-P trên sóng biển, khiên vàng đỏ, thủy lôi)
17. nf_denial_subs: Lực lượng Tàu ngầm Ngăn chặn (Tàu ngầm Kilo 636.1 phục kích, ngư lôi hạng nặng lướt sóng ngầm, dải băng vàng)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
"""

import os
import sys
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
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
    print(f"Saved DDS: {dds_path}")


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


def create_naval_anchor(w: int, h: int, color_type: str = "gold") -> Image.Image:
    """Generate a crisp metallic naval anchor."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    if color_type == "gold":
        c_fill = (220, 180, 50, 255)
        c_light = (255, 230, 110, 255)
        c_dark = (140, 100, 15, 255)
    else:
        c_fill = (180, 195, 205, 255)
        c_light = (225, 235, 245, 255)
        c_dark = (90, 105, 115, 255)

    cx = w / 2
    ring_r = int(w * 0.16)
    ring_cy = ring_r + 2
    draw.ellipse((cx - ring_r, ring_cy - ring_r, cx + ring_r, ring_cy + ring_r), fill=c_fill, outline=c_dark, width=2)
    inner_r = int(ring_r * 0.45)
    draw.ellipse((cx - inner_r, ring_cy - inner_r, cx + inner_r, ring_cy + inner_r), fill=(0, 0, 0, 0), outline=c_dark, width=1)

    bar_y = int(h * 0.26)
    bar_w = int(w * 0.65)
    bar_h = int(h * 0.09)
    draw.rounded_rectangle((cx - bar_w / 2, bar_y, cx + bar_w / 2, bar_y + bar_h), radius=2, fill=c_fill, outline=c_dark)
    draw.ellipse((cx - bar_w / 2 - 2, bar_y - 1, cx - bar_w / 2 + bar_h + 1, bar_y + bar_h + 1), fill=c_light, outline=c_dark)
    draw.ellipse((cx + bar_w / 2 - bar_h - 1, bar_y - 1, cx + bar_w / 2 + 2, bar_y + bar_h + 1), fill=c_light, outline=c_dark)

    shank_w = int(w * 0.14)
    shank_top = ring_cy + ring_r - 2
    shank_bot = int(h * 0.78)
    draw.rectangle((cx - shank_w / 2, shank_top, cx + shank_w / 2, shank_bot), fill=c_fill, outline=c_dark)
    draw.line((cx - 1, shank_top + 2, cx - 1, shank_bot - 2), fill=c_light, width=1)

    arc_box = (int(w * 0.10), int(h * 0.50), int(w * 0.90), int(h * 0.96))
    draw.arc(arc_box, start=20, end=160, fill=c_fill, width=int(w * 0.13))
    draw.arc(arc_box, start=20, end=160, fill=c_dark, width=1)

    fluke_sz = int(w * 0.20)
    lf_x = int(w * 0.16)
    lf_y = int(h * 0.65)
    draw.polygon([(lf_x, lf_y - fluke_sz), (lf_x + fluke_sz, lf_y), (lf_x - fluke_sz // 2, lf_y)], fill=c_light, outline=c_dark)
    rf_x = int(w * 0.84)
    rf_y = int(h * 0.65)
    draw.polygon([(rf_x, rf_y - fluke_sz), (rf_x - fluke_sz, rf_y), (rf_x + fluke_sz // 2, rf_y)], fill=c_light, outline=c_dark)
    draw.polygon([(cx - 4, int(h * 0.94)), (cx + 4, int(h * 0.94)), (cx, h - 2)], fill=c_fill, outline=c_dark)
    return im


def create_compass_rose(size: int = 34) -> Image.Image:
    """Generate a crisp 8-point nautical compass rose."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_maj = size / 2 - 2
    r_min = r_maj * 0.65
    r_inner = r_maj * 0.22

    # Draw 4 cardinal rays
    for i in range(4):
        ang = i * math.pi / 2
        # Tip
        tx = cx + r_maj * math.sin(ang)
        ty = cy - r_maj * math.cos(ang)
        # Left and right base points
        lx = cx + r_inner * math.sin(ang - math.pi / 4)
        ly = cy - r_inner * math.cos(ang - math.pi / 4)
        rx = cx + r_inner * math.sin(ang + math.pi / 4)
        ry = cy - r_inner * math.cos(ang + math.pi / 4)

        # Light facet
        draw.polygon([(cx, cy), (tx, ty), (lx, ly)], fill=(255, 230, 110, 255), outline=(150, 110, 20, 255))
        # Dark facet
        draw.polygon([(cx, cy), (tx, ty), (rx, ry)], fill=(180, 130, 20, 255), outline=(130, 90, 15, 255))

    # Draw 4 ordinal rays (smaller)
    for i in range(4):
        ang = i * math.pi / 2 + math.pi / 4
        tx = cx + r_min * math.sin(ang)
        ty = cy - r_min * math.cos(ang)
        lx = cx + r_inner * math.sin(ang - math.pi / 4)
        ly = cy - r_inner * math.cos(ang - math.pi / 4)
        rx = cx + r_inner * math.sin(ang + math.pi / 4)
        ry = cy - r_inner * math.cos(ang + math.pi / 4)

        draw.polygon([(cx, cy), (tx, ty), (lx, ly)], fill=(230, 195, 80, 255))
        draw.polygon([(cx, cy), (tx, ty), (rx, ry)], fill=(150, 105, 15, 255))

    # Center circle
    draw.circle((cx, cy), radius=int(r_inner * 0.8), fill=(255, 240, 150, 255), outline=(130, 90, 15, 255))
    return im


def create_tactical_reticle(size: int = 40, color=(255, 50, 50, 220)) -> Image.Image:
    """Generate high-tech HUD crosshair target reticle."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r = size / 2 - 3

    # Broken target ring
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color, width=2)
    # Inner dashed ring
    r_in = r * 0.55
    draw.ellipse((cx - r_in, cy - r_in, cx + r_in, cy + r_in), outline=color, width=1)

    # 4 tick marks
    draw.line((cx - r - 2, cy, cx - r + 5, cy), fill=color, width=2)
    draw.line((cx + r - 5, cy, cx + r + 2, cy), fill=color, width=2)
    draw.line((cx, cy - r - 2, cx, cy - r + 5), fill=color, width=2)
    draw.line((cx, cy + r - 5, cx, cy + r + 2), fill=color, width=2)

    # Target locked dot
    draw.circle((cx, cy), radius=2, fill=color)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 13. VIE_nf_medium_force (Lực lượng Hải quân Trung bình)
# =========================================================================
def build_nf_medium_force():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Modern stealth frigate / combatant cutting waves from frigates.dds
    p_frig = MD_GOALS / "00_navy" / "frigates.dds"
    if p_frig.exists():
        im_fr = Image.open(p_frig).convert("RGBA")
        im_fr = im_fr.resize((86, 80), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_fr, offset_x=0, offset_y=-2)

    # Dual combatant formation: Add second silhouette echelon frigate trailing behind
    # ASW Sonar / Depth Charge symbol on bottom right
    sonar_badge = Image.new("RGBA", (26, 26), (0, 0, 0, 0))
    sb_draw = ImageDraw.Draw(sonar_badge)
    sb_draw.ellipse((2, 2, 24, 24), fill=(20, 36, 52, 240), outline=(212, 175, 55, 255), width=2)
    sb_draw.ellipse((6, 6, 20, 20), outline=(0, 220, 255, 220), width=1)
    sb_draw.line((13, 3, 13, 23), fill=(0, 220, 255, 180), width=1)
    sb_draw.line((3, 13, 23, 13), fill=(0, 220, 255, 180), width=1)
    paste_centered(canvas, sonar_badge, offset_x=25, offset_y=18)

    # Top apex: 3D Gold Star
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom left: Anchor
    anchor = create_naval_anchor(w=18, h=22, color_type="gold")
    paste_centered(canvas, anchor, offset_x=-22, offset_y=24)

    save_game_ready_icon(canvas, "nf_medium_force")


# =========================================================================
# 14. VIE_nf_operating_range (Mở rộng Phạm vi Hoạt động)
# =========================================================================
def build_nf_operating_range():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: radar.dds (tactical radar mast with circular saw-tooth bronze compass ring)
    p_rad = MD_GOALS / "00_science" / "radar.dds"
    if p_rad.exists():
        im_rad = Image.open(p_rad).convert("RGBA")
        im_rad = im_rad.resize((84, 84), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_rad, offset_x=0, offset_y=-3)

    # In center: Crisp 8-point nautical compass rose
    compass = create_compass_rose(size=36)
    paste_centered(canvas, compass, offset_x=0, offset_y=6)

    # Expanding maritime range rings (cyan/green radar sweep over ocean)
    sweep = Image.new("RGBA", (48, 48), (0, 0, 0, 0))
    sw_draw = ImageDraw.Draw(sweep)
    swcx, swcy = 24, 24
    sw_draw.ellipse((swcx - 23, swcy - 23, swcx + 23, swcy + 23), outline=(0, 230, 255, 120), width=1)
    sw_draw.ellipse((swcx - 15, swcy - 15, swcx + 15, swcy + 15), outline=(0, 230, 255, 160), width=1)
    paste_centered(canvas, sweep, offset_x=0, offset_y=6)

    # Top apex: 3D Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-34)

    # Bottom: Golden anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "nf_operating_range")


# =========================================================================
# 15. VIE_nf_denial (Ngăn chặn biển / Maritime Denial)
# =========================================================================
def build_nf_denial():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: guided_missile.dds (heavy supersonic missile launching from TEL with plume inside wreath)
    p_mis = MD_GOALS / "00_airforce" / "guided_missile.dds"
    if p_mis.exists():
        im_mis = Image.open(p_mis).convert("RGBA")
        im_mis = im_mis.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_mis, offset_x=0, offset_y=-3)

    # Red tactical target locking reticle overlay
    reticle = create_tactical_reticle(size=36, color=(255, 45, 45, 230))
    paste_centered(canvas, reticle, offset_x=16, offset_y=-10)

    # Top apex: 3D Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_denial")


# =========================================================================
# 16. VIE_nf_denial_defence (Phòng thủ Ven bờ Tích hợp)
# =========================================================================
def build_nf_denial_defence():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: focus_FIN_coastal_defense.dds (heavy coastal turret / missile launcher on waves inside ornate red/gold shield)
    p_fort = MD_GOALS / "finland" / "focus_FIN_coastal_defense.dds"
    if p_fort.exists():
        im_fort = Image.open(p_fort).convert("RGBA")
        im_fort = im_fort.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_fort, offset_x=0, offset_y=-3)

    # Moored naval sea mine on bottom right
    mine = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    m_draw = ImageDraw.Draw(mine)
    mcx, mcy = 12, 12
    # Spikes
    for i in range(6):
        ang = i * math.pi / 3
        m_draw.line((mcx, mcy, mcx + 10 * math.cos(ang), mcy + 10 * math.sin(ang)), fill=(50, 60, 70, 255), width=2)
    # Mine body
    m_draw.ellipse((mcx - 6, mcy - 6, mcx + 6, mcy + 6), fill=(40, 50, 60, 255), outline=(100, 115, 130, 255))
    paste_centered(canvas, mine, offset_x=24, offset_y=20)

    # Top apex: 3D Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom left: Golden anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=-20, offset_y=24)

    save_game_ready_icon(canvas, "nf_denial_defence")


# =========================================================================
# 17. VIE_nf_denial_subs (Lực lượng Tàu ngầm Ngăn chặn)
# =========================================================================
def build_nf_denial_subs():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: torpedo.dds (heavy modern torpedo cruising through foaming blue ocean waves inside steel ring with golden banner)
    p_torp = MD_GOALS / "00_navy" / "torpedo.dds"
    if p_torp.exists():
        im_torp = Image.open(p_torp).convert("RGBA")
        im_torp = im_torp.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_torp, offset_x=0, offset_y=-2)

    # Submerged Kilo submarine sail & hull silhouette in deep blue behind torpedo
    # Red tactical crosshair over the torpedo
    reticle = create_tactical_reticle(size=28, color=(255, 60, 60, 200))
    paste_centered(canvas, reticle, offset_x=20, offset_y=-14)

    # Top apex: 3D Gold Star
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Inscription or anchor on the golden banner at bottom
    anchor = create_naval_anchor(w=14, h=16, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "nf_denial_subs")


def main():
    print("Building Navy Batch 3 focus icons...")
    build_nf_medium_force()
    build_nf_operating_range()
    build_nf_denial()
    build_nf_denial_defence()
    build_nf_denial_subs()
    print("Completed all 5 icons for Navy Batch 3!")


if __name__ == "__main__":
    main()
