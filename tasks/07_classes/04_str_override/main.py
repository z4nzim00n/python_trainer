class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # TODO: верни Point(<x>, <y>)
        return "TODO"


x, y = map(int, input().split())
print(Point(x, y))
