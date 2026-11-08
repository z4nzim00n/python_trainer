@@TASK
section: 05_lists
dir: 01_list_sum_average
num: 5_1
title: PY_05_01. Сумма и среднее
topics: список, `sum`, `len`, `float`
input: Число `n`, затем `n` целых чисел
@@DESC
Считай список чисел и выведи сумму и среднее арифметическое:

~~~text
Sum: <сумма>
Average: <среднее с двумя знаками>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4`<br>`1 2 3 4` | `Sum: 10`<br>`Average: 2.50` |
| `3`<br>`2 2 2` | `Sum: 6`<br>`Average: 2.00` |
@@THEORY
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
@@TESTS
| `4\n1 2 3 4` | `Sum: 10\nAverage: 2.50\n` |
| `3\n2 2 2` | `Sum: 6\nAverage: 2.00\n` |
| `1\n-5` | `Sum: -5\nAverage: -5.00\n` |
@@CASES
run_case $'4\n1 2 3 4' $'Sum: 10\nAverage: 2.50\n'
run_case $'3\n2 2 2' $'Sum: 6\nAverage: 2.00\n'
run_case $'1\n-5' $'Sum: -5\nAverage: -5.00\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: выведи Sum и Average
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

total = sum(numbers)
average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

total = sum(numbers)
# / всегда возвращает float, поэтому среднее можно печатать с .2f.
average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
@@END

@@TASK
section: 05_lists
dir: 02_min_max
num: 5_2
title: PY_05_02. Минимум и максимум
topics: `min`, `max`, список
input: Число `n`, затем `n` целых чисел
@@DESC
Найди минимальное и максимальное значения списка:

~~~text
Min: <минимум>
Max: <максимум>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 7 2 9 4` | `Min: 2`<br>`Max: 9` |
| `3`<br>`-4 -1 -9` | `Min: -9`<br>`Max: -1` |
@@THEORY
## Встроенные функции

~~~python
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
~~~

Обе функции проходят по элементам один раз и возвращают нужное значение.

## Своими руками

~~~python
lowest = numbers[0]
highest = numbers[0]
for value in numbers[1:]:
    if value < lowest:
        lowest = value
    if value > highest:
        highest = value
~~~

Начальное значение берут из первого элемента, а не из нуля: иначе для
списка из отрицательных чисел максимум остался бы нулём.

## `key`

У `min` и `max` есть параметр `key` — правило сравнения:

~~~python
words = ["aaa", "b", "cc"]
print(max(words, key=len))  # aaa
~~~

## Пустой список

`min([])` и `max([])` бросают `ValueError`. По условию `n >= 1`.
@@TESTS
| `5\n3 7 2 9 4` | `Min: 2\nMax: 9\n` |
| `3\n-4 -1 -9` | `Min: -9\nMax: -1\n` |
| `1\n5` | `Min: 5\nMax: 5\n` |
@@CASES
run_case $'5\n3 7 2 9 4' $'Min: 2\nMax: 9\n'
run_case $'3\n-4 -1 -9' $'Min: -9\nMax: -1\n'
run_case $'1\n5' $'Min: 5\nMax: 5\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: выведи Min и Max
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# min и max перебирают весь список.
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
@@END

@@TASK
section: 05_lists
dir: 03_reverse_list
num: 5_3
title: PY_05_03. Разворот списка
topics: срезы, `reversed`, список
input: Число `n`, затем `n` целых чисел
@@DESC
Выведи элементы списка в обратном порядке через пробел:

~~~text
<последний> ... <первый>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4`<br>`1 2 3 4` | `4 3 2 1` |
| `1`<br>`10` | `10` |
@@THEORY
## Срез с шагом

~~~python
numbers[::-1]
~~~

Срез `[start:stop:step]` с шагом `-1` идёт с конца к началу. Исходный
список не меняется — создаётся новый.

## `reversed`

~~~python
list(reversed(numbers))
~~~

`reversed` возвращает итератор. `list` собирает из него список.

## Разворот на месте

~~~python
numbers.reverse()
~~~

`reverse` меняет сам список и возвращает `None`.

## Вывод без скобок

~~~python
print(*numbers)
~~~

Звёздочка распаковывает список в аргументы `print`. Элементы разделяются
пробелом, скобки не печатаются.

## Строка и список

Строка тоже поддерживает срез `[::-1]` — об этом в разделе про строки.
@@TESTS
| `4\n1 2 3 4` | `4 3 2 1\n` |
| `1\n10` | `10\n` |
| `3\n-1 0 5` | `5 0 -1\n` |
@@CASES
run_case $'4\n1 2 3 4' $'4 3 2 1\n'
run_case $'1\n10' $'10\n'
run_case $'3\n-1 0 5' $'5 0 -1\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: выведи элементы в обратном порядке
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

print(*numbers[::-1])
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# Срез с шагом -1 создаёт развёрнутую копию, * распаковывает её в print.
print(*numbers[::-1])
@@END

@@TASK
section: 05_lists
dir: 04_remove_duplicates
num: 5_4
title: PY_05_04. Удаление дубликатов
topics: `set`, порядок элементов, список
input: Число `n`, затем `n` целых чисел
@@DESC
Убери повторяющиеся числа, сохранив порядок первого появления:

~~~text
<уникальные числа через пробел>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `6`<br>`1 2 3 1 2 4` | `1 2 3 4` |
| `5`<br>`5 5 5 5 5` | `5` |
@@THEORY
## Множество

~~~python
seen = set()
~~~

`set` хранит уникальные значения и проверяет вхождение за `O(1)`.

## Сохранение порядка

`set(numbers)` удалит дубликаты, но порядок не гарантирован. Чтобы
сохранить первое появление, идём по списку и добавляем только новые:

~~~python
seen = set()
result = []
for value in numbers:
    if value not in seen:
        seen.add(value)
        result.append(value)
~~~

## Почему не `list(set(...))`

Порядок элементов множества зависит от хешей. Для небольших чисел он
часто совпадает с порядком вставки, но полагаться на это нельзя.

## Вывод

~~~python
print(*result)
~~~

## Хешируемые значения

В `set` можно класть числа, строки, кортежи. Списки и словари — нельзя,
они изменяемые и не хешируются.
@@TESTS
| `6\n1 2 3 1 2 4` | `1 2 3 4\n` |
| `5\n5 5 5 5 5` | `5\n` |
| `4\n3 1 3 1` | `3 1\n` |
@@CASES
run_case $'6\n1 2 3 1 2 4' $'1 2 3 4\n'
run_case $'5\n5 5 5 5 5' $'5\n'
run_case $'4\n3 1 3 1' $'3 1\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: убери повторы, сохранив порядок
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

seen = set()
result = []
for value in numbers:
    if value not in seen:
        seen.add(value)
        result.append(value)

print(*result)
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# seen отвечает за проверку, result хранит порядок первого появления.
seen = set()
result = []
for value in numbers:
    if value not in seen:
        seen.add(value)
        result.append(value)

print(*result)
@@END

@@TASK
section: 05_lists
dir: 05_sort_numbers
num: 5_5
title: PY_05_05. Сортировка
topics: `sorted`, `sort`, порядок
input: Число `n`, затем `n` целых чисел
@@DESC
Отсортируй числа по возрастанию и выведи их через пробел:

~~~text
<числа по возрастанию>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 1 4 1 5` | `1 1 3 4 5` |
| `3`<br>`-1 5 0` | `-1 0 5` |
@@THEORY
## `sorted`

