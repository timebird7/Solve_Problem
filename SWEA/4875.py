class list(list):
    def get(self, i):
        if i >= 0:
            try:
                return self[i]
            except IndexError:
                return 0
        else:
            return 0

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

def findtwo(nums):
    for i in range(N):
        for j in range(N):
            if nums[i][j] == 2:
                return [i, j]

def findthree(nums):
    for i in range(N):
        for j in range(N):
            if nums[i][j] == 3:
                return [i, j]

TC = int(input())

for tc in range(TC):
    N = int(input())
    nums = [0 for i in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        nums[i] = list(map(int,list(input())))

    start = findtwo(nums)
    end = findthree(nums)

    stack = Stack()

    visited[start[0]][start[1]] = 1
    stack.push(start)

    while True:
        for way in ways:
            if way[0] == S and visited[way[1]] == 0:                
                S = way[1]
                stack.push(S)
                visited[S] = 1
                break
        else:
            stack.pop()
            S = stack.peek() 

    