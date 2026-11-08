@@TASK
section: 06_strings
dir: 01_string_length
num: 6_1
title: PY_06_01. Длина строки
topics: `len`, строки, `input`
input: Одна строка
@@DESC
Считай строку и выведи её длину:

~~~text
Length: <длина>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello` | `Length: 5` |
| `a b` | `Length: 3` |
@@THEORY
## Строка — последовательность символов

~~~python
text = input()
print(len(text))
~~~

`len` возвращает количество символов, включая пробелы и знаки препинания.

## Индексы

~~~python
text = "hello"
print(text[0])   # h
print(text[-1])  # o
~~~

Индексация начинается с нуля. Отрицательный индекс считается с конца.

## Срез

~~~python
print(text[1:4])  # ell
~~~

Правая граница не включается. `text[:2]` — первые два символа,
`text[2:]` — начиная с третьего.

## Пустая строка

`len("")` равен `0`. Это корректная строка, а не ошибка.

## Unicode

Python 3 считает символы Unicode, а не байты:

~~~python
len("привет")  # 6
~~~

Кириллица в выводе заданий не используется, но помнить об этом полезно.
@@TESTS
| `hello` | `Length: 5\n` |
| `a b` | `Length: 3\n` |
| `` (пустая строка) | `Length: 0\n` |
@@CASES
run_case "hello" $'Length: 5\n'
run_case "a b" $'Length: 3\n'
run_case "" $'Length: 0\n'
@@MAIN
text = input()

# TODO: выведи Length: <длина строки>
print("TODO")
@@SOLUTION
text = input()

print(f"Length: {len(text)}")
@@COMMENTED
text = input()

# len считает все символы, включая пробелы.
print(f"Length: {len(text)}")
@@END

@@TASK
section: 06_strings
dir: 02_count_letters_digits
num: 6_2
title: PY_06_02. Буквы и цифры
topics: `isalpha`, `isdigit`, цикл по строке
input: Одна строка
@@DESC
Посчитай, сколько в строке букв и сколько цифр:

~~~text
Letters: <количество букв>
Digits: <количество цифр>
~~~

Пробелы и знаки препинания не считаются.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `abc123` | `Letters: 3`<br>`Digits: 3` |
| `Hello, World!` | `Letters: 10`<br>`Digits: 0` |
@@THEORY
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
@@TESTS
| `abc123` | `Letters: 3\nDigits: 3\n` |
| `Hello, World!` | `Letters: 10\nDigits: 0\n` |
| `a1b2c3` | `Letters: 3\nDigits: 3\n` |
@@CASES
run_case "abc123" $'Letters: 3\nDigits: 3\n'
run_case "Hello, World!" $'Letters: 10\nDigits: 0\n'
run_case "a1b2c3" $'Letters: 3\nDigits: 3\n'
@@MAIN
text = input()

# TODO: посчитай буквы и цифры
print("TODO")
@@SOLUTION
text = input()

letters = 0
digits = 0
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
@@COMMENTED
text = input()

letters = 0
digits = 0
# isalpha и isdigit сами определяют категорию символа.
for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")
@@END

@@TASK
section: 06_strings
dir: 03_to_upper_lower
num: 6_3
title: PY_06_03. Верхний и нижний регистр
topics: `upper`, `lower`, строки
input: Одна строка
@@DESC
Выведи строку в верхнем и нижнем регистре:

~~~text
Upper: <ЗАГЛАВНЫЕ>
Lower: <строчные>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `Hello` | `Upper: HELLO`<br>`Lower: hello` |
| `PyThOn` | `Upper: PYTHON`<br>`Lower: python` |
@@THEORY
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
@@TESTS
| `Hello` | `Upper: HELLO\nLower: hello\n` |
| `PyThOn` | `Upper: PYTHON\nLower: python\n` |
| `123` | `Upper: 123\nLower: 123\n` |
@@CASES
run_case "Hello" $'Upper: HELLO\nLower: hello\n'
run_case "PyThOn" $'Upper: PYTHON\nLower: python\n'
run_case "123" $'Upper: 123\nLower: 123\n'
@@MAIN
text = input()

# TODO: выведи Upper и Lower
print("TODO")
@@SOLUTION
text = input()

print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
@@COMMENTED
text = input()

# upper и lower возвращают новые строки, исходная не меняется.
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
@@END

@@TASK
section: 06_strings
dir: 04_count_words
num: 6_4
title: PY_06_04. Количество слов
topics: `split`, пробельные символы
input: Одна строка
@@DESC
Посчитай количество слов в строке:

~~~text
Words: <количество>
~~~

Слова разделены пробелами; лишние пробелы не создают пустых слов.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello world` | `Words: 2` |
| `  a   b  c  ` | `Words: 3` |
@@THEORY
## `split` без аргумента

