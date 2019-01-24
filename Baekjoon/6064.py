TC = int(input())

for i in range(TC):
    M, N, x, y = list(map(int,list(input().split())))

    if M == x:
        x = 0
    if N == y:
        y = 0

    for j in range(x, M*N, M):
        if j%N == y:
            print(j)
            break
    else:
        print(-1)

        