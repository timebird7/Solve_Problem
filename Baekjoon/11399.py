N = int(input())
nums = list(map(int,input().split()))
nums.sort()

result = 0

for i in range(len(nums)):
    result += sum(nums[:i+1])

print(result)
