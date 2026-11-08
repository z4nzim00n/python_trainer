@@TASK
section: 03_expressions
dir: 01_circle_area
num: 3_1
title: PY_03_01. Площадь круга
topics: `math.pi`, `float`, возведение в степень
input: Радиус (дробное число)
@@DESC
Считай радиус круга и выведи его площадь с двумя знаками после точки:

~~~text
Area: <площадь>
~~~

Формула: `S = pi * r^2`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1` | `Area: 3.14` |
| `2` | `Area: 12.57` |
@@THEORY
## Модуль `math`

~~~python
import math
print(math.pi)  # 3.141592653589793
~~~

`math` — стандартная библиотека. После `import` к значениям обращаются
через точку: `math.pi`, `math.sqrt`, `math.degrees`.

## Степень

~~~python
area = math.pi * radius ** 2
~~~

Оператор `**` возводит в степень. `radius ** 2` — квадрат, `radius ** 0.5` —
квадратный корень.

## Порядок операций

Сначала `**`, потом `*` и `/`, потом `+` и `-`. Скобки меняют порядок:

~~~python
(2 + 3) ** 2  # 25
2 + 3 ** 2    # 11
~~~

## Форматирование

~~~python
print(f"Area: {area:.2f}")
~~~

## Другие константы

| Выражение | Значение |
| --- | --- |
| `math.pi` | 3.14159... |
| `math.e` | 2.71828... |
| `math.tau` | 6.28318... |
@@TESTS
| `1` | `Area: 3.14\n` |
| `2` | `Area: 12.57\n` |
| `0.5` | `Area: 0.79\n` |
@@CASES
run_case "1" $'Area: 3.14\n'
run_case "2" $'Area: 12.57\n'
run_case "0.5" $'Area: 0.79\n'
@@MAIN
import math

radius = float(input())

# TODO: посчитай площадь и выведи Area: <число с двумя знаками>
print("TODO")
@@SOLUTION
import math

radius = float(input())

area = math.pi * radius ** 2
print(f"Area: {area:.2f}")
@@COMMENTED
import math

radius = float(input())

# ** — возведение в степень; math.pi хранит число пи.
area = math.pi * radius ** 2
print(f"Area: {area:.2f}")
@@END

@@TASK
section: 03_expressions
dir: 02_radians_to_degrees
num: 3_2
title: PY_03_02. Радианы в градусы
topics: `math.degrees`, `float`
input: Угол в радианах
@@DESC
Переведи угол из радиан в градусы и выведи результат с двумя знаками:

~~~text
Degrees: <градусы>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3.141592653589793` | `Degrees: 180.00` |
| `1.5707963267948966` | `Degrees: 90.00` |
@@THEORY
## Перевод

Полный оборот — это `2 * pi` радиан, или 360 градусов. Значит:

~~~text
degrees = radians * 180 / pi
~~~

## Готовая функция

~~~python
import math

radians = float(input())
degrees = math.degrees(radians)
print(f"Degrees: {degrees:.2f}")
~~~

`math.degrees` делает то же самое. Обратная функция — `math.radians`.

## Почему не целые

Угол может быть дробным: `0.785398...` радиана — это 45 градусов.
Поэтому используем `float`, а не `int`.

## Точность

`math.degrees(math.pi)` возвращает ровно `180.0`, но для произвольного
ввода результат может отличаться в младших разрядах. Формат `:.2f`
скрывает эту разницу.
@@TESTS
| `3.141592653589793` | `Degrees: 180.00\n` |
| `1.5707963267948966` | `Degrees: 90.00\n` |
| `0` | `Degrees: 0.00\n` |
@@CASES
run_case "3.141592653589793" $'Degrees: 180.00\n'
run_case "1.5707963267948966" $'Degrees: 90.00\n'
run_case "0" $'Degrees: 0.00\n'
@@MAIN
import math

radians = float(input())

