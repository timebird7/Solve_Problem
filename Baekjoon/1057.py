import sys
import math

twos = [2**x for x in range(18)]
a, b, c = list(map(int, sys.stdin.readline().split()))
for x in twos:
    if a < x:
        n = twos.index(x)
        for y in range(n+1):
            if math.ceil(b/(2**y)) == math.ceil(c/(2**y)):
                print(y)
                break
        break

