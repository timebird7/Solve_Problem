#답나옴, 시간초과


import sys
from collections import deque

n = int(sys.stdin.readline())
nums = [0]*4001

summation = 0

freq = 0

for i in range(n):
    a = int(sys.stdin.readline())

    summation += a
    nums[a] += 1

    if freq < nums[a]:
        freq = nums[a]
        cand = deque([a])

    elif freq == nums[a]:
        if cand[0] > a:
            cand.appendleft(a)
        else:
            cand.append(a)

print(round(summation/n))
cnt = -1
for i in range(4001):
    if nums[i]:
        cnt += 1
    if cnt == n//2:
        print(i)
        break

if len(cand) == 1:
    print(cand[0])
else:
    print(cand[1])

for i in range(4001):
    if nums[i]:
        minnum = i
        break

print(nums)

for i in range(4000,-1,-1):
    if nums[i]:
        maxnum = i
        break

print(maxnum - minnum)


