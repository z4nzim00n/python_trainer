# Разбор задания

## Чтение и запись

~~~python
with open(source, encoding="utf-8") as src:
    text = src.read()

with open(destination, "w", encoding="utf-8") as dst:
    dst.write(text)
~~~

Содержимое читается целиком и записывается в новый файл. Переводы строк
сохраняются.

## Почему два блока `with`

Так каждый файл закрывается сразу после использования. Можно объединить:

~~~python
with open(source, encoding="utf-8") as src, \
     open(destination, "w", encoding="utf-8") as dst:
    dst.write(src.read())
~~~

## Потоковая копия

Для больших файлов читают частями:

~~~python
while True:
    chunk = src.read(8192)
    if not chunk:
        break
    dst.write(chunk)
~~~

Так файл не загружается в память целиком.

## Ошибка

~~~python
try:
    ...
except FileNotFoundError:
    print("Error: file not found")
~~~

## `shutil`

В реальном коде проще:

~~~python
import shutil
shutil.copyfile(source, destination)
~~~

Но для обучения полезно сделать копию вручную.