~~~python
result = sorted(numbers)
~~~

`sorted` возвращает новый список и не меняет исходный.

## `sort`

~~~python
numbers.sort()
~~~

`sort` сортирует список на месте и возвращает `None`. Поэтому нельзя
писать `numbers = numbers.sort()` — получится `None`.

## Убывание

~~~python
sorted(numbers, reverse=True)
~~~

## Сортировка строк

Строки сравниваются посимвольно по кодам символов:

~~~python
sorted(["banana", "apple", "cherry"])
# ['apple', 'banana', 'cherry']
~~~

## Устойчивость

Сортировка устойчива: равные элементы сохраняют относительный порядок.
Это важно при сортировке по нескольким полям.
@@TESTS
| `5\n3 1 4 1 5` | `1 1 3 4 5\n` |
| `3\n-1 5 0` | `-1 0 5\n` |
| `4\n9 9 2 2` | `2 2 9 9\n` |
@@CASES
run_case $'5\n3 1 4 1 5' $'1 1 3 4 5\n'
run_case $'3\n-1 5 0' $'-1 0 5\n'
run_case $'4\n9 9 2 2' $'2 2 9 9\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: отсортируй и выведи числа
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

print(*sorted(numbers))
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# sorted возвращает новый отсортированный список.
print(*sorted(numbers))
@@END

@@TASK
section: 05_lists
dir: 06_rotate_list
num: 5_6
title: PY_05_06. Циклический сдвиг
topics: срезы, `%`, список
input: Числа `n` и `k`, затем `n` целых чисел
@@DESC
Сдвинь список вправо на `k` позиций. Последние `k` элементов переходят
в начало:

~~~text
<сдвинутый список>
~~~

Если `k` больше `n`, сдвиг повторяется по кругу.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5 2`<br>`1 2 3 4 5` | `4 5 1 2 3` |
| `5 0`<br>`1 2 3 4 5` | `1 2 3 4 5` |
@@THEORY
## Сдвиг по модулю

Полный круг возвращает список в исходное состояние, поэтому:

~~~python
k %= n
~~~

Для `n = 5`, `k = 7` остаток равен `2` — достаточно сдвинуть на 2.

## Два среза

~~~python
result = numbers[-k:] + numbers[:-k]
~~~

- `numbers[-k:]` — последние `k` элементов;
- `numbers[:-k]` — все остальные.

Для `k = 0` первый срез даёт весь список, второй — пустой, результат
не меняется.

## Проверка

`[1, 2, 3, 4, 5]`, `k = 2`:

~~~text
last two:  [4, 5]
the rest:  [1, 2, 3]
result:    [4, 5, 1, 2, 3]
~~~

## Другой способ

~~~python
for _ in range(k):
    numbers.insert(0, numbers.pop())
~~~

Работает, но на больших `k` медленнее: каждый `insert` сдвигает элементы.
Срезы делают копию за один проход.
@@TESTS
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `5 0\n1 2 3 4 5` | `1 2 3 4 5\n` |
| `3 5\n1 2 3` | `2 3 1\n` |
@@CASES
run_case $'5 2\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'5 0\n1 2 3 4 5' $'1 2 3 4 5\n'
run_case $'3 5\n1 2 3' $'2 3 1\n'
@@MAIN
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# TODO: сдвинь список вправо на k и выведи его
print("TODO")
@@SOLUTION
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

k %= n
result = numbers[-k:] + numbers[:-k]

print(*result)
@@COMMENTED
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Полные круги не меняют список, поэтому берём остаток.
k %= n
result = numbers[-k:] + numbers[:-k]

print(*result)
@@END
