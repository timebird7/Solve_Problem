

import sys

def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,int(n**0.5)+1):
            if(n % x==0):
                return False
        return True


for x in sys.stdin:
    cnt = 0
    n = int(x)
    if n == 0:
        break
    else:
        for y in range(n+1,2*n+1):
            if is_prime(y):
                cnt += 1
        print(cnt)


