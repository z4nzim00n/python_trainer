@@TASK
section: 08_collections
dir: 01_word_count
num: 8_1
title: PY_08_01. Подсчёт слов
topics: `dict`, `Counter`, сортировка ключей
input: Одна строка
@@DESC
Посчитай, сколько раз встречается каждое слово, и выведи результат
по алфавиту:

~~~text
<слово>: <количество>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `apple banana apple` | `apple: 2`<br>`banana: 1` |
| `b a b a c` | `a: 2`<br>`b: 2`<br>`c: 1` |
@@THEORY
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
@@TESTS
| `apple banana apple` | `apple: 2\nbanana: 1\n` |
| `b a b a c` | `a: 2\nb: 2\nc: 1\n` |
| `one` | `one: 1\n` |
@@CASES
run_case "apple banana apple" $'apple: 2\nbanana: 1\n'
run_case "b a b a c" $'a: 2\nb: 2\nc: 1\n'
run_case "one" $'one: 1\n'
@@MAIN
from collections import Counter

words = input().split()

# TODO: посчитай слова и выведи их по алфавиту
print("TODO")
@@SOLUTION
from collections import Counter

words = input().split()
counts = Counter(words)

for word in sorted(counts):
    print(f"{word}: {counts[word]}")
@@COMMENTED
from collections import Counter

words = input().split()
# Counter сам подсчитывает вхождения каждого слова.
counts = Counter(words)

for word in sorted(counts):
    print(f"{word}: {counts[word]}")
@@END

@@TASK
section: 08_collections
dir: 02_dictionary_find
num: 8_2
title: PY_08_02. Поиск в словаре
topics: `dict`, `in`, `get`, `KeyError`
input: Ключ
@@DESC
Дан словарь:

~~~python
data = {"name": "Ada", "lang": "Python", "year": "1991"}
~~~

