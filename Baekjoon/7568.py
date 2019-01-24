N = int(input())

nums = []

cntlist = [1 for i in range(N)]
ranklist = [0 for i in range(N)]

for i in range(N):
    nums.append(list(map(int, list(input().split()))))

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            cntlist[i] += 1

for i in cntlist[:-1]:
    print(i,end=' ')
print(cntlist[-1])