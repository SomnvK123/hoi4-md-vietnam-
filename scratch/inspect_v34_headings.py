import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/clean_new_naval_proposal.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('==================== RANK 2')
rank2_text = text[idx:]

import re
headings = re.findall(r'(#{1,4}\s+[^\n]+)', rank2_text)
print(f"Total headings in Rank 2: {len(headings)}")
for h in headings:
    print(h)
