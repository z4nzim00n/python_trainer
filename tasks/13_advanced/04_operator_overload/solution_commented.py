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
