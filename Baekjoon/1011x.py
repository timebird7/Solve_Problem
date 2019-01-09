import sys

t = int(sys.stdin.readline())

ans = []
for tc in range(0,t):
    x, y = map(int, sys.stdin.readline().split())
    cnt = 0
    mv = 1
    while x != y-1:      
        if x+mv <= y-1:
            x += mv
            mv += 1
        elif x+mv-1 <= y-1:
            x += mv-1
        else :
            x += mv-2
        cnt +=1
    ans.append(cnt+1)
    
for x in ans:
    print(x)
