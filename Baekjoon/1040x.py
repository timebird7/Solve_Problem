import sys

N, K = list(map(int, sys.stdin.readline().rstrip('\n').split()))

while 1:
    
    result = len(set(str(N)))

    if result == K:
        print(N)
        break
    
    N += 1

