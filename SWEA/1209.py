def my_sum(my_list):
    result = 0
    for i in my_list:
        result += i
    return result

for i in range(10):
    nums = []
    result = 0
    cs = 0
    cs_ = 0
    n = int(input())

    for j in range(100):
        nums.append(list(map(int, list(input().split()))))

    for x in range(100):
        if my_sum(nums[x]) > result :
            result = my_sum(nums[x])
        cs += nums[x][x]
        cs_ += nums[x][99-x]
    
    for x in range(100):
        for y in range(100):
            if x < y:
                nums[x][y], nums[y][x] = nums[y][x], nums[x][y]

    for x in range(100):
        if my_sum(nums[x]) > result :
            result = my_sum(nums[x])

    if cs > result:
        result = cs
    if cs_ > result:
        result = cs_

    print(f'#{n} {result}')

        

    