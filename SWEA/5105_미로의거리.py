def solve(N):
    global queue
    global nums
    global flag
    global cnt
    tmp = []
    for q in queue:
        if q[0] > 0 and nums[q[0]-1][q[1]] != 1:
            tmp.append([q[0]-1,q[1]])
        if q[0] < N-1 and nums[q[0]+1][q[1]] != 1:
            tmp.append([q[0]+1,q[1]])
        if q[1] > 0 and nums[q[0]][q[1]-1] != 1:
            tmp.append([q[0],q[1]-1])
        if q[1] < N-1 and nums[q[0]][q[1]+1] != 1:
            tmp.append([q[0],q[1]+1]) 

        if nums[q[0]][q[1]] == 3:
            flag = 1
            return

        nums[q[0]][q[1]] = 1    

    queue = tmp
    cnt += 1


def findtwo(nums):
    for i in range(N):
        for j in range(N):
            if nums[i][j] == 2:
                return [i, j]

TC = int(input())

for tc in range(TC):
    N = int(input())
    flag = 0
    eflag = 0
    cnt = 0

    nums = [0 for i in range(N)]

    for i in range(N):
        nums[i] = list(map(int,list(input())))

    queue = [findtwo(nums)]

    while True:
        solve(N)

        if flag:
            break

        if not queue:
            eflag = 1
            break
    
    if eflag:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {cnt-1}')

