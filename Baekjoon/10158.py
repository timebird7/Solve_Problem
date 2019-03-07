W,H = list(map(int,input().split()))
p,q = list(map(int,input().split()))
T = int(input())
dp = 1
dq = 1
for t in range(T):
    if p==W:
        dp = -1
    if q==H:
        dq = -1

    if p==0:
        dp = 1
    if q==0:
        dq = 1

    p += dp
    q += dq

print('{} {}'.format(p,q))