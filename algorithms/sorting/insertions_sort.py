from typing import List


def insertions_sort(seq: List[int]) -> List[int]:
    '''Функция сортировки последовательности методом вставками.'''
    for i in range(1, len(seq)):
        insert_item = seq[i]
        j = i
        while j > 0 and insert_item < seq[j-1]:
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = insert_item
    return seq
