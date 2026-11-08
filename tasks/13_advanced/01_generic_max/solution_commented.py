from typing import Sequence, TypeVar

# T — переменная типа: функция обобщённая, но возвращает тот же тип.
T = TypeVar("T")


def max_value(items: Sequence[T]) -> T:
    return max(items)


n = int(input())
numbers = list(map(int, input().split()))
print(f"Max: {max_value(numbers)}")
