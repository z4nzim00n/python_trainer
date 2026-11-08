a, b = map(int, input().split())

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: division by zero")
