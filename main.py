'''Основной скрипт тестирования алгоритмов сортировок.'''
from typing import List

from algorithms.sorting import bubblesort as bs
from algorithms.sorting import countsort as cs
from algorithms.sorting import shakersort as sh_s
from utils import timeuse as tu

if __name__ == '__main__':

    not_sorted_list: List[int] = [
        5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9,
        15, 99, 194, 2, 111, 0, 13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39,
        174, 15, 100, 59, 37, 82, 61, 90, 33, 64, 348, 279, 13, 11, 28, 63, 93
    ]

    sorted_list: List[int] = tu.time_use(bs.bubble_sort)(not_sorted_list)
    print('\n', *sorted_list, end='\n\n')

    not_sorted_list: List[int] = [
        5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9,
        15, 99, 194, 2, 111, 0, 13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39,
        174, 15, 100, 59, 37, 82, 61, 90, 33, 64, 348, 279, 13, 11, 28, 63, 93
    ]

    sorted_list: List[int] = tu.time_use(cs.count_sort)(not_sorted_list)
    print('\n', *sorted_list, end='\n\n')

    not_sorted_list: List[int] = [
        5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9,
        15, 99, 194, 2, 111, 0, 13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39,
        174, 15, 100, 59, 37, 82, 61, 90, 33, 64, 348, 279, 13, 11, 28, 63, 93
    ]

    sorted_list: List[int] = tu.time_use(sh_s.shakersort)(not_sorted_list)
    print('\n', *sorted_list, end='\n\n')
