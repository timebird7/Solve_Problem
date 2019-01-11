n = list(map(int, list(input())))

m = [x for x in range(0,10)]
cnt = [0]*10
for x in m:
    cnt[x] = n.count(x)

t = (cnt[6] + cnt[9] + 1)//2

cnt[6] = 0
cnt[9] = 0
cnt.append(t)

print(max(cnt))