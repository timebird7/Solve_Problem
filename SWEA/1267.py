class Stack:
    def __init__(self):
        self.stack = [0]*V
        self.pnt = 0
   
    def push(self, x):
        self.stack[self.pnt] = x
        self.pnt += 1
   
    def pop(self):        
        self.pnt -= 1
        return self.stack[self.pnt]
   
    def peek(self):        
        return self.stack[self.pnt-1]
   
for tc in range(10):
    V, E = list(map(int,input().split())) 
    w = list(map(int,input().split()))
    S = w[-1]    
   
    stack = Stack()
    ans = Stack()
    visited = [0 for i in range(V+1)]
   
    visited[S] = 1
    stack.push(S)
   
    while True:        
        for i in range(E):
            a, b = w[i*2+1], w[i*2]
            if a == S and visited[b] == 0:                
                S = b
                stack.push(S)
                visited[S] = 1
                break
        else:
            visited[S] = 1
            ans.push(stack.pop())
            S = stack.peek()
           
        if stack.pnt == 0:
            for i in range(1,V+1):
                if visited[i] == 0:
                    S = i
            else:
                stack.push(S)
   
        if ans.pnt == V:
            break
           
    r = ''
    for c in ans.stack:
        r += ' ' + str(c)    
   
    print(f'#{tc+1}{r}')