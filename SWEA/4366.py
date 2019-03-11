import copy

def ttoi(n):
    tn = list(reversed(list(n)))    
    tnum = 0
    for i in range(len(tn)):
        tnum += int(tn[i])*(3**i)
    return tnum

def btoi(n):
    bn = list(reversed(list(n)))
    bnum = 0
    for i in range(len(bn)):
        bnum += int(bn[i])*(2**i)
    return bnum

TC = int(input())

for tc in range(TC):
    bnum = list(input())
    tnum = list(input())

    result = []

    for i in range(len(tnum)):
        tmp = copy.copy(tnum)
        if tnum[i] == '2':
            tmp[i] = '1'
            result.append(ttoi(''.join(tmp)))
            tmp[i] = '0'
            result.append(ttoi(''.join(tmp)))
        elif tnum[i] == '1':
            tmp[i] = '2'
            result.append(ttoi(''.join(tmp)))
            tmp[i] = '0'
            result.append(ttoi(''.join(tmp)))
        elif tnum[i] == '0':
            tmp[i] = '2'
            result.append(ttoi(''.join(tmp)))
            tmp[i] = '1'
            result.append(ttoi(''.join(tmp)))
        
    for i in range(len(bnum)):
        tmp = copy.copy(bnum)
        if bnum[i] == '1':
            tmp[i] = '0'
            x = btoi(''.join(tmp))
            if x in result:
                ans = x
                break
        elif bnum[i] == '0':
            tmp[i] = '1'
            x = btoi(''.join(tmp))
            if x in result:
                ans = x
                break

    print(f'#{tc+1} {ans}')


            








    
    

    

    




