class Stack:
    def __init__(self):
        self.stack = [0]*50
        self.pnt = 0

    def push(self, x):
        self.stack[self.pnt] = x
        self.pnt += 1

    def pop(self):
        if self.pnt == 0:
            return None
        else:
            self.pnt -= 1
            return self.stack[self.pnt]
    
    def isEmpty(self):
        return self.pnt == 0

    def peek(self):
        if self.pnt == 0:
            return None
        else:
            return self.stack[self.pnt-1]