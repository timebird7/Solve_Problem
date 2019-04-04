dy = [0,0,-1,1]
dx = [-1,1,0,0]

def iswall(x,y):
    global N
    if x<0 or x>=N or y<0 or y>=N:
        return True
    else:
        return False

def go_back(x,y,direction):
    global nums
    if iswall(x,y):
        return True
    elif direction == 0 and nums[x][y] in (1,4,5):
        return True
    elif direction == 1 and nums[x][y] in (2,3,5):
        return True
    elif direction == 2 and nums[x][y] in (3,4,5):
        return True
    elif direction == 3 and nums[x][y] in (1,2,5):
        return True
    else:
        return False

def go_left(x,y,direction):
    global nums
    if direction == 0 and nums[x][y] == 3:
        return True
    elif direction == 1 and nums[x][y] == 1:
        return True
    elif direction == 2 and nums[x][y] == 2:
        return True
    elif direction == 3 and nums[x][y] == 4:
        return True
    else:
        return False    

def go_right(x,y,direction):
    global nums
    if direction == 0 and nums[x][y] == 2:
        return True
    elif direction == 1 and nums[x][y] == 4:
        return True
    elif direction == 2 and nums[x][y] == 1:
        return True
    elif direction == 3 and nums[x][y] == 3:
        return True
    else:
        return False

def wormhole(x,y,direction):
    global nums
    if 6<=nums[x][y]<=10:
        return True
    else:
        return False

def go_worm(x,y):
    global nums
    worm_val = nums[x][y]
    for i in range(N):
        for j in range(N):
            if nums[i][j] == worm_val and (i,j) != (x,y):
                return (i, j)

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nums = [0] * N

    for n in range(N):
        nums[n] = list(map(int,input().split()))

    blackhole = []
    scores = []

    for i in range(N):
        for j in range(N):
            if nums[i][j] == -1:
                blackhole.append([i,j])

    for i in range(N):
        for j in range(N):
            if nums[i][j] == 0:
                endpoint = blackhole[:]                
                endpoint.append([i,j])
                            
                for k in range(4):
                    x = i
                    y = j    
                    direction = k
                    score = 0
                    while True:
                        nx = x+dx[direction]
                        ny = y+dy[direction]

                        if [nx,ny] in endpoint:
                            scores.append(score)
                            break

                        else:
                            if iswall(nx,ny):
                                if direction == 0:
                                    direction = 1
                                elif direction == 1:
                                    direction = 0
                                elif direction == 2:
                                    direction = 3
                                elif direction == 3:
                                    direction = 2
                                score += 1
                                x = nx
                                y = ny
                                continue

                            elif go_back(nx,ny,direction):
                                if direction == 0:
                                    direction = 1
                                elif direction == 1:
                                    direction = 0
                                elif direction == 2:
                                    direction = 3
                                elif direction == 3:
                                    direction = 2
                                score += 1 
                                x = nx
                                y = ny
                                continue

                            elif nums[nx][ny] == 0:
                                x = nx
                                y = ny
                                continue 

                            elif go_left(nx,ny,direction):
                                if direction == 0:
                                    direction = 2
                                elif direction == 1:
                                    direction = 3
                                elif direction == 2:
                                    direction = 1
                                elif direction == 3:
                                    direction = 0
                                score += 1 
                                x = nx
                                y = ny
                                continue

                            elif go_right(nx,ny,direction):
                                if direction == 0:
                                    direction = 3
                                elif direction == 1:
                                    direction = 2
                                elif direction == 2:
                                    direction = 0
                                elif direction == 3:
                                    direction = 1
                                score += 1 
                                x = nx
                                y = ny
                                continue

                            elif wormhole(nx,ny,direction):
                                x,y = go_worm(nx,ny)

                                continue

    print(f'#{tc} {max(scores)}')