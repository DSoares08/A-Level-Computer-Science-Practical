class CircularQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if self.front == self.rear + 1:
            return True
        else:
            return False

    def enQueue(self, data):
        self.rear += self.rear
        if self.rear > self.size:
            self.rear = 0
        self.queue.append(data)

    def deQueue(self):
        self.queue.pop(self.front)
        self.front += self.front

    def emptySpaces(self):
        if self.rear > self.front:
            return self.size - self.rear - self.front
        else:
            return self.size - self.front - self.rear

myqueue = CircularQueue(10)
print(myqueue.size)
print(myqueue.isEmpty())
print(myqueue.isFull())
myqueue.enQueue(10)
print(myqueue.queue)
myqueue.enQueue(8)
print(myqueue.queue)
print(myqueue.emptySpaces())
myqueue.deQueue()
print(myqueue.queue)
print(myqueue.emptySpaces())
