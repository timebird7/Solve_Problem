TC = int(input())

for tc in range(TC):
    V, E = list(map(int,input().split()))
    ways = []
    for e in range(E):
        way = list(map(int,input().split()))
        ways.append(way)
        way_ = [way[1],way[0]]
        ways.append(way_)
    S, G = list(map(int,input().split()))

    visited = [0 for i in range(V+1)]
    queue = [S]
    cnt = 0
    tmp = []
    eflag = 0

    while True:
        for way in ways:
            if way[0] == queue[0] and visited[way[1]] == 0:
                tmp.append(way[1])

        visited[queue[0]] = 1
        queue.pop(0)

        if not queue:
            if tmp:
                queue = tmp
                cnt += 1
                tmp = []
            else:
                eflag = 1
                break

        if G in queue:
            break

    if eflag:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {cnt}')

    


