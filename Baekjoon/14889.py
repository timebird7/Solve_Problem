from itertools import combinations

N = int(input())
nums = [[1 for i in range(N)] for j in range(N)]

for n in range(N):
    nums[n] = list(map(int,input().split()))

mem = [i for i in range(N)]
result = 10000
starts = list(combinations(mem, N//2))

for start in starts:
    link = []
    statstart = 0
    statlink = 0
    for i in range(N):
        if i not in start:
            link.append(i)

    for i in start:
        for j in start:
            statstart += nums[i][j]

    for i in link:
        for j in link:
            statlink += nums[i][j]

    result = min(result, abs(statstart-statlink))

    if result == 0:
        break

print(result)


