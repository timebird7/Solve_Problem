TC = int(input())

for tc in range(TC):
    N, B = map(int, input().split())
    nums = list(map(int, input().split()))

    n = len(nums)
    result = 1000

    for i in range(0, 1<<n):
        tmp = []
        for j in range(0, n):
            if i & (1<<j):
                tmp.append(nums[j])

        if sum(tmp) >= B:
            result = min(result,sum(tmp) - B)

        if result == 0:
            break

    print(f'#{tc+1} {result}')