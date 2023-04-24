'''ID: 86359348 Реализация двусторонней очереди на массиве в виде кольцевого
буфера.
'''
from typing import List, Optional, Union


class DequeIsEmpty(Exception):
    '''Класс ошибки доступа к элементу в пустой двусторонней очереди.'''
    ...


class DequeIsFull(Exception):
    '''Класс ошибки добавления элемента в заполненную двустороннюю очередь.'''
    ...


class MyDeque:
    '''Двусторонняя очередь на массиве в виде кольцевого буфера.'''

    def __init__(self, deque_size: int = 10) -> None:
        self.__items__: List[Optional[int]] = [None] * deque_size
        self.__deque_size__: int = 0
        self.__head__: int = 0
        self.__tail__: int = 0

    def __get_new_index__(self, index: int, step: int) -> int:
        '''Получение нового индекса, в зависимости от величины step.'''
        return (index + step) % len(self.__items__)

    def size(self) -> int:
        '''Получение количества элементов в двусторонней очереди.'''
        return self.__deque_size__

    def is_empty(self) -> bool:
        '''Проверка двусторонней очереди на пустоту.'''
        return self.__deque_size__ == 0

    def push_back(self, item: int) -> None:
        '''Вставка элемента в конец двусторонней очереди.'''
        if self.__deque_size__ >= len(self.__items__):
            raise DequeIsFull('Двусторонняя очередь заполнена.')

        self.__items__[self.__tail__] = item
        if (
            self.__deque_size__ == 0
            and self.__head__ == self.__tail__
        ):
            self.__head__ = self.__get_new_index__(self.__head__,  -1)

        self.__tail__ = self.__get_new_index__(self.__tail__, 1)
        self.__deque_size__ += 1

    def push_front(self, item: int) -> None:
        '''Вставка элемента в начало двусторонней очереди.'''
        if self.__deque_size__ >= len(self.__items__):
            raise DequeIsFull('Двусторонняя очередь заполнена.')

        self.__items__[self.__head__] = item
        if (
            self.__deque_size__ == 0
            and self.__head__ == self.__tail__
        ):
            self.__tail__ = self.__get_new_index__(self.__tail__, 1)

        self.__head__ = self.__get_new_index__(self.__head__,  -1)
        self.__deque_size__ += 1

    def pop_front(self) -> Union[int, str]:
        '''Извлечение элемента из начала двусторонней очереди.'''
        if self.__deque_size__ > 0:
            self.__head__ = self.__get_new_index__(self.__head__, 1)
            item = self.__items__[self.__head__]
            self.__items__[self.__head__] = None
            self.__deque_size__ -= 1
            return item
        raise DequeIsEmpty('Двустороннея очередь пуста.')

    def pop_back(self) -> Union[int, str]:
        '''Извлечение элемента из конца двусторонней очереди.'''
        if self.__deque_size__ > 0:
            self.__tail__ = self.__get_new_index__(self.__tail__, -1)
            item = self.__items__[self.__tail__]
            self.__items__[self.__tail__] = None
            self.__deque_size__ -= 1
            return item
        raise DequeIsEmpty('Двустороннея очередь пуста.')


def test():
    count = int(input().strip())
    size = int(input().strip())
    deque = MyDeque(size)
    commands = {
        'push_back': deque.push_back,
        'push_front': deque.push_front,
        'pop_back': deque.pop_back,
        'pop_front': deque.pop_front
    }
    while count > 0:
        command, *args = input().strip().split()
        if commands.get(command) is not None:
            try:
                if len(args) == 0:
                    print(commands.get(command)())
                else:
                    commands.get(command)(*args)
            except (DequeIsEmpty, DequeIsFull, ):
                print('error')
        count -= 1


if __name__ == '__main__':
    test()
