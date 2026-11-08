from concurrent.futures import ThreadPoolExecutor


def square(value):
    return value * value


n = int(input())

with ThreadPoolExecutor(max_workers=4) as executor:
    # submit возвращает Future — результат появится позже.
    futures = [executor.submit(square, i) for i in range(1, n + 1)]
    # result ждёт завершения конкретной задачи.
    results = [future.result() for future in futures]

print("Results:", *results)
