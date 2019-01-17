T = int(input())

for x in range(T):
    a, b = list(map(int,list(input().split())))
    nums = list(map(int,list(input().split())))        
    k = a - b + 1    
    result = []
    m = 0
    n = b
    
    for y in range(k):        
        result.append(sum(nums[m:n]))
        m += 1
        n += 1
    
    print(f'#{x+1} {max(result) - min(result)}')