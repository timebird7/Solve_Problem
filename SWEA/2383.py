def perm_re(cnt):
    global visited
    if cnt == peoplecnt:
        perms.append(perm[:peoplecnt])
        return
    perm[cnt] = 0
    visited[0] += 1
    perm_re(cnt+1)
    visited[0] -= 1
    perm[cnt] = 1
    visited[1] += 1
    perm_re(cnt+1)
    visited[1] -= 1

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nums = [0] * N
    stairs = []
    people = []

    for n in range(N):
        nums[n] = list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            if nums[i][j] == 1:
                people.append([i,j])
            elif nums[i][j] >= 2:
                stairs.append([i,j,nums[i][j]])
    
    peoplecnt = len(people)

    perms = []
    visited = [0, 0]
    perm = [0] * 10
    perm_re(0)

    result = 0
    ans = 1000000


    for d in perms:
        r1, r2 = 0,0
        stair = [[0 for i in range(4*N)] for j in range(2)]
        for i in range(peoplecnt):
            sx, sy, k = stairs[d[i]]
            px, py = people[i]
            t = abs(sx-px) + abs(sy-py) + k + 1
            stair[d[i]][t] += 1

        k = stairs[0][2]

        for i in range(len(stair[0])-k):
            if sum(stair[0][i:i+k]) > 3:
                of = sum(stair[0][i:i+k]) - 3

                for a in range(i+k-1,i-1,-1):
                    if stair[0][a] >= of:
                        stair[0][a] -= of
                        stair[0][i+k] += of
                        break
                    else:
                        of -= stair[0][a]
                        stair[0][a] = 0
                        continue

        k = stairs[1][2]

        for i in range(len(stair[1])-k):
            if sum(stair[1][i:i+k]) > 3:
                of = sum(stair[1][i:i+k]) - 3

                for a in range(i+k-1,i-1,-1):
                    if stair[1][a] >= of:
                        stair[1][a] -= of
                        stair[1][i+k] += of
                        break
                    else:
                        of -= stair[1][a]
                        stair[1][a] = 0
                        continue

        for i in range(len(stair[0])):
            if stair[0][i]:
                r1 = i
        for i in range(len(stair[1])):
            if stair[1][i]:
                r2 = i

        r = max(r1,r2)

        ans = min(ans,r)

    print(f'#{tc} {ans}')