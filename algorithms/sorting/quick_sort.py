"""Реализация рекурсивного алгоритма быстрой сортировки по возрастанию."""
from random import randint
from typing import List, Tuple


def read_input() -> List[int]:
    _ = int(input().strip())
    array = list(map(int, input().strip().split()))
    return array


def partition(array: List[int], pivot: int) -> Tuple[List[int]]:
    """Функция формирования трех списков значений: меньше, равно и больше,
    относительно pivot."""
    less, equal, more = [], [], []
    for number in array:
        if number < pivot:
            less.append(number)
        elif number > pivot:
            more.append(number)
        else:
            equal.append(number)
    return less, equal, more


def quick_sort(seq: List[int]) -> List[int]:
    """Основная функция быстрой сортировки."""
    if len(seq) < 2:
        return seq
    pivot = seq[randint(0, len(seq))]
    less, equal, more = partition(seq, pivot)
    return quick_sort(less) + equal + quick_sort(more)


if __name__ == '__main__':
    print(*quick_sort(read_input()))
