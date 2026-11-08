n = int(input())
numbers = list(map(int, input().split()))

# Срез с шагом -1 создаёт развёрнутую копию, * распаковывает её в print.
print(*numbers[::-1])
