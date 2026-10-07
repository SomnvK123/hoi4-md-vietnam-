"""Script to build Focus Icons for Vietnam Governance, State Reform & Streamlining Apparatus
(Cụm 3: Cải cách Thể chế, Hành chính & Tinh gọn Bộ máy - 13 focuses)
in Millennium Dawn with authentic 3D Painterly / Heraldic Relief style.

13 Focuses:
1.  grassroots_democracy: Quy chế Dân chủ Cơ sở (Golden ballot box, democratic voting card, parchment ordinance, laurel)
2.  mass_mobilization: Các tổ chức quần chúng ở cơ sở (Fatherland Front lotus crest, united hands of mass unions, flags)
3.  ethnic_policy: Chính sách cho Tây Nguyên và vùng biên giới (Rong communal house, border mountains, brocade pattern, star)
4.  national_assembly_role: Quốc hội mạnh hơn (National Assembly Ba Dinh building, legislative gavel, golden laurel)
5.  state_audit: Kiểm toán Nhà nước (State Audit emblem, balance scale, golden measuring ruler, inspected ledger)
6.  public_admin_reform: Cải cách hành chính công (Open modern one-stop portal door, green approved seal stamp, streamlined papers)
7.  anti_corruption_law: Luật Phòng, chống tham nhũng (Crimson law book codex with gold lettering, justice gavel, steel shield)
8.  decentralization: Phân cấp quyền hạn cho các tỉnh (Gilded map of Vietnam radiating power to regional hubs, arrows)
9.  platform_2011: Cương lĩnh 2011 và Chiến lược 2011-2020 (Monumental red Platform 2011 book, theory torch, golden star)
10. streamline_apparatus: Tinh gọn tổ chức bộ máy (Golden shears cutting redundant red tape, sleek streamlined pyramid apparatus)
11. e_government: Chính phủ điện tử (Digital tablet showing National Public Service portal with coat of arms, glowing network)
12. resolution_57_68: Nghị quyết 66 về xây dựng pháp luật (Legislative reform scroll, golden fountain pen, gear freed from chains)
13. institutional_bottlenecks: Tháo gỡ điểm nghẽn thể chế (Heavy gold sledgehammer shattering roadblock boulder, highway to horizon)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
- Brain showcase: governance_reform_icons_showcase.png
"""

import math
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

STEMS = [
    "grassroots_democracy",
    "mass_mobilization",
    "ethnic_policy",
    "national_assembly_role",
    "state_audit",
    "public_admin_reform",
    "anti_corruption_law",
    "decentralization",
    "platform_2011",
    "streamline_apparatus",
    "e_government",
    "resolution_57_68",
    "institutional_bottlenecks",
]

# =========================================================================
# UTILITIES: DDS & PNG SAVER, SHADOWS, HERALDRY
# =========================================================================

def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border to guarantee clean cutouts in Clausewitz engine
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
    """Generate faceted gold star with high-depth drop shadow."""
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


