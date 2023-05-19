"""ID: 86433540 Реализация двусторонней очереди на массиве в виде кольцевого
буфера.
"""
from typing import List, Optional, Union


class DequeIsEmpty(Exception):
    """Класс ошибки доступа к элементу в пустой двусторонней очереди."""
    ...


class DequeIsFull(Exception):
    """Класс ошибки добавления элемента в заполненную двустороннюю очередь."""
    ...


class MyDeque:
    """Двусторонняя очередь на массиве в виде кольцевого буфера."""

    def __init__(self, deque_size: int = 10) -> None:
        self._items: List[Optional[int]] = [None] * deque_size
        self._deque_size: int = 0
        self._head: int = 0
        self._tail: int = 0

    def _get_new_index(self, index: int, step: int) -> int:
        """Получение нового индекса, в зависимости от величины step."""
        return (index + step) % len(self._items)

    def size(self) -> int:
        """Получение количества элементов в двусторонней очереди."""
        return self._deque_size

    def _is_empty(self) -> bool:
        """Проверка двусторонней очереди на пустоту."""
        return self._deque_size == 0

    def push_back(self, item: int) -> None:
        """Вставка элемента в конец двусторонней очереди."""
        if self._deque_size >= len(self._items):
            raise DequeIsFull('Двусторонняя очередь заполнена.')

        self._items[self._tail] = item
        if (
            self._deque_size == 0
            and self._head == self._tail
        ):
            self._head = self._get_new_index(self._head,  -1)

        self._tail = self._get_new_index(self._tail, 1)
        self._deque_size += 1

    def push_front(self, item: int) -> None:
        """Вставка элемента в начало двусторонней очереди."""
        if self._deque_size >= len(self._items):
            raise DequeIsFull('Двусторонняя очередь заполнена.')

        self._items[self._head] = item
        if (
            self._deque_size == 0
            and self._head == self._tail
        ):
            self._tail = self._get_new_index(self._tail, 1)

        self._head = self._get_new_index(self._head,  -1)
        self._deque_size += 1

    def pop_front(self) -> Union[int, str]:
        """Извлечение элемента из начала двусторонней очереди."""
        if self._deque_size > 0:
            self._head = self._get_new_index(self._head, 1)
            item = self._items[self._head]
            self._items[self._head] = None
            self._deque_size -= 1
            return item
        raise DequeIsEmpty('Двустороннея очередь пуста.')

    def pop_back(self) -> Union[int, str]:
        """Извлечение элемента из конца двусторонней очереди."""
        if self._deque_size > 0:
            self._tail = self._get_new_index(self._tail, -1)
            item = self._items[self._tail]
            self._items[self._tail] = None
            self._deque_size -= 1
            return item
        raise DequeIsEmpty('Двустороннея очередь пуста.')


def test():
    count = int(input().strip())
    size = int(input().strip())
    deque = MyDeque(size)
    while count > 0:
        command, *args = input().strip().split()
        try:
            if len(args) == 0:
                print(getattr(deque, command)())
            else:
                getattr(deque, command)(*args)
        except (DequeIsEmpty, DequeIsFull, ):
            print('error')
        except AttributeError as err:
            print(err)
        count -= 1


if __name__ == '__main__':
    test()
