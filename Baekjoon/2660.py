N = int(input())
ways = []
scores = [0]*(N+1)
while True:
    tmp = list(map(int,input().split()))
    if tmp == [-1,-1]:
        break
    else:
        ways.append(tmp)
        ways.append([tmp[1],tmp[0]])

for i in range(1,N+1):
    start = i
    queue = [start]
    q = []
    cnt = 0
    visited = [0]*(N+1)
    visited[start] = 1
    
    while queue:
        tmp = queue.pop(0)        
        for way in ways:
            if way[0] == tmp and visited[way[1]] == 0:
                visited[way[1]] = 1
                q.append(way[1])

        if not q and not queue:
            cnt = 100000
            break

        if not queue:
            queue = q
            q = []
            cnt += 1
            if sum(visited) == N:
                break        

    scores[i] = cnt

score = min(scores[1:])
print(f'{score} {scores.count(score)}')
for i in range(1,N+1):
    if scores[i] == score:
        print(f'{i} ',end='')


    