~~~python
words = "  a   b  c  ".split()
print(words)  # ['a', 'b', 'c']
~~~

Без аргумента `split` делит строку по любым пробельным символам и
отбрасывает пустые части. Несколько пробелов подряд считаются одним
разделителем.

## `split` с аргументом

~~~python
"a,b,c".split(",")  # ['a', 'b', 'c']
"a  b".split(" ")   # ['a', '', 'b']
~~~

С явным разделителем пустые части сохраняются.

## Количество

~~~python
print(f"Words: {len(words)}")
~~~

## Пустая строка

`"".split()` возвращает `[]`, поэтому количество слов равно `0`.

## Переводы строк

`split()` без аргумента делит и по `\n`, и по табуляции. Для чтения
нескольких слов из одной строки это удобно.
@@TESTS
| `hello world` | `Words: 2\n` |
| `  a   b  c  ` | `Words: 3\n` |
| `` (пустая строка) | `Words: 0\n` |
@@CASES
run_case "hello world" $'Words: 2\n'
run_case "  a   b  c  " $'Words: 3\n'
run_case "" $'Words: 0\n'
@@MAIN
text = input()

# TODO: посчитай слова и выведи Words: <количество>
print("TODO")
@@SOLUTION
text = input()

words = text.split()
print(f"Words: {len(words)}")
@@COMMENTED
text = input()

# split без аргумента убирает лишние пробелы между словами.
words = text.split()
print(f"Words: {len(words)}")
@@END

@@TASK
section: 06_strings
dir: 05_reverse_string
num: 6_5
title: PY_06_05. Разворот строки
topics: срез `[::-1]`, строки
input: Одна строка
@@DESC
Выведи строку в обратном порядке:

~~~text
<перевёрнутая строка>
~~~
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `hello` | `olleh` |
| `abc def` | `fed cba` |
@@THEORY
## Срез с отрицательным шагом

~~~python
text[::-1]
~~~

Срез `[start:stop:step]` с шагом `-1` идёт от последнего символа к первому.
Новая строка создаётся, исходная не меняется.

## Цикл

~~~python
result = ""
for ch in text:
    result = ch + result
~~~

Каждый новый символ ставится в начало. Работает, но на длинных строках
медленнее: строки неизменяемы, и `+` каждый раз создаёт новую.

## `reversed` и `join`

~~~python
"".join(reversed(text))
~~~

`reversed` даёт итератор символов, `join` склеивает их без разделителя.

## Пустая строка

Для `""` результат тоже `""` — срез безопасен.
@@TESTS
| `hello` | `olleh\n` |
| `abc def` | `fed cba\n` |
| `` (пустая строка) | `\n` |
@@CASES
run_case "hello" $'olleh\n'
run_case "abc def" $'fed cba\n'
run_case "" $'\n'
@@MAIN
text = input()

# TODO: выведи строку в обратном порядке
print("TODO")
@@SOLUTION
text = input()

print(text[::-1])
@@COMMENTED
text = input()

# Шаг -1 означает движение с конца строки к началу.
print(text[::-1])
@@END

@@TASK
section: 06_strings
dir: 06_palindrome
num: 6_6
title: PY_06_06. Палиндром
topics: нормализация строки, срез, `isalnum`
input: Одна строка
@@DESC
Проверь, является ли строка палиндромом. Игнорируй регистр и символы,
кроме букв и цифр:

~~~text
Palindrome: <True/False>
~~~

Например, `A man a plan a canal Panama` — палиндром.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `level` | `Palindrome: True` |
| `Hello` | `Palindrome: False` |
| `A man a plan a canal Panama` | `Palindrome: True` |
@@THEORY
## Нормализация

Сначала приводим строку к нижнему регистру и оставляем только буквы
и цифры:

~~~python
cleaned = "".join(ch for ch in text.lower() if ch.isalnum())
~~~

Для `A man a plan a canal Panama` получится `amanaplanacanalpanama`.

## Проверка

Палиндром читается одинаково в обе стороны:

~~~python
cleaned == cleaned[::-1]
~~~

## Цикл с двумя указателями

~~~python
left = 0
right = len(cleaned) - 1
while left < right:
    if cleaned[left] != cleaned[right]:
        break
    left += 1
    right -= 1
~~~

Этот способ не создаёт перевёрнутую копию и раньше находит различие —
полезно для очень длинных строк.

