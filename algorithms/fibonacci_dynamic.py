'''Алгоритм вывода первых N чисел Фибоначчи при помощи функции генератора.'''


def fibonacci(x: int):
    first, second = 0, 1
    for i in range(x):
        yield first
        first, second = second, first + second


def read_input() -> int:
    return int(input('Введите количество чисел Фибоначчи: ').strip())


if __name__ == '__main__':
    try:
        x = read_input()
    except ValueError:
        x = 0
    fib = fibonacci(x)
    for _ in range(x):
        print(next(fib), end=' ')
    print('\n')
