@@TASK
section: 01_basics
dir: 01_hello_world
num: 1_1
title: PY_01_01. Первая программа
topics: `print`, строки, запуск скрипта
input: Не требуются
@@DESC
Напиши программу, которая выводит строку:

~~~text
Hello, Python!
~~~

Программа на Python — это текстовый файл `.py`, который читается сверху
вниз. Для вывода используется функция `print`.

~~~python
print("Hello, Python!")
~~~

`print` печатает значение и добавляет перевод строки.
@@EXAMPLES
| *(нет ввода)* | `Hello, Python!` |
@@THEORY
## Первая строка

~~~python
print("Hello, Python!")
~~~

`print` — встроенная функция. В скобках указывается значение, которое нужно
вывести. Строка записывается в кавычках: `"..."` или `'...'`.

## Перевод строки

Каждый `print` завершает вывод переводом строки:

~~~python
print("one")
print("two")
~~~

~~~text
one
two
~~~

Если нужен вывод без перевода строки, используют параметр `end`:

~~~python
print("one", end="")
print("two")
~~~

~~~text
onetwo
~~~

## Запуск

~~~bash
python main.py
~~~

Python не компилирует программу в отдельный файл: интерпретатор читает
исходник и сразу выполняет инструкции.

## Частые ошибки

| Ошибка | Сообщение |
| --- | --- |
| Нет закрывающей кавычки | `SyntaxError: unterminated string literal` |
| Нет скобок у `print` | `SyntaxError: Missing parentheses in call to 'print'` |
| Неверный отступ | `IndentationError` |
@@TESTS
| *(нет ввода)* | `Hello, Python!\n` |
@@CASES
run_case_devnull $'Hello, Python!\n'
@@MAIN
# TODO: выведи строку Hello, Python!
print("TODO")
@@SOLUTION
print("Hello, Python!")
@@COMMENTED
# print печатает строку и добавляет перевод строки.
print("Hello, Python!")
@@END

@@TASK
section: 01_basics
dir: 02_fix_print
num: 1_2
title: PY_01_02. Исправь print
topics: `print`, синтаксис Python 3
input: Не требуются
@@DESC
В программе остался синтаксис Python 2: `print` записан без скобок.
Исправь строку, чтобы программа вывела:

~~~text
Fixed!
~~~
@@EXAMPLES
| *(нет ввода)* | `Fixed!` |
@@THEORY
## Функция, а не оператор

В Python 3 `print` — обычная функция, поэтому аргументы обязаны быть
в скобках:

~~~python
print("Fixed!")
~~~

Старая запись `print "Fixed!"` работала только в Python 2. Современный
интерпретатор сообщает:

~~~text
SyntaxError: Missing parentheses in call to 'print'
~~~

## Почему ошибка синтаксиса

Интерпретатор разбирает весь файл до запуска. Если синтаксис неверен,
программа не выполнится вообще — даже строки до ошибки.

## Другие следы Python 2

| Python 2 | Python 3 |
| --- | --- |
| `print "text"` | `print("text")` |
| `raw_input()` | `input()` |
| `xrange(10)` | `range(10)` |
| `except Exception, e:` | `except Exception as e:` |
@@TESTS
| *(нет ввода)* | `Fixed!\n` |
@@CASES
run_case_devnull $'Fixed!\n'
@@MAIN
# TODO: исправь вызов print под Python 3
print "Fixed!"
@@SOLUTION
print("Fixed!")
@@COMMENTED
# В Python 3 print — функция, аргумент заключается в скобки.
print("Fixed!")
@@END

@@TASK
section: 01_basics
dir: 03_fix_indent
num: 1_3
title: PY_01_03. Исправь отступ
topics: отступы, блоки кода, `if`
input: Не требуются
@@DESC
В программе нарушен отступ: тело `if` должно быть сдвинуто вправо.
Исправь код, чтобы он вывел:

~~~text
Positive
~~~

Затем измени значение `value` на `-5` и убедись, что программа ничего
не печатает.
@@EXAMPLES
| *(нет ввода)* | `Positive` |
@@THEORY
## Отступы — часть синтаксиса

В Python границы блока задаются отступами, а не фигурными скобками:

~~~python
value = 7
if value > 0:
    print("Positive")
~~~

Строка `print` сдвинута на 4 пробела, поэтому относится к телу `if`.
Если убрать отступ, интерпретатор сообщит:

~~~text
IndentationError: expected an indented block
~~~

## Сколько пробелов

Стандарт PEP 8 рекомендует 4 пробела на каждый уровень. Главное —
быть последовательным: смешивать пробелы и табуляцию нельзя.

~~~python
if True:
    print("one level")
    if True:
        print("two levels")