# TODO: переведи радианы в градусы и выведи Degrees: <число>
print("TODO")
@@SOLUTION
import math

radians = float(input())

degrees = math.degrees(radians)
print(f"Degrees: {degrees:.2f}")
@@COMMENTED
import math

radians = float(input())

# math.degrees уже содержит формулу radians * 180 / pi.
degrees = math.degrees(radians)
print(f"Degrees: {degrees:.2f}")
@@END

@@TASK
section: 03_expressions
dir: 03_digit_swap
num: 3_3
title: PY_03_03. Обмен цифр
topics: `//`, `%`, целочисленная арифметика
input: Двузначное целое число
@@DESC
Поменяй цифры двузначного числа местами и выведи результат:

~~~text
Swapped: <число>
~~~

Например, для `47` получится `74`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `47` | `Swapped: 74` |
| `10` | `Swapped: 1` |
@@THEORY
## Деление нацело и остаток

Для числа `47`:

~~~python
n = 47
tens = n // 10  # 4
ones = n % 10   # 7
~~~

- `//` — деление нацело, отбрасывает дробную часть;
- `%` — остаток от деления.

## Сборка числа

Новое число: младший разряд умножаем на 10 и добавляем старший:

~~~python
swapped = ones * 10 + tens
print(swapped)  # 74
~~~

## Ведущий ноль исчезает

Для `10` получаем `ones = 0`, `tens = 1`, новое число `0 * 10 + 1 = 1`.
При выводе как целого ведущий ноль не печатается — это ожидаемо.

## Альтернатива через строки

~~~python
n = input()
print(n[::-1])
~~~

Но тогда для `10` получится строка `"01"`, а не число `1`. В задаче нужен
целочисленный результат.
@@TESTS
| `47` | `Swapped: 74\n` |
| `10` | `Swapped: 1\n` |
| `99` | `Swapped: 99\n` |
@@CASES
run_case "47" $'Swapped: 74\n'
run_case "10" $'Swapped: 1\n'
run_case "99" $'Swapped: 99\n'
@@MAIN
n = int(input())

# TODO: поменяй цифры местами и выведи Swapped: <число>
print("TODO")
@@SOLUTION
n = int(input())

tens = n // 10
ones = n % 10
swapped = ones * 10 + tens

print(f"Swapped: {swapped}")
@@COMMENTED
n = int(input())

# // даёт десятки, % — единицы.
tens = n // 10
ones = n % 10
swapped = ones * 10 + tens

print(f"Swapped: {swapped}")
@@END

@@TASK
section: 03_expressions
dir: 04_integer_division
num: 3_4
title: PY_03_04. Деление с остатком
topics: `//`, `%`, `divmod`
input: Два целых числа через пробел
@@DESC
Считай два целых числа и выведи частное и остаток от деления:

~~~text
Div: <частное>
Rem: <остаток>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `7 3` | `Div: 2`<br>`Rem: 1` |
| `10 2` | `Div: 5`<br>`Rem: 0` |
@@THEORY
## Две операции

~~~python
a, b = map(int, input().split())
q = a // b
r = a % b
~~~

Для `7 3`: `q = 2`, `r = 1`. Проверка: `a == q * b + r`.

## `divmod`

Одна функция возвращает обе величины:

~~~python
q, r = divmod(a, b)
~~~

## Отрицательные числа

Python округляет `//` вниз, к минус бесконечности:

~~~python
-7 // 3   # -3
-7 % 3    #  2
~~~

Это отличается от C# и Java, где деление отбрасывает дробную часть
к нулю и даёт `-2` и `-1`. Правило Python удобно тем, что остаток всегда
имеет знак делителя и `a == q * b + r` выполняется.

## Деление на ноль

