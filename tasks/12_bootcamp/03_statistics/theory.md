# Разбор задания

## Один проход или встроенные функции

~~~python
count = len(numbers)
total = sum(numbers)
lowest = min(numbers)
highest = max(numbers)
average = total / count
~~~

Каждая функция проходит по списку. Для небольших данных это нормально.

## Один цикл

~~~python
total = 0
lowest = numbers[0]
highest = numbers[0]
for value in numbers:
    total += value
    if value < lowest:
        lowest = value
    if value > highest:
        highest = value
~~~

Такой вариант делает всё за один проход и полезен для потоковой обработки.

## Среднее

`/` всегда даёт `float`. Формат `:.2f` печатает два знака.

## Пустой список

Статистика пустого списка не определена: `min` и `max` бросят
`ValueError`, а среднее — деление на ноль. По условию `n >= 1`.

## Модуль `statistics`

~~~python
import statistics
statistics.mean(numbers)
~~~

Есть готовые функции, включая медиану и стандартное отклонение.
