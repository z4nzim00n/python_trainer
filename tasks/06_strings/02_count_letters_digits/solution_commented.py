text = input()

letters = 0
digits = 0
# isalpha и isdigit сами определяют категорию символа.
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
