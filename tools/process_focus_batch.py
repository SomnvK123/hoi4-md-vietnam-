"""Master Image Processor & DDS Compiler for MD Vietnam Focus Icons.
Converts high-resolution concept art into AAA game-ready Paradox Clausewitz Heraldic Badge DDS assets.
Specifications:
- Canvas: 93x91 px
- Format: Uncompressed 32-bit BGRA DDS (Header: 128 bytes, Data: 33,852 bytes, Total: 33,980 bytes)
- Structure: Authentic 3D Heraldic Badge with Inset Centerpiece Artwork, Golden Laurel Wreath,
  3 Gold Stars Crest, Red-Gold Cockade Pedestal, Radial Sunburst Sparks, and Ambient Drop Shadow.
- 1px Alpha Border: Alpha = 0 strictly on all border pixels to prevent shader bleed.
"""

import math
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
TARGET_SIZE = (93, 91)

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

    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(150, 110, 15, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 248, 140, 210))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(180, 130, 15, 220))
    return im

def create_vpa_cockade(size: int = 18) -> Image.Image:
    """Generate official Vietnam gold & red cockade roundel."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(225, 185, 45, 255), outline=(130, 95, 15, 255))
    r_inner = r_outer - 2.0
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(218, 37, 29, 255), outline=(130, 20, 20, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im

def create_golden_laurel_wreath(w: int = 88, h: int = 76) -> Image.Image:
    """Render procedural 3D metallic laurel wreath with leaves and highlights."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx = w / 2
    cy = h / 2 + 3
    rx = w / 2 - 4
    ry = h / 2 - 5

    c_leaf = (235, 192, 45, 255)
    c_leaf_hl = (255, 248, 150, 230)
    c_shadow = (115, 78, 12, 255)

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

        leaf_len = 9.0 - frac * 2.0
        leaf_w = 4.4

        for px, py, lang in [(lx, ly, l_leaf_ang), (rx_pt, ry_pt, r_leaf_ang)]:
            tip_x = px + leaf_len * math.cos(lang)
            tip_y = py + leaf_len * math.sin(lang)
            norm_x = -math.sin(lang) * leaf_w * 0.5
            norm_y = math.cos(lang) * leaf_w * 0.5

            pts = [
                (px, py),
                (px + leaf_len * 0.5 * math.cos(lang) + norm_x, py + leaf_len * 0.5 * math.sin(lang) + norm_y),
                (tip_x, tip_y),
                (px + leaf_len * 0.5 * math.cos(lang) - norm_x, py + leaf_len * 0.5 * math.sin(lang) - norm_y)
            ]
            draw.polygon(pts, fill=c_leaf, outline=c_shadow)
            draw.line([(px, py), (tip_x, tip_y)], fill=c_leaf_hl, width=1)
    return im

def create_sunburst_sparks(w: int = 93, h: int = 91) -> Image.Image:
    """Generate radiant diamond sparks around the wreath."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = w / 2, h / 2 - 2
    r_spark = 41
    for i in range(14):
        ang = i * 2 * math.pi / 14 - math.pi / 2
        if 0.32 * math.pi < ang < 0.68 * math.pi:
            continue
        sx = cx + r_spark * math.cos(ang)
        sy = cy + (r_spark - 3) * math.sin(ang)
        sz = 2.6
        pts = [(sx, sy - sz), (sx + sz * 0.8, sy), (sx, sy + sz), (sx - sz * 0.8, sy)]
        draw.polygon(pts, fill=(255, 238, 130, 240), outline=(210, 160, 30, 210))
    return im

def build_framed_heraldic_badge(source_image: Image.Image) -> Image.Image:
    """Compose artwork into full 3D Paradox Heraldic Frame with transparent backdrop."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    art = source_image.convert("RGBA")

    # 1. Radiant sunburst sparks in backdrop
    sparks = create_sunburst_sparks()
    canvas.paste(sparks, (0, 0), sparks)

    # 2. Golden laurel wreath
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 7), laurel)

    # 3. Inner circular inset for centerpiece artwork (Diameter = 62px, centered)
    inset_d = 62
    inset_cx, inset_cy = 46, 40

    w, h = art.size
    min_dim = min(w, h)
    art_cropped = art.crop(((w - min_dim) // 2, (h - min_dim) // 2, (w + min_dim) // 2, (h + min_dim) // 2))
    art_resized = art_cropped.resize((inset_d, inset_d), Image.Resampling.LANCZOS)

    # Anti-aliased circular mask
    mask = Image.new("L", (inset_d * 4, inset_d * 4), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.ellipse((0, 0, inset_d * 4 - 1, inset_d * 4 - 1), fill=255)
    mask = mask.resize((inset_d, inset_d), Image.Resampling.LANCZOS)

    # Double metallic bezel ring
    bezel = Image.new("RGBA", (inset_d + 4, inset_d + 4), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bezel)
    bdraw.ellipse((0, 0, inset_d + 3, inset_d + 3), outline=(130, 95, 15, 255), width=2)
    bdraw.ellipse((1, 1, inset_d + 2, inset_d + 2), outline=(255, 238, 130, 230), width=1)

    canvas.paste(bezel, (inset_cx - (inset_d + 4) // 2, inset_cy - (inset_d + 4) // 2), bezel)
    canvas.paste(art_resized, (inset_cx - inset_d // 2, inset_cy - inset_d // 2), mask)

    # 4. Top Crown: 3 Gold Stars (middle 16px, two side 11px)
    star_mid = create_gold_star(16)
    star_side = create_gold_star(11)
    canvas.paste(star_side, (inset_cx - 19, -1), star_side)
    canvas.paste(star_mid, (inset_cx - 8, -3), star_mid)
    canvas.paste(star_side, (inset_cx + 8, -1), star_side)

    # 5. Bottom Pedestal: Vietnam Red-Gold Cockade (18px)
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, (inset_cx - 9, 68), cockade)

    # 6. Ambient Occlusion Drop Shadow onto transparent canvas
    shadow = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow.paste(canvas, (0, 1), canvas)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(1.8))
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.75))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))

    final = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    final.paste(shadow, (0, 0), shadow)
    final.paste(canvas, (0, 0), canvas)

    # 7. Smart Unsharp Masking on the composite
    final = final.filter(ImageFilter.UnsharpMask(radius=1.1, percent=115, threshold=2))

    # 8. Micro-noise injection to prevent any banding
    arr = np.array(final, dtype=np.float32)
    alpha_mask = arr[:, :, 3] > 10
    noise = np.random.normal(0, 2.0, arr[:, :, :3].shape)
    for c in range(3):
        arr[:, :, c] = np.where(alpha_mask, np.clip(arr[:, :, c] + noise[:, :, c], 0, 255), 0)
    processed = Image.fromarray(arr.astype(np.uint8), mode="RGBA").copy()

    # 9. Strict 1px alpha border
    pixels = processed.load()
    tw, th = TARGET_SIZE
    for x in range(tw):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, th - 1] = (pixels[x, th - 1][0], pixels[x, th - 1][1], pixels[x, th - 1][2], 0)
    for y in range(th):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[tw - 1, y] = (pixels[tw - 1, y][0], pixels[tw - 1, y][1], pixels[tw - 1, y][2], 0)

    return processed

