with open('scratch/clean_new_naval_proposal.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('==================== RANK 2')
rank2_text = text[idx:]
# remove the header
lines = rank2_text.splitlines()
start_line = 0
for i, l in enumerate(lines):
    if l.startswith('# V34'):
        start_line = i
        break

content = '\n'.join(lines[start_line:])
# find end of first article
end_idx = content.find('==================== RANK')
if end_idx != -1:
    content = content[:end_idx]

with open('scratch/v34_full_proposal.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Saved full proposal to scratch/v34_full_proposal.md, len={len(content)}")
