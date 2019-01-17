T = int(input())

for x in range(T):
    k = int(input())
    nums = list(map(int,list(input().split())))    
    print(f'#{x+1} {max(nums)-min(nums)}')