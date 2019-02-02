TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    strlist = [[] for x in range(N)]

    for i in range(N):
        strlist[i] = input()
    result = ''

    for s in strlist:
        for i in range(N-M+1):
            cnt = 0
            j = 0
            while s[i+j] == s[i+M-j-1] :
                cnt += 1
                j += 1
                if cnt >= (M//2) + 1:
                    result = s[i:i+M]
                    break

    for x in range(N):
        for y in range(N):
            if x < y:
                strlist[x][y] = strlist[y][x]
                strlist[y][x] = strlist[x][y]

    for s in strlist:

        
        for i in range(N-M+1):
            cnt = 0
            j = 0
            while s[i+j] == s[i+M-j-1] :
                cnt += 1
                j += 1
                if cnt >= (M//2) + 1:
                    result = s[i:i+M]
                    break

    print(result)