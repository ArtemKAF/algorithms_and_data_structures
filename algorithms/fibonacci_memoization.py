"""Оптимизации рекурсивной реализации алгоритма вывода чисел Фибоначчи."""
from functools import lru_cache


@lru_cache(None)
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def memoized(function):
    cache = {}

    def wrapped(key):
        value = cache.get(key)
        if value is None:
            value = cache[key] = function(key)
        return value
    return wrapped


@memoized
def fibonaci(n):
    if n in (0, 1):
        return n
    return fibonaci(n - 1) + fibonaci(n - 2)


def read_input() -> int:
    return int(input().strip())


def solution() -> int:
    return fibonaci(read_input())


if __name__ == '__main__':
    print(solution())
