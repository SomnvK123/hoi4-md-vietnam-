"""Script to build Batch 1 Focus Icons for Vietnam Navy (Hải quân) in Millennium Dawn.
Batch 1 focuses (Trục 2 Công nghiệp Quốc phòng Hải quân - 7 focuses):
1. nf_training_standardization: Chuẩn hóa Đào tạo Hải quân (Học viện Hải quân, bánh lái, mỏ neo, sao vàng, nguyệt quế)
2. naval_defence_law: Thể chế Quốc phòng Hải quân (Nghị định đóng tàu, ấn triện đỏ, mũi tàu chiến hiện đại, mỏ neo)
3. ba_son_shipyards: Xưởng đóng tàu Ba Son (Ụ đóng tàu, cổng trục gantry crane, vỏ tàu chiến đang đóng, bánh răng, quân kỳ HQ)
4. naval_mro: Bảo dưỡng Hải quân trong nước (Ụ nổi Cam Ranh, cờ lê kỹ thuật đan chéo, thân tàu chiến bảo dưỡng)
5. small_combatant_construction: Đóng tàu chiến cỡ nhỏ (Tàu tên lửa Molniya 1241.8 / TT-400TP rẽ sóng, ống phóng Uran-E)
6. naval_systems_integration: Tích hợp hệ thống hải quân (Đài radar Pozitiv/Sigma C4ISR, mạng pha, HUD hồng tâm, liên kết hỏa lực)
7. naval_defence_2030: Công nghiệp Quốc phòng Hải quân 2030 (Chiến hạm tàng hình tương lai, lưới số, sao vàng, nguyệt quế, mốc 2030)

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
    else: # steel
        c_fill = (180, 195, 205, 255)
        c_light = (225, 235, 245, 255)
        c_dark = (90, 105, 115, 255)

    cx = w / 2
    # Top ring
    ring_r = int(w * 0.16)
    ring_cy = ring_r + 2
    draw.ellipse((cx - ring_r, ring_cy - ring_r, cx + ring_r, ring_cy + ring_r), fill=c_fill, outline=c_dark, width=2)
    inner_r = int(ring_r * 0.45)
    draw.ellipse((cx - inner_r, ring_cy - inner_r, cx + inner_r, ring_cy + inner_r), fill=(0, 0, 0, 0), outline=c_dark, width=1)

    # Crossbar (stock)
    bar_y = int(h * 0.26)
    bar_w = int(w * 0.65)
    bar_h = int(h * 0.09)
    draw.rounded_rectangle((cx - bar_w / 2, bar_y, cx + bar_w / 2, bar_y + bar_h), radius=2, fill=c_fill, outline=c_dark)
    # stock balls at ends
    draw.ellipse((cx - bar_w / 2 - 2, bar_y - 1, cx - bar_w / 2 + bar_h + 1, bar_y + bar_h + 1), fill=c_light, outline=c_dark)
    draw.ellipse((cx + bar_w / 2 - bar_h - 1, bar_y - 1, cx + bar_w / 2 + 2, bar_y + bar_h + 1), fill=c_light, outline=c_dark)

    # Vertical shank
    shank_w = int(w * 0.14)
    shank_top = ring_cy + ring_r - 2
    shank_bot = int(h * 0.78)
    draw.rectangle((cx - shank_w / 2, shank_top, cx + shank_w / 2, shank_bot), fill=c_fill, outline=c_dark)
    # Shank highlight
    draw.line((cx - 1, shank_top + 2, cx - 1, shank_bot - 2), fill=c_light, width=1)

    # Bottom curved crown & flukes
    # Draw arc
    arc_box = (int(w * 0.10), int(h * 0.50), int(w * 0.90), int(h * 0.96))
    draw.arc(arc_box, start=20, end=160, fill=c_fill, width=int(w * 0.13))
    draw.arc(arc_box, start=20, end=160, fill=c_dark, width=1)

    # Fluke tips (triangles pointing up)
    fluke_sz = int(w * 0.20)
    # Left fluke
    lf_x = int(w * 0.16)
    lf_y = int(h * 0.65)
    draw.polygon([(lf_x, lf_y - fluke_sz), (lf_x + fluke_sz, lf_y), (lf_x - fluke_sz // 2, lf_y)], fill=c_light, outline=c_dark)
    # Right fluke
    rf_x = int(w * 0.84)
    rf_y = int(h * 0.65)
    draw.polygon([(rf_x, rf_y - fluke_sz), (rf_x - fluke_sz, rf_y), (rf_x + fluke_sz // 2, rf_y)], fill=c_light, outline=c_dark)

    # Center bottom crown point
    draw.polygon([(cx - 4, int(h * 0.94)), (cx + 4, int(h * 0.94)), (cx, h - 2)], fill=c_fill, outline=c_dark)

    return im


def create_naval_helm(size: int) -> Image.Image:
    """Generate a ship steering wheel (bánh lái)."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 3
    r_inner = r_outer * 0.65

    # 8 handles (spokes extending outward)
    spoke_len = r_outer + 2
    for i in range(8):
        ang = i * math.pi / 4
        x1 = cx + (r_inner * 0.6) * math.cos(ang)
        y1 = cy + (r_inner * 0.6) * math.sin(ang)
        x2 = cx + spoke_len * math.cos(ang)
        y2 = cy + spoke_len * math.sin(ang)
        draw.line((x1, y1, x2, y2), fill=(160, 115, 30, 255), width=3)
        # handle knob
        draw.circle((x2, y2), radius=2, fill=(230, 185, 70, 255), outline=(130, 90, 15, 255))

    # Outer wooden / brass rim
    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), outline=(190, 140, 40, 255), width=3)
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), outline=(140, 95, 20, 255), width=2)

    # Center hub
    r_hub = r_inner * 0.45
    draw.ellipse((cx - r_hub, cy - r_hub, cx + r_hub, cy + r_hub), fill=(210, 160, 45, 255), outline=(120, 80, 15, 255), width=1)
    draw.circle((cx, cy), radius=int(r_hub * 0.4), fill=(255, 220, 90, 255))
    return im


