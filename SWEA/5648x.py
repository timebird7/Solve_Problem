from copy import deepcopy


nd = {
    0 : (0,1),
    1 : (0,-1),
    2 : (-1,0),
    3 : (1,0)
}

def cango(i,j):
    global minx,maxx,miny,maxy
    if i<minx or i>maxx or j<miny or j>maxy:
        return False
    return True

def move(dot):
    x = dot[0]
    y = dot[1]
    dx, dy = nd.get(dot[2])
    nx = x+dx
    ny = y+dy

    if cango(nx,ny):
        return [nx,ny,dot[2],dot[3]]
    else:
        return 0

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    result = 0
    dots = []
    maxx = -2001
    minx = 2001
    maxy = -2001
    miny = 2001

    for n in range(N):
        dot = list(map(int,input().split()))
        dot[0] *= 2
        dot[1] *= 2
        maxx = max(maxx,dot[0])
        minx = min(minx,dot[0])
        maxy = max(maxy,dot[1])
        miny = min(miny,dot[1])
        dots.append(dot)

    while True:        
        tmp = []
        deltmp = []
        tmpdict = {}
        for dot in dots:
            ndot = move(dot)
            if not ndot:
                continue
            if tmpdict.get((ndot[0],ndot[1])):
                tmpdict[(ndot[0],ndot[1])].append(ndot[3])
            else:
                tmpdict[(ndot[0],ndot[1])] = [ndot[3]]
                tmp.append(ndot)

        for key,value in tmpdict.items():
            if len(value) > 1:
                deltmp.append(key)
                result += sum(value)

        dots = []
        if deltmp:            
            for t in tmp:
                if (t[0],t[1]) not in deltmp:
                    dots.append(deepcopy(t))
        else:
            dots = deepcopy(tmp)

        if not dots:
            break

    print(f'#{tc} {result}')

        

