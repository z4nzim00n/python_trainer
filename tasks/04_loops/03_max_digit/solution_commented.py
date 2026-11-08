n = abs(int(input()))

best = 0
while n > 0:
    digit = n % 10
    # Обновляем максимум, только если цифра больше.
    if digit > best:
        best = digit
    n //= 10

print(f"Max digit: {best}")
