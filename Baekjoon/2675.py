t = int(input())
cnt = 0
anss = []
while cnt < t:
    ans = ''
    
    results = []
    tc = list(input().split())
    param = int(tc[0])
    words = list(tc[1])
    for x in words :
        results.append(x*param)
    for x in results :
        ans += x
    anss.append(ans)
    cnt += 1

for x in anss :
    print(x)