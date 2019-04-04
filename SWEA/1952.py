from copy import copy

TC = int(input())

for tc in range(1,TC+1):
    price = list(map(int,input().split()))
    days = list(map(int,input().split()))
    result = set()
    result.add(0)
    result_ = set()
    result_.add(0)
    flag = 0
    i = 0

    while True:    
        tmp = set()
        tmp_ = set()        
        flag -= 1
        if days[i]:            
            if flag <= 0:                
                for r in result:
                    tmp_.add(r+price[2])
                flag = 3
                result_ = copy(tmp_)

            for r in result:
                
                tmp.add(r+price[0] * days[i])
                tmp.add(r+price[1])
            result = copy(tmp)
            print(result)
            print(result_)

        if flag == 1:
            result = result.union(result_)


        i += 1

        if i == 12:
            if flag <= 0:
                result = result.union(result_)
            break

    result.add(price[3])    

    print(f'#{tc} {min(result)}')
            