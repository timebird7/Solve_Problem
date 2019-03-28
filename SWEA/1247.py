from itertools import permutations

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input().split()))
    start = [nums[0], nums[1]]
    home = [nums[2], nums[3]]
    result = 1000000

    order = [i for i in range(N)]
    ways = permutations(order)

    for way in ways:        
        tmp = 0
        start = [nums[0], nums[1]]
        for w in way:
            tmp += abs(start[0] - nums[2*(w+2)]) + abs(start[1] - nums[2*(w+2)+1])
            start = [nums[2*(w+2)], nums[2*(w+2)+1]]
            if tmp > result:
                break
        else:
            tmp += abs(start[0] - home[0]) + abs(start[1] - home[1])
            result = min(result, tmp)
            
    print(f'#{tc} {result}')

