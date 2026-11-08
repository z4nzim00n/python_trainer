@@TASK
section: 10_files
dir: 01_read_file
num: 10_1
title: PY_10_01. Чтение файла
topics: `open`, `with`, `read`, `FileNotFoundError`
input: Имя файла
@@DESC
Прочитай файл и выведи его содержимое без изменений:

~~~text
hello
world
~~~

Если файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `input.txt` (содержит `hello`) | `hello` |
| `missing.txt` | `Error: file not found` |
@@THEORY
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
@@TESTS
| `input.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `input.txt` (`abc`, без `\n`) | `abc` |
| `missing.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f input.txt missing.txt' EXIT
printf 'hello\nworld\n' > input.txt
run_case "input.txt" $'hello\nworld\n'
printf 'abc' > input.txt
run_case "input.txt" "abc"
run_case "missing.txt" $'Error: file not found\n'
@@MAIN
import sys

path = input()

# TODO: прочитай файл и выведи содержимое
print("TODO")
@@SOLUTION
import sys

path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()
    sys.stdout.write(text)
except FileNotFoundError:
    print("Error: file not found")
@@COMMENTED
import sys

path = input()

try:
    # with закроет файл автоматически.
    with open(path, encoding="utf-8") as file:
        text = file.read()
    # write не добавляет свой перевод строки — вывод совпадает с файлом.
    sys.stdout.write(text)
except FileNotFoundError:
    print("Error: file not found")
@@END

@@TASK
section: 10_files
dir: 02_write_file
num: 10_2
title: PY_10_02. Запись файла
topics: `open`, режим `"w"`, `write`
input: Имя файла и строка (две строки)
@@DESC
Запиши строку в файл и подтверди:

~~~text
Written: <имя файла>
~~~

Если файл уже существовал, он перезаписывается.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `output.txt`<br>`hello` | `Written: output.txt` |
@@THEORY
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
@@TESTS
| `output.txt\nhello` | `Written: output.txt\n`, файл `hello` |
| `text.txt\nhello world` | `Written: text.txt\n`, файл `hello world` |
@@CASES
trap 'rm -f output.txt text.txt' EXIT
run_case $'output.txt\nhello' $'Written: output.txt\n'
check_file "output.txt" "hello"
run_case $'text.txt\nhello world' $'Written: text.txt\n'
check_file "text.txt" "hello world"
@@MAIN
path = input()
text = input()

# TODO: запиши text в файл и выведи Written: <путь>
print("TODO")
@@SOLUTION
path = input()
text = input()

