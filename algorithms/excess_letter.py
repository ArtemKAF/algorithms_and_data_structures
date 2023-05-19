"""Алгоритм нахождения лишней буквы во второй строке относительно первой."""
from collections import Counter
from typing import Tuple


def read_input() -> Tuple[str]:
    return input().strip(), input().strip()


def escess_letter(first_string: str, second_string: str) -> str:
    result = Counter(second_string) - Counter(first_string)
    return list(result.keys())[0]


if __name__ == '__main__':
    print(escess_letter(*read_input()))
