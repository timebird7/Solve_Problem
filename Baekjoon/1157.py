import sys

s = sys.stdin.readline().upper()
t = len(s)
cnt = [0]*26
ans = []
for x in range(0,t):
    cnt.append(s.count(s[x]))
for x in range(0,t):
    if cnt[x] == max(cnt) and s[x] not in ans:
        ans.append(s[x])

if len(ans) == 1:
    print(ans[0])
else :
    print('?')
