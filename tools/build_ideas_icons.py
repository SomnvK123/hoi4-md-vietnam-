"""Script to build 21st-Century Idea Icons for Vietnam Submod in Millennium Dawn.

Generates 4 Idea Icons (Standard 60x68 RGBA DDS & PNG):
1. VIE_military_rescue: Binh chung Cuu ho - Cuu nan / Phong thu dan su (Bao Yagi)
2. VIE_self_reliant_deterrence: Tu chu Cong nghe Quoc phong & Ran de noi dia (Radar 3D, VCM-01, STV-380)
3. VIE_def_ind_core: Doanh nghiep Quoc phong Nong cot (CNC, Vi mach so, Tau chien, Ten lua)
4. VIE_def_ind_divest: Co phan hoa & Thoai von Doanh nghiep (Chia khoa vang, Dong von, Hoa sen - Banh rang)

Outputs:
- assets/ideas/png/<stem>.png (60x68 RGBA PNG)
- gfx/interface/ideas/<stem>.dds (60x68 32-bit BGRA uncompressed DDS)
- interface/VIE_md_ideas.gfx
- Updates common/ideas/VIE_disaster_ideas.txt and common/ideas/VIE_md_ideas_p15.txt
"""

import os
import struct
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "ideas" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "ideas"
GFX_FILE = ROOT / "interface" / "VIE_md_ideas.gfx"

TARGET_SIZE = (60, 68)


def save_idea_dds_and_png(img: Image.Image, stem: str):
    """Save 60x68 canvas as PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert img.size == TARGET_SIZE
    assert img.mode == "RGBA"

    # Enforce pure alpha=0 at outer 1-pixel border for ultra-clean UI edges
    w, h = TARGET_SIZE
    pixels = img.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    img.save(png_path)

    # Write uncompressed 32-bit BGRA DDS standard for HOI4
    r, g, b, a = img.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    print(f"  [SAVED] {stem} -> PNG & DDS ({len(dds_path.read_bytes())} bytes)")


def fit_into_idea_canvas(cutout: Image.Image) -> Image.Image:
    """Scale cutout proportionally with Lanczos downsampling to fit nicely inside 60x68 canvas."""
    bbox = cutout.getbbox()
    if bbox:
        cropped = cutout.crop(bbox)
    else:
        cropped = cutout

    cw, ch = cropped.size
    # Target available area inside (60, 68) with 2px padding
    max_w, max_h = 56, 64
    scale = min(max_w / cw, max_h / ch)
    new_w = max(1, int(cw * scale))
    new_h = max(1, int(ch * scale))

    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    # Center horizontally and vertically (slightly lower if top has star)
    offset_x = (TARGET_SIZE[0] - new_w) // 2
    offset_y = (TARGET_SIZE[1] - new_h) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)
    return canvas


def main():
    print("=== Building 21st-Century Idea Icons ===")

    icons = [
        ("scratch/processed/rescue_cutout.png", "VIE_idea_military_rescue"),
        ("scratch/processed/self_reliant_cutout.png", "VIE_idea_self_reliant_deterrence"),
        ("scratch/processed/core_ind_cutout.png", "VIE_idea_def_ind_core"),
        ("scratch/processed/divest_cutout.png", "VIE_idea_def_ind_divest"),
    ]

    for src_path, stem in icons:
        cutout = Image.open(src_path).convert("RGBA")
        canvas = fit_into_idea_canvas(cutout)
        save_idea_dds_and_png(canvas, stem)

    # ----------------------------------------------------
    # Generate interface/VIE_md_ideas.gfx
    # ----------------------------------------------------
    gfx_content = '''spriteTypes = {
	# 21st-Century Vietnam Idea Icons (National Spirits & Government Laws)

	# 1. Binh chung Cuu ho - Cuu nan / Phong thu dan su (Bao Yagi)
	spriteType = {
		name = "GFX_idea_VIE_military_rescue"
		texturefile = "gfx/interface/ideas/VIE_idea_military_rescue.dds"
	}
	spriteType = {
		name = "GFX_idea_generic_military_mission"
		texturefile = "gfx/interface/ideas/VIE_idea_military_rescue.dds"
	}

	# 2. Tu chu Cong nghe Quoc phong & Ran de noi dia
	spriteType = {
		name = "GFX_idea_VIE_self_reliant_deterrence"
		texturefile = "gfx/interface/ideas/VIE_idea_self_reliant_deterrence.dds"
	}

	# 3. Doanh nghiep Quoc phong Nong cot
	spriteType = {
		name = "GFX_idea_VIE_def_ind_core"
		texturefile = "gfx/interface/ideas/VIE_idea_def_ind_core.dds"
	}
	spriteType = {
		name = "GFX_idea_generic_central_planning"
		texturefile = "gfx/interface/ideas/VIE_idea_def_ind_core.dds"
	}

	# 4. Co phan hoa & Thoai von Doanh nghiep
	spriteType = {
		name = "GFX_idea_VIE_def_ind_divest"
		texturefile = "gfx/interface/ideas/VIE_idea_def_ind_divest.dds"
	}
	spriteType = {
		name = "GFX_idea_generic_privatisation"
		texturefile = "gfx/interface/ideas/VIE_idea_def_ind_divest.dds"
	}
}
'''
    GFX_FILE.write_text(gfx_content, encoding="utf-8")
    print(f"  [UPDATED] {GFX_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
