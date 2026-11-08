@@TASK
section: 09_errors
dir: 01_safe_division
num: 9_1
title: PY_09_01. Безопасное деление
topics: `try`, `except`, `ZeroDivisionError`
input: Два целых числа через пробел
@@DESC
Раздели первое число на второе. Если делитель равен нулю, выведи
`Error: division by zero`, иначе `Result: <частное>`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `10 2` | `Result: 5.0` |
| `5 0` | `Error: division by zero` |
@@THEORY
## Исключение

Деление на ноль бросает `ZeroDivisionError`:

~~~python
10 / 0  # ZeroDivisionError: division by zero
~~~

Если исключение не обработать, программа завершится с traceback.

## `try` / `except`

~~~python
try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: division by zero")
~~~

Сначала выполняется блок `try`. Если возникает исключение указанного
типа, управление переходит в `except`.

## Порядок

Важно: `print` с результатом стоит внутри `try`. Если бы он был после
блока, при ошибке переменная `result` не существовала бы.

## `finally`

~~~python
try:
    ...
except ZeroDivisionError:
    ...
finally:
    print("Done")
~~~

`finally` выполняется всегда — и при успехе, и при ошибке. Удобно для
освобождения ресурсов.

## Другие исключения

`ValueError` при неверном `int`, `TypeError` при несовместимых типах.
Ловить стоит конкретный тип, а не всё подряд.
@@TESTS
| `10 2` | `Result: 5.0\n` |
| `5 0` | `Error: division by zero\n` |
| `-9 3` | `Result: -3.0\n` |
@@CASES
run_case "10 2" $'Result: 5.0\n'
run_case "5 0" $'Error: division by zero\n'
run_case "-9 3" $'Result: -3.0\n'
@@MAIN
a, b = map(int, input().split())

# TODO: раздели a на b, обработай деление на ноль
print("TODO")
@@SOLUTION
a, b = map(int, input().split())

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: division by zero")
@@COMMENTED
a, b = map(int, input().split())

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    # Сюда управление попадает только при b == 0.
    print("Error: division by zero")
@@END

@@TASK
section: 09_errors
dir: 02_parse_int
num: 9_2
title: PY_09_02. Разбор числа
topics: `try`, `except`, `ValueError`
input: Одна строка
@@DESC
Попробуй превратить строку в целое число. При успехе выведи
`Number: <число>`, иначе `Error: invalid number`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `42` | `Number: 42` |
| `abc` | `Error: invalid number` |
@@THEORY
## `ValueError`

~~~python
int("42")   # 42
int("abc")  # ValueError: invalid literal for int()
int("3.5")  # ValueError: int принимает только целые
~~~

## Обработка

~~~python
try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    print("Error: invalid number")
~~~

## Почему не проверять `isdigit`

`str.isdigit()` не пропускает минус:

~~~python
"-7".isdigit()  # False
~~~

Пришлось бы отдельно разрешать знак. `try`/`except` проще и точнее
повторяет правила `int`.

## `else` и `finally`

~~~python
try:
    number = int(line)
except ValueError:
    print("Error")
else:
    print(f"Number: {number}")
~~~

`else` выполняется, только если исключения не было. Это позволяет
держать в `try` минимум кода.

## Не глотать всё

`except Exception` скрывает и опечатки в коде. Ловите конкретный тип.
@@TESTS
| `42` | `Number: 42\n` |
| `abc` | `Error: invalid number\n` |
| `-7` | `Number: -7\n` |
| `3.5` | `Error: invalid number\n` |
@@CASES
run_case "42" $'Number: 42\n'
run_case "abc" $'Error: invalid number\n'
run_case "-7" $'Number: -7\n'
run_case "3.5" $'Error: invalid number\n'
@@MAIN
line = input()

# TODO: преобразуй строку в int, обработай ValueError
print("TODO")
@@SOLUTION
line = input()

