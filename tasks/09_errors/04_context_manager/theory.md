# Разбор задания

## `with`

~~~python
with Resource() as resource:
    print("Using resource")
~~~

`with` гарантирует, что код выхода выполнится даже при исключении.
Именно так работают файлы:

~~~python
with open("input.txt", encoding="utf-8") as file:
    text = file.read()
~~~

Файл закроется автоматически.

## Протокол

~~~python
class Resource:
    def __enter__(self):
        print("Open")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closed")
        return False
~~~

- `__enter__` вызывается на входе; его результат попадает в `as`;
- `__exit__` вызывается на выходе и получает информацию об исключении.

## Возврат `__exit__`

| Значение | Поведение |
| --- | --- |
| `False` или `None` | исключение распространяется дальше |
| `True` | исключение подавляется |

Возвращать `True` стоит только осознанно.

## `contextlib`

Для простых случаев есть декоратор:

~~~python
from contextlib import contextmanager

@contextmanager
def resource():
    print("Open")
    yield
    print("Closed")
~~~

Функция с `yield` превращается в контекстный менеджер.
