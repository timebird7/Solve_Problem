TC = int(input())

for tc in range(TC):
    print('#{}'.format(tc + 1))
    N = int(input())
    if N == 1:
        print(1,end='')
    elif N == 2:
        print('1')
        print('1 1',end = '')
    else:


        nums = [[0 for i in range(N)] for j in range(N)]

        for i in range(N):
            nums[i][0] = 1
        nums[1][1] = 1

        for i in range(2,N):
            for j in range(1,N):
                nums[i][j] = nums[i-1][j-1] + nums[i-1][j]



        for num in nums:
            for n in num:
                if n:
                    print(n,end=' ')
                else:
                    print()
                    break
    
    print()