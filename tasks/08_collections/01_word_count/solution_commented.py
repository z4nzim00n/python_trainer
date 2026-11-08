from collections import Counter

words = input().split()
# Counter сам подсчитывает вхождения каждого слова.
counts = Counter(words)

for word in sorted(counts):
    print(f"{word}: {counts[word]}")
