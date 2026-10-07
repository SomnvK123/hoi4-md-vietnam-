"""Redesigned Focus Icons for Vietnam Diplomacy (Cluster 1: 12 Focuses)
Cluster 1: Láng giềng Đông Dương & Trục Quan hệ Việt - Trung
1.  border_settlement: Hoàn tất Phân giới Cắm mốc Biên giới
2.  special_relations_laos: Quan hệ đặc biệt với Lào
3.  cambodia_relations: Quan hệ với Campuchia
4.  indochina_solidarity: Đoàn kết Đông Dương
5.  indochina_federation: Liên bang Đông Dương
6.  16_words: Phương châm 16 chữ và tinh thần 4 tốt
7.  border_trade_gates: Cửa khẩu thương mại biên giới
8.  defence_hotline: Đường dây nóng quốc phòng và tránh va chạm
9.  gulf_of_tonkin: Phân định Vịnh Bắc Bộ
10. shared_future: Cộng đồng chia sẻ tương lai
11. cambodia_border: Phân giới cắm mốc biên giới với Campuchia
12. funan_techo_response: Ứng phó kênh đào Phù Nam Techo

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
"""

import math
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"

TARGET_SIZE = (93, 91)

# =========================================================================
# ESSENTIAL HERALDRY & PROCEDURAL FLAGS
# =========================================================================

def save_game_ready_icon(canvas: Image.Image, stem: str):
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border
    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)

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
    print(f"  [SAVED] {stem} -> PNG & DDS (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
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

    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(160, 120, 10, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        v_left = pts[(i * 2 - 1) % 10]
        v_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, v_left], fill=(255, 248, 125, 170))
        draw.polygon([center, tip, v_right], fill=(185, 135, 10, 180))
    return im


def create_gold_star_with_glow(size: int, shadow_blur: float = 1.3) -> Image.Image:
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(shadow_blur))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas


def render_vietnam_flag(size: tuple = (34, 23), waving: bool = True) -> Image.Image:
    """Render 100% authentic Cờ đỏ sao vàng (Red flag, 5-pointed gold star in center)."""
    w, h = size
    im = Image.new("RGBA", size, (218, 37, 29, 255))
    draw = ImageDraw.Draw(im)
    cx, cy = w / 2, h / 2
    r_outer = h * 0.38
    r_inner = r_outer * 0.382
    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(180, 130, 10, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        v_left = pts[(i * 2 - 1) % 10]
        v_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, v_left], fill=(255, 248, 120, 220))
        draw.polygon([center, tip, v_right], fill=(200, 145, 15, 220))

    if waving:
        wave = Image.new("RGBA", size, (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave)
        for x in range(w):
            val = int(28 * math.sin(x / w * math.pi * 2.8))
            if val > 0:
                wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
            else:
                wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
        im = Image.alpha_composite(im, wave)

    # Gold fringe border
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], outline=(235, 195, 45, 240), width=1)
    return im


def render_laos_flag(size: tuple = (34, 23), waving: bool = True) -> Image.Image:
    """Render authentic Laos National Flag (Red-Blue-Red with white central disc)."""
    w, h = size
    im = Image.new("RGBA", size, (206, 17, 38, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, int(h * 0.25), w, int(h * 0.75)], fill=(0, 40, 104, 255))
    r = h * 0.2
    draw.ellipse([w / 2 - r, h / 2 - r, w / 2 + r, h / 2 + r], fill=(255, 255, 255, 255))
    if waving:
        wave = Image.new("RGBA", size, (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave)
        for x in range(w):
            val = int(28 * math.sin(x / w * math.pi * 2.8))
            if val > 0:
                wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
            else:
                wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
        im = Image.alpha_composite(im, wave)
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], outline=(235, 195, 45, 240), width=1)
    return im


