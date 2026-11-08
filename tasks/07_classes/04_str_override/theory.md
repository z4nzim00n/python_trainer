# Разбор задания

## `print` и `str`

Когда `print` получает объект, он вызывает `str(объект)`, а тот —
метод `__str__`:

~~~python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
~~~

~~~python
point = Point(3, 4)
print(point)        # Point(3, 4)
print(str(point))   # Point(3, 4)
~~~

## Без `__str__`

По умолчанию выводится что-то вроде `<__main__.Point object at 0x...>` —
адрес объекта, а не данные.

## `__repr__`

`repr` — представление для отладки. Часто `__repr__` делают подробным,
а `__str__` — человекочитаемым:

~~~python
def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"
~~~

В консоли Python объект показывается через `repr`.

## f-строки

`f"{point}"` тоже вызывает `__str__`, а `f"{point!r}"` — `__repr__`.