`a // 0` и `a % 0` бросают `ZeroDivisionError`. Обработку исключений
разберём в разделе 09.
@@TESTS
| `7 3` | `Div: 2\nRem: 1\n` |
| `10 2` | `Div: 5\nRem: 0\n` |
| `-7 3` | `Div: -3\nRem: 2\n` |
@@CASES
run_case "7 3" $'Div: 2\nRem: 1\n'
run_case "10 2" $'Div: 5\nRem: 0\n'
run_case "-7 3" $'Div: -3\nRem: 2\n'
@@MAIN
a, b = map(int, input().split())

# TODO: выведи частное и остаток
print("TODO")
@@SOLUTION
a, b = map(int, input().split())

q = a // b
r = a % b

print(f"Div: {q}")
print(f"Rem: {r}")
@@COMMENTED
a, b = map(int, input().split())

# // — целочисленное деление, % — остаток.
q = a // b
r = a % b

print(f"Div: {q}")
print(f"Rem: {r}")
@@END

@@TASK
section: 03_expressions
dir: 05_boolean_logic
num: 3_5
title: PY_03_05. Логические выражения
topics: `bool`, сравнения, `and`, `or`, `not`
input: Одно целое число
@@DESC
Считай целое число и выведи два признака:

~~~text
Positive: <True/False>
Even: <True/False>
~~~

`Positive` — число больше нуля. `Even` — число делится на 2 без остатка.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `4` | `Positive: True`<br>`Even: True` |
| `-3` | `Positive: False`<br>`Even: False` |
| `0` | `Positive: False`<br>`Even: True` |
@@THEORY
## Сравнения возвращают `bool`

~~~python
n = 4
print(n > 0)      # True
print(n % 2 == 0) # True
print(n != 0)     # True
~~~

Операторы сравнения: `==`, `!=`, `<`, `>`, `<=`, `>=`.

## Логические операторы

| Оператор | Смысл |
| --- | --- |
| `and` | оба истинны |
| `or` | хотя бы один истинен |
| `not` | отрицание |

~~~python
in_range = n >= 0 and n <= 10
~~~

## Ноль — не положительное число

`0 > 0` даёт `False`. При этом `0 % 2 == 0` даёт `True`: ноль делится
на два без остатка.

## Истинность значений

В условиях Python принимает не только `bool`. Пустые значения ложны:
`0`, `""`, `[]`, `None`. Непустые — истинны. Но в явных проверках лучше
писать сравнение, чтобы код читался однозначно.
@@TESTS
| `4` | `Positive: True\nEven: True\n` |
| `-3` | `Positive: False\nEven: False\n` |
| `0` | `Positive: False\nEven: True\n` |
@@CASES
run_case "4" $'Positive: True\nEven: True\n'
run_case "-3" $'Positive: False\nEven: False\n'
run_case "0" $'Positive: False\nEven: True\n'
@@MAIN
n = int(input())

# TODO: выведи Positive и Even
print("TODO")
@@SOLUTION
n = int(input())

print(f"Positive: {n > 0}")
print(f"Even: {n % 2 == 0}")
@@COMMENTED
n = int(input())

# Сравнение сразу даёт bool, его можно подставить в f-строку.
print(f"Positive: {n > 0}")
print(f"Even: {n % 2 == 0}")
@@END

@@TASK
section: 04_loops
dir: 01_sequence_max
num: 4_1
title: PY_04_01. Максимум последовательности
topics: `for`, список, `max`
input: Число `n`, затем `n` целых чисел
@@DESC
Считай `n`, затем `n` целых чисел и выведи максимальное:

~~~text
Max: <число>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 7 2 9 4` | `Max: 9` |
| `1`<br>`-5` | `Max: -5` |
@@THEORY
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
@@TESTS
| `5\n3 7 2 9 4` | `Max: 9\n` |
| `1\n-5` | `Max: -5\n` |
| `4\n10 10 1 2` | `Max: 10\n` |
@@CASES
run_case $'5\n3 7 2 9 4' $'Max: 9\n'
run_case $'1\n-5' $'Max: -5\n'
run_case $'4\n10 10 1 2' $'Max: 10\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: найди максимум и выведи Max: <число>
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

print(f"Max: {max(numbers)}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# max перебирает элементы и возвращает наибольший.
print(f"Max: {max(numbers)}")
@@END

@@TASK
section: 04_loops
dir: 02_sum_of_digits
num: 4_2
title: PY_04_02. Сумма цифр
topics: `while`, `%`, `//`, `abs`
input: Одно целое число
@@DESC
Считай целое число и выведи сумму его цифр:

