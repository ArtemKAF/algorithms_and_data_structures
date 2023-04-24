'''Алгоритм решения следующей задачи:

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
'''
from typing import List, Tuple


def read_input() -> Tuple[int, List[int]]:
    length = int(input().strip())
    houses_numbers = list(map(int, input().strip().split()))
    return length, houses_numbers


def solution(length: int, houses_numbers: List[int]) -> List[int]:
    distances = [length] * length
    empty_place = None
    for i in range(length):
        if houses_numbers[i] == 0:
            empty_place = i
            distances[i] = 0
            j = i - 1
            k = 1
            while j >= 0 and distances[j] > k:
                distances[j] = k
                j -= 1
                k += 1
        if (
                empty_place is not None
                and distances[i] > i - empty_place
           ):
            distances[i] = i - empty_place
    return distances


if __name__ == '__main__':
    print(*solution(*read_input()))
