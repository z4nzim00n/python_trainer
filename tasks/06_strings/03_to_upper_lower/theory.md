# Разбор задания

## Методы регистра

~~~python
text = "Hello"
print(text.upper())  # HELLO
print(text.lower())  # hello
~~~

Методы возвращают новую строку. Исходная строка неизменяема:

~~~python
text = "Hello"
text.upper()
print(text)  # Hello
~~~

## Другие методы

| Метод | Результат для `"hello world"` |
| --- | --- |
| `capitalize()` | `Hello world` |
| `title()` | `Hello World` |
| `swapcase()` | `HELLO WORLD` |

## Сравнение без регистра

~~~python
if text.lower() == "hello":
    ...
~~~

Так проверяют команды и ответы пользователя.

## Неизменяемость

Строку нельзя изменить по индексу:

~~~python
text[0] = "H"  # TypeError
~~~

Любое преобразование создаёт новую строку.
