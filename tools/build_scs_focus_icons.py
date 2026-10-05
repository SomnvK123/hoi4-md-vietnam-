"""Script to build Focus Icons for Vietnam South China Sea / Maritime Sovereignty
(Nhánh Biển Đông - 13 focuses) in Millennium Dawn.

13 Focuses:
1.  scs_law_of_the_sea: Luật Biển Việt Nam 2012 (Naval treaty document, golden anchor seal, scroll, faceted gold star)
2.  scs_assert_maritime_rights: Khẳng định Chủ quyền Biển đảo (Maritime shield, Vietnam star on red crest, ocean waves, lighthouse searchlight)
3.  scs_legal_warfare: Đấu tranh Pháp lý Quốc tế / UNCLOS (ITLOS / ICC international court gavel, legal dossier, balance scales)
4.  scs_dk1_platforms: Các Nhà giàn DK1 (Offshore DK1 steel jacket stilt platform, helipad, waving Vietnamese flag, radar dome)
5.  scs_spratly_fortification: Củng cố Tiền đồn Trường Sa (Concrete island fort, tetrapod breakwaters, sovereign milestone with gold star)
6.  scs_paracel_ultimatum: Thu hồi Quần đảo Hoàng Sa (Paracel chart, dual naval cannon barrels, sovereign red banner with gold star)
7.  scs_maritime_militia: Hải đội Dân quân Tự vệ Biển (Steel hull fishing trawler, Vietnamese flag, crossed rifles, militia badge)
8.  scs_fisheries_surveillance: Lực lượng Kiểm ngư (Kiểm ngư KN-781 white vessel, green/blue stripes, water cannon jet, Kiểm ngư badge)
9.  scs_coast_guard_law: Luật Cảnh sát Biển (Vietnam Coast Guard CSB 8020 cutter, red/blue racing stripes, gold CG shield, laurels)
10. scs_cam_ranh_port: Cảng Quốc tế Cam Ranh (Cam Ranh deepwater piers, gantry crane, Gepard frigate & Kilo submarine moored)
11. scs_maritime_cooperation: Hợp tác An ninh Biển (Diplomatic golden handshake, compass rose, ASEAN sheaf of rice with marine rope)
12. scs_joint_training: Huấn luyện Chung trên Biển (Guided missile frigate in tactical echelon, shipborne helicopter hovering)
13. scs_multilateral_exercise: Diễn tập An ninh Hàng hải Đa phương (Naval battleline fleet, tactical radar HUD, golden trident & laurels)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, exactly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
"""

import math
import re
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
GFX_FILE = ROOT / "interface" / "VIE_md_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")

TARGET_SIZE = (93, 91)

# =========================================================================
# UTILITIES: DDS & PNG SAVER, SHADOWS, HERALDRY
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

    draw.polygon(pts, fill=(255, 220, 20, 255), outline=(170, 130, 15, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 245, 110, 160))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 140, 10, 170))
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


def create_vpa_cockade(size: int = 24, naval: bool = False) -> Image.Image:
    """Generate official VPA or Naval roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(130, 95, 20, 255))
    if naval:
        r_mid = r_outer - 1.5
        draw.ellipse((cx - r_mid, cy - r_mid, cx + r_mid, cy + r_mid), fill=(15, 45, 105, 255), outline=(10, 25, 60, 255))
        r_inner = r_mid - 2.5
        draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))
    else:
        r_inner = r_outer - 2.0
        draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_vietnam_flag(w: int = 26, h: int = 17, waving: bool = True) -> Image.Image:
    """Generate a high-fidelity Vietnamese national flag with golden star."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], fill=(215, 25, 25, 255), outline=(140, 15, 15, 255))
    star = create_gold_star(int(h * 0.65))
    im.paste(star, (int((w - star.width) / 2), int((h - star.height) / 2)), star)
    if waving:
        # Subtle light ripple
        for x in range(w):
            alpha_wave = int(math.sin(x / 3.0) * 35)
            if alpha_wave > 0:
                draw.line([(x, 0), (x, h - 1)], fill=(255, 255, 255, alpha_wave))
            elif alpha_wave < 0:
                draw.line([(x, 0), (x, h - 1)], fill=(0, 0, 0, abs(alpha_wave)))
    return im


def apply_ambient_drop_shadow(canvas: Image.Image, radius: float = 1.8) -> Image.Image:
    """Generate soft ambient occlusion drop shadow behind entire composite icon."""
    out = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow.paste(canvas, (0, 1), canvas)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(radius))
    # Soft multiplier
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.8))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))
    out.paste(shadow, (0, 0), shadow)
    out.paste(canvas, (0, 0), canvas)
    return out


