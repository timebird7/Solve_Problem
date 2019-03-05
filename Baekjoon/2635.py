n = int(input())
ans = []

for i in range(1,n+1):
    nums = [n,i]
    while nums[-2]-nums[-1] >= 0:
        nums.append(nums[-2]-nums[-1])
    else:
        if len(nums) > len(ans):
            ans = nums

print(len(ans))
for num in ans:
    print(num,end=' ')

