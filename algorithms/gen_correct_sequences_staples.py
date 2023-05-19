"""Реализация вывода в консоль всех кооретных вариантов скобочных
последовательностей рекурсивно."""


def read_input() -> int:
    return int(input().strip())


def gen_correct_parenthesis_sequence(
            depth: int, st_open: int, st_close: int, prefix: str
        ) -> None:
    if depth == 0:
        if st_open == 0 and st_close == 0:
            print(prefix)
    else:
        gen_correct_parenthesis_sequence(
            depth - 1, st_open - 1, st_close, prefix + '('
        )
        if st_close > st_open:
            gen_correct_parenthesis_sequence(
                depth - 1, st_open, st_close - 1, prefix + ')'
            )


if __name__ == '__main__':
    n = read_input()
    gen_correct_parenthesis_sequence(n + n, n, n, '')