def export_to_game_dds_and_png(source_image: Image.Image, stem: str, framed: bool = True) -> dict:
    DDS_DIR.mkdir(parents=True, exist_ok=True)
    PNG_DIR.mkdir(parents=True, exist_ok=True)

    if framed:
        processed = build_framed_heraldic_badge(source_image)
    else:
        # Fallback raw square
        img = source_image.convert("RGBA")
        w, h = img.size
        min_dim = min(w, h)
        cropped = img.crop(((w - min_dim) // 2, (h - min_dim) // 2, (w + min_dim) // 2, (h + min_dim) // 2))
        resized = cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        processed = resized

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    processed.save(png_path, "PNG")

    # Build 32-bit BGRA DDS (exact 33,980 bytes)
    tw, th = TARGET_SIZE
    magic = b"DDS "
    size = 124
    flags = 0x00001007
    height = th
    width = tw
    pitch = tw * 4
    depth = 0
    mipmaps = 0
    reserved1 = b"\x00" * 44

    pf_size = 32
    pf_flags = 0x00000041
    pf_fourcc = b"\x00\x00\x00\x00"
    pf_rgb_bits = 32
    pf_r_mask = 0x00FF0000
    pf_g_mask = 0x0000FF00
    pf_b_mask = 0x000000FF
    pf_a_mask = 0xFF000000

    caps = 0x00001000
    caps2 = 0
    caps3 = 0
    caps4 = 0
    reserved2 = 0

    header = struct.pack(
        "<4sIIIIIII44sII4sIIIIIIIIII",
        magic, size, flags, height, width, pitch, depth, mipmaps, reserved1,
        pf_size, pf_flags, pf_fourcc, pf_rgb_bits, pf_r_mask, pf_g_mask, pf_b_mask, pf_a_mask,
        caps, caps2, caps3, caps4, reserved2
    )
    assert len(header) == 128

    pixels = processed.load()
    pixel_data = bytearray(tw * th * 4)
    idx = 0
    for y in range(th):
        for x in range(tw):
            r, g, b, a = pixels[x, y]
            pixel_data[idx] = b
            pixel_data[idx + 1] = g
            pixel_data[idx + 2] = r
            pixel_data[idx + 3] = a
            idx += 4

    dds_data = header + bytes(pixel_data)
    assert len(dds_data) == 33980, f"DDS length error: {len(dds_data)}"

    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(dds_data)

    arr = np.array(processed)
    solid = arr[:, :, 3] > 10
    unique_colors = len(set(tuple(p) for p in processed.convert("RGBA").getdata()))

    return {
        "stem": stem,
        "png_path": str(png_path),
        "dds_path": str(dds_path),
        "dds_bytes": len(dds_data),
        "unique_colors": unique_colors,
        "solid_ratio": float(np.mean(solid)),
    }

if __name__ == "__main__":
    if len(sys.argv) > 2:
        src = Path(sys.argv[1])
        stem = sys.argv[2]
        img = Image.open(src)
        res = export_to_game_dds_and_png(img, stem, framed=True)
        print("Success:", res)