Считай ключ. Если он есть, выведи `Value: <значение>`, иначе
`Value: Not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `name` | `Value: Ada` |
| `age` | `Value: Not found` |
@@THEORY
## Проверка наличия

~~~python
if key in data:
    print(f"Value: {data[key]}")
else:
    print("Value: Not found")
~~~

Оператор `in` проверяет ключи, а не значения.

## `KeyError`

Если обратиться к отсутствующему ключу напрямую:

~~~python
data["age"]  # KeyError: 'age'
~~~

## `get`

~~~python
value = data.get(key, "Not found")
print(f"Value: {value}")
~~~

Второй аргумент — значение по умолчанию. Без него `get` вернёт `None`.

## `None` как значение

Если в словаре может лежать `None`, `get` не отличит отсутствие ключа
от сохранённого `None`. Тогда используют `in`.

## Перебор

~~~python
for key, value in data.items():
    print(key, value)
~~~

`items()` даёт пары ключ-значение.
@@TESTS
| `name` | `Value: Ada\n` |
| `lang` | `Value: Python\n` |
| `age` | `Value: Not found\n` |
@@CASES
run_case "name" $'Value: Ada\n'
run_case "lang" $'Value: Python\n'
run_case "age" $'Value: Not found\n'
@@MAIN
data = {"name": "Ada", "lang": "Python", "year": "1991"}

key = input()

# TODO: выведи Value: <значение> или Value: Not found
print("TODO")
@@SOLUTION
data = {"name": "Ada", "lang": "Python", "year": "1991"}

key = input()

if key in data:
    print(f"Value: {data[key]}")
else:
    print("Value: Not found")
@@COMMENTED
data = {"name": "Ada", "lang": "Python", "year": "1991"}

key = input()

# in проверяет именно ключи словаря.
if key in data:
    print(f"Value: {data[key]}")
else:
    print("Value: Not found")
@@END

@@TASK
section: 08_collections
dir: 03_unique_elements
num: 8_3
title: PY_08_03. Уникальные элементы
topics: `set`, `sorted`, множество
input: Число `n`, затем `n` целых чисел
@@DESC
Выведи уникальные числа в порядке возрастания:

~~~text
Unique: <числа через пробел>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `6`<br>`3 1 2 1 3 2` | `Unique: 1 2 3` |
| `4`<br>`-1 -1 0 0` | `Unique: -1 0` |
@@THEORY
## Множество

~~~python
unique = set(numbers)
~~~

`set` хранит только уникальные значения. Повторные добавления игнорируются.

## Сортировка

Множество не упорядочено, поэтому для стабильного вывода его сортируют:

~~~python
result = sorted(unique)
print("Unique:", *result)
~~~

`sorted` принимает любой итерируемый объект и возвращает список.

## Операции над множествами

| Операция | Запись |
| --- | --- |
| объединение | `a \| b` |
| пересечение | `a & b` |
| разность | `a - b` |
| симметричная разность | `a ^ b` |

~~~python
{1, 2, 3} & {2, 3, 4}  # {2, 3}
~~~

## Сложность

Проверка `x in set` в среднем быстрее, чем `x in list`: множество
использует хеш-таблицу.

## Изменяемость

`set` изменяем: можно `add` и `remove`. Неизменяемый вариант —
`frozenset`.
@@TESTS
| `6\n3 1 2 1 3 2` | `Unique: 1 2 3\n` |
| `1\n5` | `Unique: 5\n` |
| `4\n-1 -1 0 0` | `Unique: -1 0\n` |
@@CASES
run_case $'6\n3 1 2 1 3 2' $'Unique: 1 2 3\n'
run_case $'1\n5' $'Unique: 5\n'
run_case $'4\n-1 -1 0 0' $'Unique: -1 0\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: выведи уникальные числа по возрастанию
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

unique = sorted(set(numbers))
print("Unique:", *unique)
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# set убирает повторы, sorted возвращает порядок.
unique = sorted(set(numbers))
print("Unique:", *unique)
@@END

@@TASK
section: 08_collections
dir: 04_group_by_length
num: 8_4
title: PY_08_04. Группировка по длине
topics: `dict`, `setdefault`, списки значений
input: Слова через пробел
@@DESC
Сгруппируй слова по длине и выведи группы по возрастанию длины:

~~~text
<длина>: <слова через пробел>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `cat dog hello` | `3: cat dog`<br>`5: hello` |
| `a bb ccc` | `1: a`<br>`2: bb`<br>`3: ccc` |
@@THEORY
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
@@TESTS
| `cat dog hello` | `3: cat dog\n5: hello\n` |
| `a bb ccc` | `1: a\n2: bb\n3: ccc\n` |
| `hi hi` | `2: hi hi\n` |
@@CASES
run_case "cat dog hello" $'3: cat dog\n5: hello\n'
run_case "a bb ccc" $'1: a\n2: bb\n3: ccc\n'
run_case "hi hi" $'2: hi hi\n'
@@MAIN
words = input().split()

# TODO: сгруппируй слова по длине и выведи группы
print("TODO")
@@SOLUTION
words = input().split()

groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)

for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
@@COMMENTED
words = input().split()

# setdefault создаёт список для новой длины и возвращает его.
groups = {}
for word in words:
    groups.setdefault(len(word), []).append(word)

for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
@@END

@@TASK
section: 08_collections
dir: 05_invert_map
num: 8_5
title: PY_08_05. Инверсия словаря
topics: `dict`, `setdefault`, группировка
input: Число `n`, затем `n` пар «ключ значение»
@@DESC
Построй обратный словарь: значению соответствует список ключей.
Выведи значения по возрастанию:

~~~text
<значение>: <ключи через пробел>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`a 1`<br>`b 2`<br>`c 1` | `1: a c`<br>`2: b` |
| `3`<br>`m 10`<br>`n 2`<br>`o 10` | `2: n`<br>`10: m o` |
@@THEORY
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
@@TESTS
| `3\na 1\nb 2\nc 1` | `1: a c\n2: b\n` |
| `3\nm 10\nn 2\no 10` | `2: n\n10: m o\n` |
| `2\nleft 10\nright 10` | `10: left right\n` |
@@CASES
run_case $'3\na 1\nb 2\nc 1' $'1: a c\n2: b\n'
run_case $'3\nm 10\nn 2\no 10' $'2: n\n10: m o\n'
run_case $'2\nleft 10\nright 10' $'10: left right\n'
@@MAIN
n = int(input())

# TODO: построй обратный словарь и выведи его
print("TODO")
@@SOLUTION
n = int(input())

inverted = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    inverted.setdefault(value, []).append(key)

for value in sorted(inverted):
    print(f"{value}: {' '.join(inverted[value])}")
@@COMMENTED
n = int(input())

# Значением обратного словаря будет список ключей.
inverted = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    inverted.setdefault(value, []).append(key)

for value in sorted(inverted):
    print(f"{value}: {' '.join(inverted[value])}")
@@END
