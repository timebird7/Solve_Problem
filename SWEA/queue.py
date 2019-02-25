class Queue:
    def __init__(self):
        self.queue = [0]*50
        self.front = 0
        self.rear = 0

    def enQueue(self, x):
        self.queue[self.rear] = x
        self.rear += 1

    def deQueue(self):
        if self.front == self.rear:
            return None
        else:
            self.front += 1
            return self.queue[self.front-1]

    def isEmpty(self):
        return self.front == self.rear

    def Qpeek(self):
        if self.front == self.rear:
            return None
        else:
            return self.queue[self.front]
