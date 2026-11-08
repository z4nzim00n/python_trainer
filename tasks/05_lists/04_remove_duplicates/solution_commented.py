n = int(input())
numbers = list(map(int, input().split()))

# seen отвечает за проверку, result хранит порядок первого появления.
seen = set()
result = []
for value in numbers:
    if value not in seen:
        seen.add(value)
        result.append(value)

print(*result)
