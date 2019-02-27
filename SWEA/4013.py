def rot(i,j):
    global m
    lflag = 0
    rflag = 0    
    
    if i == 1:
        if m[i][2] != m[i+1][-2]:
            rflag = 1
            if m[i+1][2] != m[i+2][-2]:
                rflag = 2
                if m[i+2][2] != m[i+3][-2]:
                    rflag = 3

    if i == 2:
        if m[i][-2] != m[i-1][2]:
            lflag = 1
        if m[i][2] != m[i+1][-2]:
            rflag = 1
            if m[i+1][2] != m[i+2][-2]:
                rflag = 2
    
    if i == 3:
        if m[i][-2] != m[i-1][2]:
            lflag = 1
            if m[i-1][-2] != m[i-2][2]:
                lflag = 2
        if m[i][2] != m[i+1][-2]:
            rflag = 1

    if i == 4:
        if m[i][-2] != m[i-1][2]:
            lflag = 1
            if m[i-1][-2] != m[i-2][2]:
                lflag = 2
                if m[i-2][-2] != m[i-3][2]:
                    lflag = 3

    if j == 1:
        m[i] = [m[i][7]] + m[i][:7]
        if lflag >= 1:
            m[i-1] = m[i-1][1:] + [m[i-1][0]]
            if lflag >= 2:
                m[i-2] = [m[i-2][7]] + m[i-2][:7]
                if lflag == 3:
                    m[i-3] = m[i-3][1:] + [m[i-3][0]]
        if rflag >= 1:
            m[i+1] = m[i+1][1:] + [m[i+1][0]]
            if rflag >= 2:
                m[i+2] = [m[i+2][7]] + m[i+2][:7]
                if rflag == 3:
                    m[i+3] = m[i+3][1:] + [m[i+3][0]]
    
    elif j == -1:
        m[i] = m[i][1:] + [m[i][0]]
        if lflag >= 1:
            m[i-1] = [m[i-1][7]] + m[i-1][:7]
            if lflag >= 2:
                m[i-2] = m[i-2][1:] + [m[i-2][0]]
                if lflag == 3:
                    m[i-3] = [m[i-3][7]] + m[i-3][:7]
        if rflag >= 1:
            m[i+1] = [m[i+1][7]] + m[i+1][:7]
            if rflag >= 2:
                m[i+2] = m[i+2][1:] + [m[i+2][0]]
                if rflag == 3:
                    m[i+3] = [m[i+3][7]] + m[i+3][:7]      

TC = int(input())

for tc in range(TC):
    K = int(input())
    m = [0,0,0,0,0]
    m[1] = list(map(int,input().split()))
    m[2] = list(map(int,input().split()))
    m[3] = list(map(int,input().split()))
    m[4] = list(map(int,input().split()))
    ans = 0

    for k in range(K):
        i, j = list(map(int,input().split()))
        rot(i,j)

    if m[1][0]:
        ans += 1
    if m[2][0]:
        ans += 2
    if m[3][0]:
        ans += 4
    if m[4][0]:
        ans += 8


    print(f'#{tc+1} {ans}')


