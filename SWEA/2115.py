from itertools import combinations

def select(N,M,nums):
    tmp = []
    for i in range(N):
        for j in range(N):
            nj = j+M-1
            if 0<=nj<N:
                tmp.append([i,j])

    return tmp

TC = int(input())

for tc in range(1,TC+1):
    N, M, C = map(int, input().split())
    nums = [0] * N

    for n in range(N):
        nums[n] = list(map(int, input().split()))

    ans = 0
    cand = select(N,M,nums)

    selected = combinations(cand,2)
    

    for s in selected:
        tmp_a = []
        tmp_b = []
        selected_a = set()
        selected_b = set()
        ax, ay = s[0][0], s[0][1]
        bx, by = s[1][0], s[1][1]

        if ax == bx and by<=ay+M:
            continue

        a = nums[ax][ay:ay+M]
        b = nums[bx][by:by+M]

        for i in range(M+1):
            tmp_a.extend(combinations(a,i))
            tmp_b.extend(combinations(b,i))

        for x in tmp_a:
            selected_a.add(x)

        for x in tmp_b:
            selected_b.add(x)

        for x in selected_a:
            for y in selected_b:
                result = 0
                if sum(x) <= C and sum(y) <= C:
                    result += sum(map(lambda z: z*z,x))
                    result += sum(map(lambda z: z*z,y))
                    ans = max(result, ans)

    print(f'#{tc} {ans}')



    
