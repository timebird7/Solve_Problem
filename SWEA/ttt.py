def backtrack(a, k, input):
    global MAXCANDIDATES
    global ans
    global nums
    global result
    global nsum
    c = [0] * MAXCANDIDATES
    

    if k == input:        
        if nsum < result:
            result = nsum
        nsum = 0
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            nsum += nums[i][c[i]]
            if nsum > result:
                continue
            backtrack(a, k, input)

def construct_candidates(a, k, input, c):
    in_perm = [False] *NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


TC = int(input())

for tc in range(TC):
    n = int(input())
    ans = []
    result = 10000
    nums = [[0 for x in range(n+1)] for y in range(n+1)]

    for i in range(1,n+1):
        nums[i][1:] = list(map(int, input().split()))

    MAXCANDIDATES = n+1
    NMAX = n+1
    a = [0] * NMAX
    nsum = 0
    backtrack(a, 0, n)


    print(f'#{tc+1} {result}')