~~~

## Двоеточие

После `if`, `for`, `while`, `def` и `class` ставится `:` — он открывает
блок. Без двоеточия тоже будет `SyntaxError`.
@@TESTS
| *(нет ввода)* | `Positive\n` |
@@CASES
run_case_devnull $'Positive\n'
@@MAIN
value = 7

if value > 0:
# TODO: добавь отступ у print
print("Positive")
@@SOLUTION
value = 7

if value > 0:
    print("Positive")
@@COMMENTED
value = 7

# Тело if выделяется отступом в 4 пробела.
if value > 0:
    print("Positive")
@@END

@@TASK
section: 01_basics
dir: 04_variables_output
num: 1_4
title: PY_01_04. Переменные
topics: переменные, `str`, `int`, f-строки
input: Не требуются
@@DESC
Создай две переменные:

- `language` со значением `Python`;
- `year` со значением `1991`.

Выведи:

~~~text
Language: Python
Year: 1991
~~~
@@EXAMPLES
| *(нет ввода)* | `Language: Python`<br>`Year: 1991` |
@@THEORY
## Присваивание

~~~python
language = "Python"
year = 1991
~~~

Тип переменной не указывается: Python определяет его по значению.
`"Python"` — строка (`str`), `1991` — целое число (`int`).

## Вывод нескольких значений

Самый удобный способ — f-строка:

~~~python
print(f"Language: {language}")
print(f"Year: {year}")
~~~

Буква `f` перед кавычками включает подстановку выражений в `{ ... }`.

Можно и склеить строки:

~~~python
print("Language: " + language)
print("Year: " + str(year))
~~~

`str` превращает число в строку: `+` не умеет складывать `str` и `int`.

## Основные типы

| Тип | Пример | Назначение |
| --- | --- | --- |
| `int` | `42` | целые числа |
| `float` | `3.14` | дробные числа |
| `str` | `"text"` | строки |
| `bool` | `True` | логический |
| `NoneType` | `None` | отсутствие значения |

## `type`

~~~python
print(type(year))  # <class 'int'>
~~~
@@TESTS
| *(нет ввода)* | `Language: Python\nYear: 1991\n` |
@@CASES
run_case_devnull $'Language: Python\nYear: 1991\n'
@@MAIN
language = "Python"
year = 1991

# TODO: выведи две строки: Language: Python и Year: 1991
print("TODO")
@@SOLUTION
language = "Python"
year = 1991

print(f"Language: {language}")
print(f"Year: {year}")
@@COMMENTED
language = "Python"
year = 1991

# f-строка подставляет значения переменных в фигурные скобки.
print(f"Language: {language}")
print(f"Year: {year}")
@@END

@@TASK
section: 01_basics
dir: 05_swap_two_numbers
num: 1_5
title: PY_01_05. Обмен значений
topics: `input`, `split`, `map`, кортежи
input: Два целых числа через пробел
@@DESC
Считай два целых числа и выведи их в обратном порядке через пробел:

~~~text
<b> <a>
~~~

