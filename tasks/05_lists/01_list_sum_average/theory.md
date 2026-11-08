# Разбор задания

## Список

~~~python
numbers = list(map(int, input().split()))
~~~

`list` — изменяемая последовательность. К элементам обращаются по индексу:
`numbers[0]`, `numbers[-1]` (последний).

## `sum` и `len`

~~~python
total = sum(numbers)
count = len(numbers)
average = total / count
~~~

`sum` складывает элементы, `len` возвращает количество. Оператор `/`
всегда даёт `float`, даже если числа делятся нацело.

## Форматирование

~~~python
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
~~~

## Пустой список

`sum([])` равен `0`, но `len([])` равен `0`, и деление на ноль бросит
`ZeroDivisionError`. По условию список непустой.

## Среднее без `sum`

~~~python
total = 0
for value in numbers:
    total += value
~~~

Такой цикл полезен, если значения нужно дополнительно обрабатывать.
