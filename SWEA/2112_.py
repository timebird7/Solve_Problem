def test(film):
    global D,W,K
    for j in range(W):
        flag = 0
        tmp = film[0][j]
        for i in range(1,D):            
            if tmp[-1] == film[i][j]:
                # tmp += film[i][j]
                tmp = '%s%s'%(tmp,film[i][j])
            else:
                tmp = film[i][j]
            if len(tmp) >= K:
                flag = 1
                break
        if flag == 0:
            return False
    return True

def dfs(film,doping,i,cnt,visited):
    global D,W,ans
    if cnt >= ans:
        return
    tmp = film[:]
    tmp[i] = doping*W
    tmp_ = visited[:]
    tmp_[i] = 1 

    if test(tmp):
        ans = min(ans,cnt)
        return    

    for j in range(i+1,D):
        if tmp_[j] == 0:
            dfs(tmp,'0',j,cnt+1,tmp_)
            dfs(tmp,'1',j,cnt+1,tmp_)

TC = int(input())

for tc in range(1,TC+1):
    D, W, K = map(int,input().split())
    nums = [0] * D

    for d in range(D):
        nums[d] = ''.join(input().split())

    visited = [0]*D
    ans = 10000

    if test(nums):
        ans = 0

    else:
        for i in range(D):
            dfs(nums,'0',i,1,visited)
            dfs(nums,'1',i,1,visited)

    print(f'#{tc} {ans}')