def create_wrench_pair(size: int = 34) -> Image.Image:
    """Generate crossed chrome-steel military mechanic wrenches."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2

    def draw_wrench(angle_deg):
        w_im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        w_draw = ImageDraw.Draw(w_im)
        w_len = int(size * 0.78)
        w_thick = 4
        x0 = cx - w_len / 2
        y0 = cy - w_thick / 2
        # Bar
        w_draw.rounded_rectangle((x0, y0, x0 + w_len, y0 + w_thick), radius=1, fill=(200, 210, 220, 255), outline=(90, 100, 110, 255))
        w_draw.line((x0 + 2, cy - 1, x0 + w_len - 2, cy - 1), fill=(240, 245, 250, 255), width=1)
        # Head 1 (open jaw)
        head_sz = 8
        w_draw.ellipse((x0 - 2, cy - head_sz / 2, x0 + head_sz - 2, cy + head_sz / 2), fill=(185, 195, 205, 255), outline=(80, 90, 100, 255))
        w_draw.polygon([(x0 - 3, cy - 2), (x0 + 3, cy), (x0 - 3, cy + 2)], fill=(0, 0, 0, 0))
        # Head 2 (ring or jaw)
        w_draw.ellipse((x0 + w_len - head_sz + 2, cy - head_sz / 2, x0 + w_len + 2, cy + head_sz / 2), fill=(185, 195, 205, 255), outline=(80, 90, 100, 255))
        w_draw.circle((x0 + w_len - head_sz / 2 + 2, cy), radius=2, fill=(0, 0, 0, 0), outline=(90, 100, 110, 255))
        return w_im.rotate(angle_deg, resample=Image.Resampling.BILINEAR)

    w1 = draw_wrench(42)
    w2 = draw_wrench(-42)
    im.paste(w1, (0, 0), w1)
    im.paste(w2, (0, 0), w2)
    return im


def create_gear_cog(size: int = 36, teeth: int = 8) -> Image.Image:
    """Generate a crisp industrial gear cog."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_out = size / 2 - 2
    r_body = r_out * 0.78
    r_hole = r_body * 0.38

    # Teeth
    for i in range(teeth):
        ang = i * (2 * math.pi / teeth)
        cos_a = math.cos(ang)
        sin_a = math.sin(ang)
        tx = cx + r_out * cos_a
        ty = cy + r_out * sin_a
        half_w = 3
        # normal vector
        nx = -sin_a * half_w
        ny = cos_a * half_w
        pts = [
            (cx + r_body * cos_a - nx * 1.3, cy + r_body * sin_a - ny * 1.3),
            (tx - nx, ty - ny),
            (tx + nx, ty + ny),
            (cx + r_body * cos_a + nx * 1.3, cy + r_body * sin_a + ny * 1.3)
        ]
        draw.polygon(pts, fill=(212, 175, 55, 255), outline=(130, 95, 20, 255))

    # Gear body
    draw.ellipse((cx - r_body, cy - r_body, cx + r_body, cy + r_body), fill=(225, 185, 60, 255), outline=(140, 100, 20, 255), width=2)
    # Highlight ring
    draw.ellipse((cx - r_body + 2, cy - r_body + 2, cx + r_body - 2, cy + r_body - 2), outline=(255, 235, 130, 180), width=1)
    # Center hole
    draw.ellipse((cx - r_hole, cy - r_hole, cx + r_hole, cy + r_hole), fill=(0, 0, 0, 0), outline=(120, 85, 15, 255), width=2)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 1. VIE_nf_training_standardization (Chuẩn hóa Đào tạo Hải quân)
