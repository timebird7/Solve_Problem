dx = [0,1,0,-1]
dy = [1,0,-1,0]


def dfs(i,j,result):
    global results, nums
    if len(result) == 7:
        results.add(result)
        return

    else:
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]

            if 0<=x<4 and 0<=y<4:
                dfs(x,y,result+nums[x][y])

TC = int(input())

for tc in range(1,TC+1):
    nums = [input().split() for i in range(4)]
    results = set()

    for i in range(4):
        for j in range(4):
            dfs(i,j,'')

    print(f'#{tc} {len(results)}')