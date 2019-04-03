TC = int(input())

for tc in range(1,TC+1):
    price = list(map(int,input().split()))
    days = list(map(int,input().split()))
    result = [0]
    result_ = [0]
    flag = 0

    
    for day in days:
        tmp = []        
        flag -= 1
        if day:
            p1 = price[0] * day
            p2 = price[1]
            if flag <= 0:
                for r in result_:
                    tmp.append(r+price[2])
                print(tmp)
                result_ = result[:]
                flag = 3
                
        
            for r in result:
                tmp.append(r+p1)
                tmp.append(r+p2)
            
            

            result = tmp[:]

    result.append(price[3])

    print(min(result))
            