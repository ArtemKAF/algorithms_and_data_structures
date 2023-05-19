"""Реализация алгоритма проверки сбалансированно бинарное дерево или нет."""


class Node:
    """Класс узла бинарного дерева."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def count_height(root) -> int:
    """Функция подсчета высоты бинарного дерева с корнем root."""
    if root is None:
        return 0
    return 1 + max(count_height(root.left), count_height(root.right))


def solution(root) -> bool:
    """Функция проверки сбалансировано ли двоичное дерево.
    Критерием сбалансированности выступает разница высот правого и левого
    поддерева не более 1 для всех поддеревьев дерева с корнем root."""
    if root is None:
        return True
    if (
        abs(count_height(root.left) - count_height(root.right)) <= 1
        and solution(root.left) and solution(root.right)
    ):
        return True
    else:
        return False


def test():
    node6 = Node(6)
    node5 = Node(5)
    node4 = Node(4, node5, node6)
    node3 = Node(3, node4, None)
    node2 = Node(2)
    node1 = Node(1, node3, node2)
    node0 = Node(0, node1, None)
    assert not solution(node0)


if __name__ == '__main__':
    test()
