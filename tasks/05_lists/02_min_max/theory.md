# Разбор задания

## Встроенные функции

~~~python
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
~~~

Обе функции проходят по элементам один раз и возвращают нужное значение.

## Своими руками

~~~python
lowest = numbers[0]
highest = numbers[0]
for value in numbers[1:]:
    if value < lowest:
        lowest = value
    if value > highest:
        highest = value
~~~

Начальное значение берут из первого элемента, а не из нуля: иначе для
списка из отрицательных чисел максимум остался бы нулём.

## `key`

У `min` и `max` есть параметр `key` — правило сравнения:

~~~python
words = ["aaa", "b", "cc"]
print(max(words, key=len))  # aaa
~~~

## Пустой список

`min([])` и `max([])` бросают `ValueError`. По условию `n >= 1`.
