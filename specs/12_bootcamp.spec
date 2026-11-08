@@TASK
section: 12_bootcamp
dir: 01_prime_check
num: 12_1
title: PY_12_01. Простое число
topics: `while`, делители, `bool`
input: Одно целое число
@@DESC
Определи, является ли число простым:

~~~text
Prime: <True/False>
~~~

Простое число больше единицы и делится только на `1` и на себя.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `17` | `Prime: True` |
| `9` | `Prime: False` |
| `1` | `Prime: False` |
@@THEORY
## Определение

Простое число:

- больше `1`;
- не имеет делителей, кроме `1` и самого себя.

## Проверка до корня

Если у числа есть делитель `d > 1`, то есть и делитель `n // d`.
Один из них не больше `sqrt(n)`. Поэтому достаточно проверить
`d` от `2` до `sqrt(n)`:

~~~python
is_prime = n >= 2
d = 2
while d * d <= n:
    if n % d == 0:
        is_prime = False
        break
    d += 1
~~~

`d * d <= n` заменяет `d <= sqrt(n)` и не требует `math.sqrt`.

## `break`

Как только найден делитель, дальше проверять не нужно. `break` завершает
цикл.

## Крайние случаи

| `n` | Ответ | Причина |
| --- | --- | --- |
| `2` | `True` | первое простое |
| `1` | `False` | не больше единицы |
| `0` | `False` | не больше единицы |
| `-7` | `False` | отрицательные не простые |

## Производительность

Проверка до корня работает за `O(sqrt(n))`. Для очень больших чисел
используют решето Эратосфена или вероятностные тесты.
@@TESTS
| `17` | `Prime: True\n` |
| `2` | `Prime: True\n` |
| `1` | `Prime: False\n` |
| `9` | `Prime: False\n` |
| `-7` | `Prime: False\n` |
@@CASES
run_case "17" $'Prime: True\n'
run_case "2" $'Prime: True\n'
run_case "1" $'Prime: False\n'
run_case "9" $'Prime: False\n'
run_case "-7" $'Prime: False\n'
@@MAIN
n = int(input())

# TODO: проверь, простое ли число, и выведи Prime: <True/False>
print("TODO")
@@SOLUTION
n = int(input())

is_prime = n >= 2
d = 2
while d * d <= n:
    if n % d == 0:
        is_prime = False
        break
    d += 1

print(f"Prime: {is_prime}")
@@COMMENTED
n = int(input())

is_prime = n >= 2
d = 2
# Достаточно проверить делители до корня из n.
while d * d <= n:
    if n % d == 0:
        is_prime = False
        break
    d += 1

print(f"Prime: {is_prime}")
@@END

@@TASK
section: 12_bootcamp
dir: 02_coffee_machine
num: 12_2
title: PY_12_02. Кофейный автомат
topics: `for`, `break`, накопление суммы
input: Цена и монеты (две строки)
@@DESC
Автомат принимает монеты, пока не встретит `0`. Сравни оплату с ценой:

- если денег достаточно, выведи `Change: <сдача>`;
- если нет — `Need: <не хватает>`.

Монеты после нуля игнорируются.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `50`<br>`10 10 10 10 10 0` | `Change: 0` |
| `75`<br>`25 25 0` | `Need: 25` |
@@THEORY
## Накопление

~~~python
paid = 0
for coin in coins:
    if coin == 0:
        break
    paid += coin
~~~

`break` останавливает приём, когда пользователь закончил.

## Сравнение

~~~python
if paid >= price:
    print(f"Change: {paid - price}")
else:
    print(f"Need: {price - paid}")
~~~

## Почему `break`, а не фильтрация

Если после нуля в списке окажутся числа, они не должны попасть в оплату.
`break` гарантирует остановку.

## Состояния автомата

В реальном автомате есть состояния: ожидание монеты, выбор напитка,
выдача сдачи. Здесь мы моделируем только оплату. Похожий код встречается
в заданиях School 21 про кофейный автомат.

## Проверка

Для `50` и пяти монет по `10`: оплата `50`, сдача `0`. Для `75` и
двух монет по `25`: оплата `50`, не хватает `25`.
@@TESTS
| `50\n10 10 10 10 10 0` | `Change: 0\n` |
| `75\n25 25 0` | `Need: 25\n` |
| `30\n5 10 20 0` | `Change: 5\n` |
@@CASES
run_case $'50\n10 10 10 10 10 0' $'Change: 0\n'
run_case $'75\n25 25 0' $'Need: 25\n'
run_case $'30\n5 10 20 0' $'Change: 5\n'
@@MAIN
price = int(input())
coins = list(map(int, input().split()))

