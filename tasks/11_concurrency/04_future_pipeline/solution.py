from concurrent.futures import ThreadPoolExecutor


def square(value):
    return value * value


n = int(input())

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(square, i) for i in range(1, n + 1)]
    results = [future.result() for future in futures]

print("Results:", *results)
