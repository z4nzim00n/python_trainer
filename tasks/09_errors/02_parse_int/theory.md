# Разбор задания

## `ValueError`

~~~python
int("42")   # 42
int("abc")  # ValueError: invalid literal for int()
int("3.5")  # ValueError: int принимает только целые
~~~

## Обработка

~~~python
try:
    number = int(line)
    print(f"Number: {number}")
except ValueError:
    print("Error: invalid number")
~~~

## Почему не проверять `isdigit`

`str.isdigit()` не пропускает минус:

~~~python
"-7".isdigit()  # False
~~~

Пришлось бы отдельно разрешать знак. `try`/`except` проще и точнее
повторяет правила `int`.

## `else` и `finally`

~~~python
try:
    number = int(line)
except ValueError:
    print("Error")
else:
    print(f"Number: {number}")
~~~

`else` выполняется, только если исключения не было. Это позволяет
держать в `try` минимум кода.

## Не глотать всё

`except Exception` скрывает и опечатки в коде. Ловите конкретный тип.
