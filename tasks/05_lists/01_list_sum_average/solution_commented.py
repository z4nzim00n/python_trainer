n = int(input())
numbers = list(map(int, input().split()))

total = sum(numbers)
# / всегда возвращает float, поэтому среднее можно печатать с .2f.
average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
