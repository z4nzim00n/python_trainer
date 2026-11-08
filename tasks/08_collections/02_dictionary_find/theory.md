# Разбор задания

## Проверка наличия

~~~python
if key in data:
    print(f"Value: {data[key]}")
else:
    print("Value: Not found")
~~~

Оператор `in` проверяет ключи, а не значения.

## `KeyError`

Если обратиться к отсутствующему ключу напрямую:

~~~python
data["age"]  # KeyError: 'age'
~~~

## `get`

~~~python
value = data.get(key, "Not found")
print(f"Value: {value}")
~~~

Второй аргумент — значение по умолчанию. Без него `get` вернёт `None`.

## `None` как значение

Если в словаре может лежать `None`, `get` не отличит отсутствие ключа
от сохранённого `None`. Тогда используют `in`.

## Перебор

~~~python
for key, value in data.items():
    print(key, value)
~~~

`items()` даёт пары ключ-значение.
