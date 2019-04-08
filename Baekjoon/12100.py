from copy import deepcopy

def push(nums,S):
    global N
    if S == 0:
        for i in range(N):
            for j in range(N):
                x = i
                y = j
                while x>0:  
                    if nums[x-1][y] == 0:
                        nums[x-1][y] = nums[x][y]
                        nums[x][y] = 0
                        x -= 1
                        continue
                    elif nums[x-1][y] == nums[x][y]:
                        nums[x-1][y] = nums[x][y]*2
                        nums[x-1][y] = str(nums[x-1][y])
                        nums[x][y] = 0
                        x -= 1
                        break    
                    break

                while x>0:  
                    if nums[x-1][y] == 0:
                        nums[x-1][y] = nums[x][y]
                        nums[x][y] = 0
                        x -= 1
                        continue
                    break
 
    if S == 1:
        for i in range(N-1,-1,-1):
            for j in range(N):
                x = i
                y = j
                while x<N-1:  
                    if nums[x+1][y] == 0:
                        nums[x+1][y] = nums[x][y]
                        nums[x][y] = 0
                        x += 1
                        continue
                    elif nums[x+1][y] == nums[x][y]:
                        nums[x+1][y] = nums[x][y]*2
                        nums[x+1][y] = str(nums[x+1][y])
                        nums[x][y] = 0
                        x += 1
                        break    
                    break

                while x<N-1:  
                    if nums[x+1][y] == 0:
                        nums[x+1][y] = nums[x][y]
                        nums[x][y] = 0
                        x += 1
                        continue
                    break
 
    if S == 2:
        for i in range(N):
            for j in range(N):
                x = i
                y = j
                while y>0:  
                    if nums[x][y-1] == 0:
                        nums[x][y-1] = nums[x][y]
                        nums[x][y] = 0
                        y -= 1
                        continue
                    elif nums[x][y-1] == nums[x][y]:
                        nums[x][y-1] = nums[x][y]*2
                        nums[x][y-1] = str(nums[x][y-1])
                        nums[x][y] = 0
                        y -= 1
                        break    
                    break

                while y>0:  
                    if nums[x][y-1] == 0:
                        nums[x][y-1] = nums[x][y]
                        nums[x][y] = 0
                        y -= 1
                        continue
                    break
 
    if S == 3:
        for i in range(N):
            for j in range(N-1,-1,-1):
                x = i
                y = j
                while y<N-1:  
                    if nums[x][y+1] == 0:
                        nums[x][y+1] = nums[x][y]
                        nums[x][y] = 0
                        y += 1
                        continue
                    elif nums[x][y+1] == nums[x][y]:
                        nums[x][y+1] = nums[x][y]*2
                        nums[x][y+1] = str(nums[x][y+1])
                        nums[x][y] = 0
                        y += 1
                        break    
                    break

                while y<N-1:  
                    if nums[x][y+1] == 0:
                        nums[x][y+1] = nums[x][y]
                        nums[x][y] = 0
                        y += 1
                        continue
                    break

    return nums

def perm_re(cnt):
    global visited
    if cnt == 5:
        perms.append(perm[:5])
        return
    perm[cnt] = 0
    visited[0] += 1
    perm_re(cnt+1)
    visited[0] -= 1
    perm[cnt] = 1
    visited[1] += 1
    perm_re(cnt+1)
    visited[1] -= 1    
    perm[cnt] = 2
    visited[2] += 1
    perm_re(cnt+1)
    visited[2] -= 1    
    perm[cnt] = 3
    visited[3] += 1
    perm_re(cnt+1)
    visited[3] -= 1

N = int(input())

nums = [0]*N
for n in range(N):
    nums[n] = list(map(int,input().split()))

perms = []
visited = [0,0,0,0]
perm = [0] * 10
perm_re(0)

result = 0

for p in perms:
    tmpnums = deepcopy(nums)
    tmpnums = push(tmpnums,p[0])
    for n in range(N):
        tmpnums[n] = list(map(int,tmpnums[n]))
        
    tmpnums = push(tmpnums,p[1])
    for n in range(N):
        tmpnums[n] = list(map(int,tmpnums[n]))
        
    tmpnums = push(tmpnums,p[2])
    for n in range(N):
        tmpnums[n] = list(map(int,tmpnums[n]))
        
    tmpnums = push(tmpnums,p[3])
    for n in range(N):
        tmpnums[n] = list(map(int,tmpnums[n]))
        
    tmpnums = push(tmpnums,p[4])
    for n in range(N):
        tmpnums[n] = list(map(int,tmpnums[n]))

    for i in range(N):
        for j in range(N):
            result = max(result,tmpnums[i][j])

print(result)