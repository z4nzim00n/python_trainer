# Шпаргалка по Python

Коротко о том, что встречается в заданиях. Синтаксис — Python 3.10+.

---

## Запуск

```bash
python main.py
python -c "print(2 + 2)"
```

В Windows интерпретатор может называться `py`, в Linux/macOS —
`python3`. Проверка версии:

```bash
python --version
```

---

## Вывод и ввод

```python
print("Hello")
print("a", "b")              # a b — через пробел
print("a", "b", sep="-")     # a-b
print("no newline", end="")  # без перевода строки
print(f"x = {x}, y = {y}")   # f-строка
print(f"{value:.2f}")        # два знака после точки
```

```python
line = input()               # строка без завершающего \n
number = int(input())        # сразу число
a, b = map(int, input().split())
words = input().split()      # список слов
```

`input()` всегда возвращает `str`. `int("42")` — число, `int("4.2")` —
`ValueError`. Пустой ввод в автотесте даёт `EOFError`.

---

## Типы и переменные

```python
n = 42            # int
x = 3.14          # float
s = "text"        # str
ok = True         # bool (заглавные буквы)
nothing = None    # отсутствие значения
nums = [1, 2, 3]  # list
user = {"name": "Ann"}  # dict
tags = {"py", "code"}   # set
point = (1, 2)          # tuple
```

Python — язык с динамической типизацией: тип хранится в значении, а не
в переменной. Переменная — это имя, привязанное к объекту.

```python
a = 1
a = "one"   # допустимо
```

Проверка типа: `type(x)`, `isinstance(x, int)`.

---

## Числа

```python
7 // 2      # 3   целочисленное деление
7 % 2       # 1   остаток
7 / 2       # 3.5 всегда float
2 ** 10     # 1024
abs(-5)     # 5
round(3.14159, 2)   # 3.14
divmod(17, 5)       # (3, 2)
```

`int` в Python не переполняется: ограничено только памятью. `float` —
обычный double.

Приоритет: `**`, затем `* / // %`, затем `+ -`. Скобки решают сомнения.

### Точность float

```python
0.1 + 0.2 == 0.3   # False
```

Для денег и точных сравнений используйте `decimal.Decimal` или
сравнивайте с допуском.

---

## Строки

```python
s = "Hello"
len(s)              # 5
s[0]                # 'H'
s[-1]               # 'o'
s[1:4]              # 'ell'
s[::-1]             # 'olleH'
s.upper()           # 'HELLO'
s.lower()           # 'hello'
s.strip()           # без пробелов по краям
s.split()           # список слов
",".join(parts)     # собрать строку
s.replace("l", "L")
s.startswith("He"), s.endswith("lo")
"ell" in s          # True
s.find("l")         # 2, или -1
```

Строки неизменяемы: `s[0] = "h"` — ошибка. Создавайте новую строку.

```python
f"{name}: {score:3d} {ratio:.1%}"
```

Формат: `:>10` — выравнивание, `:03d` — ведущие нули, `:.2f` —
два знака.

---

## Списки

```python
nums = [3, 1, 2]
nums.append(4)          # [3, 1, 2, 4]
nums.insert(0, 9)       # [9, 3, 1, 2, 4]
nums.remove(3)          # удалить первое вхождение
last = nums.pop()       # удалить и вернуть последний
nums.sort()             # на месте
nums.sort(reverse=True)
sorted(nums)            # новый список
nums.reverse()
len(nums), sum(nums), min(nums), max(nums)
nums[1:3], nums[::-1]
```

`list(range(5))` → `[0, 1, 2, 3, 4]`.
`list(range(1, 10, 2))` → `[1, 3, 5, 7, 9]`.

Срезы создают новый список. Отрицательные индексы считаются с конца:
`-1` — последний элемент.

---

## Словари и множества

```python
user = {"name": "Ann", "age": 20}
user["age"]                 # 20
user["city"] = "Moscow"     # добавить или заменить
user.get("city")            # None, если ключа нет
user.get("city", "—")       # значение по умолчанию
"age" in user               # True
user.keys(), user.values(), user.items()
del user["age"]
user.pop("age", None)
```

Обход:

```python
for key, value in user.items():
    print(key, value)
```

```python
a = {1, 2, 3}
b = {2, 3, 4}
a | b      # объединение
a & b      # пересечение
a - b      # разность
a ^ b      # симметричная разность
```

`set` хранит уникальные элементы без порядка. `list(set(xs))` убирает
дубликаты, но порядок не гарантирован.

`collections.Counter` считает частоты:

```python
from collections import Counter
Counter("hello")            # Counter({'l': 2, 'h': 1, ...})
Counter(words).most_common(1)
```

---

## Условия и циклы

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

```python
for i in range(3):          # 0 1 2
    print(i)

for ch in "abc":
    print(ch)

while n > 0:
    n //= 10
```

```python
for i, value in enumerate(items):
    print(i, value)

for a, b in zip(xs, ys):
    print(a, b)

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
```

Блок задают **отступы**. Двоеточие обязательно. Пустой блок — `pass`.

Тернарное выражение:

```python
label = "even" if x % 2 == 0 else "odd"
```

---

## Функции

