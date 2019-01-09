import sys


t = int(sys.stdin.readline())

ans = []
for a in range(t):
    x, y = map(int, sys.stdin.readline().split())
    cnt = 0
    r = x
    while r != y-1:      
        if r+cnt+1 <= y-1:
            r = r+cnt+1
        elif r+cnt <= y-1:
            r = r+cnt
        else :
            r = r+cnt-1
        cnt+=1
    ans.append(cnt+1)
    
for x in ans:
    print(x)
