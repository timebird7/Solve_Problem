class Stack:
    def __init__(self):
        self.stack = [0]*300
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
    forth = input().split()
    stack = Stack()

    for c in forth:
        if c == '+' and stack.pnt >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(b+a)
        elif c == '-' and stack.pnt >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(b-a)
        elif c == '*' and stack.pnt >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(b*a)
        elif c == '/' and stack.pnt >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(b//a)
        elif c == '.':
            if stack.pnt == 1:
                break
            else:
                stack.push('error')
        elif stack.pnt < 2 and (c == '+' or c == '-' or c == '*' or c == '/'):
            stack.push('error')
            break
        else:
            stack.push(int(c))

    print(f'#{tc+1} {stack.peek()}')
