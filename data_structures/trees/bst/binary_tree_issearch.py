"""Реализация алгоритма проверки является ли бинарное дерево деревом поиска."""


class Node:
    """Класс узла двоичного дерева."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def find_max(root) -> int:
    """Функция нахождения максимального значения в дереве с корнем root."""
    if root.left is None and root.right is None:
        return root.value
    if root.left is not None and root.right is not None:
        return max(root.value, find_max(root.left), find_max(root.right))
    else:
        if root.left is not None:
            return max(root.value, find_max(root.left))
        else:
            return max(root.value, find_max(root.right))


def find_min(root) -> int:
    """Функция нахождения минимального значения в дереве с корнем root."""
    if root.left is None and root.right is None:
        return root.value
    if root.left is not None and root.right is not None:
        return max(root.value, find_min(root.left), find_min(root.right))
    else:
        if root.left is not None:
            return max(root.value, find_min(root.left))
        else:
            return max(root.value, find_min(root.right))


def solution(root) -> bool:
    """Функция проверки двочное дерево поиска с корнем root или нет."""
    if root is None:
        return True
    if (
            (
                root.left is not None
                and root.value <= find_max(root.left)
            )
            or
            (
                root.right is not None
                and root.value >= find_min(root.right)
            )
    ):
        return False
    return solution(root.left) and solution(root.right)
