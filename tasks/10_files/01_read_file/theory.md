# Разбор задания

## Открытие файла

~~~python
with open(path, encoding="utf-8") as file:
    text = file.read()
~~~

`open` открывает файл на чтение по умолчанию. `with` гарантирует
закрытие даже при исключении.

## Кодировка

Всегда указывайте `encoding="utf-8"` явно. Иначе Python использует
системную кодировку, и на разных машинах результат может отличаться.

## Точный вывод

~~~python
import sys
sys.stdout.write(text)
~~~

`print` добавляет перевод строки, а содержимое файла может его не иметь.
`write` выводит текст ровно как есть.

## Файла нет

~~~python
try:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    sys.stdout.write(text)
except FileNotFoundError:
    print("Error: file not found")
~~~

`FileNotFoundError` — подкласс `OSError`.

## Режимы

| Режим | Смысл |
| --- | --- |
| `"r"` | чтение (по умолчанию) |
| `"w"` | запись с перезаписью |
| `"a"` | добавление в конец |
| `"rb"` | чтение байтов |

## Путь

Относительный путь считается от текущего каталога. В тестах это папка
задания.
