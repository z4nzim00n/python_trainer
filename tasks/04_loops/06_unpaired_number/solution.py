n = int(input())
numbers = list(map(int, input().split()))

result = 0
for value in numbers:
    result ^= value

print(f"Unpaired: {result}")
