# Разбор задания

## Чтение списка

~~~python
n = int(input())
numbers = list(map(int, input().split()))
~~~

`input().split()` даёт список строк, `map(int, ...)` превращает каждую
в число, `list(...)` собирает результат.

## Готовая функция

~~~python
print(f"Max: {max(numbers)}")
~~~

`max` перебирает элементы и возвращает наибольший. Пустой список вызовет
`ValueError`, но по условию `n >= 1`.

## Своими руками

~~~python
best = numbers[0]
for value in numbers:
    if value > best:
        best = value
~~~

Такая запись показывает, как работает `max` внутри. Она пригодится,
когда нужно найти не значение, а индекс или пару полей.

## Цикл по `range`

Если числа читаются по одному на строку:

~~~python
best = None
for _ in range(n):
    value = int(input())
    if best is None or value > best:
        best = value
~~~

`_` — обычное имя, которым пользуются, когда переменная цикла не нужна.