Например, для `3 5` вывод должен быть `5 3`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 5` | `5 3` |
| `-1 10` | `10 -1` |
@@THEORY
## Чтение двух чисел

~~~python
a, b = map(int, input().split())
~~~

- `input()` читает строку целиком;
- `split()` делит её по пробелам;
- `map(int, ...)` применяет `int` к каждой части;
- распаковка `a, b = ...` кладёт два значения в две переменные.

## Обмен через кортеж

~~~python
a, b = b, a
~~~

Справа создаётся кортеж `(b, a)`, затем он распаковывается в `a` и `b`.
Временная переменная не нужна.

Классический вариант тоже работает:

~~~python
temp = a
a = b
b = temp
~~~

## Вывод

~~~python
print(a, b)
~~~

`print` с несколькими аргументами разделяет их пробелом и добавляет
перевод строки.

## Если ввод пуст

`input()` при EOF бросает `EOFError`, а `int("abc")` — `ValueError`.
В задачах ввод корректный.
@@TESTS
| `3 5` | `5 3\n` |
| `-1 10` | `10 -1\n` |
@@CASES
run_case "3 5" $'5 3\n'
run_case "-1 10" $'10 -1\n'
@@MAIN
a, b = map(int, input().split())

# TODO: поменяй значения местами и выведи их через пробел
print("TODO")
@@SOLUTION
a, b = map(int, input().split())

a, b = b, a
print(a, b)
@@COMMENTED
a, b = map(int, input().split())

# Справа создаётся кортеж (b, a), потом он распаковывается обратно.
a, b = b, a
print(a, b)
@@END

@@TASK
section: 02_input_output
dir: 01_echo_number
num: 2_1
title: PY_02_01. Эхо числа
topics: `input`, `int`, f-строки
input: Одно целое число
@@DESC
Считай целое число и выведи его в формате:

~~~text
Number: <число>
~~~

Например, для `42` вывод `Number: 42`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `42` | `Number: 42` |
| `-7` | `Number: -7` |
@@THEORY
## `input` возвращает строку

~~~python
line = input()
print(type(line))  # <class 'str'>
~~~

Даже если пользователь ввёл `42`, `input` вернёт строку `"42"`.

## Преобразование в число

~~~python
number = int(line)
print(f"Number: {number}")
~~~

`int` разбирает строку как целое число. Пробелы по краям он игнорирует.

## Ошибки преобразования

~~~python
int("abc")     # ValueError
int("3.14")    # ValueError: int принимает только целые
~~~

Для дробных чисел нужен `float("3.14")`.

## Отладка

Полезно проверять тип:

~~~python
print(repr(line), type(line))
~~~

`repr` показывает строку в кавычках — так видно скрытые пробелы.
@@TESTS
| `42` | `Number: 42\n` |
| `-7` | `Number: -7\n` |
@@CASES
run_case "42" $'Number: 42\n'
run_case "-7" $'Number: -7\n'
@@MAIN
line = input()

# TODO: преобразуй строку в число и выведи Number: <число>
print("TODO")
@@SOLUTION
line = input()
number = int(line)

print(f"Number: {number}")
@@COMMENTED
line = input()

# int превращает текст в целое число.
number = int(line)

print(f"Number: {number}")
@@END

@@TASK
section: 02_input_output
dir: 02_sum_two_numbers
num: 2_2
title: PY_02_02. Сумма двух чисел
topics: `split`, `map`, арифметика
input: Два целых числа через пробел
@@DESC
Считай два целых числа и выведи их сумму:

~~~text
Sum: <сумма>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `2 3` | `Sum: 5` |
| `-4 4` | `Sum: 0` |
@@THEORY
## Разбор строки

~~~python
a, b = map(int, input().split())
~~~

`split()` без аргумента делит строку по любым пробельным символам,
включая несколько пробелов и табуляцию.

## Сложение

~~~python
total = a + b
print(f"Sum: {total}")
~~~

## Целые числа не переполняются

В Python `int` имеет произвольную точность:

~~~python
print(10 ** 30)  # огромное число, ошибки нет
~~~

В C# или Java такой пример переполнил бы `int`, а здесь можно не думать
о разрядности.

## Несколько чисел в строке

Если чисел больше двух, удобно собрать список:

~~~python
numbers = list(map(int, input().split()))
print(sum(numbers))
~~~
@@TESTS
| `2 3` | `Sum: 5\n` |
| `-4 4` | `Sum: 0\n` |
| `100 200` | `Sum: 300\n` |
@@CASES
run_case "2 3" $'Sum: 5\n'
run_case "-4 4" $'Sum: 0\n'
run_case "100 200" $'Sum: 300\n'
@@MAIN
a, b = map(int, input().split())

# TODO: выведи Sum: <a + b>
print("TODO")
@@SOLUTION
a, b = map(int, input().split())

total = a + b
print(f"Sum: {total}")
@@COMMENTED
a, b = map(int, input().split())

# Сначала вычисляем, потом печатаем.
total = a + b
print(f"Sum: {total}")
@@END

@@TASK
section: 02_input_output
dir: 03_read_full_line
num: 2_3
title: PY_02_03. Строка целиком
topics: `input`, пробелы в строке
input: Одна строка текста
@@DESC
Считай строку целиком, включая пробелы, и выведи её в формате:

~~~text
Line: <строка>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello world` | `Line: hello world` |
| `a b c` | `Line: a b c` |
@@THEORY
## `input` читает всю строку

~~~python
line = input()
print(f"Line: {line}")
~~~

`input` читает всё до перевода строки, поэтому пробелы внутри сохраняются.
Он убирает только завершающий `\n`.

## Чем это отличается от `split`

`split` делит строку на части:

~~~python
print("hello world".split())  # ['hello', 'world']
~~~

Если пробелы важны, `split` использовать нельзя — он их теряет.

## Пустая строка

Если нажать Enter сразу, `input()` вернёт пустую строку `""`:

~~~python
line = input()
print(f"Line: {line}")
~~~

~~~text
Line:
~~~

## Пробелы по краям

`input` сохраняет ведущие и хвостовые пробелы. Убрать их можно методами
`strip`, `lstrip`, `rstrip`:

