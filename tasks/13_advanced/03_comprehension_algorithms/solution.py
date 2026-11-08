n = int(input())
numbers = list(map(int, input().split()))

result = sum(x * x for x in numbers if x % 2 == 0)
print(f"Sum: {result}")
