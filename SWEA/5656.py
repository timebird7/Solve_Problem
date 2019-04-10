from copy import deepcopy

def perm_re(cnt):
    global N,W
    if cnt == N:
        perms.append(perm[:N])
        return
    for w in range(W):
        perm[cnt] = w
        perm_re(cnt+1)

def brick(i):
    global W,H,nums
    for h in range(H):
        if nums[h][i]:
            boom(h,i)
            return

def boom(x,y):
    global W,H,nums
    pw = nums[x][y]
    nums[x][y] = 0
    tmp = set()
    for i in range(x-pw+1,x+pw):
        if 0<=i<=H-1:    
            tmp.add((i,y))

    for i in range(y-pw+1,y+pw):
        if 0<=i<=W-1:
            tmp.add((x,i))

    for t in tmp:
        boom(t[0],t[1])


def check(nums):
    global W,H
    cnt = 0
    for i in range(H):
        for j in range(W):
            if nums[i][j]:
                cnt += 1
    return cnt

def pushdown(nums):
    global W,H
    for j in range(W):
        for i in range(H-2,-1,-1):
            t = i
            while True:
                if t >= H-1:
                    break
                if nums[t+1][j] == 0:
                    nums[t+1][j] = nums[t][j]
                    nums[t][j] = 0
                    t += 1
                else:
                    break

TC = int(input())

for tc in range(1,TC+1):
    N,W,H = map(int,input().split())
    rnums = [0]*H
    ans = W*H

    for h in range(H):
        rnums[h] = list(map(int,input().split()))

    perms = []
    perm = [0] * 10
    perm_re(0)

    for per in perms:
        result = W*H
        nums = deepcopy(rnums)
        for p in per:
            brick(p)
            pushdown(nums)

        result = check(nums)

        ans = min(ans,result)

        if ans == 0:
            break

        

    print(f'#{tc} {ans}')