def create_vpa_cockade(size: int = 20) -> Image.Image:
    """Generate official Vietnam gold & red cockade roundel."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(125, 90, 15, 255))
    r_inner = r_outer - 2.0
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_golden_laurel_wreath(w: int = 86, h: int = 76, gold_hue: bool = True) -> Image.Image:
    """Render procedural 3D metallic laurel wreath with leaves and berries."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    cx = w / 2
    cy = h / 2 + 6
    rx = w / 2 - 5
    ry = h / 2 - 5

    c_leaf = (235, 190, 45, 255) if gold_hue else (210, 175, 75, 255)
    c_leaf_hl = (255, 245, 140, 220) if gold_hue else (245, 225, 150, 220)
    c_shadow = (120, 85, 15, 255)

    for i in range(12):
        frac = i / 11.0
        ang_left = math.pi * 0.55 + frac * math.pi * 0.95
        ang_right = math.pi * 0.45 - frac * math.pi * 0.95

        lx = cx + rx * math.cos(ang_left)
        ly = cy + ry * math.sin(ang_left)
        l_leaf_ang = ang_left - 0.4

        rx_pt = cx + rx * math.cos(ang_right)
        ry_pt = cy + ry * math.sin(ang_right)
        r_leaf_ang = ang_right + 0.4

        leaf_len = 8.5 - frac * 2.0
        leaf_w = 4.0

        for px, py, lang in [(lx, ly, l_leaf_ang), (rx_pt, ry_pt, r_leaf_ang)]:
            tip_x = px + leaf_len * math.cos(lang)
            tip_y = py + leaf_len * math.sin(lang)
            norm_x = -math.sin(lang) * leaf_w * 0.5
            norm_y = math.cos(lang) * leaf_w * 0.5

            pts = [(px, py), (px + leaf_len * 0.5 * math.cos(lang) + norm_x, py + leaf_len * 0.5 * math.sin(lang) + norm_y),
                   (tip_x, tip_y), (px + leaf_len * 0.5 * math.cos(lang) - norm_x, py + leaf_len * 0.5 * math.sin(lang) - norm_y)]
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


# =========================================================================
# 13 BUILDER FUNCTIONS (CỤM 3: CẢI CÁCH THỂ CHẾ & TINH GỌN BỘ MÁY)
# =========================================================================

