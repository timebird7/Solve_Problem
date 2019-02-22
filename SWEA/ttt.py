# def backtrack(a, k, input, nsum, x):
#     global MAXCANDIDATES
#     global ans
#     global nums
#     global result
#     x += 1
#     c = [0] * MAXCANDIDATES
#     if nsum > result:
#         x = 0
#         return

#     if k == input:        
#         if nsum < result:
#             result = nsum
#         nsum = 0
#         x = 0
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             nsum += nums[x][a[k]]
#             backtrack(a, k, input, nsum, x)

# def construct_candidates(a, k, input, c):
#     in_perm = [False] *NMAX

#     for i in range(1, k):
#         in_perm[a[i]] = True

#     ncandidates = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates


# TC = int(input())

# for tc in range(TC):
#     n = int(input())
#     ans = []
#     result = 10000
#     nums = [[0 for x in range(n+1)] for y in range(n+1)]

#     for i in range(1,n+1):
#         nums[i][1:] = list(map(int, input().split()))

#     MAXCANDIDATES = n+1
#     NMAX = n+1
#     a = [0] * NMAX
#     backtrack(a, 0, n, 0, 0)


#     print(f'#{tc+1} {result}')
def backtrack(input,k,visited,nsum):
    global nums
    global result
    if nsum > result:
        return
    if k == input:
        result = min(result,nsum)
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