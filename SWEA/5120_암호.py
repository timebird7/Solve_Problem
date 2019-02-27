TC = int(input())

for tc in range(TC):
    N, M, K = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    x = 0

    for k in range(K):
        x += M
        if x < len(nums):
            y = nums[x-1] + nums[x]   
            nums.insert(x, y)
        elif x%len(nums) == 0:
            x = -1
            y = nums[-1] + nums[0]
            nums.append(y)
        else:
            x %= len(nums)
            y = nums[x-1] + nums[x]   
            nums.insert(x, y)                

    print(f'#{tc+1}',end='')

    for num in nums[:-11:-1]:
        print(f' {num}',end='')

    print()