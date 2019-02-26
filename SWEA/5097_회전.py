TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    print(f'#{tc+1} {nums[M%N]}')