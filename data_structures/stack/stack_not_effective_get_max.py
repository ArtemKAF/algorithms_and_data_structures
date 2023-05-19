"""Стек на мессиве с неэффективным методом получения максимального элемента."""
from typing import List, Optional


class StackIsEmptyError(Exception):
    """Класс ошибки при извлечении элемента из пустого стека."""
    ...


class Stack:
    def __init__(self):
        self.__items__: List[int] = []

    def push(self, item) -> None:
        self.__items__.append(item)

    def pop(self) -> Optional[int]:
        if not self.is_empty():
            return self.__items__.pop()
        raise StackIsEmptyError('Стек пустой.')

    def peek(self) -> Optional[int]:
        if not self.is_empty():
            return self.__items__[-1]
        raise StackIsEmptyError('Стек пустой.')

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.__items__)

    def get_max(self) -> Optional[int]:
        if self.is_empty():
            return None
        return max(self.__items__)


def test():
    count = int(input().strip())
    stack = Stack()
    commands = {
        'push': stack.push,
        'pop': stack.pop,
        'peek': stack.peek,
        'size': stack.size,
        'get_max': lambda: print(stack.get_max()),
    }
    while count > 0:
        command, *args = input().strip().split()
        if commands.get(command) is not None:
            try:
                if len(args) == 0:
                    commands.get(command)()
                else:
                    commands.get(command)(int(*args))
            except StackIsEmptyError:
                print('error')
        count -= 1


if __name__ == '__main__':
    test()
