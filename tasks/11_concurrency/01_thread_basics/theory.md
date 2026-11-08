# Разбор задания

## Поток

~~~python
import threading

def worker():
    print("Hello from thread")

thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("Main done")
~~~

`Thread` принимает функцию через `target`. `start` запускает её
в отдельном потоке.

## `join`

`join` блокирует главный поток, пока рабочий не завершится. Без него
порядок строк был бы случайным: `Main done` могла бы напечататься
раньше.

## Аргументы

~~~python
def worker(name):
    print(f"Hello, {name}")

thread = threading.Thread(target=worker, args=("Ada",))
~~~

`args` — кортеж. Для одного аргумента нужна запятая: `("Ada",)`.

## Daemon-потоки

~~~python
thread = threading.Thread(target=worker, daemon=True)
~~~

Демон не мешает программе завершиться. Обычный поток программа ждёт.

## Когда потоки полезны

Для сетевых запросов и файловых операций: пока один поток ждёт ответа,
другой работает. Для чистых вычислений в Python есть GIL — об этом
в задаче про пул.
