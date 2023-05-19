"""Реализация алгоритма сортировки слиянием."""
from typing import List


# TODO: Подумать над оптимизацией.
def merge(arr: List[int], lf: int, mid: int, rg: int) -> List[int]:
    cache = [None] * (rg - lf)
    i, j, k = lf, mid, 0
    while k < rg - lf:
        if j == rg or arr[i] <= arr[j] and i < mid:
            cache[k] = arr[i]
            i += 1
            k += 1
            continue
        cache[k] = arr[j]
        j += 1
        k += 1
    arr[lf:rg] = cache[:]
    return arr


def merge_sort(arr: List[int], lf: int, rg: int) -> None:
    if rg - lf <= 1:
        return
    mid = lf + (rg - lf) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
