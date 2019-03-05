TC = int(input())

for tc in range(TC):
    N = int(input())
    heap = [0]+list(map(int,input().split()))
    ans = 0

    for i in range(1,N+1):
        tmp = i
        while heap[tmp//2] > heap[tmp]:
            heap[tmp//2], heap[tmp] = heap[tmp], heap[tmp//2]
            tmp//=2

    tmp = N
    while heap[tmp]:
        tmp//=2
        ans+=heap[tmp]

    print(f'#{tc+1} {ans}')


