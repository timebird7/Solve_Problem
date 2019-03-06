TC = int(input())

for tc in range(TC):
    N = int(input())
    nums = list(map(int,input().split()))
    ans = -1
    for i in range(N):
        for j in range(i+1,N):
            r = nums[i]*nums[j]
            s = list(str(r))
            for k in range(len(s)-1):
                if s[k] <= s[k+1]:
                    continue
                else:
                    break
            else:
                ans = max(ans, r)

    print(f'#{tc+1} {ans}')