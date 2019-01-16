for i in range(10):
    n = int(input())
    nums = list(map(int,list(input().split())))    
    result = 0
    for x in range(2,n-1):
        if nums[x] == sorted(nums[x-2:x+3])[-1]:
            result += nums[x] - sorted(nums[x-2:x+3])[-2]    
    print(f'#{i+1} {result}')


