with open('scratch/extracted_new_naval_chat.md', 'r', encoding='utf-8') as f:
    text = f.read()

chunks = text.split('<!-- String ')
sorted_chunks = sorted(chunks[1:], key=lambda c: len(c), reverse=True)

with open('scratch/clean_new_naval_proposal.txt', 'w', encoding='utf-8') as out:
    for i, c in enumerate(sorted_chunks[:5]):
        out.write(f"\n\n==================== RANK {i+1} (len: {len(c)}) ====================\n\n")
        out.write(c)

print("Saved top chunks to scratch/clean_new_naval_proposal.txt")
