from copy import deepcopy

def findroad(nums,i,j):
    global N
    queue = [(i,j)]
    cnt = 0
    while True:
        cnt += 1
        tmp = []
        for q in queue:
            if q[0]-1 >=0 and nums[q[0]-1][q[1]] < nums[q[0]][q[1]]:
                tmp.append((q[0]-1,q[1]))
            if q[0]+1 <=N-1 and nums[q[0]+1][q[1]] < nums[q[0]][q[1]]:
                tmp.append((q[0]+1,q[1]))
            if q[1]-1 >=0 and nums[q[0]][q[1]-1] < nums[q[0]][q[1]]:
                tmp.append((q[0],q[1]-1))
            if q[1]+1 <=N-1 and nums[q[0]][q[1]+1] < nums[q[0]][q[1]]:
                tmp.append((q[0],q[1]+1))

        queue = tmp[:]
        if not queue:
            return cnt



TC = int(input())

for tc in range(1,TC+1):
    N,K = map(int,input().split())
    nums = [0]*N
    maxn = 0
    starts = []
    roads = []
    ans = 0

    for n in range(N):
        nums[n] = list(map(int,input().split()))
        maxn = max(maxn,max(nums[n]))

    for i in range(N):
        for j in range(N):
            if nums[i][j] == maxn:
                starts.append((i,j))            
            roads.append((i,j))


    for start in starts:
        for road in roads:
            if start != road:
                tnums = deepcopy(nums)
                ans = max(ans,findroad(tnums,start[0],start[1]))
                for k in range(K):
                    tnums[road[0]][road[1]] -= 1
                    ans = max(ans,findroad(tnums,start[0],start[1]))

    print(f'#{tc} {ans}')

    
