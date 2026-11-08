source = input()
destination = input()

try:
    with open(source, encoding="utf-8") as src:
        text = src.read()

    # Новый файл создаётся в режиме "w".
    with open(destination, "w", encoding="utf-8") as dst:
        dst.write(text)

    print(f"Copied: {source} -> {destination}")
except FileNotFoundError:
    print("Error: file not found")
