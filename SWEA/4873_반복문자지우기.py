class Stack:
    def __init__(self):
        self.stack = [0]*1000
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

TC = int(input())

for tc in range(TC):
    s = input()
    result = Stack()
    for c in s:
        if c == result.peek():
            result.pop()
        else:
            result.push(c)

    print(f'#{tc+1} {result.pnt}')