import sys

path = input()

try:
    # with закроет файл автоматически.
    with open(path, encoding="utf-8") as file:
        text = file.read()
    # write не добавляет свой перевод строки — вывод совпадает с файлом.
    sys.stdout.write(text)
except FileNotFoundError:
    print("Error: file not found")
