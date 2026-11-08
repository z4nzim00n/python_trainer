# Разбор задания

## Задача

Исходно: ключ → значение. Нужно: значение → список ключей. Одному
значению может соответствовать несколько ключей, поэтому значением
обратного словаря становится список.

## Решение

~~~python
n = int(input())
inverted = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    inverted.setdefault(value, []).append(key)
~~~

`setdefault` создаёт список при первом появлении значения.

## Числовая сортировка

Значения приводим к `int`, иначе `"10"` окажется раньше `"2"`:

~~~python
for value in sorted(inverted):
    print(f"{value}: {' '.join(inverted[value])}")
~~~

## `defaultdict`

~~~python
from collections import defaultdict

inverted = defaultdict(list)
inverted[value].append(key)
~~~

Короче, если не нужно проверять наличие ключа.

## Потеря данных

При обычной инверсии `{v: k for k, v in data.items()}` несколько ключей
с одинаковым значением перезапишут друг друга. Список в значении решает
эту проблему.
