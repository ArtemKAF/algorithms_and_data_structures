class MyQueueSyzed:
    def __init__(self, queue_size=10):
        self.items = [None] * queue_size
        self.queue_size = 0
        self.head = 0
        self.tail = 0

    def size(self):
        return self.queue_size

    def peek(self):
        return self.items[self.head]

    def push(self, item):
        if self.queue_size < len(self.items):
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % len(self.items)
            self.queue_size += 1
        else:
            print('error')

    def pop(self):
        if self.queue_size > 0:
            item = self.items[self.head]
            self.items[self.head] = None
            self.head = (self.head + 1) % len(self.items)
            self.queue_size -= 1
            return item
        return None


def test():
    count = int(input().strip())
    size = int(input().strip())
    queue = MyQueueSyzed(size)
    command = []
    while count > 0:
        command = input().strip().split()
        if command[0] == 'push':
            queue.push(int(command[1]))
        if command[0] == 'pop':
            print(queue.pop())
        if command[0] == 'peek':
            print(queue.peek())
        if command[0] == 'size':
            print(queue.size())
        count -= 1


if __name__ == '__main__':
    test()
