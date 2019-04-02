TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    f = set()
    ff = set()
    tmp = []

    for m in range(M):
        x, y = map(int, input().split())
        if x == 1:
            f.add(y)
        if y == 1:
            f.add(x)
        tmp.append([x, y])

    if len(f):
        for t in tmp:
            for i in f:                
                if t[0] == i:
                    ff.add(t[1])
                if t[1] == i:
                    ff.add(t[0])

        for j in ff:
            f.add(j)

        ans = len(f) - 1
    
    else:
        ans = 0

    print(f'#{tc} {ans}')