try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    print("Error: invalid number")
@@COMMENTED
line = input()

try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    # int бросает ValueError, если строка не является целым числом.
    print("Error: invalid number")
@@END

@@TASK
section: 09_errors
dir: 03_custom_exception
num: 9_3
title: PY_09_03. Своё исключение
topics: `Exception`, `raise`, `except`
input: Возраст (целое число)
@@DESC
Опиши исключение `NegativeAgeError`. Если возраст меньше нуля, брось его
и выведи `Error: negative age`. Иначе выведи `Age: <возраст>`.

Обработку сделай через `try`/`except`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `36` | `Age: 36` |
| `-1` | `Error: negative age` |
@@THEORY
## Свой класс исключения

~~~python
class NegativeAgeError(Exception):
    pass
~~~

Наследуемся от `Exception`. Тело может быть пустым: важнее имя типа,
по которому исключение ловят.

## `raise`

~~~python
if age < 0:
    raise NegativeAgeError("negative age")
~~~

`raise` прерывает обычное выполнение и передаёт управление ближайшему
подходящему `except`.

## Обработка

~~~python
try:
    check_age(age)
    print(f"Age: {age}")
except NegativeAgeError:
    print("Error: negative age")
~~~

## Зачем своё исключение

Стандартный `ValueError` мог бы прийти из десятка мест. Свой тип
позволяет отличить именно эту ошибку и дать понятное сообщение.

## Атрибуты

~~~python
class NegativeAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"age must be >= 0, got {age}")
        self.age = age
~~~

Так исключение несёт данные о проблеме.

## Иерархия

Все исключения наследуются от `BaseException`; обычные ошибки — от
`Exception`. Наследоваться стоит от `Exception`.
@@TESTS
| `36` | `Age: 36\n` |
| `-1` | `Error: negative age\n` |
| `0` | `Age: 0\n` |
@@CASES
run_case "36" $'Age: 36\n'
run_case "-1" $'Error: negative age\n'
run_case "0" $'Age: 0\n'
@@MAIN
class NegativeAgeError(Exception):
    pass


age = int(input())

# TODO: проверь возраст через try/except и NegativeAgeError
print("TODO")
@@SOLUTION
class NegativeAgeError(Exception):
    pass


age = int(input())

try:
    if age < 0:
        raise NegativeAgeError("negative age")
    print(f"Age: {age}")
except NegativeAgeError:
    print("Error: negative age")
@@COMMENTED
class NegativeAgeError(Exception):
    pass


age = int(input())

try:
    if age < 0:
        # raise прерывает try и передаёт управление в except.
        raise NegativeAgeError("negative age")
    print(f"Age: {age}")
except NegativeAgeError:
    print("Error: negative age")
@@END

@@TASK
section: 09_errors
dir: 04_context_manager
num: 9_4
title: PY_09_04. Контекстный менеджер
topics: `with`, `__enter__`, `__exit__`
input: Не требуются
@@DESC
Опиши класс `Resource`, который при входе в блок `with` печатает `Open`,
а при выходе — `Closed`. Внутри блока выведи `Using resource`:

~~~text
Open
Using resource
Closed
~~~
@@EXAMPLES
| *(нет ввода)* | `Open`<br>`Using resource`<br>`Closed` |
@@THEORY
## `with`

~~~python
with Resource() as resource:
    print("Using resource")
~~~

`with` гарантирует, что код выхода выполнится даже при исключении.
Именно так работают файлы:

~~~python
with open("input.txt", encoding="utf-8") as file:
    text = file.read()
~~~

Файл закроется автоматически.

## Протокол

~~~python
class Resource:
    def __enter__(self):
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closed")
        return False
~~~

- `__enter__` вызывается на входе; его результат попадает в `as`;
- `__exit__` вызывается на выходе и получает информацию об исключении.

## Возврат `__exit__`

| Значение | Поведение |
| --- | --- |
| `False` или `None` | исключение распространяется дальше |
| `True` | исключение подавляется |

