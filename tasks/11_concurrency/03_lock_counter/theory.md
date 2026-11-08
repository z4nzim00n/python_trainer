# Разбор задания

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
