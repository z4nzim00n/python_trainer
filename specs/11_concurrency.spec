@@TASK
section: 11_concurrency
dir: 01_thread_basics
num: 11_1
title: PY_11_01. Первый поток
topics: `threading.Thread`, `start`, `join`
input: Не требуются
@@DESC
Запусти поток, который печатает `Hello from thread`, дождись его
завершения и напечатай `Main done`:

~~~text
Hello from thread
Main done
~~~
@@EXAMPLES
| *(нет ввода)* | `Hello from thread`<br>`Main done` |
@@THEORY
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
@@TESTS
| (пустой ввод) | `Hello from thread\nMain done\n` |
@@CASES
run_case_devnull $'Hello from thread\nMain done\n'
@@MAIN
import threading

# TODO: запусти поток, дождись его и выведи Main done
print("TODO")
@@SOLUTION
import threading


def worker():
    print("Hello from thread")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
print("Main done")
@@COMMENTED
import threading


def worker():
    print("Hello from thread")


thread = threading.Thread(target=worker)
thread.start()
# join гарантирует, что поток закончит до следующей строки.
thread.join()
print("Main done")
@@END

@@TASK
section: 11_concurrency
dir: 02_two_threads
num: 11_2
title: PY_11_02. Два потока
topics: `Thread`, `args`, общий список
input: Два целых числа `a` и `b`
@@DESC
Посчитай квадраты `a` и `b` в двух разных потоках. Выведи результаты:

~~~text
A: 4
B: 9
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2 3` | `A: 4`<br>`B: 9` |
| `-4 5` | `A: 16`<br>`B: 25` |
@@THEORY
## Результаты в разных ячейках

~~~python
results = [0, 0]

def square(index, value):
    results[index] = value * value

t1 = threading.Thread(target=square, args=(0, a))
t2 = threading.Thread(target=square, args=(1, b))
t1.start()
t2.start()
t1.join()
t2.join()
~~~

Каждый поток пишет в свою ячейку. Гонки за одну переменную нет.

## Почему это безопасно

Потоки не изменяют одну и ту же память на запись. После `join` обе
записи видны главному потоку.

## Порядок печати

Печатает только главный поток, поэтому `A:` всегда идёт перед `B:`,
хотя вычисления выполнялись параллельно.

## Замыкания

Функция `square` не захватывает `a` и `b` — они передаются через `args`.
Так код проще и надёжнее.

## GIL

Из-за глобальной блокировки интерпретатора два потока не выполняют
Python-байткод одновременно. Но для коротких задач и операций ввода-вывода
потоки всё равно полезны.
@@TESTS
| `2 3` | `A: 4\nB: 9\n` |
| `-4 5` | `A: 16\nB: 25\n` |
| `0 0` | `A: 0\nB: 0\n` |
@@CASES
run_case "2 3" $'A: 4\nB: 9\n'
run_case "-4 5" $'A: 16\nB: 25\n'
run_case "0 0" $'A: 0\nB: 0\n'
@@MAIN
import threading

a, b = map(int, input().split())

# TODO: посчитай квадраты в двух потоках
print("TODO")
@@SOLUTION
import threading

a, b = map(int, input().split())

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
@@COMMENTED
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
@@END

@@TASK
section: 11_concurrency
dir: 03_lock_counter
num: 11_3
title: PY_11_03. Счётчик с замком
topics: `Lock`, `with lock`, гонка данных
input: Количество потоков и число прибавлений
@@DESC
Запусти указанное число потоков. Каждый поток увеличивает общий счётчик
заданное число раз. Выведи итог:

~~~text
Counter: <значение>
~~~

Используй `threading.Lock`, чтобы прибавления не терялись.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4 1000` | `Counter: 4000` |
| `2 5` | `Counter: 10` |
@@THEORY
## Гонка данных

Операция `counter += 1` состоит из трёх шагов: прочитать, прибавить,
записать. Если два потока выполнят их одновременно, одно прибавление
может потеряться.

## `Lock`

~~~python
lock = threading.Lock()

def worker():
    global counter
    for _ in range(increments):
        with lock:
            counter += 1
~~~

`with lock` захватывает замок на время блока. Второй поток ждёт, пока
первый не освободит его.

## `global`

Внутри функции `counter += 1` создала бы локальную переменную. `global`
указывает, что меняется переменная модуля.

## Создание потоков

