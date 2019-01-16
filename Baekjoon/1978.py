n = int(input())
nums = list(map(int, input().split()))

cnt = 0
if 1 in nums :
    nums.remove(1)
if 2 in nums :
    nums.remove(2)
    cnt += 1



for x in nums:
    m = 0
    for y in range(2,x):
        if x%y == 0:
            m = y
    if m == 0:
        cnt += 1

print(cnt)