## Пустая строка

Пустая строка после нормализации считается палиндромом: `"" == ""[::-1]`.
@@TESTS
| `level` | `Palindrome: True\n` |
| `Hello` | `Palindrome: False\n` |
| `A man a plan a canal Panama` | `Palindrome: True\n` |
| `` (пустая строка) | `Palindrome: True\n` |
@@CASES
run_case "level" $'Palindrome: True\n'
run_case "Hello" $'Palindrome: False\n'
run_case "A man a plan a canal Panama" $'Palindrome: True\n'
run_case "" $'Palindrome: True\n'
@@MAIN
text = input()

# TODO: проверь палиндром и выведи Palindrome: <True/False>
print("TODO")
@@SOLUTION
text = input()

cleaned = "".join(ch for ch in text.lower() if ch.isalnum())
print(f"Palindrome: {cleaned == cleaned[::-1]}")
@@COMMENTED
text = input()

# Сначала убираем регистр, пробелы и знаки препинания.
cleaned = "".join(ch for ch in text.lower() if ch.isalnum())

# Палиндром совпадает со своей перевёрнутой версией.
print(f"Palindrome: {cleaned == cleaned[::-1]}")
@@END

@@TASK
section: 06_strings
dir: 07_caesar_cipher
num: 6_7
title: PY_06_07. Шифр Цезаря
topics: `ord`, `chr`, `%`, строки
input: Сдвиг и строка (две строки)
@@DESC
Зашифруй строку шифром Цезаря: каждая латинская буква сдвигается
на `k` позиций по алфавиту. Регистр сохраняется, остальные символы
не меняются:

~~~text
<зашифрованная строка>
~~~

Например, при сдвиге `3` строка `Hello, World!` превращается
в `Khoor, Zruog!`.
@@EXAMPLES
| Входные данные | Результат работы |
| ------ | ------ |
| `3`<br>`Hello, World!` | `Khoor, Zruog!` |
| `1`<br>`abc XYZ` | `bcd YZA` |
@@THEORY
## Код символа

~~~python
print(ord("a"))  # 97
print(ord("z"))  # 122
print(chr(98))   # b
~~~

`ord` возвращает числовой код символа, `chr` — символ по коду.

## Сдвиг внутри алфавита

~~~python
base = ord("a")
code = ord(ch) - base          # 0..25
shifted = (code + k) % 26      # замыкаем алфавит
result = chr(shifted + base)
~~~

Остаток `% 26` важен: после `z` снова идёт `a`. Для заглавных букв база
`ord("A")`, диапазон тот же `0..25`.

## Почему нужен `%`

Без остатка `chr(122 + 3)` даст `}`, а не `c`. Модуль замыкает алфавит.

## Большой сдвиг

`k = 29` эквивалентен `k = 3`. Можно сразу взять `k %= 26`.

## Сохранение регистра

Проверяем диапазон буквы и выбираем базу:

~~~python
if "a" <= ch <= "z":
    base = ord("a")
elif "A" <= ch <= "Z":
    base = ord("A")
else:
    result.append(ch)
    continue
~~~

Сравнение строк работает по кодам символов, поэтому диапазоны `a..z`
и `A..Z` записываются наглядно.
@@TESTS
| `3\nHello, World!` | `Khoor, Zruog!\n` |
| `1\nabc XYZ` | `bcd YZA\n` |
| `0\nTest` | `Test\n` |
| `26\nTest` | `Test\n` |
@@CASES
run_case $'3\nHello, World!' $'Khoor, Zruog!\n'
run_case $'1\nabc XYZ' $'bcd YZA\n'
run_case $'0\nTest' $'Test\n'
run_case $'26\nTest' $'Test\n'
@@MAIN
shift = int(input())
text = input()

# TODO: зашифруй текст и выведи результат
print("TODO")
@@SOLUTION
shift = int(input())
text = input()

result = []
for ch in text:
    if "a" <= ch <= "z":
        base = ord("a")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    elif "A" <= ch <= "Z":
        base = ord("A")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    else:
        result.append(ch)

print("".join(result))
@@COMMENTED
shift = int(input())
text = input()

result = []
for ch in text:
    if "a" <= ch <= "z":
        # Приводим букву к 0..25, сдвигаем по кругу и возвращаем в алфавит.
        base = ord("a")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    elif "A" <= ch <= "Z":
        base = ord("A")
        result.append(chr((ord(ch) - base + shift) % 26 + base))
    else:
        # Пробелы, запятые и другие символы остаются как есть.
        result.append(ch)

print("".join(result))
@@END
