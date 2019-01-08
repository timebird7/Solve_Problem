t = int(input())
tc = 0
ans = []
while tc < t:
    x, y = map(int, input().split())
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
    tc += 1
for x in ans:
    print(x)
