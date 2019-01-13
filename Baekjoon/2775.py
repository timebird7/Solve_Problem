# math 안쓴답 런타임에러지만 답은나옴
import sys
n = int(sys.stdin.readline())

f = [[]]*14
f[0] = [x for x in range(1,15)]
for x in range(1,14):
    f[x] = [0]*14
for y in range(0, n):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())-1
    for p in range(0, 13):
        for x in range(0,14):
            result = 0
            for t in range(0,x+1):
                result += f[p][t]
            f[p+1][x] = result
    
    print(f[a][b])

#======================================================
#math 쓴답

import math

n = int(input())
for x in range(0, n):
    a = int(input())
    b = int(input())
    c = math.factorial(a+b)
    c = c // math.factorial(a+1)
    c = c // math.factorial(b-1)
    print(c)