~~~python
threads = [threading.Thread(target=worker) for _ in range(count)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
~~~

Сначала запускаем все, потом ждём все — так потоки работают параллельно.

## Альтернатива

~~~python
lock = threading.Lock()
with lock:
    ...
~~~

Или `counter = itertools.count()` и `next(counter)` — многие операции
атомарны. Но явный `Lock` нагляднее.

## Без замка

Итог может оказаться меньше ожидаемого, причём нестабильно. Такие
ошибки трудно воспроизвести.
@@TESTS
| `4 1000` | `Counter: 4000\n` |
| `2 5` | `Counter: 10\n` |
| `1 0` | `Counter: 0\n` |
@@CASES
run_case "4 1000" $'Counter: 4000\n'
run_case "2 5" $'Counter: 10\n'
run_case "1 0" $'Counter: 0\n'
@@MAIN
import threading

threads_count, increments = map(int, input().split())

counter = 0
lock = threading.Lock()

# TODO: запусти потоки, которые увеличивают counter под замком
print("TODO")
@@SOLUTION
import threading

threads_count, increments = map(int, input().split())

counter = 0
lock = threading.Lock()


def worker():
    global counter
    for _ in range(increments):
        with lock:
            counter += 1


threads = [threading.Thread(target=worker) for _ in range(threads_count)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Counter: {counter}")
@@COMMENTED
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
@@END

@@TASK
section: 11_concurrency
dir: 04_future_pipeline
num: 11_4
title: PY_11_04. Пул потоков
topics: `ThreadPoolExecutor`, `submit`, `Future.result`
input: Одно целое число `n`
@@DESC
Вычисли квадраты чисел от `1` до `n` в пуле потоков. Выведи результаты
в порядке возрастания чисел:

~~~text
Results: 1 4 9 ...
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3` | `Results: 1 4 9` |
| `5` | `Results: 1 4 9 16 25` |
@@THEORY
## Пул потоков

~~~python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(square, i) for i in range(1, n + 1)]
    results = [future.result() for future in futures]
~~~

`submit` ставит функцию в очередь и возвращает `Future` — обещание
результата. `result()` ждёт завершения и возвращает значение.

## Порядок

`futures` хранятся в порядке отправки, поэтому `results` тоже идут
по порядку, даже если задачи завершились в другом порядке.

## `map`

~~~python
with ThreadPoolExecutor() as executor:
    results = list(executor.map(square, range(1, n + 1)))
~~~

Короче, если аргументы берутся из одного итерируемого объекта.

## Контекстный менеджер

`with ThreadPoolExecutor(...)` дожидается завершения задач при выходе.
Без `with` нужно вызывать `shutdown`.

## Исключения

Если задача бросила исключение, `future.result()` пробросит его в
вызывающий поток.

## GIL

Пул удобен для ввода-вывода. Для тяжёлых вычислений на чистом Python
используют `ProcessPoolExecutor`: процессы обходят GIL.
@@TESTS
| `3` | `Results: 1 4 9\n` |
| `5` | `Results: 1 4 9 16 25\n` |
| `1` | `Results: 1\n` |
@@CASES
run_case "3" $'Results: 1 4 9\n'
run_case "5" $'Results: 1 4 9 16 25\n'
run_case "1" $'Results: 1\n'
@@MAIN
from concurrent.futures import ThreadPoolExecutor

n = int(input())

# TODO: посчитай квадраты в пуле и выведи их по порядку
print("TODO")
@@SOLUTION
from concurrent.futures import ThreadPoolExecutor


def square(value):
    return value * value


n = int(input())

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(square, i) for i in range(1, n + 1)]
    results = [future.result() for future in futures]

print("Results:", *results)
@@COMMENTED
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
@@END

@@TASK
section: 11_concurrency
dir: 05_parallel_sum
num: 11_5
title: PY_11_05. Параллельная сумма
topics: `Thread`, части списка, `sum`
input: Число `n`, затем `n` целых чисел
@@DESC
Раздели список на две половины и посчитай суммы в двух потоках.
Выведи общую сумму:

~~~text
Sum: <сумма>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `6`<br>`1 2 3 4 5 6` | `Sum: 21` |
| `1`<br>`10` | `Sum: 10` |
@@THEORY
## Разбиение

~~~python
middle = n // 2
left = numbers[:middle]
right = numbers[middle:]
~~~

Для нечётного `n` левая часть короче на один — это нормально.

## Потоки

~~~python
partial = [0, 0]

def add(index, values):
    partial[index] = sum(values)

t1 = threading.Thread(target=add, args=(0, left))
t2 = threading.Thread(target=add, args=(1, right))
t1.start()
t2.start()
t1.join()
t2.join()
~~~

Каждый поток пишет в свою ячейку, главный — складывает результаты.

## Пустая часть

Для `n = 1` левая часть пуста, `sum([])` равен `0`. Ошибки нет.

## Итог

~~~python
print(f"Sum: {partial[0] + partial[1]}")
~~~

## Стоит ли так делать

Для суммы это учебный пример: `sum(numbers)` быстрее. Потоки оправданы,
когда части считаются долго и независимо. Из-за GIL чистые вычисления
на Python не ускоряются — нужны процессы.
@@TESTS
| `6\n1 2 3 4 5 6` | `Sum: 21\n` |
| `1\n10` | `Sum: 10\n` |
| `5\n-1 1 -2 2 0` | `Sum: 0\n` |
@@CASES
run_case $'6\n1 2 3 4 5 6' $'Sum: 21\n'
run_case $'1\n10' $'Sum: 10\n'
run_case $'5\n-1 1 -2 2 0' $'Sum: 0\n'
@@MAIN
import threading

n = int(input())
numbers = list(map(int, input().split()))

# TODO: посчитай суммы двух половин в потоках и выведи общую
print("TODO")
@@SOLUTION
import threading

n = int(input())
numbers = list(map(int, input().split()))

middle = n // 2
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
@@COMMENTED
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
@@END
