def my_sum(ans):
    result = 0
    for i in ans:
        result += i
    return result

nums = []

for i in range(9):
    nums.append(int(input()))

ans = []
for i in range(1<<9):
    result = []
    for j in range(10):
        
        if i & (1<<j):
            result.append(nums[j])

    ans.append(result)



for ans in ans:
    if len(ans) == 7 and my_sum(ans) == 100:
        for x in sorted(ans):
            print(x)

