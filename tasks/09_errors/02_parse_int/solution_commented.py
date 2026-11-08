line = input()

try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    # int бросает ValueError, если строка не является целым числом.
    print("Error: invalid number")
