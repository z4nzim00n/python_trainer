# Разбор задания

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
