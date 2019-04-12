from itertools import product

def tour(x,y,h):
    global nums,N
    tmp = []
    for p in range(h[0]):
        if x+1<=N-1 and y-1>=0 and nums[x+1][y-1] not in tmp:
            tmp.append(nums[x+1][y-1])
            x += 1
            y -= 1
        else:
            return False

    for p in range(h[1]):
        if x+1<=N-1 and y+1<=N-1 and nums[x+1][y+1] not in tmp:
            tmp.append(nums[x+1][y+1])
            x += 1
            y += 1
        else:
            return False

    for p in range(h[0]):
        if x-1>=0 and y+1<=N-1 and nums[x-1][y+1] not in tmp:
            tmp.append(nums[x-1][y+1])
            x -= 1
            y += 1
        else:
            return False
    
    for p in range(h[1]):
        if x-1>=0 and y-1>=0 and nums[x-1][y-1] not in tmp:
            tmp.append(nums[x-1][y-1])
            x -= 1
            y -= 1
        else:
            return False

    return len(tmp)



TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nums = [0]*N
    for n in range(N):
        nums[n] = list(map(int,input().split()))

    a = [i for i in range(1,N-1)]
    ans = -1

    ls = list(product(a,repeat=2))
    for i in range(N-2):
        for j in range(1,N-1):
            for l in ls:
                if tour(i,j,l):
                    result = tour(i,j,l)
                    ans = max(ans,result)

    print(f'#{tc} {ans}')

    
