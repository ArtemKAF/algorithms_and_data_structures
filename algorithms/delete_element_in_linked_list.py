'''Реализация удаления элемента из односвязного списка по индексу.'''


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_list(node):
    while node:
        print(node.value)
        node = node.next_item


def get_node(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(head, index):
    if index == 0:
        node = head.next_item
        return node
    node = get_node(head, index)
    previouse_node = get_node(head, index - 1)
    previouse_node.next_item = node.next_item
    return head


def test(index):
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0, index)
    print_list(node0)


if __name__ == '__main__':
    test(int(input()))
