def push(S):
    global N
    global nums
    if S == 'up':
        for i in range(N):
            for j in range(N):
                x = i
                y = j
                while x>0:  
                    if nums[x-1][y] == 0:
                        nums[x-1][y] = nums[x][y]
                        nums[x][y] = 0
                        x -= 1
                        continue
                    elif nums[x-1][y] == nums[x][y]:
                        nums[x-1][y] = nums[x][y]*2
                        nums[x-1][y] = str(nums[x-1][y])
                        nums[x][y] = 0
                        x -= 1
                        break    
                    break

                while x>0:  
                    if nums[x-1][y] == 0:
                        nums[x-1][y] = nums[x][y]
                        nums[x][y] = 0
                        x -= 1
                        continue
                    break
 
    if S == 'down':
        for i in range(N-1,-1,-1):
            for j in range(N):
                x = i
                y = j
                while x<N-1:  
                    if nums[x+1][y] == 0:
                        nums[x+1][y] = nums[x][y]
                        nums[x][y] = 0
                        x += 1
                        continue
                    elif nums[x+1][y] == nums[x][y]:
                        nums[x+1][y] = nums[x][y]*2
                        nums[x+1][y] = str(nums[x+1][y])
                        nums[x][y] = 0
                        x += 1
                        break    
                    break

                while x<N-1:  
                    if nums[x+1][y] == 0:
                        nums[x+1][y] = nums[x][y]
                        nums[x][y] = 0
                        x += 1
                        continue
                    break
 
    if S == 'left':
        for i in range(N):
            for j in range(N):
                x = i
                y = j
                while y>0:  
                    if nums[x][y-1] == 0:
                        nums[x][y-1] = nums[x][y]
                        nums[x][y] = 0
                        y -= 1
                        continue
                    elif nums[x][y-1] == nums[x][y]:
                        nums[x][y-1] = nums[x][y]*2
                        nums[x][y-1] = str(nums[x][y-1])
                        nums[x][y] = 0
                        y -= 1
                        break    
                    break

                while y>0:  
                    if nums[x][y-1] == 0:
                        nums[x][y-1] = nums[x][y]
                        nums[x][y] = 0
                        y -= 1
                        continue
                    break
 
    if S == 'right':
        for i in range(N):
            for j in range(N-1,-1,-1):
                x = i
                y = j
                while y<N-1:  
                    if nums[x][y+1] == 0:
                        nums[x][y+1] = nums[x][y]
                        nums[x][y] = 0
                        y += 1
                        continue
                    elif nums[x][y+1] == nums[x][y]:
                        nums[x][y+1] = nums[x][y]*2
                        nums[x][y+1] = str(nums[x][y+1])
                        nums[x][y] = 0
                        y += 1
                        break    
                    break

                while y<N-1:  
                    if nums[x][y+1] == 0:
                        nums[x][y+1] = nums[x][y]
                        nums[x][y] = 0
                        y += 1
                        continue
                    break
                 
 
TC = int(input())
 
for tc in range(TC):
    N, S = input().split()
    N = int(N)
 
    nums = [[] for i in range(N)]
 
    for i in range(N):
        nums[i] = list(map(int,input().split()))
 
    push(S)
 
    print(f'#{tc+1}')
 
    for num in nums:
        for n in num:
            print(f'{n}',end=' ')
        print()