# TODO: посчитай оплату до нуля и выведи сдачу или нехватку
print("TODO")
@@SOLUTION
price = int(input())
coins = list(map(int, input().split()))

paid = 0
for coin in coins:
    if coin == 0:
        break
    paid += coin

if paid >= price:
    print(f"Change: {paid - price}")
else:
    print(f"Need: {price - paid}")
@@COMMENTED
price = int(input())
coins = list(map(int, input().split()))

paid = 0
for coin in coins:
    # Ноль означает конец приёма монет.
    if coin == 0:
        break
    paid += coin

if paid >= price:
    print(f"Change: {paid - price}")
else:
    print(f"Need: {price - paid}")
@@END

@@TASK
section: 12_bootcamp
dir: 03_statistics
num: 12_3
title: PY_12_03. Статистика
topics: `sum`, `min`, `max`, `len`, форматирование
input: Число `n`, затем `n` целых чисел
@@DESC
Выведи статистику списка:

~~~text
Count: <количество>
Sum: <сумма>
Min: <минимум>
Max: <максимум>
Average: <среднее с двумя знаками>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `Count: 5`<br>`Sum: 15`<br>`Min: 1`<br>`Max: 5`<br>`Average: 3.00` |
| `1`<br>`7` | `Count: 1`<br>`Sum: 7`<br>`Min: 7`<br>`Max: 7`<br>`Average: 7.00` |
@@THEORY
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
@@TESTS
| `5\n1 2 3 4 5` | `Count: 5\nSum: 15\nMin: 1\nMax: 5\nAverage: 3.00\n` |
| `1\n7` | `Count: 1\nSum: 7\nMin: 7\nMax: 7\nAverage: 7.00\n` |
| `3\n-2 0 2` | `Count: 3\nSum: 0\nMin: -2\nMax: 2\nAverage: 0.00\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'Count: 5\nSum: 15\nMin: 1\nMax: 5\nAverage: 3.00\n'
run_case $'1\n7' $'Count: 1\nSum: 7\nMin: 7\nMax: 7\nAverage: 7.00\n'
run_case $'3\n-2 0 2' $'Count: 3\nSum: 0\nMin: -2\nMax: 2\nAverage: 0.00\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: выведи Count, Sum, Min, Max и Average
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

count = len(numbers)
total = sum(numbers)
lowest = min(numbers)
highest = max(numbers)
average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Min: {lowest}")
print(f"Max: {highest}")
print(f"Average: {average:.2f}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

count = len(numbers)
total = sum(numbers)
lowest = min(numbers)
highest = max(numbers)
average = total / count

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Min: {lowest}")
print(f"Max: {highest}")
# / даёт float, поэтому среднее печатается с двумя знаками.
print(f"Average: {average:.2f}")
@@END

@@TASK
section: 12_bootcamp
dir: 04_histogram
num: 12_4
title: PY_12_04. Гистограмма
topics: `Counter`, `sorted`, умножение строк
input: Число `n`, затем `n` положительных чисел
@@DESC
Построй горизонтальную гистограмму: для каждого значения выведи его
и столько звёздочек, сколько раз оно встретилось:

~~~text
<значение>: <звёздочки>
~~~

Строки идут по возрастанию значения.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `6`<br>`1 2 2 3 3 3` | `1: *`<br>`2: **`<br>`3: ***` |
| `3`<br>`5 5 5` | `5: ***` |
@@THEORY
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
@@TESTS
| `6\n1 2 2 3 3 3` | `1: *\n2: **\n3: ***\n` |
| `3\n5 5 5` | `5: ***\n` |
| `4\n3 1 3 1` | `1: **\n3: **\n` |
@@CASES
run_case $'6\n1 2 2 3 3 3' $'1: *\n2: **\n3: ***\n'
run_case $'3\n5 5 5' $'5: ***\n'
run_case $'4\n3 1 3 1' $'1: **\n3: **\n'
@@MAIN
from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

# TODO: построй гистограмму
print("TODO")
@@SOLUTION
from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counts = Counter(numbers)

for value in sorted(counts):
    print(f"{value}: {'*' * counts[value]}")
@@COMMENTED
from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counts = Counter(numbers)

for value in sorted(counts):
    # Умножение строки повторяет её нужное число раз.
    print(f"{value}: {'*' * counts[value]}")
@@END

@@TASK
section: 12_bootcamp
dir: 05_rotate_matrix
num: 12_5
title: PY_12_05. Поворот матрицы
topics: вложенные списки, `zip`, срезы
input: Размер `n`, затем `n` строк матрицы
@@DESC
Поверни квадратную матрицу на 90 градусов по часовой стрелке и выведи
результат:

~~~text
<новая строка 1>
...
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2`<br>`1 2`<br>`3 4` | `3 1`<br>`4 2` |
| `3`<br>`1 2 3`<br>`4 5 6`<br>`7 8 9` | `7 4 1`<br>`8 5 2`<br>`9 6 3` |
@@THEORY
## Матрица как список списков

