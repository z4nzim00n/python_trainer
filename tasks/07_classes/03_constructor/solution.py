class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, {self.name}! Age: {self.age}"


name = input()
age = int(input())
person = Person(name, age)
print(person.greet())
