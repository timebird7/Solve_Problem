def rot(i,j):
    global m
    lflag = 0
    rflag = 0
    
    
    if i < 4 and m[i][2] != m[i+1][6]:
        if j == 1:            
            rot(i+1,-1)
        else:            
            rot(i+1,1)

    if i > 1 and m[i][6] != m[i-1][2]:
        if j == 1:
            rot(i-1,-1)
        else:
            rot(i-1,1)

    if j == 1:
        m[i] = [m[i][7]] + m[i][:7]
    else:
        m[i] = m[i][1:] + [m[i][0]]
    

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

    # for x in range(4):
    #     if m[x+1][0]:
    #         ans += 2^x

    # print(ans)


