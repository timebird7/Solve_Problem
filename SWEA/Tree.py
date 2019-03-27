N = int(input())
ways = list(map(int,input().split()))
print(ways)
nums = [[None,None,None] for i in range(max(ways))]
for n in range(N):
    print(n)
    if nums[ways[2*n]][0] == None:
        nums[ways[2*n]][0] = ways[2*n+1]
        nums[ways[2*n+1]][2] = ways[2*n]
    else:
        nums[ways[2*n]][1] = ways[2*n+1]
        nums[ways[2*n+1]][2] = ways[2*n]

print(nums)


