# Разбор задания

## Функция, а не оператор

В Python 3 `print` — обычная функция, поэтому аргументы обязаны быть
в скобках:

~~~python
print("Fixed!")
~~~

Старая запись `print "Fixed!"` работала только в Python 2. Современный
интерпретатор сообщает:

~~~text
SyntaxError: Missing parentheses in call to 'print'
~~~

## Почему ошибка синтаксиса

Интерпретатор разбирает весь файл до запуска. Если синтаксис неверен,
программа не выполнится вообще — даже строки до ошибки.

## Другие следы Python 2

| Python 2 | Python 3 |
| --- | --- |
| `print "text"` | `print("text")` |
| `raw_input()` | `input()` |
| `xrange(10)` | `range(10)` |
| `except Exception, e:` | `except Exception as e:` |
