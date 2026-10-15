"""Export the existing document diagram from its SVG, never game artwork.

Only node title metadata and B label text are updated from catalog 16.
All SVG rectangles and paths retain their authored geometry.
The small renderer handles this SVG's actual rect/line/text vocabulary and
fails on unhandled visible elements instead of silently dropping them.
"""
import hashlib
import io
import json
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SVG = "VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.svg"
PNG = "VIE_REGIONAL_DIPLOMACY_LAYOUT_PLAN.png"
NS = "{http://www.w3.org/2000/svg}"
FONT = Path("C:/Windows/Fonts")


def geometry_hash(svg):
    shapes = [(e.tag, sorted(e.attrib.items())) for e in svg.iter()
              if e.tag.rsplit("}", 1)[-1] in ("svg", "rect", "path")]
    return hashlib.sha256(json.dumps(shapes, ensure_ascii=False).encode("utf-8")).hexdigest()


def get_font(size, bold=False):
    return ImageFont.truetype(str(FONT / ("arialbd.ttf" if bold else "arial.ttf")), round(size))


def render_png(svg):
    """Rasterize document SVG primitives, using SVG positions and native size."""
    width, height = int(svg.get("width")), int(svg.get("height"))
    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)
    rules = {}
    for css in svg.iter(NS+"style"):
        for selector, declarations in re.findall(r"([^{}]+)\{([^{}]+)\}", css.text or ""):
            rules[selector.strip()] = dict(part.strip().split(":", 1) for part in declarations.split(";") if part.strip())

    def paint(element):
        tag = element.tag.rsplit("}", 1)[-1]
        style = dict(rules.get(tag, {}))
        for cls in element.get("class", "").split():
            style.update(rules.get("."+cls, {}))
        style.update(element.attrib)
        if tag in ("svg", "g"):
            for child in element:
                paint(child)
        elif tag in ("style", "title"):
            return
        elif tag == "rect":
            x, y = float(style.get("x", 0)), float(style.get("y", 0))
            w = width if style["width"] == "100%" else float(style["width"])
            h = height if style["height"] == "100%" else float(style["height"])
            fill, outline = style.get("fill", "black"), style.get("stroke")
            box = (x, y, x+w, y+h)
            draw.rounded_rectangle(box, radius=float(style.get("rx", 0)),
                                   fill=None if fill == "none" else fill,
                                   outline=outline, width=round(float(style.get("stroke-width", 1))))
        elif tag == "path":
            if not re.fullmatch(r"[\d.\sML-]+", style["d"]):
                raise ValueError("Unsupported document path: "+style["d"])
            coordinates = list(map(float, re.findall(r"-?\d+(?:\.\d+)?", style["d"])))
            if len(coordinates) != 4:
                raise ValueError("Expected one straight document edge")
            x0,y0,x1,y1 = coordinates
            line_width = round(float(style.get("stroke-width", 1)))
            stroke = style.get("stroke", "black")
            dash = list(map(float, style.get("stroke-dasharray", "").split()))
            if not dash:
                draw.line((x0,y0,x1,y1), fill=stroke, width=line_width)
            else:
                if len(dash) != 2 or min(dash) <= 0:
                    raise ValueError("Unsupported dash array")
                length = math.hypot(x1-x0,y1-y0)
                at = 0
                while at < length:
                    stop = min(length, at+dash[0])
                    draw.line((x0+(x1-x0)*at/length,y0+(y1-y0)*at/length,
                               x0+(x1-x0)*stop/length,y0+(y1-y0)*stop/length),fill=stroke,width=line_width)
                    at += sum(dash)
        elif tag == "text":
            anchor = {"middle":"ms","start":"ls","end":"rs"}[style.get("text-anchor","start")]
            draw.text((float(style["x"]),float(style["y"])),element.text or "",
                      font=get_font(float(style.get("font-size",12)),style.get("font-weight")=="bold"),
                      fill=style.get("fill","black"),anchor=anchor)
        else:
            raise ValueError("Unsupported visible SVG element "+tag)
    paint(svg)
    output = io.BytesIO()
    canvas.save(output, format="PNG", optimize=True)
    return output.getvalue()


def export_layout(root, catalog, renamed_nodes):
    path = root/SVG
    svg = ET.fromstring(path.read_text(encoding="utf-8"))
    before = geometry_hash(svg)
    for group in svg.findall(NS+"g"):
        title = group.find(NS+"title")
        if title is None:
            continue
        node = title.text.split(":",1)[0]
        data = catalog[node]
        title.text = f"{node}: {data['name']} | prerequisite: {data['prereq']} | {data['available']}"
        if node not in renamed_nodes:
            continue
        texts = group.findall(NS+"text")
        template = dict(texts[1].attrib)
        for item in texts[1:]:
            group.remove(item)
        rect = group.find(NS+"rect")
        max_width = float(rect.get("width"))-8
        for size in (12,11):
            font = get_font(size)
            lines = [""]
            for word in data["name"].split():
                proposed = (lines[-1]+" "+word).strip()
                if font.getlength(proposed) <= max_width:
                    lines[-1] = proposed
                else:
                    lines.append(word)
            if len(lines) <= 3:
                break
        if len(lines)>3:
            raise ValueError("Document label does not fit "+node)
        for index,line in enumerate(lines):
            attrs = dict(template)
            attrs["y"] = str(float(template["y"])+index*13)
            attrs["font-size"] = str(size)
            item = ET.SubElement(group,NS+"text",attrs)
            item.text = line
    if before != geometry_hash(svg):
        raise AssertionError("Export changed authored diagram geometry")
    ET.register_namespace("","http://www.w3.org/2000/svg")
    path.write_bytes(ET.tostring(svg,encoding="utf-8",xml_declaration=True))
    (root/PNG).write_bytes(render_png(svg))
    return dict(width=int(svg.get("width")),height=int(svg.get("height")),geometry_sha256=before)
