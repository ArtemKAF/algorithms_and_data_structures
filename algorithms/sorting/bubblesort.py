def bubble_sort(seq):
    """ Функция сортировки последовательности методом сортировки пузырьком"""
    for x in range(len(seq)-1, 0, -1):
        while x < len(seq) and seq[x-1] > seq[x]:
            seq[x], seq[x-1] = seq[x-1], seq[x]
            x += 1
    return seq
