from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counts = Counter(numbers)

for value in sorted(counts):
    # Умножение строки повторяет её нужное число раз.
    print(f"{value}: {'*' * counts[value]}")
