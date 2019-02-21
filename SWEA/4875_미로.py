class Stack:
    def __init__(self):
        self.stack = [0]*10000
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

TC = int(input())

for tc in range(TC):
    N = int(input())
    nums = [0 for i in range(N)]
    visited = [[0 for i in range(N)] for i in range(N)]
    flag = 0
    eflag = 0

    for i in range(N):
        nums[i] = list(map(int,list(input())))

    start = findtwo(nums)
    stack = Stack()

    while True:       
        if start[1] > 0 and (nums[start[0]][start[1]-1] != 1 and visited[start[0]][start[1]-1] == 0):
            visited[start[0]][start[1]] = 1
            stack.push(start)
            start = [start[0],start[1]-1]
            
            if nums[start[0]][start[1]] == 3:
                flag = 1

        elif start[0] > 0 and (nums[start[0]-1][start[1]] != 1 and visited[start[0]-1][start[1]] == 0):
            visited[start[0]][start[1]] = 1
            stack.push(start)
            start = [start[0]-1,start[1]]
            
            if nums[start[0]][start[1]] == 3:
                flag = 1

        elif start[0] < N-1 and (nums[start[0]+1][start[1]] != 1 and visited[start[0]+1][start[1]] == 0):
            visited[start[0]][start[1]] = 1
            stack.push(start)
            start = [start[0]+1,start[1]]
            
            
            if nums[start[0]][start[1]] == 3:
                flag = 1

        elif start[1] < N-1 and (nums[start[0]][start[1]+1] != 1 and visited[start[0]][start[1]+1] == 0):
            visited[start[0]][start[1]] = 1
            stack.push(start)
            start = [start[0],start[1]+1]
            
            if nums[start[0]][start[1]] == 3:
                flag = 1

        else:
            if stack.isEmpty():
                eflag = 1
            visited[start[0]][start[1]] = 1
            start = stack.pop()

        if flag:
            break
        
        if eflag:
            break        

    print(f'#{tc+1} {flag}')
