


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

a, b = list(map(int, sys.stdin.readline().split()))

for x in range(a, b+1):
    if is_prime(x):
        print(x)
