n = int(input())

# // даёт десятки, % — единицы.
tens = n // 10
ones = n % 10
swapped = ones * 10 + tens

print(f"Swapped: {swapped}")
