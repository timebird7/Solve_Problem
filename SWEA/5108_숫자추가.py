TC = int(input())

for tc in range(TC):
    N, M, L = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    for m in range(M):
        i, j = list(map(int,input().split()))
        nums = nums[:i] + [j] + nums[i:]

    print(f'#{tc+1} {nums[L]}')