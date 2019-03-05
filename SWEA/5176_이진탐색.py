def inord(n):
    global tree
    global cnt
    if n:        
        inord(tree[n][0])
        nums[n] = cnt
        cnt += 1        
        inord(tree[n][1])

TC = int(input())

for tc in range(TC):
    N = int(input())
    tree = [[0,0] for i in range(N+1)]
    nums = [0 for i in range(N+1)]
    cnt = 1

    for i in range(1,N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1

    inord(1)
    print(f'#{tc+1} {nums[1]} {nums[N//2]}')

