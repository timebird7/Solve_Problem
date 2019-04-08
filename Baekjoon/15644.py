from copy import deepcopy
from collections import deque

def findred(rboard):
    global N,M
    for i in range(N):
        for j in range(M):
            if rboard[i][j] == 'R':
                return [i,j]
    return 0

def findblue(rboard):
    global N,M
    for i in range(N):
        for j in range(M):
            if rboard[i][j] == 'B':
                return [i,j]
    return 0

def goup(rboard,rred,rblue):
    global flag
    board = deepcopy(rboard)
    red = deepcopy(rred)
    blue = deepcopy(rblue)
    sflag = 0
    fflag = 0


    if red[1] == blue[1]:
        if red[0] > blue[0]:
            while True:
                if board[blue[0]-1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] -= 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]-1][blue[1]] == '#':
                    break
                elif board[blue[0]-1][blue[1]] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
            while True:
                if board[red[0]-1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] -= 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]-1][red[1]] == '#' or board[red[0]-1][red[1]] == 'B':
                    break
                elif board[red[0]-1][red[1]] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
        else:
            while True:
                if board[red[0]-1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] -= 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]-1][red[1]] == '#':
                    break
                elif board[red[0]-1][red[1]] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
            while True:
                if board[blue[0]-1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] -= 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]-1][blue[1]] == '#' or board[blue[0]-1][blue[1]] == 'R':
                    break
                elif board[blue[0]-1][blue[1]] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
    else:
        while True:
            if board[red[0]-1][red[1]] == '.':
                board[red[0]][red[1]] = '.'
                red[0] -= 1
                board[red[0]][red[1]] = 'R'
            elif board[red[0]-1][red[1]] == '#':
                break
            elif board[red[0]-1][red[1]] == 'O':
                board[red[0]][red[1]] = '.'
                sflag = 1
                break
        while True:
            if board[blue[0]-1][blue[1]] == '.':
                board[blue[0]][blue[1]] = '.'
                blue[0] -= 1
                board[blue[0]][blue[1]] = 'B'
            elif board[blue[0]-1][blue[1]] == '#':
                break
            elif board[blue[0]-1][blue[1]] == 'O':
                board[blue[0]][blue[1]] = '.'
                fflag = 1
                break

    if (fflag, sflag) == (0,0):
        return board
    elif (fflag, sflag) == (0,1):
        flag = 1
        return board
    elif (fflag, sflag) == (1,0):
        return rboard
    elif (fflag, sflag) == (1,1):
        return rboard

def godown(rboard,rred,rblue):
    global flag
    board = deepcopy(rboard)
    red = deepcopy(rred)
    blue = deepcopy(rblue)
    sflag = 0
    fflag = 0

    if red[1] == blue[1]:
        if red[0] < blue[0]:
            while True:
                if board[blue[0]+1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] += 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]+1][blue[1]] == '#':
                    break
                elif board[blue[0]+1][blue[1]] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
            while True:
                if board[red[0]+1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] += 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]+1][red[1]] == '#' or board[red[0]+1][red[1]] == 'B':
                    break
                elif board[red[0]+1][red[1]] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
        else:
            while True:
                if board[red[0]+1][red[1]] == '.':
                    board[red[0]][red[1]] = '.'
                    red[0] += 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]+1][red[1]] == '#':
                    break
                elif board[red[0]+1][red[1]] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
            while True:
                if board[blue[0]+1][blue[1]] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[0] += 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]+1][blue[1]] == '#' or board[blue[0]+1][blue[1]] == 'R':
                    break
                elif board[blue[0]+1][blue[1]] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
    else:
        while True:
            if board[red[0]+1][red[1]] == '.':
                board[red[0]][red[1]] = '.'
                red[0] += 1
                board[red[0]][red[1]] = 'R'
            elif board[red[0]+1][red[1]] == '#':
                break
            elif board[red[0]+1][red[1]] == 'O':
                board[red[0]][red[1]] = '.'
                sflag = 1
                break
        while True:
            if board[blue[0]+1][blue[1]] == '.':
                board[blue[0]][blue[1]] = '.'
                blue[0] += 1
                board[blue[0]][blue[1]] = 'B'
            elif board[blue[0]+1][blue[1]] == '#':
                break
            elif board[blue[0]+1][blue[1]] == 'O':
                board[blue[0]][blue[1]] = '.'
                fflag = 1
                break

    if (fflag, sflag) == (0,0):
        return board
    elif (fflag, sflag) == (0,1):
        flag = 1
        return board
    elif (fflag, sflag) == (1,0):
        return rboard
    elif (fflag, sflag) == (1,1):
        return rboard

