import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

HTML_DATA = [
    {"id": "N00", "row": 0, "x": 1450},
    {"id": "T01", "row": 1, "x": 960},
    {"id": "I01", "row": 1, "x": 1940},
    {"id": "S01", "row": 2, "x": 345},
    {"id": "T02", "row": 2, "x": 730},
    {"id": "T03", "row": 2, "x": 1100},
    {"id": "L01", "row": 2, "x": 1470},
    {"id": "I02", "row": 2, "x": 1840},
    {"id": "I03", "row": 2, "x": 2220},
    {"id": "S02", "row": 3, "x": 205},
    {"id": "S03", "row": 3, "x": 520},
    {"id": "W01", "row": 3, "x": 835},
    {"id": "W04", "row": 3, "x": 1150},
    {"id": "T04", "row": 3, "x": 1465},
    {"id": "L02", "row": 3, "x": 1780},
    {"id": "L03", "row": 3, "x": 2095},
    {"id": "I04", "row": 3, "x": 2410},
    {"id": "S04", "row": 4, "x": 525},
    {"id": "W02", "row": 4, "x": 850},
    {"id": "W03", "row": 4, "x": 1180},
    {"id": "L04", "row": 4, "x": 1925},
    {"id": "S05", "row": 5, "x": 525},
    {"id": "W05", "row": 5, "x": 1180},
    {"id": "L05", "row": 5, "x": 1925},
    {"id": "P01", "row": 6, "x": 865},
    {"id": "H01", "row": 6, "x": 1650},
    {"id": "P02", "row": 7, "x": 640},
    {"id": "P03", "row": 7, "x": 965},
    {"id": "H02", "row": 7, "x": 1650},
    {"id": "P04", "row": 8, "x": 640},
    {"id": "G01", "row": 8, "x": 1480},
    {"id": "B01", "row": 8, "x": 1930},
    {"id": "P05", "row": 9, "x": 865},
    {"id": "G02", "row": 9, "x": 1480},
    {"id": "B02", "row": 9, "x": 1930},
    {"id": "P06", "row": 10, "x": 865},
    {"id": "G03", "row": 10, "x": 1480},
    {"id": "B03", "row": 10, "x": 1930},
    {"id": "F01", "row": 11, "x": 1460},
    {"id": "F02", "row": 12, "x": 1460}
]

# Look at alignment in HTML:
# S04 & S05 have same x (525)
# W03 & W05 have same x (1180)
# L04 & L05 have same x (1925)
# P02 & P04 have same x (640)
# P01, P05, P06 have same x (865)
# H01 & H02 have same x (1650)
# G01, G02, G03 have same x (1480)
# B01, B02, B03 have same x (1930)
# F01 & F02 have same x (1460)

# Let's see the columns in HTML:
# Distinct x positions:
unique_x = sorted(list(set(n['x'] for n in HTML_DATA)))
print("Unique X in HTML:", unique_x)
print(f"Number of distinct X: {len(unique_x)}")

# Let's map unique X to HOI4 grid where N00 is around 210 or 212.
# Let's test a scaling factor: (x - 1450) / scale + center
# If scale = 110:
# 205 -> (205-1450)/110 = -11.3 -> 210 - 11 = 199
# 2410 -> (2410-1450)/110 = +8.7 -> 210 + 9 = 219
# Total width = 219 - 199 = 20 units.
