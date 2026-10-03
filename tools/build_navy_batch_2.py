"""Script to build Batch 2 Focus Icons for Vietnam Navy (Hải quân) in Millennium Dawn.
Batch 2 focuses (Trục 3 Lực lượng & Bộ chỉ huy Khởi đầu - 5 focuses):
8.  nf_surface_force: Phát triển Lực lượng Tàu mặt nước (Khinh hạm tàng hình, pháo hạm, khiên đỏ vàng, mỏ neo)
9.  nf_submarine_force: Phát triển Lực lượng Tàu ngầm (Tàu ngầm Kilo 636.1 lặn sâu, sóng âm sonar, sao vàng)
10. nf_command_reform_1: Cải cách Bộ chỉ huy Hải quân I (Bộ Tư lệnh HQ, khiên chỉ huy mạ vàng, mỏ neo, chevron cấp 1)
11. nf_first_force: Cơ cấu Lực lượng Ban đầu (Biên đội hỗn hợp mặt nước - tàu ngầm, khiên hải quân, nguyệt quế)
12. nf_command_reform_2: Cải cách Bộ chỉ huy Hải quân II (Bánh lái hải đoàn, nòng pháo hạm, 2 chevron nâng cấp, quân hiệu VPA)

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


def create_naval_chevron(w: int = 24, h: int = 12, double: bool = False) -> Image.Image:
    """Generate military naval chevrons for command ranks."""
    total_h = h if not double else h + 8
    im = Image.new("RGBA", (w, total_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    def draw_single_chev(top_y):
        thick = 4
        cx = w / 2
        pts = [
            (2, top_y + h - 2), (cx, top_y + 2), (w - 2, top_y + h - 2),
            (w - 2, top_y + h + thick - 2), (cx, top_y + thick + 2), (2, top_y + h + thick - 2)
        ]
        draw.polygon(pts, fill=(255, 215, 0, 255), outline=(160, 120, 20, 255))
        draw.line([(3, top_y + h - 1), (cx, top_y + 3), (w - 3, top_y + h - 1)], fill=(255, 240, 140, 255), width=1)

    if double:
        draw_single_chev(0)
        draw_single_chev(7)
    else:
        draw_single_chev(0)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 8. VIE_nf_surface_force (Phát triển Lực lượng Tàu mặt nước)
# =========================================================================
def build_nf_surface_force():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: arm_Reformador (modern stealth frigate with automated turret on red shield)
    p_ref = MD_GOALS / "00_navy" / "arm_Reformador.dds"
    if p_ref.exists():
        im_ref = Image.open(p_ref).convert("RGBA")
        im_ref = im_ref.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_ref, offset_x=0, offset_y=-3)

    # 3D Gold Star of Vietnam at top apex
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden naval anchor on bottom rim
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_surface_force")


# =========================================================================
# 9. VIE_nf_submarine_force (Phát triển Lực lượng Tàu ngầm)
# =========================================================================
def build_nf_submarine_force():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic_Submarine2 (modern teardrop submarine diving deep underwater)
    p_sub = MD_GOALS / "00_navy" / "Generic_Submarine2.dds"
    if p_sub.exists():
        im_sub = Image.open(p_sub).convert("RGBA")
        im_sub = im_sub.resize((88, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_sub, offset_x=0, offset_y=-3)

    # Sonar acoustic concentric emission rings
    sonar = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(sonar)
    scx, scy = 22, 22
    s_draw.ellipse((scx - 20, scy - 20, scx + 20, scy + 20), outline=(0, 200, 255, 120), width=1)
    s_draw.ellipse((scx - 13, scy - 13, scx + 13, scy + 13), outline=(0, 230, 255, 160), width=1)
    s_draw.ellipse((scx - 6, scy - 6, scx + 6, scy + 6), outline=(0, 255, 230, 200), width=1)
    paste_centered(canvas, sonar, offset_x=-14, offset_y=-6)

    # 3D Gold Star at top apex
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Small gold anchor at bottom
    anchor = create_naval_anchor(w=15, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_submarine_force")


# =========================================================================
# 10. VIE_nf_command_reform_1 (Cải cách Bộ chỉ huy Hải quân I)
# =========================================================================
def build_nf_command_reform_1():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic_Command_Power (glorious gold star in tactical shield with laurel wreath)
    p_cmd = MD_GOALS / "00_army" / "Generic_Command_Power.dds"
    if p_cmd.exists():
        im_cmd = Image.open(p_cmd).convert("RGBA")
        im_cmd = im_cmd.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_cmd, offset_x=0, offset_y=-3)

    # Golden naval anchor overlaid in center of star
    anchor = create_naval_anchor(w=20, h=26, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=-2)

    # Command Rank Chevron 1 at bottom
    chev = create_naval_chevron(w=22, h=10, double=False)
    paste_centered(canvas, chev, offset_x=0, offset_y=24)

    save_game_ready_icon(canvas, "nf_command_reform_1")


# =========================================================================
# 11. VIE_nf_first_force (Cơ cấu Lực lượng Ban đầu)
# =========================================================================
def build_nf_first_force():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: destroyers.dds (sleek modern combatant, silver anchor, blue medallion, golden laurel wreath)
    p_dest = MD_GOALS / "00_navy" / "destroyers.dds"
    if p_dest.exists():
        im_dest = Image.open(p_dest).convert("RGBA")
        im_dest = im_dest.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_dest, offset_x=0, offset_y=-2)

    # Top apex: 3D Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Tactical rank 1 chevron
    chev = create_naval_chevron(w=22, h=10, double=False)
    paste_centered(canvas, chev, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "nf_first_force")


# =========================================================================
# 12. VIE_nf_command_reform_2 (Cải cách Bộ chỉ huy Hải quân II)
# =========================================================================
def build_nf_command_reform_2():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: navy2.dds (steering wheel helm mounted on crossed naval cannon barrels inside ornate shield)
    p_navy2 = MD_GOALS / "00_navy" / "navy2.dds"
    if p_navy2.exists():
        im_navy2 = Image.open(p_navy2).convert("RGBA")
        im_navy2 = im_navy2.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_navy2, offset_x=0, offset_y=-4)

    # Center: Official VPA Cockade
    cockade = create_vpa_cockade(size=22)
    paste_centered(canvas, cockade, offset_x=0, offset_y=-4)

    # Double Chevrons for Command Reform II at bottom
    chev = create_naval_chevron(w=26, h=10, double=True)
    paste_centered(canvas, chev, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_command_reform_2")


def main():
    print("Building Navy Batch 2 focus icons...")
    build_nf_surface_force()
    build_nf_submarine_force()
    build_nf_command_reform_1()
    build_nf_first_force()
    build_nf_command_reform_2()
    print("Completed all 5 icons for Navy Batch 2!")


if __name__ == "__main__":
    main()
