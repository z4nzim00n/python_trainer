class NegativeAgeError(Exception):
    pass


age = int(input())

try:
    if age < 0:
        # raise прерывает try и передаёт управление в except.
        raise NegativeAgeError("negative age")
    print(f"Age: {age}")
except NegativeAgeError:
    print("Error: negative age")
