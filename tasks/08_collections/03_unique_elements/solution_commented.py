n = int(input())
numbers = list(map(int, input().split()))

# set убирает повторы, sorted возвращает порядок.
unique = sorted(set(numbers))
print("Unique:", *unique)
