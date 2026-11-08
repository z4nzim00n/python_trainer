n = int(input())
numbers = list(map(int, input().split()))

# min и max перебирают весь список.
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
