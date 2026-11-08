# Разбор задания

## Абстрактный класс

~~~python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
~~~

`ABC` — базовый класс для абстракций. Метод с `@abstractmethod` обязан
быть реализован в наследнике.

## Почему нельзя создать `Shape`

~~~python
Shape()  # TypeError: Can't instantiate abstract class
~~~

Абстракция описывает общий интерфейс, но не конкретную фигуру.

## Наследники

~~~python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
~~~

## Полиморфизм

~~~python
shapes = [Circle(2), Square(3)]
for shape in shapes:
    print(f"{shape.area():.2f}")
~~~

Код работает с `Shape`, не зная конкретный класс. Так строят расширяемые
системы: новая фигура — новый наследник, остальной код не меняется.

## Утиная типизация

В Python абстрактный класс не обязателен: достаточно, чтобы у объекта
был метод `area`. Но `ABC` явно фиксирует контракт и помогает поймать
ошибку раньше.
