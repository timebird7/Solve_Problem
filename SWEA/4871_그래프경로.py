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
    V, E = list(map(int,input().split())) 
    ways = []
    for e in range(E):
        ways.append(list(map(int, input().split())))

    stack = Stack()
    ans = 0
    visited = [0 for i in range(V)]

    S, G = list(map(int,input().split()))
    visited[S-1] = 1
    stack.push(S)

    while True:        
        for way in ways:
            if way[0] == S and visited[way[1]-1] == 0:                
                S = way[1]
                stack.push(S)
                visited[S-1] = 1
                break
        else:
            stack.pop()
            S = stack.peek()  

        if stack.peek() == G:
            ans = 1
            break
        elif stack.isEmpty():
            ans = 0
            break

    print(f'#{tc+1} {ans}')