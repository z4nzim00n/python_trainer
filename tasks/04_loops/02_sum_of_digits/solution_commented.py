n = abs(int(input()))

total = 0
# На каждом шаге добавляем последнюю цифру и отбрасываем её.
while n > 0:
    total += n % 10
    n //= 10

print(f"Sum: {total}")
