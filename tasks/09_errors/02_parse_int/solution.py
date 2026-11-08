line = input()

try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    print("Error: invalid number")
