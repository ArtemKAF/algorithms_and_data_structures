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
        if self.size() != 0:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)


def test():
    staples = input().strip()
    stack = Stack()
    result = True
    for staple in staples:
        if staple == '(' or staple == '[' or staple == '{':
            stack.push(staple)
            continue
        if (
            staple == ')' and stack.peek() == '('
            or staple == ']' and stack.peek() == '['
            or staple == '}' and stack.peek() == '{'
        ):
            stack.pop()
        else:
            result = False
            break
    if stack.size() != 0:
        result = False
    print(result)


if __name__ == '__main__':
    test()
