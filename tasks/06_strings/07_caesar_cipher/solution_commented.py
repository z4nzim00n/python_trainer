shift = int(input())
text = input()

result = []
for ch in text:
    if "a" <= ch <= "z":
        # Приводим букву к 0..25, сдвигаем по кругу и возвращаем в алфавит.
        base = ord("a")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    elif "A" <= ch <= "Z":
        base = ord("A")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    else:
        # Пробелы, запятые и другие символы остаются как есть.
        result.append(ch)

print("".join(result))
