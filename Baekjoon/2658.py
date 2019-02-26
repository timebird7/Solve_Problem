def isok(i,j):
    global nums

    if i<9 and j<8 and nums[i][j+1] and nums[i][j+2] and nums[i+1][j+1] and not nums[i+1][j]:
        return [1,i,j]
    elif i<9 and j>0 and j<9 and nums[i+1][j-1] and nums[i+1][j] and nums[i+1][j+1] and not nums[i][j+1]:
        return [2,i,j]
    elif i<8 and j<9 and nums[i+1][j] and nums[i+2][j] and nums[i+1][j-1]:
        return [3,i,j]
    elif i<8 and j>0 and nums[i+1][j] and nums[i+2][j] and nums[i+1][j+1] and not nums[i][j+1]:
        return [4,i,j]
    else:
        return [0,i,j]

nums = [[] for i in range(10)]
a = [-1,-1,-1]
for i in range(10):
    nums[i] = list(map(int,list(input())))

for i in range(10):
    for j in range(10):
        if nums[i][j]:
            a = isok(i,j)
            break
    if a[0] >= 0:
        break

if a[0] == 0:
    print(0)
else:
    if a[0] == 1:
        cnt = 0
        while a[2]+cnt <= 9 and nums[a[1]][a[2]+cnt]:
            cnt += 1

        x = a[2]+cnt
        sum(nums[a[1]+1][a[2]+1:x])


# 111
# 01               1

# *1
# 11
# *1            3

# *10
# 111              2

# 10
# 11
# 1*            4
        


        