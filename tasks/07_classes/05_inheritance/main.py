class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):
        # TODO: переопредели speak строкой "<name> says Woof"
        return super().speak()


dog = Dog("Dog")
print(dog.speak())