# 1. VIE_grassroots_democracy: Quy chế Dân chủ Cơ sở
def build_grassroots_democracy() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Election / Assembly Box
    base_p = MD_GOALS / "00_politics" / "democracy_genericus.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Golden Democratic Ballot Box with red star voting card
    bbox = Image.new("RGBA", (44, 34), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bbox)
    # Box front in gold & bronze
    bdraw.polygon([(4, 12), (40, 12), (36, 32), (8, 32)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    bdraw.rectangle([6, 10, 38, 14], fill=(255, 225, 75, 255), outline=(130, 90, 15, 255))
    # Ballot slot
    bdraw.rectangle([16, 11, 28, 13], fill=(40, 25, 10, 255))
    # Red ballot paper inserting into slot
    bdraw.rounded_rectangle([18, 2, 26, 14], radius=2, fill=(200, 25, 25, 255), outline=(245, 215, 60, 255))
    s_ballot = create_gold_star(6)
    bbox.paste(s_ballot, (19, 4), s_ballot)
    # Star on ballot box face
    s_box = create_gold_star(10)
    bbox.paste(s_box, (17, 18), s_box)
    canvas.paste(bbox, ((TARGET_SIZE[0] - bbox.width) // 2, 40), bbox)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "grassroots_democracy")
    return canvas


# 2. VIE_mass_mobilization: Các tổ chức quần chúng ở cơ sở (Dân vận & Đoàn thể)
def build_mass_mobilization() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Popular Front / Mass Crowd Assembly
    base_p = MD_GOALS / "00_politics" / "focus_generic_conference.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Fatherland Front Lotus Crest + United Clasp
    crest = Image.new("RGBA", (48, 38), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(crest)
    # Red enamel oval badge
    cdraw.ellipse([4, 4, 44, 34], fill=(185, 20, 20, 255), outline=(245, 215, 60, 255), width=2)
    # Golden lotus petals of Fatherland Front
    cdraw.polygon([(24, 8), (28, 20), (24, 28), (20, 20)], fill=(255, 235, 120, 255), outline=(150, 110, 15, 255))
    cdraw.polygon([(24, 18), (14, 16), (16, 26), (24, 28)], fill=(245, 215, 75, 255), outline=(140, 100, 15, 255))
    cdraw.polygon([(24, 18), (34, 16), (32, 26), (24, 28)], fill=(245, 215, 75, 255), outline=(140, 100, 15, 255))
    # Center star
    s_cr = create_gold_star(9)
    crest.paste(s_cr, (20, 15), s_cr)
    canvas.paste(crest, ((TARGET_SIZE[0] - crest.width) // 2, 36), crest)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "mass_mobilization")
    return canvas


# 3. VIE_ethnic_policy: Chính sách cho Tây Nguyên và vùng biên giới
def build_ethnic_policy() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Mountainous Regions / Land Development
    base_p = MD_GOALS / "00_politics" / "focus_generic_land_redistribution.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Highland Rong Communal House & Brocade Emblem
    rong = Image.new("RGBA", (44, 42), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(rong)
    # High soaring triangular roof of Rong house (Nhà rông)
    rdraw.polygon([(22, 2), (38, 28), (6, 28)], fill=(155, 95, 35, 255), outline=(235, 195, 45, 255), width=2)
    # Wood stilts & floor
    rdraw.rectangle([10, 28, 34, 32], fill=(130, 75, 25, 255), outline=(225, 175, 40, 255))
    rdraw.line([(12, 32), (12, 40)], fill=(120, 70, 20, 255), width=2)
    rdraw.line([(22, 32), (22, 40)], fill=(120, 70, 20, 255), width=2)
    rdraw.line([(32, 32), (32, 40)], fill=(120, 70, 20, 255), width=2)
    # Traditional brocade geometric diamond pattern on roof
    rdraw.polygon([(22, 8), (28, 18), (22, 26), (16, 18)], fill=(205, 25, 25, 255), outline=(255, 235, 120, 255), width=1)
    s_rong = create_gold_star(8)
    rong.paste(s_rong, (18, 14), s_rong)
    canvas.paste(rong, ((TARGET_SIZE[0] - rong.width) // 2, 30), rong)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "ethnic_policy")
    return canvas


# 4. VIE_national_assembly_role: Quốc hội mạnh hơn (Nâng cao vai trò Quốc hội)
def build_national_assembly_role() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Parliament Building / Assembly Dome
    base_p = MD_GOALS / "00_politics" / "Focus_Parliament_Constitution.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # National Assembly of Vietnam (Nhà Quốc hội Ba Đình) emblem + Gavel
    na = Image.new("RGBA", (50, 36), (0, 0, 0, 0))
    ndraw = ImageDraw.Draw(na)
    # Square building with central round dome (trời tròn đất vuông)
    ndraw.rectangle([6, 14, 44, 32], fill=(235, 235, 240, 255), outline=(215, 175, 45, 255), width=2)
    # Central cylindrical assembly chamber
    ndraw.rounded_rectangle([14, 6, 36, 18], radius=4, fill=(245, 205, 55, 255), outline=(130, 90, 15, 255))
    # Red star crest on assembly facade
    ndraw.rectangle([18, 20, 32, 28], fill=(185, 20, 20, 255), outline=(235, 195, 45, 255))
    s_na = create_gold_star(8)
    na.paste(s_na, (21, 20), s_na)
    canvas.paste(na, ((TARGET_SIZE[0] - na.width) // 2, 38), na)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "national_assembly_role")
    return canvas


# 5. VIE_state_audit: Kiểm toán Nhà nước
def build_state_audit() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Financial Agreement / Audit Ledger
    base_p = MD_GOALS / "00_politics" / "focus_generic_financial_agreement.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # State Audit Golden Balance Scale & Measurement Ruler
    audit = Image.new("RGBA", (48, 36), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(audit)
    # Balance beam in gold
    adraw.line([(6, 12), (42, 12)], fill=(245, 215, 65, 255), width=3)
    adraw.line([(24, 6), (24, 30)], fill=(245, 215, 65, 255), width=3)
    # Scale pans
    # Left pan
    adraw.line([(6, 12), (2, 22)], fill=(215, 175, 40, 255), width=1)
    adraw.line([(6, 12), (10, 22)], fill=(215, 175, 40, 255), width=1)
    adraw.arc([1, 18, 11, 26], start=0, end=180, fill=(245, 205, 55, 255), width=2)
    # Right pan
    adraw.line([(42, 12), (38, 22)], fill=(215, 175, 40, 255), width=1)
    adraw.line([(42, 12), (46, 22)], fill=(215, 175, 40, 255), width=1)
    adraw.arc([37, 18, 47, 26], start=0, end=180, fill=(245, 205, 55, 255), width=2)
    # Red star badge on center pillar
    adraw.ellipse([18, 18, 30, 30], fill=(185, 20, 20, 255), outline=(245, 215, 60, 255))
    s_aud = create_gold_star(8)
    audit.paste(s_aud, (20, 20), s_aud)
    canvas.paste(audit, ((TARGET_SIZE[0] - audit.width) // 2, 38), audit)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "state_audit")
    return canvas


# 6. VIE_public_admin_reform: Cải cách hành chính công (Cơ chế Một cửa)
def build_public_admin_reform() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Administrative Reform / Modern Bureau
    base_p = MD_GOALS / "00_politics" / "focus_generic_improve_the_administration.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Modern One-Stop Portal Door (Cơ chế Một cửa) & Approved Green Stamp
    door = Image.new("RGBA", (44, 34), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(door)
    # Portal frame in bronze & gold
    ddraw.rounded_rectangle([2, 4, 42, 32], radius=4, fill=(35, 55, 80, 255), outline=(235, 195, 45, 255), width=2)
    # Glass service window
    ddraw.rectangle([6, 8, 38, 22], fill=(40, 160, 220, 180), outline=(255, 235, 120, 255))
    # Green APPROVED stamp badge
    ddraw.rounded_rectangle([18, 16, 40, 28], radius=3, fill=(25, 145, 45, 255), outline=(255, 255, 255, 255), width=1)
    # Checkmark inside stamp
    ddraw.polygon([(22, 22), (25, 25), (32, 18), (30, 17), (25, 23), (23, 21)], fill=(255, 255, 255, 255))
    # Red star at portal peak
    s_d = create_gold_star(7)
    door.paste(s_d, (6, 5), s_d)
    canvas.paste(door, ((TARGET_SIZE[0] - door.width) // 2, 42), door)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "public_admin_reform")
    return canvas


# 7. VIE_anti_corruption_law: Luật Phòng, chống tham nhũng sửa đổi
def build_anti_corruption_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Legal Codex & Gavel
    base_p = MD_GOALS / "00_politics" / "pass_legislation.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Gilded Law Book "LUAT PCTN" on Pedestal
    book = Image.new("RGBA", (48, 34), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(book)
    # Red leather cover with gold filigree border
    bdraw.rounded_rectangle([2, 4, 46, 30], radius=4, fill=(175, 20, 20, 255), outline=(245, 215, 60, 255), width=2)
    bdraw.line([(24, 4), (24, 30)], fill=(245, 215, 60, 255), width=2)
    # Gold star crest on cover
    s_bk = create_gold_star(12)
    book.paste(s_bk, (6, 11), s_bk)
    # Balance scales on right page
    bdraw.line([(28, 14), (42, 14)], fill=(255, 235, 120, 255), width=2)
    bdraw.line([(35, 10), (35, 24)], fill=(255, 235, 120, 255), width=2)
    bdraw.arc([(27, 16), (33, 22)], start=0, end=180, fill=(255, 235, 120, 255), width=1)
    bdraw.arc([(37, 16), (43, 22)], start=0, end=180, fill=(255, 235, 120, 255), width=1)
    canvas.paste(book, ((TARGET_SIZE[0] - book.width) // 2, 42), book)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "anti_corruption_law")
    return canvas


# 8. VIE_decentralization: Phân cấp quyền hạn cho các tỉnh
def build_decentralization() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Decentralization / Regional Network
    base_p = MD_GOALS / "00_politics" / "Decentralization.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Golden Map S-curve of Vietnam radiating power to provincial hubs
    vmap = Image.new("RGBA", (44, 38), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vmap)
    # S-curve spine in gold
    vdraw.line([(26, 6), (22, 14), (25, 22), (20, 32)], fill=(245, 215, 60, 255), width=3)
    # Radiating nodes: Hanoi, Danang, HCMC, Cantho
    nodes = [(26, 6), (24, 18), (22, 28), (18, 34)]
    for nx, ny in nodes:
        vdraw.ellipse([nx - 3, ny - 3, nx + 3, ny + 3], fill=(200, 25, 25, 255), outline=(255, 240, 140, 255), width=1)
        # Radiating arrows outward
        vdraw.line([(nx, ny), (nx - 6, ny - 2)], fill=(255, 220, 60, 200), width=1)
        vdraw.line([(nx, ny), (nx + 6, ny + 2)], fill=(255, 220, 60, 200), width=1)
    canvas.paste(vmap, ((TARGET_SIZE[0] - vmap.width) // 2, 38), vmap)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "decentralization")
    return canvas


# 9. VIE_platform_2011: Cương lĩnh 2011 và Chiến lược 2011-2020
def build_platform_2011() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Legislative Palace / Communist Theory Platform
    base_p = MD_GOALS / "china" / "communist_party_of_china.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((78, 68), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Red Platform Book "2011" with Golden Theory Torch
    book2011 = Image.new("RGBA", (54, 34), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(book2011)
    bdraw.rounded_rectangle([0, 0, 52, 32], radius=5, fill=(185, 20, 20, 255), outline=(245, 215, 60, 255), width=2)
    bdraw.line([(26, 2), (26, 30)], fill=(245, 215, 60, 255), width=2)
    # Text "2011" on cover in gold
    try:
        font_p = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 10)
    except Exception:
        font_p = ImageFont.load_default()
    bdraw.text((3, 5), "CUONG", fill=(255, 235, 120, 255), font=font_p)
    bdraw.text((4, 17), "LINH", fill=(255, 235, 120, 255), font=font_p)

    # Right page: Golden Torch of Socialist Direction
    bdraw.polygon([(40, 14), (43, 26), (38, 26)], fill=(225, 185, 45, 255), outline=(130, 90, 15, 255))
    bdraw.polygon([(36, 14), (40, 4), (44, 14)], fill=(255, 180, 20, 255), outline=(255, 70, 10, 255))
    bdraw.polygon([(38, 13), (40, 7), (42, 13)], fill=(255, 255, 150, 255))
    canvas.paste(book2011, ((TARGET_SIZE[0] - book2011.width) // 2, 38), book2011)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "platform_2011")
    return canvas


# 10. VIE_streamline_apparatus: Tinh gọn tổ chức bộ máy (Nghị quyết 18)
def build_streamline_apparatus() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base State Organization / Reform
    base_p = MD_GOALS / "00_politics" / "focus_generic_improve_the_administration.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Golden Shears cutting redundant red tape & Streamlined Triangle Apparatus
    shears = Image.new("RGBA", (48, 38), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shears)
    # Streamlined 3-tier hierarchy pyramid (pure efficiency)
    sdraw.polygon([(24, 6), (36, 26), (12, 26)], fill=(35, 55, 80, 255), outline=(245, 215, 60, 255), width=2)
    # Internal division lines
    sdraw.line([(18, 16), (30, 16)], fill=(245, 215, 60, 255), width=1)
    # Golden shears / scissors cutting redundant ribbons
    # Blade 1
    sdraw.line([(8, 8), (28, 28)], fill=(245, 205, 55, 255), width=3)
    # Blade 2
    sdraw.line([(8, 28), (28, 8)], fill=(245, 205, 55, 255), width=3)
    # Pivot screw
    sdraw.ellipse([16, 16, 20, 20], fill=(200, 25, 25, 255))
    # Cut ribbon pieces falling
    sdraw.line([(28, 14), (38, 10)], fill=(200, 25, 25, 255), width=2)
    sdraw.line([(28, 22), (38, 26)], fill=(200, 25, 25, 255), width=2)
    canvas.paste(shears, ((TARGET_SIZE[0] - shears.width) // 2, 40), shears)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "streamline_apparatus")
    return canvas


# 11. VIE_e_government: Chính phủ điện tử (Dịch vụ công trực tuyến)
def build_e_government() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Cyber Grid / High-Tech Computing
    base_p = MD_GOALS / "00_economy" / "economic_tech.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Digital Tablet Portal displaying National Public Service with Coat of Arms
    tablet = Image.new("RGBA", (46, 34), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(tablet)
    # Tablet bezel in slate grey & gold rim
    tdraw.rounded_rectangle([2, 2, 44, 32], radius=4, fill=(25, 30, 42, 255), outline=(225, 185, 45, 255), width=2)
    # Luminous cyan screen
    tdraw.rectangle([6, 6, 40, 28], fill=(15, 60, 110, 255))
    # National coat of arms cockade on screen
    s_tab = create_gold_star(10)
    tablet.paste(s_tab, (18, 9), s_tab)
    # Digital wifi / transmission waves above tablet
    tdraw.arc([16, 2, 30, 12], start=210, end=330, fill=(40, 220, 240, 255), width=2)
    tdraw.arc([12, -2, 34, 16], start=210, end=330, fill=(40, 220, 240, 200), width=1)
    canvas.paste(tablet, ((TARGET_SIZE[0] - tablet.width) // 2, 42), tablet)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "e_government")
    return canvas


# 12. VIE_resolution_57_68: Nghị quyết 66 về xây dựng pháp luật
def build_resolution_57_68() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Legislative Treaty / Legal Reform Scroll
    base_p = MD_GOALS / "00_politics" / "pass_legislation.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Legal Reform Scroll with Golden Pen & Broken Bureaucratic Chains
    scroll = Image.new("RGBA", (48, 36), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scroll)
    # White-gold scroll parchment
    sdraw.rounded_rectangle([4, 4, 44, 32], radius=4, fill=(245, 245, 235, 255), outline=(225, 185, 45, 255), width=2)
    # Red heading bar
    sdraw.rectangle([6, 6, 42, 12], fill=(185, 20, 20, 255))
    # Text lines on parchment
    for y in [16, 21, 26]:
        sdraw.line([(8, y), (36, y)], fill=(70, 85, 100, 255), width=1)
    # Golden fountain pen signing
    sdraw.line([(26, 28), (40, 10)], fill=(245, 205, 55, 255), width=3)
    sdraw.polygon([(40, 10), (43, 7), (41, 13)], fill=(255, 245, 150, 255))
    # Star wax seal on left
    s_sc = create_gold_star(8)
    scroll.paste(s_sc, (8, 16), s_sc)
    canvas.paste(scroll, ((TARGET_SIZE[0] - scroll.width) // 2, 42), scroll)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_57_68")
    return canvas


# 13. VIE_institutional_bottlenecks: Tháo gỡ điểm nghẽn thể chế
def build_institutional_bottlenecks() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Economic Highway / Open Road Ahead
    base_p = MD_GOALS / "00_economy" / "economic_prosperity2.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.28)
    base = ImageEnhance.Contrast(base).enhance(1.18)
    base = base.resize((84, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Massive Golden Sledgehammer shattering the institutional boulder
    breakthrough = Image.new("RGBA", (52, 44), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(breakthrough)
    # Grey roadblock stone boulder shattering with cracks
    pts_rock = [(10, 20), (22, 14), (36, 16), (44, 28), (38, 40), (14, 40)]
    bdraw.polygon(pts_rock, fill=(75, 85, 100, 255), outline=(215, 185, 60, 255), width=2)
    # Bright fracture cracks in stone
    bdraw.line([(24, 18), (28, 28)], fill=(255, 235, 120, 255), width=2)
    bdraw.line([(28, 28), (20, 36)], fill=(255, 235, 120, 255), width=2)
    bdraw.line([(28, 28), (38, 34)], fill=(255, 235, 120, 255), width=2)

    # Heavy gold sledgehammer swinging down
    # Hammer head
    bdraw.polygon([(16, 4), (34, 4), (36, 14), (14, 14)], fill=(245, 205, 45, 255), outline=(130, 90, 15, 255), width=2)
    bdraw.line([(16, 6), (34, 6)], fill=(255, 245, 150, 255), width=1)
    # Shaft
    bdraw.line([(25, 14), (25, 32)], fill=(160, 110, 20, 255), width=3)
    # Striking sparks radiating
    for sp in [(6, 18), (46, 20), (12, 10), (40, 10)]:
        bdraw.line([(25, 14), sp], fill=(255, 240, 130, 255), width=2)
    canvas.paste(breakthrough, ((TARGET_SIZE[0] - breakthrough.width) // 2, 28), breakthrough)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "institutional_bottlenecks")
    return canvas


# =========================================================================
# REGISTRATION & INTEGRATION
# =========================================================================

def register_sprites():
    """Register spriteTypes in interface/VIE_md_focus_icons.gfx."""
    text = GFX_FILE.read_text(encoding="utf-8")
    added = 0
    new_entries = []

    for stem in STEMS:
        sprite_name = f"GFX_focus_VIE_{stem}"
        if sprite_name not in text:
            entry = f"""\tspriteType = {{
\t\tname = "{sprite_name}"
\t\ttexturefile = "gfx/interface/goals/{stem}.dds"
\t}}"""
            new_entries.append(entry)
            added += 1

    if new_entries:
        idx = text.rfind("}")
        if idx != -1:
            updated = text[:idx] + "\n".join(new_entries) + "\n" + text[idx:]
            GFX_FILE.write_text(updated, encoding="utf-8")
            print(f"Registered {added} new spriteTypes in {GFX_FILE}")
    else:
        print("All spriteTypes already registered.")


def update_focus_tree_icons():
    """Update common/national_focus/VIE_md_focus.txt with the new GFX_focus_VIE_ icons."""
    text = FOCUS_FILE.read_text(encoding="utf-8")
    updated = text

    focus_mapping = {
        "VIE_grassroots_democracy": "GFX_focus_VIE_grassroots_democracy",
        "VIE_mass_mobilization": "GFX_focus_VIE_mass_mobilization",
        "VIE_ethnic_policy": "GFX_focus_VIE_ethnic_policy",
        "VIE_national_assembly_role": "GFX_focus_VIE_national_assembly_role",
        "VIE_state_audit": "GFX_focus_VIE_state_audit",
        "VIE_public_admin_reform": "GFX_focus_VIE_public_admin_reform",
        "VIE_anti_corruption_law": "GFX_focus_VIE_anti_corruption_law",
        "VIE_decentralization": "GFX_focus_VIE_decentralization",
        "VIE_platform_2011": "GFX_focus_VIE_platform_2011",
        "VIE_streamline_apparatus": "GFX_focus_VIE_streamline_apparatus",
        "VIE_e_government": "GFX_focus_VIE_e_government",
        "VIE_resolution_57_68": "GFX_focus_VIE_resolution_57_68",
        "VIE_institutional_bottlenecks": "GFX_focus_VIE_institutional_bottlenecks",
    }

    import re
    replaced_count = 0
    for fid, new_gfx in focus_mapping.items():
        pattern = rf"(id\s*=\s*{fid}\s*\n\s*icon\s*=\s*)(\w+)"
        if re.search(pattern, updated):
            updated, n = re.subn(pattern, rf"\g<1>{new_gfx}", updated)
            if n > 0:
                replaced_count += n
                print(f"  [FOCUS TREE] {fid} -> icon = {new_gfx}")

    if replaced_count > 0:
        FOCUS_FILE.write_text(updated, encoding="utf-8")
        print(f"Updated {replaced_count} focuses in {FOCUS_FILE}")
    else:
        print("Focus tree icons already up to date.")


def create_showcase_artifact(icons: dict[str, Image.Image]):
    """Create a contact sheet showcase image of all 13 Governance & State Reform focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "governance_reform_icons_showcase.png"

    cols = 5
    rows = (len(icons) + cols - 1) // cols
    card_w, card_h = 185, 145
    pad_x, pad_y = 20, 20
    header_h = 90

    total_w = pad_x * 2 + cols * card_w + (cols - 1) * 15
    total_h = header_h + rows * card_h + (rows - 1) * 15 + pad_y

    canvas = Image.new("RGBA", (total_w, total_h), (14, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_id = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_name = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_title = font_sub = font_id = font_name = None

    draw.text((pad_x, 20), "BỘ ICON GFX: CẢI CÁCH THỂ CHẾ & TINH GỌN BỘ MÁY (CỤM 3)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "13 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "grassroots_democracy": "Dân chủ ở cơ sở",
        "mass_mobilization": "Đoàn thể & Dân vận",
        "ethnic_policy": "Đoàn kết Dân tộc & Miền núi",
        "national_assembly_role": "Nâng cao vai trò Quốc hội",
        "state_audit": "Kiểm toán Nhà nước",
        "public_admin_reform": "Cải cách Hành chính công",
        "anti_corruption_law": "Luật PCTN sửa đổi",
        "decentralization": "Phân cấp phân quyền",
        "platform_2011": "Cương lĩnh 2011",
        "streamline_apparatus": "Tinh gọn bộ máy (NQ 18)",
        "e_government": "Chính phủ điện tử",
        "resolution_57_68": "NQ 66 Xây dựng pháp luật",
        "institutional_bottlenecks": "Tháo gỡ điểm nghẽn thể chế",
    }

    for idx, (stem, img) in enumerate(icons.items()):
        c = idx % cols
        r = idx // cols
        x = pad_x + c * (card_w + 15)
        y = header_h + r * (card_h + 15)

        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill=(22, 28, 38, 255), outline=(45, 60, 80, 255))

        icon_x = x + (card_w - img.width) // 2
        icon_y = y + 10
        canvas.paste(img, (icon_x, icon_y), img)

        t_title = focus_titles.get(stem, stem)
        draw.text((x + 8, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 8, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    canvas.save(out_path)
    print(f"Showcase image saved: {out_path}")


def main():
    print("=" * 65)
    print("BUILDING 13 GOVERNANCE & STATE REFORM FOCUS ICONS")
    print("=" * 65)

    built_icons = {}
    built_icons["grassroots_democracy"] = build_grassroots_democracy()
    built_icons["mass_mobilization"] = build_mass_mobilization()
    built_icons["ethnic_policy"] = build_ethnic_policy()
    built_icons["national_assembly_role"] = build_national_assembly_role()
    built_icons["state_audit"] = build_state_audit()
    built_icons["public_admin_reform"] = build_public_admin_reform()
    built_icons["anti_corruption_law"] = build_anti_corruption_law()
    built_icons["decentralization"] = build_decentralization()
    built_icons["platform_2011"] = build_platform_2011()
    built_icons["streamline_apparatus"] = build_streamline_apparatus()
    built_icons["e_government"] = build_e_government()
    built_icons["resolution_57_68"] = build_resolution_57_68()
    built_icons["institutional_bottlenecks"] = build_institutional_bottlenecks()

    print("\nRegistering GFX sprites...")
    register_sprites()

    print("\nUpdating focus tree...")
    update_focus_tree_icons()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 13 ICONS GENERATED & REGISTERED")
    print("=" * 65)


if __name__ == "__main__":
    main()
