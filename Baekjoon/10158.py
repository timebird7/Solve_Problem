import sys
from time import time


W,H = map(int,sys.stdin.readline().split())
p,q = map(int,sys.stdin.readline().split())
T = int(sys.stdin.readline())
s = time()
dp = 1
dq = 1
# 0: 오른쪽위, 1:왼쪽위, 2:왼쪽아래, 3:오른쪽아래
d = 0
history = [0]*100000
history[0] = (p,q,0)
cnt = 1
for t in range(T):
    if p==0 and q==0:
        dp = 1
        dq = 1
        d = 0
    elif p==W and q==H:
        dp = -1
        dq = -1
        d = 2
    elif p==0 and q==H:
        dp = 1
        dq = -1
        d = 3
    elif p==W and q==0:
        dp = -1
        dq = 1
        d = 1
    elif p==W:
        dp = -1
        if d == 0:
            d = 1
        elif d == 3:
            d = 2
    elif q==H:
        dq = -1
        if d == 1:
            d = 2
        elif d == 0:
            d = 3
    elif p==0:
        dp = 1
        if d == 1:
            d = 0
        elif d == 2:
            d = 3
    elif q==0:
        dq = 1
        if d == 2:
            d = 1
        elif d == 3:
            d = 0

    p += dp
    q += dq

    if (p,q,d) != history[0]:
        history[cnt] = (p,q,d)
        cnt += 1
    else:
        break

r = T%len(history)

print(history[:cnt])

print(history[r][0],history[r][1])
print(time()-s)