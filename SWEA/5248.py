def makeset(x):
    team[x] = x

def find_set(x):
    if x == team[x]:
        return x
    else:
        return find_set(team[x])

def union(x,y):
    re = find_set(y)
    for t in range(len(team)):
        if team[t] == re:
            team[t] = find_set(x)

TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    team = [0] * N

    for i in range(N):
        makeset(i)

    for j in range(len(nums)//2):
        union(nums[2*j]-1, nums[2*j+1]-1)
        
    print(f'#{tc} {len(set(team))}')

