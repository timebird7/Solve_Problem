TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    cnt = 0

    queue = set()
    queue.add(M)
    visited = [0] * 1000001

    while True:
        cnt += 1
        tmp = set()
        for q in queue:
            if q+1 <= 1000000 and visited[q+1] == 0:
                tmp.add(q+1)
                visited[q+1] = 1
            if q-1 <= 1000000 and visited[q-1] == 0:
                tmp.add(q-1)
                visited[q-1] = 1
            if q%2 == 0 and q//2 <= 1000000 and visited[q//2] == 0:
                tmp.add(q//2)
                visited[q//2] = 1
            if q+10 <= 1000000 and visited[q+10] == 0:
                tmp.add(q+10)
                visited[q+10] = 1        

        if N in tmp:
            break
        else:
            queue = tmp

    print(f'#{tc} {cnt}')