```python
def add(a, b=0):
    """Сумма двух чисел."""
    return a + b

add(2, 3)
add(2)
add(b=3, a=2)
```

```python
def total(*args):          # кортеж аргументов
    return sum(args)

def show(**kwargs):        # словарь именованных аргументов
    print(kwargs)
```

Функция без `return` возвращает `None`. Значения по умолчанию
вычисляются один раз — не используйте изменяемый список как значение
по умолчанию:

```python
def bad(x, acc=[]):        # общий список на все вызовы
    acc.append(x)
    return acc
```

---

## Генераторы и включения

```python
squares = [x * x for x in range(5)]          # список
evens = [x for x in nums if x % 2 == 0]      # с условием
pairs = [(x, y) for x in range(2) for y in range(2)]
```

```python
gen = (x * x for x in range(5))   # ленивый генератор
sum(x * x for x in range(5))      # без лишнего списка

def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

Генератор можно пройти один раз. `list(gen)` материализует значения.

---

## Классы

```python
class Point:
    count = 0                   # атрибут класса

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

```python
p = Point(3, 4)
print(p.length())    # 5.0
print(p)             # вызывает __str__
```

Наследование:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof"

class Puppy(Dog):
    def __init__(self, name):
        super().__init__(name)
```

Абстрактный класс:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
```

Перегрузка операторов:

```python
class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

## Исключения

```python
try:
    value = int(text)
except ValueError:
    print("not a number")
except (TypeError, KeyError) as e:
    print(type(e).__name__)
else:
    print("no exception")
finally:
    print("always")
```

```python
class NegativeAgeError(ValueError):
    pass

raise NegativeAgeError("age must be >= 0")
```

Не ловите голый `except:` — он скрывает и `KeyboardInterrupt`. Ловите
конкретные типы.

Частые исключения: `ValueError`, `TypeError`, `IndexError`, `KeyError`,
`ZeroDivisionError`, `FileNotFoundError`.

---

## Файлы

```python
with open("input.txt", encoding="utf-8") as f:
    text = f.read()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))
```

Режимы: `"r"` — чтение, `"w"` — запись с перезаписью, `"a"` — дописать,
`"x"` — создать, ошибка если существует. `"b"` — бинарный режим.

`read()` — весь файл, `readline()` — одна строка, `readlines()` —
список строк. `with` закрывает файл даже при исключении.

```python
from pathlib import Path
text = Path("input.txt").read_text(encoding="utf-8")
```

---

## Потоки

```python
import threading

result = []

def work(value):
    result.append(value * value)

t = threading.Thread(target=work, args=(5,))
t.start()
t.join()
```

```python
lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
```

`Lock` защищает критическую секцию: `counter += 1` — это чтение,
сложение и запись, между ними поток может быть вытеснен.

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(work, i) for i in range(3)]
    results = [f.result() for f in futures]
```

`Future.result()` ждёт завершения и возвращает значение или пробрасывает
исключение.

### GIL

В CPython потоки выполняют байткод по очереди (GIL). Для счёта это не
даёт ускорения, но гонки, блокировки и порядок событий видны так же, как
в других языках. Для параллельного счёта на нескольких ядрах используют
`multiprocessing`.

---

## Типизация

```python
from typing import TypeVar, Sequence

T = TypeVar("T")

def maximum(items: Sequence[T]) -> T:
    best = items[0]
    for item in items:
        if item > best:
            best = item
    return best
```

Аннотации не проверяются во время выполнения, но помогают читать код и
работать IDE. `list[int]`, `dict[str, int]`, `int | None` — современный
синтаксис (3.9+/3.10+).

---

## Полезные встроенные функции

```python
len(x), sum(x), min(x), max(x), abs(x), round(x, 2)
sorted(x), reversed(x)
enumerate(x), zip(a, b)
any(xs), all(xs)
map(f, xs), filter(f, xs)
isinstance(x, int)
```

`sorted(xs, key=lambda v: v[1])` — сортировка по второму элементу.
Сортировка стабильная.

---

## Частые ошибки новичка

| Ошибка | Причина |
| --- | --- |
| `IndentationError` | смешаны табы и пробелы или неверный отступ |
| `SyntaxError: Missing parentheses in call to 'print'` | синтаксис Python 2 |
| `TypeError: can only concatenate str` | `"x" + 5` вместо `f"x{5}"` |
| `IndexError` | индекс за пределами списка |
| `KeyError` | обращение к отсутствующему ключу словаря |
| `UnboundLocalError` | присваивание локальной переменной вместо `global` |
| Изменяемый аргумент по умолчанию | `def f(x, acc=[])` |
| `input()` в автотесте падает | неверный формат ввода или лишний вызов |
| `2.0` вместо `2` | деление `/` всегда даёт float; используйте `//` |
| Вывод без `\n`, когда тест ждёт `\n` | `print` против `print(..., end="")` |

---

## Стиль

- отступ — 4 пробела;
- имена: `snake_case` для переменных и функций, `PascalCase` для классов,
  `UPPER_CASE` для констант;
- пустые строки вокруг функций и классов;
- импорты сверху, каждый на своей строке;
- `if __name__ == "__main__":` — точка входа, если файл можно запускать и
  импортировать.

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Стандарт: [PEP 8](https://peps.python.org/pep-0008/).
