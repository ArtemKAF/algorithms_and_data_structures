""" Динамический и рекурсивные алгоритмы решения задачи:
Полёты на Марс с участием человека уже не за горами. Команда для полёта почти
сформирована. Осталось одно свободное место и масса претендентов на него.

Для решения этой задачи создан проект С.Ч.И.Т.А.Л.К.А. — Стандартный Числовой
Иррационально-Точный АЛгоритм Кастинга Астронавтов.

На практике алгоритм реализуется так:
Группа претендентов выстраивается в круг. Число претендентов обозначим через
N, претенденты получают номера от 1 до N.

Претенденты получают лист бумаги, на котором написана считалка. Считалка
состоит из определённого количества «ритмических частей», тактов. Число тактов
обозначим через K.

Претендент под номером 1 произносит вслух считалку и, начиная с себя, на
каждый такт указывает на каждого из претендентов. Тот, на ком считалка
закончилась, выбывает из числа претендентов.

Участник, следующий за выбывшим, вновь начинает произносить считалку, начав с
себя и указывая последовательно на оставшихся претендентов.

Отсев продолжается до тех пор, пока не останется только один претендент.
"""
from sys import stdin


def read_input() -> tuple[list[int], int]:
    amount = int(stdin.readline().strip())
    chalengers = [x for x in range(1, amount + 1)]
    tacts = int(stdin.readline().strip())
    return chalengers, tacts


def recursive_solution(
    chalengers: list[int],
    tacts: int,
    start: int = 0
) -> int:
    if len(chalengers) == 1:
        return chalengers.pop()
    else:
        start = (start + tacts - 1) % len(chalengers)
        chalengers.pop(start)
        return recursive_solution(
            chalengers=chalengers,
            tacts=tacts,
            start=start
        )


def dynamic_solution(chalengers: list[int], tacts: int, start: int = 0) -> int:
    while len(chalengers) > 1:
        start = (start + tacts - 1) % len(chalengers)
        chalengers.pop(start)
    return chalengers[0]


if __name__ == '__main__':
    input_data = read_input()
    print(dynamic_solution(*input_data))
    print(recursive_solution(*input_data))
