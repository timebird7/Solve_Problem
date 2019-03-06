nums = []

for i in range(5):
    nums.append(list(map(int,input().split())))

nums.append([nums[0][0],nums[1][0],nums[2][0],nums[3][0],nums[4][0]])
nums.append([nums[0][1],nums[1][1],nums[2][1],nums[3][1],nums[4][1]])
nums.append([nums[0][2],nums[1][2],nums[2][2],nums[3][2],nums[4][2]])
nums.append([nums[0][3],nums[1][3],nums[2][3],nums[3][3],nums[4][3]])
nums.append([nums[0][4],nums[1][4],nums[2][4],nums[3][4],nums[4][4]])

nums.append([nums[0][0],nums[1][1],nums[2][2],nums[3][3],nums[4][4]])
nums.append([nums[0][4],nums[1][3],nums[2][2],nums[3][1],nums[4][0]])

check = []

for i in range(5):
    check.extend(list(map(int,input().split())))

for i in range(25):
    for num in nums:
        for j in range(5):
            if check[i] == num[j]:
                num[j] = 0
    else:
        cnt = 0
        for k in nums:
            if sum(k) == 0:
                cnt += 1

        if cnt >= 3:
            print(i+1)
            break