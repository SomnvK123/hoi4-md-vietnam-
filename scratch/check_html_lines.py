import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# HTML DATA definitions
HTML_NODES = {
    "N00": {"lines": [], "extra": [], "mut": []},
    "T01": {"lines": ["N00"], "extra": [], "mut": []},
    "I01": {"lines": ["N00"], "extra": [], "mut": []},
    "S01": {"lines": ["T01"], "extra": [], "mut": []},
    "T02": {"lines": ["T01"], "extra": [], "mut": []},
    "T03": {"lines": ["T01"], "extra": [], "mut": []},
    "L01": {"lines": ["T01"], "extra": [], "mut": []},
    "I02": {"lines": ["I01"], "extra": [], "mut": []},
    "I03": {"lines": ["I01"], "extra": [], "mut": []},
    "S02": {"lines": ["S01"], "extra": [], "mut": []},
    "S03": {"lines": ["S01"], "extra": [], "mut": []},
    "W01": {"lines": ["T02"], "extra": [], "mut": []},
    "W04": {"lines": ["T02"], "extra": [], "mut": []},
    "T04": {"lines": ["T03"], "extra": ["T02"], "mut": []},
    "L02": {"lines": ["L01"], "extra": [], "mut": []},
    "L03": {"lines": ["L01"], "extra": [], "mut": []},
    "I04": {"lines": ["I02", "I03"], "extra": [], "mut": []},
    "S04": {"lines": ["S03"], "extra": ["S02"], "mut": []},
    "W02": {"lines": ["W01"], "extra": [], "mut": []},
    "W03": {"lines": ["W01"], "extra": [], "mut": []},
    "L04": {"lines": ["L02", "L03"], "extra": [], "mut": []},
    "S05": {"lines": ["S04"], "extra": [], "mut": []},
    "W05": {"lines": ["W03"], "extra": ["S03"], "mut": []},
    "L05": {"lines": ["L04"], "extra": [], "mut": []},
    "P01": {"lines": ["T04"], "extra": ["W01"], "mut": ["H01"]},
    "H01": {"lines": ["T04"], "extra": ["W01"], "mut": ["P01"]},
    "P02": {"lines": ["P01"], "extra": ["S02"], "mut": []},
    "P03": {"lines": ["P01"], "extra": ["L03"], "mut": []},
    "H02": {"lines": ["H01"], "extra": ["W03", "L02"], "mut": []},
    "P04": {"lines": ["P02"], "extra": [], "mut": []},
    "G01": {"lines": ["H02"], "extra": [], "mut": ["B01"]},
    "B01": {"lines": ["H02"], "extra": ["L05"], "mut": ["G01"]},
    "P05": {"lines": ["P04"], "extra": ["P03"], "mut": []},
    "G02": {"lines": ["G01"], "extra": ["W05"], "mut": []},
    "B02": {"lines": ["B01"], "extra": ["S04"], "mut": []},
    "P06": {"lines": ["P05"], "extra": [], "mut": []},
    "G03": {"lines": ["G02"], "extra": ["L03"], "mut": []},
    "B03": {"lines": ["B02"], "extra": [], "mut": []},
    "F01": {"lines": ["P06|G03|B03"], "extra": [], "mut": []},
    "F02": {"lines": ["F01"], "extra": ["S05", "L05"], "mut": []}
}

print("=== SO SÁNH THIẾT KẾ HTML LINES & EXTRA ===")
for nid, data in HTML_NODES.items():
    print(f"{nid:4}: lines (VẼ ĐƯỜNG) = {data['lines']}, extra (ẨN ĐƯỜNG) = {data['extra']}, mut = {data['mut']}")
