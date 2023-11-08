class Stack2:
    def __init__(self):
        self.top = None
        self.elements = []
        self.size = 0

    def push(self, data):
        self.elements.append(data)
        self.size += 1
        self.top = self.elements[self.size - 1]

    def printStack(self):
        if self.top:
            print(self.elements)
        else:
            print("Stack is Empty")

    def peekStack(self):
        if self.top:
            print(self.elements)
    def bracket_matching(self)
        
