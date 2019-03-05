N = int(input())

nums = [list(map(int,input().split())) for i in range(N)]
ans = 0

for num in nums:
    result = 100000
    for n in nums:
        if num[1] == n[1] and num[0] != n[0]:
            if abs(num[0]-n[0]) < result:
                result = abs(num[0]-n[0])

    else:
        ans += result

print(ans)
