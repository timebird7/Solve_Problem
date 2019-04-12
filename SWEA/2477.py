TC = int(input())

for tc in range(1,TC+1):
    N,M,K,A,B = map(int,input().split())
    js = [[0,-1,0,i] for i in range(N)]
    jb = [[0,-1,0,i] for i in range(M)]
    js_time = list(map(int,input().split()))
    jb_time = list(map(int,input().split()))

    for n in range(N):
        js[n][0] = js_time[n]
    for m in range(M):
        jb[m][0] = jb_time[m]

    people = [[0,-1,-1,i] for i in range(K)]
    arrival_time = list(map(int,input().split()))

    for k in range(K):
        people[k][0] = arrival_time[k]

    t = 0
    flag = 0
    js_queue = []
    jb_queue = []
    ans = 0

    while True:
        for s in js:
            if s[1] >= 0:
                s[2] -= 1
        for b in jb:
            if b[1] >= 0:
                b[2] -= 1

        for person in people:
            if person[0] == t:
                js_queue.append(person)
        for s in js:
            if s[1]>=0 and s[2] == 0:
                jb_queue.append(people[s[1]])
                s[1] = -1
                s[2] = 0
        for b in jb:
            if b[1]>=0 and b[2] == 0:
                b[1] = -1
                b[2] = 0

        
        for s in js:
            if s[1] == -1 and js_queue:
                tmp = js_queue.pop(0)
                tmp[1] = s[3]
                s[1] = tmp[3]
                s[2] = s[0]
                people[tmp[3]] = tmp
        for b in jb:
            if b[1] == -1 and jb_queue:
                tmp = jb_queue.pop(0)
                tmp[2] = b[3]
                b[1] = tmp[3]
                b[2] = b[0]
                people[tmp[3]] = tmp

        for person in people:
            if person[1]==-1 or person[2]==-1:
                break
        else:
            flag = 1

        if flag:
            break

        t += 1
    
    for person in people:
        if person[1] == A-1 and person[2] == B-1:
            ans += person[3]+1

    if ans == 0:
        ans = -1

    print(f'#{tc} {ans}')


