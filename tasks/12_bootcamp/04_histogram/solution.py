from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counts = Counter(numbers)

for value in sorted(counts):
    print(f"{value}: {'*' * counts[value]}")
