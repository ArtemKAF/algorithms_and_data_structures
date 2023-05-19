"""ID 87198914
Алгоритм быстрой сортировки inplace для решения задачи:
Отсортировать таблицу результатов следующим образом: при сравнении двух
соперников выше будет идти тот, у которого решено больше задач.
При равенстве числа решённых задач первым идёт соперник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше
в алфавитном (лексикографическом) порядке.
"""
from dataclasses import dataclass
from typing import List


@dataclass
class Competitor():
    """Класс соперников."""
    nickname: str
    score: int
    penalty: int

    def __str__(self):
        """Метод строкового представления объекта."""
        return self.nickname

    def __lt__(self, other):
        """Метод проверки, что результаты соперника хуже, чем другого."""
        return (
            self.score < other.score
            or self.score == other.score and self.penalty > other.penalty
            or self.score == other.score and self.penalty == other.penalty
            and self.nickname > other.nickname
        )

    def __gt__(self, other) -> bool:
        """Метод проверки, что результаты первого лучше, другого."""
        return (
            self.score > other.score
            or self.score == other.score and self.penalty < other.penalty
            or self.score == other.score and self.penalty == other.penalty
            and self.nickname < other.nickname
        )


def read_input() -> List[Competitor]:
    """Функция считывания данных о соперниках из стандартного потока ввода.
    Возвращает список объектов класса Competitor с результатами соперников.
    """
    n: int = int(input().strip())
    array = [
        Competitor(
            *[int(value) if value.isnumeric() else value for value in (
                input().strip().split()
            )]
        )
        for _ in range(n)
    ]
    return array


def partition(seq: List[Competitor], left: int, right: int) -> int:
    """Функция, упорядочивающая результаты соперников относительно опорного в
    пределах [left, right] таким образом, что в левую часть списка результатов
    переносятся все результаты больше опорного, а в правую меньше опорного.
    В результате функция возвращает индекс соперника, относительно которого
    разделены элементы на больше опорного и меньше.
    Вход:
    [['alla', 4, 1000], ['gena', 6, 1000], ['gosha', 2, 90]
    Выход:
    0
    """
    pivot = (left + right) // 2
    seq_pivot = seq[pivot]
    while left < right:
        while left < right and seq[right] < seq_pivot:
            right -= 1
        while left < right and seq[left] > seq_pivot:
            left += 1
        if left < right:
            seq[left], seq[right] = seq[right], seq[left]
            left += 1
            right -= 1
    if seq[right] > seq_pivot or seq[right] == seq_pivot:
        return right
    return right - 1


def quick_sort(seq: List[Competitor], left: int, right: int) -> None:
    """Функция сортировки списка результатов участников."""
    if right - left >= 1:
        middle = partition(seq, left, right)
        quick_sort(seq, left, middle)
        quick_sort(seq, middle + 1, right)


if __name__ == '__main__':
    competitors = read_input()
    quick_sort(competitors, 0, len(competitors) - 1)
    print(*competitors, sep='\n')
