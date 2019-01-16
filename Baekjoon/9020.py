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

for i in range(int(sys.stdin.readline())):

    n = int(sys.stdin.readline())

    for x in range(int(n/2),n):
        if is_prime(n-x) and is_prime(x):
            print(f'{n-x} {x}')
            break
