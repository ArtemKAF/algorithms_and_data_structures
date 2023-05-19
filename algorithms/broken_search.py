""" ID 87198994

Алгоритм поиска в массиве, в котором отсортированные по возрастанию уникальные
числа занесены со сдвигом.
Необходимо обеспечить возможность находить элемент за О(logn)
"""
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Функция бинарного поиска.
    Возвращает индекс искомого элемента или -1, если элемента нет в массиве.
    Вход:
    [30, 33, 55, 90, 1, 8, 12], 8
    Выход:
    5
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        if (
            (
                nums[left] <= nums[middle]
                and nums[left] <= target < nums[middle]
            )
            or (
                nums[left] > nums[middle]
                and not (nums[middle] < target <= nums[right])
            )
        ):
            right = middle - 1
        else:
            left = middle + 1
    return -1
