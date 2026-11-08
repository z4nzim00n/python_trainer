# Разбор задания

## Поля и метод

~~~python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
~~~

Метод использует поля объекта, поэтому одни и те же вычисления работают
для любого прямоугольника.

## Создание и вызов

~~~python
width, height = map(int, input().split())
rect = Rectangle(width, height)
print(f"Area: {rect.area()}")
~~~

`rect.area()` — вызов метода без аргументов: `self` подставляется сам.

## Метод, возвращающий значение

Хорошая практика: метод вычисляет и возвращает результат, а печать
остаётся в основной программе. Так метод можно переиспользовать.

## Свойства

Если хочется обращаться к площади как к полю, есть `@property`:

~~~python
@property
def area(self):
    return self.width * self.height
~~~

Тогда пишут `rect.area` без скобок. В этой задаче достаточно обычного
метода.
