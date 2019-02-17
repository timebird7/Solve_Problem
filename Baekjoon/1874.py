nums = []
ans = []
pnt = 1
result = 1
n = int(input())

for i in range(n):
    num = int(input())

    while pnt <= num:            
        nums.append(pnt)      
        ans.append('+')      
        pnt += 1

    if nums[-1] == num:
        nums.pop()              
        ans.append('-')      
    else:
        result = 0         
 
if result == 0:
    print('NO')
else:
    for c in ans:
        print(c)


