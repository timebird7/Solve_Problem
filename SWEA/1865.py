def divnum(n):
    n = int(n)
    n = n/100
    return n

def backtrack(input,k,visited,ans):
    global nums
    global result
    if ans <= result:
        return
    if k == input:
        if ans > result:
            result = ans
    else:
        for i in range(input):
            if visited[i]==1:
                continue
            visited[i] = 1
            backtrack(input,k+1,visited,ans*nums[k][i])
            visited[i] = 0

TC = int(input())

for tc in range(TC):
    n = int(input())
    nums = [[] for i in range(n)]
    for i in range(n):
        nums[i] = list(map(divnum,input().split()))

    visited = [0]*n
    result = 0

    backtrack(n,0,visited,1)


    print('#{} {:0.6f}'.format(tc+1, 100*result))