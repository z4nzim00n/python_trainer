n = int(input())
numbers = list(map(int, input().split()))

total = sum(numbers)
average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
