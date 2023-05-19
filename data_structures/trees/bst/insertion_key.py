"""Реализация алгоритма добавления ключа в двоичное дерево поиска."""


class Node:
    """Класс узла двоичного дерева."""
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key) -> Node:
    """Функция добавления ключа в двоичное дерево с сохранением его свойства
    быть двоичным деревом поиска.
    """
    if root is None:
        return Node(value=key)

    if root.value > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
