def my_sum(ans):
    result = 0
    for i in ans:
        result += i
    return result

nums = [x+1 for x in range(12)]

TC = int(input())

for x in range(TC):
    ans = []
    N, K = list(map(int,list(input().split())))
    for i in range(1<<12):
        result = []
        for j in range(13):
            
            if i & (1<<j):
                result.append(nums[j])

        ans.append(result)
    
    cnt = 0
    
    for ans in ans:
        if len(ans) == N and my_sum(ans) == K:
            cnt += 1

    print(f'#{x+1} {cnt}')
