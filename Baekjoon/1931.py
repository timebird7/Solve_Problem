N = int(input())
nums = [0 for i in range(N)]
for n in range(N):
    nums[n] = tuple(map(int, input().split()))
if N <= 1:
    print(N)

else:    
    nums = sorted(nums, key=lambda x:(x[1], x[0]))
    selected = nums.pop(0)
    cnt = 1

    for num in nums:    
        if num[0] < selected[1]:
            continue
        else:
            selected = num
            cnt += 1
            continue

    print(cnt)