def render_cambodia_flag(size: tuple = (34, 23), waving: bool = True) -> Image.Image:
    """Render authentic Cambodia National Flag (Blue-Red-Blue with Angkor Wat)."""
    w, h = size
    im = Image.new("RGBA", size, (3, 46, 161, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, int(h * 0.25), w, int(h * 0.75)], fill=(218, 18, 26, 255))
    cx, cy = w / 2, h / 2
    draw.rectangle([cx - 7, cy - 1, cx + 7, cy + 5], fill=(255, 255, 255, 255))
    draw.polygon([(cx, cy - 5), (cx - 2, cy), (cx + 2, cy)], fill=(255, 255, 255, 255))
    draw.polygon([(cx - 5, cy - 3), (cx - 7, cy), (cx - 3, cy)], fill=(255, 255, 255, 255))
    draw.polygon([(cx + 5, cy - 3), (cx + 3, cy), (cx + 7, cy)], fill=(255, 255, 255, 255))
    if waving:
        wave = Image.new("RGBA", size, (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave)
        for x in range(w):
            val = int(28 * math.sin(x / w * math.pi * 2.8))
            if val > 0:
                wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
            else:
                wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
        im = Image.alpha_composite(im, wave)
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], outline=(235, 195, 45, 240), width=1)
    return im


def create_golden_laurel_wreath(width: int = 86, height: int = 74) -> Image.Image:
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = width / 2, height / 2 + 6
    rx, ry = width * 0.43, height * 0.45

    c_leaf = (235, 190, 40, 255)
    c_leaf_hl = (255, 235, 115, 255)
    c_shadow = (140, 95, 15, 255)

    num_leaves = 13
    for side in (-1, 1):
        for i in range(num_leaves):
            t = i / (num_leaves - 1)
            ang = math.pi * 0.55 + t * math.pi * 0.85 if side == -1 else math.pi * 0.45 - t * math.pi * 0.85
            px = cx + rx * math.cos(ang)
            py = cy + ry * math.sin(ang)
            tang_x = -rx * math.sin(ang)
            tang_y = ry * math.cos(ang)
            tang_len = math.hypot(tang_x, tang_y) + 1e-5
            tang_x /= tang_len
            tang_y /= tang_len

            leaf_ang = math.atan2(tang_y, tang_x) + (0.45 if side == -1 else -0.45)
            leaf_len = 8.5
            tip_x = px + leaf_len * math.cos(leaf_ang)
            tip_y = py + leaf_len * math.sin(leaf_ang)
            norm_x = -math.sin(leaf_ang) * 2.1
            norm_y = math.cos(leaf_ang) * 2.1

            pts = [
                (px, py),
                (px + leaf_len * 0.5 * math.cos(leaf_ang) + norm_x, py + leaf_len * 0.5 * math.sin(leaf_ang) + norm_y),
                (tip_x, tip_y),
                (px + leaf_len * 0.5 * math.cos(leaf_ang) - norm_x, py + leaf_len * 0.5 * math.sin(leaf_ang) - norm_y),
            ]
            draw.polygon(pts, fill=c_leaf, outline=c_shadow)
            draw.line([(px, py), (tip_x, tip_y)], fill=c_leaf_hl, width=1)
    return im


def apply_ambient_drop_shadow(canvas: Image.Image, radius: float = 1.8) -> Image.Image:
    out = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow.paste(canvas, (0, 1), canvas)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(radius))
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.8))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))
    out.paste(shadow, (0, 0), shadow)
    out.paste(canvas, (0, 0), canvas)
    return out


def load_md_goal(rel_path: str, target_box: tuple = (76, 68), enhance_color: float = 1.25) -> Image.Image:
    p = MD_GOALS / rel_path
    if not p.exists():
        return Image.new("RGBA", target_box, (0, 0, 0, 0))
    im = Image.open(p).convert("RGBA")
    if enhance_color != 1.0:
        im = ImageEnhance.Color(im).enhance(enhance_color)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    im.thumbnail(target_box, Image.Resampling.LANCZOS)
    return im


# =========================================================================
# 12 CLUSTER 1 BUILDERS - 100% UNIQUE & AUTHENTIC
# =========================================================================

