# Разбор задания

## Индексация

~~~python
numbers = [10, 20, 30]
numbers[0]   # 10
numbers[2]   # 30
numbers[3]   # IndexError
~~~

Допустимые индексы: от `0` до `len(numbers) - 1`.

## Отрицательные индексы

~~~python
numbers[-1]  # 30
numbers[-3]  # 10
numbers[-4]  # IndexError
~~~

Отрицательный индекс считается с конца. Это не ошибка, пока не выходит
за границы.

## Обработка

~~~python
try:
    print(f"Value: {numbers[index]}")
except IndexError:
    print("Error: index out of range")
~~~

## Проверка заранее

~~~python
if -len(numbers) <= index < len(numbers):
    ...
else:
    ...
~~~

Такой вариант тоже правильный. `try`/`except` короче, если ошибка
ожидается редко.

## Срез не бросает ошибку

~~~python
numbers[10:20]  # []
~~~

Срез за границами возвращает пустой список, а не исключение. Это важное
отличие от обращения по индексу.
