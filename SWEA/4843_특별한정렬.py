def findmaxswitch(nums):
    result = 0
    for x in nums:
        if x > result :
            result = x

    for y in range(len(nums)):
        if nums[y] == result:
            nums.pop(y)
            break
    
    print(f' {result}',end='')
    return nums



def findminswitch(nums):
    result = 100
    for x in nums:
        if x < result :
            result = x

    for y in range(len(nums)):
        if nums[y] == result:
            nums.pop(y)
            break
    
    print(f' {result}',end='')
    return nums


TC = int(input())

for i in range(TC):
    n = int(input())
    nums = list(map(int,list(input().split())))

    print(f'#{i+1}',end='')

    for j in range(5):
        nums = findmaxswitch(nums)
        nums = findminswitch(nums)

    print('')
