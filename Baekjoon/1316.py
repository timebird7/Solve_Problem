t = int(input())
cnt = 0

for q in range(0,t):
    s = list(input())
    ans = []

    ans.append(s[0])
    for n in s[1:]:
        if n != ans[-1]:
            ans.append(n)



    result = []

    for n in ans:
        if ans.count(n) == 1:
            result.append(1)
    


    if len(ans) == len(result):
        cnt += 1

print(cnt)

