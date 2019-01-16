import sys

def is_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = 0
minnum = -1
for x in range(m, n+1):
    if is_prime(x):
        minnum = x
        break

for x in range(m, n+1):
    if is_prime(x):
        result += x
if result :
    print(result)
print(minnum)