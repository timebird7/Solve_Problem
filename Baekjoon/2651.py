D = int(input())
N = int(input())
nums = [0]+list(map(int,input().split()))
time = [0]+list(map(int,input().split()))

tmp = 0
start = [[]]
ways = []
for i in range(1,N+2):
    tmp += nums[i]
    if tmp <= D:
        start[0].append(i)

for i in range(1,N+2):
    tmp = 0
    for j in range(i+1,N+2):
        tmp += nums[j]
        if tmp <= D:
            ways.append([i,j])