~~~python
line = input().strip()
~~~
@@TESTS
| `hello world` | `Line: hello world\n` |
| `a b c` | `Line: a b c\n` |
| `` (пустая строка) | `Line: \n` |
@@CASES
run_case "hello world" $'Line: hello world\n'
run_case "a b c" $'Line: a b c\n'
run_case "" $'Line: \n'
@@MAIN
line = input()

# TODO: выведи строку целиком после префикса Line:
print("TODO")
@@SOLUTION
line = input()

print(f"Line: {line}")
@@COMMENTED
line = input()

# input сохраняет пробелы внутри строки, поэтому текст не теряется.
print(f"Line: {line}")
@@END

@@TASK
section: 02_input_output
dir: 04_formatted_output
num: 2_4
title: PY_02_04. Форматирование числа
topics: `float`, f-строки, формат `:.2f`
input: Одно дробное число
@@DESC
Считай дробное число и выведи его с двумя знаками после запятой:

~~~text
Value: 3.14
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3.14159` | `Value: 3.14` |
| `2` | `Value: 2.00` |
@@THEORY
## Чтение `float`

~~~python
value = float(input())
~~~

`float` принимает и `"3.14"`, и `"2"`, и `"-0.5"`, и даже `"1e3"`.

## Формат f-строки

~~~python
print(f"Value: {value:.2f}")
~~~

`.2f` означает: два знака после точки, вывод в формате с фиксированной
точкой. Число округляется по правилам IEEE 754.

## Другие форматы

| Запись | Результат для `3.14159` |
| --- | --- |
| `{value:.0f}` | `3` |
| `{value:.2f}` | `3.14` |
| `{value:.4f}` | `3.1416` |
| `{value:8.2f}` | `    3.14` (ширина 8) |
| `{value:e}` | `3.141590e+00` |

## Локаль

В отличие от C#, Python не зависит от системной локали: разделитель —
всегда точка. Поэтому `3.14` выглядит одинаково на всех машинах.

## Округление

`round(2.675, 2)` может дать `2.67`, потому что число `2.675` не
представимо точно в двоичной системе. Формат `:.2f` ведёт себя так же.
@@TESTS
| `3.14159` | `Value: 3.14\n` |
| `2` | `Value: 2.00\n` |
| `-0.5` | `Value: -0.50\n` |
@@CASES
run_case "3.14159" $'Value: 3.14\n'
run_case "2" $'Value: 2.00\n'
run_case "-0.5" $'Value: -0.50\n'
@@MAIN
value = float(input())

# TODO: выведи Value: <число с двумя знаками после точки>
print("TODO")
@@SOLUTION
value = float(input())

print(f"Value: {value:.2f}")
@@COMMENTED
value = float(input())

# .2f — два знака после точки.
print(f"Value: {value:.2f}")
@@END

@@TASK
section: 02_input_output
dir: 05_mixed_input
num: 2_5
title: PY_02_05. Смешанный ввод
topics: `input`, `int`, чтение нескольких строк
input: Число и строка (две строки)
@@DESC
Сначала считай целое число, затем строку. Выведи:

~~~text
<имя>: <число>
~~~

Например, для:

~~~text
3
Ada
~~~

вывод должен быть `Ada: 3`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`Ada` | `Ada: 3` |
| `42`<br>`Bob` | `Bob: 42` |
@@THEORY
## Два вызова `input`

Каждый `input` читает одну строку:

~~~python
number = int(input())
name = input()
print(f"{name}: {number}")
~~~

Первый `input` забирает `3`, второй — `Ada`.

## Порядок важен

Если перепутать порядок, `int(input())` попытается превратить `Ada`
в число и получит `ValueError`. Сначала читаем то, что ожидаем.

## Чтение всех строк сразу

Иногда удобнее прочитать весь ввод:

~~~python
import sys
data = sys.stdin.read().splitlines()
~~~

`splitlines()` делит текст на строки без символов перевода строки.
В этой задаче достаточно двух `input`.

## Почему не `split` сразу

`split` разбил бы `Ada` на части, если бы в имени был пробел. Для строки
целиком нужен отдельный `input`.
@@TESTS
| `3\nAda` | `Ada: 3\n` |
| `42\nBob` | `Bob: 42\n` |
| `0\nX` | `X: 0\n` |
@@CASES
run_case $'3\nAda' $'Ada: 3\n'
run_case $'42\nBob' $'Bob: 42\n'
run_case $'0\nX' $'X: 0\n'
@@MAIN
number = int(input())
name = input()

# TODO: выведи <имя>: <число>
print("TODO")
@@SOLUTION
number = int(input())
name = input()

print(f"{name}: {number}")
@@COMMENTED
number = int(input())
name = input()

# Сначала число, потом строка — в том же порядке, как во вводе.
print(f"{name}: {number}")
@@END