# =========================================================================
def build_nf_training_standardization():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Antwerp Maritime Academy building & laurel badge
    p_acad = MD_GOALS / "00_navy" / "Focus_BEL_antwerp_maritime_academy.dds"
    if p_acad.exists():
        im_acad = Image.open(p_acad).convert("RGBA")
        # Resize to fit inside 93x91 nicely
        im_acad = im_acad.resize((84, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_acad, offset_x=0, offset_y=-4)

    # In front: Wooden / brass naval helm (bánh lái)
    helm = create_naval_helm(size=38)
    paste_centered(canvas, helm, offset_x=0, offset_y=16)

    # Center of helm: Official VPA cockade with gold star
    cockade = create_vpa_cockade(size=18)
    paste_centered(canvas, cockade, offset_x=0, offset_y=16)

    # Anchor at the very bottom center
    anchor = create_naval_anchor(w=20, h=24, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=30)

    save_game_ready_icon(canvas, "nf_training_standardization")


# =========================================================================
# 2. VIE_naval_defence_law (Thể chế Quốc phòng Hải quân)
# =========================================================================
def build_naval_defence_law():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic Naval Treaty (parchment scrolls, red wax seal, modern ship prow, golden wreath)
    p_treaty = MD_GOALS / "00_navy" / "Generic_Naval_Treaty.dds"
    if p_treaty.exists():
        im_tr = Image.open(p_treaty).convert("RGBA")
        im_tr = im_tr.resize((88, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_tr, offset_x=0, offset_y=-2)

    # Golden naval anchor in front of the warship prow
    anchor = create_naval_anchor(w=22, h=26, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=25)

    # Small official VPA star atop the treaty
    star = create_gold_star(14)
    paste_centered(canvas, star, offset_x=-16, offset_y=-24)

    save_game_ready_icon(canvas, "naval_defence_law")


# =========================================================================
# 3. VIE_ba_son_shipyards (Xưởng đóng tàu Ba Son)
# =========================================================================
def build_ba_son_shipyards():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Industrial portal gantry crane with ship in drydock and gold banner
    p_dock = MD_GOALS / "00_economy" / "develop_polish_shipbuilding.dds"
    if p_dock.exists():
        im_dock = Image.open(p_dock).convert("RGBA")
        im_dock = im_dock.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_dock, offset_x=0, offset_y=-4)

    # 3D Gold Star at the pinnacle of the gantry crane
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=-10, offset_y=-32)

    # Inscription "BA SON" on the gold banner at bottom
    try:
        font_bason = ImageFont.truetype("arialbd.ttf", 9)
    except:
        font_bason = ImageFont.load_default()
    
    # Text overlay on banner
    banner_txt = Image.new("RGBA", (50, 14), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(banner_txt)
    b_draw.text((25, 7), "BA SON", fill=(255, 235, 120, 255), font=font_bason, anchor="mm")
    paste_centered(canvas, banner_txt, offset_x=0, offset_y=30)

    # Small gold anchor at center
    anchor = create_naval_anchor(w=14, h=16, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=16)

    save_game_ready_icon(canvas, "ba_son_shipyards")


# =========================================================================
# 4. VIE_naval_mro (Bảo dưỡng Hải quân trong nước)
# =========================================================================
def build_naval_mro():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Modern stealth destroyer inside circular porthole frame with laurel wreath
    p_ship = MD_GOALS / "00_navy" / "generic_ship1.dds"
    if p_ship.exists():
        im_ship = Image.open(p_ship).convert("RGBA")
        im_ship = im_ship.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_ship, offset_x=0, offset_y=-5)

    # In front at bottom: Crossed heavy precision chrome wrenches
    wrenches = create_wrench_pair(size=44)
    paste_centered(canvas, wrenches, offset_x=0, offset_y=20)

    # Center of wrenches: Official VPA Cockade
    cockade = create_vpa_cockade(size=20)
    paste_centered(canvas, cockade, offset_x=0, offset_y=20)

    save_game_ready_icon(canvas, "naval_mro")


