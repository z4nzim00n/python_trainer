@@TASK
section: 07_classes
dir: 01_first_class
num: 7_1
title: PY_07_01. Первый класс
topics: `class`, `__init__`, `self`, методы
input: Не требуются
@@DESC
Опиши класс `Dog`:

- конструктор принимает `name` и `sound` и сохраняет их;
- метод `speak` возвращает строку `<name> says <sound>`.

Создай собаку `Rex` со звуком `Woof` и выведи результат `speak`:

~~~text
Rex says Woof
~~~
@@EXAMPLES
| *(нет ввода)* | `Rex says Woof` |
@@THEORY
## Класс и объект

~~~python
class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"
~~~

`class` описывает шаблон. `Dog("Rex", "Woof")` создаёт объект — экземпляр
класса.

## `__init__`

Конструктор вызывается автоматически при создании объекта. Первый
параметр — `self`, ссылка на сам объект. Через `self` создаются атрибуты:
`self.name`, `self.sound`.

## `self`

`self` не передаётся вручную:

~~~python
dog = Dog("Rex", "Woof")
dog.speak()
~~~

Python сам подставляет `dog` в `self`. Имя `self` — соглашение, но
нарушать его не стоит.

## Атрибуты экземпляра

Каждый объект хранит свои значения:

~~~python
a = Dog("Rex", "Woof")
b = Dog("Bobik", "Gav")
print(a.speak())  # Rex says Woof
print(b.speak())  # Bobik says Gav
~~~

## Без `self`

Если забыть `self` в параметрах метода, при вызове будет `TypeError`:
метод получит лишний аргумент.
@@TESTS
| *(нет ввода)* | `Rex says Woof\n` |
@@CASES
run_case_devnull $'Rex says Woof\n'
@@MAIN
class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        # TODO: верни строку "<name> says <sound>"
        return "TODO"


dog = Dog("Rex", "Woof")
print(dog.speak())
@@SOLUTION
class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


dog = Dog("Rex", "Woof")
print(dog.speak())
@@COMMENTED
class Dog:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        # self даёт доступ к атрибутам конкретного объекта.
        return f"{self.name} says {self.sound}"


dog = Dog("Rex", "Woof")
print(dog.speak())
@@END

@@TASK
section: 07_classes
dir: 02_methods_area
num: 7_2
title: PY_07_02. Метод площади
topics: класс, метод, арифметика
input: Ширина и высота через пробел
@@DESC
Опиши класс `Rectangle` с полями `width` и `height` и методом `area`,
который возвращает площадь. Считай размеры и выведи:

~~~text
Area: <площадь>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 4` | `Area: 12` |
| `5 5` | `Area: 25` |
@@THEORY
## Поля и метод

~~~python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
~~~

Метод использует поля объекта, поэтому одни и те же вычисления работают
для любого прямоугольника.

## Создание и вызов

~~~python
width, height = map(int, input().split())
rect = Rectangle(width, height)
print(f"Area: {rect.area()}")
~~~

`rect.area()` — вызов метода без аргументов: `self` подставляется сам.

## Метод, возвращающий значение

Хорошая практика: метод вычисляет и возвращает результат, а печать
остаётся в основной программе. Так метод можно переиспользовать.

## Свойства

Если хочется обращаться к площади как к полю, есть `@property`:

~~~python
@property
def area(self):
    return self.width * self.height
~~~

Тогда пишут `rect.area` без скобок. В этой задаче достаточно обычного
метода.
@@TESTS
| `3 4` | `Area: 12\n` |
| `5 5` | `Area: 25\n` |
| `0 7` | `Area: 0\n` |
@@CASES
run_case "3 4" $'Area: 12\n'
run_case "5 5" $'Area: 25\n'
run_case "0 7" $'Area: 0\n'
@@MAIN
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
@@SOLUTION
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


width, height = map(int, input().split())
rect = Rectangle(width, height)
print(f"Area: {rect.area()}")
@@COMMENTED
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
@@END

@@TASK
section: 07_classes
dir: 03_constructor
num: 7_3
title: PY_07_03. Конструктор
topics: `__init__`, `self`, несколько аргументов
input: Имя и возраст (две строки)
@@DESC
Опиши класс `Person`. Конструктор принимает имя и возраст и сохраняет
их в поля `name` и `age`. Метод `greet` возвращает:

~~~text
Hi, <name>! Age: <age>
~~~

Считай имя и возраст, создай объект и выведи приветствие.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `Ada`<br>`36` | `Hi, Ada! Age: 36` |
| `Bob`<br>`0` | `Hi, Bob! Age: 0` |
@@THEORY
## Несколько аргументов

~~~python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
~~~

Порядок аргументов при создании объекта должен совпадать с порядком
параметров:

~~~python
person = Person("Ada", 36)
~~~

## Именованные аргументы

Их можно передавать по имени — тогда порядок не важен:

~~~python
person = Person(age=36, name="Ada")
~~~

## Метод

~~~python
def greet(self):
    return f"Hi, {self.name}! Age: {self.age}"
~~~

## Значения по умолчанию

~~~python
def __init__(self, name, age=0):
    ...
~~~

Тогда `Person("Ada")` создаст объект с возрастом `0`.

## Ошибки

| Ошибка | Причина |
| --- | --- |
| `TypeError: missing 1 required positional argument` | передано меньше аргументов |
| `TypeError: takes 3 positional arguments but 4 were given` | передано больше |
| `AttributeError` | поле не создано в `__init__` |
@@TESTS
| `Ada\n36` | `Hi, Ada! Age: 36\n` |
| `Bob\n0` | `Hi, Bob! Age: 0\n` |
@@CASES
run_case $'Ada\n36' $'Hi, Ada! Age: 36\n'
run_case $'Bob\n0' $'Hi, Bob! Age: 0\n'
@@MAIN
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
@@SOLUTION
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
@@COMMENTED
class Person:
    def __init__(self, name, age):
        # Аргументы конструктора становятся полями объекта.
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, {self.name}! Age: {self.age}"


name = input()
age = int(input())
person = Person(name, age)
print(person.greet())
@@END

@@TASK
section: 07_classes
dir: 04_str_override
num: 7_4
title: PY_07_04. Метод `__str__`
topics: `__str__`, `print`, строковое представление
input: Координаты `x` и `y` через пробел
@@DESC
Опиши класс `Point` с полями `x` и `y`. Метод `__str__` должен
возвращать:

~~~text
Point(<x>, <y>)
~~~

Считай координаты и выведи объект через `print`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3 4` | `Point(3, 4)` |
| `-1 0` | `Point(-1, 0)` |
@@THEORY
## `print` и `str`

