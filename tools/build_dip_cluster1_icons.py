"""Script to build Focus Icons for Vietnam Diplomacy & Foreign Affairs (Cluster 1: 12 Focuses)
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
MD_FLAGS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\flags")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")

TARGET_SIZE = (93, 91)

# =========================================================================
# COMMON UTILITIES: DDS SAVER, STARS, LAURELS, FLAGS, SHADOWS
# =========================================================================

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
    print(f"  [SAVED] {stem} -> PNG & DDS (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted 3D shading."""
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
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 248, 125, 170))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(185, 135, 10, 180))
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


def create_golden_laurel_wreath(width: int = 86, height: int = 74) -> Image.Image:
    """Generate high-luster golden laurel wreath with 3D embossed leaves."""
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
            ang = math.pi * 0.55 + t * math.pi * 0.85
            if side == 1:
                ang = math.pi * 0.45 - t * math.pi * 0.85

            px = cx + rx * math.cos(ang)
            py = cy + ry * math.sin(ang)

            tang_x = -rx * math.sin(ang)
            tang_y = ry * math.cos(ang)
            tang_len = math.hypot(tang_x, tang_y) + 1e-5
            tang_x /= tang_len
            tang_y /= tang_len

            leaf_ang = math.atan2(tang_y, tang_x) + (0.45 if side == -1 else -0.45)
            leaf_len = 8.5
            leaf_w = 4.2

            tip_x = px + leaf_len * math.cos(leaf_ang)
            tip_y = py + leaf_len * math.sin(leaf_ang)
            norm_x = -math.sin(leaf_ang) * (leaf_w * 0.5)
            norm_y = math.cos(leaf_ang) * (leaf_w * 0.5)

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
    """Generate soft ambient occlusion drop shadow behind entire composite icon."""
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
    """Safely load and enhance a base MD goal texture."""
    p = MD_GOALS / rel_path
    if not p.exists():
        # Fallback to empty transparent image
        return Image.new("RGBA", target_box, (0, 0, 0, 0))
    im = Image.open(p).convert("RGBA")
    if enhance_color != 1.0:
        im = ImageEnhance.Color(im).enhance(enhance_color)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    im.thumbnail(target_box, Image.Resampling.LANCZOS)
    return im


def create_waving_flag(flag_name: str, size: tuple = (34, 22), border_gold: bool = True) -> Image.Image:
    """Load flag and render as an embossed heraldic waving banner."""
    flag_path = MD_FLAGS / flag_name
    if not flag_path.exists():
        # Fallback plain red flag
        im = Image.new("RGBA", size, (210, 25, 25, 255))
    else:
        im = Image.open(flag_path).convert("RGBA")
        im = im.resize(size, Image.Resampling.LANCZOS)

    # Apply 3D wave shading
    w, h = size
    wave = Image.new("RGBA", size, (0, 0, 0, 0))
    wdraw = ImageDraw.Draw(wave)
    for x in range(w):
        val = int(35 * math.sin(x / w * math.pi * 2.8))
        if val > 0:
            wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
        else:
            wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
    im = Image.alpha_composite(im, wave)

    if border_gold:
        bdraw = ImageDraw.Draw(im)
        bdraw.rectangle([0, 0, w - 1, h - 1], outline=(220, 180, 45, 240), width=1)

    return im


# =========================================================================
# 12 CLUSTER 1 ICON BUILDERS
# =========================================================================

