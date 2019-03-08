TC = int(input())

for tc in range(TC):
    N, K = list(map(int,input().split()))
    puzzle = [[0 for i in range(N)] for j in range(N)]

    for n in range(N):
        puzzle[n] = list(map(int,input().split()))
        
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j]:
                cnt += 1
            elif cnt and not puzzle[i][j]:
                if cnt == K:
                    ans += 1
                cnt = 0
        else:
            if cnt:
                if cnt == K:
                    ans += 1

    for x in range(N):
        for y in range(N):
            if x > y:
                puzzle[x][y],puzzle[y][x] = puzzle[y][x],puzzle[x][y]

    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j]:
                cnt += 1
            elif cnt and not puzzle[i][j]:
                if cnt == K:
                    ans += 1
                cnt = 0
        else:
            if cnt:
                if cnt == K:
                    ans += 1

    print('#{} {}'.format(tc+1,ans))