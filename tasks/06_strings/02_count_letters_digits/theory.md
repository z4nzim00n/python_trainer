# Разбор задания

## Цикл по символам

~~~python
for ch in text:
    ...
~~~

Строка итерируется посимвольно, без индексов.

## Методы проверки

| Метод | Истинно для |
| --- | --- |
| `ch.isalpha()` | буквы |
| `ch.isdigit()` | цифры |
| `ch.isspace()` | пробельных символов |
| `ch.isalnum()` | букв и цифр |

~~~python
letters = 0
digits = 0
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
~~~

## Генераторы и `sum`

~~~python
letters = sum(ch.isalpha() for ch in text)
~~~

`True` в сумме считается за `1`, `False` — за `0`. Компактно, но цикл
с счётчиками понятнее новичку.

## Кириллица

`isalpha()` возвращает `True` и для русских букв. Это ещё одно отличие
от простой проверки диапазона `a..z`.
