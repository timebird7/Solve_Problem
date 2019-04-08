from itertools import combinations
from collections import deque
from copy import deepcopy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def iswall(i,j):
    global N,M
    if i<0 or i>N-1 or j<0 or j>M-1:
        return True
    return False

def spread(tmproom,x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if not iswall(nx,ny):
            if tmproom[nx][ny] == 0:
                tmproom[nx][ny] = 2
                spread(tmproom,nx,ny)

N, M = map(int,input().split())
nums = [0]*N
for n in range(N):
    nums[n] = list(map(int,input().split()))

cands = deque([])
twos = deque([])
cnt = 0
ans = 0

for i in range(N):
    for j in range(M):
        if nums[i][j] == 0:
            cands.append((i,j))
        elif nums[i][j] == 2:
            twos.append((i,j))

walls = combinations(cands,3)

for wall in walls:
    tmp = deepcopy(nums)
    cnt = 0
    flag = 0
    tmp[wall[0][0]][wall[0][1]] = 1
    tmp[wall[1][0]][wall[1][1]] = 1
    tmp[wall[2][0]][wall[2][1]] = 1

    for two in twos:
        spread(tmp,two[0],two[1])

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1

    ans = max(cnt, ans)

print(ans)
