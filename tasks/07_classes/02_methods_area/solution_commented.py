class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Метод читает поля конкретного объекта.
        return self.width * self.height


width, height = map(int, input().split())
rect = Rectangle(width, height)
print(f"Area: {rect.area()}")
