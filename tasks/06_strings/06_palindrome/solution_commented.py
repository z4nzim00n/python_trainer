text = input()

# Сначала убираем регистр, пробелы и знаки препинания.
cleaned = "".join(ch for ch in text.lower() if ch.isalnum())

# Палиндром совпадает со своей перевёрнутой версией.
print(f"Palindrome: {cleaned == cleaned[::-1]}")