def goleft(rboard,rred,rblue):
    global flag
    board = deepcopy(rboard)
    red = deepcopy(rred)
    blue = deepcopy(rblue)
    sflag = 0
    fflag = 0

    if red[0] == blue[0]:
        if red[1] > blue[1]:
            while True:
                if board[blue[0]][blue[1]-1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] -= 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]][blue[1]-1] == '#':
                    break
                elif board[blue[0]][blue[1]-1] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
            while True:
                if board[red[0]][red[1]-1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] -= 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]][red[1]-1] == '#' or board[red[0]][red[1]-1] == 'B':
                    break
                elif board[red[0]][red[1]-1] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
        else:
            while True:
                if board[red[0]][red[1]-1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] -= 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]][red[1]-1] == '#':
                    break
                elif board[red[0]][red[1]-1] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
            while True:
                if board[blue[0]][blue[1]-1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] -= 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]][blue[1]-1] == '#' or board[blue[0]][blue[1]-1] == 'R':
                    break
                elif board[blue[0]][blue[1]-1] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
    else:
        while True:
            if board[red[0]][red[1]-1] == '.':
                board[red[0]][red[1]] = '.'
                red[1] -= 1
                board[red[0]][red[1]] = 'R'
            elif board[red[0]][red[1]-1] == '#':
                break
            elif board[red[0]][red[1]-1] == 'O':
                board[red[0]][red[1]] = '.'
                sflag = 1
                break
        while True:
            if board[blue[0]][blue[1]-1] == '.':
                board[blue[0]][blue[1]] = '.'
                blue[1] -= 1
                board[blue[0]][blue[1]] = 'B'
            elif board[blue[0]][blue[1]-1] == '#':
                break
            elif board[blue[0]][blue[1]-1] == 'O':
                board[blue[0]][blue[1]] = '.'
                fflag = 1
                break

    if (fflag, sflag) == (0,0):
        return board
    elif (fflag, sflag) == (0,1):
        flag = 1
        return board
    elif (fflag, sflag) == (1,0):
        return rboard
    elif (fflag, sflag) == (1,1):
        return rboard

def goright(rboard,rred,rblue):
    global flag
    board = deepcopy(rboard)
    red = deepcopy(rred)
    blue = deepcopy(rblue)
    sflag = 0
    fflag = 0

    if red[0] == blue[0]:
        if red[1] < blue[1]:
            while True:
                if board[blue[0]][blue[1]+1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] += 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]][blue[1]+1] == '#':
                    break
                elif board[blue[0]][blue[1]+1] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
            while True:
                if board[red[0]][red[1]+1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] += 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]][red[1]+1] == '#' or board[red[0]][red[1]+1] == 'B':
                    break
                elif board[red[0]][red[1]+1] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
        else:
            while True:
                if board[red[0]][red[1]+1] == '.':
                    board[red[0]][red[1]] = '.'
                    red[1] += 1
                    board[red[0]][red[1]] = 'R'
                elif board[red[0]][red[1]+1] == '#':
                    break
                elif board[red[0]][red[1]+1] == 'O':
                    board[red[0]][red[1]] = '.'
                    sflag = 1
                    break
            while True:
                if board[blue[0]][blue[1]+1] == '.':
                    board[blue[0]][blue[1]] = '.'
                    blue[1] += 1
                    board[blue[0]][blue[1]] = 'B'
                elif board[blue[0]][blue[1]+1] == '#' or board[blue[0]][blue[1]+1] == 'R':
                    break
                elif board[blue[0]][blue[1]+1] == 'O':
                    board[blue[0]][blue[1]] = '.'
                    fflag = 1
                    break
    else:
        while True:
            if board[red[0]][red[1]+1] == '.':
                board[red[0]][red[1]] = '.'
                red[1] += 1
                board[red[0]][red[1]] = 'R'
            elif board[red[0]][red[1]+1] == '#':
                break
            elif board[red[0]][red[1]+1] == 'O':
                board[red[0]][red[1]] = '.'
                sflag = 1
                break
        while True:
            if board[blue[0]][blue[1]+1] == '.':
                board[blue[0]][blue[1]] = '.'
                blue[1] += 1
                board[blue[0]][blue[1]] = 'B'
            elif board[blue[0]][blue[1]+1] == '#':
                break
            elif board[blue[0]][blue[1]+1] == 'O':
                board[blue[0]][blue[1]] = '.'
                fflag = 1
                break

    if (fflag, sflag) == (0,0):
        return board
    elif (fflag, sflag) == (0,1):
        flag = 1
        return board
    elif (fflag, sflag) == (1,0):
        return rboard
    elif (fflag, sflag) == (1,1):
        return rboard

N, M = map(int,input().split())

rboard = [0]*N
for n in range(N):
    rboard[n] = list(input())

queue = deque([[rboard,'']])
cnt = 0
history = deque([rboard])
ans = ''

while True:
    cnt += 1
    tmp = deque([])
    flag = 0
    for q in queue:
        rred = findred(q[0])
        rblue = findblue(q[0])
        if rred == 0 or rblue == 0:
            continue
        rup = goup(q[0],rred,rblue)
        if rup not in history:
            tmp.append([rup,'%s%s'%(q[1],'U')])  
            history.append(rup)   
        rdown = godown(q[0],rred,rblue)
        if rdown not in history:
            tmp.append([rdown,'%s%s'%(q[1],'D')])    
            history.append(rdown)    
        rleft = goleft(q[0],rred,rblue)
        if rleft not in history:
            tmp.append([rleft,'%s%s'%(q[1],'L')])    
            history.append(rleft)     
        rright = goright(q[0],rred,rblue)
        if rright not in history:
            tmp.append([rright,'%s%s'%(q[1],'R')])   
            history.append(rright)   

    queue = deepcopy(tmp)
    

    if flag:
        for q in queue:
            rred = findred(q[0])
            rblue = findblue(q[0])
            if rred == 0 and rblue:
                ans = q[1]
                break
        break

    if not queue:
        cnt = -1
        break

    if cnt >= 10:
        cnt = -1
        break

print(cnt)
print(ans)