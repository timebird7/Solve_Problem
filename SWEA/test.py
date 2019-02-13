class my_list(list):
    def get(self, i):
        try:
            return self[i]
        except IndexError:
            return False


def findtwo(nums):
    for i in range(100):
        if nums[99][i] == 2:
            return i


for i in range(10):
    n = int(input())
    start = 0
    
    m = 99
    nums = [[0 for x in range(100)] for y in range(100)]

    for j in range(100):
        nums[j] = my_list(map(int, input().split()))

    start = findtwo(nums)

    while m > 0:
        
        if nums[m].get(start-1):
            while nums[m].get(start-1):
                start -= 1
            m -= 1
            continue
        
        elif nums[m].get(start+1):
            while nums[m].get(start+1):
                start += 1
            m -= 1
            continue
            
        else :
            m -= 1
        
    print(f'#{n} {start}')
