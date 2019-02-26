def cnt():
    global N
    global queue
    global ans
    x = 0

    while True:
        if not queue:
            ans.append(x)
            return
        for q in queue:
            tmp = queue.pop(0)
            x+=1
            i = tmp[0]
            j = tmp[1]
            nums[tmp[0]][tmp[1]] = 0

            if i>0 and nums[i-1][j] and [i-1,j] not in queue:
                queue.append([i-1,j])
            if i<N-1 and nums[i+1][j] and [i+1,j] not in queue:
                queue.append([i+1,j])
            if j>0 and nums[i][j-1] and [i,j-1] not in queue:
                queue.append([i,j-1])
            if j<N-1 and nums[i][j+1] and [i,j+1] not in queue:
                queue.append([i,j+1])

        


N = int(input())

nums = [[] for i in range(N)]
queue = []
ans = []

for i in range(N):
    nums[i] = list(map(int,list(input())))

for i in range(N):
    for j in range(N):
        if nums[i][j]:
            queue = [[i,j]]
            cnt()

ans.sort()
print(len(ans))
for a in ans:
    print(a)