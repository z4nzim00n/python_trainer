class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # print вызывает __str__, поэтому объект печатается как строка.
        return f"Point({self.x}, {self.y})"


x, y = map(int, input().split())
print(Point(x, y))
