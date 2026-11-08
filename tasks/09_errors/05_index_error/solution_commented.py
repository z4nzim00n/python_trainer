n, index = map(int, input().split())
numbers = list(map(int, input().split()))

try:
    print(f"Value: {numbers[index]}")
except IndexError:
    # Индекс вышел за допустимый диапазон.
    print("Error: index out of range")
