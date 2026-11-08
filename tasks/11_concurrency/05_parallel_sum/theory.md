# Разбор задания

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
