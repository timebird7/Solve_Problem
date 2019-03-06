N = int(input())

nums = [[0 for i in range(102)] for j in range(102)]

for i in range(1,N+1):
    tmp = list(map(int,input().split()))

    for x in range(tmp[0],tmp[0]+tmp[2]):
        for y in range(tmp[1],tmp[1]+tmp[3]):
            nums[x][y] = i

for i in range(1,N+1):
    cnt = 0
    for x in range(102):
        for y in range(102):
            if nums[x][y] == i:
                cnt += 1

    print(cnt)