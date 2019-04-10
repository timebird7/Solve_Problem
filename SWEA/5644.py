TC = int(input())

for tc in range(1,TC+1):
    M,A = map(int, input().split())
    a_move = list(map(int,input().split()))
    b_move = list(map(int,input().split()))
    aps = [0]*A

    for a in range(A):
        aps[a] = list(map(int,input().split()))

    a = [1,1]
    b = [10,10]
    result = 0
    a_can = []
    b_can = []
    tmp = [0]

    for i in range(A):
        if abs(aps[i][0] - a[0]) + abs(aps[i][1] - a[1]) <= aps[i][2]:
            a_can.append(i)
        if abs(aps[i][0] - b[0]) + abs(aps[i][1] - b[1]) <= aps[i][2]:
            b_can.append(i)

    if a_can and b_can:
        for x in a_can:
            for y in b_can:
                if x == y:
                    tmp.append(aps[x][3])
                else:
                    tmp.append(aps[x][3]+aps[y][3])
    elif a_can:
        for x in a_can:
            tmp.append(aps[x][3])
    elif b_can:
        for x in b_can:
            tmp.append(aps[x][3])

    result += max(tmp)

    for m in range(M):
        if a_move[m] == 0:
            pass
        elif a_move[m] == 1:
            a[1] -= 1
        elif a_move[m] == 2:
            a[0] += 1
        elif a_move[m] == 3:
            a[1] += 1
        elif a_move[m] == 4:
            a[0] -= 1
        if b_move[m] == 0:
            pass
        elif b_move[m] == 1:
            b[1] -= 1
        elif b_move[m] == 2:
            b[0] += 1
        elif b_move[m] == 3:
            b[1] += 1
        elif b_move[m] == 4:
            b[0] -= 1

        ############################
        a_can = []
        b_can = []
        tmp = [0]

        for i in range(A):
            if abs(aps[i][0] - a[0]) + abs(aps[i][1] - a[1]) <= aps[i][2]:
                a_can.append(i)
            if abs(aps[i][0] - b[0]) + abs(aps[i][1] - b[1]) <= aps[i][2]:
                b_can.append(i)

        if a_can and b_can:
            for x in a_can:
                for y in b_can:
                    if x == y:
                        tmp.append(aps[x][3])
                    else:
                        tmp.append(aps[x][3]+aps[y][3])
        elif a_can:
            for x in a_can:
                tmp.append(aps[x][3])
        elif b_can:
            for x in b_can:
                tmp.append(aps[x][3])

        result += max(tmp)

    print(f'#{tc} {result}')
