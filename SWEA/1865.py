def revnum(n):
    n = int(n)
    n = 100 - n
    return n

def backtrack(input,k,visited,nsum,ans):
    global nums
    global result
    global p
    if nsum > result:
        return
    if k == input:
        if nsum <= result:
            result = nsum
            p = max(ans, p)
    else:
        for i in range(input):
            if visited[i]==1:
                continue
            visited[i] = 1
            backtrack(input,k+1,visited,nsum*nums[k][i],100*(ans*((100-nums[k][i])/100)))
            visited[i] = 0

TC = int(input())

for tc in range(TC):
    n = int(input())
    nums = [[] for i in range(n)]
    p = 0.0
    for i in range(n):
        nums[i] = list(map(revnum,input().split()))

    visited = [0]*n
    result = 1000000000

    backtrack(n,0,visited,0,1)
    
    p = round(p/10000, 6)


    print('#{} {:0.6f}'.format(tc+1, p))