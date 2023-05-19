""" ID 85770457 Алгоритм решения следующей задачи:

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить,
имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый
участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого
участка. Если участок пустой, эта величина будет равна нулю — расстояние до
самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта
улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены
нулями.
"""
from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    """Функция считывания данных из стандартного ввода.

    Длиннны улицы и списка номеров домов.
    None = (5, [0, 1, 4, 9, 0])
    None = (7, [5, 0, 3, 6, 2, 12, 1])
    """
    length = int(input().strip())
    houses_numbers = list(map(int, input().strip().split()))
    return length, houses_numbers


def passing_on_street(
        length: int,
        houses_numbers: List[int],
        distances: List[int],
        reverse: bool
) -> List[int]:
    """Проход по улице с заполнением расстояний до пустого участка.

    В зависимости от значения reverse расстояния заполняются слева от пустого
    участка или справа.
    На входе длинна улицы (количество участков), список номеров домов,
    список расстояний до пустого участка и флаг направления прохода.
    На выходе список расстояний до пустого участка слева или справа.
    5, [0, 1, 4, 9, 0], [5, 5, 5, 5, 5], False = [0, 1, 2, 3, 0]
    5, [0, 9, 4, 1, 0], [0, 3, 2, 1, 0], True = [0, 1, 2, 1, 0]
    7, [5, 0, 3, 6, 2, 12, 1], [7, 7, 7, 7, 7, 7, 7], False
     = [7, 0, 1, 2, 3, 4, 5]
    7, [1, 12, 2, 6, 3, 0, 5], [5, 4, 3, 2, 1, 0, 7], True
     = [1, 0, 1, 2, 3, 4, 5]
    """
    empty_place = None
    for i in range(length):
        if houses_numbers[i] == 0:
            empty_place = i
            if not reverse:
                distances[i] = 0
            continue
        if (
            empty_place is not None
            and distances[i] > i - empty_place
        ):
            distances[i] = i - empty_place
    return distances


def solution(length: int, houses_numbers: List[int]) -> List[int]:
    """Функция решения поставленной задачи.

    На входе длина улицы (количество участков на улице) и номера домов.
    На выходе список с расстояниями от участка до ближайшего к нему пустого
    участка.
    5, [0, 1, 4, 9, 0] = [0, 1, 2, 1, 0]
    7, [5, 0, 3, 6, 2, 12, 1] = [1, 0, 1, 2, 3, 4, 5]
    """
    distances = [length] * length
    distances = passing_on_street(length, houses_numbers, distances,
                                  reverse=False)
    houses_numbers = houses_numbers[::-1]
    distances = distances[::-1]
    distances = passing_on_street(length, houses_numbers, distances,
                                  reverse=True)
    return distances[::-1]


if __name__ == '__main__':
    print(*solution(*read_input()))
