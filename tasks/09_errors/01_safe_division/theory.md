# Разбор задания

## Исключение

Деление на ноль бросает `ZeroDivisionError`:

~~~python
10 / 0  # ZeroDivisionError: division by zero
~~~

Если исключение не обработать, программа завершится с traceback.

## `try` / `except`

~~~python
try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: division by zero")
~~~

Сначала выполняется блок `try`. Если возникает исключение указанного
типа, управление переходит в `except`.

## Порядок

Важно: `print` с результатом стоит внутри `try`. Если бы он был после
блока, при ошибке переменная `result` не существовала бы.

## `finally`

~~~python
try:
    ...
except ZeroDivisionError:
    ...
finally:
    print("Done")
~~~

`finally` выполняется всегда — и при успехе, и при ошибке. Удобно для
освобождения ресурсов.

## Другие исключения

`ValueError` при неверном `int`, `TypeError` при несовместимых типах.
Ловить стоит конкретный тип, а не всё подряд.
