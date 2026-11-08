# Разбор задания

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
