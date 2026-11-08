# Разбор задания

## Подсчёт

~~~python
from collections import Counter

counts = Counter(numbers)
~~~

`Counter` хранит частоты. Обращение к отсутствующему значению даёт `0`.

## Строка из звёздочек

~~~python
"*" * count
~~~

Умножение строки на число повторяет её. Для `count = 3` получится `***`.

## Вывод

~~~python
for value in sorted(counts):
    print(f"{value}: {'*' * counts[value]}")
~~~

Сортировка значений делает вывод стабильным.

## Без `Counter`

~~~python
counts = {}
for value in numbers:
    counts[value] = counts.get(value, 0) + 1
~~~

## Нулевые значения

Если значение не встречалось, строка не печатается: в `counts` его нет.

## Вертикальная гистограмма

Иногда рисуют столбцы сверху вниз, но горизонтальная проще и не зависит
от шрифта.
