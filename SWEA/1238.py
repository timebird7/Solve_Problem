for tc in range(10):
    n, start = list(map(int, input().split()))
 
    graph = list(map(int, input().split()))
 
    visited = [0 for i in range(n+1)]
    queue = [[start]]
    visited[start] = 1
 
    while queue[-1]:
        tmp = []
        for q in queue[-1]:  
            for i in range(0,len(graph),2):
                if graph[i] == q and visited[graph[i+1]] == 0:
                    visited[graph[i+1]] = 1
                    tmp.append(graph[i+1])
 
        queue.append(tmp)
 
    print(f'#{tc+1} {max(queue[-2])}')