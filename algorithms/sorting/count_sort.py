from typing import List


def count_sort(seq: List[int]) -> List[int]:
    """Функция сортировки последовательности методом сортировки подсчетом."""
    freq = [0]*(max(seq)+1)
    for i in range(len(seq)):
        freq[seq[i]] += 1
    j = 0
    for i in range(len(freq)):
        while freq[i] > 0:
            seq[j] = i
            freq[i] -= 1
            j += 1
    return seq
