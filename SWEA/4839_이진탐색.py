TC = int(input())

for i in range(TC):
    P, A, B = list(map(int,list(input().split())))
    l = 1
    r = P
    mid = 0
    cnta = 0    

    while A != mid:
        cnta += 1
        mid = (l+r)//2
        if mid < A:
            l = mid
        else :
            r = mid

    l = 1
    r = P
    mid = 0
    cntb = 0

    while B != mid:
        cntb += 1
        mid = (l+r)//2
        if mid < B:
            l = mid
        else :
            r = mid

    
    if cnta < cntb:
        result = 'A'
    elif cntb < cnta:
        result = 'B'
    else :
        result = 0

    print(f'#{i+1} {result}')



        
        




