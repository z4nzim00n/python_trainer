from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


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


# У каждого объекта свой area, но вызывается он одинаково.
circle = Circle(2)
square = Square(3)
print(f"Circle: {circle.area():.2f}")
print(f"Square: {square.area():.2f}")
