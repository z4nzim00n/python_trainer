n = int(input())
numbers = list(map(int, input().split()))

# Пары одинаковых чисел дают 0, поэтому остаётся только непарное.
result = 0
for value in numbers:
    result ^= value

print(f"Unpaired: {result}")
