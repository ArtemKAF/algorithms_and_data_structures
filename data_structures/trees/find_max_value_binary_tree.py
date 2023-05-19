"""Поиск максимального элемента в бинарном дереве при помощи стека."""
from typing import List


class Node:
    """Класс узла двоичного дерева."""
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> int:
    """Функция посика максимального значения в узлах двоичного дерева."""
    stack: List[int] = []
    max_value = None
    if root is not None:
        stack.append(root)

        while len(stack) > 0:
            current_node = stack.pop()
            if max_value is None or max_value < current_node.value:
                max_value = current_node.value
            if current_node.right is not None:
                stack.append(current_node.right)
            if current_node.left is not None:
                stack.append(current_node.left)
    return max_value
