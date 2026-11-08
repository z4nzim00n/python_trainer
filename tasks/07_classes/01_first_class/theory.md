# Разбор задания

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
