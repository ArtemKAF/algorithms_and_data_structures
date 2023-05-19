"""Реализация поиска элемента в односвязном списке."""


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    count = 0
    while node:
        if node.value == elem:
            return count
        node = node.next_item
        count += 1
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()
