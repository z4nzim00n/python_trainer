n = int(input())

# Значением обратного словаря будет список ключей.
inverted = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    inverted.setdefault(value, []).append(key)

for value in sorted(inverted):
    print(f"{value}: {' '.join(inverted[value])}")
