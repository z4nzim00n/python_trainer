# Разбор задания

## Словарь

~~~python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
~~~

`dict` хранит пары «ключ — значение». `get` возвращает значение или
значение по умолчанию, если ключа нет.

## `Counter`

~~~python
from collections import Counter

counts = Counter(words)
~~~

`Counter` — словарь, который сам считает вхождения. Обращение к
отсутствующему ключу возвращает `0`, а не бросает `KeyError`.

## Сортировка ключей

~~~python
for word in sorted(counts):
    print(f"{word}: {counts[word]}")
~~~

`sorted(dict)` сортирует ключи. Без сортировки порядок был бы порядком
вставки — он тоже определён, но задание требует алфавит.

## `most_common`

~~~python
for word, count in counts.most_common(3):
    ...
~~~

Возвращает самые частые элементы. Для вывода по алфавиту этот метод
не подходит.

## Регистр

В задаче слова сравниваются как есть: `Apple` и `apple` — разные ключи.
Если нужен регистронезависимый подсчёт, применяют `word.lower()`.
