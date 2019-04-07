import sys

N = int(sys.stdin.readline())

nums = [0]*10001

for n in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)