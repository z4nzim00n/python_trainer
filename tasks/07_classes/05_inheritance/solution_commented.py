class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    # Метод с тем же именем заменяет версию родителя.
    def speak(self):
        return f"{self.name} says Woof"


dog = Dog("Dog")
print(dog.speak())
