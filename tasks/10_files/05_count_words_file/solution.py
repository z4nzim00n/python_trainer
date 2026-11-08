path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    print(f"Words: {len(words)}")
except FileNotFoundError:
    print("Error: file not found")
