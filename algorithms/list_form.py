"""Реализация сложения двух натуральных чисел.
Одно из чисел представлено в виде списка цифр разрядов, а второе в свернутой
форме записи.
Результат выводится в виде списка цифр разрядов.
"""
from typing import List, Tuple


def read_input() -> Tuple[int, List[int], int]:
    digits = int(input().strip())
    first_number: List[int] = [int(x) for x in list(input().strip().split())]
    second_number = int(input().strip())
    return digits, first_number, second_number


def sum_numbers(
            digits: int, first_number: List[int], second_number: int
        ) -> List[int]:
    f_number = 0
    digit = 0
    while digits > 0:
        digits -= 1
        f_number += first_number[digits] * 10 ** digit
        digit += 1
    result_number = f_number + second_number
    result = []
    while result_number >= 1:
        result.append(result_number % 10)
        result_number //= 10
    return result[::-1]


if __name__ == '__main__':
    print(*sum_numbers(*read_input()))
