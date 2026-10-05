import glob, re

MD = 'D:/SteamLibrary/steamapps/workshop/content/394360/2777392649'
sprites = set()
for q in glob.glob(MD + '/interface/**/*.gfx', recursive=True) + glob.glob('D:/SteamLibrary/steamapps/common/Hearts of Iron IV/interface/**/*.gfx', recursive=True) + glob.glob('interface/**/*.gfx', recursive=True):
    sprites |= set(re.findall(r'name = "(\w+)"', open(q, encoding='utf-8-sig', errors='ignore').read()))

selected_icons = [
    'legislative_palace',
    'Generic_Political_Purge',
    'propaganda',
    'communist_purge',
    'focus_generic_central_planning',
    'economic_civil_industry',
    'economic_prosperity',
    'asian_investment',
    'anti_corruption',
    'five_year_plan',
    'GFX_focus_generic_military_mission',
    'army_cyberwar',
    'GFX_focus_AFG_education_reform',
    'sov_free_media',
    'treaty2',
    'diplomatic_treaty',
    'diplomacy',
    'economic_prosperity2',
    'election2',
]

all_ok = True
for ic in selected_icons:
    ok = ic in sprites
    print(f"{ic} -> {ok}")
    if not ok:
        all_ok = False

print("All ok?", all_ok)
