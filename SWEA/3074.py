TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    nums = [int(input()) for i in range(N)]
    
    l = 0
    r = M*max(nums)
    m = (l+r)//2

    while True:
        result = 0
        for num in nums:
            result += m//num

        if l == r:
            break

        elif result < M:
            l = m + 1
            m = (l+r)//2

        elif result >= M:
            r = m
            m = (l+r)//2

    print(f'#{tc} {m}')