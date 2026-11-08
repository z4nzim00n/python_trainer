path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    # split без аргумента понимает и пробелы, и переводы строк.
    numbers = list(map(int, text.split()))
    print(f"Sum: {sum(numbers)}")
except FileNotFoundError:
    print("Error: file not found")
