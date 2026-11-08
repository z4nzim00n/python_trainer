import threading

a, b = map(int, input().split())

# Каждый поток пишет в свою ячейку — общая память не конфликтует.
results = [0, 0]


def square(index, value):
    results[index] = value * value


t1 = threading.Thread(target=square, args=(0, a))
t2 = threading.Thread(target=square, args=(1, b))
t1.start()
t2.start()
t1.join()
t2.join()

print(f"A: {results[0]}")
print(f"B: {results[1]}")
