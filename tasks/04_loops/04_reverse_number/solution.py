number = int(input())

sign = -1 if number < 0 else 1
n = abs(number)

result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10

print(f"Reversed: {sign * result}")
