TC = int(input())

for tc in range(TC):
    N,M,L = list(map(int,input().split()))
    tree = [0 for i in range(N+1)]

    for m in range(M):
        tmp = list(map(int,input().split()))
        tree[tmp[0]] = tmp[1]

    for i in range(N,0,-1):
        if tree[i] == 0:
            try:
                tree[i] = tree[i*2] + tree[i*2+1]
            except IndexError:
                tree[i] = tree[i*2]


    print(f'#{tc+1} {tree[L]}')