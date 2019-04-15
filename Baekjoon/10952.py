import sys
while True:
    nums =list(map(int, sys.stdin.readline().rstrip('\n').split()))
    n=sum(nums)
    if n:
        print(n)
    else:
        break