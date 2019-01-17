T = int(input())

for x in range(T):
    a, b, c = map(int,list(input().split()))  
    nums = list(map(int,list(input().split())))    
    n = 0
    cnt = 0
    while n+a < b:
        i = len(nums)
        n += a
        nums_ = [z for z in nums if z <= n]
        nums = [z for z in nums if z > n]
        
        if len(nums) == i:
            cnt = 0
            break
        else:
            n = nums_[-1]
            cnt += 1  
    
    print(f'#{x+1} {cnt}')