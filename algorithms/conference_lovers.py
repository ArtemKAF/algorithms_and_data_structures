""" Алгоритм решения следующей задачи:
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Для каждого студента известен ID университета, в котором он учится.
Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше
всего учащихся.

Формат ввода:
Первая строка - количество студентов в списке - n (1 ≤ n ≤ 15 000).
Вторая строка - n целых чисел через пробел - ID вуза каждого студента. Каждое
из чисел находится в диапазоне от 0 до 10 000.
Третья строка - число k.

Формат вывода:
Выведите через пробел k ID вузов с максимальным числом участников.
Они должны быть отсортированы по убыванию популярности (по количеству гостей
от конкретного вуза). Если более одного вуза имеет одно и то же количество
учащихся, то выводить их ID нужно в порядке возрастания. 
"""


from typing import List, Tuple


def read_input() -> Tuple[List[int], int]:
    number_students = int(input().strip())
    university_ids: List[int] = [int(x) for x in input().strip().split()]
    number_ids = int(input().strip())
    return university_ids, number_ids


def count_students(seq: List[int]):
    cache = {}
    for elem in seq:
        cache[elem] = 1 + cache.get(elem, 0)
    return cache


def solution(university_ids: List[int], number_ids: int) -> int:
    cnt = count_students(university_ids)
    most_common = list(
            dict(
                sorted(cnt.items(), key=lambda item: item[1], reverse=True)
            ).keys()
        )[:number_ids]
    return most_common


if __name__ == '__main__':
    print(*solution(*read_input()))
