# Разбор задания

## Режим записи

~~~python
with open(path, "w", encoding="utf-8") as file:
    file.write(text)
~~~

`"w"` создаёт файл или очищает существующий. Старое содержимое
исчезает.

## `write` и `print`

`file.write` не добавляет перевод строки:

~~~python
file.write("hello")
file.write("world")
# файл: helloworld
~~~

Чтобы разделить строки, добавьте `\n` вручную.

## Добавление в конец

~~~python
with open(path, "a", encoding="utf-8") as file:
    file.write("more\n")
~~~

`"a"` не стирает старое содержимое.

## Подтверждение

~~~python
print(f"Written: {path}")
~~~

## Ошибки

Нет каталога — `FileNotFoundError`; нет прав — `PermissionError`.
В задаче путь корректен.
