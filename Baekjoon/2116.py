import copy

dice = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0
}

N = int(input())
dices = [list(map(int,input().split())) for i in range(N)]
ans = []

for i in range(6):
    r = 0
    tmp = copy.deepcopy(dices)
    bot = tmp[0][i]
    top = tmp[0][dice[i]]   
    for j in range(N):
        
        botidx = tmp[j].index(bot)
        tmp[j].pop(botidx)
        topidx = tmp[j].index(top)
        tmp[j].pop(topidx)

        try:
            bot = top
            botidx = tmp[j+1].index(bot)
            top = tmp[j+1][dice[botidx]]
        except IndexError:
            break

    for t in tmp:
        r += max(t)
    else:
        ans.append(r)

print(max(ans))


