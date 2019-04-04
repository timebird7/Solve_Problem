def dfs(month, money):
    global days, price, result
    if month > 12:
        result.add(money)
        return

    dfs(month+1, money+days[month-1]*price[0])
    dfs(month+1, money+price[1])
    dfs(month+3, money+price[2])

TC = int(input())

for tc in range(1,TC+1):
    price = list(map(int,input().split()))
    days = list(map(int,input().split()))
    result = set()

    dfs(1,0)

    result.add(price[3])    

    print(f'#{tc} {min(result)}')

    