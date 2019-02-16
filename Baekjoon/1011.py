import math

TC = int(input())

for tc in range(TC):
    x, y = list(map(int, input().split()))
    n = y - x
    m = int((math.sqrt(n) - 0.0001)//0.5)

    print(m)

    