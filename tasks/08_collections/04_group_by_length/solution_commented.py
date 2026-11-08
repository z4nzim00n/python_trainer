words = input().split()

# setdefault создаёт список для новой длины и возвращает его.
groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)

for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
