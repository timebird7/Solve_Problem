def testup(road,start,end,n):
    global visited
    if start < 0:
        return False
    for r in range(start,end):
        if road[r] != n or r in visited:
            return False
        visited.append(r)
    return True

def testdown(road,start,end,n):
    global N
    global visited
    if end > N:
        return False
    for r in range(start,end):
        if road[r] != n or r in visited:
            return False
        visited.append(r)
    return True

def test(road,X):
    global N

    for i in range(N-1):
        if road[i+1] == road[i]:
            continue
        elif road[i+1]-1 == road[i]:
            if testup(road,i-X+1,i+1,road[i]):
                continue
            else:
                return False
        elif road[i+1]+1 == road[i]:
            if testdown(road,i+1,i+X+1,road[i+1]):
                continue
            else:
                return False
        else:
            return False

    return True


N,X = map(int,input().split())

nums = [0]*N
cnt = 0


for n in range(N):
    nums[n] = list(map(int,input().split()))
    visited = []
    if test(nums[n],X):
        cnt += 1

for j in range(N):
    tmp = []
    for i in range(N):
        tmp.append(nums[i][j])
    visited = []
    if test(tmp,X):
        cnt += 1

print(cnt)


