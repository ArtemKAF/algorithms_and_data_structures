'''Реализация задачи транспонирования матрицы.'''
from typing import List, Tuple


def read_input() -> Tuple[int, int, List[List[int]]]:
    m = int(input().strip())
    n = int(input().strip())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().strip().split())))
    return m, n, matrix


def solution(m: int, n: int, matrix: List[List[int]]) -> List[List[int]]:
    transposed_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix


if __name__ == '__main__':
    for i in solution(*read_input()):
        print(' '.join(list(map(str, i))))
