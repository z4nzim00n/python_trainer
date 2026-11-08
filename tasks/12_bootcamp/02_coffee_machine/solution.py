price = int(input())
coins = list(map(int, input().split()))

paid = 0
for coin in coins:
    if coin == 0:
        break
    paid += coin

if paid >= price:
    print(f"Change: {paid - price}")
else:
    print(f"Need: {price - paid}")
