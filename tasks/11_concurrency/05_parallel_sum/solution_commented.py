import threading

n = int(input())
numbers = list(map(int, input().split()))

middle = n // 2
# Каждый поток пишет в свою ячейку, поэтому замок не нужен.
partial = [0, 0]


def add(index, values):
    partial[index] = sum(values)


t1 = threading.Thread(target=add, args=(0, numbers[:middle]))
t2 = threading.Thread(target=add, args=(1, numbers[middle:]))
t1.start()
t2.start()
t1.join()
t2.join()

print(f"Sum: {partial[0] + partial[1]}")
