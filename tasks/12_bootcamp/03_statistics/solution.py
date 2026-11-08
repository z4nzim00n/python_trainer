n = int(input())
numbers = list(map(int, input().split()))

count = len(numbers)
total = sum(numbers)
lowest = min(numbers)
highest = max(numbers)
average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Min: {lowest}")
print(f"Max: {highest}")
print(f"Average: {average:.2f}")
