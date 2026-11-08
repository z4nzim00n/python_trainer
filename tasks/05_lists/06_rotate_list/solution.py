n, k = map(int, input().split())
numbers = list(map(int, input().split()))

k %= n
result = numbers[-k:] + numbers[:-k]

print(*result)
