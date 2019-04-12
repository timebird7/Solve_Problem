from itertools import combinations

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())

    tastes = [0]*N
    for n in range(N):
        tastes[n] = list(map(int,input().split()))

    combs = combinations(range(N),N//2)
    ans = 1000000

    for comb_a in combs:
        a_taste = 0
        b_taste = 0
        comb_b = []
        for i in range(N):
            if i not in comb_a:
                comb_b.append(i)

        combs_a = combinations(comb_a,2)
        for c in combs_a:
            a_taste += tastes[c[0]][c[1]]
            a_taste += tastes[c[1]][c[0]]
        combs_b = combinations(comb_b,2)
        for c in combs_b:
            b_taste += tastes[c[0]][c[1]]
            b_taste += tastes[c[1]][c[0]]


        result = abs(a_taste-b_taste)
        ans = min(ans,result)

    print(f'#{tc} {ans}')