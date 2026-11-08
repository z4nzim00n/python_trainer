data = {"name": "Ada", "lang": "Python", "year": "1991"}

key = input()

# in проверяет именно ключи словаря.
if key in data:
    print(f"Value: {data[key]}")
else:
    print("Value: Not found")
