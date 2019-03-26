N, K = map(int, input().split())

coins = [0 for n in range(N)]
cnt = 0

for n in range(N-1,-1,-1):
    coins[n] = int(input())

for coin in coins:
    while K >= coin:
        K -= coin
        cnt += 1

    if K == 0:
        break

print(cnt)

