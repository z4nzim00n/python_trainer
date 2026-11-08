a, b = map(int, input().split())

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    # Сюда управление попадает только при b == 0.
    print("Error: division by zero")
