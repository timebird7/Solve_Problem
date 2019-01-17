for i in range(10):
    n = int(input())
    nums = list(map(int,list(input().split())))    
    result = 0
    for x in range(n):
        nums.sort()
        if nums[-1] - nums[0] <= 1 :
            break
        nums[-1] -= 1
        nums[0] += 1
    nums.sort()
    result = nums[-1] - nums[0]
    print(f'#{i+1} {result}')