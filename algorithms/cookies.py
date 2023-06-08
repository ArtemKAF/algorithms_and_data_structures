""" Алгоритм решения следущей задачи:
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Печенья могут быть разного размера. У каждого ребёнка есть фактор
жадности — минимальный размер печенья, которое он возьмёт. Нужно выяснить,
сколько ребят останутся довольными в лучшем случае, когда они действуют
оптимально. Каждый ребёнок может взять не больше одного печенья.

Формат ввода:
Первая строка - n - количество детей.
Вторая строка - n чисел, разделённых пробелом, каждое из которых - фактор
жадности ребёнка. Это натуральные числа, не превосходящие 1000.
Третья строка - число m - количество печенек.
Четвертая строка - m натуральных чисел, разделённых пробелом - размеры печенек.
Размеры печенек не превосходят 1000.
Числа n и m не превосходят 10000.

Формат вывода:
Одно число - количество детей, которые останутся довольными.
"""


from typing import List, Tuple


def read_input() -> Tuple[List[int]]:
    childrens = int(input().strip())
    greed_factors: List[int] = [int(x) for x in input().strip().split()]
    cookies = int(input().strip())
    cookies_sizes: List[int] = [int(x) for x in input().strip().split()]
    return greed_factors, cookies_sizes


def solution(greed_factors: List[int], cookies_sizes: List[int]) -> int:
    cookies_sizes.sort()
    greed_factors.sort(reverse=True)
    happy_childrens = 0
    index = 0
    while len(cookies_sizes) > 0 and index < len(greed_factors):
        if greed_factors[index] <= cookies_sizes[-1]:
            cookies_sizes.pop(-1)
            happy_childrens += 1
        index += 1
    return happy_childrens


if __name__ == '__main__':
    print(solution(*read_input()))
