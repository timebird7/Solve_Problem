N = int(input())
switch = [None] + list(map(int,input().split()))
M = int(input())

for m in range(M):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        for i in range(tmp[1],N+1,tmp[1]):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1
    elif tmp[0] == 2:
        cnt = 0
        while tmp[1]-cnt > 0 and tmp[1]+cnt < N+1:
            if switch[tmp[1]-cnt] == switch[tmp[1]+cnt]:
                if switch[tmp[1]-cnt]:
                    switch[tmp[1]-cnt] = 0
                    switch[tmp[1]+cnt] = 0
                else:
                    switch[tmp[1]-cnt] = 1
                    switch[tmp[1]+cnt] = 1
                cnt += 1
            else:
                break

cnt = 0
for s in switch[1:]:
    cnt += 1
    print(s,end=' ')
    if cnt == 20:
        print()
        cnt = 0

