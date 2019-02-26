def findmax(nums):
    result = 0
    for num in nums:
        if max(num) > result:
            result = max(num)
    return result

def findans(field):
    r = 0
    for f in field:
        r += sum(f)
    return r

nums = []
for i in range(4):
    nums.append(list(map(int,input().split())))

m = findmax(nums)

field = [[0 for i in range(m)] for j in range(m)]

for num in nums:
    for i in range(num[0],num[2]):
        for j in range(num[1],num[3]):
            field[i][j] = 1

print(findans(field))
