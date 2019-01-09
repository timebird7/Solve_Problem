import sys
t = int(sys.stdin.readline())

nums = []
ans = []
nums.append(list(map(int, sys.stdin.readline().split())))
nums.append(list(map(int, sys.stdin.readline().split())))
nums.append(list(map(int, sys.stdin.readline().split())))



cnt = 0
r = nums[0][0]
while r != nums[0][1]-1:      
    if r+cnt+1 <= nums[0][1]-1:
        r = r+cnt+1
    elif r+cnt <= nums[0][1]-1:
        r = r+cnt
    else :
        r = r+cnt-1
    cnt+=1
ans.append(cnt+1)
    

cnt = 0
r = nums[1][0]
while r != nums[1][1]-1:      
    if r+cnt+1 <= nums[1][1]-1:
        r = r+cnt+1
    elif r+cnt <= nums[1][1]-1:
        r = r+cnt
    else :
        r = r+cnt-1
    cnt+=1
ans.append(cnt+1)

cnt = 0
r = nums[2][0]
while r != nums[2][1]-1:      
    if r+cnt+1 <= nums[2][1]-1:
        r = r+cnt+1
    elif r+cnt <= nums[2][1]-1:
        r = r+cnt
    else :
        r = r+cnt-1
    cnt+=1
ans.append(cnt+1)

for x in ans:
    print(x)
