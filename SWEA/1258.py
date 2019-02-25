def solve(n):
    global nums
    global matrix
    for i in range(n):
        for j in range(n):
            if nums[i][j] != 0:
                tmp = [0,0,0,0]
                mtrx = [0,0,0]
                tmp[0] = i
                tmp[2] = i
                tmp[1] = j
                tmp[3] = j
                xcnt = 1
                ycnt = 1
                while tmp[2]<n-1 and nums[tmp[2]+1][tmp[3]]:
                    tmp[2] += 1
                    xcnt += 1
                while tmp[3]<n-1 and nums[tmp[2]][tmp[3]+1]:
                    tmp[3] += 1
                    ycnt += 1
 
                mtrx[0] = tmp[2] - tmp[0] + 1
                mtrx[1] = tmp[3] - tmp[1] + 1
                mtrx[2] = xcnt*ycnt
 
                makezero(tmp)
                matrix.append(mtrx)                
 
def makezero(tmp):
    global nums
    for i in range(tmp[0], tmp[2] + 1):
        for j in range(tmp[1], tmp[3] + 1):
            nums[i][j] = 0
 
TC = int(input())
 
for tc in range(TC):
    n = int(input())
    nums = [[] for i in range(n)]
    matrix = []
 
    for i in range(n):
        nums[i] = list(map(int, input().split()))    
 
    solve(n)
 
    matrix.sort(key=lambda mtrx: mtrx[0])
    matrix.sort(key=lambda mtrx: mtrx[2])
 
    a = len(matrix)
    ans = ''
 
    for m in matrix:
        ans += ' ' + str(m[0]) + ' ' + str(m[1])
 
    print(f'#{tc+1} {a}{ans}')