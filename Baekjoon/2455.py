import sys
k = 0
ans = 0
for i in range(4):
    m, n = list(map(int, sys.stdin.readline().split()))
    k = k - m + n
    if k > ans :
        ans = k

print(ans)