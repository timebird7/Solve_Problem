# nums = []

# for i in range(9):
#     nums.append(int(input()))

# ans = []
# for i in range(1<<9):
#     result = []
#     for j in range(10):
        
#         if i & (1<<j):
#             result.append(nums[j])

#     ans.append(result)



# for ans in ans:
#     if len(ans) == 7 and sum(ans) == 100:
#         for x in sorted(ans):
#             print(x)

from itertools import combinations

nums = [0]*9

for i in range(9):
    nums[i] = int(input())

nums.sort()
    
selected = combinations(nums,7)
flag = 0
for s in selected:
    if sum(s) == 100:
        for i in s:
            print(i)
        flag = 1

    if flag:
        break