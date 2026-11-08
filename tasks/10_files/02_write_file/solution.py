path = input()
text = input()

with open(path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Written: {path}")