~~~text
Sum: <сумма>
~~~

Знак числа не влияет на сумму: для `-47` сумма равна `11`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `123` | `Sum: 6` |
| `9005` | `Sum: 14` |
| `-47` | `Sum: 11` |
@@THEORY
## Выделение последней цифры

~~~python
digit = n % 10
~~~

Для `123` это `3`.

## Удаление последней цифры

~~~python
n = n // 10
~~~

`123 // 10` даёт `12`. Цифра `3` отброшена.

## Цикл

~~~python
n = abs(n)
total = 0
while n > 0:
    total += n % 10
    n //= 10
~~~

`n //= 10` — сокращённая запись `n = n // 10`.

## Знак

Для отрицательного числа `%` в Python даёт неотрицательный остаток
(`-47 % 10 == 3`), но проще сразу взять `abs(n)`: сумма цифр от знака
не зависит.

## Ноль

Для `n = 0` цикл не выполнится ни разу, и сумма останется `0` — это
правильный ответ.

## Альтернатива через строку

~~~python
total = sum(int(ch) for ch in input().lstrip("-"))
~~~

Коротко, но цикл с `%` и `//` — базовый навык для числовых задач.
@@TESTS
| `123` | `Sum: 6\n` |
| `9005` | `Sum: 14\n` |
| `-47` | `Sum: 11\n` |
| `0` | `Sum: 0\n` |
@@CASES
run_case "123" $'Sum: 6\n'
run_case "9005" $'Sum: 14\n'
run_case "-47" $'Sum: 11\n'
run_case "0" $'Sum: 0\n'
@@MAIN
n = int(input())

# TODO: посчитай сумму цифр и выведи Sum: <сумма>
print("TODO")
@@SOLUTION
n = abs(int(input()))

total = 0
while n > 0:
    total += n % 10
    n //= 10

print(f"Sum: {total}")
@@COMMENTED
n = abs(int(input()))

total = 0
# На каждом шаге добавляем последнюю цифру и отбрасываем её.
while n > 0:
    total += n % 10
    n //= 10

print(f"Sum: {total}")
@@END

@@TASK
section: 04_loops
dir: 03_max_digit
num: 4_3
title: PY_04_03. Максимальная цифра
topics: `while`, сравнение, цифры числа
input: Одно целое число
@@DESC
Считай целое число и выведи его максимальную цифру:

~~~text
Max digit: <цифра>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `123` | `Max digit: 3` |
| `9005` | `Max digit: 9` |
| `-47` | `Max digit: 7` |
@@THEORY
## Алгоритм

1. Взять модуль числа.
2. Завести `best = 0`.
3. Пока число больше нуля:
   - выделить последнюю цифру `n % 10`;
   - если она больше `best`, обновить `best`;
   - отбросить цифру: `n //= 10`.

~~~python
n = abs(int(input()))
best = 0
while n > 0:
    digit = n % 10
    if digit > best:
        best = digit
    n //= 10
~~~

## Почему `best = 0`

Цифры лежат в диапазоне `0..9`, поэтому ноль — безопасное начальное
значение. Для числа `0` ответ тоже `0`.

## Ранний выход

Если встретилась девятка, дальше искать нет смысла:

~~~python
if best == 9:
    break
~~~

`break` немедленно завершает цикл. В этой задаче оптимизация не нужна,
но приём полезен.

## Сравнение с суммой цифр