# 1. VIE_border_settlement: Hoàn tất Phân giới Cắm mốc Biên giới
def build_border_settlement() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base border milestone and treaty map
    base = load_md_goal("00_diplomacy/treaty2.dds", target_box=(80, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels framing the border achievement
    laurel = create_golden_laurel_wreath(84, 72)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 11), laurel)

    # Granite border landmark monument (Cột mốc biên giới chính quy)
    mon = Image.new("RGBA", (32, 44), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mon)
    # Beveled granite pillar in stone-gray with gold accents
    mdraw.polygon([(16, 2), (28, 8), (28, 38), (4, 38), (4, 8)], fill=(185, 190, 195, 255), outline=(90, 95, 100, 255), width=2)
    # Shading facets
    mdraw.polygon([(16, 2), (28, 8), (28, 38), (16, 41), (16, 2)], fill=(160, 165, 170, 255))
    mdraw.polygon([(16, 2), (4, 8), (4, 38), (16, 41), (16, 2)], fill=(210, 215, 220, 255))
    # Red national emblem plate on pillar
    mdraw.rounded_rectangle([9, 13, 23, 27], radius=2, fill=(215, 25, 25, 255), outline=(245, 215, 50, 255), width=1)
    s_mon = create_gold_star(9)
    mon.paste(s_mon, (11, 15), s_mon)
    # Milestone base pedestal
    mdraw.rectangle([2, 38, 30, 43], fill=(120, 125, 130, 255), outline=(70, 75, 80, 255))
    canvas.paste(mon, ((TARGET_SIZE[0] - mon.width) // 2, 30), mon)

    # Top golden star of sovereignty
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "border_settlement")
    return canvas


# 2. VIE_special_relations_laos: Quan hệ đặc biệt với Lào
def build_special_relations_laos() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base diplomatic conference / friendship halo
    base = load_md_goal("00_diplomacy/diplomacy.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags of Vietnam and Laos
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_lao = create_waving_flag("LAO_communism.tga", size=(34, 23))

    # Rotate flags slightly outward
    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_lao_rot = f_lao.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_lao_rot, (TARGET_SIZE[0] - 11 - f_lao_rot.width, 26), f_lao_rot)

    # Center golden handshake badge over Truong Son mountain silhouette
    center_badge = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(center_badge)
    cdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.ellipse([5, 4, 28, 26], fill=(200, 25, 25, 255), outline=(255, 235, 95, 255), width=1)
    # Gold handshake glyph
    cdraw.polygon([(9, 15), (14, 11), (20, 15), (25, 12), (22, 19), (16, 21), (11, 18)], fill=(255, 230, 80, 255))
    canvas.paste(center_badge, ((TARGET_SIZE[0] - center_badge.width) // 2, 46), center_badge)

    # Top gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "special_relations_laos")
    return canvas


# 3. VIE_cambodia_relations: Quan hệ với Campuchia
def build_cambodia_relations() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_cambodia.dds", target_box=(80, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and Cambodia
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_cam = create_waving_flag("CAM_neutrality.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_cam_rot = f_cam.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_cam_rot, (TARGET_SIZE[0] - 11 - f_cam_rot.width, 26), f_cam_rot)

    # Friendship medallion with lotus and Angkor silhouette
    med = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 28, 26], fill=(25, 60, 145, 255), outline=(255, 235, 95, 255), width=1)
    # Gold handshake / Angkor emblem
    mdraw.polygon([(10, 16), (15, 12), (19, 16), (24, 13), (22, 20), (16, 21), (11, 19)], fill=(255, 230, 80, 255))
    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 46), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cambodia_relations")
    return canvas


# 4. VIE_indochina_solidarity: Đoàn kết Đông Dương
def build_indochina_solidarity() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base tripartite alliance
    base = load_md_goal("00_alliance/alliance.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Tripartite Heraldic Shield (Vietnam, Laos, Cambodia)
    shield = Image.new("RGBA", (44, 46), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shield)
    # Shield shape
    pts = [(22, 3), (41, 10), (37, 34), (22, 44), (7, 34), (3, 10)]
    sdraw.polygon(pts, fill=(225, 185, 40, 255), outline=(130, 90, 15, 255), width=2)
    # Inside tri-partition: Left Laos (blue/red), Center Vietnam (red/star), Right Cambodia (blue/red)
    sdraw.polygon([(22, 6), (38, 12), (34, 32), (22, 41)], fill=(20, 60, 150, 255))
    sdraw.polygon([(22, 6), (6, 12), (10, 32), (22, 41)], fill=(200, 25, 25, 255))
    # Center crimson core
    sdraw.polygon([(22, 6), (29, 14), (27, 35), (22, 41), (17, 35), (15, 14)], fill=(220, 25, 25, 255), outline=(255, 225, 75, 255))

    s_star = create_gold_star(14)
    shield.paste(s_star, (15, 16), s_star)
    canvas.paste(shield, ((TARGET_SIZE[0] - shield.width) // 2, 28), shield)

    # Flaming golden torch of solidarity
    torch = create_gold_star_with_glow(22)
    canvas.paste(torch, ((TARGET_SIZE[0] - torch.width) // 2, -1), torch)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "indochina_solidarity")
    return canvas


# 5. VIE_indochina_federation: Liên bang Đông Dương
def build_indochina_federation() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base grand federation crest
    base = load_md_goal("00_alliance/major_alliance.dds", target_box=(84, 70), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Grand golden federation crest with 3 radiant stars
    fed_box = Image.new("RGBA", (48, 44), (0, 0, 0, 0))
    fdraw = ImageDraw.Draw(fed_box)
    # Imperial eagle wings / radiant mantle behind
    fdraw.polygon([(24, 2), (46, 12), (40, 36), (24, 42), (8, 36), (2, 12)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    fdraw.polygon([(24, 5), (42, 14), (37, 34), (24, 39), (11, 34), (6, 14)], fill=(180, 20, 20, 255), outline=(255, 225, 75, 255), width=1)

    # 3 Gold stars in triangle
    s_top = create_gold_star(12)
    s_l = create_gold_star(9)
    s_r = create_gold_star(9)
    fed_box.paste(s_top, (18, 9), s_top)
    fed_box.paste(s_l, (11, 23), s_l)
    fed_box.paste(s_r, (28, 23), s_r)

    canvas.paste(fed_box, ((TARGET_SIZE[0] - fed_box.width) // 2, 28), fed_box)

    # Radiant capstone star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "indochina_federation")
    return canvas


# 6. VIE_16_words: Phương châm 16 chữ và tinh thần 4 tốt
def build_16_words() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_align/blr_china_friendship.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Golden diplomatic scroll with imperial seal
    scroll = Image.new("RGBA", (44, 38), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scroll)
    # Scroll rolled paper in parchment ivory with gold borders
    sdraw.rounded_rectangle([4, 6, 39, 32], radius=3, fill=(245, 240, 215, 255), outline=(190, 145, 30, 255), width=2)
    # Scroll roller rods at left & right
    sdraw.rectangle([2, 4, 6, 34], fill=(215, 175, 45, 255), outline=(130, 90, 15, 255))
    sdraw.rectangle([37, 4, 41, 34], fill=(215, 175, 45, 255), outline=(130, 90, 15, 255))
    # Calligraphic 16 words text lines representation
    for y in [11, 16, 21, 26]:
        sdraw.line([(10, y), (33, y)], fill=(180, 25, 25, 255), width=2)
    # Imperial red wax seal at center
    sdraw.ellipse([16, 13, 27, 24], fill=(205, 20, 20, 255), outline=(255, 225, 60, 255), width=1)
    s_seal = create_gold_star(6)
    scroll.paste(s_seal, (18, 15), s_seal)

    canvas.paste(scroll, ((TARGET_SIZE[0] - scroll.width) // 2, 34), scroll)

    # Top golden star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "16_words")
    return canvas


# 7. VIE_border_trade_gates: Cửa khẩu thương mại biên giới
def build_border_trade_gates() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/ExpandTrade.dds", target_box=(82, 68), enhance_color=1.25)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Monumental International Border Gate Archway (Hữu Nghị Quan architecture)
    gate = Image.new("RGBA", (46, 40), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gate)
    # Stone arch walls in granite-ochre
    gdraw.polygon([(4, 38), (4, 14), (23, 8), (42, 14), (42, 38), (34, 38), (34, 22), (12, 22), (12, 38)],
                  fill=(210, 180, 120, 255), outline=(110, 80, 40, 255), width=2)
    # Pagoda tiled roof tiers
    gdraw.polygon([(0, 16), (23, 6), (46, 16), (23, 11)], fill=(185, 45, 30, 255), outline=(100, 20, 15, 255))
    gdraw.polygon([(6, 10), (23, 2), (40, 10), (23, 6)], fill=(205, 55, 35, 255), outline=(100, 20, 15, 255))
    # Center passage archway
    gdraw.rectangle([14, 22, 32, 38], fill=(35, 40, 50, 255), outline=(215, 175, 45, 255))
    # Red star plate on gate forehead
    gdraw.rectangle([18, 12, 28, 18], fill=(210, 25, 25, 255), outline=(245, 215, 50, 255))
    s_gate = create_gold_star(5)
    gate.paste(s_gate, (20, 13), s_gate)

    canvas.paste(gate, ((TARGET_SIZE[0] - gate.width) // 2, 32), gate)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "border_trade_gates")
    return canvas


# 8. VIE_defence_hotline: Đường dây nóng quốc phòng và tránh va chạm
def build_defence_hotline() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_diplomacy/peace.dds", target_box=(82, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crimson Direct Defense Hotline Telephone with radio pulse waves
    phone = Image.new("RGBA", (44, 38), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(phone)
    # Phone console base in defense scarlet
    pdraw.rounded_rectangle([6, 14, 38, 36], radius=4, fill=(190, 25, 25, 255), outline=(110, 15, 15, 255), width=2)
    # Keypad / rotary gold circle
    pdraw.ellipse([16, 20, 28, 32], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    # Telephone handset resting on cradle
    pdraw.rounded_rectangle([2, 6, 42, 14], radius=3, fill=(160, 20, 20, 255), outline=(90, 10, 10, 255), width=2)
    pdraw.rounded_rectangle([0, 3, 10, 17], radius=3, fill=(210, 30, 30, 255), outline=(110, 15, 15, 255))
    pdraw.rounded_rectangle([34, 3, 44, 17], radius=3, fill=(210, 30, 30, 255), outline=(110, 15, 15, 255))

    # Star on phone dial
    s_phone = create_gold_star(7)
    phone.paste(s_phone, (19, 23), s_phone)

    canvas.paste(phone, ((TARGET_SIZE[0] - phone.width) // 2, 34), phone)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "defence_hotline")
    return canvas


# 9. VIE_gulf_of_tonkin: Phân định Vịnh Bắc Bộ
def build_gulf_of_tonkin() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_diplomacy/treaty.dds", target_box=(82, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Nautical Chart & Maritime Compass of Gulf of Tonkin
    chart = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chart)
    # Sea chart slate in deep nautical navy
    cdraw.rounded_rectangle([4, 6, 40, 36], radius=3, fill=(25, 75, 130, 255), outline=(215, 175, 45, 255), width=2)
    # Demarcation line across gulf (dashed gold line)
    cdraw.line([(8, 30), (22, 20), (36, 12)], fill=(255, 230, 80, 255), width=2)
    # Islands representation (Bach Long Vi)
    cdraw.ellipse([21, 19, 24, 22], fill=(255, 255, 255, 255))
    # Brass nautical compass divider
    cdraw.line([(22, 8), (14, 28)], fill=(235, 195, 45, 255), width=2)
    cdraw.line([(22, 8), (30, 28)], fill=(235, 195, 45, 255), width=2)
    cdraw.ellipse([20, 6, 24, 10], fill=(255, 235, 95, 255), outline=(130, 90, 15, 255))

    canvas.paste(chart, ((TARGET_SIZE[0] - chart.width) // 2, 32), chart)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "gulf_of_tonkin")
    return canvas


# 10. VIE_shared_future: Cộng đồng chia sẻ tương lai
def build_shared_future() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_economy/strait_messina_bridge.dds", target_box=(82, 68), enhance_color=1.3)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_diplomacy/accept_treaty.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Shared Future Bridge & Handshake Medallion
    med = Image.new("RGBA", (42, 38), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 39, 36], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 36, 33], fill=(195, 25, 25, 255), outline=(255, 235, 95, 255), width=1)
    # Cable stayed bridge towers in gold
    mdraw.polygon([(21, 6), (25, 26), (17, 26)], fill=(255, 235, 95, 255))
    # Golden bridge stay cables
    for ox in [-12, -7, 7, 12]:
        mdraw.line([(21, 9), (21 + ox, 26)], fill=(255, 220, 60, 200), width=1)
    # Handshake silhouette
    mdraw.polygon([(11, 23), (16, 19), (21, 23), (26, 20), (29, 25), (21, 28), (13, 26)], fill=(255, 240, 120, 255))

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 34), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "shared_future")
    return canvas


# 11. VIE_cambodia_border: Phân giới cắm mốc biên giới với Campuchia
def build_cambodia_border() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_army/Generic_Redraw_Borders.dds", target_box=(82, 68), enhance_color=1.2)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_diplomacy/treaty2.dds", target_box=(82, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Southwest border milestone post with surveyor theodolite
    mon = Image.new("RGBA", (34, 44), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mon)
    # Granite milestone pillar
    mdraw.polygon([(17, 2), (29, 8), (29, 38), (5, 38), (5, 8)], fill=(175, 180, 185, 255), outline=(80, 85, 90, 255), width=2)
    mdraw.polygon([(17, 2), (29, 8), (29, 38), (17, 41), (17, 2)], fill=(150, 155, 160, 255))
    mdraw.polygon([(17, 2), (5, 8), (5, 38), (17, 41), (17, 2)], fill=(205, 210, 215, 255))
    # Bilateral milestone marker plaque (red VN, blue KH)
    mdraw.rounded_rectangle([(9, 13), (16, 27)], radius=1, fill=(215, 25, 25, 255), outline=(245, 215, 50, 255))
    mdraw.rounded_rectangle([(18, 13), (25, 27)], radius=1, fill=(25, 65, 155, 255), outline=(245, 215, 50, 255))
    s_mon = create_gold_star(6)
    mon.paste(s_mon, (10, 17), s_mon)

    canvas.paste(mon, ((TARGET_SIZE[0] - mon.width) // 2, 30), mon)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cambodia_border")
    return canvas


# 12. VIE_funan_techo_response: Ứng phó kênh đào Phù Nam Techo
def build_funan_techo_response() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("egypt/suez_canal_project.dds", target_box=(82, 68), enhance_color=1.3)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_economy/economic_water_supply.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Water lock canal gate diagram & diplomatic balancing scales
    canal_ui = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(canal_ui)
    # Canal waterway channel in river cyan
    cdraw.rounded_rectangle([4, 10, 40, 36], radius=3, fill=(35, 115, 175, 255), outline=(215, 175, 45, 255), width=2)
    # Lock gates
    cdraw.rectangle([10, 12, 14, 34], fill=(130, 135, 140, 255), outline=(60, 65, 70, 255))
    cdraw.rectangle([30, 12, 34, 34], fill=(130, 135, 140, 255), outline=(60, 65, 70, 255))
    # Flow direction arrows
    cdraw.polygon([(17, 23), (27, 23), (25, 19), (25, 27)], fill=(255, 240, 80, 255))
    # Diplomatic gavel / scale of water rights on top
    cdraw.rectangle([18, 5, 26, 9], fill=(215, 160, 40, 255), outline=(110, 70, 15, 255))
    cdraw.line([(22, 9), (22, 15)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(canal_ui, ((TARGET_SIZE[0] - canal_ui.width) // 2, 32), canal_ui)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "funan_techo_response")
    return canvas


def main():
    print("=" * 60)
    print("BUILDING CLUSTER 1: 12 DIPLOMACY FOCUS ICONS")
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

    print("\nCluster 1 complete! 12 icons rendered & saved.")


if __name__ == "__main__":
    main()
