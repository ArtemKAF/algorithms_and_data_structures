"""Реализация алгоритма генерации вариантов буквенных комбинаций из заданного
набора."""


def read_input() -> str:
    return input().strip()


def gen_combinations(depth: int, prefix: str) -> None:
    """Функция вывода в консоль комбинаций букв."""
    if depth == 0:
        print(prefix, end=' ')
    else:
        for letter in letters_dict.get(numbers[len(numbers) - depth]):
            gen_combinations(depth - 1, prefix + letter)


if __name__ == '__main__':
    letters_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    numbers = read_input()
    gen_combinations(len(numbers), '')
