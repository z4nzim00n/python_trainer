@@TASK
section: 13_advanced
dir: 01_generic_max
num: 13_1
title: PY_13_01. Обобщённый максимум
topics: аннотации типов, `TypeVar`, `Sequence`
input: Число `n`, затем `n` целых чисел
@@DESC
Напиши функцию `max_value`, которая возвращает максимальный элемент
последовательности. Используй аннотации типов и `TypeVar`. Выведи:

~~~text
Max: <число>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`3 7 2 9 4` | `Max: 9` |
| `1`<br>`-5` | `Max: -5` |
@@THEORY
## Динамическая типизация

Python не проверяет типы при запуске:

~~~python
def first(items):
    return items[0]
~~~

Функция работает со списком, строкой, кортежем — с чем угодно, у чего
есть индексация. Это называют утиной типизацией.

## Аннотации

~~~python
from typing import Sequence, TypeVar

T = TypeVar("T")

def max_value(items: Sequence[T]) -> T:
    return max(items)
~~~

Аннотации не влияют на выполнение, но помогают IDE и проверяющим
инструментам вроде `mypy`.

## `TypeVar`

`T` — переменная типа. Одна и та же `T` в аргументе и результате
означает: «вернётся такой же тип, как элементы».

~~~python
max_value([1, 2, 3])        # int
max_value(["a", "b"])       # str
~~~

## Ограничения

`max` требует сравнимости элементов. Если нужна строгая типизация,
используют протокол `SupportsRichComparison` или ограниченный `TypeVar`:

~~~python
T = TypeVar("T", int, float, str)
~~~

## Запуск проверки

~~~bash
pip install mypy
mypy solution.py
~~~

Для учебных заданий достаточно аннотаций и аккуратного кода.
@@TESTS
| `5\n3 7 2 9 4` | `Max: 9\n` |
| `1\n-5` | `Max: -5\n` |
| `4\n10 10 1 2` | `Max: 10\n` |
@@CASES
run_case $'5\n3 7 2 9 4' $'Max: 9\n'
run_case $'1\n-5' $'Max: -5\n'
run_case $'4\n10 10 1 2' $'Max: 10\n'
@@MAIN
from typing import Sequence, TypeVar

T = TypeVar("T")


def max_value(items: Sequence[T]) -> T:
    # TODO: верни максимальный элемент
    return items[0]


n = int(input())
numbers = list(map(int, input().split()))
print(f"Max: {max_value(numbers)}")
@@SOLUTION
from typing import Sequence, TypeVar

T = TypeVar("T")


def max_value(items: Sequence[T]) -> T:
    return max(items)


n = int(input())
numbers = list(map(int, input().split()))
print(f"Max: {max_value(numbers)}")
@@COMMENTED
from typing import Sequence, TypeVar

# T — переменная типа: функция обобщённая, но возвращает тот же тип.
T = TypeVar("T")


def max_value(items: Sequence[T]) -> T:
    return max(items)


n = int(input())
numbers = list(map(int, input().split()))
print(f"Max: {max_value(numbers)}")
@@END

@@TASK
section: 13_advanced
dir: 02_lambda_sort
num: 13_2
title: PY_13_02. Сортировка с лямбдой
topics: `lambda`, `key`, сортировка кортежей
input: Число `n`, затем `n` строк «имя балл»
@@DESC
Отсортируй участников по баллам по убыванию. При равных баллах —
по имени по возрастанию. Выведи:

~~~text
<имя>: <балл>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`Ada 90`<br>`Bob 75`<br>`Cy 90` | `Ada: 90`<br>`Cy: 90`<br>`Bob: 75` |
| `2`<br>`Zoe 100`<br>`Amy 100` | `Amy: 100`<br>`Zoe: 100` |
@@THEORY
## `lambda`

~~~python
square = lambda x: x * x
~~~

Лямбда — короткая функция без имени. Удобна для одноразового правила.

