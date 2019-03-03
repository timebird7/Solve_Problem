def issudoku(i,j):
    cnt = 0  
    bcnt = 0  

    for k in range(9):
        if nums[i][j] == nums[i][k]:
            cnt += 1
        if nums[i][j] == nums[k][j]:
            bcnt += 1

    if cnt != 1 or bcnt != 1:
        return 0

    x = i%3
    y = j%3

    cnt = 0
    

    for a in range(i-x,i+3-x):
        for b in range(j-y,j+3-y):
            if nums[i][j] == nums[a][b]:
                cnt += 1

    if cnt != 1:
        return 0

    return 1

TC = int(input())

for tc in range(TC):
    nums = [[] for i in range(9)]

    for i in range(9):
        nums[i] = list(map(int,input().split()))

    for i in range(9):
        for j in range(9):
            ans = issudoku(i,j)

            if not ans:
                break
        if not ans:
            break

    print(f'#{tc+1} {ans}')





    