# 1. VIE_border_settlement: Cột mốc biên giới chính quy Quốc huy mạ vàng & dãy núi biên cương
def build_border_settlement() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Northern karst mountain background in dawn mist
    bg = Image.new("RGBA", (84, 52), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bg)
    # Layered green-teal mountains
    bdraw.polygon([(0, 50), (14, 18), (30, 32), (48, 12), (66, 26), (84, 16), (84, 50)], fill=(45, 95, 80, 180))
    bdraw.polygon([(0, 50), (22, 28), (42, 20), (58, 30), (74, 22), (84, 34), (84, 50)], fill=(65, 125, 105, 220))
    canvas.paste(bg, ((TARGET_SIZE[0] - bg.width) // 2, 22), bg)

    # Imposing 3D Granite Milestone (Cột Mốc Biên Giới Số 1111)
    milestone = Image.new("RGBA", (42, 54), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(milestone)
    # Stone pedestal
    mdraw.polygon([(4, 46), (38, 46), (36, 52), (6, 52)], fill=(120, 125, 130, 255), outline=(60, 65, 70, 255))
    # Beveled granite pillar (white-gray granite with fine speckles)
    mdraw.polygon([(21, 2), (37, 10), (35, 46), (7, 46), (5, 10)], fill=(215, 218, 222, 255), outline=(90, 95, 100, 255), width=2)
    # Right shaded facet
    mdraw.polygon([(21, 2), (37, 10), (35, 46), (21, 46)], fill=(175, 180, 185, 255))
    # Left highlight facet
    mdraw.polygon([(21, 2), (5, 10), (7, 46), (21, 46)], fill=(235, 238, 242, 255))

    # Gilded National Coat of Arms plaque (Quốc huy Việt Nam)
    mdraw.ellipse([11, 14, 31, 34], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    s_core = create_gold_star(11)
    milestone.paste(s_core, (15, 18), s_core)
    # Milestone inscription line "VIỆT NAM"
    mdraw.rectangle([13, 38, 29, 41], fill=(218, 37, 29, 255))

    canvas.paste(milestone, ((TARGET_SIZE[0] - milestone.width) // 2, 26), milestone)

    # Brass Surveyor Theodolite Transit on tripod to the right
    theo = Image.new("RGBA", (24, 38), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(theo)
    # Tripod legs
    tdraw.line([(12, 14), (2, 36)], fill=(150, 95, 30, 255), width=2)
    tdraw.line([(12, 14), (12, 37)], fill=(180, 120, 45, 255), width=2)
    tdraw.line([(12, 14), (22, 36)], fill=(120, 75, 20, 255), width=2)
    # Theodolite scope in brass
    tdraw.polygon([(6, 10), (18, 8), (17, 14), (5, 16)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    tdraw.ellipse([9, 11, 15, 17], fill=(255, 225, 75, 255))
    canvas.paste(theo, (TARGET_SIZE[0] - 28, 42), theo)

    # Radiant summit gold star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "border_settlement")
    return canvas


# 2. VIE_special_relations_laos: Tháp Pha That Luang & Đài Sen Việt Nam, Cờ đỏ sao vàng & Cờ Lào
def build_special_relations_laos() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Truong Son mountains background in morning sun
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Grand Centerpiece: Golden Stupa of Pha That Luang & Vietnamese Lotus Pavilion
    mon = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mon)
    # Pha That Luang golden tiered spire in rich faceted gold
    # Base terrace
    mdraw.polygon([(8, 44), (42, 44), (38, 32), (12, 32)], fill=(235, 195, 45, 255), outline=(140, 95, 15, 255), width=1)
    mdraw.polygon([(14, 32), (36, 32), (32, 20), (18, 20)], fill=(255, 225, 75, 255), outline=(150, 105, 20, 255))
    # Central needle spire
    mdraw.polygon([(22, 20), (28, 20), (26, 4), (24, 4)], fill=(255, 240, 110, 255), outline=(170, 120, 20, 255))
    mdraw.ellipse([23, 2, 27, 6], fill=(255, 255, 160, 255))
    # Red & gold lotus pedestal
    mdraw.chord([12, 36, 38, 47], 0, 180, fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))

    canvas.paste(mon, ((TARGET_SIZE[0] - mon.width) // 2, 24), mon)

    # Two Authentic Flags flanking with golden ceremonial staffs
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_lao = render_laos_flag(size=(32, 21), waving=True)

    # Flagpoles in brass gold
    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_lao, (TARGET_SIZE[0] - 6 - f_lao.width, 36), f_lao)

    # Center golden friendship medallion
    med = Image.new("RGBA", (28, 24), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 25, 23], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([4, 3, 23, 21], fill=(218, 37, 29, 255))
    s_med = create_gold_star(8)
    med.paste(s_med, (10, 8), s_med)
    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 58), med)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "special_relations_laos")
    return canvas


# 3. VIE_cambodia_relations: Tháp đá Angkor Wat soi bóng dòng Mê Kông, Cờ đỏ sao vàng & Cờ Campuchia
def build_cambodia_relations() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Angkor Wat Stone Towers Monument
    angkor = Image.new("RGBA", (52, 46), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(angkor)
    # Temple foundation in carved stone sandstone
    adraw.polygon([(4, 42), (48, 42), (44, 28), (8, 28)], fill=(170, 155, 140, 255), outline=(85, 75, 65, 255), width=2)
    # Center grand tower
    adraw.polygon([(20, 28), (32, 28), (28, 6), (24, 6)], fill=(195, 180, 165, 255), outline=(95, 85, 75, 255))
    adraw.polygon([(23, 6), (29, 6), (26, 2)], fill=(235, 195, 45, 255))
    # Left tower
    adraw.polygon([(10, 28), (18, 28), (15, 12), (13, 12)], fill=(160, 145, 130, 255), outline=(80, 70, 60, 255))
    adraw.polygon([(12, 12), (16, 12), (14, 8)], fill=(235, 195, 45, 255))
    # Right tower
    adraw.polygon([(34, 28), (42, 28), (39, 12), (37, 12)], fill=(160, 145, 130, 255), outline=(80, 70, 60, 255))
    adraw.polygon([(36, 12), (40, 12), (38, 8)], fill=(235, 195, 45, 255))
    # Mekong River blue water reflection
    adraw.chord([2, 38, 50, 46], 0, 180, fill=(30, 110, 175, 255), outline=(235, 195, 45, 255))

    canvas.paste(angkor, ((TARGET_SIZE[0] - angkor.width) // 2, 26), angkor)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_cam = render_cambodia_flag(size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_cam, (TARGET_SIZE[0] - 6 - f_cam.width, 36), f_cam)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cambodia_relations")
    return canvas


# 4. VIE_indochina_solidarity: Ngọn đuốc đồng đoàn kết rực lửa, ba lá cờ chính quy VN-Lào-Campuchia
def build_indochina_solidarity() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Great Golden Solidarity Torch
    torch = Image.new("RGBA", (48, 52), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(torch)
    # Torch bronze handle & bowl
    tdraw.polygon([(20, 22), (28, 22), (26, 48), (22, 48)], fill=(185, 130, 35, 255), outline=(110, 70, 15, 255), width=2)
    tdraw.polygon([(14, 18), (34, 18), (28, 26), (20, 26)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    # Brilliant roaring flame in gradient orange-gold-white
    tdraw.polygon([(24, 2), (32, 10), (30, 18), (18, 18), (16, 10)], fill=(255, 120, 20, 255))
    tdraw.polygon([(24, 4), (29, 11), (27, 18), (21, 18), (19, 11)], fill=(255, 210, 40, 255))
    tdraw.polygon([(24, 6), (27, 13), (25, 17), (23, 17), (21, 13)], fill=(255, 255, 180, 255))

    canvas.paste(torch, ((TARGET_SIZE[0] - torch.width) // 2, 18), torch)

    # 3 Authentic Waving Flags surrounding the torch
    f_lao = render_laos_flag(size=(26, 17), waving=True)
    f_vie = render_vietnam_flag(size=(30, 20), waving=True)
    f_cam = render_cambodia_flag(size=(26, 17), waving=True)

    canvas.paste(f_lao, (6, 38), f_lao)
    canvas.paste(f_cam, (TARGET_SIZE[0] - 6 - f_cam.width, 38), f_cam)
    # Vietnam flag at center forefront
    canvas.paste(f_vie, ((TARGET_SIZE[0] - f_vie.width) // 2, 46), f_vie)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "indochina_solidarity")
    return canvas


# 5. VIE_indochina_federation: Bản đồ bán đảo Đông Dương mạ vàng, cánh đại bàng & 3 ngôi sao vàng
def build_indochina_federation() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Grand Heraldic Crest with Indochina Peninsula Map Relief
    crest = Image.new("RGBA", (54, 52), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(crest)
    # Imperial eagle wings / radiant mantle behind
    cdraw.polygon([(27, 2), (52, 14), (46, 42), (27, 50), (8, 42), (2, 14)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.polygon([(27, 6), (48, 16), (43, 39), (27, 46), (11, 39), (6, 16)], fill=(160, 20, 20, 255), outline=(255, 225, 75, 255), width=1)

    # Indochina Peninsula Golden Silhouette Relief
    # S-shape curve of Vietnam, Laos, Cambodia
    pts_map = [
        (22, 14), (32, 15), (36, 22), (32, 30), (34, 38), (30, 44),
        (26, 44), (28, 38), (24, 34), (20, 36), (18, 28), (22, 22)
    ]
    cdraw.polygon(pts_map, fill=(255, 235, 95, 255), outline=(170, 120, 15, 255))

    # Triumvirate of 3 3D Gold Stars
    s_top = create_gold_star(12)
    s_l = create_gold_star(9)
    s_r = create_gold_star(9)
    crest.paste(s_top, (21, 8), s_top)
    crest.paste(s_l, (11, 22), s_l)
    crest.paste(s_r, (34, 22), s_r)

    canvas.paste(crest, ((TARGET_SIZE[0] - crest.width) // 2, 22), crest)

    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "indochina_federation")
    return canvas


# 6. VIE_16_words: Cuộn thư chiếu hoàng gia gấm lụa chạm rồng, triện son và bồ câu hòa bình
def build_16_words() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Magnificent Imperial Diplomatic Scroll (Thư chiếu ngoại giao 16 chữ vàng)
    scroll = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scroll)
    # Scroll parchment in aged ivory with gold borders
    sdraw.rounded_rectangle([5, 8, 44, 40], radius=4, fill=(248, 242, 220, 255), outline=(190, 145, 30, 255), width=2)
    # Scroll carved wooden/gold roller rods
    sdraw.rectangle([2, 5, 7, 43], fill=(225, 185, 45, 255), outline=(130, 90, 15, 255))
    sdraw.rectangle([42, 5, 47, 43], fill=(225, 185, 45, 255), outline=(130, 90, 15, 255))
    # Red & gold header brocade
    sdraw.rectangle([8, 10, 41, 15], fill=(218, 37, 29, 255))
    # Four lines representing "16 chữ vàng - 4 tốt"
    for y in [19, 24, 29, 34]:
        sdraw.line([(11, y), (38, y)], fill=(160, 30, 30, 255), width=2)
    # Imperial vermilion wax seal with national star
    sdraw.ellipse([18, 20, 31, 33], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    s_seal = create_gold_star(7)
    scroll.paste(s_seal, (21, 23), s_seal)

    canvas.paste(scroll, ((TARGET_SIZE[0] - scroll.width) // 2, 28), scroll)

    # Two Golden Peace Doves carrying olive branch over scroll
    doves = Image.new("RGBA", (44, 20), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(doves)
    # Left dove
    ddraw.polygon([(6, 14), (14, 6), (18, 10), (14, 16)], fill=(255, 255, 255, 255), outline=(215, 175, 45, 255))
    # Right dove
    ddraw.polygon([(38, 14), (30, 6), (26, 10), (30, 16)], fill=(255, 255, 255, 255), outline=(215, 175, 45, 255))
    canvas.paste(doves, ((TARGET_SIZE[0] - doves.width) // 2, 14), doves)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "16_words")
    return canvas


# 7. VIE_border_trade_gates: Cổng Cửa khẩu Quốc tế Hữu Nghị mái ngói ba tầng, barie & container
def build_border_trade_gates() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Majestic International Border Gate (Cổng Cửa Khẩu Hữu Nghị)
    gate = Image.new("RGBA", (52, 48), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gate)
    # Monumental stone arch walls in granite-ochre
    gdraw.polygon([(6, 46), (6, 18), (26, 12), (46, 18), (46, 46), (36, 46), (36, 26), (16, 26), (16, 46)],
                  fill=(220, 195, 150, 255), outline=(120, 90, 50, 255), width=2)
    # Multi-tiered curved pagoda tile eaves in terracotta crimson
    gdraw.polygon([(2, 20), (26, 8), (50, 20), (26, 14)], fill=(195, 45, 30, 255), outline=(100, 20, 15, 255))
    gdraw.polygon([(8, 12), (26, 4), (44, 12), (26, 8)], fill=(220, 55, 35, 255), outline=(100, 20, 15, 255))

    # Center gateway arch passage
    gdraw.rounded_rectangle([18, 26, 34, 46], radius=3, fill=(35, 45, 60, 255), outline=(235, 195, 45, 255))

    # Red plaque with golden national star on arch forehead
    gdraw.rectangle([20, 16, 32, 22], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))
    s_gate = create_gold_star(6)
    gate.paste(s_gate, (23, 16), s_gate)

    # Modern automated customs boom barrier & container freight transport
    gdraw.line([(10, 42), (42, 42)], fill=(255, 230, 80, 255), width=2)
    # Clearance stamp seal in gold
    gdraw.ellipse([34, 30, 46, 42], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    s_stamp = create_gold_star(6)
    gate.paste(s_stamp, (37, 33), s_stamp)

    canvas.paste(gate, ((TARGET_SIZE[0] - gate.width) // 2, 24), gate)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "border_trade_gates")
    return canvas


# 8. VIE_defence_hotline: Bàn điện thoại đỏ điều hành quân sự, màn hình radar quét tọa độ Biển Đông
def build_defence_hotline() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Direct Defense Hotline Console with Tactical Radar Grid
    hotline = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(hotline)

    # Radar display screen in background
    hdraw.ellipse([10, 4, 40, 34], fill=(15, 40, 30, 255), outline=(40, 160, 90, 255), width=2)
    hdraw.ellipse([16, 10, 34, 28], outline=(50, 190, 110, 200))
    hdraw.line([(25, 4), (25, 34)], fill=(50, 190, 110, 160))
    hdraw.line([(10, 19), (40, 19)], fill=(50, 190, 110, 160))
    # Glowing radar sweep beam
    hdraw.polygon([(25, 19), (38, 9), (40, 15)], fill=(80, 255, 140, 160))

    # Crimson Direct Hotline Desk Phone
    # Console base in military crimson
    hdraw.rounded_rectangle([8, 20, 42, 44], radius=4, fill=(195, 25, 25, 255), outline=(100, 15, 15, 255), width=2)
    # Golden rotary/keypad disc
    hdraw.ellipse([18, 26, 32, 40], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    # Telephone handset resting across
    hdraw.rounded_rectangle([4, 15, 46, 23], radius=3, fill=(150, 20, 20, 255), outline=(80, 10, 10, 255), width=2)
    hdraw.rounded_rectangle([2, 12, 12, 26], radius=3, fill=(210, 30, 30, 255), outline=(90, 10, 10, 255))
    hdraw.rounded_rectangle([38, 12, 48, 26], radius=3, fill=(210, 30, 30, 255), outline=(90, 10, 10, 255))

    # Star on dial
    s_dial = create_gold_star(8)
    hotline.paste(s_dial, (21, 29), s_dial)

    canvas.paste(hotline, ((TARGET_SIZE[0] - hotline.width) // 2, 26), hotline)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "defence_hotline")
    return canvas


# 9. VIE_gulf_of_tonkin: Hải đồ phân định Vịnh Bắc Bộ 2000, compa hàng hải đồng và ngọn hải đăng
def build_gulf_of_tonkin() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Nautical Demarcation Chart of Gulf of Tonkin
    chart = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chart)
    # Parchment chart slate in deep nautical navy
    cdraw.rounded_rectangle([4, 6, 46, 42], radius=4, fill=(20, 65, 120, 255), outline=(235, 195, 45, 255), width=2)
    # Demarcation Boundary Line across Gulf (bright golden dashed line)
    pts_demarc = [(10, 38), (18, 28), (28, 20), (38, 12)]
    for i in range(len(pts_demarc) - 1):
        cdraw.line([pts_demarc[i], pts_demarc[i + 1]], fill=(255, 225, 75, 255), width=2)
    # Bach Long Vi Island marker
    cdraw.ellipse([26, 18, 30, 22], fill=(255, 255, 255, 255), outline=(218, 37, 29, 255))

    # Brass Nautical Compass Divider
    cdraw.line([(25, 8), (16, 32)], fill=(235, 195, 45, 255), width=2)
    cdraw.line([(25, 8), (34, 32)], fill=(235, 195, 45, 255), width=2)
    cdraw.ellipse([23, 6, 27, 10], fill=(255, 235, 95, 255), outline=(130, 90, 15, 255))

    # Lighthouse beam sweeping across calm waters
    cdraw.polygon([(6, 14), (20, 8), (20, 20)], fill=(255, 245, 160, 140))

    canvas.paste(chart, ((TARGET_SIZE[0] - chart.width) // 2, 26), chart)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "gulf_of_tonkin")
    return canvas


# 10. VIE_shared_future: Cầu hữu nghị dây văng hiện đại, cái bắt tay ngoại giao & vầng thái dương
def build_shared_future() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Modern Cable-stayed Friendship Bridge & Diplomatic Handshake
    bridge = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bridge)

    # Rising golden sun behind bridge
    bdraw.ellipse([14, 8, 36, 30], fill=(255, 220, 60, 220))

    # River waters below
    bdraw.chord([4, 28, 46, 44], 0, 180, fill=(35, 100, 175, 255), outline=(235, 195, 45, 255))

    # Cable-stayed bridge towers in gleaming gold
    bdraw.polygon([(24, 6), (28, 28), (22, 28)], fill=(255, 235, 95, 255), outline=(150, 105, 20, 255))
    # Stay cables radiating
    for ox in [-16, -11, -6, 6, 11, 16]:
        bdraw.line([(25, 10), (25 + ox, 30)], fill=(255, 240, 140, 200), width=1)
    # Bridge highway deck
    bdraw.line([(6, 30), (44, 30)], fill=(235, 195, 45, 255), width=3)

    # Diplomatic Handshake Medallion on bridge deck
    med = Image.new("RGBA", (34, 24), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 31, 23], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    # Handshake glyph in gold
    mdraw.polygon([(8, 12), (13, 8), (18, 12), (23, 9), (21, 16), (15, 18), (10, 15)], fill=(255, 230, 80, 255))
    bridge.paste(med, ((50 - med.width) // 2, 22), med)

    canvas.paste(bridge, ((TARGET_SIZE[0] - bridge.width) // 2, 26), bridge)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "shared_future")
    return canvas


# 11. VIE_cambodia_border: Cột mốc Tây Nam VN-Campuchia, máy kinh vĩ trắc địa & phù sa Mê Kông
def build_cambodia_border() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Southwest Border Milestone (Cột Mốc Biên Giới Tây Nam)
    milestone = Image.new("RGBA", (44, 52), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(milestone)
    # Alluvial earth pedestal
    mdraw.polygon([(4, 44), (40, 44), (38, 50), (6, 50)], fill=(110, 115, 120, 255), outline=(60, 65, 70, 255))
    # Beveled granite pillar
    mdraw.polygon([(22, 2), (38, 10), (36, 44), (8, 44), (6, 10)], fill=(210, 215, 220, 255), outline=(90, 95, 100, 255), width=2)
    mdraw.polygon([(22, 2), (38, 10), (36, 44), (22, 44)], fill=(170, 175, 180, 255))
    mdraw.polygon([(22, 2), (6, 10), (8, 44), (22, 44)], fill=(230, 235, 240, 255))

    # Dual boundary plaques: Left Vietnam (red/star), Right Cambodia (blue)
    mdraw.rounded_rectangle([11, 16, 20, 32], radius=1, fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))
    mdraw.rounded_rectangle([23, 16, 32, 32], radius=1, fill=(3, 46, 161, 255), outline=(255, 222, 35, 255))
    s_vn = create_gold_star(6)
    milestone.paste(s_vn, (12, 21), s_vn)

    canvas.paste(milestone, ((TARGET_SIZE[0] - milestone.width) // 2, 26), milestone)

    # Surveyor theodolite on tripod to the right
    theo = Image.new("RGBA", (24, 38), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(theo)
    tdraw.line([(12, 14), (2, 36)], fill=(150, 95, 30, 255), width=2)
    tdraw.line([(12, 14), (12, 37)], fill=(180, 120, 45, 255), width=2)
    tdraw.line([(12, 14), (22, 36)], fill=(120, 75, 20, 255), width=2)
    tdraw.polygon([(6, 10), (18, 8), (17, 14), (5, 16)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    canvas.paste(theo, (TARGET_SIZE[0] - 28, 42), theo)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cambodia_border")
    return canvas


# 12. VIE_funan_techo_response: Sơ đồ âu thuyền kênh đào, thước đo cao trình nước & búa đàm phán
def build_funan_techo_response() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Funan Techo Canal Water Diversion Lock & Diplomatic Water Rights Gavel
    canal = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(canal)

    # Canal Channel in rich river cyan
    cdraw.rounded_rectangle([4, 10, 46, 42], radius=4, fill=(25, 115, 175, 255), outline=(235, 195, 45, 255), width=2)
    # Concrete Lock Gate walls
    cdraw.rectangle([12, 12, 17, 40], fill=(140, 145, 155, 255), outline=(60, 65, 75, 255), width=1)
    cdraw.rectangle([33, 12, 38, 40], fill=(140, 145, 155, 255), outline=(60, 65, 75, 255), width=1)
    # Water flow redirection arrow in gold
    cdraw.polygon([(19, 26), (31, 26), (28, 21), (28, 31)], fill=(255, 235, 80, 255))

    # Water Height Measurement Scale on left wall
    for y in [16, 22, 28, 34]:
        cdraw.line([(14, y), (17, y)], fill=(255, 255, 255, 255), width=1)

    # Diplomatic Gavel of International Water Law resting on top
    cdraw.polygon([(18, 5), (32, 5), (30, 12), (16, 12)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    cdraw.line([(24, 12), (24, 20)], fill=(160, 105, 30, 255), width=3)

    canvas.paste(canal, ((TARGET_SIZE[0] - canal.width) // 2, 26), canal)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "funan_techo_response")
    return canvas


def main():
    print("=" * 60)
    print("REBUILDING CLUSTER 1: 12 REDESIGNED DIPLOMACY FOCUS ICONS")
    print("=" * 60)

    builders = [
        ("border_settlement", build_border_settlement),
        ("special_relations_laos", build_special_relations_laos),
        ("cambodia_relations", build_cambodia_relations),
        ("indochina_solidarity", build_indochina_solidarity),
        ("indochina_federation", build_indochina_federation),
        ("16_words", build_16_words),
        ("border_trade_gates", build_border_trade_gates),
        ("defence_hotline", build_defence_hotline),
        ("gulf_of_tonkin", build_gulf_of_tonkin),
        ("shared_future", build_shared_future),
        ("cambodia_border", build_cambodia_border),
        ("funan_techo_response", build_funan_techo_response),
    ]

    for stem, fn in builders:
        fn()

    print("\nCluster 1 Redesign complete! 12 icons rendered & saved.")


if __name__ == "__main__":
    main()
