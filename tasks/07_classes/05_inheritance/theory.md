# Разбор задания

## Базовый класс

~~~python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
~~~

## Наследование

~~~python
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"
~~~

`Dog(Animal)` означает: класс `Dog` наследует поля и методы `Animal`.
Свой `speak` переопределяет родительский.

## `super`

Если нужно дополнить поведение родителя, вызывают `super()`:

~~~python
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.kind = "dog"
~~~

`super().__init__(name)` вызывает конструктор `Animal`, чтобы не
дублировать присваивание имени.

## Полиморфизм

~~~python
animals = [Animal("Cat"), Dog("Dog")]
for animal in animals:
    print(animal.speak())
~~~

Вызывается метод фактического класса объекта.

## Проверка типа

~~~python
print(isinstance(Dog("Dog"), Animal))  # True
~~~

Наследник является экземпляром базового класса.
