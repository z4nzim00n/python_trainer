# Разбор задания

## Свой класс исключения

~~~python
class NegativeAgeError(Exception):
    pass
~~~

Наследуемся от `Exception`. Тело может быть пустым: важнее имя типа,
по которому исключение ловят.

## `raise`

~~~python
if age < 0:
    raise NegativeAgeError("negative age")
~~~

`raise` прерывает обычное выполнение и передаёт управление ближайшему
подходящему `except`.

## Обработка

~~~python
try:
    check_age(age)
    print(f"Age: {age}")
except NegativeAgeError:
    print("Error: negative age")
~~~

## Зачем своё исключение

Стандартный `ValueError` мог бы прийти из десятка мест. Свой тип
позволяет отличить именно эту ошибку и дать понятное сообщение.

## Атрибуты

~~~python
class NegativeAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"age must be >= 0, got {age}")
        self.age = age
~~~

Так исключение несёт данные о проблеме.

## Иерархия

Все исключения наследуются от `BaseException`; обычные ошибки — от
`Exception`. Наследоваться стоит от `Exception`.
