n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Сначала переворачиваем строки, затем транспонируем.
rotated = [list(row) for row in zip(*matrix[::-1])]

for row in rotated:
    print(*row)
