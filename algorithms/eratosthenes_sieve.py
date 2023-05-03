'''Алгоритм реализации решето Эратосфена.'''
from typing import List, Optional


def eratosthenes_sieve(numbers: List[bool]) -> List[Optional[int]]:
    for number in range(2, len(numbers)):
        if numbers[number]:
            for i in range(2*number, len(numbers), number):
                numbers[i] = False
    return numbers


def read_input() -> int:
    return int(input('Введите количество проверяемых чисел: ').strip())


if __name__ == '__main__':
    for number, result in enumerate(eratosthenes_sieve([True] * read_input())):
        print(number, "-", "простое" if result else "составное")