## `key` в сортировке

~~~python
people.sort(key=lambda person: (-person[1], person[0]))
~~~

`key` возвращает значение, по которому сравниваются элементы. Кортеж
сравнивается покомпонентно:

1. сначала `-score` — по возрастанию минуса, то есть по убыванию балла;
2. при равенстве — `name` по возрастанию.

## Почему минус

Сортировка по умолчанию возрастает. Минус переворачивает порядок чисел
без `reverse=True`. Но `reverse=True` развернул бы и имена, а нам нужно
разное направление для полей.

## `sorted`

~~~python
sorted(people, key=lambda person: (-person[1], person[0]))
~~~

Возвращает новый список. `sort` сортирует на месте.

## Устойчивость

Можно сортировать в два прохода: сначала по имени, потом по баллам:

~~~python
people.sort(key=lambda p: p[0])
people.sort(key=lambda p: p[1], reverse=True)
~~~

Устойчивая сортировка сохранит порядок имён внутри одинаковых баллов.
@@TESTS
| `3\nAda 90\nBob 75\nCy 90` | `Ada: 90\nCy: 90\nBob: 75\n` |
| `2\nZoe 100\nAmy 100` | `Amy: 100\nZoe: 100\n` |
| `3\nL 5\nM 9\nN 1` | `M: 9\nL: 5\nN: 1\n` |
@@CASES
run_case $'3\nAda 90\nBob 75\nCy 90' $'Ada: 90\nCy: 90\nBob: 75\n'
run_case $'2\nZoe 100\nAmy 100' $'Amy: 100\nZoe: 100\n'
run_case $'3\nL 5\nM 9\nN 1' $'M: 9\nL: 5\nN: 1\n'
@@MAIN
n = int(input())
people = []
for _ in range(n):
    name, score = input().split()
    people.append((name, int(score)))

# TODO: отсортируй по баллам убыв., при равенстве — по имени
print("TODO")
@@SOLUTION
n = int(input())
people = []
for _ in range(n):
    name, score = input().split()
    people.append((name, int(score)))

people.sort(key=lambda person: (-person[1], person[0]))

for name, score in people:
    print(f"{name}: {score}")
@@COMMENTED
n = int(input())
people = []
for _ in range(n):
    name, score = input().split()
    people.append((name, int(score)))

# Кортеж в key задаёт два правила: минус балла и имя по возрастанию.
people.sort(key=lambda person: (-person[1], person[0]))

for name, score in people:
    print(f"{name}: {score}")
@@END

@@TASK
section: 13_advanced
dir: 03_comprehension_algorithms
num: 13_3
title: PY_13_03. Генераторы и алгоритмы
topics: генераторные выражения, `sum`, `filter`, `map`
input: Число `n`, затем `n` целых чисел
@@DESC
Посчитай сумму квадратов чётных чисел:

~~~text
Sum: <сумма>
~~~

Например, для `1 2 3 4 5` ответ `20`: `2^2 + 4^2`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `5`<br>`1 2 3 4 5` | `Sum: 20` |
| `4`<br>`2 2 2 2` | `Sum: 16` |
| `3`<br>`1 3 5` | `Sum: 0` |
@@THEORY
## Генераторное выражение

~~~python
result = sum(x * x for x in numbers if x % 2 == 0)
~~~

Выражение вычисляется лениво: промежуточный список не создаётся.
`sum` забирает значения по одному.

## Список против генератора

~~~python
squares = [x * x for x in numbers if x % 2 == 0]  # список
squares = (x * x for x in numbers if x % 2 == 0)  # генератор
~~~

Скобки `()` создают генератор. Для `sum`, `any`, `all` это экономит
память.

## `filter` и `map`

~~~python
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, evens)
result = sum(squares)
~~~

Функциональный стиль. В Python генераторы читаются проще.

## `any` и `all`

~~~python
any(x < 0 for x in numbers)   # есть ли отрицательное
all(x > 0 for x in numbers)   # все ли положительные
~~~

