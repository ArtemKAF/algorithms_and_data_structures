"""Реализация алгоритма разложения числа на простые множители."""


def read_input() -> int:
    return int(input().strip())


def factorization(number: int) -> None:
    simple_multiplier = 2

    while simple_multiplier * simple_multiplier <= number:
        if number % simple_multiplier == 0:
            print(simple_multiplier, end=' ')
            number //= simple_multiplier
        else:
            simple_multiplier += 1

    if number > 1:
        print(number)


if __name__ == '__main__':
    factorization(read_input())
