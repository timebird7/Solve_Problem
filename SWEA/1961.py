TC = int(input())

for tc in range(TC):
    N = int(input())

    nums = [[] for i in range(N)]

    for i in range(N):
        nums[i] = input().split()
    print(f'#{tc+1}')    

    for j in range(N):
        a,b,c = '','',''
        for i in range(N):
            a += nums[N-1-i][j]
            b += nums[N-1-j][N-1-i]
            c += nums[i][N-1-j]

        print(f'{a} {b} {c}')    