Когда `print` получает объект, он вызывает `str(объект)`, а тот —
метод `__str__`:

~~~python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
~~~

~~~python
point = Point(3, 4)
print(point)        # Point(3, 4)
print(str(point))   # Point(3, 4)
~~~

## Без `__str__`

По умолчанию выводится что-то вроде `<__main__.Point object at 0x...>` —
адрес объекта, а не данные.

## `__repr__`

`repr` — представление для отладки. Часто `__repr__` делают подробным,
а `__str__` — человекочитаемым:

~~~python
def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"
~~~

В консоли Python объект показывается через `repr`.

## f-строки

`f"{point}"` тоже вызывает `__str__`, а `f"{point!r}"` — `__repr__`.
@@TESTS
| `3 4` | `Point(3, 4)\n` |
| `-1 0` | `Point(-1, 0)\n` |
| `0 0` | `Point(0, 0)\n` |
@@CASES
run_case "3 4" $'Point(3, 4)\n'
run_case "-1 0" $'Point(-1, 0)\n'
run_case "0 0" $'Point(0, 0)\n'
@@MAIN
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # TODO: верни Point(<x>, <y>)
        return "TODO"


x, y = map(int, input().split())
print(Point(x, y))
@@SOLUTION
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


x, y = map(int, input().split())
print(Point(x, y))
@@COMMENTED
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # print вызывает __str__, поэтому объект печатается как строка.
        return f"Point({self.x}, {self.y})"


x, y = map(int, input().split())
print(Point(x, y))
@@END

@@TASK
section: 07_classes
dir: 05_inheritance
num: 7_5
title: PY_07_05. Наследование
topics: наследование, `super`, переопределение методов
input: Не требуются
@@DESC
Есть класс `Animal` с методом `speak`. Опиши класс `Dog`, который
наследует `Animal` и переопределяет `speak`:

~~~text
Dog says Woof
~~~

Имя животного — `Dog`.
@@EXAMPLES
| *(нет ввода)* | `Dog says Woof` |
@@THEORY
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
@@TESTS
| *(нет ввода)* | `Dog says Woof\n` |
@@CASES
run_case_devnull $'Dog says Woof\n'
@@MAIN
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
@@SOLUTION
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"


dog = Dog("Dog")
print(dog.speak())
@@COMMENTED
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
@@END

@@TASK
section: 07_classes
dir: 06_abstract_shape
num: 7_6
title: PY_07_06. Абстрактный класс
topics: `ABC`, `@abstractmethod`, полиморфизм
input: Не требуются
@@DESC
Опиши абстрактный класс `Shape` с методом `area` и два наследника:
`Circle` (радиус) и `Square` (сторона). Выведи площади:

~~~text
Circle: 12.57
Square: 9.00
~~~

Круг радиуса `2`, квадрат со стороной `3`.
@@EXAMPLES
| *(нет ввода)* | `Circle: 12.57`<br>`Square: 9.00` |
@@THEORY
## Абстрактный класс

~~~python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
~~~

`ABC` — базовый класс для абстракций. Метод с `@abstractmethod` обязан
быть реализован в наследнике.

## Почему нельзя создать `Shape`

~~~python
Shape()  # TypeError: Can't instantiate abstract class
~~~

Абстракция описывает общий интерфейс, но не конкретную фигуру.

## Наследники

~~~python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
~~~

## Полиморфизм

~~~python
shapes = [Circle(2), Square(3)]
for shape in shapes:
    print(f"{shape.area():.2f}")
~~~

Код работает с `Shape`, не зная конкретный класс. Так строят расширяемые
системы: новая фигура — новый наследник, остальной код не меняется.

## Утиная типизация

В Python абстрактный класс не обязателен: достаточно, чтобы у объекта
был метод `area`. Но `ABC` явно фиксирует контракт и помогает поймать
ошибку раньше.
@@TESTS
| *(нет ввода)* | `Circle: 12.57\nSquare: 9.00\n` |
@@CASES
run_case_devnull $'Circle: 12.57\nSquare: 9.00\n'
@@MAIN
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # TODO: верни площадь круга
        return 0.0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # TODO: верни площадь квадрата
        return 0.0


circle = Circle(2)
square = Square(3)
print(f"Circle: {circle.area():.2f}")
print(f"Square: {square.area():.2f}")
@@SOLUTION
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


circle = Circle(2)
square = Square(3)
print(f"Circle: {circle.area():.2f}")
print(f"Square: {square.area():.2f}")
@@COMMENTED
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


# У каждого объекта свой area, но вызывается он одинаково.
circle = Circle(2)
square = Square(3)
print(f"Circle: {circle.area():.2f}")
print(f"Square: {square.area():.2f}")
@@END
