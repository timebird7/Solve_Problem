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

TC = int(input())
for tc in range(TC):
    s = input()
    stack = Stack()
    ans = 0
    for c in s:
        if c == '(' or c == '{':
            stack.push(c)
        
        elif c == ')' and stack.peek() == '(':
            stack.pop()

        elif c == '}' and stack.peek() == '{':
            stack.pop()

        elif c == ')' and stack.peek() != '(':
            break

        elif c == '}' and stack.peek() != '{':
            break

    else:
        if stack.isEmpty():
            ans = 1

    print(f'#{tc+1} {ans}')
            
