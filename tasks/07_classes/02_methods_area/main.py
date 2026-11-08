class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # TODO: верни площадь
        return 0


width, height = map(int, input().split())
rect = Rectangle(width, height)
print(f"Area: {rect.area()}")
