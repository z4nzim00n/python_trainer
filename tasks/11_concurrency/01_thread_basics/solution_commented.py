import threading


def worker():
    print("Hello from thread")


thread = threading.Thread(target=worker)
thread.start()
# join гарантирует, что поток закончит до следующей строки.
thread.join()
print("Main done")
