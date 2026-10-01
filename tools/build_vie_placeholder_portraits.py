"""Generate neutral placeholder portraits for the VIE army and air force commanders added by this submod.

These are NOT likenesses. Each file is a flat silhouette so the character panel is not empty and
HOI4 finds the files the character definitions point at. To use a real photo later, overwrite the
same two files (156x210 large, 38x51 small) and remove the id from PLACEHOLDERS below.

Output format matches the existing submod portraits (gfx/leaders/VIE/Portrait_Le_Xuan_Thuan*.dds):
uncompressed 32-bit BGRA DDS, no mipmaps. Pillow is only used to draw; the DDS header is written here.

Run from anywhere: python tools/build_vie_placeholder_portraits.py
"""
import os
import struct

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_LARGE = os.path.join(ROOT, "gfx", "leaders", "VIE")
OUT_SMALL = os.path.join(OUT_LARGE, "small")

LARGE = (156, 210)
SMALL = (38, 51)
SS = 4  # supersampling factor for smooth edges

PHASE1 = ((75, 90, 60), (34, 42, 28))  # olive: 2000-2014 roster
PHASE2 = ((60, 80, 92), (26, 36, 44))  # slate: 2015-now roster
MODERN = ((98, 64, 58), (44, 28, 26))  # dark red: Corps 12/34 group
AIR = ((70, 112, 152), (28, 48, 70))  # sky blue: Air Defence - Air Force advisors

# file stem (after "Portrait_") -> palette
PLACEHOLDERS = {
    "Le_Van_Dung": PHASE1,
    "Le_Manh": PHASE1,
    "Nguyen_Khac_Nghien": PHASE1,
    "Huynh_Tien_Phong": PHASE1,
    "Nguyen_Van_Duoc": PHASE1,
    "Hoang_Ky": PHASE1,
    "Pham_Xuan_Hung": PHASE1,
    "Nguyen_Phuong_Nam": PHASE2,
    "Vu_Hai_San": PHASE2,
    "Phung_Si_Tan": PHASE2,
    "Nguyen_Doan_Anh": PHASE2,
    "Nguyen_Hong_Thai": PHASE2,
    "Truong_Manh_Dung": MODERN,
    "Nguyen_Duc_Soat": AIR,
    "Nguyen_Van_Than": AIR,
    "Le_Huu_Duc": AIR,
    "Phuong_Minh_Hoa": AIR,
    "Le_Huy_Vinh": AIR,
    "Vu_Van_Kha": AIR,
    "Nguyen_Van_Hien": AIR,
    "Vu_Hong_Son": AIR,
    "Pham_Thanh_Ngan": AIR,
    "Han_Vinh_Tuong": AIR,
    "Pham_Tuan": AIR,
    "Nguyen_Van_Phiet": AIR,
    "Vo_Van_Tuan": AIR,
    "Nguyen_Van_Tho": AIR,
    "Nguyen_Van_Thanh": AIR,
    "Lam_Quang_Dai": AIR,
    "Pham_Van_Tinh": AIR,
    "Tran_Ngoc_Quyen": AIR,
    "Pham_Tuan_Anh": AIR,
    "Bui_Duc_Hien": AIR,
}


def draw_silhouette(size, palette):
    w, h = size
    top, bottom = palette
    img = Image.new("RGBA", (w * SS, h * SS))
    px = img.load()
    for y in range(h * SS):
        t = y / (h * SS - 1)
        row = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)) + (255,)
        for x in range(w * SS):
            px[x, y] = row
    d = ImageDraw.Draw(img)
    cx = w * SS / 2
    uniform = (52, 64, 44, 255)
    skin = (190, 160, 130, 255)
    # shoulders / uniform
    d.ellipse([cx - 0.46 * w * SS, 0.62 * h * SS, cx + 0.46 * w * SS, 1.35 * h * SS], fill=uniform)
    # neck
    d.rectangle([cx - 0.07 * w * SS, 0.50 * h * SS, cx + 0.07 * w * SS, 0.68 * h * SS], fill=skin)
    # head
    d.ellipse([cx - 0.17 * w * SS, 0.22 * h * SS, cx + 0.17 * w * SS, 0.56 * h * SS], fill=skin)
    # cap
    d.pieslice([cx - 0.19 * w * SS, 0.16 * h * SS, cx + 0.19 * w * SS, 0.44 * h * SS], 180, 360, fill=(40, 52, 36, 255))
    d.rectangle([cx - 0.19 * w * SS, 0.29 * h * SS, cx + 0.19 * w * SS, 0.33 * h * SS], fill=(40, 52, 36, 255))
    # collar tab and star
    for sign in (-1, 1):
        d.polygon([(cx + sign * 0.05 * w * SS, 0.68 * h * SS), (cx + sign * 0.16 * w * SS, 0.74 * h * SS),
                   (cx + sign * 0.05 * w * SS, 0.80 * h * SS)], fill=(170, 40, 36, 255))
    return img.resize((w, h), Image.LANCZOS)


def write_dds(path, img):
    w, h = img.size
    r, g, b, a = img.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()  # BGRA byte order, matches masks below
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, h, w, w * 4, 0, 0,
        *([0] * 11),
        32, 0x41,
        0, 32,
        0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000,
        0x1000, 0, 0, 0, 0,
    )
    assert len(header) == 128, len(header)
    with open(path, "wb") as f:
        f.write(header + bytes(data))


def main():
    os.makedirs(OUT_SMALL, exist_ok=True)
    for stem, palette in PLACEHOLDERS.items():
        write_dds(os.path.join(OUT_LARGE, f"Portrait_{stem}.dds"), draw_silhouette(LARGE, palette))
        write_dds(os.path.join(OUT_SMALL, f"Portrait_{stem}_small.dds"), draw_silhouette(SMALL, palette))
        print("wrote", stem)


if __name__ == "__main__":
    main()
