TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N < M:
        result = []
        for i in range(M-N+1):
            r = 0
            for j in range(N):
                r += A[j]*B[i+j]
            else:
                result.append(r)

    elif N > M:
        result = []
        for i in range(N - M + 1):
            r = 0
            for j in range(M):
                r += A[i+j] * B[j]
            else:
                result.append(r)

    else:
        r = 0
        for i in range(N):
            r += A[i] * B[i]
        else:
            result.append(r)

    print('#{} {}'.format(tc+1, max(result)))