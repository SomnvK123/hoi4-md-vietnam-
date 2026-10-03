"""Script to build Batch 4 Focus Icons for Vietnam Navy (Hải quân) in Millennium Dawn.
Batch 4 focuses (Trục 3 Chỉ huy Ven bờ & Hạm đội Vùng biển xanh Greenwater - 5 focuses):
18. nf_denial_command: Bộ chỉ huy Phòng thủ Ven bờ (Đài radar bờ biển, khiên vàng nguyệt quế, quân hiệu VPA, mỏ neo)
19. nf_greenwater: Hải quân Khu vực / Greenwater Fleet (Khinh hạm tuần tra Biển Đông / Đông Nam Á, hải đồ xanh ngọc, la bàn hoa tiêu, sao vàng)
20. nf_regional_frigates: Khinh hạm Viễn hành (Khinh hạm tên lửa tầm xa Gepard 3.9/SIGMA lướt sóng, khiên xanh biển, sao vàng, mỏ neo)
21. nf_amphibious_fleet: Hạm đội Đổ bộ (Tàu đổ bộ LST/LPD đổ quân trên sóng biển, vành nguyệt quế, mỏ neo vàng, sao vàng)
22. nf_lhd_program: Chương trình Tàu đổ bộ Trực thăng (Trực thăng hải quân Ka-28 cất hạ cánh boong tàu LHD, mỏ neo vàng, sao vàng)

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


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 18. VIE_nf_denial_command (Bộ chỉ huy Phòng thủ Ven bờ)
# =========================================================================
def build_nf_denial_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: radar2.dds (coastal tracking radar station inside golden shield with laurel wreath)
    p_rad = MD_GOALS / "00_science" / "radar2.dds"
    if p_rad.exists():
        im_rad = Image.open(p_rad).convert("RGBA")
        im_rad = im_rad.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_rad, offset_x=0, offset_y=-3)

    # VPA Naval Roundel Cockade at center bottom
    cockade = create_vpa_cockade(size=22)
    paste_centered(canvas, cockade, offset_x=0, offset_y=16)

    # Top apex: 3D Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Small gold anchor below the cockade
    anchor = create_naval_anchor(w=14, h=16, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "nf_denial_command")
    return canvas


# =========================================================================
# 19. VIE_nf_greenwater (Hải quân Khu vực / Greenwater Fleet)
# =========================================================================
def build_nf_greenwater() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: CHI_south_chinese_sea (frigate on sea medallion)
    p_scs = MD_GOALS / "china" / "CHI_south_chinese_sea.dds"
    if p_scs.exists():
        scs = Image.open(p_scs).convert("RGBA")
        pixels = scs.load()

        # Inpaint red dashes ONLY in x >= 54, y 24..60
        for y in range(24, 60):
            for x in range(54, 78):
                r, g, b, a = pixels[x, y]
                if r > 100 and r > g * 1.3 and r > b * 1.3:
                    sx = max(42, x - 8)
                    pixels[x, y] = pixels[sx, y]

        # Inpaint mast red flag at y 33..40, x 26..35 to neutral naval haze gray mast
        for y in range(33, 40):
            for x in range(26, 35):
                r, g, b, a = pixels[x, y]
                if r > 90 and r > g * 1.2:
                    pixels[x, y] = (150, 165, 175, 255)

        # Draw an authentic 8-point nautical compass rose on the maritime chart
        overlay = Image.new("RGBA", scs.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)
        cx, cy = 64, 40
        r_out = 13
        r_in = 4

        # Outer degree rings
        d.ellipse((cx - r_out, cy - r_out, cx + r_out, cy + r_out), outline=(215, 185, 80, 150), width=1)
        d.ellipse((cx - r_out + 2, cy - r_out + 2, cx + r_out - 2, cy + r_out - 2), outline=(215, 185, 80, 80), width=1)

        # 8 nautical compass points
        for i in range(8):
            ang = i * math.pi / 4 - math.pi / 2
            r_pt = r_out if i % 2 == 0 else r_out * 0.65
            tip = (cx + r_pt * math.cos(ang), cy + r_pt * math.sin(ang))
            ang_l = ang - math.pi / 8
            ang_r = ang + math.pi / 8
            fl = (cx + r_in * math.cos(ang_l), cy + r_in * math.sin(ang_l))
            fr = (cx + r_in * math.cos(ang_r), cy + r_in * math.sin(ang_r))
            d.polygon([(cx, cy), tip, fl], fill=(255, 225, 90, 220))
            d.polygon([(cx, cy), tip, fr], fill=(160, 120, 20, 210))

        # Center gold hub
        d.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=(255, 240, 150, 255), outline=(130, 95, 20, 255))
        scs.paste(overlay, (0, 0), overlay)

        scs = scs.resize((86, 80), Image.Resampling.LANCZOS)
        paste_centered(canvas, scs, offset_x=0, offset_y=-2)

    # Top apex: 3D Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_greenwater")
    return canvas


# =========================================================================
# 20. VIE_nf_regional_frigates (Khinh hạm Viễn hành)
# =========================================================================
def build_nf_regional_frigates() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: europe_ship.dds (modern naval combatant in front of shield with laurel wreath)
    p_ship = MD_GOALS / "00_navy" / "europe_ship.dds"
    if p_ship.exists():
        im_ship = Image.open(p_ship).convert("RGBA")
        pixels = im_ship.load()

        # Inpaint EU yellow star pixels inside shield (x: 27..65, y: 14..45)
        for y in range(14, 46):
            for x in range(27, 65):
                r, g, b, a = pixels[x, y]
                if a > 100 and r > 105 and g > 95 and (r + g) > b * 1.5:
                    for dist in range(2, 7):
                        found = False
                        for dy in [-dist, 0, dist]:
                            for dx in [-dist, 0, dist]:
                                nx, ny = x + dx, y + dy
                                if 26 <= nx <= 66 and 14 <= ny <= 46:
                                    nr, ng, nb, na = pixels[nx, ny]
                                    if nb > 70 and nb > nr * 1.2:
                                        pixels[x, y] = (nr, ng, nb, na)
                                        found = True
                                        break
                            if found:
                                break
                        if found:
                            break

        im_ship = im_ship.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_ship, offset_x=0, offset_y=-3)

    # In center of deep blue shield: prominent 3D Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-18)

    # Bottom: Golden anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=-20, offset_y=24)

    save_game_ready_icon(canvas, "nf_regional_frigates")
    return canvas


# =========================================================================
# 21. VIE_nf_amphibious_fleet (Hạm đội Đổ bộ)
# =========================================================================
def build_nf_amphibious_fleet() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: generic_landing_ship.dds (modern LST/LPD landing ship on waves in circular wreath)
    p_land = MD_GOALS / "00_navy" / "generic_landing_ship.dds"
    if p_land.exists():
        im_land = Image.open(p_land).convert("RGBA")
        im_land = im_land.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_land, offset_x=0, offset_y=-3)

    # Top apex: 3D Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_amphibious_fleet")
    return canvas


# =========================================================================
# 22. VIE_nf_lhd_program (Chương trình Tàu đổ bộ Trực thăng)
# =========================================================================
def build_nf_lhd_program() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic_Naval_Helicopter.dds (naval helicopter hovering over sea with golden laurel wreath)
    p_heli = MD_GOALS / "00_airforce" / "Generic_Naval_Helicopter.dds"
    if p_heli.exists():
        im_heli = Image.open(p_heli).convert("RGBA")
        im_heli = im_heli.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_heli, offset_x=0, offset_y=-4)

    # Top apex: 3D Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-30)

    # Bottom: Golden anchor in ribbon
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=24)

    save_game_ready_icon(canvas, "nf_lhd_program")
    return canvas


def create_showcase(icons, labels):
    """Generate professional Batch 4 showcase artifact."""
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

    draw.text((15, 12), "HẢI QUÂN NHÂN DÂN VIỆT NAM (HQNDVN) - BATCH 4: VEN BỜ & GREENWATER", fill=(255, 215, 0, 255), font=font_title)

    for i, (icon, label) in enumerate(zip(icons, labels)):
        cx = 15 + i * card_w + 8
        cy = 40

        # Card container
        draw.rounded_rectangle((cx - 4, cy - 4, cx + 93 + 4, cy + 91 + 4), radius=4, fill=(24, 32, 44, 255), outline=(48, 64, 84, 255), width=1)
        im.paste(icon, (cx, cy), icon)

        # Label underneath
        draw.text((cx - 2, cy + 98), label, fill=(215, 225, 235, 255), font=font_label)

    out_path = BRAIN_DIR / "navy_batch_4_showcase.png"
    im.save(out_path)
    print(f"Saved Showcase: {out_path}")


def create_tree_simulation():
    """Generate in-game focus tree simulation diagram for Batch 4."""
    canvas_w = 750
    canvas_h = 420
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

    draw.text((20, 15), "HOI4 / MILLENNIUM DAWN - CÂY TIÊU ĐIỂM HẢI QUÂN (BATCH 4: VEN BỜ & GREENWATER)", fill=(255, 215, 0, 255), font=font_header)
    draw.text((20, 35), "Mô phỏng hiển thị in-game: Trụ sở Ven bờ, Hải quân Khu vực, Khinh hạm, Hạm đội Đổ bộ & Tàu LHD", fill=(160, 175, 195, 255), font=font_sub)

    # Nodes layout:
    # Top anchor: VIE_nf_operating_range (Batch 3) at center (x=460, y=70)
    # Left branch: VIE_nf_denial_subs (Batch 3) at (x=130, y=140) -> VIE_nf_denial_command at (x=130, y=250)
    # Center branch: VIE_nf_operating_range -> VIE_nf_greenwater at (x=460, y=150)
    # From greenwater -> VIE_nf_regional_frigates at (x=350, y=240) and VIE_nf_amphibious_fleet at (x=570, y=240)
    # Converge -> VIE_nf_lhd_program at (x=460, y=320)

    # Golden branch connectors
    c_gold = (190, 150, 45, 255)
    # denial_subs to denial_command
    draw.line((130 + 46, 140 + 70, 130 + 46, 250), fill=c_gold, width=2)
    # operating_range to greenwater
    draw.line((460 + 46, 70 + 70, 460 + 46, 150), fill=c_gold, width=2)
    # greenwater to frigates & amphib
    draw.line((460 + 46, 150 + 70, 460 + 46, 230), fill=c_gold, width=2)
    draw.line((350 + 46, 230, 570 + 46, 230), fill=c_gold, width=2)
    draw.line((350 + 46, 230, 350 + 46, 240), fill=c_gold, width=2)
    draw.line((570 + 46, 230, 570 + 46, 240), fill=c_gold, width=2)
    # frigates & amphib to lhd_program
    draw.line((350 + 46, 240 + 70, 350 + 46, 310), fill=c_gold, width=2)
    draw.line((570 + 46, 240 + 70, 570 + 46, 310), fill=c_gold, width=2)
    draw.line((350 + 46, 310, 570 + 46, 310), fill=c_gold, width=2)
    draw.line((460 + 46, 310, 460 + 46, 320), fill=c_gold, width=2)

    nodes = [
        # Upstream Batch 3 icons
        ("nf_denial_subs", "Tàu ngầm Kilo", 130, 100, False),
        ("nf_operating_range", "Mở rộng Phạm vi HĐ", 460, 55, False),
        # Batch 4 icons
        ("nf_denial_command", "Chỉ huy Bờ biển", 130, 245, True),
        ("nf_greenwater", "HQ Khu vực (Greenwater)", 460, 145, True),
        ("nf_regional_frigates", "Khinh hạm Viễn hành", 350, 235, True),
        ("nf_amphibious_fleet", "Hạm đội Đổ bộ", 570, 235, True),
        ("nf_lhd_program", "Tàu đổ bộ trực thăng LHD", 460, 315, True),
    ]

    for stem, title, nx, ny, is_batch4 in nodes:
        png_p = PNG_DIR / f"{stem}.png"
        if png_p.exists():
            ic = Image.open(png_p).convert("RGBA").resize((70, 68), Image.Resampling.LANCZOS)
        else:
            ic = Image.new("RGBA", (70, 68), (40, 50, 60, 255))

        # Focus box
        outline_c = (235, 195, 60, 255) if is_batch4 else (65, 85, 110, 255)
        fill_c = (26, 36, 50, 255) if is_batch4 else (20, 28, 38, 255)
        draw.rounded_rectangle((nx, ny, nx + 92, ny + 74), radius=4, fill=fill_c, outline=outline_c, width=2 if is_batch4 else 1)
        im.paste(ic, (nx + 11, ny + 3), ic)

        # Title ribbon underneath
        tb_w = 125
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255) if is_batch4 else (180, 195, 210, 255), font=font_foc)

    out_sim = BRAIN_DIR / "navy_batch_4_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Navy Batch 4 focus icons...")
    ic1 = build_nf_denial_command()
    ic2 = build_nf_greenwater()
    ic3 = build_nf_regional_frigates()
    ic4 = build_nf_amphibious_fleet()
    ic5 = build_nf_lhd_program()
    print("Completed all 5 icons for Navy Batch 4!")

    icons = [ic1, ic2, ic3, ic4, ic5]
    labels = [
        "Bộ chỉ huy PT Ven bờ",
        "HQ Khu vực (Greenwater)",
        "Khinh hạm Viễn hành",
        "Hạm đội Đổ bộ",
        "Tàu đổ bộ trực thăng LHD"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 4 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
