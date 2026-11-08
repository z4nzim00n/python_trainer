# Разбор задания

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
