import math

nums = [[0 for i in range(2)] for j in range(7)]

N, K = list(map(int,input().split()))
ans = 0

for n in range(N):
    j, i = list(map(int,input().split()))
    nums[i][j] += 1

for i in range(7):
    for j in range(2):
        if nums[i][j]:
            ans += math.ceil(nums[i][j]/K)

print(ans)