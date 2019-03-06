nums = [[0 for i in range(101)] for j in range(101)]

N = int(input())

for n in range(N):
    tmp = list(map(int,input().split()))
    for i in range(tmp[0],tmp[0]+10):
        for j in range(tmp[1],tmp[1]+10):
            nums[i][j] = 1
ans = 0
for i in range(101):
    for j in range(101):
        ans += nums[i][j]

print(ans)