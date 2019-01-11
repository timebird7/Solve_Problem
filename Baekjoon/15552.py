import sys
for x in range(0, int(sys.stdin.readline())):
    nums =list(map(int, sys.stdin.readline().rstrip('\n').split()))
    print(sum(nums))