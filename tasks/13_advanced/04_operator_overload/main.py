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
