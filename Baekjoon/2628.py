tmp = list(map(int,input().split()))

hor = [1 for i in range(tmp[0])]
ver = [1 for i in range(tmp[1])]

horcut = [0]
vercut = [0]

T = int(input())
if T != 0:
    for t in range(T):
        x, y = list(map(int,input().split()))
        if x:
            horcut.append(y)
        else:
            vercut.append(y)

    horcut.sort()
    vercut.sort()

    hmax = 0
    vmax = 0
    if len(horcut) > 1:
        for i in range(len(horcut)-1):
            if len(hor[horcut[i]:horcut[i+1]]) > hmax:
                hmax = len(hor[horcut[i]:horcut[i+1]])
        else:
            if len(hor[horcut[i+1]:]) > hmax:
                hmax = len(hor[horcut[i+1]:])
    else:
        hmax = tmp[0]

    if len(vercut) > 1:

        for i in range(len(vercut)-1):
            if len(ver[vercut[i]:vercut[i+1]]) > vmax:
                vmax = len(ver[vercut[i]:vercut[i+1]])
        else:
            if len(ver[vercut[i+1]:]) > vmax:
                vmax = len(ver[vercut[i+1]:])
    else:
        vmax = tmp[1]

    print(hmax*vmax)
else:
    print(tmp[0]*tmp[1])
