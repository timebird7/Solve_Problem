def findside(nums):
    sidelist = [0,0,0,0]
    for i in range(len(nums)):
        if nums.count(nums[i]) % 2:
            if i % 2:
                sidelist[3] = nums[i]
                sidelist[2] = nums[i-1]                
            else :
                sidelist[0] = nums[i]
                sidelist[1] = nums[i+1]                
    return sidelist

def rmvpipe(a,b,nums):    
    for i in range(0,len(nums),2):
        if nums[i] == a and nums[i+1] == b:
            nums[i] = 0
            nums[i+1] = 0
    return nums

TC = int(input())
sidelist = []

for i in range(TC):
    n = int(input())
    nums = list(map(int,list(input().split())))
    result = []
    resultstr = ''

    sidelist = findside(nums)

    nums = rmvpipe(sidelist[0],sidelist[1],nums)
    nums = rmvpipe(sidelist[2],sidelist[3],nums)    

    result.append(sidelist[0])
    result.append(sidelist[1])   

    while sum(nums):
        for j in range(0,len(nums),2):
            if result[-1] == nums[j]:
                result.append(nums[j])
                result.append(nums[j+1])
                nums = rmvpipe(nums[j], nums[j+1],nums)
                break        

    result.append(sidelist[2])
    result.append(sidelist[3])    

    for j in result[:-1]:
        resultstr += str(j) + ' '
    else:
        resultstr += str(result[-1])

    print(f'#{i+1} {resultstr}')
        
