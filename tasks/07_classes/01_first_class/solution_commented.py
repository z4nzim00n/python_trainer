class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        # self даёт доступ к атрибутам конкретного объекта.
        return f"{self.name} says {self.sound}"


dog = Dog("Rex", "Woof")
print(dog.speak())
