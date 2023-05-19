"""ID: 86433483 Реализация калькулятора с постфиксной нотацией, при условии,
что деление математическое целочисленное.
"""
from typing import List, Optional


class StackIsEmpty(Exception):
    """Класс ошибки доступа к элементу в пустом стеке."""
    ...


class Stack:
    """Класс стека на базе списка."""

    def __init__(self) -> None:
        self._items: List[int] = []

    def is_empty(self) -> bool:
        """Проверка стека на пустоту."""
        return not self._items

    def push(self, item: int) -> None:
        """Добавление элемента в стек."""
        self._items.append(item)

    def pop(self) -> Optional[int]:
        """Извлечение элемента из стека."""
        if not self.is_empty():
            return self._items.pop()
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
            try:
                stack.push(operations.get(element)(a, b))
            except UnboundLocalError:
                print(
                    f'Недостаточно операндов для выполнения операции {element}'
                )
        else:
            stack.push(int(element))
    try:
        print(stack.pop())
    except StackIsEmpty:
        print('error')


if __name__ == '__main__':
    test()
