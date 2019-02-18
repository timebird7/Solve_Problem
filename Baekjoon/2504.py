class Stack:
    def __init__(self):
        self.stack = [0]*30
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

words = input()
stack_ = Stack()
ans = 0
for c in words:
    if c == '(' or c == '[':
        stack_.push(c)
    
    elif c == ')' and stack_.peek() == '(':
        stack_.pop()

    elif c == ']' and stack_.peek() == '[':
        stack_.pop()

    elif c == ')' and stack_.peek() != '(':
        break

    elif c == ']' and stack_.peek() != '[':
        break

else:
    if stack_.isEmpty():
        ans = 1

if ans == 0:
    print(0)
elif ans and words == '[]':
    print(3)
elif ans and words == '()':
    print(2)
else:        
    lst = ['(','[',')',']']
    stack = Stack()
    words = words.replace('()', '2')
    words = words.replace('[]', '3')

    for c in words:
        if c not in lst:
            if stack.pnt > 0 and stack.peek() not in lst:
                stack.push(int(c) + stack.pop())
            else:
                stack.push(int(c))

        elif c in lst[0:2]:
            stack.push(c)

        elif c == lst[2]:
            n = 0
            while stack.peek() not in lst:
                n += stack.pop()
            stack.pop()

            if stack.pnt > 0 and stack.peek() not in lst:
                stack.push(2*n + stack.pop())
            else:
                stack.push(2*n)            
            
        elif c == lst[3]:
            n = 0
            while stack.peek() not in lst:
                n += stack.pop()
            stack.pop()

            if stack.pnt > 0 and stack.peek() not in lst:
                stack.push(3*n + stack.pop())
            else:
                stack.push(3*n)

    print(stack.stack[0])