with open(path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Written: {path}")
@@COMMENTED
path = input()
text = input()

# Режим "w" перезаписывает файл целиком.
with open(path, "w", encoding="utf-8") as file:
    file.write(text)

print(f"Written: {path}")
@@END

@@TASK
section: 10_files
dir: 03_copy_file
num: 10_3
title: PY_10_03. Копирование файла
topics: чтение, запись, `FileNotFoundError`
input: Имя исходного и нового файла (две строки)
@@DESC
Скопируй содержимое одного файла в другой и выведи:

~~~text
Copied: <источник> -> <назначение>
~~~

Если исходного файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `input.txt`<br>`copy.txt` | `Copied: input.txt -> copy.txt` |
@@THEORY
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
@@TESTS
| `input.txt\ncopy.txt` | `Copied: input.txt -> copy.txt\n`, файл `copy.txt` совпадает |
| `text.txt\nbackup.txt` | `Copied: text.txt -> backup.txt\n`, файл совпадает |
| `missing.txt\ncopy.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f input.txt copy.txt text.txt backup.txt' EXIT
printf 'hello\nworld\n' > input.txt
run_case $'input.txt\ncopy.txt' $'Copied: input.txt -> copy.txt\n'
check_file "copy.txt" $'hello\nworld\n'
printf 'abc' > text.txt
run_case $'text.txt\nbackup.txt' $'Copied: text.txt -> backup.txt\n'
check_file "backup.txt" "abc"
run_case $'missing.txt\ncopy.txt' $'Error: file not found\n'
@@MAIN
source = input()
destination = input()

# TODO: скопируй файл и выведи Copied: <источник> -> <назначение>
print("TODO")
@@SOLUTION
source = input()
destination = input()

try:
    with open(source, encoding="utf-8") as src:
        text = src.read()

    with open(destination, "w", encoding="utf-8") as dst:
        dst.write(text)

    print(f"Copied: {source} -> {destination}")
except FileNotFoundError:
    print("Error: file not found")
@@COMMENTED
source = input()
destination = input()

try:
    with open(source, encoding="utf-8") as src:
        text = src.read()

    # Новый файл создаётся в режиме "w".
    with open(destination, "w", encoding="utf-8") as dst:
        dst.write(text)

    print(f"Copied: {source} -> {destination}")
except FileNotFoundError:
    print("Error: file not found")
@@END

@@TASK
section: 10_files
dir: 04_sum_numbers_file
num: 10_4
title: PY_10_04. Сумма чисел из файла
topics: `read`, `split`, `map`, `sum`
input: Имя файла
@@DESC
В файле записаны целые числа через пробелы и переводы строк. Посчитай
их сумму:

~~~text
Sum: <сумма>
~~~

Если файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `numbers.txt` (`1 2 3\n4 5`) | `Sum: 15` |
| `numbers.txt` (`10`) | `Sum: 10` |
@@THEORY
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
@@TESTS
| `numbers.txt` (`1 2 3\n4 5`) | `Sum: 15\n` |
| `numbers.txt` (`10`) | `Sum: 10\n` |
| `numbers.txt` (пустой) | `Sum: 0\n` |
| `missing.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f numbers.txt' EXIT
printf '1 2 3\n4 5' > numbers.txt
run_case "numbers.txt" $'Sum: 15\n'
printf '10' > numbers.txt
run_case "numbers.txt" $'Sum: 10\n'
printf '' > numbers.txt
run_case "numbers.txt" $'Sum: 0\n'
run_case "missing.txt" $'Error: file not found\n'
@@MAIN
path = input()

# TODO: прочитай числа, посчитай сумму и выведи Sum: <сумма>
print("TODO")
@@SOLUTION
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    numbers = list(map(int, text.split()))
    print(f"Sum: {sum(numbers)}")
except FileNotFoundError:
    print("Error: file not found")
@@COMMENTED
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    # split без аргумента понимает и пробелы, и переводы строк.
    numbers = list(map(int, text.split()))
    print(f"Sum: {sum(numbers)}")
except FileNotFoundError:
    print("Error: file not found")
@@END

@@TASK
section: 10_files
dir: 05_count_words_file
num: 10_5
title: PY_10_05. Слова в файле
topics: `read`, `split`, `len`
input: Имя файла
@@DESC
Посчитай количество слов в файле:

~~~text
Words: <количество>
~~~

Если файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `text.txt` (`hello world\npython`) | `Words: 3` |
| `text.txt` (`one`) | `Words: 1` |
@@THEORY
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
@@TESTS
| `text.txt` (`hello world\npython`) | `Words: 3\n` |
| `text.txt` (`one`) | `Words: 1\n` |
| `text.txt` (пустой) | `Words: 0\n` |
| `missing.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f text.txt' EXIT
printf 'hello world\npython' > text.txt
run_case "text.txt" $'Words: 3\n'
printf 'one' > text.txt
run_case "text.txt" $'Words: 1\n'
printf '' > text.txt
run_case "text.txt" $'Words: 0\n'
run_case "missing.txt" $'Error: file not found\n'
@@MAIN
path = input()

# TODO: посчитай слова в файле и выведи Words: <количество>
print("TODO")
@@SOLUTION
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    print(f"Words: {len(words)}")
except FileNotFoundError:
    print("Error: file not found")
@@COMMENTED
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    # split делит по любым пробельным символам.
    words = text.split()
    print(f"Words: {len(words)}")
except FileNotFoundError:
    print("Error: file not found")
@@END

@@TASK
section: 10_files
dir: 06_file_stats
num: 10_6
title: PY_10_06. Статистика файла
topics: `read`, `splitlines`, строки и слова
input: Имя файла
@@DESC
Посчитай строки, слова и символы (без переводов строк):

~~~text
Lines: <строк>
Words: <слов>
Chars: <символов>
~~~

Если файла нет, выведи `Error: file not found`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `text.txt` (`hello world\npython\n`) | `Lines: 2`<br>`Words: 3`<br>`Chars: 17` |
| `text.txt` (`abc`) | `Lines: 1`<br>`Words: 1`<br>`Chars: 3` |
@@THEORY
## `splitlines`

~~~python
lines = text.splitlines()
~~~

Делит текст на строки без символов перевода строки. Для `"a\nb\n"` даёт
`["a", "b"]` — завершающий перевод не создаёт пустую строку.

## Подсчёт

~~~python
line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)
~~~

Символы считаются без `\n`, поэтому `char_count` — сумма длин строк.

## Генераторное выражение

~~~python
sum(len(line.split()) for line in lines)
~~~

Внутри `sum` можно писать выражение без квадратных скобок: это
генератор, он не создаёт промежуточный список.

## Пустой файл

`"".splitlines()` возвращает `[]`, все три счётчика равны `0`.

## Переводы строк

`splitlines()` понимает `\n`, `\r\n` и `\r`. Поэтому статистика не
зависит от платформы.

## Ошибка

~~~python
try:
    ...
except FileNotFoundError:
    print("Error: file not found")
~~~
@@TESTS
| `text.txt` (`hello world\npython\n`) | `Lines: 2\nWords: 3\nChars: 17\n` |
| `text.txt` (`abc`) | `Lines: 1\nWords: 1\nChars: 3\n` |
| `text.txt` (пустой) | `Lines: 0\nWords: 0\nChars: 0\n` |
| `missing.txt` | `Error: file not found\n` |
@@CASES
trap 'rm -f text.txt' EXIT
printf 'hello world\npython\n' > text.txt
run_case "text.txt" $'Lines: 2\nWords: 3\nChars: 17\n'
printf 'abc' > text.txt
run_case "text.txt" $'Lines: 1\nWords: 1\nChars: 3\n'
printf '' > text.txt
run_case "text.txt" $'Lines: 0\nWords: 0\nChars: 0\n'
run_case "missing.txt" $'Error: file not found\n'
@@MAIN
path = input()

# TODO: посчитай строки, слова и символы
print("TODO")
@@SOLUTION
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    lines = text.splitlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Chars: {char_count}")
except FileNotFoundError:
    print("Error: file not found")
@@COMMENTED
path = input()

try:
    with open(path, encoding="utf-8") as file:
        text = file.read()

    # splitlines убирает переводы строк, но сохраняет пустые строки внутри.
    lines = text.splitlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Chars: {char_count}")
except FileNotFoundError:
    print("Error: file not found")
@@END
