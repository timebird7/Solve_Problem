from itertools import product
from time import time

s = time()
def perm_re(cnt):
    if cnt == 10:
        perms.append(perm[:10])
        return
    perm[cnt] = 0
    perm_re(cnt+1)
    perm[cnt] = 1
    perm_re(cnt+1)

perms = []
perm = [0] * 10
perm_re(0)

print(perms)
print(time()-s)
s =time()

a = [0,1]

print(list(product(a,repeat=10)))
print(time()-s)