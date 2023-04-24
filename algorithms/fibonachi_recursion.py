'''Рекурсивная реализация алгоритма суммы чисел Фибоначчи.'''


def fibonachi(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


def read_input() -> int:
    return int(input().strip())


def solution() -> int:
    print(fibonachi(read_input()))


if __name__ == '__main__':
    solution()