~~~python
matrix = [list(map(int, input().split())) for _ in range(n)]
~~~

Каждая строка — отдельный список. `matrix[i][j]` — элемент в строке `i`,
столбце `j`.

## Поворот

При повороте на 90° по часовой стрелке:

- последний столбец становится первой строкой;
- предпоследний — второй, и так далее.

Формула: `rotated[i][j] = matrix[n - 1 - j][i]`.

## Через `zip`

~~~python
rotated = [list(row) for row in zip(*matrix[::-1])]
~~~

- `matrix[::-1]` — строки в обратном порядке;
- `zip(*...)` — транспонирование: собирает первые элементы, вторые и т.д.;
- `list` превращает кортежи в строки матрицы.

## Ручной вариант

~~~python
rotated = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated[i][j] = matrix[n - 1 - j][i]
~~~

## Важно: копия строк

`[[0] * n] * n` создаёт `n` ссылок на один список. Меняя одну строку,
вы измените все. Поэтому используют генератор списков.
@@TESTS
| `2\n1 2\n3 4` | `3 1\n4 2\n` |
| `3\n1 2 3\n4 5 6\n7 8 9` | `7 4 1\n8 5 2\n9 6 3\n` |
| `1\n42` | `42\n` |
@@CASES
run_case $'2\n1 2\n3 4' $'3 1\n4 2\n'
run_case $'3\n1 2 3\n4 5 6\n7 8 9' $'7 4 1\n8 5 2\n9 6 3\n'
run_case $'1\n42' $'42\n'
@@MAIN
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# TODO: поверни матрицу на 90 градусов по часовой стрелке и выведи
print("TODO")
@@SOLUTION
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

rotated = [list(row) for row in zip(*matrix[::-1])]

for row in rotated:
    print(*row)
@@COMMENTED
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Сначала переворачиваем строки, затем транспонируем.
rotated = [list(row) for row in zip(*matrix[::-1])]

for row in rotated:
    print(*row)
@@END

@@TASK
section: 12_bootcamp
dir: 06_matrix_sum
num: 12_6
title: PY_12_06. Сумма матриц
topics: вложенные списки, генераторы, `zip`
input: Размер `n`, затем две матрицы `n x n`
@@DESC
Сложи две матрицы поэлементно и выведи результат:

~~~text
<строка 1>
...
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2`<br>`1 2`<br>`3 4`<br>`5 6`<br>`7 8` | `6 8`<br>`10 12` |
@@THEORY
## Чтение двух матриц

~~~python
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
~~~

Одинаковый код читает сначала первую матрицу, потом вторую.

## Сложение

~~~python
result = [
    [a[i][j] + b[i][j] for j in range(n)]
    for i in range(n)
]
~~~

Внешний генератор идёт по строкам, внутренний — по столбцам.

## Через `zip`

~~~python
result = [
    [x + y for x, y in zip(row_a, row_b)]
    for row_a, row_b in zip(a, b)
]
~~~

`zip` попарно объединяет строки, затем элементы строк.

## Вывод

~~~python
for row in result:
    print(*row)
~~~

## Размерности

Складывать можно только матрицы одинакового размера. В задаче они
квадратные `n x n`.

## Списки и генераторы

Внутренний `[... for ...]` создаёт новый список. Если заменить его на
кортеж, строка станет неизменяемой — для вывода это не важно.
@@TESTS
| `2\n1 2\n3 4\n5 6\n7 8` | `6 8\n10 12\n` |
| `1\n5\n6` | `11\n` |
| `2\n1 -1\n0 2\n-1 1\n0 -2` | `0 0\n0 0\n` |
@@CASES
run_case $'2\n1 2\n3 4\n5 6\n7 8' $'6 8\n10 12\n'
run_case $'1\n5\n6' $'11\n'
run_case $'2\n1 -1\n0 2\n-1 1\n0 -2' $'0 0\n0 0\n'
@@MAIN
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

# TODO: сложи матрицы и выведи результат
print("TODO")
@@SOLUTION
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

result = [
    [x + y for x, y in zip(row_a, row_b)]
    for row_a, row_b in zip(a, b)
]

for row in result:
    print(*row)
@@COMMENTED
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

# zip попарно соединяет строки, внутренний zip — элементы строк.
result = [
    [x + y for x, y in zip(row_a, row_b)]
    for row_a, row_b in zip(a, b)
]

for row in result:
    print(*row)
@@END
