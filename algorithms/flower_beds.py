"""Реализация алгоритма решения следующей задачи:

Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме
земельного участка клумбы обозначаются просто горизонтальными отрезками,
лежащими на одной прямой. Для ландшафтных работ было нанято n садовников.
Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован
не очень хорошо, иногда один и тот же отрезок или его часть могли быть
обработаны сразу несколькими садовниками. Таким образом, отрезки,
обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный
обработанный отрезок затем станет клумбой. Нужно определить границы будущих
клумб.
Алгоритм получает количество садовников и список границ для каждого из них.
Необходимо вывести в отсортированном по возрастанию порядке границы клумб,
которые получатся по окончании работ садовников.
"""
from typing import List, Tuple

from algorithms.sorting.merge_sort_inplace import merge_sort


def read_input() -> Tuple[int, List[List[int]]]:
    n = int(input().strip())
    segments = []
    for _ in range(n):
        segments.append(list(map(int, input().strip().split())))
    return n, segments


def beds_borders(length: int, segments: List[List[int]]) -> List[List[int]]:
    """Функция определяющая границы итоговых клумб."""
    merge_sort(segments, 0, len(segments))
    beds = []
    start = segments[0][0]
    stop = segments[0][1]
    for index, segment in enumerate(segments):
        if stop < segment[1] and segment[0] <= stop:
            stop = segment[1]
        if stop < segment[0]:
            beds.append([start, stop])
            start, stop = segment[0], segment[1]
    beds.append([start, stop])
    return beds


if __name__ == '__main__':
    for bed in beds_borders(*read_input()):
        print(*bed)
