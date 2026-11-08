import threading


def worker():
    print("Hello from thread")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("Main done")
