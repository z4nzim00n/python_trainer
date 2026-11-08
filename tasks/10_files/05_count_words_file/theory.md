# Разбор задания

## Слова

~~~python
text = file.read()
words = text.split()
print(f"Words: {len(words)}")
~~~

`split()` отбрасывает пробелы и переводы строк, поэтому слова считаются
одинаково в любом форматировании.

## Пустой файл

`len("".split())` равен `0`.

## Пунктуация

`split()` не убирает запятые и точки:

~~~python
"hello, world!".split()  # ['hello,', 'world!']
~~~

Это по-прежнему два слова. Если нужна очистка, используют
`ch.strip(".,!?")` или регулярные выражения.

## Построчный подсчёт

~~~python
total = 0
for line in file:
    total += len(line.split())
~~~

Эквивалентный вариант без загрузки файла целиком.

## Ошибка

~~~python
try:
    ...
except FileNotFoundError:
    print("Error: file not found")
~~~
