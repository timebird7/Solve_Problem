nums = [0 for i in range(1001)]

N = int(input())

for n in range(N):
    tmp = list(map(int,input().split()))
    nums[tmp[0]] = tmp[1]

hmax = max(nums)
tmp = 0
left = 0
right = 0
for i in range(1001):
    if nums[i] == hmax:
        left = i
        break
    if nums[i]:
        if nums[i] > tmp:
            tmp = nums[i]
        else:
            nums[i] = tmp
    else:
        nums[i] = tmp
tmp = 0

for i in range(1000,-1,-1):
    if nums[i] == hmax:
        right = i
        break
    if nums[i]:
        if nums[i] > tmp:
            tmp = nums[i]
        else:
            nums[i] = tmp
    else:
        nums[i] = tmp

for i in range(left,right):
    nums[i] = hmax

print(sum(nums))