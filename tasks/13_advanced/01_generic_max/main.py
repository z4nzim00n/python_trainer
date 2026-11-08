from typing import Sequence, TypeVar

T = TypeVar("T")


def max_value(items: Sequence[T]) -> T:
    # TODO: верни максимальный элемент
    return items[0]


n = int(input())
numbers = list(map(int, input().split()))
print(f"Max: {max_value(numbers)}")
