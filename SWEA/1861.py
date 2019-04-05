def cango(i,j,ni,nj):
    global N
    if ni<0 or ni>N-1 or nj<0 or nj>N-1:
        return False    
    if nums[ni][nj] - nums[i][j] == 1:
        return True
    return False

TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    nums = [0]*N

    for n in range(N):
        nums[n] = list(map(int,input().split()))

    results = []
    result = 0

    for i in range(N):
        for j in range(N):
            start = (i,j)
            cnt = 0        

            while True:
                cnt += 1
                flag = 1
                x,y = start

                if cango(x,y,x-1,y):
                    start = (x-1,y)
                    flag = 0
                    continue
                if cango(x,y,x+1,y):
                    start = (x+1,y)
                    flag = 0
                    continue
                if cango(x,y,x,y-1):
                    start = (x,y-1)
                    flag = 0
                    continue
                if cango(x,y,x,y+1):
                    start = (x,y+1)
                    flag = 0
                    continue
                
                if cnt > result:
                    result = cnt
                    results = nums[i][j]
                elif cnt == result:
                    results = min(results,nums[i][j])
                break

    print(f'#{tc} {results} {result}')

    