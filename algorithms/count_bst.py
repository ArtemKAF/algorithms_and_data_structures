"""Реализация алгоритма подсчета количества различных бинарных деревьев
поиска, в узлах которых могут быть размещены числа от 1 до n включительно."""


def read_input() -> int:
    return int(input().strip())


def count_binary_search_trees(start: int, end: int, cache={}) -> int:
    count: int = 0

    if (start, end) in cache:
        return cache[(start, end)]

    if start > end:
        return 1

    for i in range(start, end + 1):
        cache[(start, i - 1)] = count_binary_search_trees(start, i - 1)
        cache[(i + 1, end)] = count_binary_search_trees(i + 1, end)
        count += cache[(start, i - 1)] * cache[(i + 1, end)]
    return count


if __name__ == '__main__':

    print(count_binary_search_trees(0, read_input() - 1))
