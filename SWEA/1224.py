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

for tc in range(10):
    n = input()
    s = input()
    lst = ['(',')','+','*']
    stack = Stack()
    ans = ''

    for c in s:
        if c == '(':
            stack.push(c)
        elif c == ')':
            while stack.peek() != '(':
                ans += stack.pop()
            stack.pop()
        elif c == '+':
            while stack.peek() == '+' or stack.peek() == '*':
                ans += stack.pop()
            else:
                stack.push(c)
        elif c == '*':
            while stack.peek() == '*':
                ans += stack.pop()
            else:
                stack.push(c)
        else:
            ans += c

    while not stack.isEmpty():
        ans += stack.pop()    

    nsum = Stack()

    for c in ans:
        if c == '+':
            x = nsum.pop()
            y = nsum.pop()
            nsum.push(x+y)
        elif c == '*':
            x = nsum.pop()
            y = nsum.pop()
            nsum.push(x*y)
        else:
            nsum.push(int(c))

    print(f'#{tc+1} {nsum.stack[0]}')