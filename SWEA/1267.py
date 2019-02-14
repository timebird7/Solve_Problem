class Stack:
    def __init__(self):
        self.stack = [0]*V
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
    V, E = list(map(int,input().split())) 
    w = list(map(int,input().split()))
    S = w[-1]
    ways = [0 for i in range(E)]
    for i in range(E):
        a = [w[i*2+1], w[i*2]]
        ways[i] = a
 
    stack = Stack()
    ans = Stack()
    visited = [0 for i in range(V+1)]
 
    visited[S] = 1
    stack.push(S)
 
    while True:        
        for way in ways:
            if way[0] == S and visited[way[1]] == 0:                
                S = way[1]
                stack.push(S)
                visited[S] = 1
                break
        else:
            visited[S] = 1
            ans.push(stack.pop())
            S = stack.peek()
         
        if stack.isEmpty():
            for i in range(1,V+1):
                if visited[i] == 0:
                    S = i
            else:
                stack.push(S)
 
        if ans.pnt == V:
            break
         
    result = ''
    for c in ans.stack:
        result += ' ' + str(c)    
 
    print(f'#{tc+1}{result}')