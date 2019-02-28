def issudoku(i,j):
    global a
    if nums[i].count(nums[i][j]) == 1:
        a += 1
    else:
        return 0

    cnt = 0    

    for k in range(9):
        if nums[i][j] == nums[k][j]:
            cnt += 1

    if cnt == 1:
        a += 1
    else:
        return 0

    x = i%3
    y = j%3

    cnt = 0
    

    for a in range(i-x,i+3-x):
        for b in range(j-y,j+3-y):
            if nums[i][j] == nums[a][b]:
                cnt += 1

    if cnt == 1:
        a += 1
    else:
        return 0

    return 1

TC = int(input())

for tc in range(TC):
    a = 0
    nums = [[] for i in range(9)]

    for i in range(9):
        nums[i] = list(map(int,input().split()))

    for i in range(9):
        for j in range(9):
            ans = issudoku(i,j)

            if ans:
                a += 1

            else:
                break
        if ans:
            a += 1
        else:
            break

    print(f'#{tc+1} {ans}')





    