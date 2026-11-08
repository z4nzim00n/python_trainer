from collections import Counter

words = input().split()
counts = Counter(words)

for word in sorted(counts):
    print(f"{word}: {counts[word]}")
