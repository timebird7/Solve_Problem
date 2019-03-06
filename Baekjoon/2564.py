W, H = list(map(int,input().split()))
N = int(input())
stores = []
for n in range(N):
    stores.append(list(map(int,input().split())))

loc = list(map(int,input().split()))
result = 0
for store in stores:
    if store[0] == loc[0]:
        ans = abs(store[1]-loc[1])
    elif store[0] == 1 and loc[0] == 2:
        ans = H
        ans += min(store[1] + loc[1],W-store[1]+W-loc[1])
    elif store[0] == 2 and loc[0] == 1:
        ans = H
        ans += min(store[1] + loc[1],W-store[1]+W-loc[1])
    elif store[0] == 3 and loc[0] == 4:
        ans = W
        ans += min(store[1]+loc[1],H-store[1]+H-loc[1])
    elif store[0] == 4 and loc[0] == 3:
        ans = W
        ans += min(store[1] + loc[1], H - store[1] + H - loc[1])
    elif store[0] == 1 and loc[0] == 3:
        ans = store[1] + loc[1]
    elif store[0] == 1 and loc[0] == 4:
        ans = W-store[1]+loc[1]
    elif store[0] == 2 and loc[0] == 3:
        ans = store[1]+H-loc[1]
    elif store[0] == 2 and loc[0] == 4:
        ans = W-store[1]+H-loc[1]
    elif store[0] == 3 and loc[0] == 1:
        ans = store[1]+loc[1]
    elif store[0] == 3 and loc[0] == 2:
        ans = H-store[1]+loc[1]
    elif store[0] == 4 and loc[0] == 1:
        ans = store[1]+W-loc[1]
    elif store[0] == 4 and loc[0] == 2:
        ans = H-store[1]+W-loc[1]

    result += ans
print(result)
