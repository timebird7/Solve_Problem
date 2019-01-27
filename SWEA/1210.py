def findtwo(nums):
    for i in range(1,101):
        if nums[99][i] == 2:
            return i


for i in range(10):
    n = int(input())
    start = 0
    
    m = 99
    nums = [[0 for x in range(102)] for y in range(100)]

    for j in range(100):
        nums[j][1:101] = list(map(int, list(input().split())))

    start = findtwo(nums)

    while m > 0:
        
        if nums[m][start-1]:
            while nums[m][start-1]:
                start -= 1
            m -= 1
            continue
        
        elif nums[m][start+1]:
            while nums[m][start+1]:
                start += 1
            m -= 1
            continue
            
        else :
            m -= 1
        
    print(f'#{n} {start-1}')
