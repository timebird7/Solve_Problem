import sys

def cango(i,j,d):
    global nums
    if i<0 or i>N-1 or j<0 or j>N-1:
        return False

    if nums[i][j]:
        return False

    if d == 2:
        if nums[i-1][j] or nums[i][j-1]:
            return False

    return True

N = int(sys.stdin.readline())

nums = [0]*N
for n in range(N):
    nums[n] = list(map(int,sys.stdin.readline().split()))

result = [[[0 for j in range(3)] for k in range(N)] for n in range(N)]
result[0][1][0] = 1

for i in range(N):
    for j in range(N):
        x,y = i,j
        if result[x][y][0]: 
            if cango(x,y+1,0):
                result[x][y+1][0] += result[x][y][0]
            if cango(x+1,y+1,2):
                result[x+1][y+1][2] += result[x][y][0]
        if result[x][y][1]: 
            if cango(x+1,y,1):
                result[x+1][y][1] += result[x][y][1]
            if cango(x+1,y+1,2):
                result[x+1][y+1][2] += result[x][y][1]
        if result[x][y][2]: 
            if cango(x,y+1,0):
                result[x][y+1][0] += result[x][y][2]
            if cango(x+1,y,1):
                result[x+1][y][1] += result[x][y][2]
            if cango(x+1,y+1,2):
                result[x+1][y+1][2] += result[x][y][2]
print(sum(result[N-1][N-1]))