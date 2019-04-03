import copy

for tc in range(1, int(input()) + 1):
    i = input().split()
    k = int(i[1])
    n = len(i[0])
    queue = [list(i[0])]
    cnt = 0
    result = set()
    while True:
        cnt += 1
        tmp = []

        for q in queue:
            for x in range(n):
                for y in range(x+1,n):
                    a = copy.copy(q)
                    a[x], a[y] = a[y], a[x]
                    if a[:] not in tmp:
                        tmp.append(a[:])

        queue = copy.copy(tmp)

        if cnt == int(i[1]):
            break

    for q in queue:
        result.add(int(''.join(q)))
        
    print('#{} {}'.format(tc, max(result)))

