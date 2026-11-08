n = int(input())
numbers = list(map(int, input().split()))

# sorted возвращает новый отсортированный список.
print(*sorted(numbers))
