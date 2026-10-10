import re
from pathlib import Path

# 1. common/national_focus/VIE_md_focus.txt
focus_path = Path('common/national_focus/VIE_md_focus.txt')
focus_text = focus_path.read_text(encoding='utf-8')

# Find the 4 focuses block
idx_def = focus_text.find('id = VIE_def_industry_law')
if idx_def != -1:
    header_idx = focus_text.rfind('###############################', 0, idx_def)
    idx_capstone = focus_text.find('id = VIE_path_self_reliant_deterrence')
    end_block = focus_text.find('\n\t}\n', idx_capstone) + len('\n\t}\n')
    focus_text = focus_text[:header_idx] + focus_text[end_block:]
    focus_path.write_text(focus_text, encoding='utf-8')
    print("1. Removed 4 defense industry focuses from VIE_md_focus.txt")

# 2. common/decisions/VIE_md_def_industry.txt
Path('common/decisions/VIE_md_def_industry.txt').write_text('# Nhánh quyết định Công nghiệp Quốc phòng đã được xóa.\n', encoding='utf-8')
print("2. Cleared common/decisions/VIE_md_def_industry.txt")

# 3. common/decisions/categories/VIE_md_categories.txt
cat_path = Path('common/decisions/categories/VIE_md_categories.txt')
cat_text = cat_path.read_text(encoding='utf-8')
cat_text = re.sub(r'VIE_def_industry_category\s*=\s*\{[^}]*\}', '', cat_text)
cat_path.write_text(cat_text, encoding='utf-8')
print("3. Removed VIE_def_industry_category from VIE_md_categories.txt")

# 4. common/ideas/VIE_md_ideas_p15.txt
Path('common/ideas/VIE_md_ideas_p15.txt').write_text('# Ideas CNQP da duoc xoa.\nideas = {\n\tcountry = {\n\t}\n}\n', encoding='utf-8')
print("4. Cleared common/ideas/VIE_md_ideas_p15.txt")

# 5. events/VIE_def_ind.txt
Path('events/VIE_def_ind.txt').write_text('add_namespace = vie_def_ind\n# Su kien CNQP da duoc xoa.\n', encoding='utf-8')
print("5. Cleared events/VIE_def_ind.txt")

# 6. common/scripted_effects/VIE_md_effects_p15.txt
Path('common/scripted_effects/VIE_md_effects_p15.txt').write_text('# Scripted effects CNQP da duoc xoa.\n', encoding='utf-8')
print("6. Cleared common/scripted_effects/VIE_md_effects_p15.txt")

# 7. common/scripted_triggers/VIE_md_triggers_p15.txt
Path('common/scripted_triggers/VIE_md_triggers_p15.txt').write_text('# Scripted triggers CNQP da duoc xoa.\n', encoding='utf-8')
print("7. Cleared common/scripted_triggers/VIE_md_triggers_p15.txt")

# 8. Decouple drills decisions from VIE_def_ind_bankrupt
for drill_file in ['common/decisions/VIE_md_decisions_af_drills.txt', 'common/decisions/VIE_md_decisions_nf_drills.txt']:
    p = Path(drill_file)
    content = p.read_text(encoding='utf-8')
    content = content.replace('VIE_def_ind_bankrupt = yes', 'has_active_mission = bankruptcy_incoming_collapse')
    p.write_text(content, encoding='utf-8')
print("8. Decoupled drills decisions from VIE_def_ind_bankrupt")

# 9. common/on_actions/VIE_md_on_actions_startup.txt
startup_path = Path('common/on_actions/VIE_md_on_actions_startup.txt')
startup_text = startup_path.read_text(encoding='utf-8')
# Remove the startup block for VIE_def_industry_level
startup_text = re.sub(r'# VIE_def_industry_level ve 0.*?\bset_country_flag = VIE_def_ind_vars_init \}\s*\}', '', startup_text, flags=re.DOTALL)
startup_path.write_text(startup_text, encoding='utf-8')
print("9. Cleaned startup on_actions")

print("\nSuccessfully executed complete removal of Defense Industry branch!")
