# Разбор задания

## Чтение и разбор

~~~python
with open(path, encoding="utf-8") as file:
    text = file.read()

numbers = list(map(int, text.split()))
total = sum(numbers)
~~~

`split()` без аргумента делит по пробелам и переводам строк, поэтому
формат файла не важен.

## Пустой файл

`"".split()` даёт `[]`, а `sum([])` равен `0`. Ошибки не будет.

## Отрицательные числа

`int("-5")` работает, поэтому знак не мешает разбору.

## Построчно

~~~python
total = 0
for line in file:
    total += sum(map(int, line.split()))
~~~

Такой вариант не загружает весь файл в память. Для небольших файлов
разница незаметна.

## Ошибка файла

~~~python
try:
    ...
except FileNotFoundError:
    print("Error: file not found")
~~~

## `ValueError`

Если в файле окажется слово, `int` бросит `ValueError`. По условию файл
содержит только числа.
