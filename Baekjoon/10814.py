import sys
from collections import deque

N = int(sys.stdin.readline())

nums = [deque([]) for i in range(201)]

for n in range(N):
    i, j = sys.stdin.readline().split()
    nums[int(i)].append(j)

for i in range(201):
    for j in range(len(nums[i])):
        print(i,nums[i].popleft())