# Разбор задания

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
