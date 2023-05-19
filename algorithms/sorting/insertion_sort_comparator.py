"""Реализация алгоритма сортировки вставками с функцей-компаратор."""
from typing import List, Tuple


def read_input() -> Tuple[int, List[str]]:
    length = int(input().strip())
    numbers = input().strip().split()
    return length, numbers


def insertions_sort(seq: List[str], comparator) -> List[str]:
    """Функция сортировки последовательности методом вставками."""
    for i in range(1, len(seq)):
        insert_item = seq[i]
        j = i
        while j > 0 and comparator(seq[j-1], insert_item):
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = insert_item
    return seq


def second_number_is_more(first: str, second: str) -> bool:
    """Функция-компаратор для функции сортировки вставками."""
    if len(first) == len(second):
        return first < second
    first_temp = first + second
    second_temp = second + first
    return first_temp < second_temp


def solution(length: int, numbers: List[int]) -> None:
    print(''.join(insertions_sort(numbers, second_number_is_more)))


if __name__ == '__main__':
    solution(*read_input())
