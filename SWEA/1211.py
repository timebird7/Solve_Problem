def findstart(nums):
    startlist = []
    for i in range(1,101):
        if nums[99][i]:
            startlist.append(i)
    return startlist
        
def findans(endlist, cntlist):
    anslist = []
    for i in range(len(cntlist)):
        if cntlist[i] == min(cntlist):
            anslist.append(endlist[i])
    return max(anslist)

for i in range(10):
    n = int(input())
       
    
    nums = [[0 for x in range(102)] for y in range(100)]
    startlist = []
    cntlist = []
    endlist = []
    ans = 0

    for j in range(100):
        nums[j][1:101] = list(map(int, list(input().split())))

    startlist = findstart(nums)

    for start in startlist:
        cnt = 0
        m = 99

        while m > 0:
            
            if nums[m][start-1]:
                while nums[m][start-1]:
                    start -= 1
                    cnt += 1
                m -= 1
                cnt += 1
                continue
            
            elif nums[m][start+1]:
                while nums[m][start+1]:
                    start += 1
                    cnt += 1
                m -= 1
                cnt += 1
                continue
                
            else :
                m -= 1
                cnt += 1

        endlist.append(start-1)
        cntlist.append(cnt)

        
    ans = findans(endlist, cntlist)
    print(f'#{n} {ans}')