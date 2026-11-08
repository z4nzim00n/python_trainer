n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

result = [
    [x + y for x, y in zip(row_a, row_b)]
    for row_a, row_b in zip(a, b)
]

for row in result:
    print(*row)
