n, index = map(int, input().split())
numbers = list(map(int, input().split()))

try:
    print(f"Value: {numbers[index]}")
except IndexError:
    print("Error: index out of range")
