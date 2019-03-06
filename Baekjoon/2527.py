for tc in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = list(map(int,input().split()))
    if x1 == p2 and q1 == y2:
        print('c')
    elif x1 == p2 and y1 == q2:
        print('c')
    elif p1 == x2 and q1 == y2:
        print('c')
    elif p1 == x2 and y1 == q2:
        print('c')
    elif x1 == p2:
        print('b')
    elif q1 == y2:
        print('b')
    elif y1 == q2:
        print('b')
    elif p1 == x2:
        print('b')
    elif p1 < x2 or p2 < x1:
        print('d')
    elif y2 > q1 or q2 < y1:
        print('d')
    else:
        print('a')