def solve(i,j):
    global nums
    global M
    result = 0
    for x in range(i,i+M):
        for y in range(j,j+M):
            result += nums[x][y]
    return result

TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = [[] for i in range(N)]
    result = 0
    ans = 0

    for n in range(N):
        nums[n] = list(map(int,input().split()))

    for i in range(N-M+1):
        for j in range(N-M+1):

            ans = max(solve(i,j),ans)

    print('#{} {}'.format(tc+1,ans))