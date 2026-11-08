import threading

threads_count, increments = map(int, input().split())

counter = 0
lock = threading.Lock()


def worker():
    # global нужен, чтобы менять переменную модуля, а не локальную.
    global counter
    for _ in range(increments):
        # with lock делает чтение и запись неделимыми.
        with lock:
            counter += 1


threads = [threading.Thread(target=worker) for _ in range(threads_count)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Counter: {counter}")