Сумма накапливается через `+=`, максимум обновляется через условие.
Похожие циклы часто встречаются вместе.
@@TESTS
| `123` | `Max digit: 3\n` |
| `9005` | `Max digit: 9\n` |
| `-47` | `Max digit: 7\n` |
| `0` | `Max digit: 0\n` |
@@CASES
run_case "123" $'Max digit: 3\n'
run_case "9005" $'Max digit: 9\n'
run_case "-47" $'Max digit: 7\n'
run_case "0" $'Max digit: 0\n'
@@MAIN
n = int(input())

# TODO: найди максимальную цифру и выведи Max digit: <цифра>
print("TODO")
@@SOLUTION
n = abs(int(input()))

best = 0
while n > 0:
    digit = n % 10
    if digit > best:
        best = digit
    n //= 10

print(f"Max digit: {best}")
@@COMMENTED
n = abs(int(input()))

best = 0
while n > 0:
    digit = n % 10
    # Обновляем максимум, только если цифра больше.
    if digit > best:
        best = digit
    n //= 10

print(f"Max digit: {best}")
@@END

@@TASK
section: 04_loops
dir: 04_reverse_number
num: 4_4
title: PY_04_04. Разворот числа
topics: `while`, цифры, знак числа
input: Одно целое число
@@DESC
Разверни цифры числа и выведи результат:

~~~text
Reversed: <число>
~~~

Ведущие нули не печатаются: для `1200` получается `21`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `123` | `Reversed: 321` |
| `1200` | `Reversed: 21` |
| `-45` | `Reversed: -54` |
@@THEORY
## Сборка числа

~~~python
result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10
~~~

Для `123`:

| Шаг | `n` | `result` |
| --- | --- | --- |
| 1 | 123 | 3 |
| 2 | 12 | 32 |
| 3 | 1 | 321 |

## Знак

Отделяем знак до цикла:

~~~python
sign = -1 if number < 0 else 1
n = abs(number)
~~~

В конце умножаем результат на `sign`.

## Ведущие нули

Для `1200` после первого шага `result = 0`, затем `0 * 10 + 0 = 0`,
и только потом появляются `2` и `1`. Итог `21` — ровно как у числа.

## Альтернатива через строку

~~~python
text = input()
sign = "-" if text.startswith("-") else ""
digits = text.lstrip("-")
print(sign + digits[::-1].lstrip("0") or "0")
~~~

Строковый вариант короче, но требует аккуратной обработки нуля. Цикл
с `%` и `//` проще проверить.
@@TESTS
| `123` | `Reversed: 321\n` |
| `1200` | `Reversed: 21\n` |
| `-45` | `Reversed: -54\n` |
| `0` | `Reversed: 0\n` |
@@CASES
run_case "123" $'Reversed: 321\n'
run_case "1200" $'Reversed: 21\n'
run_case "-45" $'Reversed: -54\n'
run_case "0" $'Reversed: 0\n'
@@MAIN
number = int(input())

# TODO: разверни число и выведи Reversed: <число>
print("TODO")
@@SOLUTION
number = int(input())

sign = -1 if number < 0 else 1
n = abs(number)

result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10

print(f"Reversed: {sign * result}")
@@COMMENTED
number = int(input())

# Знак запоминаем отдельно, со всеми цифрами работаем как с положительными.
sign = -1 if number < 0 else 1
n = abs(number)

result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10

print(f"Reversed: {sign * result}")
@@END

@@TASK
section: 04_loops
dir: 05_fizzbuzz
num: 4_5
title: PY_04_05. FizzBuzz
topics: `for`, `range`, `%`, `elif`
input: Одно целое число `n`
@@DESC
Выведи числа от 1 до `n`. Вместо чисел, кратных 3, печатай `Fizz`,
вместо кратных 5 — `Buzz`, вместо кратных и 3, и 5 — `FizzBuzz`:

