# Разбор задания

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
