N = int(input())

tmp = []
for i in range(6):
    tmp.append(list(map(int,input().split())))

nmax = 0
cut = 0
for i in range(6):
    if tmp[i][1] > nmax:
        cut = i
        nmax = tmp[i][1]

tmp = tmp[cut:] + tmp[:cut]

dr = [0,0,0,0,0]
ans = 1
flag = 0
for t in tmp:
    if dr[t[0]]:
        if flag:
            b = dr[t[0]]
            dr[t[0]] = 0
        else:
            flag = 1
            a = t[1]
            dr[t[0]] = 0
    else:
        dr[t[0]] = t[1]

for d in dr:
    if d:
        ans *= d

ans -= a*b

print(ans*N)