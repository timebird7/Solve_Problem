def backtrack(input,k,visited,nsum):
    global nums
    global result
    if nsum > result:
        return
    if k == input:
        if nsum < result:
            result = nsum
    else:
        for i in range(input):
            if visited[i]==1:
                continue
            visited[i] = 1
            backtrack(input,k+1,visited,nsum+nums[k][i])
            visited[i] = 0

TC = int(input())

for tc in range(TC):
    n = int(input())
    nums = [[] for i in range(n)]
    
    for i in range(n):
        nums[i] = list(map(int,input().split()))

    visited = [0]*n
    result = 10000

    backtrack(n,0,visited,0)
    
    print(f'#{tc+1} {result}')