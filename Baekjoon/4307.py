TC = int(input())

for tc in range(TC):
    L, N = list(map(int,input().split()))

    ants = [0 for n in range(N)]

    for n in range(N):
        ants[n] = int(input())

    result1 = 0
    result2 = 0

    for ant in ants:
        result1 = max(result1, min(ant, L-ant))
        result2 = max(result2, max(ant, L-ant))

    print(f'{result1} {result2}')

