class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, maxSize):
        self.top = None
        self.size = 0
        self.maxSize = maxSize

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
            self.size += 1
        else:
            self.top = node
            self.size += 1

    def pop(self):
        if self.top == None:
            return -1
        else:
            node = self.top
            self.top = node.next
            self.size = -1
            return node.data

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.size == self.maxSize:
            return True
        else:
            return False


stack = Stack(10)
stack.push("Hello")
print(stack.pop())
