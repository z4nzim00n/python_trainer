# Разбор задания

## Генераторное выражение

~~~python
result = sum(x * x for x in numbers if x % 2 == 0)
~~~

Выражение вычисляется лениво: промежуточный список не создаётся.
`sum` забирает значения по одному.

## Список против генератора

~~~python
squares = [x * x for x in numbers if x % 2 == 0]  # список
squares = (x * x for x in numbers if x % 2 == 0)  # генератор
~~~

Скобки `()` создают генератор. Для `sum`, `any`, `all` это экономит
память.

## `filter` и `map`

~~~python
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, evens)
result = sum(squares)
~~~

Функциональный стиль. В Python генераторы читаются проще.

## `any` и `all`

~~~python
any(x < 0 for x in numbers)   # есть ли отрицательное
all(x > 0 for x in numbers)   # все ли положительные
~~~

`any` и `all` тоже ленивы: останавливаются на первом решающем элементе.

## Отрицательные чётные

`-2 % 2 == 0`, поэтому `-2` считается чётным. Это соответствует
математическому определению.
