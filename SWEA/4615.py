def checkb(i,j):
    global board
    global N
    tm = []
    for k in range(i-1,-1,-1):
        if board[k][j] == 'W':
            tm.append([k,j])
            continue
        elif board[k][j] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(j-1,-1,-1):
        if board[i][k] == 'W':
            tm.append([i,k])
            continue
        elif board[i][k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(i+1,N):
        if board[k][j] == 'W':
            tm.append([k, j])
            continue
        elif board[k][j] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(j+1,N):
        if board[i][k] == 'W':
            tm.append([i, k])
            continue
        elif board[i][k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(1,N):
        if i-k>=0 and j-k>=0 and board[i-k][j-k] == 'W':
            tm.append([i-k,j-k])
            continue
        elif i-k>=0 and j-k>=0 and board[i-k][j-k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(1,N):
        if i-k>=0 and j+k<N and board[i-k][j+k] == 'W':
            tm.append([i-k,j+k])
            continue
        elif i-k>=0 and j+k<N and board[i-k][j+k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(1,N):
        if i+k<N and j-k>=0 and board[i+k][j-k] == 'W':
            tm.append([i+k,j-k])
            continue
        elif i+k<N and j-k>=0 and board[i+k][j-k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break

    tm = []
    for k in range(1,N):
        if i+k<N and j+k<N and board[i+k][j+k] == 'W':
            tm.append([i+k,j+k])
            continue
        elif i+k<N and j+k<N and board[i+k][j+k] == 'B':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'B'
            break
        break


def checkw(i, j):
    global board
    global N
    tm = []
    for k in range(i - 1, -1, -1):
        if board[k][j] == 'B':
            tm.append([k, j])
            continue
        elif board[k][j] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(j - 1, -1, -1):
        if board[i][k] == 'B':
            tm.append([i, k])
            continue
        elif board[i][k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(i + 1, N):
        if board[k][j] == 'B':
            tm.append([k, j])
            continue
        elif board[k][j] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(j + 1, N):
        if board[i][k] == 'B':
            tm.append([i, k])
            continue
        elif board[i][k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(1, N):
        if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 'B':
            tm.append([i - k, j - k])
            continue
        elif i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(1, N):
        if i - k >= 0 and j + k < N and board[i - k][j + k] == 'B':
            tm.append([i - k, j + k])
            continue
        elif i - k >= 0 and j + k < N and board[i - k][j + k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break

    tm = []
    for k in range(1, N):
        if i + k < N and j - k >= 0 and board[i + k][j - k] == 'B':
            tm.append([i + k, j - k])
            continue
        elif i + k < N and j - k >= 0 and board[i + k][j - k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break

        break

    tm = []
    for k in range(1, N):
        if i + k < N and j + k < N and board[i + k][j + k] == 'B':
            tm.append([i + k, j + k])
            continue
        elif i + k < N and j + k < N and board[i + k][j + k] == 'W':
            if tm:
                for t in tm:
                    board[t[0]][t[1]] = 'W'
            break
        break



TC = int(input())

for tc in range(TC):
    N, M = list(map(int,input().split()))
    bcnt = 0
    wcnt = 0
    board = [[0 for i in range(N)] for j in range(N)]
    board[N//2-1][N//2-1] = 'W'
    board[N//2][N//2] = 'W'
    board[N//2][N//2-1] = 'B'
    board[N//2-1][N//2] = 'B'

    for m in range(M):
        tmp = list(map(int,input().split()))
        if m+4+1 > N*N:
            break

        if tmp[2] == 1:
            board[tmp[1]-1][tmp[0]-1] = 'B'
            checkb(tmp[1]-1,tmp[0]-1)

        elif tmp[2] == 2:
            board[tmp[1] - 1][tmp[0] - 1] = 'W'
            checkw(tmp[1] - 1, tmp[0] - 1)

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                bcnt += 1
            elif board[i][j] == 'W':
                wcnt += 1

    print('#{} {} {}'.format(tc+1,bcnt,wcnt))