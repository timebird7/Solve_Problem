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

def pinball(x,y,direction,score,endpoint):
    global nums,scores
    nx = x+dx[direction]
    ny = y+dy[direction]

    if [nx,ny] in endpoint:
        scores.append(score)
        return
    else:
        if iswall(nx,ny):
            if direction == 0:
                nd = 1
            elif direction == 1:
                nd = 0
            elif direction == 2:
                nd = 3
            elif direction == 3:
                nd = 2
            pinball(nx,ny,nd,score+1,endpoint)            

        elif go_back(nx,ny,direction):
            if direction == 0:
                nd = 1
            elif direction == 1:
                nd = 0
            elif direction == 2:
                nd = 3
            elif direction == 3:
                nd = 2
            pinball(nx,ny,nd,score+1,endpoint)    

        elif nums[nx][ny] == 0:
            pinball(nx,ny,direction,score,endpoint) 

        elif nums[nx][ny] == -1:
            pinball(nx,ny,direction,score,endpoint)   

        elif go_left(nx,ny,direction):
            if direction == 0:
                nd = 2
            elif direction == 1:
                nd = 3
            elif direction == 2:
                nd = 1
            elif direction == 3:
                nd = 0
            pinball(nx,ny,nd,score+1,endpoint)

        elif go_right(nx,ny,direction):
            if direction == 0:
                nd = 3
            elif direction == 1:
                nd = 2
            elif direction == 2:
                nd = 0
            elif direction == 3:
                nd = 1
            pinball(nx,ny,nd,score+1,endpoint)

        elif wormhole(nx,ny,direction):
            worm_val = nums[nx][ny]
            for i in range(N):
                for j in range(N):
                    if nums[i][j] == worm_val and (i,j) != (nx,ny):
                        pinball(i,j,direction,score,endpoint)

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
                pinball(i,j,0,0,endpoint)
                pinball(i,j,1,0,endpoint)
                pinball(i,j,2,0,endpoint)
                pinball(i,j,3,0,endpoint)

    print(f'#{tc} {max(scores)}')