# =========================================================================
# 5. VIE_small_combatant_construction (Đóng tàu chiến cỡ nhỏ)
# =========================================================================
def build_small_combatant_construction():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Modern stealth combatant cutting waves inside nautical chain ring
    p_frig = MD_GOALS / "00_navy" / "frigates.dds"
    if p_frig.exists():
        im_fr = Image.open(p_frig).convert("RGBA")
        im_fr = im_fr.resize((86, 82), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_fr, offset_x=0, offset_y=-2)

    # Uran-E / Kh-35 missile launcher canisters on lower right
    canister = Image.new("RGBA", (28, 22), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(canister)
    c_draw.polygon([(4, 18), (22, 4), (25, 7), (7, 21)], fill=(75, 85, 95, 255), outline=(35, 45, 55, 255))
    c_draw.polygon([(1, 14), (19, 0), (22, 3), (4, 17)], fill=(95, 105, 115, 255), outline=(45, 55, 65, 255))
    c_draw.ellipse((17, 0, 23, 4), fill=(180, 50, 50, 255), outline=(40, 40, 40, 255))
    c_draw.ellipse((20, 4, 26, 8), fill=(180, 50, 50, 255), outline=(40, 40, 40, 255))
    paste_centered(canvas, canister, offset_x=24, offset_y=16)

    # In front at bottom-left: Anchor with gold star
    anchor = create_naval_anchor(w=20, h=24, color_type="gold")
    paste_centered(canvas, anchor, offset_x=-22, offset_y=22)

    save_game_ready_icon(canvas, "small_combatant_construction")


# =========================================================================
# 6. VIE_naval_systems_integration (Tích hợp hệ thống hải quân)
# =========================================================================
def build_naval_systems_integration():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Tactical naval radar mast with signal emissions
    p_rad = MD_GOALS / "00_science" / "radar.dds"
    if p_rad.exists():
        im_rad = Image.open(p_rad).convert("RGBA")
        im_rad = im_rad.resize((82, 82), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_rad, offset_x=0, offset_y=-4)

    # Modern warship with radar dome and tactical chevron
    p_upg = MD_GOALS / "00_navy" / "naval_upgrade.dds"
    if p_upg.exists():
        im_upg = Image.open(p_upg).convert("RGBA")
        im_upg = im_upg.resize((72, 63), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_upg, offset_x=2, offset_y=10)

    # Tactical radar HUD overlay (concentric radar range circles and sweeping vector)
    hud = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(hud)
    hcx, hcy = 22, 22
    h_draw.ellipse((hcx - 20, hcy - 20, hcx + 20, hcy + 20), outline=(0, 220, 255, 180), width=1)
    h_draw.ellipse((hcx - 12, hcy - 12, hcx + 12, hcy + 12), outline=(0, 220, 255, 200), width=1)
    h_draw.ellipse((hcx - 4, hcy - 4, hcx + 4, hcy + 4), outline=(0, 255, 200, 230), width=1)
    h_draw.line((hcx - 21, hcy, hcx + 21, hcy), fill=(0, 220, 255, 150), width=1)
    h_draw.line((hcx, hcy - 21, hcx, hcy + 21), fill=(0, 220, 255, 150), width=1)
    h_draw.circle((hcx + 8, hcy - 7), radius=2, fill=(255, 60, 60, 255))
    paste_centered(canvas, hud, offset_x=18, offset_y=-18)

    # Gold star at the top apex of the radar tower
    star = create_gold_star(14)
    paste_centered(canvas, star, offset_x=0, offset_y=-34)

    save_game_ready_icon(canvas, "naval_systems_integration")


# =========================================================================
# 7. VIE_naval_defence_2030 (Công nghiệp Quốc phòng Hải quân 2030)
# =========================================================================
def build_naval_defence_2030():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Golden hex shield with 3 modern warships cutting foaming waves & golden wreath
    p_fleet = MD_GOALS / "00_navy" / "focus_generic_large_navy.dds"
    if p_fleet.exists():
        im_fleet = Image.open(p_fleet).convert("RGBA")
        im_fleet = im_fleet.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_fleet, offset_x=0, offset_y=-3)

    # Top apex: Large faceted 3D Gold Star with radiant rays
    star = create_gold_star(22)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Milestone Banner at Bottom: "2030"
    banner_w, banner_h = 48, 18
    banner = Image.new("RGBA", (banner_w, banner_h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(banner)
    # Gold ribbon with dark navy inlay
    b_draw.polygon([
        (0, banner_h // 2), (4, 0), (banner_w - 5, 0), (banner_w - 1, banner_h // 2),
        (banner_w - 5, banner_h - 1), (4, banner_h - 1)
    ], fill=(212, 175, 55, 255), outline=(130, 95, 20, 255))
    b_draw.polygon([
        (3, banner_h // 2), (6, 2), (banner_w - 7, 2), (banner_w - 4, banner_h // 2),
        (banner_w - 7, banner_h - 3), (6, banner_h - 3)
    ], fill=(15, 28, 48, 255))

    # Text "2030"
    try:
        font = ImageFont.truetype("arialbd.ttf", 11)
    except:
        font = ImageFont.load_default()
    b_draw.text((banner_w // 2, banner_h // 2 - 1), "2030", fill=(255, 225, 90, 255), font=font, anchor="mm")

    paste_centered(canvas, banner, offset_x=0, offset_y=28)

    save_game_ready_icon(canvas, "naval_defence_2030")


def main():
    print("Building Navy Batch 1 focus icons...")
    build_nf_training_standardization()
    build_naval_defence_law()
    build_ba_son_shipyards()
    build_naval_mro()
    build_small_combatant_construction()
    build_naval_systems_integration()
    build_naval_defence_2030()
    print("Completed all 7 icons for Navy Batch 1!")


if __name__ == "__main__":
    main()
