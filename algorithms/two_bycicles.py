"""Алгоритм решения следующей задачи:
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре.
У Васи есть копилка, в которую каждый день он может добавлять деньги
(если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.
У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
было денег в каждый из дней.
Задача: по заданной стоимости велосипеда найти первый день, в который Вася
смог бы купить первый велосипед и первый день, в который Вася смог бы купить
два велосипеда."""
from typing import List, Tuple


def read_input() -> Tuple[int, List[int], int]:
    """Функция считывания данных из стандартного ввода.

    Аргументы: None

    Возврат:
    Кортеж с количеством дней отслеживания Васиных накоплений, Васины
    накопления по дням и стоимость одного велосипеда:
    (6, [1, 2, 5, 6, 10, 12], 4)
    (4, [2, 4, 6, 6, 8, 9], 3)
    """
    n = int(input().strip())
    values = list(map(int, input().strip().split()))
    price = int(input().strip())
    return n, values, price


def binary_search(array: List[int], x: int, left: int, right: int) -> int:
    """Функция нахождения первого дня, когда Вася может купить велосипед.

    Аргументы:
    Список с Васиными накоплениями по дням, искомая сумма, левая и правая
    граница поиска:
    [1, 2, 5, 6, 10, 12], 4, 0, 6
    [2, 4, 6, 6, 8, 9], 3, 0, 6

    Возврат:
    Индекс элемента в списке, по которому найдена искомая сумма или -1, если
    не найдена:
    2
    1
    """
    if left >= right:
        return -1
    middle = (left + right) // 2
    if (
        array[middle] == x and binary_search(array, x, left, middle) == -1
        or array[middle] > x and binary_search(array, x, left, middle) == -1
    ):
        return middle
    elif array[middle] < x:
        return binary_search(array, x, middle + 1, right)
    else:
        return binary_search(array, x, left, middle)


def solution(n: int, values: List[int], price: int) -> List[int]:
    first_day = binary_search(values, price, 0, n)
    second_day = binary_search(values, price + price, first_day + 1, n)
    return list(map(lambda x: x + 1 if x >= 0 else x, (first_day, second_day)))


if __name__ == '__main__':
    print(*solution(*read_input()))
