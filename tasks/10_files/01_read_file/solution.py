import sys

path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    sys.stdout.write(text)
except FileNotFoundError:
    print("Error: file not found")