~~~text
1
2
Fizz
4
Buzz
...
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5` | `1`<br>`2`<br>`Fizz`<br>`4`<br>`Buzz` |
| `15` | ...<br>`FizzBuzz` |
@@THEORY
## Цикл

~~~python
for i in range(1, n + 1):
    ...
~~~

`range(1, n + 1)` даёт `1, 2, ..., n`. Правая граница не включается,
поэтому нужен `+ 1`.

## Порядок проверок

Сначала самое сильное условие — кратность 15:

~~~python
if i % 15 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)
~~~

Если начать с `% 3`, число 15 попадёт в ветку `Fizz` и до `FizzBuzz`
не дойдёт. `elif` проверяется только тогда, когда предыдущие условия
ложны.

## `elif`

`elif` — сокращение от `else if`. Ветки идут сверху вниз, выполняется
первая подходящая.

## Компактная запись

~~~python
word = "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
print(word or i)
~~~

`True` ведёт себя как `1`, `False` — как `0`. Пустая строка ложна,
поэтому `word or i` печатает число, если слово пустое. Это трюк для
опытных; в решении лучше явные `if`.
@@TESTS
| `5` | `1\n2\nFizz\n4\nBuzz\n` |
| `3` | `1\n2\nFizz\n` |
| `15` | `1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n` |
@@CASES
run_case "5" $'1\n2\nFizz\n4\nBuzz\n'
run_case "3" $'1\n2\nFizz\n'
run_case "15" $'1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n'
@@MAIN
n = int(input())

# TODO: выведи FizzBuzz от 1 до n
print("TODO")
@@SOLUTION
n = int(input())

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
@@COMMENTED
n = int(input())

for i in range(1, n + 1):
    # Проверка на 15 идёт первой: 15 делится и на 3, и на 5.
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
@@END

@@TASK
section: 04_loops
dir: 06_unpaired_number
num: 4_6
title: PY_04_06. Непарное число
topics: `for`, XOR `^`, поиск пары
input: Число `n`, затем `n` целых чисел
@@DESC
В последовательности каждое число встречается дважды, кроме одного.
Найди и выведи его:

~~~text
Unpaired: <число>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 2 1` | `Unpaired: 3` |
| `1`<br>`42` | `Unpaired: 42` |
@@THEORY
## Свойство XOR

Побитовое исключающее ИЛИ `^`:

| `a` | `b` | `a ^ b` |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Свойства:

- `x ^ x == 0`;
- `x ^ 0 == x`;
- порядок не важен: `a ^ b ^ c == c ^ a ^ b`.

## Алгоритм

~~~python
result = 0
for value in numbers:
    result ^= value
~~~

Пары взаимно уничтожаются, остаётся единственное непарное число.

## Проверка

Для `1 2 3 2 1`:

~~~text
0 ^ 1 = 1
1 ^ 2 = 3
3 ^ 3 = 0
0 ^ 2 = 2
2 ^ 1 = 3
~~~

## Альтернатива через словарь

~~~python
from collections import Counter
result = [x for x, c in Counter(numbers).items() if c == 1][0]
~~~

Тоже правильно, но XOR использует `O(1)` дополнительной памяти.
@@TESTS
| `5\n1 2 3 2 1` | `Unpaired: 3\n` |
| `7\n4 4 9 9 5 5 7` | `Unpaired: 7\n` |
| `1\n42` | `Unpaired: 42\n` |
@@CASES
run_case $'5\n1 2 3 2 1' $'Unpaired: 3\n'
run_case $'7\n4 4 9 9 5 5 7' $'Unpaired: 7\n'
run_case $'1\n42' $'Unpaired: 42\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: найди число без пары и выведи Unpaired: <число>
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

result = 0
for value in numbers:
    result ^= value

print(f"Unpaired: {result}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# Пары одинаковых чисел дают 0, поэтому остаётся только непарное.
result = 0
for value in numbers:
    result ^= value

print(f"Unpaired: {result}")
@@END
