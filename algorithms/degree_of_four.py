'''Реализация алгоритма проверки числа на степень четырёх.'''


def read_input() -> int:
    a = int(input().strip())
    return a


def solution(a: int) -> bool:
    return ((a & (a - 1)) == 0) and (a % 3 == 1)


if __name__ == '__main__':
    print(solution(read_input()))
