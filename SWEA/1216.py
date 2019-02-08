for tc in range(10):    
    a = int(input())
    strlist = [[] for x in range(100)]

    for i in range(100):
        strlist[i] = list(input())
    result = 0
    result1 = 0
    result2 = 0

    for s in strlist:        
        for M in range(100,1,-1):
            if result1 > M:
                break        
            for i in range(100-M+1):                
                cnt = 0
                j = 0
                while s[i+j] == s[i+M-j-1] :
                    cnt += 1
                    j += 1
                    if cnt >= (M//2) + 1:
                        if result1 < M:
                            result1 = M
                        break

    for x in range(100):
        for y in range(100):
            if x < y:
                strlist[x][y], strlist[y][x] = strlist[y][x], strlist[x][y]

    for s in strlist:        
        for M in range(100,1,-1):
            if result2 > M:
                break                       
            for i in range(100-M+1):                
                cnt = 0
                j = 0
                while s[i+j] == s[i+M-j-1] :
                    cnt += 1
                    j += 1
                    if cnt >= (M//2) + 1:
                        if result2 < M:
                            result2 = M
                        break
                    
    if result1 >= result2 :
        result = result1
    else :
        result = result2
                 

    print(f'#{a} {result}')