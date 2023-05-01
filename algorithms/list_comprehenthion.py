'''Реализация задачи: вывести список комбинаций целых чисел, сумма которых
не равна заданному числу, сгенерированный при помощи list comprehension.'''
from typing import List, Optional


def solution(x: int, y: int, z: int, n: int) -> List[Optional[List[int]]]:
    return (
        [
            [i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if i + j + k != n
        ]
    )


if __name__ == '__main__':
    print(solution(6, 4, 2, 4))
