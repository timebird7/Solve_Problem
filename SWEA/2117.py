def findarea(i,j,k):
    global N, nums
    cnt = 0
    for x in range(N):
        for y in range(N):
            if abs(i-x)+abs(j-y) <= k-1:
                if nums[x][y]:
                    cnt += 1

    return cnt 

TC = int(input())

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    nums = [0] * N
    result = 0
    allhome = 0

    for n in range(N):
        nums[n] = list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            if nums[i][j]:
                allhome += 1

    for i in range(N):
        for j in range(N):
            k = 1
            while True:
                home = findarea(i,j,k)
                price = k*k+(k-1)*(k-1)
                if M*home >= price:
                    result = max(result,home)

                if home == allhome:
                    break

                k += 1
    
    print(f'#{tc} {result}')
