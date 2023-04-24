LOCAL = True

if LOCAL:
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if self.size() == 0:
                print('error')
            else:
                return self.items.pop()

        def peek(self):
            return self.items[-1]

        def size(self):
            return len(self.items)

        def get_max(self):
            if self.size() == 0:
                return None
            return max(self.items)


def test():
    count = int(input().strip())
    stack = Stack()
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