Возвращать `True` стоит только осознанно.

## `contextlib`

Для простых случаев есть декоратор:

~~~python
from contextlib import contextmanager

@contextmanager
def resource():
    print("Open")
    yield
    print("Closed")
~~~

Функция с `yield` превращается в контекстный менеджер.
@@TESTS
| *(нет ввода)* | `Open\nUsing resource\nClosed\n` |
@@CASES
run_case_devnull $'Open\nUsing resource\nClosed\n'
@@MAIN
class Resource:
    def __enter__(self):
        # TODO: напечатай Open и верни self
        return self

    def __exit__(self, exc_type, exc, tb):
        # TODO: напечатай Closed
        return False


with Resource():
    print("Using resource")
@@SOLUTION
class Resource:
    def __enter__(self):
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closed")
        return False


with Resource():
    print("Using resource")
@@COMMENTED
class Resource:
    def __enter__(self):
        # Выполняется при входе в with.
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        # Выполняется при выходе, даже если было исключение.
        print("Closed")
        return False


with Resource():
    print("Using resource")
@@END

@@TASK
section: 09_errors
dir: 05_index_error
num: 9_5
title: PY_09_05. Индекс вне диапазона
topics: `IndexError`, индексы, `try`
input: Число `n` и индекс, затем `n` целых чисел
@@DESC
Считай список и индекс. Выведи элемент по индексу или сообщение
об ошибке:

~~~text
Value: <элемент>
~~~

~~~text
Error: index out of range
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 1`<br>`10 20 30` | `Value: 20` |
| `3 5`<br>`10 20 30` | `Error: index out of range` |
@@THEORY
## Индексация

~~~python
numbers = [10, 20, 30]
numbers[0]   # 10
numbers[2]   # 30
numbers[3]   # IndexError
~~~

Допустимые индексы: от `0` до `len(numbers) - 1`.

## Отрицательные индексы

~~~python
numbers[-1]  # 30
numbers[-3]  # 10
numbers[-4]  # IndexError
~~~

Отрицательный индекс считается с конца. Это не ошибка, пока не выходит
за границы.

## Обработка

~~~python
try:
    print(f"Value: {numbers[index]}")
except IndexError:
    print("Error: index out of range")
~~~

## Проверка заранее

~~~python
if -len(numbers) <= index < len(numbers):
    ...
else:
    ...
~~~

Такой вариант тоже правильный. `try`/`except` короче, если ошибка
ожидается редко.

## Срез не бросает ошибку

~~~python
numbers[10:20]  # []
~~~

Срез за границами возвращает пустой список, а не исключение. Это важное
отличие от обращения по индексу.
@@TESTS
| `3 1\n10 20 30` | `Value: 20\n` |
| `3 5\n10 20 30` | `Error: index out of range\n` |
| `3 -1\n10 20 30` | `Value: 30\n` |
| `3 -4\n10 20 30` | `Error: index out of range\n` |
@@CASES
run_case $'3 1\n10 20 30' $'Value: 20\n'
run_case $'3 5\n10 20 30' $'Error: index out of range\n'
run_case $'3 -1\n10 20 30' $'Value: 30\n'
run_case $'3 -4\n10 20 30' $'Error: index out of range\n'
@@MAIN
n, index = map(int, input().split())
numbers = list(map(int, input().split()))

# TODO: выведи элемент или сообщение об ошибке
print("TODO")
@@SOLUTION
n, index = map(int, input().split())
numbers = list(map(int, input().split()))

try:
    print(f"Value: {numbers[index]}")
except IndexError:
    print("Error: index out of range")
@@COMMENTED
n, index = map(int, input().split())
numbers = list(map(int, input().split()))

try:
    print(f"Value: {numbers[index]}")
except IndexError:
    # Индекс вышел за допустимый диапазон.
    print("Error: index out of range")
@@END
