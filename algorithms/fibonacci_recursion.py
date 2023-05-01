'''Рекурсивная реализация алгоритма вычисления N-го числа Фибоначчи.'''
from typing import Tuple


def fibonacci_simple(n: int) -> int:
    if n == 1 or n == 0:
        return n
    return fibonacci_simple(n - 1) + fibonacci_simple(n - 2)


def fibonacci_cache_dict(n, cache={}):
    if n in cache:
        return cache[n]
    if n in [0, 1]:
        return n
    cache[n] = (fibonacci_cache_dict(n - 1) + fibonacci_cache_dict(n - 2))
    return cache[n]


def read_input() -> Tuple[int]:
    print('0 - Простой рекурсивный')
    print('1 - Оптимизированный рекурсивный с кэшем в виде словаря')
    return (
        int(input('Введите номер желаемого алгоритма: ').strip()),
        int(input('Введите номер вычисляемого числа Фибоначчи: ').strip()),
    )


def solution() -> int:
    algorithms = {0: fibonacci_simple, 1: fibonacci_cache_dict}
    algorithm, n = read_input()
    if algorithms.get(algorithm):
        return algorithms.get(algorithm)(n)


if __name__ == '__main__':
    print(solution())
