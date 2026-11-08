# Разбор задания

## Первая строка

~~~python
print("Hello, Python!")
~~~

`print` — встроенная функция. В скобках указывается значение, которое нужно
вывести. Строка записывается в кавычках: `"..."` или `'...'`.

## Перевод строки

Каждый `print` завершает вывод переводом строки:

~~~python
print("one")
print("two")
~~~

~~~text
one
two
~~~

Если нужен вывод без перевода строки, используют параметр `end`:

~~~python
print("one", end="")
print("two")
~~~

~~~text
onetwo
~~~

## Запуск

~~~bash
python main.py
~~~

Python не компилирует программу в отдельный файл: интерпретатор читает
исходник и сразу выполняет инструкции.

## Частые ошибки

| Ошибка | Сообщение |
| --- | --- |
| Нет закрывающей кавычки | `SyntaxError: unterminated string literal` |
| Нет скобок у `print` | `SyntaxError: Missing parentheses in call to 'print'` |
| Неверный отступ | `IndentationError` |
