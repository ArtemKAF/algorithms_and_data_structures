"""Реверс двусвязного списка."""


class DoublyLinkedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    while node:
        next_node = node.next
        node.next, node.prev = node.prev, node.next
        if next_node is None:
            return node
        node = next_node


def test():
    node3 = DoublyLinkedNode("node3")
    node2 = DoublyLinkedNode("node2")
    node1 = DoublyLinkedNode("node1")
    node0 = DoublyLinkedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()
