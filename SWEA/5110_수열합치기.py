TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    nums = [[] for i in range(M-1)]
    
    ans = list(map(int,input().split()))
    for i in range(M-1):
        nums[i] = list(map(int,input().split()))

    for i in range(M-1):
        for n in range(len(ans)):
            if ans[n] > nums[i][0]:
                ans = ans[:n] + nums[i] + ans[n:]
                break
        else:
            ans = ans + nums[i]
            
        if N > 10 and len(ans) > N:
            ans = ans[-N-10:]

    print(f'#{tc+1}',end='')
    for a in ans[:-11:-1]:
        print(f' {a}',end='')

    print()