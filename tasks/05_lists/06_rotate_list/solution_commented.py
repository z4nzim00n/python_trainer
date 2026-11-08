n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Полные круги не меняют список, поэтому берём остаток.
k %= n
result = numbers[-k:] + numbers[:-k]

print(*result)
