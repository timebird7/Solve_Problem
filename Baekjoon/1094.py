n = int(input())
cnt = 0
nums = [64, 32, 16, 8, 4, 2, 1]

for x in nums:
    if n >= x:
        n -= x
        cnt += 1
        
print(cnt)