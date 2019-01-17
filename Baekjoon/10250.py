import math

TC = int(input())

for i in range(TC):
    H, W, N = map(int,list(input().split()))  
    x = str(N%H)
    if x == '0':
        x = str(H)
    y = str(math.ceil(N/H))
    if int(y) < 10:
        result = x + '0' + y
    else:
        result = x + y
    print(int(result))
