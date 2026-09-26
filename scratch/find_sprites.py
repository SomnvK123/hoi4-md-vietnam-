import glob, re

MD = 'D:/SteamLibrary/steamapps/workshop/content/394360/2777392649'
sprites = set()
for q in glob.glob(MD + '/interface/**/*.gfx', recursive=True) + glob.glob('D:/SteamLibrary/steamapps/common/Hearts of Iron IV/interface/**/*.gfx', recursive=True) + glob.glob('interface/**/*.gfx', recursive=True):
    sprites |= set(re.findall(r'name = "(\w+)"', open(q, encoding='utf-8-sig', errors='ignore').read()))

test = ['trade_with_america', 'GFX_focus_generic_industry_2', 'GFX_focus_generic_industry_3', 'GFX_focus_generic_diplomatic_treaty', 'focus_generic_industry_investment']
for t in test:
    print(t, '->', t in sprites)
