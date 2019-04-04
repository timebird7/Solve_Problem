import copy

def cango(x,y,d):
    global N,M,nums,possible
    if (x,y) in possible:
        return False    
    if x<0 or x>=N or y<0 or y>=M:
        return False
    elif nums[x][y] == 0:
        return False

    if d == 0:
        if nums[x][y] in (3,4,7):
            return False
    elif d == 1:
        if nums[x][y] in (3,5,6):
            return False
    elif d == 2:
        if nums[x][y] in (2,6,7):
            return False
    elif d == 3:
        if nums[x][y] in (2,4,5):
            return False    

    return True

TC = int(input())

for tc in range(1,TC+1):
    N, M, R, C, L = map(int, input().split())
    nums = [0] * N
    
    for n in range(N):
        nums[n] = list(map(int, input().split()))

    starts = set()
    starts.add((R,C))
    t = 1
    possible = set()
    possible.add((R,C))

    while True:
        t += 1
        tmp = set()
        for start in starts:
            x, y = start
            if nums[x][y] == 1:
                if cango(x,y+1,3):
                    tmp.add((x,y+1))
                if cango(x,y-1,2):
                    tmp.add((x,y-1))
                if cango(x+1,y,1):
                    tmp.add((x+1,y))
                if cango(x-1,y,0):
                    tmp.add((x-1,y))
            elif nums[x][y] == 2:
                if cango(x-1,y,0):
                    tmp.add((x-1,y))
                if cango(x+1,y,1):
                    tmp.add((x+1,y))
            elif nums[x][y] == 3:
                if cango(x,y-1,2):
                    tmp.add((x,y-1))
                if cango(x,y+1,3):
                    tmp.add((x,y+1))
            elif nums[x][y] == 4:
                if cango(x-1,y,0):
                    tmp.add((x-1,y))
                if cango(x,y+1,3):
                    tmp.add((x,y+1))
            elif nums[x][y] == 5:
                if cango(x+1,y,1):
                    tmp.add((x+1,y))
                if cango(x,y+1,3):
                    tmp.add((x,y+1))
            elif nums[x][y] == 6:
                if cango(x,y-1,2):
                    tmp.add((x,y-1))
                if cango(x+1,y,1):
                    tmp.add((x+1,y))
            elif nums[x][y] == 7:
                if cango(x-1,y,0):
                    tmp.add((x-1,y))
                if cango(x,y-1,2):
                    tmp.add((x,y-1))

        starts = copy.copy(tmp)
        possible = possible.union(tmp)

        if t == L:
            break
        if not starts:
            break

    print(f'#{tc} {len(possible)}')
