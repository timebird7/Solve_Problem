dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def isarr(p, q):
    if 0 <= p < N and 0 <= q < N:
        return True
    else:
        return False


TC = int(input())

for tc in range(TC):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    sx, sy, ex, ey = 0, 0, N-1, N-1
    route, fuel = 0, 0
    queue = []
    results = 99999999
    queue.append([sx, sy, route, fuel])

    while queue:
        x, y, r, f = queue.pop(0)
        visited[x][y] = 1
        if x == ex and y == ey:
            if results > r + f:
                results = r + f

        r += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isarr(nx, ny) and not visited[nx][ny]:
                if arr[nx][ny] > arr[x][y]:
                    queue.append([nx, ny, r, f + arr[nx][ny] - arr[x][y]])
                else:
                    queue.append([nx, ny, r, f])

    #print(results)
    print("#{} {}".format(tc+1, results))