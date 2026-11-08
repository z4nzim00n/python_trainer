text = input()

cleaned = "".join(ch for ch in text.lower() if ch.isalnum())
print(f"Palindrome: {cleaned == cleaned[::-1]}")
