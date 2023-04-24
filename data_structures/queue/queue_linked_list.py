class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class MyQueueLinkedList:
    def __init__(self):
        self.queue_size = 0
        self.head = None
        self.tail = None

    def size(self):
        return self.queue_size

    def put(self, item):
        node = Node(item)
        if self.queue_size == 0:
            self.head = node
            self.tail = node
        self.tail.next_item = node
        self.tail = node
        self.queue_size += 1

    def get(self):
        if self.queue_size > 0:
            item = self.head
            self.head = self.head.next_item
            item.next_item = None
            self.queue_size -= 1
            return item.value
        return 'error'


def test():
    count = int(input().strip())
    queue = MyQueueLinkedList()
    command = []
    while count > 0:
        command = input().strip().split()
        if command[0] == 'put':
            queue.put(int(command[1]))
        if command[0] == 'get':
            print(queue.get())
        if command[0] == 'size':
            print(queue.size())
        count -= 1


if __name__ == '__main__':
    test()
