class Person:
    def __init__(self, name, age):
        # TODO: сохрани name и age в self.name и self.age
        self.name = "TODO"
        self.age = 0

    def greet(self):
        return f"Hi, {self.name}! Age: {self.age}"


name = input()
age = int(input())
person = Person(name, age)
print(person.greet())
