words = input().split()

groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)

for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