`any` и `all` тоже ленивы: останавливаются на первом решающем элементе.

## Отрицательные чётные

`-2 % 2 == 0`, поэтому `-2` считается чётным. Это соответствует
математическому определению.
@@TESTS
| `5\n1 2 3 4 5` | `Sum: 20\n` |
| `4\n2 2 2 2` | `Sum: 16\n` |
| `3\n1 3 5` | `Sum: 0\n` |
| `4\n-2 1 2 3` | `Sum: 8\n` |
@@CASES
run_case $'5\n1 2 3 4 5' $'Sum: 20\n'
run_case $'4\n2 2 2 2' $'Sum: 16\n'
run_case $'3\n1 3 5' $'Sum: 0\n'
run_case $'4\n-2 1 2 3' $'Sum: 8\n'
@@MAIN
n = int(input())
numbers = list(map(int, input().split()))

# TODO: посчитай сумму квадратов чётных чисел
print("TODO")
@@SOLUTION
n = int(input())
numbers = list(map(int, input().split()))

result = sum(x * x for x in numbers if x % 2 == 0)
print(f"Sum: {result}")
@@COMMENTED
n = int(input())
numbers = list(map(int, input().split()))

# Генератор не создаёт промежуточный список.
result = sum(x * x for x in numbers if x % 2 == 0)
print(f"Sum: {result}")
@@END

@@TASK
section: 13_advanced
dir: 04_operator_overload
num: 13_4
title: PY_13_04. Перегрузка операторов
topics: `__add__`, `__str__`, dunder-методы
input: Два вектора (две строки)
@@DESC
Опиши класс `Vector` с координатами `x` и `y`. Перегрузи `+` так,
чтобы векторы складывались, и `__str__` для вывода:

~~~text
(<x>, <y>)
~~~

Считай два вектора и выведи их сумму.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `1 2`<br>`3 4` | `(4, 6)` |
| `0 0`<br>`0 0` | `(0, 0)` |
@@THEORY
## Dunder-методы

Методы с двумя подчёркиваниями задают поведение встроенных операций:

| Метод | Операция |
| --- | --- |
| `__init__` | создание объекта |
| `__str__` | `str(obj)`, `print` |
| `__add__` | `a + b` |
| `__sub__` | `a - b` |
| `__eq__` | `a == b` |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |

## Сложение

~~~python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
~~~

`a + b` превращается в `a.__add__(b)`.

## Новый объект

`__add__` не меняет исходные векторы, а возвращает новый. Так работают
числа и строки: `a + b` не изменяет `a`.

## Проверка типа

~~~python
def __add__(self, other):
    if not isinstance(other, Vector):
        return NotImplemented
    ...
~~~

`NotImplemented` позволяет Python попробовать `other.__radd__`.

## `@dataclass`

~~~python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
~~~

Автоматически создаёт `__init__`, `__repr__` и `__eq__`. Для простых
структур данных это удобно.
@@TESTS
| `1 2\n3 4` | `(4, 6)\n` |
| `0 0\n0 0` | `(0, 0)\n` |
| `-1 5\n1 -5` | `(0, 0)\n` |
@@CASES
run_case $'1 2\n3 4' $'(4, 6)\n'
run_case $'0 0\n0 0' $'(0, 0)\n'
run_case $'-1 5\n1 -5' $'(0, 0)\n'
@@MAIN
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # TODO: верни новый Vector — сумму координат
        return Vector(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Vector(*map(int, input().split()))
b = Vector(*map(int, input().split()))
print(a + b)
@@SOLUTION
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Vector(*map(int, input().split()))
b = Vector(*map(int, input().split()))
print(a + b)
@@COMMENTED
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # a + b вызывает a.__add__(b); возвращаем новый объект.
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


a = Vector(*map(int, input().split()))
b = Vector(*map(int, input().split()))
print(a + b)
@@END
