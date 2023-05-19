"""Реализация алгоритма вывода значений узлов бинарного дерева из заданного
диапазона.
"""


class Node:
    """Класс узла двоичного дерева."""
    def __init__(self, left=None, right=None, value=0) -> None:
        self.right = right
        self.left = left
        self.value = value


def print_range(node: Node, left_limit: int, right_limit: int) -> None:
    """Функция вывода на печать значений узлов бинарного дерева из диапазона
    [left_limit:right_limit]
    """
    if node is None:
        return None

    if node.value >= left_limit:
        print_range(node.left, left_limit, right_limit)
    if left_limit <= node.value <= right_limit:
        print(node.value)
    if node.value <= right_limit:
        print_range(node.right, left_limit, right_limit)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
