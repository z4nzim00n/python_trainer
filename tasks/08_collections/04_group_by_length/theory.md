# Разбор задания

## Словарь списков

~~~python
groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)
~~~

`setdefault(key, default)`:

- если ключ есть, возвращает его значение;
- если ключа нет, создаёт его со значением `default` и возвращает это
  значение.

Получается список слов для каждой длины.

## Без `setdefault`

~~~python
length = len(word)
if length not in groups:
    groups[length] = []
groups[length].append(word)
~~~

То же самое, но длиннее. Оба варианта правильные.

## Вывод

~~~python
for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
~~~

`join` склеивает список строк через пробел.

## `defaultdict`

~~~python
from collections import defaultdict

groups = defaultdict(list)
groups[len(word)].append(word)
~~~

`defaultdict` создаёт пустой список автоматически. Удобно, когда групп
много.

## Порядок

Слова внутри группы сохраняют порядок появления. Группы сортируются
по длине.
