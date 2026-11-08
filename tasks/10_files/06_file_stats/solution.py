path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Chars: {char_count}")
except FileNotFoundError:
    print("Error: file not found")
