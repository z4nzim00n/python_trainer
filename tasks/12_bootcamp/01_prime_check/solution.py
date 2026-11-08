n = int(input())

is_prime = n >= 2
d = 2
while d * d <= n:
    if n % d == 0:
        is_prime = False
        break
    d += 1

print(f"Prime: {is_prime}")