# =========================================================================
# 13 BUILDER FUNCTIONS FOR BIỂN ĐÔNG (SCS)
# =========================================================================

# 1. VIE_law_of_the_sea
def build_scs_law_of_the_sea() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "Generic_Naval_Treaty.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 73), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 3D Gold Star at apex
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Golden Scales of Maritime Justice on the treaty scroll
    draw = ImageDraw.Draw(canvas)
    draw.line([(46, 32), (46, 44)], fill=(255, 225, 50, 255), width=2)
    draw.line([(38, 35), (54, 35)], fill=(255, 225, 50, 255), width=2)
    draw.polygon([(34, 42), (42, 42), (38, 38)], fill=(240, 200, 40, 255), outline=(160, 120, 15, 255))
    draw.polygon([(50, 42), (58, 42), (54, 38)], fill=(240, 200, 40, 255), outline=(160, 120, 15, 255))

    # Bottom VPA cockade pinning the treaty ribbon
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_law_of_the_sea")
    return canvas


# 2. VIE_assert_maritime_rights
def build_scs_assert_maritime_rights() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_regions" / "focus_GER_northern_shield.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Central crimson heart shield with golden star
    draw = ImageDraw.Draw(canvas)
    pts_shield = [(36, 30), (56, 30), (56, 46), (46, 56), (36, 46)]
    draw.polygon(pts_shield, fill=(195, 25, 25, 255), outline=(235, 195, 45, 255), width=2)
    star_center = create_gold_star(16)
    canvas.paste(star_center, ((TARGET_SIZE[0] - star_center.width) // 2, 34), star_center)

    # Top faceted gold star
    star_top = create_gold_star_with_glow(20)
    canvas.paste(star_top, ((TARGET_SIZE[0] - star_top.width) // 2, -1), star_top)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_assert_maritime_rights")
    return canvas


# 3. VIE_legal_warfare
def build_scs_legal_warfare() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "israel_palestine" / "icc_justice_court.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 73), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # UN blue radiant halo behind gavel
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((46 - 22, 36 - 15, 46 + 22, 36 + 15), outline=(60, 160, 240, 120), width=2)

    # Top gold star
    star = create_gold_star_with_glow(19)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    # Bottom official seal with VPA cockade
    cockade = create_vpa_cockade(16, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_legal_warfare")
    return canvas


# 4. VIE_dk1_platforms
def build_scs_dk1_platforms() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_energy_resources" / "north_sea_oilrig.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((82, 74), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Waving Vietnamese national flag on top helipad mast
    flag = create_vietnam_flag(24, 15, waving=True)
    canvas.paste(flag, (48, 14), flag)

    # Top faceted gold star
    star = create_gold_star_with_glow(19)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom naval anchor insignia
    anchor_p = MD_GOALS / "00_navy" / "amphibious_assault.dds"
    if anchor_p.exists():
        anchor_im = Image.open(anchor_p).convert("RGBA")
        anchor_sub = anchor_im.crop((32, 40, 60, 68)).resize((22, 22), Image.Resampling.LANCZOS)
        canvas.paste(anchor_sub, ((TARGET_SIZE[0] - anchor_sub.width) // 2, 66), anchor_sub)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_dk1_platforms")
    return canvas


# 5. VIE_spratly_fortification
def build_scs_spratly_fortification() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "coastal_fort.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((80, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Sovereign stone milestone obelisk on left bastion
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(22, 42), (30, 42), (29, 64), (23, 64)], fill=(210, 215, 225, 255), outline=(130, 140, 155, 255))
    draw.rectangle([24, 46, 28, 54], fill=(200, 25, 25, 255))
    draw.polygon([(26, 48), (27, 51), (25, 51)], fill=(255, 225, 30, 255))

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom laurel branch accents
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_spratly_fortification")
    return canvas


# 6. VIE_paracel_ultimatum
def build_scs_paracel_ultimatum() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "iran" / "iran_commie_knife.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Dual heavy naval cannon barrels trained forward (3D metallic)
    draw = ImageDraw.Draw(canvas)
    # Left cannon barrel
    draw.polygon([(28, 52), (14, 28), (17, 26), (31, 50)], fill=(160, 175, 190, 255), outline=(90, 100, 115, 255))
    draw.ellipse((13, 25, 18, 29), fill=(50, 60, 70, 255), outline=(120, 130, 145, 255))
    # Right cannon barrel
    draw.polygon([(64, 52), (78, 28), (75, 26), (61, 50)], fill=(160, 175, 190, 255), outline=(90, 100, 115, 255))
    draw.ellipse((74, 25, 79, 29), fill=(50, 60, 70, 255), outline=(120, 130, 145, 255))

    # Sovereign red banner with gold star
    flag = create_vietnam_flag(26, 16, waving=True)
    canvas.paste(flag, ((TARGET_SIZE[0] - flag.width) // 2, 42), flag)

    # Top faceted gold star
    star = create_gold_star_with_glow(21)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_paracel_ultimatum")
    return canvas


# 7. VIE_maritime_militia
def build_scs_maritime_militia() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "focus_SIA_river_patrols.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 75), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Tàu cá vỏ thép: Blue hull overlay with red waterline
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(30, 52), (64, 52), (60, 60), (34, 60)], fill=(25, 75, 145, 220), outline=(15, 45, 90, 255))
    draw.line([(34, 60), (60, 60)], fill=(210, 30, 30, 255), width=2)

    # Vietnamese flag fluttering on wheelhouse mast
    flag = create_vietnam_flag(22, 14, waving=True)
    canvas.paste(flag, (44, 25), flag)

    # Crossed rifles behind mast
    draw.line([(24, 38), (42, 24)], fill=(50, 45, 40, 255), width=2)
    draw.line([(68, 38), (50, 24)], fill=(50, 45, 40, 255), width=2)

    # Top faceted gold star
    star = create_gold_star_with_glow(19)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Militia cockade at bottom
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_maritime_militia")
    return canvas


# 8. VIE_fisheries_surveillance
def build_scs_fisheries_surveillance() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "comoros" / "Comorean_Coast_Guard_1.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Vietnam Fisheries Surveillance (Kiểm ngư Việt Nam) Livery:
    # White cutter hull with green & blue diagonal racing stripes
    draw = ImageDraw.Draw(canvas)
    # Diagonal green & blue stripes
    draw.polygon([(46, 44), (52, 44), (44, 62), (38, 62)], fill=(20, 145, 65, 235))
    draw.polygon([(53, 44), (59, 44), (51, 62), (45, 62)], fill=(20, 85, 175, 235))

    # High pressure water cannon stream spraying forward
    draw.arc([16, 26, 48, 52], start=180, end=330, fill=(160, 235, 255, 220), width=3)
    draw.arc([14, 28, 46, 54], start=180, end=320, fill=(240, 250, 255, 180), width=2)

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Official Kiểm ngư golden badge (Fish + Anchor + Star roundel)
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_fisheries_surveillance")
    return canvas


# 9. VIE_coast_guard_law
def build_scs_coast_guard_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "comoros" / "Comorean_Coast_Guard_1.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Vietnam Coast Guard (Cảnh sát biển Việt Nam) Livery:
    # Iconic Red & Blue diagonal racing stripes on white prow
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(46, 44), (52, 44), (44, 62), (38, 62)], fill=(205, 30, 30, 240))
    draw.polygon([(53, 44), (59, 44), (51, 62), (45, 62)], fill=(20, 55, 155, 240))

    # Golden Coast Guard shield with star and anchor
    pts_cg = [(40, 48), (53, 48), (53, 60), (46, 66), (40, 60)]
    draw.polygon(pts_cg, fill=(235, 195, 45, 255), outline=(140, 100, 15, 255), width=1)
    cg_star = create_gold_star(10)
    canvas.paste(cg_star, (41, 51), cg_star)

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom Coast Guard cockade
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_coast_guard_law")
    return canvas


# 10. VIE_scs_cam_ranh_port
def build_scs_cam_ranh_port() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "civitavecchia_port.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Modern Kilo 636 submarine hull silhouette moored at pier
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(26, 56), (46, 56), (48, 62), (24, 62)], fill=(35, 40, 48, 255), outline=(65, 75, 88, 255))
    draw.rectangle([34, 52, 38, 56], fill=(30, 35, 42, 255), outline=(65, 75, 88, 255))

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom golden anchor
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_cam_ranh_port")
    return canvas


# 11. VIE_scs_maritime_cooperation
def build_scs_maritime_cooperation() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_trade" / "trade_with_asean.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Central golden handshake & maritime compass ring
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((46 - 15, 38 - 15, 46 + 15, 38 + 15), outline=(235, 195, 45, 160), width=1)

    # Bottom ASEAN ribbon cockade
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_maritime_cooperation")
    return canvas


# 12. VIE_scs_joint_training
def build_scs_joint_training() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "frigates.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.10)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Patrol helicopter hovering above warship flight deck
    draw = ImageDraw.Draw(canvas)
    # Rotor blade
    draw.line([(54, 20), (74, 20)], fill=(45, 55, 65, 230), width=2)
    # Heli fuselage
    draw.ellipse((60, 20, 68, 25), fill=(70, 85, 100, 255), outline=(40, 50, 60, 255))
    draw.line([(68, 22), (73, 21)], fill=(70, 85, 100, 255), width=2)

    # Tactical sonar / radar pulse rings
    draw.arc([20, 36, 48, 64], start=210, end=330, fill=(70, 210, 255, 160), width=1)
    draw.arc([16, 32, 52, 68], start=210, end=330, fill=(70, 210, 255, 120), width=1)

    # Top faceted gold star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom naval cockade
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_joint_training")
    return canvas


# 13. VIE_scs_multilateral_exercise
def build_scs_multilateral_exercise() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_regions" / "focus_generic_baltic_sea_fleet.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Tactical combat radar HUD overlay (Cyan crosshair and bearing circle)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 42
    draw.ellipse((cx - 24, cy - 24, cx + 24, cy + 24), outline=(40, 220, 255, 110), width=1)
    draw.line([(cx - 28, cy), (cx - 20, cy)], fill=(40, 220, 255, 160), width=1)
    draw.line([(cx + 20, cy), (cx + 28, cy)], fill=(40, 220, 255, 160), width=1)
    draw.line([(cx, cy - 28), (cx, cy - 20)], fill=(40, 220, 255, 160), width=1)
    draw.line([(cx, cy + 20), (cx, cy + 28)], fill=(40, 220, 255, 160), width=1)

    # Golden naval trident at center
    draw.line([(cx, 32), (cx, 48)], fill=(245, 210, 45, 255), width=2)
    draw.line([(cx - 7, 34), (cx + 7, 34)], fill=(245, 210, 45, 255), width=2)
    draw.line([(cx - 7, 30), (cx - 7, 34)], fill=(245, 210, 45, 255), width=2)
    draw.line([(cx + 7, 30), (cx + 7, 34)], fill=(245, 210, 45, 255), width=2)

    # Top faceted gold star
    star = create_gold_star_with_glow(21)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    # Bottom naval cockade
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "scs_multilateral_exercise")
    return canvas


# =========================================================================
# REGISTRATION & IN-TREE INTEGRATION
# =========================================================================

FOCUS_MAP = {
    "VIE_law_of_the_sea": "scs_law_of_the_sea",
    "VIE_assert_maritime_rights": "scs_assert_maritime_rights",
    "VIE_legal_warfare": "scs_legal_warfare",
    "VIE_dk1_platforms": "scs_dk1_platforms",
    "VIE_spratly_fortification": "scs_spratly_fortification",
    "VIE_paracel_ultimatum": "scs_paracel_ultimatum",
    "VIE_maritime_militia": "scs_maritime_militia",
    "VIE_fisheries_surveillance": "scs_fisheries_surveillance",
    "VIE_coast_guard_law": "scs_coast_guard_law",
    "VIE_scs_cam_ranh_port": "scs_cam_ranh_port",
    "VIE_scs_maritime_cooperation": "scs_maritime_cooperation",
    "VIE_scs_joint_training": "scs_joint_training",
    "VIE_scs_multilateral_exercise": "scs_multilateral_exercise",
}


def register_sprites():
    """Register spriteTypes in interface/VIE_md_focus_icons.gfx."""
    gfx_txt = GFX_FILE.read_text(encoding="utf-8")
    new_entries = []
    for fid, stem in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        if sprite_name not in gfx_txt:
            entry = f"\tspriteType = {{\n\t\tname = \"{sprite_name}\"\n\t\ttexturefile = \"gfx/interface/goals/{stem}.dds\"\n\t}}"
            new_entries.append(entry)

    if new_entries:
        last_brace_idx = gfx_txt.rfind("}")
        updated_gfx = gfx_txt[:last_brace_idx] + "\n".join(new_entries) + "\n}\n"
        GFX_FILE.write_text(updated_gfx, encoding="utf-8")
        print(f"Registered {len(new_entries)} new spriteTypes in {GFX_FILE.name}")
    else:
        print("All spriteTypes already registered.")


def update_focus_tree():
    """Update icon references in common/national_focus/VIE_md_focus.txt."""
    tree_txt = FOCUS_FILE.read_text(encoding="utf-8")
    updated_count = 0
    for fid, stem in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        pattern = re.compile(rf"(id\s*=\s*{re.escape(fid)}\s*\n\s*icon\s*=\s*)(\S+)")
        m = pattern.search(tree_txt)
        if m and m.group(2) != sprite_name:
            tree_txt = pattern.sub(rf"\g<1>{sprite_name}", tree_txt)
            updated_count += 1
            print(f"  Updated {fid} -> icon = {sprite_name}")

    if updated_count > 0:
        FOCUS_FILE.write_text(tree_txt, encoding="utf-8")
        print(f"Updated {updated_count} focus icons in {FOCUS_FILE.name}")
    else:
        print("All focus icons already up to date.")


def create_showcase_artifact(icons: dict[str, Image.Image]):
    """Create a contact sheet showcase image of all 13 South China Sea focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "south_china_sea_icons_showcase.png"

    # Layout: 4 columns x 4 rows
    cols = 4
    rows = (len(icons) + cols - 1) // cols
    card_w, card_h = 195, 145
    pad_x, pad_y = 20, 20
    header_h = 90

    total_w = pad_x * 2 + cols * card_w + (cols - 1) * 15
    total_h = header_h + rows * card_h + (rows - 1) * 15 + pad_y

    canvas = Image.new("RGBA", (total_w, total_h), (14, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)

    # Header font
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_id = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_name = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_title = font_sub = font_id = font_name = None

    draw.text((pad_x, 20), "BỘ ICON GFX BIỂN ĐÔNG & CHỦ QUYỀN HÀNG HẢI (SOUTH CHINA SEA)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "13 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "scs_law_of_the_sea": "Luật Biển Việt Nam",
        "scs_assert_maritime_rights": "Khẳng định Chủ quyền",
        "scs_legal_warfare": "Đấu tranh Pháp lý UNCLOS",
        "scs_dk1_platforms": "Các Nhà giàn DK1",
        "scs_spratly_fortification": "Củng cố Tiền đồn Trường Sa",
        "scs_paracel_ultimatum": "Thu hồi Quần đảo Hoàng Sa",
        "scs_maritime_militia": "Hải đội Dân quân Biển",
        "scs_fisheries_surveillance": "Lực lượng Kiểm ngư",
        "scs_coast_guard_law": "Luật Cảnh sát Biển",
        "scs_cam_ranh_port": "Cảng Quốc tế Cam Ranh",
        "scs_maritime_cooperation": "Hợp tác An ninh Biển",
        "scs_joint_training": "Huấn luyện Chung trên Biển",
        "scs_multilateral_exercise": "Diễn tập Hàng hải Đa phương",
    }

    for idx, (stem, img) in enumerate(icons.items()):
        c = idx % cols
        r = idx // cols
        x = pad_x + c * (card_w + 15)
        y = header_h + r * (card_h + 15)

        # Draw card container
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill=(22, 28, 38, 255), outline=(45, 60, 80, 255))

        # Paste icon (centered horizontally in top portion of card)
        icon_x = x + (card_w - img.width) // 2
        icon_y = y + 10
        canvas.paste(img, (icon_x, icon_y), img)

        # Text labels
        t_title = focus_titles.get(stem, stem)
        draw.text((x + 10, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 10, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    canvas.save(out_path)
    print(f"Showcase image saved: {out_path}")


def main():
    print("=" * 65)
    print("BUILDING 13 SOUTH CHINA SEA FOCUS ICONS (PAINTERLY 3D MD STYLE)")
    print("=" * 65)

    built_icons = {}
    built_icons["scs_law_of_the_sea"] = build_scs_law_of_the_sea()
    built_icons["scs_assert_maritime_rights"] = build_scs_assert_maritime_rights()
    built_icons["scs_legal_warfare"] = build_scs_legal_warfare()
    built_icons["scs_dk1_platforms"] = build_scs_dk1_platforms()
    built_icons["scs_spratly_fortification"] = build_scs_spratly_fortification()
    built_icons["scs_paracel_ultimatum"] = build_scs_paracel_ultimatum()
    built_icons["scs_maritime_militia"] = build_scs_maritime_militia()
    built_icons["scs_fisheries_surveillance"] = build_scs_fisheries_surveillance()
    built_icons["scs_coast_guard_law"] = build_scs_coast_guard_law()
    built_icons["scs_cam_ranh_port"] = build_scs_cam_ranh_port()
    built_icons["scs_maritime_cooperation"] = build_scs_maritime_cooperation()
    built_icons["scs_joint_training"] = build_scs_joint_training()
    built_icons["scs_multilateral_exercise"] = build_scs_multilateral_exercise()

    print("\nRegistering in interface/VIE_md_focus_icons.gfx...")
    register_sprites()

    print("\nUpdating focus tree icons in common/national_focus/VIE_md_focus.txt...")
    update_focus_tree()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 13 SOUTH CHINA SEA ICONS INTEGRATED")
    print("=" * 65)


if __name__ == "__main__":
    main()
