class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class StackMaxEffective:
    def __init__(self):
        self.head = None
        self.max_values = []

    def push(self, item):
        node = Node(item, self.head)
        self.head = node
        if len(self.max_values) == 0 or item >= self.max_values[-1]:
            self.max_values.append(item)

    def pop(self):
        if self.head is None:
            print('error')
        else:
            item = self.head.value
            self.head = self.head.next_item
            if item == self.max_values[-1]:
                self.max_values.pop()
            return item

    def peek(self):
        return self.head.value

    def size(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next_item
        return count

    def get_max(self):
        if self.head is not None:
            return self.max_values[-1]
        return None


def test():
    count = int(input().strip())
    stack = StackMaxEffective()
    command = []
    while count > 0:
        command = input().strip().split()
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'peek':
            print(stack.peek())
        if command[0] == 'size':
            print(stack.size())
        if command[0] == 'get_max':
            print(stack.get_max())
        count -= 1


if __name__ == '__main__':
    test()
