'''ID: 86355680 Реализация калькулятора с постфиксной нотацией, при условии,
что деление математическое целочисленное.
'''
from typing import Optional, List


class StackIsEmpty(Exception):
    '''Класс ошибки доступа к элементу в пустом стеке.'''
    ...


class Stack:
    '''Класс стека на базе списка.'''

    def __init__(self) -> None:
        self.__items__: List[int] = []

    def is_empty(self) -> bool:
        '''Проверка стека на пустоту.'''
        return len(self.__items__) == 0

    def push(self, item: int) -> None:
        '''Добавление элемента в стек.'''
        self.__items__.append(item)

    def pop(self) -> Optional[int]:
        '''Извлечение элемента из стека.'''
        if not self.is_empty():
            return self.__items__.pop()
        raise StackIsEmpty('Стек пуст.')


def test():
    stack = Stack()
    operations = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: a//b
    }
    for element in list(input().strip().split()):
        if operations.get(element) is not None:
            try:
                b, a = stack.pop(), stack.pop()
            except StackIsEmpty:
                print('error')
            stack.push(operations.get(element)(a, b))
        else:
            stack.push(int(element))
    try:
        print(stack.pop())
    except StackIsEmpty:
        print('error')


if __name__ == '__main__':
    test()
